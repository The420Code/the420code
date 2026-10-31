# -*- coding: utf-8 -*-
"""The gate: a language's memory must pass before its pages are built.

    python qa.py <lang> [--redo]   report; with --redo, take every failing translation out of the memory, so the
                                   next batchize.py cuts exactly those sentences again

Checks, per segment: a translation exists; every token of the English is present exactly once, pairs in order;
no raw < or >; no English left where there were words to translate (a translation identical to its English);
the locked names the English contains appear in the translation (the papers, the rooms, the books, the slogan and
the lines of three words or more; a lock key that is the whole segment must be rendered exactly as locked); the
digits of the English survive (as a multiset); no line-break token lost; nothing empty. English is canon: a
failure is fixed by translating the English again, never by bending the English.
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, MEMORY, LANGS
from extract import TOKEN
from batchize import is_fixed, load_memory

# locked phrases that are enforced inside longer segments: titles and the lines G fixed. Short labels are not
# (a label inside a sentence may inflect).
ENFORCE_MIN_WORDS = 3
LATIN_SCRIPT = {"de", "es", "fr", "it", "nl", "pt"}


def tokens(s): return sorted(TOKEN.findall(s))


CJK_DIGIT = {"〇": 0, "零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}


def cjk_numerals(s):
    """Chinese and Japanese write small numbers in characters (第七章, 三十一): read them as digits for the digit
    check, so 'Chapter 7' and 第七章 agree. Handles 1 to 9999; anything else is left as it is."""
    def val(m):
        t, total, cur = m.group(0), 0, 0
        if t in ("百", "千"): return t            # 千米 is a kilometre, not a thousand
        for ch in t:
            if ch in CJK_DIGIT: cur = CJK_DIGIT[ch]
            else:
                unit = {"十": 10, "百": 100, "千": 1000}[ch]
                total += (cur or 1) * unit; cur = 0
        return " %d " % (total + cur)             # spaced, so 一起 after KS-31.6 never runs into its digits
    return re.sub(r"[〇零一二两三四五六七八九十百千]+", val, s)


FUNCTION_WORDS = {"the", "a", "an", "of", "and", "is", "in", "to", "you", "it", "that", "this", "be", "are", "for",
                  "on", "with", "not", "or", "your", "one", "what", "by", "from"}
# names that stay in Latin letters in every language; taken out before a segment is judged
NAMES = ["The 420 Code", "the 420 code", "the420code.org", "whybekind.global", "media.the420code.org", "studiog.global", "artist-g.global",
         "Studio G Global", "Studio G", "Artist G", "TikTok", "YouTube", "Instagram", "Facebook", "why be kind",
         "iam@the420code.org", "CC BY-ND 4.0", "Antichristos", "lucid.rodeo", "Kill Switches", "Kill Switch",
         "the lifestyle 1980-08-05 – 2025-12-25", "Copyleft", "GitHub", "Zenodo", "OSF", "Rosin", "The Records"]


def strip_names(plain):
    plain = re.sub(r"(?:https?://)?[a-z0-9.-]+\.(?:org|global|com)(?:/\S*)?", " ", plain)
    for n in NAMES: plain = plain.replace(n, " ")
    return plain


def has_english_words(plain):
    """A segment with none of English's little words is a name, a handle or a formula, and may stay as it is."""
    return any(w.strip(".,;:!?()“”\"'’") in FUNCTION_WORDS for w in strip_names(plain).lower().split())


def pairs_ok(s):
    stack = []
    for t in TOKEN.findall(s):
        if t.startswith("/"):
            if not stack or stack[-1] != t[1:]: return False
            stack.pop()
        elif not re.match(r"(br|svg|img|wbr|use|source|input|hr|path|track|meta|link)\d+$", t) and not t.startswith("x"): stack.append(t)
    return not stack


def main():
    lang = sys.argv[1]; assert lang in LANGS
    en = json.load(io.open(os.path.join(WORK, "en", "segments.json"), encoding="utf-8"))
    lock = json.load(io.open(os.path.join(WORK, "lock", "lock_%s.json" % lang), encoding="utf-8"))
    mem = load_memory(lang)
    # "why be kind" is also the Facebook account's name on a follow card, so the wordmark is not enforced inside sentences
    # enforced inside longer text: the book titles and the lines G has fixed. A chapter title is enforced only where
    # it stands alone (its own heading, its menu entry), because prose may name it in passing ("the Master Kill Switch
    # Registry" is not the chapter "Kill Switch Registry").
    lk = json.load(io.open(os.path.join(WORK, "lock", "lock_en.json"), encoding="utf-8"))["keys"]
    # names are enforced inside prose (the papers, the rooms, the books, lines of three words or more that begin with a
    # capital); the menu's lower-case room lines ("the structure of reality") are not: prose inflects them
    fixed_lines = {k for k in lk if (len(k.split()) >= ENFORCE_MIN_WORDS and k[:1].isupper()) or re.match(r"AP\d\d ", k)
                   or k.startswith("Ø ")}
    import lock as L
    chapters = set(L.chapter_titles())
    enforce = {k: v for k, v in lock.items() if k in fixed_lines and k not in chapters and k != v}
    whole = {k: v for k, v in lock.items() if k in lk}           # a segment that IS a lock key reads exactly as locked
    hard = []
    fails, kinds = [], {}
    # reviewed exceptions: i18n/qa_accepted_<lang>.json, English => {"t": the translation as reviewed, "why": ...}.
    # An exception holds only while the translation is exactly the one reviewed; any change is checked again.
    acc_p = os.path.join(MEMORY, "qa_accepted_%s.json" % lang)
    accepted = json.load(io.open(acc_p, encoding="utf-8")) if os.path.exists(acc_p) else {}
    def bad(key, why):
        if key in accepted and mem.get(key, {}).get("t") == accepted[key]["t"]: return
        fails.append((key, why)); kinds[why.split(":")[0]] = kinds.get(why.split(":")[0], 0) + 1
    for key, info in en.items():
        m = mem.get(key)
        if not m or not m.get("t"): bad(key, "missing"); continue
        t = m["t"]
        if is_fixed(key): continue
        if tokens(t) != tokens(key): bad(key, "tokens: %s vs %s" % (tokens(key), tokens(t))); continue
        if not pairs_ok(t): bad(key, "token pairs out of order"); continue
        if "<" in t or ">" in t: bad(key, "raw angle bracket"); continue
        if re.search(r"[\x00-\x08\x0b-\x1f\x7f�]", t): bad(key, "control character"); continue
        import html as _h
        plain_en = _h.unescape(TOKEN.sub(" ", key)).strip(); plain_t = _h.unescape(TOKEN.sub(" ", t)).strip()
        code = "⟦code" in key or "⟦pre" in key or re.match(r"(pip|python3?|git|curl|npm) ", plain_en)             or (" = " in plain_en and not re.search(r"[A-Za-z]{4,}", plain_en))     # an equation is written as it stands
        if plain_t == plain_en and len(plain_en.split()) >= 2 and m.get("src") != "lock" and has_english_words(plain_en) and not code:
            bad(key, "untranslated: identical to English"); continue
        if lang not in LATIN_SCRIPT and has_english_words(plain_en):
            # a non-Latin language: a translation that is mostly Latin letters is not translated
            letters = re.findall(r"[^\W\d_]", strip_names(plain_t))
            latin = [c for c in letters if c.isascii()]
            if letters and len(latin) / len(letters) > 0.6 and len(strip_names(plain_en).split()) >= 3 and not re.search(r"AP\d|KS-", plain_en):
                bad(key, "untranslated: Latin script"); continue
        if plain_en in whole and plain_t != whole[plain_en] and m.get("src") != "review":
            bad(key, "lock: the whole segment %r expected %r" % (plain_en, whole[plain_en])); continue
        for ph, tr in ({} if code else enforce).items():            # code is code: its comments stay as written
            if ph in plain_en and tr not in plain_t:
                # a longer locked phrase that contains this one (a book title that carries a chapter's name) rules
                if any(ph != o and ph in o and o in plain_en for o in lock): continue
                bad(key, "lock: %r expected %r" % (ph, tr)); break
        else:
            for w in hard:
                if w in t: bad(key, "profanity: %r" % w); break
            else:
                # every number the English writes in digits survives; a language may add digits (3분 49초 for
                # "three minutes and forty-nine seconds") but never lose one
                # thousands separators are each language's own (1,836 / 1.836 / 1 836 / 1836): read the number whole
                ungroup = lambda x: re.sub(r"(?<=\d)[,.    '](?=\d{3}(?!\d))", "", x)
                d_en = re.findall(r"\d+", ungroup(plain_en)); d_t = re.findall(r"\d+", ungroup(cjk_numerals(plain_t)))
                lost = [d for d in d_en if d_en.count(d) > d_t.count(d)]
                if lost: bad(key, "digits lost: %s" % lost); continue
                if re.search(r"c[u*]nt", t, re.I): bad(key, "profanity: the hard word"); continue
    print(lang, "QA:", len(fails), "failures of", len(en), "segments;", kinds)
    for key, why in [f for f in fails if not f[1].startswith("missing")][:40] + fails[:3]: print("  -", why, "|", key[:110].replace("\n", " "))
    if "--redo" in sys.argv and fails:
        from merge import save_memory
        n = 0
        for k, why in fails:
            if k in mem and mem[k].get("src") not in ("lock", "fixed"):
                del mem[k]; n += 1
        save_memory(lang, mem)
        print("redo:", n, "translations taken out of the memory; now run batchize.py", lang, "and the workflow")
    if "--fix-slices" in sys.argv and fails:
        out = os.path.join(WORK, lang, "slices")
        inst = json.load(io.open(os.path.join(WORK, "en", "instances.json"), encoding="utf-8"))
        page_of = {}
        for page, ii in inst.items():
            for v in ii.values(): page_of.setdefault(v["key"], page)
        items = [{"id": "r%05d" % n, "page": page_of.get(k, ""), "kind": en[k]["k"], "text": k, "why": why}
                 for n, (k, why) in enumerate(fails) if why != "missing" or True]
        n = 0
        for i in range(0, len(items), 60):
            name = "%s__r%03d" % (lang, n); n += 1
            json.dump({"lang": lang, "batch": name, "items": items[i:i + 60]}, io.open(os.path.join(out, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print("wrote", n, "repair slices")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
