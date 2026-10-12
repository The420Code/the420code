# -*- coding: utf-8 -*-
"""The translator agent's prompt for one slice, and the reviewer's for one slice.

    python prompts.py <lang> <batch>           prints the translation prompt (what the workflow sends)
    python prompts.py <lang> <batch> --review  prints the review prompt
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, ENGLISH_NAME
from briefs import BRIEF, VOICE

RULES = """THE ONE RULE. The English is canon; this is a translation of it, word for word. Translate exactly what the English says: nothing added, nothing dropped, nothing softened or strengthened, no explanation, no summary. A claim keeps its exact strength and its exact condition ("held", "derived", "forced", "fired", "paid", "open" mean what they mean, every time). Keep G's sentence breaks: one short English sentence is one short sentence in your language; never merge two sentences into one, never split one into two. Keep his images literally (the hourglass, the grain, the neck, the glass, the window, the hand and the mirror).

ONE TO ONE. Each item has an "id" and a "text". Give exactly one translation per item, keyed by its id. Never merge, split or reorder items.

TOKENS. The text carries tokens such as ⟦a1⟧…⟦/a1⟧, ⟦b2⟧…⟦/b2⟧, ⟦span3⟧…⟦/span3⟧, ⟦br4⟧, ⟦svg5⟧ and ⟦xa6⟧ (a marker of a link that opens or closes outside this item). They stand for the page's markup. Copy every token EXACTLY as written, the same number of times, and keep each opening token before its own closing token; put the translated words between the same pair that wraps them in English. An item that is only tokens, a name, a code, a number or an address is copied through unchanged. Never write a real < or > character (write the words; a "<" or ">" in a formula is written as the English writes it only if it is already a character in the text).

NUMBERS AND CODES ARE NEVER CHANGED. Every number, value, uncertainty, unit, sign and symbol is copied exactly as the English writes it: digits, decimal points, separators, ×, ±, σ, α, ε, superscripts, ratios, percentages, years. Codes stay exactly: AP01 to AP54, KS-31.1, KS-CCC.3, KS-GLASS.3, D-ID.1, D85, MKSR v5.37, DOIs (10.5281/zenodo...), versions, dates' digits, file names (.pdf, .py), commands and code. Formulae and equations stay as written.

KEEP IN ENGLISH, exactly: The 420 Code, the420code.org, whybekind.org, G, Studio G, Artist G, iam@the420code.org and every address and handle, AJ and the names of people, journals, institutions, collaborations and experiments (Planck, CODATA, PDG, DESI, JWST, SH0ES, KATRIN, Physical Review Letters ...), the titles of other people's papers and books, CC BY-ND 4.0, Ø, Greek letters, and the footer's line "the lifestyle 1980-08-05 – 2025-12-25" (G's art: never translated, never changed). A quotation of scripture is given as your language's standard, widely read Bible renders that verse, with its reference kept.

LOCKED WORDS. The table below gives the site's fixed names: the rooms, the papers, the books, every chapter title, the slogan and the labels, and the work's terms. Wherever an English item contains one of the names, your translation must contain its locked rendering, character for character, in the natural place (a term may take its grammatical case and number). Never vary a locked name, not even its punctuation.

THE SLOGAN. "Don’t be a cunt. Be kind." is G's own line on this site, the hard one, and is given exactly as locked; never softened, never censored. Nothing else is coarsened: no profanity the English does not have.

ITEM KINDS. "block" is page text. "meta:…" is a page's description or title for search engines and link previews (plain text, no tokens). "attr:aria-label" and "attr:title" are read aloud or shown on hover. "txt" is a line of llms.txt, the site's plain-text summary for AI readers. "jsonld" is a name or description in structured data. Translate them all as text in the same voice; a title stays a title."""


def slice_path(lang, batch): return os.path.join(WORK, lang, "slices", batch + ".json").replace("\\", "/")
def patch_path(lang, batch): return os.path.join(WORK, lang, "patches", batch + ".json").replace("\\", "/")
def review_path(lang, batch): return os.path.join(WORK, lang, "reviews", batch + ".json").replace("\\", "/")


def lock_table(lang):
    lock = json.load(io.open(os.path.join(WORK, "lock", "lock_%s.json" % lang), encoding="utf-8"))
    return "\n".join("  %s => %s" % (k, v) for k, v in lock.items() if k != "The 420 Code")


def translate_prompt(lang, batch):
    sl = slice_path(lang, batch); pt = patch_path(lang, batch)
    n = len(json.load(io.open(sl, encoding="utf-8"))["items"])
    return f"""You are translating the420code.org, G's work (an ethic derived from one axiom, the physics that fell out of it, and the condition under which every claim dies), from English into {ENGLISH_NAME[lang].upper()}, word for word, for publication under his name. The English is canon. This slice is {batch}.

{VOICE}

{BRIEF[lang]}

{RULES}

LOCKED (English => {ENGLISH_NAME[lang]}):
{lock_table(lang)}

STEPS
1. Read the slice (JSON: {{"items": [{{"id", "page", "kind", "text"}}, ...]}}): {sl}
   Read ALL of it first, so you know the page and the argument before you translate a line.
2. Translate every item.
3. With the Write tool, write ONE JSON object to exactly this path: {pt}
   It maps every item's id (a string) to its translation (a string). Valid JSON: UTF-8, double quotes, every inner double quote escaped as \\", no trailing comma, no comments, no other keys. Include EVERY id; the slice has {n} items.
4. Validate with exactly this command and confirm it prints {n}:
   python -c "import json;print(len(json.load(open(r'{pt}',encoding='utf-8'))))"
   If it errors or prints another number, fix the file and run it again.
5. Return only: batch={batch} n=<count> valid=<true|false>."""


def review_prompt(lang, batch):
    sl = slice_path(lang, batch); pt = patch_path(lang, batch); rv = review_path(lang, batch)
    return f"""You are the reviewer of a {ENGLISH_NAME[lang].upper()} translation of the420code.org, G's work, published under his name; the English is canon. Slice {batch}.

{VOICE}

{BRIEF[lang]}

{RULES}

LOCKED (English => {ENGLISH_NAME[lang]}):
{lock_table(lang)}

Read the English slice {sl} and the translation {pt} (a JSON object id => translation).
Judge every item against the English: meaning exact, nothing added or dropped or softened, G's sentence breaks kept, the images kept, the register and conventions above kept, every token present and paired, every locked phrase rendered exactly, the language natural enough that a native reader never senses a translation. Fix what is wrong; leave what is right.
With the Write tool, write to exactly {rv} a JSON object with two keys: "fixes": an object mapping an item id to its corrected translation, ONLY for items you changed (an empty object if none), and "notes": a list of at most eight short English sentences naming the kinds of faults you found (none invented). Validate it with:
   python -c "import json;d=json.load(open(r'{rv}',encoding='utf-8'));print(len(d['fixes']))"
Return only: batch={batch} fixed=<count>."""


def write_all(lang, review=False):
    """One prompt file per slice: WORK/<lang>/prompts/<batch>.md (or .review.md). The workflow's agents read them."""
    import glob
    out = os.path.join(WORK, lang, "prompts"); os.makedirs(out, exist_ok=True)
    os.makedirs(os.path.join(WORK, lang, "patches"), exist_ok=True)
    os.makedirs(os.path.join(WORK, lang, "reviews"), exist_ok=True)
    names = []
    for sp in sorted(glob.glob(os.path.join(WORK, lang, "slices", "*.json"))):
        batch = os.path.basename(sp)[:-5]
        text = review_prompt(lang, batch) if review else translate_prompt(lang, batch)
        io.open(os.path.join(out, batch + (".review.md" if review else ".md")), "w", encoding="utf-8").write(text)
        names.append(batch)
    print(lang, len(names), "prompts written")
    return names


if __name__ == "__main__":
    if sys.argv[1] == "write":
        write_all(sys.argv[2], review="--review" in sys.argv)
    else:
        lang, batch = sys.argv[1], sys.argv[2]
        print(review_prompt(lang, batch) if "--review" in sys.argv else translate_prompt(lang, batch))
