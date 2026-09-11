# The front door, in thirteen languages

The source of every edition of `/what-is-the-420-code/`. Each `frontdoor_strings_<lang>.json`
holds the page's 89 translatable strings. `python build.py` rebuilds all twelve editions from
them around the English page, so structure, links, anchors, type and the axiom line are identical
in every edition, and gives each edition's home page the same drop-down header as its front door.

- **Edit a translation here, never on the page.** A page edit is lost at the next rebuild.
- Keys, their order, every inline tag and every `href` match `frontdoor_strings_en.json`.
- The axiom line is never in a table. It is the template's, character for character, on every page.
- Room links (`#axiom #physics #models #five-doors #confirm-the-math`) are localised at build
  time. Per-paper anchors and the Notebooks list exist only in English and stay pointed there.
- Arabic is built right-to-left, with dates, ids and formulas isolated in `<bdi>`, except the
  axiom paragraph, which stands alone, is set LTR, and is left exactly as written.

Translated by the second desk on 10 September 2026, reviewed blind, and corrected on
11 September 2026 to G's rulings: chain.5 reads *through* its own opening (the moment, a ratio);
the axiom room is always *1 Axiom*; AP52 is *Reading Relativity*.
