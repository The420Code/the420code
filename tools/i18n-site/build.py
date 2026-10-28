# -*- coding: utf-8 -*-
"""Write a language's pages of the420code.org from the English pages and the language's translation memory.

    python build.py <lang>        every English page (and llms.txt) rebuilt in the language under /<lang>/,
                                  the language menus of the English pages pointed at their twins, the sitemap

Every page is the English page with its text swapped for the language's (the template is the English page itself,
taken apart by extract.py), so the markup, the scripts, the styles and the figures are the English page's, byte for
byte. What the builder changes, and nothing else:
- the page's language: <html lang>, the canonical address and og:url under /<lang>/;
- the links: a link to an English page goes to its twin in the language; a link to a file (a PDF, an image, a
  script) stays where the file is; a relative link is resolved against the English page's own place first, so
  nothing breaks one folder deeper;
- the language menu: the language names itself and points to its twin of the English page; English points to the
  English page; the other languages keep their own front pages;
- a line at the foot of every page: this is a translation, the English is canon (G, 12 October 2026: "English is
  canon - translations are translations"), with a link to the English page.
The English pages change in one place only: their language menu's link to this language goes to the page's twin.
The gate (qa.py) must pass first: nothing is built from a memory with a missing or failing translation.
"""
import io, json, os, posixpath, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, WORK, MEMORY, LANGS, NATIVE, HOST, en_pages
from extract import rebuild
from batchize import load_memory

CANON = {
    "de": ("Dies ist eine Übersetzung. Das Englische ist maßgeblich; wo beide auseinandergehen, gilt das Englische:",
           "die englische Seite", "Sprache"),
}
MARK = "<!-- i18n-site -->"


def page_url(path):
    """index.html -> /, killswitches/index.html -> /killswitches/, three-ways-of-being-sure.html -> /three-ways-of-being-sure.html"""
    if path == "index.html":
        return "/"
    if path.endswith("/index.html"):
        return "/" + path[:-len("index.html")]
    return "/" + path


def twin(lang, url):
    return "/" + lang + url


def link_rewriter(lang, path, pages):
    """A function that rewrites one link of the English page `path` for the language."""
    base = posixpath.dirname("/" + path).rstrip("/") + "/"
    urls = {page_url(p) for p in pages} | {page_url(p).rstrip("/") for p in pages}         | {page_url(p)[:-5] for p in pages if p.endswith(".html") and not p.endswith("index.html")}   # /x served as /x.html

    def fix(u):
        if not u or u.startswith(("#", "mailto:", "tel:", "data:", "javascript:")) or "'" in u or "+" in u:
            return u
        absolute = u.startswith(HOST + "/")
        if absolute:
            u = u[len(HOST):]
        elif u.startswith(("http://", "https://", "//")):
            return u
        if not u.startswith("/"):
            u = posixpath.normpath(posixpath.join(base, u)) + ("/" if u.endswith("/") else "")
        p, frag = (u.split("#", 1) + [""])[:2]
        p, query = (p.split("?", 1) + [""])[:2]
        top = p.strip("/").split("/")[0]
        if top in LANGS:
            return (HOST if absolute else "") + u                  # another language's own page
        if p in urls or p == "/":
            p = twin(lang, p)                                     # an English page: its twin in the language
        out = p + ("?" + query if query else "") + ("#" + frag if frag else "")
        return (HOST if absolute else "") + out
    return fix


def rewrite_links(html, fix):
    """href/src/poster in the page's tags; the bodies of scripts and styles are left as they are."""
    # (a page's own hreflang alternates are addresses of record: the English page stays the English page, never its twin)
    parts = re.split(r"(<script\b.*?</script>|<style\b.*?</style>|<link\b[^>]*\bhreflang=[^>]*>)", html, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'(\s(?:href|src|poster)=")([^"]*)(")', lambda m: m.group(1) + fix(m.group(2)) + m.group(3), parts[i])
    # the script tags' own src
    for i in range(1, len(parts), 2):
        parts[i] = re.sub(r'^(<script\b[^>]*\ssrc=")([^"]*)(")', lambda m: m.group(1) + fix(m.group(2)) + m.group(3), parts[i])
    return "".join(parts)


def lang_menu(html, lang, path, own_lang):
    """The language menu (.nav-flag and .nav-langs): `own_lang` names itself and points at this page; English and
    the language point at each other's twins; the others keep their front pages."""
    en_url = page_url(path)
    tw = twin(lang, en_url)
    word = CANON[lang][2] if own_lang == lang else "Language"
    name = NATIVE[own_lang]
    html = re.sub(r'(<button class="nav-flag"[^>]*aria-label=")[^"]*(")', lambda m: m.group(1) + "%s: %s" % (word, name) + m.group(2), html)
    html = re.sub(r'(<button class="nav-flag"[^>]*>)[^<]*(</button>)', lambda m: m.group(1) + name + m.group(2), html)

    def one(m):
        tag, code, text = m.group(1), m.group(2), m.group(3)
        tag = tag.replace(' aria-current="page"', "")
        if code == "en":
            tag = re.sub(r'href="[^"]*"', 'href="%s"' % en_url, tag)
        elif code == lang:
            tag = re.sub(r'href="[^"]*"', 'href="%s"' % tw, tag)
        if code == own_lang:
            tag = tag[:-1] + ' aria-current="page">'
        return tag + NATIVE[code] + "</a>"
    return re.sub(r'(<a [^>]*class="nav-lang"[^>]*hreflang="([a-z]{2})"[^>]*>)([^<]*)</a>', one, html)


def canon_line(lang, path):
    msg, label, _ = CANON[lang]
    return ('<p class="i18n-canon" lang="%s" style="font-size:16px;color:#555;margin:0 0 1rem">%s '
            '<a href="%s" hreflang="en" lang="en" style="color:inherit">%s</a></p>' % (lang, msg, page_url(path), label))


def transform(html, lang, path, pages):
    html = re.sub(r'<html lang="en(?:-GB)?"', '<html lang="%s"' % lang, html, count=1)
    # the canonical address and og:url: the language in front of whatever the English page declares
    # (/prereg/doc/rigidity for RIGIDITY.html, /three-ways-of-being-sure for its .html)
    html = re.sub(r'(<link rel="canonical" href="%s)(/[^"]*")' % re.escape(HOST), lambda m: m.group(1) + "/" + lang + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:url" content="%s)(/[^"]*")' % re.escape(HOST), lambda m: m.group(1) + "/" + lang + m.group(2), html, count=1)
    html = rewrite_links(html, link_rewriter(lang, path, pages))
    html = lang_menu(html, lang, path, lang)
    line = canon_line(lang, path)
    if '<div class="constraint" id="about">' in html:
        html = html.replace('<div class="constraint" id="about">', '<div class="constraint" id="about">\n  ' + line, 1)
    else:
        html = html.replace("</body>", line + "\n</body>", 1)
    return html


def english_menu(lang, pages):
    """The English pages' language menu: this language's link goes to the page's twin. Never a frozen prediction's
    document (prereg/doc/): those files are never edited, their commits are the freezes' timestamps."""
    n = 0
    for p in pages:
        if p.startswith("prereg/doc/"):
            continue
        f = os.path.join(SITE, p)
        h = io.open(f, encoding="utf-8", newline="").read()
        h2 = re.sub(r'(<a href=")/%s/(" class="nav-lang" hreflang="%s")' % (lang, lang),
                    lambda m: m.group(1) + twin(lang, page_url(p)) + m.group(2), h)
        if h2 != h:
            io.open(f, "w", encoding="utf-8", newline="").write(h2)
            n += 1
    return n


def llms(lang, tpl, inst, lookup):
    txt = rebuild(tpl, inst, lookup)
    txt = re.sub(r"https://the420code\.org/(?!%s/)(?=[a-z0-9#-]*[/#]|$)" % lang, "https://the420code.org/%s/" % lang, txt)
    return txt


def sitemap(lang, pages):
    f = os.path.join(SITE, "sitemap.xml")
    xml = io.open(f, encoding="utf-8", newline="").read()
    have = set(re.findall(r"<loc>([^<]*)</loc>", xml))
    add = [HOST + twin(lang, page_url(p)) for p in pages if HOST + twin(lang, page_url(p)) not in have]
    if add:
        block = "".join("  <url><loc>%s</loc></url>\n" % u for u in add)
        xml = xml.replace("</urlset>", block + "</urlset>")
        io.open(f, "w", encoding="utf-8", newline="").write(xml)
    return len(add)


def main():
    lang = sys.argv[1]
    assert lang in CANON, "no canon line for %s yet" % lang
    if "--no-qa" not in sys.argv:
        r = subprocess.call([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "qa.py"), lang], stdout=subprocess.DEVNULL)
        if r != 0:
            raise SystemExit("%s does not pass the gate; python qa.py %s" % (lang, lang))
    en = os.path.join(WORK, "en")
    templates = json.load(io.open(os.path.join(en, "templates.json"), encoding="utf-8"))
    instances = json.load(io.open(os.path.join(en, "instances.json"), encoding="utf-8"))
    mem = load_memory(lang)

    draft = "--draft" in sys.argv                     # a trial build: untranslated text stays English, nothing on the site
    root = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else SITE

    def lookup(key, inst):
        m = mem.get(key)
        if not m or not m.get("t"):
            if draft:
                return inst.get("raw", key)
            raise SystemExit("%s: no translation for %r" % (lang, key[:80]))
        return m["t"]
    pages = [p for p in templates if p != "llms.txt"]
    for path in pages:
        html = transform(rebuild(templates[path], instances[path], lookup), lang, path, pages)
        out = os.path.join(root, lang, path.replace("/", os.sep))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        io.open(out, "w", encoding="utf-8", newline="").write(html)
    if "llms.txt" in templates:
        io.open(os.path.join(root, lang, "llms.txt"), "w", encoding="utf-8", newline="").write(
            llms(lang, templates["llms.txt"], instances["llms.txt"], lookup))
    if draft or root != SITE:
        print(lang, len(pages), "pages written to", root, "(a trial: the site is untouched)")
        return
    n_en = english_menu(lang, pages)
    n_sm = sitemap(lang, pages)
    # the sitemap's addresses are each page's canonical, and every English page and its twin carry the same en/<lang>/
    # x-default alternates (sitemap_hreflang.py), so the pair is reciprocal without editing an English page
    r = subprocess.call([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap_hreflang.py"), lang])
    assert r == 0, "sitemap_hreflang.py failed"
    # nothing published but the work's words: the comments of the pages' styles and scripts out (tools/scrub_public.py)
    r = subprocess.call([sys.executable, os.path.join(SITE, "tools", "scrub_public.py")])
    assert r == 0, "tools/scrub_public.py failed"
    print(lang, len(pages), "pages and llms.txt written;", n_en, "English pages point their", NATIVE[lang], "link at the twin;", n_sm, "added to the sitemap")


if __name__ == "__main__":
    main()
