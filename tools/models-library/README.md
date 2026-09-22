# Ø Models — online library bundle

For the website desk. Static HTML. No build step needed on the site. Drop `models/` into the Netlify publish directory so that the paths below resolve at the site root.

## What is here

```
models/
  reader.css                 one stylesheet for every page (the site's colours and face)
  reader.js                  expand all / collapse all; opens the section a #hash points into
  models-snippet.html        the Read · Listen · Download line to add under each book on /models/
  dissolutions/index.html    book page: The Axiom (open), The words, Artist's Note, How to read, chapter list, epilogue link
  dissolutions/01-why-is-there-something-rather-than-nothing/index.html   one page per chapter
  …
  dissolutions/epilogue/index.html
  resolutions/  applications/  horizons/                                   same shape
  dissolutions.pdf  resolutions.pdf  applications.pdf  horizons.pdf        the short editions (the Download target); the originals stay at /<Book>.pdf
source/                      the chapter texts and the generator, so the pages can be rebuilt
```

58 pages: 4 book pages, 50 chapter pages, 4 epilogues. Every chapter page has the same structure: strap (book, the short edition, chapter n of N, Read / Listen — soon / Download) · In this book · image · the question · one line · opening section · every section open, collapsible · Where it would die closed, with the switch count · the chapter's closing paragraphs · source line · previous/next.

## URLs

- `/models/dissolutions/` `/models/resolutions/` `/models/applications/` `/models/horizons/`
- `/models/<book>/<nn>-<slug>/` for chapters, e.g. `/models/resolutions/08-5-choice/`
- `/models/<book>/epilogue/`
- `/models/<book>.pdf`

All internal links are root-relative (`/models/...`). If the site does not serve `index.html` for a directory path, enable that (Netlify does by default).

## Things to check or decide

1. **Kill switch links.** Every switch ID (PZ-1.1, RES-8.5.1, APP-3.2, HOR-13.6 …) links to the registry as `https://the420code.org/killswitches/#ks-pz1-1`, `#ks-res8-5-1`, `#ks-app3-2`, `#ks-hor13-6` — the registry's own convention (KS-PZ1.1 → `ks-pz1-1`). Each switch paragraph on its chapter page carries the same id, so the registry can link back to `/models/<book>/<chapter>/#ks-pz1-1`. The line under each switch list says how the registry writes the IDs and links "Where It Would Die" to `/what-is-the-420-code/#where-it-would-die`.
2. **Images.** Every chapter shows a placeholder drawing (two jars, one grain) captioned "Image to come". To use a real image, put `source/images/<book>/<chapter-slug>.jpg` in place and rebuild, or replace the `<figure class="hero">` block in the page by hand.
3. **Listen** is a greyed-out label on every page until there is audio. Make it a link when there is.
4. **Artist's Note** on each book page is still G's candidate text. G said he will do the notes last. The editorial bracket is gone from pages and PDFs.
5. **PDFs** are the short editions, with the edition line on the colophon: all four v1.0, all 22 September 2026. The originals are not in this bundle and stay at `/Dissolutions.pdf`, `/Resolutions.pdf`, `/Applications.pdf`, `/Horizons.pdf`, where the site and the registry already point. Each book page links to its original; no page count is printed, so nothing goes stale when an original is republished.
5a. **Two editions, named.** The strap on every page says "the short edition". The book page says so under the one-line and links the original. The Source line at the foot of every chapter links the book title to the original PDF.
6. **Font.** One face, Atkinson Hyperlegible, as the site. Loaded from Google Fonts as the site loads it.
7. **Colours** are the site's: white ground, #f3f3ed panels, #1a1a1a ink, #8B6914 bronze. They live in the `:root` block at the top of `reader.css`; the theme-color meta is #ffffff.
8. **Snippet.** `models-snippet.html` holds five short lines in the site's `nb-pdf` pill class — one per book (Read online · Download the short edition · Download the original) and one for Ø Predictions (Read the predictions page · Download the original). Paste each under the cat-desc paragraph of its cat-section on `/models/`. Nothing to add to the site's CSS.
9. **Page shape.** Sections open by default; "Where it would die" closed, with its switch count on the row; the chapter's closing paragraphs after the last switch are shown open, after the drawer (the "All five stand" lines are gone, at G's ruling). Collapse all / Expand all sit under the opening section. On the book page the Axiom is first and open; The words is its own row below it; the Artist's Note and How to read are closed below that. Every page ends with a line naming it as the short edition, a summary, with links to the original book (PDF), this edition (PDF) and this edition online.
10. **Head.** Every page carries canonical, robots and Open Graph title/description (the one-line is the description).

## Rebuilding

```
cd source/reader
python3 build_site.py        # writes site/models/ from ../<book>/*.txt and onelines_*.json
```

Python 3, no dependencies. Chapter text lives in `source/<book>/ch*.txt`, front matter in `00_front.txt`, epilogue in `99_epilogue.txt`. The one line under each chapter title is in `onelines_*.json`, keyed by chapter file; it is always a sentence, or a run of sentences, verbatim from the chapter.

## Not included

Ø Predictions. It is a table and a set of derivations, not chapters; the predictions page already reads it online. The snippet gives it "Read the predictions page · Download the original".

## Rulings of 22 September 2026 (G), carried in v1.0

The "Five switches. All five stand." line is cut from every chapter. The switches stay; the epilogue's sentence carries what the line was for.
The Artist's Note in every book now opens the six words — "Don't be a cunt. Be kind. That is us." — so the closing line is a return, not an arrival. "The Axiom speaks. We transcribe." is gone.
The first-person line in Horizons Thirteen stays.
Every chapter that stands on the one interior says so at its opening, names Ø Dissolutions Six, and links the wall page https://the420code.org/one-awareness/.
Where a chapter says "derived", "falls out of" or "structural" and the steps are not on the page, it now says where to check them: the original, by chapter.
The correction hierarchy is Applications Two's ladder everywhere. The Horizons original, Chapter Thirteen, lists a different ladder and needs correcting on the wall; see the notes document.
