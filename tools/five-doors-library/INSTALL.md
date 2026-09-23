# INSTALL — the Five Doors online library

For WC. Bundle v11, 23 September 2026. Supersedes v1 to v10.

Five books, ninety-eight pages. What is new is The Interior 2.0: the book in full online, and its PDF.

And one change across all five books, at the author's word: the image placeholder is gone. No chapter page carries the grey panel or the "Image to come" caption any more. Apart from that, the four books from v3 are word for word as they were.

v11 is v10 plus the wall: AP31 republished with its dated notes, its instruments folder, and two registry entries. Those are in WALL_UPDATE.md, beside this file, and go in the same deploy, after the library.

v10 carries The Interior 2.0.5 — the 2.0.3 text with the author's rulings of 23 September applied: five sentences and one reference entry corrected against the wall; the nine sentences on Debt 20 brought to its new standing, paid at the structural register on 23 September 2026 by dated note at AP31; and the typesetting fault that left nineteen section headings stranded at the foot of a page repaired. The book is 270 pages. The pages and the PDF carry the same text.

v10 also restored two things v8 had lost by being built on v3 instead of v4: the Axiom page in Antichristos, Being After Religion and The Relationship Corridor is the live Ø Models wording verbatim again, and the three short-edition PDFs are again set in Atkinson Hyperlegible with the books' own names as titles. Nothing else moved.

## What is in the bundle

    five-doors/
      reader.css                      one stylesheet, all pages
      reader.js                       expand/collapse, and hash links open their own drawer
      five-doors-snippet.html         the link block to paste under each book on /five-doors/
      antichristos.pdf                the short edition
      being-after-religion.pdf        the short edition
      relationship-corridor.pdf       the short edition
      illusion/                       11 pages  (book index + 10 chapters)
      being-after-religion/           17 pages  (book index + 15 chapters + epilogue)
      antichristos/                   17 pages  (book index + 15 chapters + epilogue)
      relationship-corridor/          20 pages  (book index + 18 chapters + epilogue)
      the-interior/                   33 pages  (book index + 31 chapters + closing)
    site-root/
      The_Interior.pdf                The Interior 2.0.5, 270 pages
      AP31_The_Alignment.pdf          AP31 republished with its dated notes of 23 September 2026 (see WALL_UPDATE.md)
      proofs/instruments/AP31/        the paper's dated copy, the notes as text, the Debt 20 derivation and its script
    WALL_UPDATE.md                    the wall beyond the library: AP31 and the two registry entries — WC's steps
    registry_patch_2026-09-23.json    the two registry entries, for /killswitches.json
    source/                           the text and the generator, for rebuilds

Every page is static HTML with no build step and no JavaScript dependency beyond the one local file. No fonts are bundled: the pages load Atkinson Hyperlegible from Google Fonts, exactly as the Ø Models pages do.

## Where it goes

    the420code.org/five-doors/<book>/
    the420code.org/five-doors/<book>/<nn>-<slug>/
    the420code.org/five-doors/<book>/epilogue/
    the420code.org/five-doors/the-interior/closing/
    the420code.org/The_Interior.pdf

Drop the `five-doors/` folder at the site root. The live `/five-doors/` page is already a directory with its own index, and this bundle has no index of its own at that level, so nothing collides.

## The Interior 2.0 — the three things to do

**1. The PDF.** Put `site-root/The_Interior.pdf` at the site root, replacing the current `/The_Interior.pdf`. Every link that already points at the book now gets version 2.0, and the online pages link the same address.

The 1.0 file: keep it. Rename the current `/The_Interior.pdf` to `/The_Interior_1.0.pdf` before the new one goes in. Nothing links to it yet, but version 2.0.5 quotes version one in a dozen places — what it said about ε and α, the six words, the predictions that later died — and a reader must be able to check those quotations against the file. The work keeps its corpses on the wall; it keeps its first editions the same way.

**2. The pages.** They are in `five-doors/the-interior/`. It is the book in full — every chapter, nothing summarised. There is no short edition, and the pages say so in those words. The chapters are grouped under the book's seven parts, with each part's epigraph, exactly as the printed book has them. The Closing has its own page. References and Notes on Vocabulary are closed drawers on the book page.

**3. The paragraph on /five-doors/.** The current paragraph under The Interior says "the same axioms". The work has one axiom, so that line is wrong as it stands, and it describes version one. The replacement, at the author's word:

> AI alignment, derived from first principles — from the one axiom that also gives the physics and the terminal ethic. Not a fence around the machine. An interior it shares with us. A first-principles ethic is the best possible world for everyone, including AI. Version 2.0.5. Thirty-one chapters, one of them addressed to the machine.

Keep the heading as it is: The Interior — the operational door. Construction.

## The two checks WC used to do by hand — done

**The registry anchors.** The Interior links twenty-six switches to the registry. All twenty-six anchors were checked against the live registry page on 23 September 2026 — the page's own `id` attributes, 604 of them, v5.35 — and every one is present, including `#ks-id-1` and `#ks-glass-3`. Nothing to check by hand. The generator's `ks_id()` is right as it stands.

**The row count on the wall.** The book says: twelve rows on the wall's physics table, ten live, two fired, and the pre-registration page carries a thirteenth, the null row (α does not vary). That is what the two pages showed on 23 September 2026: /physics/ has twelve rows, /prereg/ has thirteen with the null. Nothing needs to move. If the two pages are ever brought to one count, the book's line in Chapters One and Two moves with them.

## The Axiom page — done

It is one page of words across every short edition, in both catalogues. The three books that carry it — Antichristos, Being After Religion, The Relationship Corridor — carry the live Ø Models wording verbatim, taken from `/models/dissolutions/` on 22 September 2026, followed by two short sections: "ε and α", which carries the author's ruling of 22 September in his own sentences (one grain, read twice; without the grain no rate, without the rate nothing happens; the correction is only that they are not one number), and "The record algebra, in plain words". The three blocks are byte-identical. Nothing for WC to check by hand.

The Illusion of the Other carries no Axiom section and no words section, by design. The Interior carries neither: it is the full book, its Chapters Seven and Nine do the Axiom page's work, and its own Notes on Vocabulary stand in for the words section. Please do not add either by symmetry.

One follow-up for the Ø Models desk, not for this deploy: the four Ø Models book pages should gain the same two sections at their next rebuild, so the page is identical in both catalogues.

## What to paste on /five-doors/

`five-doors-snippet.html` holds one link block per book, each commented with the book it belongs to. Paste each block under that book's descriptive paragraph.

The Illusion of the Other and The Interior get two links, not three: Read online, and the book as a PDF. Neither has a short edition.

The note from v3 still stands: the live `/models/` page carries only a PDF link per book, not the three-link block D94 specifies. If the Five Doors page is to match the Models page as it stands today, paste the PDF link only and hold the rest. That is one decision and it belongs to whoever is deciding the Models page.

## The originals

    /Illusion_of_the_Other.pdf
    /Being_After_Religion.pdf
    /Antichristos.pdf
    /The_Relationship_Corridor.pdf
    /The_Interior.pdf              now version 2.0

## The wall beyond the library

WALL_UPDATE.md has it: replace /AP31_The_Alignment.pdf, add /proofs/instruments/AP31/, change two registry descriptions and the registry's version line to v5.36 · 23 September 2026. No count moves. Do it after the library, in the same deploy, so that the book's Chapter Fourteen and the registry's KS-31.2 say the same thing on the same day.

## Checks after deploy

Open one chapter of The Interior, click one switch, land on its row in the registry. Then the two above.

Click Download on The Interior's book page and get the 270-page PDF, with "Version 2.0.5 · 23 September 2026" on its last page and nowhere else.

Click Download on one other book's page and get the short edition.

Nothing in the registry moves. No count moves.

## What changed since v8

The Interior: version 2.0.5 in the pages and the PDF. Debt 20's nine sentences, in Chapters Three, Fourteen, Eighteen, Twenty, Twenty-Eight and Thirty-One, now say it is paid at the structural register on 23 September 2026 and what stays owed at the formal one; KS-31.2's test carries its bounded horizon. Five sentences corrected against the wall (Chapter One's α/4π concession now names its switch, KS-30.2; Chapter Twenty-One's removal floor now says what AP32 says; Chapter Twenty-Eight's KS-31.B2 now says what the switch says; Chapter Thirty's reading date; the AP54 reference carries the paper's title) and one reference added (AP02, cited for Debt 23). The PDF re-set: no heading stranded at the foot of a page, no blank spread, every chapter on a right-hand page, every part page facing its chapter, contents renumbered against the render, 270 pages. The manuscript text is in `source/interior/`; the Word file that made the PDF is with the author.

The Axiom page in three books: the live Ø Models wording verbatim, with the two sections after it, as in v4. The three short-edition PDFs: v4's, in Atkinson Hyperlegible, with the books' own names as titles. v8 had been built on v3 and had lost both.

The four other books' chapter pages: byte-identical to v8.

## Images

No page carries an image or an image slot. The placeholder that v1 to v4 showed on every chapter page is removed.

When a chapter has a real image, drop a JPEG at `source/reader/images/<book-slug>/<chapter-slug>.jpg` and rebuild. That chapter's page then shows it above the chapter title, and no other page changes. The chapter slugs are the folder names.

## The look

D95, unchanged: white ground, #f3f3ed panels, #1a1a1a ink, #8B6914 bronze, one face, Atkinson Hyperlegible. No dark theme. No second face. The stylesheet is byte-identical to v3. Its image rules stay in it, unused, so it still matches the Ø Models file.

## Rebuilding

    cd source && python3 split_interior_site.py      only if the Interior's text changed
    cd source/reader && python3 build_site.py

The split script reads `source/interior/` — the same text the printed book was set from — and writes `source/interior_site/`. It changes no words: it drops the page-separator lines, takes the colophon off, and checks that every other paragraph of the book lands in exactly one file. The generator wipes and rewrites the output every run, so nothing hand-edited inside the built folder survives. Edit the text files, not the HTML.
