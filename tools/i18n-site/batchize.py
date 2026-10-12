# -*- coding: utf-8 -*-
"""Cut the untranslated segments of a language into slices for the translator agents.

    python batchize.py <lang> [--words 1100] [--items 70]

A slice follows the site's reading order and never crosses a page unless a page is small; a long chapter is cut
into several slices. Segments the lock table settles, segments with no letters, and segments the memory already
holds are left out. Writes WORK/<lang>/slices/<lang>__bNNN.json and WORK/<lang>/manifest.json.
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, MEMORY, LANGS
from extract import TOKEN

FIXED = re.compile(r"^(?:[\W\d_]*|G|X|---|— G|@\S+|\S+@\S+|(?:https?://)?[a-z0-9.-]+\.[a-z]{2,}(?:/\S*)?)$")


# lines the builder writes itself, in every language: never translated
BUILDER_LINES = {"the lifestyle 1980-08-05 – 2025-12-25"}      # G's art: the same line in every language


def is_fixed(key):
    plain = TOKEN.sub(" ", key).strip()
    if plain in BUILDER_LINES or plain.startswith("<!"): return True      # a doctype the extractor read as text
    if not re.search(r"[A-Za-z]{2,}", plain): return True          # no Latin letters to translate
    return bool(FIXED.fullmatch(plain))


def lock_fill(key, lock):
    """A segment that is a locked phrase, alone or wrapped in edge tokens, needs no translator."""
    plain = TOKEN.sub("", key).strip()
    if plain in lock:
        return key.replace(plain, lock[plain]) if key.count(plain) == 1 else None
    return None


def seg_id(key):
    """A segment's id is its English's own fingerprint: the same everywhere, in every cut, for ever."""
    import hashlib
    return "h" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def load_memory(lang):
    p = os.path.join(MEMORY, lang + ".json")
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}


def main():
    lang = sys.argv[1]
    assert lang in LANGS, lang
    words_max = int(sys.argv[sys.argv.index("--words") + 1]) if "--words" in sys.argv else 1100
    items_max = int(sys.argv[sys.argv.index("--items") + 1]) if "--items" in sys.argv else 70
    en = os.path.join(WORK, "en")
    templates = json.load(io.open(os.path.join(en, "templates.json"), encoding="utf-8"))
    instances = json.load(io.open(os.path.join(en, "instances.json"), encoding="utf-8"))
    lock = json.load(io.open(os.path.join(WORK, "lock", "lock_%s.json" % lang), encoding="utf-8"))
    lk = set(json.load(io.open(os.path.join(WORK, "lock", "lock_en.json"), encoding="utf-8"))["keys"])
    lock = {k: v for k, v in lock.items() if k in lk}             # the terms inflect: they are a glossary, not a fill
    memory = load_memory(lang)
    seen, todo = set(), []          # (page, key, kind)
    skipped = {"fixed": 0, "locked": 0, "memory": 0}
    for page, inst in instances.items():
        for iid in sorted(inst, key=lambda x: int(x[1:])):
            key, kind = inst[iid]["key"], inst[iid]["kind"]
            if key in seen: continue
            seen.add(key)
            if key in memory and memory[key].get("t"): skipped["memory"] += 1; continue
            if is_fixed(key): skipped["fixed"] += 1; continue
            if lock_fill(key, lock) is not None: skipped["locked"] += 1; continue
            todo.append((page, key, kind))
    out = os.path.join(WORK, lang, "slices"); os.makedirs(out, exist_ok=True)
    # a new generation every cut: names are never reused, so no patch can meet the wrong slice (10 October 2026)
    gens = [int(m.group(1)) for f in os.listdir(out) for m in [re.match(r"[a-z]{2}__g(\d+)b\d+\.json$", f)] if m]
    gen = max(gens) + 1 if gens else 1
    slices, cur, cur_words, cur_page = [], [], 0, None
    def close():
        nonlocal cur, cur_words
        if cur: slices.append(cur); cur, cur_words = [], 0
    for n, (page, key, kind) in enumerate(todo):
        w = len(TOKEN.sub(" ", key).split())
        if cur and (cur_words + w > words_max or len(cur) >= items_max or (page != cur_page and cur_words > words_max * 0.6)):
            close()
        cur.append({"id": seg_id(key), "page": page, "kind": kind, "text": key})
        cur_words += w; cur_page = page
    close()
    manifest = []
    for i, s in enumerate(slices):
        name = "%s__g%db%03d" % (lang, gen, i)
        json.dump({"lang": lang, "batch": name, "items": s}, io.open(os.path.join(out, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        manifest.append({"batch": name, "n": len(s), "words": sum(len(TOKEN.sub(" ", x["text"]).split()) for x in s), "pages": sorted(set(x["page"] for x in s))})
    json.dump({"gen": gen, "batches": manifest}, io.open(os.path.join(WORK, lang, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(lang, "generation", gen, ":", len(todo), "segments to translate in", len(slices), "slices;", sum(m["words"] for m in manifest), "words; skipped", skipped)


if __name__ == "__main__":
    main()
