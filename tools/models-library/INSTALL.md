# Installing the Ø Models library on the420code.org

For WC. Read once, then do the steps in order. Nothing here touches the originals, the registry, or any count.

## 0. What you are installing

A static folder, `models/`, that adds fifty-eight pages under `/models/…` on the site, plus four PDFs (the short editions), one stylesheet and one script. Pure HTML. No build step on Netlify. No dependency on the site's CSS. No changes to any existing page except one paste on `/models/` (step 4).

Bundle: `o-models-library-bundle_v5_2026-09-22.zip`. Contents:

```
models/                       -> goes into the site's publish directory as /models/
  reader.css  reader.js
  models-snippet.html         -> not served; it is the paste for step 4
  dissolutions/  resolutions/  applications/  horizons/   (book page, chapter pages, epilogue)
  dissolutions.pdf  resolutions.pdf  applications.pdf  horizons.pdf
source/                       -> NOT served. Keep it in the repo beside the site (see step 7). It is the text and the generator.
README.md  INSTALL.md
```

## 1. Before you start — one dependency

The chapter pages link "Where It Would Die" to `/what-is-the-420-code/#where-it-would-die`. That anchor exists only after the front-door rebuild of 19 September. Deploy that rebuild first, or in the same deploy. If it is already live, carry on.

The pages also link to `/Dissolutions.pdf`, `/Resolutions.pdf`, `/Applications.pdf`, `/Horizons.pdf` (the originals, as the site serves them today), to `/killswitches/` with anchors, to `/one-awareness/`, to `/prereg/` and to `/models/`. All of those exist today. Nothing needs to move.

## 2. Copy the folder

Unzip. Copy `models/` into the Netlify publish directory (the folder the site deploys from), so that these paths resolve at the root:

```
/models/dissolutions/
/models/dissolutions/01-why-is-there-something-rather-than-nothing/
/models/dissolutions/epilogue/
/models/dissolutions.pdf
/models/reader.css
/models/reader.js
```

Same for `resolutions`, `applications`, `horizons`.

If a `/models/` page already exists as a file (`models.html` or `models/index.html`), leave it. The bundle has no `models/index.html`, so nothing collides. If your `/models/` page is a directory index that Netlify serves from `models/index.html`, check the bundle did not overwrite it: it does not contain that file.

Do not put `models-snippet.html` or `source/` in the publish directory. They are not pages.

## 3. Directory paths

Every internal link is root-relative and ends in a slash, e.g. `/models/resolutions/08-5-choice/`. Netlify serves `index.html` for a directory path by default. If the site has "pretty URLs" disabled or a redirect rule that strips trailing slashes, check one chapter link after deploy (step 6). Nothing else is needed.

## 4. The Ø Models page — one paste per book

Open `models-snippet.html`. It holds five short blocks, one per book and one for Ø Predictions. Each is a `<p>` with links in the site's existing `nb-pdf` pill class:

```
<p><a class="nb-pdf" href="/models/dissolutions/">Read online</a>
   <a class="nb-pdf" href="/models/dissolutions.pdf">Download the short edition (PDF)</a>
   <a class="nb-pdf" href="/Dissolutions.pdf">Download the original (PDF)</a></p>
```

Paste each block under the description paragraph (`cat-desc`) of its book's section (`cat-section`) on `/models/`. Keep the existing "PDF" link on the heading if you like; the new block adds the three doors. Nothing is added to the site's stylesheet; `nb-pdf` is already there.

The Predictions block gives "Read the predictions page" (`/prereg/`) and "Download the original". There is no short edition of Predictions.

## 5. Deploy

Deploy as usual. No environment variables, no functions, no headers file needed. The pages load one font from Google Fonts (Atkinson Hyperlegible), as the site already does; if the site's CSP or headers restrict font hosts, the pages fall back to the system sans-serif and still work.

## 6. Check — five clicks

1. Open `/models/dissolutions/`. The Axiom row is open, The words is a row below it, the chapter list shows twelve chapters with a one-line each.
2. Open the first chapter. Sections are open. "Where it would die" is closed with "6 switches" on its row. Open it. Click **PZ-1.1**. You land on that row in the registry (`/killswitches/#ks-pz1-1`).
3. On the same page, at the foot, click **The original book (PDF)**. The long original opens. Click **This edition (PDF)**. The short edition opens (115 pages, edition line on the colophon).
4. On `/models/`, click **Read online** under Ø Resolutions, then **Eight and a Half** in the chapter list. The page loads at `/models/resolutions/08-5-choice/`.
5. On a phone, open any chapter. No horizontal scroll. The switch IDs sit above their text.

If step 2 lands at the top of the registry rather than on the row, the registry anchors changed; tell the desk that built this and the anchors are one line in `source/reader/build_site.py` (`ks_id`).

## 7. Keep `source/` in the repo

`source/` is the text of all four short editions and the generator. Keep it in the repo, outside the publish directory (for example `tools/models-library/source/`). It is how the pages are rebuilt when G changes a chapter, adds an image, or writes his Artist's Notes.

Rebuild:

```
cd source/reader
python3 build_site.py
```

Python 3, no packages. It writes `site/models/` from `../<book>/*.txt` and the one-line files. Copy the result over `/models/` and deploy. The PDFs are not rebuilt by this script; they come from the desk with each edition.

## 8. Later changes, and where they go

- **G changes a chapter's text.** Edit `source/<book>/chNN.txt`, rebuild, copy, deploy. Keep the file's shape: `# Title`, `## Section` headings, blank line between paragraphs, the `> Source:` line last.
- **An image for a chapter.** Put `source/images/<book>/<chapter-slug>.jpg` in place (the slug is the folder name of the chapter page). Rebuild. The placeholder drawing is replaced and the image is copied beside the page as `image.jpg`. Landscape, about 1280 wide, under 300 KB.
- **Audio.** When a chapter has audio, "Listen — soon" becomes a link. That is a two-line change in `strap()` in `build_site.py`; ask the desk, or change `<span class="soon">Listen — soon</span>` to an `<a>` there.
- **G's Artist's Notes.** Replace the text under `# Artist's Note` in `source/<book>/00_front.txt`. Rebuild. The book page and the PDF both take it (the PDF comes from the desk).
- **A new edition of a PDF.** Replace `/models/<book>.pdf`. The edition line is inside the PDF; the pages do not print a version.
- **An original is republished.** Nothing to do. The pages link to `/<Book>.pdf` and print no page count.
- **Colours or type.** The `:root` block at the top of `reader.css` holds every colour. One face, Atkinson Hyperlegible, loaded in each page's head.

## 9. What not to do

Do not edit the generated HTML by hand; edit the source and rebuild, or the next rebuild loses the edit.
Do not move the originals from the site root. Three hundred links point there.
Do not rename a chapter folder. Its URL is on the registry's side of the link.
Do not add the short-edition PDFs anywhere but `/models/`.

## 10. Registry, when its desk gets to it

Each switch paragraph on a chapter page carries the id the registry uses: `#ks-pz1-1`, `#ks-res8-5-1`, `#ks-app3-2`, `#ks-hor13-6`. The registry can link each Ø Models switch back to `/models/<book>/<chapter-slug>/#ks-…` and land on the switch with its section open. No change to the pages is needed for that.
