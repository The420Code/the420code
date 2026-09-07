# -*- coding: utf-8 -*-
"""The paragraph-level test of record, per the desk's ruling of 7 September 2026.

Reports PARAGRAPHS, not percentages. My earlier chunk test is withdrawn: it flags
a document against a PDF made from itself as 16% diverged, so it cannot be the gate.

  1. every source paragraph and table cell of >= 60 chars, in document order
  2. normalise both sides: whitespace collapsed; curly quotes, every dash,
     non-breaking hyphens and spaces mapped to ASCII; bold/italic markers stripped;
     the Contents block, running heads and bare page numbers dropped from the PDF
  3. forward: each source paragraph's first 70 characters must occur in the PDF
     reverse: each PDF sentence of >= 60 characters must occur in the source
  4. output the missing paragraphs VERBATIM, both directions
  5. control: AP49, whose PDF is made from its own markdown -- both lists must be
     empty or pure layout, or the checker is wrong

This logic belongs in museum/check_of_record.py, which MC maintains. It is written
here so it can be run now without overwriting MC's working file; hand it over."""
import os, re, sys, io, unicodedata

MIN, HEAD = 60, 70

DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), "-")
QUOTES = {0x2018: "'", 0x2019: "'", 0x201A: "'", 0x201B: "'",
          0x201C: '"', 0x201D: '"', 0x201E: '"', 0x00A0: " ", 0x202F: " ",
          0x2009: " ", 0x200A: " ", 0x2007: " ", 0xFEFF: ""}
MAP = {**DASHES, **QUOTES}

def norm(s):
    s = unicodedata.normalize("NFKC", s or "").translate(MAP)
    s = re.sub(r"\*\*|__|\*|_|`", "", s)          # bold / italic / code markers
    s = re.sub(r"---|--", "-", s)
    return re.sub(r"\s+", " ", s).strip()

def cmpkey(s):
    return re.sub(r"[^0-9a-z]+", "", norm(s).lower())

# ── the source side ──────────────────────────────────────────────────────────
def drop_contents(units):
    """Drop the source's own Contents block, exactly as pdf_body drops the PDF's.

    Added 7 September 2026, after AP44, AP45, AP46 and AP47 came back DIVERGED on
    nothing but their own front matter. The test dropped Contents on the published
    side and not on the source side, so every Contents sub-line in the source --
    "ten vertices, twenty-one edges: constitution at nodes, flow along edges",
    "KS-NPP.1, fired and shown forever - The proton elimination at the named bar"
    -- came back as a paragraph the published paper was missing. It is not
    missing; it was never printed as prose. Symmetry, not a loosened rule."""
    start = None
    for i, u in enumerate(units):
        if re.fullmatch(r"Contents", u.strip(), re.I):
            start = i; break
    if start is None:
        return units
    for j in range(start + 1, min(start + 80, len(units))):
        if re.match(r"(0 [-—]|1 [-—]|Artist.s Note)", units[j]):
            return units[:start] + units[j:]
    return units

def source_units(path):
    """Paragraphs and table cells, in document order."""
    ext = os.path.splitext(path)[1].lower()
    out = []
    if ext == ".docx":
        import docx
        from docx.table import Table
        from docx.text.paragraph import Paragraph
        d = docx.Document(path)
        for el in d.element.body.iterchildren():
            if el.tag.endswith("}p"):
                out.append(Paragraph(el, d).text)
            elif el.tag.endswith("}tbl"):
                for row in Table(el, d).rows:
                    for c in row.cells:
                        out.append(c.text)
    else:
        t = open(path, encoding="utf-8", errors="replace").read()
        t = re.sub(r"^\s*@@.*$", "", t, flags=re.M)   # typesetter directives, never printed
        t = re.sub(r"^\s*\|.*\|\s*$", lambda m: m.group(0).replace("|", " "), t, flags=re.M)
        out = re.split(r"\n\s*\n", t)
    return drop_contents([norm(x) for x in out if len(norm(x)) >= MIN])

# ── the published side ───────────────────────────────────────────────────────
def pdf_body(path, want_contents=False):
    """PDF text with the Contents block, running heads and bare page numbers dropped.

    With want_contents=True, returns (body, contents) instead of body. The dropped
    Contents block is not rubbish: it is the exact list of this paper's own front
    matter, and a source paragraph that is absent from the body but present in it
    is a Contents sub-line, not a divergence. Added 7 September 2026 -- it settles
    AP44's and AP47's flags by looking at the published paper rather than by
    teaching the checker each source file's markdown dialect."""
    import fitz
    d = fitz.open(path)
    pages = []
    for i in range(d.page_count):
        t = d[i].get_text()
        lines = []
        for ln in t.split("\n"):
            s = ln.strip()
            if not s: continue
            if re.fullmatch(r"\d{1,4}", s): continue                    # bare page number
            if re.search(r"\.{4,}\s*\d+$", s): continue                 # contents dot leader
            if re.fullmatch(r"(the420code\.org|Copyleft \d{4}\..*)", s): continue
            lines.append(s)
        pages.append("\n".join(lines))
    d.close()
    txt = "\n".join(pages)
    # drop everything from a "Contents" heading to the first numbered section
    contents = ""
    m = re.search(r"\bContents\b", txt)
    if m:
        n = re.search(r"\n\s*(0 —|0 -|1 —|1 -|Artist['’]s Note)", txt[m.end():])
        if n and n.start() < 6000:
            contents = txt[m.start():m.end() + n.start()]
            txt = txt[:m.start()] + txt[m.end() + n.start():]
    return (txt, contents) if want_contents else txt

SENT = re.compile(r"(?<=[.!?])\s+(?=[A-Z‘“(])")
def pdf_sentences(txt):
    """Sentences WITHIN a line, never across one.

    Extraction puts a heading on its own line and the body on the next; splitting
    the whole document into sentences glues them together, and the glued string
    exists in no source. The AP49 control caught exactly this -- 25 false
    divergences, every one a heading fused to the sentence after it."""
    out = []
    for line in txt.split(chr(10)):
        line = line.strip()
        if not line: continue
        for s in SENT.split(line):
            s = norm(s)
            if len(s) >= MIN: out.append(s)
    return out

# ── the test ─────────────────────────────────────────────────────────────────
def check(source, pdf):
    units = source_units(source)
    body, contents = pdf_body(pdf, want_contents=True)
    pblob = cmpkey(body)
    cblob = cmpkey(contents)
    sblob = cmpkey(" ".join(units))
    miss  = [u for u in units if cmpkey(u[:HEAD]) and cmpkey(u[:HEAD]) not in pblob]
    front = [u for u in miss if cmpkey(u[:HEAD]) in cblob]     # the paper's own Contents
    fwd   = [u for u in miss if u not in front]
    rev = [s for s in pdf_sentences(body) if cmpkey(s) not in sblob]
    return dict(source=source, pdf=pdf, n_units=len(units), fwd=fwd, rev=rev, front=front,
                verdict=("OF RECORD" if not fwd and not rev else "DIVERGED"))

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    r = check(sys.argv[1], sys.argv[2])
    print(f"{r['verdict']}  units={r['n_units']}  fwd={len(r['fwd'])}  rev={len(r['rev'])}")
    for x in r["fwd"][:10]: print("  source-only :", x[:150])
    for x in r["rev"][:10]: print("  pdf-only    :", x[:150])
