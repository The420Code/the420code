# -*- coding: utf-8 -*-
"""Make sitemap.xml say, for every page that has a twin in a language, what search engines need:

    python sitemap_hreflang.py <lang> [--check]

1. the language's entries use the page's own canonical address (the page says /de/prereg/doc/rigidity; the sitemap
   used to say /de/prereg/doc/RIGIDITY.html, an address Google drops as a duplicate);
2. the English page and its twin each carry the same three xhtml:link alternates (en, <lang>, x-default), so the
   pair is reciprocal without a single English page being edited (the frozen predictions' files are never touched:
   their commits are the freezes' timestamps);
3. an English page whose twin exists but which the sitemap did not list is listed.

Idempotent. Entries that already carry xhtml:link (the front pages, all languages) are left as they are.
build.py calls this after it writes a language; it can be run on its own.
"""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, HOST

CANON = re.compile(r'<link rel="canonical" href="([^"]+)"')


def canonical(path):
    h = io.open(path, encoding="utf-8").read(40000)
    m = CANON.search(h)
    return m.group(1) if m else None


def twin_pairs(lang):
    """[(english file's path from the root, english canonical, twin canonical, twin's old address)]"""
    out = []
    base = os.path.join(SITE, lang)
    for dp, _, fs in os.walk(base):
        for f in fs:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), base).replace(os.sep, "/")
            en_file = os.path.join(SITE, rel.replace("/", os.sep))
            if not os.path.isfile(en_file):
                continue
            en_c, tw_c = canonical(en_file), canonical(os.path.join(dp, f))
            if not en_c or not tw_c:
                continue
            if rel == "index.html":
                old = "/"
            elif rel.endswith("/index.html"):
                old = "/" + rel[:-len("index.html")]
            else:
                old = "/" + rel
            out.append((rel, en_c, tw_c, HOST + "/" + lang + old))
    return out


def links(en, tw, lang):
    return ('<xhtml:link rel="alternate" hreflang="en" href="%s"/>'
            '<xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
            '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>') % (en, lang, tw, en)


def main():
    lang = sys.argv[1]
    check = "--check" in sys.argv
    f = os.path.join(SITE, "sitemap.xml")
    xml = io.open(f, encoding="utf-8", newline="").read()
    orig = xml
    n_fixed = n_links = n_added = 0
    for rel, en_c, tw_c, old in twin_pairs(lang):
        if old != tw_c and "<loc>%s</loc>" % old in xml:
            if "<loc>%s</loc>" % tw_c in xml:
                # the canonical is already listed: drop the duplicate line
                xml = re.sub(r"[ \t]*<url><loc>%s</loc>[^\n]*</url>\r?\n" % re.escape(old), "", xml, count=1)
            else:
                xml = xml.replace("<loc>%s</loc>" % old, "<loc>%s</loc>" % tw_c, 1)
            n_fixed += 1
        if "<loc>%s</loc>" % en_c not in xml and "<loc>%s</loc>" % tw_c in xml:
            xml = xml.replace("</urlset>", "  <url><loc>%s</loc></url>\n</urlset>" % en_c)
            n_added += 1
        block = links(en_c, tw_c, lang)
        for loc in (en_c, tw_c):
            m = re.search(r"<url><loc>%s</loc>(?!<xhtml:link)" % re.escape(loc), xml)
            if m:
                xml = xml[:m.end()] + block + xml[m.end():]
                n_links += 1
    print("%s: %d addresses made canonical, %d English pages listed, %d entries given alternates" % (lang, n_fixed, n_added, n_links))
    if check:
        print("(--check: nothing written)")
        return
    if xml != orig:
        io.open(f, "w", encoding="utf-8", newline="").write(xml)


if __name__ == "__main__":
    main()
