# INSTALL — the Five Doors online library

For WC. Bundle v4, 22 September 2026. Supersedes v1, v2 and v3 of the same date. This is the bundle to deploy.

Four books, sixty-five pages. The Interior is not in it — its short edition follows from the 2.0 rewrite once the author has ruled on it, and its folder is added at that point without touching anything here.

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
    source/                           the text and the generator, for rebuilds

Every page is static HTML with no build step and no JavaScript dependency beyond the one local file. No fonts are bundled: the pages load Atkinson Hyperlegible from Google Fonts, exactly as the Ø Models pages do.

## Where it goes

    the420code.org/five-doors/<book>/
    the420code.org/five-doors/<book>/<nn>-<slug>/
    the420code.org/five-doors/<book>/epilogue/

Drop the `five-doors/` folder at the site root. The live `/five-doors/` page is already a directory with its own index, and this bundle has no index of its own at that level, so nothing collides.

## The Axiom page — done, nothing for WC to check

The Axiom page is one page of words across the library. In this bundle the three books that carry it — Antichristos, Being After Religion, The Relationship Corridor — carry the live Ø Models wording verbatim, taken from `/models/dissolutions/` on 22 September 2026, with two short sections added after it: "ε and α", which carries the author's ruling of 22 September (ε and α are one grain, read twice; the correction is only that they are not one number), and "The record algebra, in plain words". The three blocks are byte-identical.

One follow-up for the Ø Models desk, not for this deploy: the four Ø Models book pages should gain the same two sections at their next rebuild, so the page is identical in both catalogues. Until then the Five Doors page is the models page plus those two sections, and nothing in it contradicts the models page.

The Illusion of the Other carries no Axiom section and no words section, by design. It has no terms and no switches. Please do not add either by symmetry.

## What changed since v1

v1 was read cold. The reading found five things and all five are fixed.

The three short-edition PDFs are in the folder. In v1 every Download button pointed at an address that returned nothing.

The Artist's Notes are the author's own, verbatim from the published originals. v1 carried reworked versions, and one of them — Antichristos — carried a sentence written in his voice that he did not write. That sentence is gone. Only the counts inside his own sentences were updated. The "candidate text" line is deleted from every page.

The Illusion of the Other now has its Artist's Note, Preface and Orientation, verbatim; its real subtitle on the page and in the title tag; the correct line about switches (it has none of its own); and the back matter cut from the end of Chapter Ten, where it had been reading as the chapter continuing after its ending.

Being After Religion Chapter Eight — the record chapter — had nine figures that would not have survived a hostile check. Each is corrected. The Rhineland passage now separates the two families and the two cities correctly, and the chronicle's quoted prayer and the author's own answering line are both restored, attributed to Mistress Rachel of Mainz, which is where the chronicles put her.

Four sentences: Antichristos Four, Corridor One, Corridor Six and Fifteen, Corridor Eighteen.

## What changed since v2

The Bucha vignette in Being After Religion Ten, at the author's ruling. It carried a composite under a real man's name. It now carries the man as the record has him: Mykhailo Kovalenko, sixty-two, at a checkpoint on Yablunska Street on 5 March 2022, hands up, evacuating his family, body on that street for twenty-nine days.

The transatlantic trade passage in Chapter Eight now carries the author's own two-figure structure — the people shipped, and the deaths on the crossing counted separately from the deaths across the whole system. The single flattened figure was a compression error of the desk's, not the author's.

The counts throughout the four books are now the forms that do not go stale: over fifty Artist's Proofs, over six hundred kill switches. The work is still being written, so a fixed number in a printed book is stale the week after it prints. The exact figures live on the wall, counted live.

The Axiom page rebuilt to the Ø Models structure, as above.

## What changed since v3

The Axiom page, as above: the live Ø Models wording verbatim, with the "ε and α" and record-algebra sections after it, in all three books that carry it.

The three short-edition PDFs are rebuilt from this bundle's own source, so they carry the same Axiom page as the pages do, and they are set in the house typeface, Atkinson Hyperlegible, embedded. The v3 PDFs were set in a fallback face. Their metadata titles are the books' own names.

Nothing else moved. Every chapter page is byte-identical to v3.

## What to paste on /five-doors/

`five-doors-snippet.html` holds one link block per book, each commented with the book it belongs to. Paste each block under that book's descriptive paragraph on `/five-doors/`.

The live `/models/` page already carries the three-link block under each book — Read online, Download the short edition, Download the original — checked on 22 September 2026. Paste the full block under each book on `/five-doors/` so the two catalogue pages match.

The Illusion of the Other gets two links, not three. It has no short edition, so what is online is the book itself, and the page says so in those words.

## The originals

The snippet links the original PDFs at the filenames the live site already uses:

    /Illusion_of_the_Other.pdf
    /Being_After_Religion.pdf
    /Antichristos.pdf
    /The_Relationship_Corridor.pdf

## The registry links

All twenty-seven switch anchors were compared against the live registry on 22 September 2026 — KS-AC.1 to 7, KS-BAR.1 to 9, KS-RC.1 to 11. Every one is present, every one is live, and the anchor form matches the registry's own. **WC does not need to check these.**

    KS-AC.2  ->  /killswitches/#ks-ac-2
    KS-BAR.9 ->  /killswitches/#ks-bar-9
    KS-RC.11 ->  /killswitches/#ks-rc-11

Each switch also carries that same id on its own page, so the registry can link back: `/five-doors/antichristos/06-the-name-before-the-name/#ks-ac-2`.

## Two checks after deploy

Open one chapter, click one switch, land on its row in the registry.

Click Download on one book page and get the short edition. Click Download the original on `/five-doors/` and get the long one.

Nothing in the registry moves. No count moves.

## Images

Every chapter page has a hero slot. None of the books has images yet, so every page currently renders the placeholder SVG with the caption "Image to come".

To add one, drop a JPEG at `source/reader/images/<book-slug>/<chapter-slug>.jpg` and rebuild; the builder copies it into the chapter folder as `image.jpg` and drops the placeholder. The chapter slugs are the folder names.

## The look

D95, unchanged: white ground, #f3f3ed panels, #1a1a1a ink, #8B6914 bronze, one face, Atkinson Hyperlegible. No dark theme. No second face. The stylesheet is byte-identical to the Ø Models one, so if you have patched that file, patch this one the same way or serve one copy for both.

## Rebuilding

    cd source/reader && python3 build_site.py

It reads `../<book-src>/00_front.txt`, `../<book-src>/ch*.txt` and `../<book-src>/99_epilogue.txt`, plus `onelines_fivedoors.json` for the line under each chapter title. It wipes and rewrites the output every run, so nothing hand-edited inside the built folder survives. Edit the text files, not the HTML.

The book source folders are `illusion`, `bar`, `antichristos`, `corridor`. The mapping from folder to URL slug is in the BOOKS list at the top of the builder.

## For the originals, when they are next reprinted

The nine corrections in Being After Religion Chapter Eight are on these pages and not in the printed original. The same sentences are in the original and the author has them. So is the Bucha vignette.
