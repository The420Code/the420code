#!/usr/bin/env python3
"""Build the Five Doors online library: static HTML for Netlify.

Input:  ../<book>/00_front.txt, ../<book>/ch*.txt, ../<book>/99_epilogue.txt, onelines_*.json
Output: site/five-doors/<book>/index.html, site/five-doors/<book>/<slug>/index.html, .../epilogue/index.html,
        site/five-doors/reader.css, site/five-doors/reader.js, site/five-doors/five-doors-snippet.html

The stylesheet and the script are the Ø Models library's own files, copied: one object serves both
libraries, so the 16px floor, the site's greys, the header's rules and the counters cannot drift apart.

Every chapter page has the same structure:
  strap · question · one line · opening · sections (closed) · where it would die (closed, IDs link to the registry) · source · prev/next
"""
import re, os, sys, json, html, glob, shutil
sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, '..')
OUT = os.path.join(ROOT, 'site', 'five-doors')
REGISTRY = 'https://the420code.org/killswitches/'
WALL = 'https://the420code.org/what-is-the-420-code/#where-it-would-die'

SITE = 'https://the420code.org'

# The site's header, as every English-only room has it (WC/tools/room_shell.py): built by the site's own
# header.py, with the rooms block taken verbatim from the English front door. After any change to the
# menu, rebuild this library too.
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'i18n', 'frontdoor'))
import header as H  # noqa: E402
_door = open(os.path.join(REPO, 'what-is-the-420-code', 'index.html'), encoding='utf-8').read()
_i = _door.index('  <div class="nav-menu">')
ROOMS_MENU = _door[_i:_door.index('  </div>', _i) + len('  </div>')]
assert _door.count('  <div class="nav-menu">') == 1 and ROOMS_MENU.count('class="nav-room"') == 17, 'the front door\'s rooms block'
BOOKS = [
    dict(slug='illusion', src='illusion', title='The Illusion of the Other', door='the gentle door',
         pdf=None, original='/Illusion_of_the_Other.pdf', edition=None, epilogue_file=None),
    dict(slug='being-after-religion', src='bar', title='Being After Religion', door='the front door',
         pdf='/five-doors/being-after-religion.pdf', original='/Being_After_Religion.pdf', edition='v1.1'),
    dict(slug='antichristos', src='antichristos', title='Antichristos', door='the sacred door',
         pdf='/five-doors/antichristos.pdf', original='/Antichristos.pdf', edition='v1.1'),
    dict(slug='relationship-corridor', src='corridor', title='The Relationship Corridor', door='the personal door',
         pdf='/five-doors/relationship-corridor.pdf', original='/The_Relationship_Corridor.pdf', edition='v1.1'),
]
WORDS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
         10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
         16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen'}

ONELINES = {}
for f in glob.glob(os.path.join(ROOT, 'onelines_*.json')):
    ONELINES.update(json.load(open(f, encoding='utf-8')))

KS_RE = re.compile(r'^(KS-[A-Z]+\.[\d]+[a-z]?) — (.*)$', re.S)

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
    # registry anchors: KS-AC.1 -> #ks-ac-1 ; KS-BAR.9 -> #ks-bar-9
    return sid.lower().replace('.', '-')

def ks_anchor(sid):
    return REGISTRY + '#' + ks_id(sid)

def ks_registry_form(sid):
    return sid

def para_html(p):
    m = KS_RE.match(p)
    if m:
        sid, rest = m.group(1), m.group(2)
        return (f'<p class="ks" id="{ks_id(sid)}"><a class="ks-id" href="{ks_anchor(sid)}" '
                f'title="This switch in the registry">{esc(sid)}</a>{esc(rest)}</p>')
    h = esc(p)
    h = re.sub(r'the420code\.org/([a-z0-9-]+)/?', r'<a href="https://the420code.org/\1/">the420code.org/\1/</a>', h)
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

# ---------- page shell ----------
def editions_line(book):
    if book.get('pdf'):
        return (f'This is the short edition of {esc(book["title"])} — a summary. Where a step is compressed here, '
                f'the original carries it in full. <a href="{book["original"]}">The original book (PDF)</a> · '
                f'<a href="{book["pdf"]}">This edition (PDF)</a> · '
                f'<a href="/five-doors/{book["slug"]}/">Read this edition online</a>')
    return (f'{esc(book["title"])} has no short edition. Its chapters are already at the short edition’s length, '
            f'and every word in them is the argument, so what you are reading is the book itself. '
            f'<a href="{book["original"]}">The original book (PDF)</a> · '
            f'<a href="/five-doors/{book["slug"]}/">Read it online</a>')


def shell(title, body, book, depth, description='', path='/', book_first=False):
    rel = '../' * depth
    full_title = (f'{book["title"]} — {title} — The 420 Code' if book_first else f'{title} — {book["title"]} — The 420 Code')
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
<title>{esc(full_title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<link rel="stylesheet" href="{rel}reader.css">
<link rel="apple-touch-icon" href="/Eye_of_the_Universe.jpg">
<link rel="icon" type="image/jpeg" href="/Eye_of_the_Universe.jpg">
</head>
<body>
<div class="c">
{H.english_header(ROOMS_MENU, "en-only", path)}
{body}
<footer class="colophon">
<p class="editions">{editions_line(book)}</p>
<p><a href="https://the420code.org/">The 420 Code</a> · <a href="/five-doors/">Ø Five Doors</a> · {esc(book["title"])}</p>
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
    dl = f'<a href="{book["pdf"]}">Download</a>' if book.get('pdf') else f'<a href="{book["original"]}">Download</a>'
    kind = 'the short edition' if book.get('pdf') else 'read in full'
    return (f'<header class="strap"><div class="book"><a href="/five-doors/{book["slug"]}/"><b>{esc(book["title"])}</b></a>'
            f' · {kind}{crumb}</div>'
            f'<ul class="modes"><li><span class="on">Read</span></li>'
            f'<li>{dl}</li></ul></header>')

# ---------- parse a book ----------
def load_book(book):
    d = os.path.join(SRC, book['src'])
    fp = os.path.join(d, '00_front.txt')
    if not os.path.exists(fp):
        book['subtitle'] = book['title']
        book['tagline'] = book['door']
        book['front'] = []
    else:
        front = open(fp, encoding='utf-8').read()
        tl = [l[2:].strip() for l in front.splitlines() if l.startswith('~ ')]
        book['subtitle'] = tl[1]
        book['tagline'] = tl[2]
        parts = re.split(r'^# ', front.split('\n---\n', 1)[1] if '\n---\n' in front else front, flags=re.M)
        front_parts = []
        for chunk in parts[1:]:
            head, _, rest = chunk.partition('\n')
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
        pre, secs = split_sections(body)
        if pre:
            secs = [('', pre)] + secs
        rel = os.path.relpath(f, SRC).replace(os.sep, '/')
        chapters.append(dict(num=num, question=question, key=key, slug=f'{key.zfill(2) if "-" not in key else key.replace("-", "-")}-{slugify(question)}',
                             secs=secs, source=src, oneline=ONELINES.get(rel, ''), file=rel))
    for c in chapters:
        k = c['key']
        c['slug'] = (k.zfill(2) if '-' not in k else k.split('-')[0].zfill(2) + '-' + k.split('-')[1]) + '-' + slugify(c['question'])
    book['chapters'] = chapters

    epp = os.path.join(d, '99_epilogue.txt')
    if not os.path.exists(epp):
        book['epilogue'] = None
        return book
    ep = open(epp, encoding='utf-8').read()
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
def up(book=None):
    """The way back, on every page, between Previous and Next: the book's contents and Ø Five Doors."""
    to_book = f'<a href="/five-doors/{book["slug"]}/">{esc(book["title"])}</a>' if book else ''
    return f'<div class="up"><small>Back to</small>{to_book}<a href="/five-doors/">Ø Five Doors</a></div>'


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
        f'<a href="/five-doors/{book["slug"]}/{cc["slug"]}/">{esc(cc["question"])}</a></li>'
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
            which = (f'The registry writes it {esc(ids[0])}.' if len(ids) == 1
                     else f'The registry writes them {esc(ids[0])} to {esc(ids[-1])}.')
            reg_line = (f'<p class="reg">Every switch above is filed, with its status, in the <a href="{REGISTRY}">registry</a>. '
                        f'{which} '
                        f'What a kill switch is: <a href="{WALL}">Where It Would Die</a>, on the wall.</p>')
        die_html = details(h, ''.join(para_html(p) for p in drawer) + reg_line,
                           cls='sec die', extra=f'<span class="count">{nks} switch{"es" if nks != 1 else ""}</span>')
        if coda:
            coda_html = '<section class="coda">' + ''.join(para_html(p) for p in coda) + '</section>'
    src_html = esc(c['source']).replace(esc(book['title']), f'<a href="{book["original"]}">{esc(book["title"])}</a>', 1)
    crumb = f' · {esc(c["num"])} of {of_word}'
    prev_c = book['chapters'][i - 1] if i > 0 else None
    next_c = book['chapters'][i + 1] if i + 1 < n else None
    prev_html = (f'<a class="p" href="/five-doors/{book["slug"]}/{prev_c["slug"]}/"><small>Previous</small>{esc(prev_c["question"])}</a>'
                 if prev_c else '')
    next_html = (f'<a class="r" href="/five-doors/{book["slug"]}/{next_c["slug"]}/"><small>Next</small>{esc(next_c["question"])}</a>'
                 if next_c else (f'<a class="r" href="/five-doors/{book["slug"]}/epilogue/"><small>Next</small>{esc(book["epilogue"]["title"])}</a>' if book["epilogue"] else ''))

    body = f'''{strap(book, crumb)}
<details class="toc"><summary>In this book</summary><ol>{toc}</ol></details>
<p class="eyebrow">Chapter {esc(c['num'])}</p>
<h1>{esc(c['question'])}</h1>
<p class="oneline">{esc(oneline)}</p>
<section class="opening">
{('<h2>' + esc(opening[0]) + '</h2>') if opening[0] else ''}
{''.join(para_html(p) for p in opening[1])}
</section>
<div class="tools"><button type="button" data-collapse>Collapse all</button><button type="button" data-expand>Expand all</button></div>
{sec_html}
{die_html}
{coda_html}
<p class="source">{src_html}</p>
<nav class="pn">{prev_html}{up(book)}{next_html}</nav>'''
    return shell(c['question'], body, book, 2, oneline, path=f'/five-doors/{book["slug"]}/{c["slug"]}/')

def render_book(book):
    n = len(book['chapters'])
    rows = ''.join(
        f'<li><a href="/five-doors/{book["slug"]}/{c["slug"]}/"><span class="num">{esc(c["num"])}</span>'
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
    if book.get('edition'):
        ed = (f'<p class="edition">This is the short edition, {esc(book["edition"])}. It is a summary. '
              f'The original is <a href="{book["original"]}">here</a>. Go to it whenever this one moves too fast.</p>')
    else:
        ed = (f'<p class="edition">This book has no short edition. Its chapters are already at the short edition’s '
              f'length, and every word in them is the argument, so what you read here is the book itself. '
              f'The printed original is <a href="{book["original"]}">here</a>.</p>')
    ep = (f'<p class="ep"><a href="/five-doors/{book["slug"]}/epilogue/">{esc(book["epilogue"]["title"])}</a></p>'
          if book['epilogue'] else '')
    has_ks = any(KS_RE.match(p) for c in book['chapters'] for _h, ps in c['secs'] for p in ps)
    if has_ks:
        reg = (f'<p class="reg">Every kill switch in this book is filed in the '
               f'<a href="{REGISTRY}">registry</a>. '
               f'The five books: <a href="/five-doors/">The Five Doors</a>.</p>')
    else:
        reg = (f'<p class="reg">This book carries no switches of its own; the claims it makes are fenced in the '
               f'companion volumes and filed in the <a href="{REGISTRY}">registry</a>. '
               f'The five books: <a href="/five-doors/">The Five Doors</a>.</p>')
    body = f'''{strap(book, '')}
<p class="eyebrow">The 420 Code · The Five Doors · {esc(book['door'])}</p>
<h1 class="bt">{esc(book['title'])}</h1>
<p class="oneline">{esc(book['subtitle'])}. {esc(tagline)}.</p>
{ed}
{front_html}
<h2 class="lh">The chapters</h2>
<ol class="chapters">{rows}</ol>
{ep}
{reg}
<nav class="pn solo">{up()}</nav>'''
    return shell(book['subtitle'], body, book, 1, f'{book["title"]} — {book["subtitle"]}. Read online.', path=f'/five-doors/{book["slug"]}/', book_first=True)

def render_epilogue(book):
    e = book['epilogue']
    last = book['chapters'][-1]
    body = f'''{strap(book, ' · Epilogue')}
<p class="eyebrow">Epilogue</p>
<h1>{esc(e['title'].partition(' — ')[2] or e['title'])}</h1>
<section class="opening">{''.join(para_html(p) for p in e['paras'])}</section>
<p class="source">{esc(e['source'])}</p>
<nav class="pn"><a class="p" href="/five-doors/{book["slug"]}/{last["slug"]}/"><small>Previous</small>{esc(last["question"])}</a>{up(book)}</nav>'''
    return shell(e['title'], body, book, 2, f'{book["title"]} — {e["title"]}', path=f'/five-doors/{book["slug"]}/epilogue/')

# One stylesheet and one script for both libraries, as the bundle's INSTALL asks ("serve one copy for
# both"): the Ø Models files, which carry the 16px floor, the site's greys, the header's rules and the
# visit and download counters. Read here so a patch to one can never leave the other behind.
CSS = open(os.path.join(REPO, 'models', 'reader.css'), encoding='utf-8').read()
JS = open(os.path.join(REPO, 'models', 'reader.js'), encoding='utf-8').read()
assert '.c{max-width:760px' in CSS and H.BASE_CSS in CSS and 'visit-counter' in JS, 'the Ø Models stylesheet or script is not the patched one'

# One stylesheet and one script for both libraries, as the bundle's INSTALL asks ("serve one copy for
# both"): the Ø Models files, which carry the 16px floor, the site's greys, the header's rules and the
# visit and download counters. Read here so a patch to one can never leave the other behind.
CSS = open(os.path.join(REPO, 'models', 'reader.css'), encoding='utf-8').read()
JS = open(os.path.join(REPO, 'models', 'reader.js'), encoding='utf-8').read()
assert '.c{max-width:760px' in CSS and H.BASE_CSS in CSS and 'visit-counter' in JS, 'the Ø Models stylesheet or script is not the patched one'


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
        open(os.path.join(bd, 'index.html'), 'w', encoding='utf-8', newline='\n').write(render_book(book))
        total_pages += 1
        for i, c in enumerate(book['chapters']):
            cd = os.path.join(bd, c['slug'])
            os.makedirs(cd, exist_ok=True)
            open(os.path.join(cd, 'index.html'), 'w', encoding='utf-8', newline='\n').write(render_chapter(book, i))
            total_pages += 1
        if book['epilogue']:
            ed = os.path.join(bd, 'epilogue')
            os.makedirs(ed, exist_ok=True)
            open(os.path.join(ed, 'index.html'), 'w', encoding='utf-8', newline='\n').write(render_epilogue(book))
            total_pages += 1
        if book.get('pdf'):
            snippet.append(f'''<!-- {book["title"]} — under its paragraph on the Five Doors page -->
<p><a class="nb-pdf" href="/five-doors/{book["slug"]}/">Read online</a> <a class="nb-pdf" href="{book["pdf"]}">Download the short edition (PDF)</a> <a class="nb-pdf" href="{book["original"]}">Download the original (PDF)</a></p>''')
        else:
            snippet.append(f'''<!-- {book["title"]} — no short edition; the chapters are the book -->
<p><a class="nb-pdf" href="/five-doors/{book["slug"]}/">Read online</a> <a class="nb-pdf" href="{book["original"]}">Download the original (PDF)</a></p>''')
        print(book['title'], len(book['chapters']), 'chapters', [c['slug'] for c in book['chapters']][:2], '…')
    open(os.path.join(OUT, 'five-doors-snippet.html'), 'w', encoding='utf-8', newline='\n').write('\n\n'.join(snippet) + '\n')
    print('pages:', total_pages)

if __name__ == '__main__':
    main()
