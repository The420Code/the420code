# -*- coding: utf-8 -*-
"""Fold the patches of a language into its translation memory, and apply the lock table.

    python merge.py <lang>            patches -> i18n/<lang>.json (and reviews' fixes on top, if any)
    python merge.py <lang> --missing  list the slices with no patch, or a patch that misses ids

The memory is one JSON object: English key => {"t": translation, "src": "lock|patch|review|fixed", "b": batch}.
A key the lock table settles is filled from the lock; a key with nothing to translate (a handle, a number, a
name) is copied through. Nothing in the memory is ever overwritten by an older patch: a review's fix wins over
the patch it reviewed; otherwise the last patch written wins.
"""
import glob, io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, MEMORY, LANGS
from batchize import is_fixed, lock_fill, load_memory


def repair(en, t):
    """Mechanical token faults the agents make, fixed without re-translation:
    an empty pair the English opens with (the summary's triangle, ⟦span1⟧⟦/span1⟧) dropped -> put back in front;
    tokens in a translation whose English has none (a meta title) -> taken out."""
    from extract import TOKEN
    if not TOKEN.search(en):
        return TOKEN.sub("", t).strip()
    m = re.match(r"^(⟦([a-z]+\d+)⟧⟦/\2⟧)", en)
    if m and m.group(1) not in t:
        t = m.group(1) + t.lstrip()
    return t


def save_memory(lang, mem):
    os.makedirs(MEMORY, exist_ok=True)
    json.dump(mem, io.open(os.path.join(MEMORY, lang + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)


def main():
    lang = sys.argv[1]; assert lang in LANGS
    en = json.load(io.open(os.path.join(WORK, "en", "segments.json"), encoding="utf-8"))
    lock = json.load(io.open(os.path.join(WORK, "lock", "lock_%s.json" % lang), encoding="utf-8"))
    lk = set(json.load(io.open(os.path.join(WORK, "lock", "lock_en.json"), encoding="utf-8"))["keys"])
    lock = {k: v for k, v in lock.items() if k in lk}             # the terms are a glossary, not a fill
    mem = load_memory(lang)
    counts = {"lock": 0, "fixed": 0, "patch": 0, "review": 0}
    for key in en:
        if is_fixed(key):
            if key not in mem: mem[key] = {"t": key, "src": "fixed"}; counts["fixed"] += 1
            continue
        lf = lock_fill(key, lock)
        if lf is not None and mem.get(key, {}).get("src") != "review":
            if mem.get(key, {}).get("t") != lf: counts["lock"] += 1
            mem[key] = {"t": lf, "src": "lock"}
    from batchize import seg_id
    by_id = {seg_id(k): k for k in en}
    slices = {}
    for sp in sorted(glob.glob(os.path.join(WORK, lang, "slices", "*.json"))):
        s = json.load(io.open(sp, encoding="utf-8"))
        items = {it["id"]: it["text"] for it in s["items"]}
        # every id must be the fingerprint of its own English, or this slice is not of this engine
        assert all(by_id.get(i) == t for i, t in items.items()), "slice %s: ids are not fingerprints" % s["batch"]
        slices[s["batch"]] = items
    missing = []
    for batch, items in slices.items():
        pp = os.path.join(WORK, lang, "patches", batch + ".json")
        if not os.path.exists(pp): missing.append((batch, "no patch")); continue
        try: patch = json.load(io.open(pp, encoding="utf-8"))
        except Exception as e: missing.append((batch, "unreadable: %s" % e)); continue
        lost = [i for i in items if i not in patch or not str(patch[i]).strip()]
        if lost: missing.append((batch, "%d ids missing" % len(lost)))
        for i, text in items.items():
            if i in patch and str(patch[i]).strip():
                if mem.get(text, {}).get("src") == "review": continue
                mem[text] = {"t": repair(text, str(patch[i]).strip()), "src": "patch", "b": batch}; counts["patch"] += 1
        rp = os.path.join(WORK, lang, "reviews", batch + ".json")
        if os.path.exists(rp):
            try: rv = json.load(io.open(rp, encoding="utf-8"))
            except Exception as e: missing.append((batch, "review unreadable: %s" % e)); continue
            for i, text in rv.get("fixes", {}).items():
                if i in items and str(text).strip():
                    mem[items[i]] = {"t": repair(items[i], str(text).strip()), "src": "review", "b": batch}; counts["review"] += 1
    if "--missing" in sys.argv:
        for b, why in missing: print(b, why)
        print(len(missing), "slices incomplete"); return
    save_memory(lang, mem)
    done = sum(1 for k in en if k in mem and mem[k].get("t"))
    print(lang, "memory:", done, "/", len(en), "segments;", counts, ";", len(missing), "slices incomplete")
    for b, why in missing[:20]: print("  ", b, why)


if __name__ == "__main__":
    main()
