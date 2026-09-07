# Sources of record — AP01–AP49 — v3, 7 September 2026

**26 of record. 23 diverged.** This is the report to read. Two earlier reports of the same day are kept beside it, superseded and never deleted:

- **v1** ruled *"all 43 diverge; the harvest must never touch OneDrive"*. Withdrawn. Its test compared sliding chunks and reported percentages, and on a control — a document against a PDF made from that same document — it reported 16% diverged. It also audited only `00 - KDP/420code_final/Standalone_Artists_Proofs/`, never `000 - AP's and Notebooks/Final Documents To Publish/Formatted/`, where most papers are of record. Both faults were mine; the first was caught by the desk's control, the second by MC's harvester, which had been pointing at the right folder all along.
- **v2** replaced the test correctly but miscounted: 21 and 28. Its checker dropped the Contents block on the published side and not on the source side, so a paper's own front matter came back as prose the published paper was missing — AP44 and AP47 were failed on nothing but their tables of contents — and it read the typesetter's `@@TITLE` / `@@SUB` directive lines, which are never printed, as prose, which failed AP45 and AP46. v2's withdrawal of v1 stands; v2's count does not.

Two corrections in one day on the same question is worth stating plainly rather than burying: the ruling that AP44–AP47 diverged from their own freeze bundles was wrong, and **no paper's published text was ever in doubt** — what was in doubt was my checker.

## The test of record

Paragraph-level, layout-normalised, reporting paragraphs and never percentages:

1. every source paragraph and table cell of ≥ 60 characters, in document order, with the typesetter's `@@` directive lines excluded — they are instructions to the compositor, not text;
2. both sides normalised — whitespace collapsed, curly quotes and every dash and non-breaking hyphen mapped to ASCII, emphasis markers stripped, and the Contents block, running heads and bare page numbers dropped from the PDF;
3. **forward** — each source paragraph's first 70 characters must occur in the published text; **reverse** — each published sentence of ≥ 60 characters must occur in the source, split within a line and never across one;
4. a forward miss that occurs in **the published paper's own Contents block** is front matter, not a divergence. The Contents block the checker strips from the body is not rubbish: it is this paper's own list of its front matter, and it settles the question by looking at the published paper rather than by teaching the checker each source file's markdown dialect;
5. the missing paragraphs are printed verbatim, both directions, so each is classified in seconds as content or layout;
6. **controls** — AP49, whose PDF is built from its own markdown, and AP30, whose PDF was built from the dated-notes document beside it, must both come out empty in both directions.

**Both controls pass, 0 and 0.** AP49 did not at first: the reverse direction produced 25 false divergences because PDF extraction glues a heading onto the sentence after it, and the glued string exists in no source. Splitting sentences within a line rather than across the document fixed it. AP30's control was still showing one item at v2 and is clean at v3. The controls earned their place twice.

## Result

| Verdict | Papers |
|---|---|
| **OF RECORD** | 26 |
| **DIVERGED** | 23 |

**Of record (26):** AP07, AP13, AP17, AP20, AP25, AP29, AP30, AP31, AP32, AP33, AP34, AP35, AP36, AP37, AP38, AP39, AP40, AP41, AP42, AP43, AP44, AP45, AP46, AP47, AP48, AP49

**Diverged (23):** AP01, AP02, AP03, AP04, AP05, AP06, AP08, AP09, AP10, AP11, AP12, AP14, AP15, AP16, AP18, AP19, AP21, AP22, AP23, AP24, AP26, AP27, AP28

Every paper has `proofs/instruments/AP<nn>/SOURCE_OF_RECORD.md`. Where a paper is of record the verified source sits beside it with the published digest; where it diverged, **no file is placed**, so nothing can be harvested from it by mistake, and the divergent paragraphs are printed there verbatim.

### One item cleared by inspection

**AP43.** One item: the definition beginning "where R_μν is a Ricci-analog curvature". It is in the published paper, on page 47. PyMuPDF lifts the script-ℛ and script-ℐ glyphs out of reading order and emits them on their own lines after the words they belong to, so the source's plain R has no counterpart at that position in the extracted text. Published, as extracted: "where \n_μν is a Ricci-analog curvature on the amplitude landscape \n𝒡\n(configuration space with a metric modulated by the Born density), and \n^B_μν\n𝒣\nis a Born stress-energy tensor...". Same text; a glyph-ordering artifact of the PDF text layer. It is recorded on the paper's own `SOURCE_OF_RECORD.md` as cleared by eye and not by the checker, so the clearance is auditable. It is the only such clearance in the set.

## The four freeze bundles, settled

v2 flagged AP44, AP45, AP46 and AP47 as each showing one or two content items against their own markdown instruments — the files their PDFs were built from — and said they should be read first because, if real, four freeze bundles had a discrepancy. **They were not real.** All four are of record:

| Paper | What v2 flagged | What it is |
|---|---|---|
| AP44 | *ten vertices, twenty-one edges: constitution at nodes, flow along edges* and *KS-CCC.1 through KS-CCC.6, with KS-CCC.4 split into 4a and 4b* | two sub-lines inside the paper's own `# Contents` block, lines 91 and 107 |
| AP45 | `@@TITLE The Blink @@AP Artist's Proof 45 @@DOMAIN …` | the typesetter's directive block at the head of the file, never printed |
| AP46 | `@@TITLE The Stretch @@AP Artist's Proof 46 @@DOMAIN …` | the same |
| AP47 | *KS-NPP.1, fired and shown forever · The proton elimination at the named bar* | a Contents sub-line, line 41. The checker's heading test was defeated by the full stop inside `KS-NPP.1` |

## Paper by paper

| Paper | Verdict | Source | Found in | Paragraphs | Content divergences | Front matter |
|---|---|---|---|---|---|---|
| **AP01** | DIVERGED | `AP01_The_Actualization_State.docx` | Formatted | 1300 | 72 + 2 | 3 |
| **AP02** | DIVERGED | `AP02_The_Operator_FINAL_v6.docx` | Formatted | 338 | 1 + 0 | 5 |
| **AP03** | DIVERGED | `AP03_The_Ratio_FINAL.docx` | Formatted | 297 | 3 + 0 | 8 |
| **AP04** | DIVERGED | `AP04_The_Loop_Hypothesis_FINAL.docx` | Formatted | 155 | 1 + 1 | 5 |
| **AP05** | DIVERGED | `AP05_The_Break_FINAL.docx` | Formatted | 248 | 3 + 1 | 16 |
| **AP06** | DIVERGED | `AP06_The_Leakage_Constant_FINAL.docx` | Standalone | 199 | 3 + 2 | 12 |
| **AP07** | OF RECORD | `AP07_The_Record_Measure_FINAL.docx` | Formatted | 206 | 0 + 0 | 0 |
| **AP08** | DIVERGED | `AP08_The_Identity_FINAL.docx` | Formatted | 316 | 5 + 0 | 11 |
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
| **AP30** | OF RECORD | `AP30_The_Resistance_FINAL_v1_0_dated_notes_2` | instruments | 160 | 0 + 0 | 1 |
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
| **AP43** | OF RECORD ·  by inspection | `AP43_The_Gravity_of_Possibilities_FINAL_v3.d` | Formatted | 601 | 1 + 0 | 12 |
| **AP44** | OF RECORD | `AP44_The_Snap_FINAL_v1_0.md` | instruments | 163 | 0 + 0 | 10 |
| **AP45** | OF RECORD | `AP45_The_Blink_FINAL_v1_7.md` | instruments | 233 | 0 + 0 | 1 |
| **AP46** | OF RECORD | `AP46_The_Stretch_FINAL_v1_5.md` | instruments | 205 | 0 + 0 | 1 |
| **AP47** | OF RECORD | `AP47_The_Flip_FINAL_v3_dated_notes_2026-09-0` | instruments | 92 | 0 + 0 | 9 |
| **AP48** | OF RECORD | `AP48_The_Assembly_FINAL_v1_1.docx` | instruments | 221 | 0 + 0 | 0 |
| **AP49** | OF RECORD | `AP49_The_Hold_FINAL_v1_0.md` | instruments | 113 | 0 + 0 | 0 |

## What the remaining divergences are

They are not errors in the published corpus. Each is either a pre-publication draft difference — as AP30's seventeen turned out to be — or a paragraph edited after publication, which becomes a dated note. **That reading is G's.** The paragraphs are printed verbatim in each paper's `SOURCE_OF_RECORD.md` so the judgement is made on the text and not on a percentage.

The 23 that diverge cannot take the AP30 republish procedure — appending dated notes to a locked body requires the document the locked body was set from. Any republish of one of them would be a re-typesetting, which is the one thing that can put an invisible error into a paper that is otherwise correct.

*Run 2026-09-07. Nothing in OneDrive and nothing published was modified.*

**The checker is beside this report** at `reports/of_record_2026-09-07.py`, so the ruling is
reproducible and MC has the exact file to fold into `museum/check_of_record.py`. Run it as
`python of_record_2026-09-07.py <source> <published.pdf>`.

*9 September 2026: AP30 and AP47 were republished with dated notes on that day. Their rows above
are re-verified against the new PDFs and carry the new digests; both remain of record.*
