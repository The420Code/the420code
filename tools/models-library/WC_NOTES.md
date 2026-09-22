# WC notes — installed 22 September 2026

The bundle `o-models-library-bundle_v5_2026-09-22` was installed as delivered, with the changes below. Every change to the pages is in `source/reader/build_site.py`, so a rebuild keeps it.

1. **It runs on Windows.** Files are read and written as UTF-8 with LF endings. The one-line keys use forward slashes: on Windows, `os.path.relpath` gave `applications\ch01.txt`, which missed every one-line and printed the chapter's last paragraph instead. From this repo it rebuilds the delivered pages byte for byte, apart from the stylesheet.
2. **The 16px floor and the site's greys.** Nothing on the420code.org is set below 16px. The library's labels were 11.5–15.2px and are now 16px. Body text is 18px/1.65, as on the site. `--ink-2` and `--mute` are the site's `#4a4a4a`; the library's `#8a8a8a` was 3.5:1 on white. The switch-ID column is 7rem, the book-list number 6.2rem and the chapter-list number 6.8rem, so that "Thirteen" and "RES-8.5.5" fit at 16px.
3. **G's rulings of 22 September, after it went live.** The Axiom row is closed on arrival like every other row of the book page. Every page ends with the site's own footer, byte for byte as `/models/` carries it: the studio block, the three lines, the ethic and the lifestyle line. The colophon keeps the edition line and a line home. Every page posts its visit and every PDF click to the site's counters, as every other page does (`reader.js`). The two functions in `netlify/functions/` were widened to match: the visit counter now counts every page that posts, library included, and keeps paths up to 160 characters (a chapter's path runs to 72). The download counter names the short editions `models/<book>.pdf`, so they never merge with the originals.

On `/models/`, each book's three doors sit in `<p class="lib-doors">`. That one rule in the page's style block keeps each pill whole and lets the row wrap on a phone. The sitemap lists the 58 pages.

Rebuild from `tools/models-library/source/reader/`:

```
python build_site.py
```

Then copy `site/models/*` over `/models/`, except `models-snippet.html`, and delete `site/`.
