# -*- coding: utf-8 -*-
"""Build /xx/what-is-the-420-code/ for the twelve editions, mechanically, from the
corrected string tables -- and give each edition's home page the same drop-down
header as its front door, because G ruled the two menus identical.

The English front door is the template, so structure, type, links, anchors and
the axiom line are the same object in every edition. Each translated value is
placed by position -- the same element walk that extracted the English -- never by
searching for English text, which repeats on the page.

Links: every edition has its own #axiom, #physics, #models, #five-doors and
#confirm-the-math, so those stay inside the reader's language. The per-paper
anchors and the Notebooks list exist only in English, so those stay pointed there.
Arabic is set right-to-left, with its technical runs isolated."""
import sys, io, os, re, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lang_entrance import L as ENTRANCE

REPO  = os.path.abspath(os.path.join(HERE, "..", ".."))
FINAL = HERE
LANGS = ["ar","de","es","fr","hi","it","ja","ko","nl","pt","ru","zh"]
LOCAL_ROOMS = ("axiom", "physics", "models", "five-doors", "confirm-the-math")

TEMPLATE = io.open(os.path.join(REPO, "what-is-the-420-code", "index.html"), encoding="utf-8").read()
EN_HOME  = io.open(os.path.join(REPO, "index.html"), encoding="utf-8").read()
EN = json.load(open(os.path.join(FINAL, "frontdoor_strings_en.json"), encoding="utf-8"))["strings"]

slug = lambda s: re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")

# ── the drop-down header, as the English pages carry it ─────────────────────
DROPDOWN_CSS = re.search(r"\n/\* ── the header: one row, with the rooms behind a drop-down.*?\n\}\n",
                         EN_HOME, re.S).group(0)
DOOR_CSS = ".nav a.nav-door{font-weight:700;color:#1a1a1a}\n.nav a.nav-door:hover{color:#8B6914}\n"
CLOSE_JS = re.search(r'<script id="nav-menu-close">.*?</script>', EN_HOME, re.S).group(0)
RTL_CSS = """
[dir="rtl"] .nav-toggle{margin-left:0;margin-right:auto}
[dir="rtl"] .nav-menu{right:auto;left:0}
[dir="rtl"] .fd ol.chain li{padding:0 2.6rem 1.1rem 0}
[dir="rtl"] .fd ol.chain li::before{left:auto;right:0}
[dir="rtl"] .fd blockquote{padding:0 1.25rem 0 0;border-left:none;border-right:3px solid #8B6914}
[dir="rtl"] .fd .axiom{direction:ltr}
bdi{unicode-bidi:isolate}
"""

def edition_nav(lang, home, door):
    """The edition's rooms, read from its original header where a pre-change
    snapshot sits beside this script, otherwise from the header on the page.

    A header already turned into a drop-down is read back by its nav-room links,
    and only by them. The earlier version tried the flat-menu pattern first; on a
    rebuilt header that matched the Predictions link alone, one match looked like
    success, and the header came back with one room instead of five."""
    nav = re.search(r'<nav class="nav">(.*?)</nav>', home, re.S).group(1)
    snap = os.path.join(HERE, f"pre_fix_{lang}.html")
    src_nav = (re.search(r'<nav class="nav">(.*?)</nav>', io.open(snap, encoding="utf-8").read(), re.S).group(1)
               if os.path.exists(snap) else nav)
    logo = re.search(r'<a [^>]*href="([^"]+)"[^>]*>\s*(<img [^>]*>)\s*</a>', nav)
    img = re.sub(r'src="(?:\.\./)?([^"/][^"]*)"', r'src="/\1"', logo.group(2))
    built = re.findall(r'<a href="([^"]+)" class="nav-room">([^<]+)</a>', src_nav)
    rooms = built or [(h, x) for h, x in
                      re.findall(r'<a (?:class="[^"]*" )?href="([^"]+)"[^>]*>([^<]+)</a>', src_nav)
                      if h.startswith("#") or h.startswith("/prereg")]
    assert len(rooms) == 5, f"{lang}: expected five rooms in the header, read {len(rooms)}"
    flags = re.search(r'<div class="lang-sel".*?</div>', nav, re.S).group(0)
    room_links = "\n    ".join(
        f'<a href="{("/" + lang + "/" + h) if h.startswith("#") else h}" class="nav-room">{x}</a>'
        for h, x in rooms)
    label = ENTRANCE[lang]["rooms"]
    return (f'<nav class="nav">\n'
            f'  <a href="/{lang}/" class="nav-logo">{img}</a>\n'
            f'  <a href="/{lang}/what-is-the-420-code/" class="nav-door">{door}</a>\n'
            f'  <button class="nav-toggle" aria-expanded="false" aria-label="{label}" '
            f"onclick=\"var n=this.closest('.nav');n.classList.toggle('open');"
            f"this.setAttribute('aria-expanded',n.classList.contains('open'))\">{label}</button>\n"
            f'  <div class="nav-menu">\n    {room_links}\n    {flags}\n  </div>\n'
            f'</nav>'), len(rooms)

def rebuild_fd(fd, tr):
    """Place every translated value by position, mirroring the extraction walk."""
    for key, pat in (("pre", r'(<p class="fd-pre">)(.*?)(</p>)'), ("h1", r"(<h1>)(.*?)(</h1>)"),
                     ("strap", r'(<p class="fd-strap">)(.*?)(</p>)'),
                     ("strap_land", r'(<p class="fd-strap-land">)(.*?)(</p>)')):
        fd, n = re.subn(pat, lambda m: m.group(1) + tr[key] + m.group(3), fd, count=1, flags=re.S)
        assert n == 1, key
    head, *secs = re.split(r"(?=<h2>)", fd)
    out = [head]
    for sec in secs:
        s = slug(re.match(r"<h2>(.*?)</h2>", sec, re.S).group(1))
        sec = re.sub(r"(<h2>)(.*?)(</h2>)", lambda m: m.group(1) + tr[f"h2.{s}"] + m.group(3),
                     sec, count=1, flags=re.S)
        ctr = {"i": 0}
        def para(m):
            i = ctr["i"]; ctr["i"] += 1
            key = f"src.{s}" if m.group(2) == "src" else f"p.{s}.{i}"
            return m.group(1) + tr[key] + "</p>"
        sec = re.sub(r'(<p(?: class="(land|src)")?>)(?:.*?)</p>', para, sec, flags=re.S)
        sec = re.sub(r"(<blockquote>)(.*?)(</blockquote>)",
                     lambda m: m.group(1) + tr[f"quote.{s}"] + m.group(3), sec, flags=re.S)
        li = {"n": 0}
        def item(m):
            li["n"] += 1
            return m.group(1) + tr[f"chain.{li['n']}"] + m.group(3)
        sec = re.sub(r"(<li>)(.*?)(</li>)", item, sec, flags=re.S)
        out.append(sec)
    fd = "".join(out)
    fd, n = re.subn(r'(<p class="fd-take"><a[^>]*>)(.*?)(</a></p>)',
                    lambda m: m.group(1) + tr["take"] + m.group(3), fd, count=1, flags=re.S)
    assert n == 1, "take"
    return fd

TECH = re.compile("(" + "|".join([
    r"\d{4}-\d{2}-\d{2}", r"\bv\d+\.\d+(?:\.\d+)?\b", r"\bAP\d{2}\b", r"\bKS[-\u2011][A-Za-z0-9.]+",
    r"\bSU\(\d\)(?:\s*×\s*SU\(\d\))*(?:\s*×\s*U\(\d\))?",
    r"\d+(?:\.\d+)?\s*[+\-−×/]\s*[A-Za-zα-ω0-9][A-Za-z0-9α-ω.]*", r"\b\d+/\d+\b"]) + ")")

def isolate(html):
    """Isolate technical runs for right-to-left pages. The axiom paragraph is left
    exactly as written: it stands alone in its block, is set LTR by its own rule,
    and must match every other page character for character."""
    keep = []
    def stash(m):
        keep.append(m.group(0)); return chr(0xE000) + str(len(keep) - 1) + chr(0xE001)
    html = re.sub(r'<p class="axiom">.*?</p>', stash, html, flags=re.S)
    parts = re.split(r"(<[^>]+>)", html)
    for i, seg in enumerate(parts):
        if not seg.startswith("<") and seg.strip():
            parts[i] = TECH.sub(lambda m: f'<bdi dir="ltr">{m.group(0)}</bdi>', seg)
    return re.sub(chr(0xE000) + r"(\d+)" + chr(0xE001), lambda m: keep[int(m.group(1))], "".join(parts))

def absolute_imgs(s):
    return re.sub(r'src="\.\./', 'src="/', s)

report = []
for lang in LANGS:
    tr = json.load(open(os.path.join(FINAL, f"frontdoor_strings_{lang}.json"), encoding="utf-8"))["strings"]
    home_p = os.path.join(REPO, lang, "index.html")
    home = io.open(home_p, encoding="utf-8").read()
    door = tr["h1"]
    rtl = lang == "ar"

    # ── the shared header ────────────────────────────────────────────────────
    nav_html, n_rooms = edition_nav(lang, home, door)

    # ── the front door ───────────────────────────────────────────────────────
    t = TEMPLATE
    t = re.sub(r"<html[^>]*>", f'<html lang="{lang}" dir="{"rtl" if rtl else "ltr"}">', t, count=1)
    plain = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
    desc = plain(tr["strap"] + " " + tr["strap_land"])
    t = re.sub(r"<title>[^<]*</title>", f"<title>the 420 code — {plain(door)}</title>", t, count=1)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        t = re.sub(rf'(<meta {attr} content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), t, count=1)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        t = re.sub(rf'(<meta {attr} content=")[^"]*(")',
                   lambda m: m.group(1) + f"{plain(door)} — the 420 code" + m.group(2), t, count=1)
    url = f"https://the420code.org/{lang}/what-is-the-420-code/"
    t = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), t, count=1)
    t = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), t, count=1)
    t = re.sub(r'<nav class="nav">.*?</nav>', lambda m: nav_html, t, count=1, flags=re.S)

    a = t.index('<div class="fd">'); b = t.index("</div>", a)
    assert "<div" not in t[a + 5:b], "a div nested inside .fd"
    fd = rebuild_fd(t[a:b], tr)
    for room in LOCAL_ROOMS:
        fd = fd.replace(f'href="/#{room}"', f'href="/{lang}/#{room}"')
    if rtl:
        fd = isolate(fd)
    t = t[:a] + fd + t[b:]

    about = re.search(r'<div class="constraint" id="about">.*?</div>', home, re.S).group(0)
    about = re.sub(r'\n\s*<p [^>]*><span id="dl-count">\d*</span>[^<]*</p>', "", about)
    footer = re.search(r'<div class="footer">.*?</div>', home, re.S).group(0)
    t = re.sub(r'<div class="constraint" id="about">.*?</div>', lambda m: about, t, count=1, flags=re.S)
    t = re.sub(r'<p class="oneness">.*?</p>', lambda m: f'<p class="oneness">{tr["close"]}</p>', t, count=1, flags=re.S)
    t = re.sub(r'<div class="footer">.*?</div>', lambda m: footer, t, count=1, flags=re.S)
    t = absolute_imgs(t)
    if rtl:
        i = t.rindex("</style>"); t = t[:i] + RTL_CSS + t[i:]
    os.makedirs(os.path.join(REPO, lang, "what-is-the-420-code"), exist_ok=True)
    io.open(os.path.join(REPO, lang, "what-is-the-420-code", "index.html"), "w",
            encoding="utf-8", newline="\n").write(t)

    # ── the edition's home page: same header, door link flipped home ─────────
    home = re.sub(r'<nav class="nav">.*?</nav>', lambda m: nav_html, home, count=1, flags=re.S)
    home = re.sub(r'(<p class="opening-link"><a href=")[^"]*(">)[^<]*(</a></p>)',
                  lambda m: m.group(1) + f"/{lang}/what-is-the-420-code/" + m.group(2)
                  + door + " " + ENTRANCE[lang]["arrow"] + m.group(3), home, count=1)
    if "the header: one row, with the rooms behind a drop-down" not in home:
        i = home.rindex("</style>"); home = home[:i] + DROPDOWN_CSS + DOOR_CSS + home[i:]
    if rtl and '[dir="rtl"] .nav-toggle' not in home:
        i = home.rindex("</style>"); home = home[:i] + RTL_CSS + home[i:]
    if 'id="nav-menu-close"' not in home:
        home = home.replace("</body>", CLOSE_JS + "\n</body>", 1)
    io.open(home_p, "w", encoding="utf-8", newline="\n").write(home)

    # ── round-trip: every translated value is on the page; no English one is ──
    built = io.open(os.path.join(REPO, lang, "what-is-the-420-code", "index.html"), encoding="utf-8").read()
    fdb = built[built.index('<div class="fd">'):built.index("</div>", built.index('<div class="fd">'))]
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"</?bdi[^>]*>", "", s))
    placed = sum(1 for k, v in tr.items() if k != "close" and
                 norm(re.sub(r'href="/#(' + "|".join(LOCAL_ROOMS) + r')"', rf'href="/{lang}/#\1"', v)) in norm(fdb))
    left = [k for k, v in EN.items() if k not in ("close",) and v != tr.get(k) and len(v) > 12 and v in fdb]
    report.append((lang, n_rooms, placed, len(tr) - 1, left))

print(f"{'lang':5s}{'rooms':>6s}{'placed':>9s}  english left on the page")
for lang, nr, placed, total, left in report:
    print(f"{lang:5s}{nr:6d}{placed:5d}/{total:<3d}  {left or 'none'}")
