# -*- coding: utf-8 -*-
"""The lock table: the names that must read the same wherever they appear on the420code.org, settled once per
language before any slice is translated. The rooms of the menu and their lines, the fifty-four Artist's Proofs by
number and title, the books (the Five Doors, the Ø Models, the eight notebooks, the registry), every chapter title,
the slogan, the oneness line and the page labels. And a glossary of the work's terms (record, operator, window, kill
switch ...), which every translator is given; terms inflect, so the gate checks the titles and phrases, not the terms.

    python lock.py seed            WORK/lock/lock_en.json (the keys, with their kind) and WORK/lock/seed_<lang>.json
    python lock.py prompt <lang>   the prompt for the one agent that fills WORK/lock/lock_<lang>.json
    python lock.py check [lang]    every lock file complete and sane

The seeds are words already published in the language and are not re-translated: whybekind.org's lock table for the
language (the same five books, their chapters, the oneness line; github.com/The420Code/whybekind, i18n/), and the
slogan as this site's own edition in that language prints it.
"""
import glob, io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, WORK, LANGS, ENGLISH_NAME

WBK = os.environ.get("WBK_REPO", r"C:\Users\info\whybekind")
LOCKDIR = os.path.join(WORK, "lock")

FIVE_DOORS = ["The Illusion of the Other", "Being After Religion", "Antichristos", "The Relationship Corridor",
              "The Relationship Corridor: What Is Love", "The Interior"]
MODELS = ["Dissolutions", "Resolutions", "Horizons", "Applications", "Ø Dissolutions", "Ø Resolutions", "Ø Horizons",
          "Ø Applications"]
NOTEBOOKS = ["Notebook I", "Notebook II", "Notebook III", "Notebook IV", "Notebook V", "Notebook VI", "Notebook VII",
             "Notebook VIII", "The Premise", "Spacetime", "Quantum Mechanics", "Forces and Constants",
             "Particles and Matter", "Cosmology", "The Operator Interface", "Consequences",
             "Master Kill Switch Registry", "Artist’s Proofs", "Artist’s Proof"]
ROOMS = ["What Is The 420 Code", "Ø Physics", "Ø Confirm the Math", "Ø Museum", "Ø Five Doors", "Ø Models",
         "Ø Exhibition", "Ø Films", "1 Axiom", "Ø Predictions", "Ø Notebooks", "Ø Proofs", "Ø Why 21 Is Forced",
         "Ø One Awareness", "Ø Instruments", "Ø Independent Check", "Ø Kill Switches", "Ø Method", "Ø Glossary",
         "Ø Frozen Predictions", "Ø Support the Work", "Three Ways of Being Sure", "Ø On this page",
         # the rooms' lines under their names in the menu
         "start here", "ethics from reality", "the heart of it", "the philosophy", "the whole story",
         "the argument, on film", "one record exists", "the structure of reality", "frozen before the test",
         "all the proofs, bound", "fifty-four artist’s proofs", "the count, in full", "the ethic, derived",
         "proof records", "run it yourself", "ways it could be wrong", "forced logic, nothing else",
         "the words, defined", "external verification", "the work is free, the cost is not"]
PHRASES = ["Don’t be a cunt. Be kind.", "Don’t be cruel. Be kind.", "Be kind.", "One record exists.",
           "One record exists", "The awareness in me is the awareness in you.", "Why be kind?",
           "The one being harmed is the one doing the harming, experienced from a different window.",
           "Nothing here compels anyone.", "reality audits.",
           # labels
           "Read", "Read online", "Download", "In this book", "Collapse all", "Expand all", "Back to", "The chapters",
           "Watch the films", "Where it would die", "Where the reach ends", "Already inside", "Epilogue",
           "Artist’s Note", "Preface", "Orientation", "Closing", "Machine-readable summary", "Everything in a few pages",
           "The short answer:", "Artist:", "Duration:", "Exhibition:", "Contact:", "Support once", "the document of record"]
# the work's terms: the translator is given them; they inflect, so they are not checked character for character
TERMS = ["record", "record history", "operator", "the one operator", "window", "the neck", "grain", "the glass",
         "the interior", "coupling", "coupling capacity", "kill switch", "debt", "corpse", "the wall", "fired",
         "live", "closed", "paid", "frozen prediction", "pre-registration", "registration", "freeze",
         "Actualization State", "the axiom", "the break", "the hold", "the leak", "leakage", "the flow", "outflow",
         "inflow", "symmetry", "restriction", "awareness", "the other", "corridor", "viability corridor",
         "consequence geometry", "Architecture A", "Architecture B", "the minimum bias", "ε-bias", "the floor",
         "fine-structure constant", "standard deviation", "free parameter", "measured input", "derivation",
         "derived", "forced", "numerology", "the scoreboard", "the registry", "notebook", "dated note", "erratum",
         "finding", "superseding entry", "the room", "the doors", "the front door", "Five Doors", "the scaffold"]


def chapter_titles():
    out = []
    for sec in ("five-doors", "models"):
        for p in sorted(glob.glob(os.path.join(SITE, sec, "*", "*", "index.html"))):
            h = io.open(p, encoding="utf-8").read()
            m = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
            if m:
                out.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip())
    return out


def paper_titles():
    """AP01 The Actualization State ... AP54 Seeing Alpha, from the papers' own file names."""
    out = []
    for f in sorted(os.listdir(SITE)):
        m = re.match(r"^(AP\d\d)_(.+)\.pdf$", f)
        if m:
            out.append("%s %s" % (m.group(1), m.group(2).replace("_", " ")))
    return out


def lock_keys():
    keys = FIVE_DOORS + MODELS + NOTEBOOKS + ROOMS + paper_titles() + PHRASES + chapter_titles()
    return list(dict.fromkeys(k for k in keys if k))


def seed(lang):
    s = {"The 420 Code": "The 420 Code"}
    wl = os.path.join(WBK, "i18n", "lock_%s.json" % lang)
    if os.path.exists(wl):
        w = json.load(io.open(wl, encoding="utf-8"))
        keys = set(lock_keys())
        for k, v in w.items():
            if k in keys and "ollbruch" not in v:        # this site says Kill Switch, as its own edition does
                s[k] = v
    # the rooms, as this site's edition in the language names them in its menu (the same rooms, in the same order)
    names = lambda p: [re.sub(r"\s+", " ", x).strip() for x in
                       re.findall(r'class="nav-room"[^>]*>([^<]*)', io.open(p, encoding="utf-8").read())]
    ed = os.path.join(SITE, lang, "index.html")
    if os.path.exists(ed):
        en_rooms, ed_rooms = names(os.path.join(SITE, "index.html")), names(ed)
        if len(en_rooms) == len(ed_rooms):
            for a, b in zip(en_rooms, ed_rooms):
                s[a] = b
    # the Ø Models books, where the edition keeps their English names (the German edition does: Ø Dissolutions ...)
    if os.path.exists(ed):
        h = io.open(ed, encoding="utf-8").read()
        for k in MODELS:
            if k.startswith("Ø ") and k in h:
                s[k] = k
                s[k[2:]] = k[2:]
    # the hard slogan, as this site's edition in the language prints it (G's published line)
    st = os.path.join(SITE, "i18n", "frontdoor", "frontdoor_strings_%s.json" % lang)
    if os.path.exists(st):
        q = json.load(io.open(st, encoding="utf-8"))["strings"].get("quote.the_ethic", "").strip()
        if q:
            s["Don’t be a cunt. Be kind."] = q
    return s


def cmd_seed(langs):
    os.makedirs(LOCKDIR, exist_ok=True)
    keys = lock_keys()
    json.dump({"keys": keys, "terms": TERMS}, io.open(os.path.join(LOCKDIR, "lock_en.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for lang in langs:
        s = seed(lang)
        json.dump(s, io.open(os.path.join(LOCKDIR, "seed_%s.json" % lang), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(lang, len(s), "seeded; the slogan:", s.get("Don’t be a cunt. Be kind."))
    print(len(keys), "lock keys,", len(TERMS), "terms")


def prompt(lang):
    from briefs import BRIEF, VOICE
    en = json.load(io.open(os.path.join(LOCKDIR, "lock_en.json"), encoding="utf-8"))
    keys, terms = en["keys"], en["terms"]
    s = json.load(io.open(os.path.join(LOCKDIR, "seed_%s.json" % lang), encoding="utf-8"))
    out = os.path.join(LOCKDIR, "lock_%s.json" % lang).replace("\\", "/")
    seeded = "\n".join("  %s => %s" % (k, v) for k, v in s.items())
    todo = [k for k in keys if k not in s]
    total = len(keys) + len(terms)
    return f"""You are settling the LOCK TABLE for the {ENGLISH_NAME[lang]} edition of the420code.org, G's work: ethics derived from one axiom, "one record exists", with the physics that fell out of it and, for every claim, the condition under which it dies. The whole English site is being translated into {ENGLISH_NAME[lang]} word for word. Every entry in this table will be used verbatim, everywhere it appears, by every translator of the site, so each must be the single best rendering: exact, natural, consistent with the others. The English is canon; a translation is a translation.

{VOICE}

{BRIEF[lang]}

ALREADY SETTLED (published in {ENGLISH_NAME[lang]} already: whybekind.org's edition of the same books, and this site's own slogan; copy them EXACTLY):
{seeded}

WHAT THE KEYS ARE
- Room names begin with Ø, the work's sign; keep the Ø and translate the name ("Ø Physics" => Ø + the word for physics). "1 Axiom" keeps its 1.
- The rooms' lines ("start here", "the heart of it", ...) are the short lines under each room's name in the menu: lower case where your language allows, as short as the English.
- "APnn Title" are the fifty-four Artist's Proofs, G's papers: keep "APnn" and translate the title as a title.
- "Notebook I" ... "Notebook VIII" keep their Roman numerals; the notebooks' names follow ("The Premise", ...).
- Chapter titles are the chapters of the Five Doors and the Ø Models books: titles, short and strong.
- Labels ("Read", "Download", "Collapse all", "Back to", "Artist:") are buttons, links and captions: short; keep a trailing colon.
- "Don’t be a cunt. Be kind." is G's line, the hard one, on this site only: it is settled above and is never softened.
- "The 420 Code", "G", "the420code.org", "whybekind.org", "AP", "KS" stay in English.

THE TERMS (a glossary every translator will be given; give each its one rendering, the base form, as the work uses it: a technical term of the work, consistent with the settled lines above):
{json.dumps(terms, ensure_ascii=False)}

ENTRIES TO SETTLE (the key is the English, exactly):
{json.dumps(todo, ensure_ascii=False, indent=0)}

OUTPUT. With the Write tool, write ONE JSON object to exactly this path:
  {out}
It maps EVERY key above, the already-settled ones included, AND every term, to its {ENGLISH_NAME[lang]} text: {total} entries. Valid JSON, UTF-8, double quotes, no trailing comma, no comments. Then validate with exactly:
  python -c "import json;d=json.load(open(r'{out}',encoding='utf-8'));print(len(d))"
It must print {total}. Fix and re-run until it does. Return one line: the count, and how you rendered "Ø Kill Switches", "kill switch" and "record"."""


def cmd_check(langs):
    en = json.load(io.open(os.path.join(LOCKDIR, "lock_en.json"), encoding="utf-8"))
    keys = en["keys"] + en["terms"]
    ok = True
    for lang in langs:
        p = os.path.join(LOCKDIR, "lock_%s.json" % lang)
        if not os.path.exists(p):
            print(lang, "MISSING"); ok = False; continue
        d = json.load(io.open(p, encoding="utf-8"))
        s = json.load(io.open(os.path.join(LOCKDIR, "seed_%s.json" % lang), encoding="utf-8"))
        miss = [k for k in keys if k not in d or not str(d[k]).strip()]
        bad = [k for k, v in s.items() if d.get(k) != v]
        print(lang, "entries", len(d), "missing", len(miss), miss[:5], "seed changed", bad)
        if miss or bad:
            ok = False
    print("OK" if ok else "NOT OK")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "seed"
    langs = sys.argv[2:] or ["de"]
    if cmd == "seed": cmd_seed(langs)
    elif cmd == "prompt": print(prompt(langs[0]))
    elif cmd == "check": cmd_check(langs)
