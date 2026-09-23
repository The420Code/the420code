# WALL UPDATE — AP31 and the registry, 23 September 2026

For WC. This is the part of bundle v11 that is not the library. It carries one paper's republish and two registry entries. Do it in the same deploy as the library, after it.

## 1. AP31 The Alignment — republish with its dated notes

    site-root/AP31_The_Alignment.pdf   ->   the420code.org/AP31_The_Alignment.pdf   (replaces the current file)

The paper's body is unchanged, word for word. It gains a Dated notes section on its own page, after "What This Establishes and What Remains Open" and before "Claim Summary": four matters of record dated 23 September 2026. The contents page gains the entry and two page numbers move. 43 pages.

The proofs page (/proofs/) needs no change: AP31's blurb, its switch count and its link stay as they are.

## 2. The instruments folder for AP31 — new

    site-root/proofs/instruments/AP31/   ->   the420code.org/proofs/instruments/AP31/

Four files, the way AP12, AP28 and AP30 keep theirs:

    AP31_The_Alignment_notes_1to4_published_2026-09-23.pdf   the republished paper, dated copy
    DATED_NOTES_2026-09-23.md                                the four notes as plain text
    Debt_20_the_stability_proof_for_epsilon_2026-09-23.pdf    the derivation the payment stands on, with its check
    debt20_corridor_check.py                                  the check's script

No page links to these yet. They are the record, reachable by address, like the other instruments folders.

## 3. The registry — two entries change, no count moves

Registry version v5.35 of 21 September 2026 becomes v5.36 of 23 September 2026. Six hundred and four switches, five hundred and eighty-four live, two fired: unchanged. No status changes. The debts table is unchanged — Debts 20 to 23 are AP31's own and live in the paper, not in the registry's table.

Two descriptions gain text. Replace the description field of each with the text below, exactly. `registry_patch_2026-09-23.json` beside this file carries the same two strings for /killswitches.json.

KS-31.2 — description becomes:

> ε-optimality. Claim sharpened at the structural register by dated note of 23 September 2026 at AP31, on the payment of AP31's Debt 20 at the structural register (DERIVED-CONDITIONAL, the class of KS-COUP.1): the bias ε toward the organism uniquely maximises the coupled viability corridor; below ε the corridor collapses at the organism's drift rate; above ε it is strictly narrower at every bias, and it collapses where the losses the rule lets through outpace cooperative coupling's widening. Test bounded (D113): exhibit a bias other than ε that produces a wider coupled corridor sustained over three drift-times of the organism, τ = 1/a as AP01 D2.2 defines the drift timescale. Owed at the formal register: the statement on AP01 Paper D's joint viability kernel; the collapse above ε at every bias, with Step 2's information loop written as a term; the thresholds. The derivation is at /proofs/instruments/AP31/.

Status line unchanged: LIVE — STRUCTURAL.

KS-31.7 — description becomes:

> Civilisational test (MASTER). Reading adopted by dated note of 23 September 2026 at AP31: "structurally coherent" is judged before the outcome, by the load-bearing test — remove the commitment to the foundation and watch the system's own predictions, the counter-test of Addendum B fenced at KS-31.B2. A system that passed the test and then destabilises civilisation fires the switch. It is not reclassified after the fact.

Status line unchanged: LIVE — EMPIRICAL.

The registry's own PDF, /Master_Kill_Switch_Registry.pdf, is built by the registry desk from the registry file; it follows at v5.36 when that desk republishes it. If your pipeline builds the page and the PDF from /killswitches.json, the patch is all you need; if the registry desk's file is the source, apply the two entries there and rebuild. Either way the page shows v5.36 · 23 September 2026 in its header.

## 4. Nothing else on the wall moves

The physics page, the pre-registration page, the One Awareness page, the home page and the Ø Models pages are untouched by this deploy.

## Checks after deploy

Open /AP31_The_Alignment.pdf and find "Dated notes" on the contents page, pointing at page 38.

Open /proofs/instruments/AP31/DATED_NOTES_2026-09-23.md and see the four notes.

Open /killswitches/#ks-31-2 and read the sharpened claim and the three-drift-times test; open /killswitches/#ks-31-7 and read the reading. The header says v5.36 · 23 September 2026. The counts are the ones above.

Open /five-doors/the-interior/14-the-epsilon-bias/ and see the same three-drift-times fence in the book's own words, so the book and the registry agree.
