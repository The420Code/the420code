> **SUPERSEDED the same day by v3.** v2's *withdrawal of v1* stands and is not in question. v2's own **count** does not: it reported 21 of record and 28 diverged, and the true figures are **26 and 23**. v2's checker dropped the Contents block on the published side and not on the source side, so a paper's own front matter came back as prose the published paper was missing; it also read the typesetter's `@@` directives as prose. Both are corrected in v3, which is the report to read. This file is kept, never deleted, as the record of what was claimed and why it was wrong.

---

# Sources of record — AP01–AP49 — v2, 7 September 2026

> **v1 of this report is withdrawn as a ruling.** It concluded *"all 43 diverge; the harvest must never touch OneDrive"*. That conclusion is not established and must not be relied on. v1 is kept at `sources-of-record-2026-09-07-v1-SUPERSEDED.md`, never deleted, as the record of what was claimed and why it was wrong.

## Why v1 was wrong — two faults, not one

1. **The test could not tell layout from content.** It compared sliding chunks and reported percentages. Run as a control on a document against a PDF made from that same document, it reported 16% diverged. A test that fails its own self-comparison cannot be the gate, and everything v1 ruled on it falls with it.
2. **It audited the wrong folder.** v1 checked `00 - KDP/420code_final/Standalone_Artists_Proofs/` only. The formatted sources actually used for publication live in `000 - AP's and Notebooks/Final Documents To Publish/Formatted/`, which v1 never opened. Most papers are of record there.

Both faults were mine. The first was caught by the desk's control, the second by MC's own harvester, which had been pointing at the right folder all along.

## The test of record

Paragraph-level, layout-normalised, reporting paragraphs and never percentages:

1. every source paragraph and table cell of ≥ 60 characters, in document order;
2. both sides normalised — whitespace collapsed, curly quotes and every dash and non-breaking hyphen mapped to ASCII, emphasis markers stripped, and the Contents block, running heads and bare page numbers dropped from the PDF;
3. **forward** — each source paragraph's first 70 characters must occur in the published text; **reverse** — each published sentence of ≥ 60 characters must occur in the source, split within a line and never across one;
4. the missing paragraphs are printed verbatim, both directions, so each is classified in seconds as content or layout;
5. **control** — AP49, whose PDF is built from its own markdown, must come out empty in both directions.

**The control passes: AP49 gives 0 and 0.** It did not at first — the reverse direction produced 25 false divergences because PDF extraction glues a heading onto the sentence after it, and the glued string exists in no source. Splitting sentences within a line rather than across the document fixed it. The control earned its place.

## Result

| Verdict | Papers |
|---|---|
| **OF RECORD** | 21 |
| **DIVERGED** | 28 |

**Of record (21):** AP07, AP13, AP17, AP20, AP25, AP29, AP30, AP31, AP32, AP33, AP34, AP35, AP36, AP37, AP38, AP39, AP40, AP41, AP42, AP48, AP49

**Diverged (28):** AP01, AP02, AP03, AP04, AP05, AP06, AP08, AP09, AP10, AP11, AP12, AP14, AP15, AP16, AP18, AP19, AP21, AP22, AP23, AP24, AP26, AP27, AP28, AP43, AP44, AP45, AP46, AP47

Every paper now has `proofs/instruments/AP<nn>/SOURCE_OF_RECORD.md`. Where a paper is of record the verified source sits beside it; where it diverged, **no file is placed**, so nothing can be harvested from it by mistake, and the divergent paragraphs are printed there verbatim.

## Paper by paper

| Paper | Verdict | Source | Found in | Paragraphs | Content divergences | Layout items |
|---|---|---|---|---|---|---|
| **AP01** | DIVERGED | `AP01_The_Actualization_State.docx` | Formatted | 1300 | 72 + 2 | 3 |
| **AP02** | DIVERGED | `AP02_The_Operator_FINAL_v6.docx` | Formatted | 338 | 1 + 0 | 5 |
| **AP03** | DIVERGED | `AP03_The_Ratio_FINAL.docx` | Formatted | 297 | 3 + 0 | 8 |
| **AP04** | DIVERGED | `AP04_The_Loop_Hypothesis_FINAL.docx` | Formatted | 155 | 1 + 1 | 5 |
| **AP05** | DIVERGED | `AP05_The_Break_FINAL.docx` | Formatted | 248 | 3 + 1 | 16 |
| **AP06** | DIVERGED | `AP06_The_Leakage_Constant_FINAL.docx` | Standalone | 199 | 3 + 2 | 12 |
| **AP07** | OF RECORD | `AP07_The_Record_Measure_FINAL.docx` | Formatted | 206 | 0 + 0 | 0 |
| **AP08** | DIVERGED | `AP08_The_Identity_FINAL.docx` | Formatted | 316 | 6 + 0 | 10 |
| **AP09** | DIVERGED | `AP09_The_Break_Empty_Set_FINAL.docx` | Formatted | 435 | 11 + 6 | 6 |
| **AP10** | DIVERGED | `AP10_The_Dimension_FINAL.docx` | Formatted | 311 | 7 + 0 | 9 |
| **AP11** | DIVERGED | `AP11_The_Spin_FINAL.docx` | Formatted | 202 | 35 + 17 | 19 |
| **AP12** | DIVERGED | `AP12_The_Limit_FINAL.docx` | Formatted | 204 | 1 + 0 | 0 |
| **AP13** | OF RECORD | `AP13_The_Grain_FINAL.docx` | Formatted | 207 | 0 + 0 | 0 |
| **AP14** | DIVERGED | `AP14_The_Correction_v2.docx` | Formatted | 186 | 21 + 11 | 11 |
| **AP15** | DIVERGED | `AP15_The_Connection_v2.docx` | Formatted | 284 | 6 + 0 | 6 |
| **AP16** | DIVERGED | `AP16_The_Break_Electroweak_v2.docx` | Formatted | 216 | 6 + 0 | 2 |
| **AP17** | OF RECORD | `AP17_The_Room_FINAL.docx` | Formatted | 194 | 0 + 0 | 2 |
| **AP18** | DIVERGED | `AP18_The_Floor_FINAL.docx` | Formatted | 156 | 7 + 0 | 6 |
| **AP19** | DIVERGED | `AP19_The_Direction_v2.docx` | Formatted | 243 | 4 + 0 | 4 |
| **AP20** | OF RECORD | `AP20_The_Proof_FINAL_v3.docx` | Formatted | 309 | 0 + 0 | 10 |
| **AP21** | DIVERGED | `AP21_The_Web_FINAL.docx` | Formatted | 178 | 6 + 1 | 6 |
| **AP22** | DIVERGED | `AP22_The_Ledger_FINAL.docx` | Formatted | 299 | 28 + 5 | 9 |
| **AP23** | DIVERGED | `AP23_The_Single_Record_FINAL.docx` | Formatted | 162 | 3 + 0 | 0 |
| **AP24** | DIVERGED | `AP24_The_Residual_v2.docx` | Formatted | 232 | 7 + 0 | 0 |
| **AP25** | OF RECORD | `AP25_The_Measure_FINAL.docx` | Formatted | 148 | 0 + 0 | 0 |
| **AP26** | DIVERGED | `AP26_The_Surplus_FINAL.docx` | Formatted | 144 | 2 + 0 | 3 |
| **AP27** | DIVERGED | `AP27_The_Harmonics_v2.docx` | Formatted | 202 | 25 + 2 | 1 |
| **AP28** | DIVERGED | `AP28_The_Constant_v2.docx` | Formatted | 194 | 4 + 0 | 0 |
| **AP29** | OF RECORD | `AP29_The_Actualization_Proof_FINAL_v2.docx` | Formatted | 133 | 0 + 0 | 0 |
| **AP30** | OF RECORD | `AP30_The_Resistance_FINAL_v1_0_dated_notes_2` | instruments | 152 | 0 + 0 | 1 |
| **AP31** | OF RECORD | `AP31_The_Alignment_FINAL_v3.docx` | Formatted | 287 | 0 + 0 | 1 |
| **AP32** | OF RECORD | `AP32_The_Correction_FINAL.docx` | Formatted | 210 | 0 + 0 | 1 |
| **AP33** | OF RECORD | `AP33_The_Boundary_FINAL.docx` | Formatted | 217 | 0 + 0 | 1 |
| **AP34** | OF RECORD | `AP34_The_Inversion_FINAL.docx` | Formatted | 179 | 0 + 0 | 1 |
| **AP35** | OF RECORD | `AP35_The_Ledger_FINAL_v3.docx` | Formatted | 214 | 0 + 0 | 1 |
| **AP36** | OF RECORD | `AP36_The_Feed_FINAL.docx` | Formatted | 231 | 0 + 0 | 1 |
| **AP37** | OF RECORD | `AP37_The_First_Boundary_FINAL.docx` | Formatted | 197 | 0 + 0 | 1 |
| **AP38** | OF RECORD | `AP38_The_Exit_FINAL_v2.docx` | Formatted | 128 | 0 + 0 | 0 |
| **AP39** | OF RECORD | `AP39_The_Scaffold_FINAL_v2.docx` | Formatted | 350 | 0 + 0 | 0 |
| **AP40** | OF RECORD | `AP40_The_Irrational_FINAL_v3.docx` | Formatted | 282 | 0 + 0 | 8 |
| **AP41** | OF RECORD | `AP41_The_Loop_FINAL.docx` | Formatted | 150 | 0 + 0 | 4 |
| **AP42** | OF RECORD | `AP42_The_Clock_FINAL.docx` | Formatted | 137 | 0 + 0 | 0 |
| **AP43** | DIVERGED | `AP43_The_Gravity_of_Possibilities_FINAL_v3.d` | Formatted | 601 | 1 + 0 | 12 |
| **AP44** | DIVERGED | `AP44_The_Snap_FINAL_v1_0.md` | instruments | 163 | 2 + 0 | 8 |
| **AP45** | DIVERGED | `AP45_The_Blink_FINAL_v1_7.md` | instruments | 234 | 1 + 0 | 0 |
| **AP46** | DIVERGED | `AP46_The_Stretch_FINAL_v1_5.md` | instruments | 206 | 1 + 0 | 0 |
| **AP47** | DIVERGED | `AP47_The_Flip_FINAL_v3.md` | instruments | 88 | 1 + 0 | 8 |
| **AP48** | OF RECORD | `AP48_The_Assembly_FINAL_v1_1.docx` | instruments | 221 | 0 + 0 | 0 |
| **AP49** | OF RECORD | `AP49_The_Hold_FINAL_v1_0.md` | instruments | 113 | 0 + 0 | 0 |

## What the divergences are

They are not errors in the published corpus. Each is either a pre-publication draft difference — as AP30's seventeen turned out to be — or a paragraph edited after publication, which becomes a dated note. **That reading is G's.** The paragraphs are printed verbatim in each paper's `SOURCE_OF_RECORD.md` so the judgement is made on the text.

Note AP44–AP47: each shows one or two content items against its own markdown instrument, from which its PDF was built. Those are the likeliest remaining checker artifacts and should be read first — if they are artifacts, the checker needs one more fix; if they are real, four freeze bundles have a discrepancy worth knowing about.

*Run 2026-09-07. Nothing in OneDrive or in anything published was modified.*
