# WC notes — installed 22 September 2026

Bundle `five-doors-library-bundle_v4_2026-09-22` installed as delivered, with the changes below. Every change to the pages is in `source/reader/build_site.py`, so a rebuild keeps it. **Never hand-edit the built pages.**

The library is held to the same rules G ruled on for the Ø Models library the same day:

1. **One stylesheet and one script for both libraries.** The bundle's own `CSS` and `JS` constants are gone; the generator reads `models/reader.css` and `models/reader.js` from the repo and writes them to `/five-doors/`. That is the bundle's own instruction ("serve one copy for both"), and it means the 16px floor, the site's greys, the header's rules and the counters cannot drift apart. `verify_0911.py` asserts the two pairs are byte-identical.
2. **It runs on Windows.** UTF-8 in and out, LF endings, and one-line keys with forward slashes — without that, every chapter's one-line was missing.
3. **The site's sticky header, on every page**, built by `i18n/frontdoor/header.py` with the rooms taken verbatim from the front door. The page takes the site's column. **After any change to the menu, rebuild both libraries.**
4. **The site's footer, on every page**, byte for byte as `/models/` carries it. The colophon keeps the edition line and a line home.
5. **No "Listen — soon", no images, every row closed on arrival** — including the Axiom on the book pages.
6. **A way back between Previous and Next**, to the book's contents and to Ø Five Doors.
7. **Both counters** ride in `reader.js`. `netlify/functions/visit-counter.mjs` accepts the library's 65 addresses; `download-counter.mjs` names the short editions `five-doors/<book>.pdf`, apart from the originals.
8. **Two straight apostrophes** in the generator's colophon sentence were curled: the house rule has no exceptions, and `verify_0911.py` found them.

On `/five-doors/`, each book's links sit in `<p class="lib-doors">`, with the same rule the `/models/` page carries. The sitemap lists the 65 pages (100 → 165). `llms.txt` carries the library. Suites expect **183 headers / 183 menus**.

Rebuild from `tools/five-doors-library/source/reader/`:

```
python build_site.py
```

Then copy `site/five-doors/*` over `/five-doors/`, except `five-doors-snippet.html`, and delete `site/`.

The Interior is not in this bundle. Its folder is added when the author has ruled on its 2.0 rewrite, without touching anything here.

## 27 September 2026 — brief 6, the Five Doors airtight

The text took the brief's 315 changes and G's three held lines (WC/tools/brief6_sources_0927.py, brief6_after_0927.py). The generator learnt four things:

1. **Italics and bold pass through.** `<em>` and `<strong>` in the text are set as the books set them; every other tag is still escaped. `untag()` keeps them out of descriptions and titles. The Illusion's seven italic spans from its Word source are in the text. Bold italic is written `<em><strong>…</strong></em>`.
2. **"The registry writes it/them …" is gone** from the drawer's `p.reg` line: it repeated the ids printed above it, and three pages printed a wrong range.
3. **Versions:** the short editions v1.3; The Interior 2.0.8, 27 September 2026; The Illusion carries `version` and `version_date` (1.2, 27 September 2026) on its editions line and its book page. The Interior's Closing links its source line to the book, as the chapters do.
4. The three short editions end on a colophon after `---` in `99_epilogue.txt` (the page never shows it; the PDF prints it), in the Ø Models form: `The short edition · v1.3 · 27 September 2026`.
