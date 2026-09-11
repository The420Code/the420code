# The front door, in thirteen languages

The source of every edition of `/what-is-the-420-code/`, and of the header that every page with
the Rooms drop-down carries.

- `frontdoor_strings_<lang>.json`: the page's translatable strings, with the closing lines. `python build.py`
  rebuilds all twelve editions from them around the English page, so structure, links, anchors,
  type and the axiom line are identical in every edition.
- `header.py`: the header. Rooms, and beside it the language drop-down, a button showing the flag
  of the language being read. A flag leads to the same page in the chosen language wherever the
  page exists in it: front door to front door, home to home, Proofs to that edition's proofs room.
  One row at every width; on a narrow phone the door's name wraps inside its own box and never
  splits *The 420 Code*. build.py uses it for the twelve editions; the three English pages that
  carry Rooms (home, front door, Proofs) are made by the same code.
- `lang_entrance.py`: each edition's entrance strings, level with its live home page.

## Rules

- **Edit a translation here, never on the page.** A page edit is lost at the next rebuild.
- Keys, their order, every inline tag and every `href` match `frontdoor_strings_en.json`.
- The axiom line is never in a table. It is the template's, character for character, on every page.
- Room links (`#axiom #physics #models #five-doors #confirm-the-math`) are localised at build
  time. Per-paper anchors and the Notebooks list exist only in English and stay pointed there.
- Arabic is built right-to-left, with dates, ids and formulas isolated in `<bdi>`, except the
  axiom paragraph, which stands alone, is set LTR, and is left exactly as written. Its header is
  the mirror image of the others, the same on its home page and its front door.
- *Actualization State* stays in English in every edition but Spanish, which uses the corpus's
  locked *Estado de Actualización*. The other editions' decision (DEC-AS) is still open.

## History

- 10 September 2026: translated by the second desk, reviewed blind.
- 11 September 2026: corrected to G's rulings. chain.5 reads *through* its own opening (the
  moment, a ratio); the axiom room is always *1 Axiom*; AP52 is *Reading Relativity*.
- 11 September 2026, later: G's edits to the English page carried into all twelve tables. The
  edits are: what a record is; "what I ought to do"; the Actualization State; the outflow; the
  neck as one sheet of glass; the one Operator expressed as many; the operator and the ethic
  rewritten. The tables were re-keyed around the paragraphs the edits add and split, and a
  second reviewer read every new string blind.
