# -*- coding: utf-8 -*-
"""Measure what was built: every page of a language against its English page.

    python verify_i18n.py <lang> [--root DIR]     (DIR: a trial build's folder; default the site)

For each page: the tag skeleton (every tag, in order, with its attributes except the ones the builder changes on
purpose: the text-bearing attributes, the links, the language marks) equals the English page's, apart from the
one line the builder adds (the canon line); the html tag carries the language; the canonical address and og:url
are the page's own; every link of the page lands on a file (a page of the language, or a file of the site); the
language menu names the language and points English at the English page; the canon line is there and points at
the English page; the longest English paragraphs do not survive verbatim. Exit 1 on any failure.
"""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, LANGS, HOST, NATIVE, en_pages
from build import page_url

TAG = re.compile(r"<[^>]+>")


def skeleton(html):
    html = re.sub(r"<script type=\"application/ld\+json\">.*?</script>", "<script-ld>", html, flags=re.S)
    html = re.sub(r"<svg.*?</svg>", "<svg/>", html, flags=re.S)
    html = re.sub(r'<p class="i18n-canon".*?</p>\s*', "", html, flags=re.S)
    html = re.sub(r"<script\b(?![^>]*\bsrc=)[^>]*>.*?</script>", "<script/>", html, flags=re.S)
    html = re.sub(r"<style\b[^>]*>.*?</style>", "<style/>", html, flags=re.S)
    out = []
    for t in TAG.findall(html):
        if t.startswith("<!"):
            continue
        t = re.sub(r'\s(?:aria-label|aria-current|title|alt|content|href|src|poster|lang|hreflang|placeholder)="[^"]*"', "", t)
        out.append(t)
    return out


def exists(root, lang, url):
    p = url.split("#")[0].split("?")[0]
    if not p or p == "/":
        return True
    if p.startswith("/%s/" % lang) or p == "/" + lang:
        base = root
    else:
        if p.strip("/").split("/")[0] in LANGS:
            return True                                    # another language's own page
        base = SITE
    f = os.path.join(base, p.lstrip("/").replace("/", os.sep))
    return os.path.isfile(f) or os.path.isfile(os.path.join(f, "index.html")) or os.path.isfile(f + ".html")


def main():
    lang = sys.argv[1]
    root = sys.argv[sys.argv.index("--root") + 1] if "--root" in sys.argv else SITE
    fails, n = [], 0
    for path in en_pages():
        ep = os.path.join(SITE, path)
        lp = os.path.join(root, lang, path)
        if not os.path.exists(lp):
            fails.append("missing %s" % path)
            continue
        en = io.open(ep, encoding="utf-8").read()
        tr = io.open(lp, encoding="utf-8").read()
        n += 1
        a, b = skeleton(en), skeleton(tr)
        if a != b:
            i = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
            fails.append("%s: skeleton differs at tag %d: %s vs %s" % (path, i, a[i:i + 2], b[i:i + 2]))
        if not re.search(r'<html lang="%s"' % lang, tr):
            fails.append("%s: html lang" % path)
        for name, before in (("canonical", '<link rel="canonical" href="'), ("og:url", '<meta property="og:url" content="')):
            m = re.search(re.escape(before + HOST) + r'(/[^"]*)"', en)
            if m and before + HOST + "/" + lang + m.group(1) + '"' not in tr:
                fails.append("%s: %s" % (path, name))
        body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", tr, flags=re.S)
        for u in re.findall(r'\s(?:href|src|poster)="([^"]*)"', body):
            if not u or u.startswith(("#", "mailto:", "tel:", "data:", "javascript:")) or re.match(r"https?://", u):
                continue
            if not exists(root, lang, u):
                fails.append("%s: link lands nowhere: %s" % (path, u))
        if 'class="nav-flag"' in en:
            if not re.search(r'<button class="nav-flag"[^>]*>%s</button>' % re.escape(NATIVE[lang]), tr):
                fails.append("%s: the language menu does not name %s" % (path, NATIVE[lang]))
            if not re.search(r'<a href="%s" class="nav-lang" hreflang="en"' % re.escape(page_url(path)), tr):
                fails.append("%s: the language menu's English is not the English page" % path)
        if not re.search(r'<p class="i18n-canon"[^>]*>.*?<a href="%s"' % re.escape(page_url(path)), tr, re.S):
            fails.append("%s: the canon line" % path)
        paras = sorted(re.findall(r"<p>([^<]{120,})</p>", en), key=len, reverse=True)[:3]
        for p in paras:
            if p in tr:
                fails.append("%s: an English paragraph survives: %r" % (path, p[:60]))
    print(lang, n, "pages checked,", len(fails), "failures")
    for f in fails[:60]:
        print("FAIL", f)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
