#!/usr/bin/env python3
"""Build the Ø Models online library: static HTML for Netlify.

Input:  ../<book>/00_front.txt, ../<book>/ch*.txt, ../<book>/99_epilogue.txt, onelines_*.json
Output: site/models/<book>/index.html, site/models/<book>/<slug>/index.html, site/models/<book>/epilogue/index.html,
        site/models/reader.css, site/models/reader.js, site/models/models-snippet.html

Every chapter page has the same structure:
  strap · question · one line · opening · sections (closed) · where it would die (closed, IDs link to the registry) · source · prev/next
"""
import re, os, sys, json, html, glob, shutil
sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, '..')
OUT = os.path.join(ROOT, 'site', 'models')
REGISTRY = 'https://the420code.org/killswitches/'
WALL = 'https://the420code.org/what-is-the-420-code/#where-it-would-die'

SITE = 'https://the420code.org'

# The site's header, 22 September 2026 (G: "all pages must ideally have the same sticky menu at the top").
# Built by the site's own header.py, with the rooms block taken verbatim from the English front door, as
# every English-only room is built (WC/tools/room_shell.py). After any change to the menu, rebuild.
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'i18n', 'frontdoor'))
import header as H  # noqa: E402
_door = open(os.path.join(REPO, 'what-is-the-420-code', 'index.html'), encoding='utf-8').read()
_i = _door.index('  <div class="nav-menu">')
ROOMS_MENU = _door[_i:_door.index('  </div>', _i) + len('  </div>')]
# 17 -> 18 on 24 September 2026: Ø The Films joins the menu (films_menu.py). Rebuild this
# library after any menu change, or its pages carry a menu the rest of the site has left.
assert _door.count('  <div class="nav-menu">') == 1 and ROOMS_MENU.count('class="nav-room"') == 18, 'the front door\'s rooms block'
BOOKS = [
    dict(slug='dissolutions', title='Ø Dissolutions', prefix='PZ', pdf='/models/dissolutions.pdf', original='/Dissolutions.pdf', original_pages=370, edition='v1.0'),
    dict(slug='resolutions', title='Ø Resolutions', prefix='RES', pdf='/models/resolutions.pdf', original='/Resolutions.pdf', original_pages=548, edition='v1.0'),
    dict(slug='applications', title='Ø Applications', prefix='APP', pdf='/models/applications.pdf', original='/Applications.pdf', original_pages=549, edition='v1.0'),
    dict(slug='horizons', title='Ø Horizons', prefix='HOR', pdf='/models/horizons.pdf', original='/Horizons.pdf', original_pages=494, edition='v1.0'),
]
WORDS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
         10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen'}

ONELINES = {}
for f in glob.glob(os.path.join(ROOT, 'onelines_*.json')):
    ONELINES.update(json.load(open(f, encoding='utf-8')))

KS_RE = re.compile(r'^([A-Z]+-[\d.]+) — (.*)$', re.S)

# ---------- text helpers ----------
def curly(s):
    s = re.sub(r'(^|[\s(\[—])"', r'\1“', s)
    s = s.replace('"', '”')
    s = re.sub(r"(^|[\s(\[—])'", r'\1‘', s)
    s = s.replace("'", '’')
    return s

def esc(s):
    return curly(html.escape(s, quote=False))

def slugify(s):
    s = s.lower().replace('’', '').replace("'", '')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

def ks_id(sid):
    # registry anchors: KS-PZ1.1 -> #ks-pz1-1 ; RES-8.5.1 -> #ks-res8-5-1
    return 'ks-' + sid.lower().replace('-', '', 1).replace('.', '-')

def ks_anchor(sid):
    return REGISTRY + '#' + ks_id(sid)

def ks_registry_form(sid):
    # PZ-1.1 -> KS-PZ1.1
    return 'KS-' + sid.replace('-', '', 1)

def blurb(parts, lo=120, hi=155):
    """A page's own first lines, between 120 and 155 characters: enough for a search result to say
    what the page is, never cut in the middle of a word."""
    out = ''
    for p in parts:
        for s in re.split(r'(?<=[.!?])\s+', (p or '').strip()):
            s = ' '.join(s.split())
            if not s:
                continue
            if s in out:
                continue          # the one line is often the opening's first sentence
            cand = (out + ' ' + s).strip()
            if len(cand) <= hi:
                out = cand
                if len(out) >= lo:
                    return out
                continue
            if len(out) >= lo:
                return out
            return cand[:hi].rsplit(' ', 1)[0].rstrip(' ,;:—-')
    return out


def fit_title(a, b, limit=60):
    """The longest form of a page's title that still fits. The page's own name never goes; the
    work's name goes first, then the book's."""
    for t in ((f'{a} — {b} — The 420 Code', f'{a} — {b}') if b else ()) + (f'{a} — The 420 Code', a):
        if len(t) <= limit:
            return t
    return a[:limit].rsplit(' ', 1)[0].rstrip(' ,;:—-')


def link_help(s):
    """The crisis line is a link: a reader who needs it should not have to type it out."""
    return esc(s).replace('findahelpline.com',
                          '<a href="https://findahelpline.com/" rel="noopener">findahelpline.com</a>', 1)


def check(page, where):
    """Nothing leaves the build with a tool's tag on it, a double-encoded character in it, or a
    heading still written as markdown (the desk's brief of 24 September 2026, 6.1, 6.2, 6.11)."""
    for bad in ('claude-agent', 'â€', 'Î±', 'Ã˜', '<p>## '):
        assert bad not in page, f'{where}: {bad!r}'
    return page


def para_html(p):
    if p.startswith('## '):
        return f'<h2 class="sub">{esc(p[3:].strip())}</h2>'
    m = KS_RE.match(p)
    if m:
        sid, rest = m.group(1), m.group(2)
        return (f'<p class="ks" id="{ks_id(sid)}"><a class="ks-id" href="{ks_anchor(sid)}" '
                f'title="This switch in the registry">{esc(sid)}</a>{esc(rest)}</p>')
    h = esc(p)
    h = re.sub(r'the420code\.org/([a-z0-9-]+)', r'<a href="https://the420code.org/\1/">the420code.org/\1</a>', h)
    return f'<p>{h}</p>'

def paras(block):
    return [p.strip() for p in block.strip().split('\n\n') if p.strip()]

def split_sections(body, level='## '):
    """-> (preamble_paras, [(heading, paras)])"""
    parts = re.split(r'^' + re.escape(level), body, flags=re.M)
    pre = paras(parts[0])
    secs = []
    for chunk in parts[1:]:
        head, _, rest = chunk.partition('\n')
        secs.append((head.strip(), paras(rest)))
    return pre, secs

def details(heading, body_html, cls='sec', extra='', open_=None):
    if open_ is None:
        open_ = False   # every row arrives closed, G's word, 22 September 2026
    o = ' open' if open_ else ''
    return (f'<details class="{cls}"{o}><summary><span class="tri" aria-hidden="true"></span>{esc(heading)}{extra}</summary>'
            f'<div class="sec-body">{body_html}</div></details>')

# 24 September 2026: the pages carry the author's corrections of that day and the short
# edition's PDF, set by the desk that typesets it, does not yet. The book page says so until
# it does (WC/tools/stale_pdf_note_0924.py --off).
STALE_PDF = ('<p class="edition"><b>Dated note, 24 September 2026.</b> This edition’s PDF was set '
             'before the author’s corrections of 24 September and does not carry them yet; the '
             'pages here do. It is being reset. Nothing on this page waits for it.</p>')

# ---------- page shell ----------
def shell(title, body, book, depth, description='', path='/', book_first=False):
    rel = '../' * depth
    full_title = (fit_title(book['title'], title) if book_first
                  else fit_title(title, book.get('short', book['title'])))
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The 420 Code — Eye of the Universe">
<title>{esc(full_title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<link rel="stylesheet" href="{rel}reader.css">
<link rel="apple-touch-icon" href="/Eye_of_the_Universe.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/jpeg" href="/Eye_of_the_Universe.jpg">
</head>
<body>
<div class="c">
{H.english_header(ROOMS_MENU, "en-only", path)}
{body}
<footer class="colophon">
<p class="editions">This is the short edition of {esc(book["title"])} — a summary. Where a step is compressed here, the original carries it in full. <a href="{book["original"]}">The original book (PDF)</a> · <a href="{book["pdf"]}">This edition (PDF)</a> · <a href="/models/{book["slug"]}/">Read this edition online</a></p>
<p><a href="https://the420code.org/">The 420 Code</a> · <a href="/models/">Ø Models</a> · {esc(book["title"])}</p>
</footer>
<div class="constraint" id="about">
  <p style="margin:0 0 1rem"><a href="https://studiog.global" target="_blank" rel="noopener"><img src="/StudioG_Logo_Web.jpg" alt="Studio G" style="height:40px"></a></p>
  <p><b>Artist:</b> <a href="https://artist-g.global/about/" target="_blank" rel="noopener" style="color:inherit">G</a> · <a href="https://studiog.global" target="_blank" rel="noopener" style="color:inherit">Studio G, Cape Town</a></p>
  <p><b>Duration:</b> 30+ years · <b>Exhibition:</b> over a million words</p>
  <p><b>Contact:</b> <a href="mailto:iam@the420code.org" style="color:inherit">iam@the420code.org</a></p>
  <p style="margin-top:1rem">This work is Copyleft. You are free to download, print, share, and distribute. You are not free to alter the source. Keep the signal clean.</p>
</div>

<p class="oneness">One record exists.<br>Be kind is a derivation.<br>The I Am in me is the I Am in you.</p>

<div class="footer">
  <p style="text-align:center;margin:0 0 1rem"><img src="/Eye_of_the_Universe.jpg" alt="the 420 code" style="height:40px"></p>
  <p style="font-weight:700">Don’t be a cunt. Be kind.</p>
  <p>the420code.org · Copyleft 2026</p>
  <p>the lifestyle 1980-08-05 – 2025-12-25</p>
</div>
</div>
<script src="{rel}reader.js"></script>
{H.JS}
</body>
</html>
'''

def strap(book, crumb, current='read'):
    # 22 September 2026, G: "remove listen - soon for now". When a chapter has audio, add a
    # 'listen' mode here as a link and put its <li> back between Read and Download.
    modes = {
        'read': '<span class="on">Read</span>',
        'download': f'<a href="{book["pdf"]}">Download</a>',
    }
    return (f'<header class="strap"><div class="book"><a href="/models/{book["slug"]}/"><b>{esc(book["title"])}</b></a>'
            f' · the short edition{crumb}</div>'
            f'<ul class="modes"><li>{modes["read"]}</li><li>{modes["download"]}</li></ul></header>')

def up(book=None):
    """The way back, on every page, between Previous and Next: the book's contents and Ø Models."""
    to_book = f'<a href="/models/{book["slug"]}/">{esc(book["title"])}</a>' if book else ''
    return f'<div class="up"><small>Back to</small>{to_book}<a href="/models/">Ø Models</a></div>'

# ---------- parse a book ----------
def load_book(book):
    d = os.path.join(SRC, book['slug'])
    front = open(os.path.join(d, '00_front.txt'), encoding='utf-8').read()
    tl = [l[2:].strip() for l in front.splitlines() if l.startswith('~ ')]
    book['subtitle'] = tl[1]
    book['tagline'] = tl[2]
    # level-1 parts of the front matter
    parts = re.split(r'^# ', front.split('\n---\n', 1)[1] if '\n---\n' in front else front, flags=re.M)
    front_parts = []
    for chunk in parts[1:]:
        head, _, rest = chunk.partition('\n')
        rest = re.sub(r'^\[Candidate.*?\]\s*$', '', rest, flags=re.M)  # candidate marker line
        cite = ''
        m = re.search(r'^> (.+)$', rest, re.M)
        if m:
            cite = m.group(1); rest = rest.replace(m.group(0), '')
        pre, secs = split_sections(rest)
        front_parts.append((head.strip(), pre, secs, cite))
    book['front'] = front_parts

    chapters = []
    files = sorted(glob.glob(os.path.join(d, 'ch*.txt')),
                   key=lambda p: float(re.search(r'ch(\d+)(?:_(\d))?', p).group(1) +
                                       ('.' + re.search(r'ch(\d+)(?:_(\d))?', p).group(2)
                                        if re.search(r'ch(\d+)(?:_(\d))?', p).group(2) else '')))
    for f in files:
        t = open(f, encoding='utf-8').read()
        title = re.search(r'^# (.+)$', t, re.M).group(1)
        num, _, question = title.partition(' — ')
        m = re.search(r'ch(\d+)(?:_(\d))?', f)
        key = m.group(1) + ('-' + m.group(2) if m.group(2) else '')
        body = t.split('\n', 1)[1]
        src = ''
        m2 = re.search(r'^> (.+)$', body, re.M)
        if m2:
            src = m2.group(1); body = body.replace(m2.group(0), '')
        # 24 September 2026, the desk's brief B4b: a line marked "! " is the help line. It is
        # lifted out of the text the way the source line is, and set under the chapter's one line,
        # above everything else. It stays in the text so the page and the PDF carry one text.
        help_line = ''
        m4 = re.search(r'^! (.+)$', body, re.M)
        if m4:
            help_line = m4.group(1); body = body.replace(m4.group(0), '')
        _, secs = split_sections(body)
        rel = os.path.relpath(f, SRC).replace(os.sep, '/')
        chapters.append(dict(help=help_line, num=num, question=question, key=key, slug=f'{key.zfill(2) if "-" not in key else key.replace("-", "-")}-{slugify(question)}',
                             secs=secs, source=src, oneline=ONELINES.get(rel, ''), file=rel))
    for c in chapters:
        k = c['key']
        c['slug'] = (k.zfill(2) if '-' not in k else k.split('-')[0].zfill(2) + '-' + k.split('-')[1]) + '-' + slugify(c['question'])
    book['chapters'] = chapters

    ep = open(os.path.join(d, '99_epilogue.txt'), encoding='utf-8').read()
    ep_main = ep.split('\n---\n')[0]
    ep_title = re.search(r'^# (.+)$', ep_main, re.M).group(1)
    ep_body = ep_main.split('\n', 1)[1]
    ep_src = ''
    m3 = re.search(r'^> (.+)$', ep_body, re.M)
    if m3:
        ep_src = m3.group(1); ep_body = ep_body.replace(m3.group(0), '')
    book['epilogue'] = dict(title=ep_title, paras=paras(ep_body), source=ep_src)
    return book

# ---------- render ----------
def render_chapter(book, i):
    c = book['chapters'][i]
    n = len(book['chapters'])
    secs = c['secs']
    opening = secs[0]
    middle = [s for s in secs[1:] if s[0] != 'Where it would die']
    die = [s for s in secs if s[0] == 'Where it would die']
    oneline = c['oneline'] or middle[-1][1][-1]
    of_word = WORDS.get(n, str(n))

    here = ' class="here"'
    toc = ''.join(
        f'<li{here if j == i else ""}><span class="num">{esc(cc["num"])}</span>'
        f'<a href="/models/{book["slug"]}/{cc["slug"]}/">{esc(cc["question"])}</a></li>'
        for j, cc in enumerate(book['chapters']))
    sec_html = '\n'.join(details(h, ''.join(para_html(p) for p in ps)) for h, ps in middle)
    die_html = ''
    coda_html = ''
    if die:
        h, ps = die[0]
        # split at the stand line: switches stay in the drawer, the chapter's ending is shown open
        # the drawer holds everything up to the last switch (and a following "Fire one..." line); the rest is the chapter's ending
        cut = None
        for k, p in enumerate(ps):
            if KS_RE.match(p):
                cut = k
        if cut is not None and cut + 1 < len(ps) and ps[cut + 1].startswith('Fire one'):
            cut += 1
        drawer = ps if cut is None else ps[:cut + 1]
        coda = [] if cut is None else ps[cut + 1:]
        ids = [KS_RE.match(p).group(1) for p in ps if KS_RE.match(p)]
        nks = len(ids)
        reg_line = ''
        if ids:
            reg_line = (f'<p class="reg">Every switch above is filed, with its status, in the <a href="{REGISTRY}">registry</a>. '
                        f'The registry writes them {esc(ks_registry_form(ids[0]))} to {esc(ks_registry_form(ids[-1]))}. '
                        f'What a kill switch is: <a href="{WALL}">Where It Would Die</a>, on the wall.</p>')
        die_html = details(h, ''.join(para_html(p) for p in drawer) + reg_line,
                           cls='sec die', extra=f'<span class="count">{nks} switches</span>')
        if coda:
            coda_html = '<section class="coda">' + ''.join(para_html(p) for p in coda) + '</section>'
    src_html = esc(c['source']).replace(esc(book['title']), f'<a href="{book["original"]}">{esc(book["title"])}</a>', 1)
    crumb = f' · {esc(c["num"])}' if book['slug'] == 'resolutions' else f' · {esc(c["num"])} of {of_word}'
    prev_c = book['chapters'][i - 1] if i > 0 else None
    next_c = book['chapters'][i + 1] if i + 1 < n else None
    prev_html = (f'<a class="p" href="/models/{book["slug"]}/{prev_c["slug"]}/"><small>Previous</small>{esc(prev_c["question"])}</a>'
                 if prev_c else '')
    next_html = (f'<a class="r" href="/models/{book["slug"]}/{next_c["slug"]}/"><small>Next</small>{esc(next_c["question"])}</a>'
                 if next_c else f'<a class="r" href="/models/{book["slug"]}/epilogue/"><small>Next</small>{esc(book["epilogue"]["title"])}</a>')

    help_html = (f'<p class="help">{link_help(c["help"])}</p>\n' if c.get('help') else '')
    body = f'''{strap(book, crumb)}
<details class="toc"><summary>In this book</summary><ol>{toc}</ol></details>
<p class="eyebrow">Chapter {esc(c['num'])}</p>
<h1>{esc(c['question'])}</h1>
<p class="oneline">{esc(oneline)}</p>
{help_html}<section class="opening">
<h2>{esc(opening[0])}</h2>
{''.join(para_html(p) for p in opening[1])}
</section>
<div class="tools"><button type="button" data-collapse>Collapse all</button><button type="button" data-expand>Expand all</button></div>
{sec_html}
{die_html}
{coda_html}
<p class="source">{src_html}</p>
<nav class="pn">{prev_html}{up(book)}{next_html}</nav>'''
    return shell(c['question'], body, book, 2, blurb([oneline] + list(opening[1]) + [q for _h, _ps in middle for q in _ps]),
                 path=f'/models/{book["slug"]}/{c["slug"]}/')

def render_book(book):
    n = len(book['chapters'])
    rows = ''.join(
        f'<li><a href="/models/{book["slug"]}/{c["slug"]}/"><span class="num">{esc(c["num"])}</span>'
        f'<span class="q">{esc(c["question"])}</span><span class="line">{esc(c["oneline"])}</span></a></li>'
        for c in book['chapters'])
    front_html = ''
    order = {'The Axiom': 0, 'The words': 1}
    parts = sorted(book['front'], key=lambda p: order.get(p[0], 2))
    for head, pre, secs, cite in parts:
        inner = ''.join(para_html(p) for p in pre)
        for h, ps in secs:
            inner += f'<h3>{esc(h)}</h3>' + ''.join(para_html(p) for p in ps)
        if cite:
            inner += f'<p class="source">{esc(cite)}</p>'
        front_html += details(head, inner, open_=False)
    tagline = book['tagline'].replace('. The short edition', '').rstrip('.')
    body = f'''{strap(book, '')}
<p class="eyebrow">The 420 Code · Ø Models</p>
<h1 class="bt">{esc(book['title'])}</h1>
<p class="oneline">{esc(book['subtitle'])}. {esc(tagline)}.</p>
{STALE_PDF}<p class="edition">This is the short edition, {esc(book['edition'])}. It is a summary. The original is <a href="{book['original']}">here</a>. Go to it whenever this one moves too fast.</p>
{front_html}
<h2 class="lh">The chapters</h2>
<ol class="chapters">{rows}</ol>
<p class="ep"><a href="/models/{book["slug"]}/epilogue/">{esc(book['epilogue']['title'])}</a></p>
<p class="reg">Every kill switch in this book is filed in the <a href="{REGISTRY}">registry</a>. The book on the wall: <a href="/models/">Ø Models</a>.</p>
<nav class="pn solo">{up()}</nav>'''
    return shell(book['subtitle'], body, book, 1, blurb([f'{book["title"]} — {book["subtitle"]}. {tagline}.'] + [p for _h, _pre, _s, _c in parts for p in _pre]),
                 path=f'/models/{book["slug"]}/', book_first=True)

def render_epilogue(book):
    e = book['epilogue']
    last = book['chapters'][-1]
    body = f'''{strap(book, ' · Epilogue')}
<p class="eyebrow">Epilogue</p>
<h1>{esc(e['title'].partition(' — ')[2] or e['title'])}</h1>
<section class="opening">{''.join(para_html(p) for p in e['paras'])}</section>
<p class="source">{esc(e['source'])}</p>
<nav class="pn"><a class="p" href="/models/{book["slug"]}/{last["slug"]}/"><small>Previous</small>{esc(last["question"])}</a>{up(book)}</nav>'''
    return shell(e['title'], body, book, 2, blurb([f'{book["title"]} — {e["title"]}.'] + e['paras']),
                 path=f'/models/{book["slug"]}/epilogue/')

CSS = '''/* Ø Models reader — one stylesheet for every book and chapter. Colours and face are the site's. */
:root{--bg:#ffffff;--surface:#f3f3ed;--ink:#1a1a1a;--ink-2:#4a4a4a;--mute:#4a4a4a;--rule:#d5d5d0;--accent:#8B6914;--accent-ink:#6f5310;--bk:#111;--g1:#f3f3ed;--g3:#d5d5d0;--g5:#4a4a4a;--edge:#8a8a8a}
*{box-sizing:border-box}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Atkinson Hyperlegible",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:18px;line-height:1.65;padding:0}
.c{max-width:760px;margin:0 auto;padding:3rem 1.5rem 4rem}
@media (max-width:600px){.c{padding:2rem 1rem 3rem}}
a{color:var(--accent-ink)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.strap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:.6rem 1rem;padding-block:1rem;border-bottom:1px solid var(--rule);font-size:1rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.strap .book a{text-decoration:none;color:var(--ink)}
.modes{display:flex;flex-wrap:wrap;gap:.4rem;margin:0;padding:0;list-style:none}
.modes a,.modes span{display:inline-block;white-space:nowrap;padding:.3rem .7rem;border:1px solid var(--rule);border-radius:2px;text-decoration:none;color:var(--ink-2)}
.modes .on{border-color:var(--accent);color:var(--accent-ink)}
.eyebrow{font-size:1rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);margin:1.6rem 0 .5rem}
h1{font-weight:700;font-size:clamp(1.8rem,5.5vw,2.5rem);line-height:1.12;letter-spacing:-.01em;margin:0 0 1.2rem;text-wrap:balance}
h1.bt{font-size:clamp(2.4rem,8vw,3.2rem)}
.oneline{font-size:1.25rem;line-height:1.4;font-style:italic;color:var(--ink);border-left:2px solid var(--accent);padding-left:1rem;margin:0 0 1.2rem}
.edition{font-size:1rem;color:var(--ink-2);margin:0 0 2rem}
.opening{margin:0 0 .6rem}
.opening h2,h2.lh{font-weight:700;font-size:1.15rem;margin:0 0 .6rem}
h2.lh{margin:2.4rem 0 .8rem}
h3{font-weight:700;font-size:1rem;margin:1.2rem 0 .4rem}
p{margin:0 0 1rem;max-width:65ch}
details.sec{border-top:1px solid var(--rule)}
details.sec:last-of-type{border-bottom:1px solid var(--rule)}
details.sec summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:.7rem;padding:.9rem 0;font-size:1.15rem;font-weight:700;color:var(--ink)}
details.sec summary::-webkit-details-marker{display:none}
.tri{display:inline-block;width:1rem;color:var(--accent);font-size:1rem;line-height:1;transition:transform .18s ease;flex:none;transform-origin:40% 50%}
.tri::before{content:"\\25B8"}
details[open]>summary .tri{transform:rotate(90deg)}
@media (prefers-reduced-motion:reduce){.tri{transition:none}}
.sec-body{padding:.2rem 0 1rem 1.2rem}
.count{margin-left:auto;font-size:1rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);font-weight:400}
details.die summary{color:var(--accent-ink)}
.coda{margin:1.4rem 0 0}
.ks{padding-left:7rem;text-indent:-7rem}
.ks-id{display:inline-block;width:7rem;text-indent:0;font-size:1rem;letter-spacing:.04em;text-decoration:none;color:var(--accent-ink);font-variant-numeric:tabular-nums}
.ks-id:hover{text-decoration:underline}
.reg{font-size:1rem;color:var(--mute)}
.tools{display:flex;gap:1.2rem;justify-content:flex-start;padding:0 0 .8rem;font-size:1rem;letter-spacing:.06em;text-transform:uppercase}
.tools button{background:none;border:0;color:var(--ink-2);font:inherit;cursor:pointer;padding:0;letter-spacing:inherit;text-transform:inherit}
.tools button:hover{color:var(--accent-ink)}
.source{margin:1.6rem 0 0;font-size:1rem;color:var(--mute);font-style:italic}
.source a{color:inherit}
nav.pn{display:grid;grid-template-columns:1fr auto 1fr;gap:1.2rem 1.5rem;align-items:start;margin-top:2.4rem;padding-top:1rem;border-top:1px solid var(--rule);font-size:1rem}
nav.pn a{text-decoration:none}
nav.pn a.p{grid-column:1}
nav.pn .up{grid-column:2;text-align:center}
nav.pn .up a{display:block}
nav.pn a.r{grid-column:3;text-align:right}
@media (max-width:600px){nav.pn{grid-template-columns:1fr 1fr}nav.pn a.r{grid-column:2}nav.pn .up{grid-column:1/-1;grid-row:2}nav.pn.solo .up{grid-row:1}}
nav.pn small{display:block;font-size:1rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}
details.toc{margin:1.2rem 0 0;font-size:1rem}
details.toc summary{cursor:pointer;color:var(--ink-2);letter-spacing:.06em;text-transform:uppercase;font-size:1rem}
details.toc ol{list-style:none;margin:.6rem 0 0;padding:0;columns:2;column-gap:2rem}
details.toc li{display:flex;gap:.6rem;padding:.2rem 0;break-inside:avoid;color:var(--ink-2)}
details.toc li a{color:inherit;text-decoration:none}
details.toc li.here a{color:var(--accent-ink)}
details.toc .num{width:6.2rem;color:var(--mute);flex:none;font-size:1rem;letter-spacing:.06em;text-transform:uppercase;padding-top:.15rem}
ol.chapters{list-style:none;margin:0;padding:0}
ol.chapters li{border-top:1px solid var(--rule)}
ol.chapters li:last-child{border-bottom:1px solid var(--rule)}
ol.chapters a{display:grid;grid-template-columns:6.8rem 1fr;gap:.2rem 1rem;padding:1rem 0;text-decoration:none;color:var(--ink)}
ol.chapters .num{grid-row:span 2;font-size:1rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);padding-top:.35rem}
ol.chapters .q{font-size:1.2rem;font-weight:700;line-height:1.2}
ol.chapters .line{font-size:1rem;color:var(--ink-2);font-style:italic}
ol.chapters a:hover .q{color:var(--accent-ink)}
.ep{margin:1.2rem 0}
.ep a{font-size:1.1rem;font-weight:700;text-decoration:none}
footer.colophon{margin-top:3rem;font-size:1rem;color:var(--mute);letter-spacing:.03em}
footer.colophon a{color:var(--ink-2);text-decoration:none}
footer.colophon .editions{font-size:1rem;color:var(--ink);border-top:1px solid var(--rule);padding-top:1rem;margin-bottom:.8rem}
footer.colophon .editions a{color:var(--accent-ink);text-decoration:underline}
/* The site's footer, as on every page of the420code.org. Measured on /models/, 22 September 2026. */
.constraint{margin:2rem 0;padding:1.5rem 0;color:#1a1a1a}
.constraint p{font-size:16px;line-height:1.65;margin:0 0 .25rem;max-width:none}
.oneness{font-size:19px;font-weight:700;text-align:center;line-height:1.5;margin:3.5rem 0 1rem;max-width:none;color:#1a1a1a}
.footer{margin:4rem 0 0;padding:2rem 0 0;font-size:16px;line-height:1.65;color:#4a4a4a;border-top:1px solid #e8e8e8}
.footer p{margin:0 0 .25rem;max-width:none}
@media (max-width:700px){.oneness{font-size:18px}}
@media (max-width:520px){details.toc ol{columns:1}.ks{padding-left:0;text-indent:0}.ks-id{display:block;width:auto}ol.chapters a{grid-template-columns:1fr}ol.chapters .num{grid-row:auto}}
'''

CSS += H.BASE_CSS + '\n' + H.CSS + '\n'

JS = '''(function(){
  var all=document.querySelectorAll('details.sec');
  var ex=document.querySelector('[data-expand]'),co=document.querySelector('[data-collapse]');
  if(ex)ex.addEventListener('click',function(){all.forEach(function(d){d.open=true})});
  if(co)co.addEventListener('click',function(){all.forEach(function(d){d.open=false})});
  // a link to #section-or-switch opens the section that holds it
  function reveal(){var h=location.hash&&document.getElementById(location.hash.slice(1));if(!h)return;var d=h.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details')}h.scrollIntoView()}
  window.addEventListener('hashchange',reveal);reveal();
})();
// Counted as on every page of the site: one visit per browser session (a reload does not count
// again), and every click on a PDF, by its file name.
(function(){
  try{
    if(!sessionStorage.getItem('v420')){
      sessionStorage.setItem('v420','1');
      fetch('/.netlify/functions/visit-counter',{method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({path:location.pathname})}).catch(function(){});
    }
  }catch(e){/* private windows and blocked storage: skip the count, never break the page */}
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href$=".pdf"]');
    if(!a)return;
    fetch('/.netlify/functions/download-counter',{method:'POST',keepalive:true,headers:{'Content-Type':'application/json'},
      body:JSON.stringify({file:a.getAttribute('href').split('/').pop()})}).catch(function(){});
  },true);
})();
'''

def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, 'reader.css'), 'w', encoding='utf-8', newline='\n').write(CSS)
    open(os.path.join(OUT, 'reader.js'), 'w', encoding='utf-8', newline='\n').write(JS)
    snippet = []
    total_pages = 0
    for book in BOOKS:
        load_book(book)
        bd = os.path.join(OUT, book['slug'])
        os.makedirs(bd, exist_ok=True)
        open(os.path.join(bd, 'index.html'), 'w', encoding='utf-8', newline='\n').write(check(render_book(book), book['slug']))
        total_pages += 1
        for i, c in enumerate(book['chapters']):
            cd = os.path.join(bd, c['slug'])
            os.makedirs(cd, exist_ok=True)
            open(os.path.join(cd, 'index.html'), 'w', encoding='utf-8', newline='\n').write(check(render_chapter(book, i), c['slug']))
            total_pages += 1
        ed = os.path.join(bd, 'epilogue')
        os.makedirs(ed, exist_ok=True)
        open(os.path.join(ed, 'index.html'), 'w', encoding='utf-8', newline='\n').write(check(render_epilogue(book), book['slug'] + '/epilogue'))
        total_pages += 1
        snippet.append(f'''<!-- {book["title"]} — under the cat-desc paragraph of its cat-section on /models/ -->
<p><a class="nb-pdf" href="/models/{book["slug"]}/">Read online</a> <a class="nb-pdf" href="{book["pdf"]}">Download the short edition (PDF)</a> <a class="nb-pdf" href="{book["original"]}">Download the original (PDF)</a></p>''')
        print(book['title'], len(book['chapters']), 'chapters', [c['slug'] for c in book['chapters']][:2], '…')
    snippet.append('''<!-- Ø Predictions — no short edition; it is a table and derivations, not chapters -->
<p><a class="nb-pdf" href="/prereg/">Read the predictions page</a> <a class="nb-pdf" href="/Predictions.pdf">Download the original (PDF)</a></p>''')
    open(os.path.join(OUT, 'models-snippet.html'), 'w', encoding='utf-8', newline='\n').write('\n\n'.join(snippet) + '\n')
    print('pages:', total_pages)

if __name__ == '__main__':
    main()
