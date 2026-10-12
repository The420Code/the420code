# the420code.org in every language: the whole English site, word for word

G, 12 October 2026: "get the translations on the420code.org done ... make sure the english website is translated in
full - word for word - in each language ... if anything on a translation is in dispute, the english is always the
version to default back to. English is canon - translations are translations. - one language at a time - lets start
with German". Text only; the films come much later.

**English is canon.** Every page in a language is the English page with its text swapped for a translation, and says
so at its foot, with a link to the English page. Numbers, codes (AP, KS, D, versions, DOIs), formulae, names and the
footer's art line "the lifestyle 1980-08-05 – 2025-12-25" are never changed. The frozen predictions' English files
are never touched: their translations are new files under /<lang>/prereg/doc/.

This engine is the one that put whybekind.org into twelve languages (github.com/The420Code/whybekind, tools/i18n),
brought here. The Five Doors books are the same text on both sites, so their translations are shared
(`seed_memory.py`).

## The pipeline, one language

All from this folder. The working files (slices, prompts, patches) live outside the repository in
`C:\Users\info\the420code-i18n-work` (`T420_I18N_WORK`); the translation memory, the one thing that matters, is
committed: `i18n/site/<lang>.json` (English key => {"t": translation, "src": "patch|whybekind|lock|fixed|review"}).

1. `python extract.py --check`: every English page (the front door, three-ways-of-being-sure.html and every page
   under the rooms, 206 pages; the sitemap is not the list, it misses eleven of the prediction documents) taken
   apart into a template and its text, and every page rebuilt byte for byte from them. 25,401 unique segments,
   467,299 words (12 October 2026).
2. `python lock.py seed <lang>`, then one agent with `python lock.py prompt <lang>`: the lock table, the names that
   read the same everywhere (the rooms, the 54 papers by number and title, the books, every chapter title, the
   slogan, the labels) and the glossary of the work's terms. Seeds are words already published in the language:
   whybekind.org's lock table, this site's own edition's menu (room by room) and slogan, and the Ø Models titles
   where the edition keeps them in English. `python lock.py check <lang>`.
3. `python seed_memory.py <lang>`: whybekind.org's published translation of every segment that is the same English
   (German: 5,219 segments, 113,000 words), except where this site's terms differ (German: "Kill Switch", as this
   site's edition prints it, never "Sollbruchstelle").
4. `python batchize.py <lang>` (prints the generation and the count) and `python prompts.py write <lang>`: slices of
   about 1,100 words in the site's reading order, one prompt file each.
5. The Workflow tool with `translate.workflow.js`, args `{"lang": "de", "batches": [...]}`: one agent per slice
   writes its patch. Run it in groups (German: the core rooms b000-b128, the books, then the films and llms.txt).
6. `python merge.py <lang>`, then `python qa.py <lang>`: the gate (tokens, numbers digit for digit, locked names,
   nothing left English). `python qa.py <lang> --redo` takes failing translations out of the memory; batchize and
   the workflow translate them again.
7. `python build.py <lang>`: the language's pages under /<lang>/ (the old edition's /de/ front page and
   /de/what-is-the-420-code/ are replaced by the word-for-word twins), its llms.txt, the English pages' language
   menu pointed at each page's twin, the sitemap. `--draft --out DIR` makes a trial build anywhere, English filling
   what is not yet translated. `python verify_i18n.py <lang>`: every page's tag skeleton equals the English
   page's, every link lands on a file, the menu, the canonical address and the canon line are right.
8. Commit with `git add` of exactly the files (never `-A`: the tree holds translation PDFs in progress), then push
   to main: that is a publish.

⛔ `i18n/frontdoor/build.py` builds the old editions' front pages; it must never run for a language this engine has
built, or it would overwrite the word-for-word front page with the old edition.

What stays English for now, and why: the search box's own few words and its index (a script; the results lead to
the English pages); the PDFs (the papers are English; the books' translations in /<lang>/ are G's separate editions).
