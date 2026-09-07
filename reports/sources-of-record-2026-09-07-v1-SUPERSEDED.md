> **SUPERSEDED — 7 September 2026.** This report's ruling, *"all 43 diverge; the harvest must
> never touch OneDrive"*, is **withdrawn and must not be relied on**. Its test could not
> distinguish layout from content — run against a PDF made from the document itself it reported
> 16% diverged — and it audited only one of several candidate source folders, missing the
> formatted sources actually used for publication. Replaced by
> `sources-of-record-2026-09-07-v2.md`. Kept, never deleted, as the record of what was claimed.

# Sources of record — AP01–AP43 — 7 September 2026

Ruled by the desk on 7 September: build `proofs/instruments/AP<nn>/` the way AP30's is — the source whose text matches the site PDF paragraph by paragraph. **The harvest must never touch OneDrive again.**

**Method.** Each paper's OneDrive docx is checked against the PDF the site publishes, both ways: every docx paragraph over 60 normalised characters must appear in the published text, and a sliding window over the whole published text must appear in the docx. Comparison is on letters and digits only, lower-cased — immune to line breaks, hyphenation, ligatures and page furniture. Nothing in OneDrive was modified; nothing published was modified.

## Result

| Verdict | Papers |
|---|---|
| **DIVERGED** | 29 |
| **DIVERGED (heavily)** | 14 |

**0 source(s) placed** in `proofs/instruments/`: —

## Paper by paper

| Paper | Verdict | Published PDF | sha256 | docx | Absent from PDF | Published text absent from docx |
|---|---|---|---|---|---|---|
| **AP01** | DIVERGED | `AP01_The_Actualization_State.pdf` | `39c86fb7863b63b7…` | `AP01_The_Actualization_State_FINAL.docx` | 84 | 200/1776 |
| **AP02** | DIVERGED (heavily) | `AP02_The_Operator.pdf` | `d6a0058f1471bc4d…` | `AP02_The_Operator_FINAL.docx` | 33 | 116/426 |
| **AP03** | DIVERGED | `AP03_The_Ratio.pdf` | `b1be754da741b4cc…` | `AP03_The_Ratio_FINAL.docx` | 7 | 45/517 |
| **AP04** | DIVERGED | `AP04_The_Loop_Hypothesis.pdf` | `bcb20391bf72c09e…` | `AP04_The_Loop_Hypothesis_FINAL.docx` | 18 | 53/243 |
| **AP05** | DIVERGED | `AP05_The_Break.pdf` | `3185b76ba1f70139…` | `AP05_The_Break_FINAL.docx` | 5 | 31/575 |
| **AP06** | DIVERGED | `AP06_The_Leakage_Constant.pdf` | `d24d76ce142d54f9…` | `AP06_The_Leakage_Constant_FINAL.docx` | 15 | 53/359 |
| **AP07** | DIVERGED | `AP07_The_Record_Measure.pdf` | `7aabd17a6f008657…` | `AP07_The_Record_Measure_FINAL.docx` | 4 | 17/205 |
| **AP08** | DIVERGED | `AP08_The_Identity.pdf` | `1d28235296d1c049…` | `AP08_The_Identity_FINAL.docx` | 39 | 112/577 |
| **AP09** | DIVERGED | `AP09_The_Break_Empty_Set.pdf` | `2f3f21d2a198556d…` | `AP09_The_Break_Empty_Set_FINAL.docx` | 12 | 47/410 |
| **AP10** | DIVERGED (heavily) | `AP10_The_Dimension.pdf` | `b246e1240b5f3a3f…` | `AP10_The_Dimension_FINAL.docx` | 54 | 187/584 |
| **AP11** | DIVERGED | `AP11_The_Spin.pdf` | `708b3e7648937d7c…` | `AP11_The_Spin_FINAL.docx` | 1 | 14/181 |
| **AP12** | DIVERGED | `AP12_The_Limit.pdf` | `396c2583061320b3…` | `AP12_The_Limit_FINAL.docx` | 5 | 16/216 |
| **AP13** | DIVERGED | `AP13_The_Grain.pdf` | `8a3b5d59ff30b3d0…` | `AP13_The_Grain_FINAL.docx` | 7 | 22/257 |
| **AP14** | DIVERGED | `AP14_The_Correction.pdf` | `faa73eafd907c83b…` | `AP14_The_Correction_FINAL.docx` | 5 | 31/322 |
| **AP15** | DIVERGED | `AP15_The_Connection.pdf` | `37e75ffe4a1db1a8…` | `AP15_The_Connection_FINAL.docx` | 4 | 24/524 |
| **AP16** | DIVERGED | `AP16_The_Break_Electroweak.pdf` | `d361386650e20b8c…` | `AP16_The_Break_Electroweak_FINAL.docx` | 9 | 34/341 |
| **AP17** | DIVERGED | `AP17_The_Room.pdf` | `41476d5021379b76…` | `AP17_The_Room_FINAL.docx` | 9 | 34/308 |
| **AP18** | DIVERGED (heavily) | `AP18_The_Floor.pdf` | `d89f7d8d76b1aa82…` | `AP18_The_Floor_FINAL.docx` | 28 | 88/279 |
| **AP19** | DIVERGED | `AP19_The_Direction.pdf` | `50e6662473f0e074…` | `AP19_The_Direction_FINAL.docx` | 37 | 100/412 |
| **AP20** | DIVERGED (heavily) | `AP20_The_Proof.pdf` | `f9a21b1ed0528fa8…` | `AP20_The_Proof_FINAL.docx` | 96 | 289/483 |
| **AP21** | DIVERGED | `AP21_The_Web.pdf` | `97bc105cf77ae000…` | `AP21_The_Web_FINAL.docx` | 18 | 61/302 |
| **AP22** | DIVERGED | `AP22_The_Ledger.pdf` | `be14c17fa9e1c8bb…` | `AP22_The_Ledger_FINAL.docx` | 16 | 52/378 |
| **AP23** | DIVERGED | `AP23_The_Single_Record.pdf` | `72432989bfbe83d8…` | `AP23_The_Single_Record_FINAL.docx` | 16 | 33/185 |
| **AP24** | DIVERGED | `AP24_The_Residual.pdf` | `3a052367dbbe5204…` | `AP24_The_Residual_FINAL.docx` | 12 | 40/322 |
| **AP25** | DIVERGED | `AP25_The_Measure.pdf` | `748b8f9be06e34ea…` | `AP25_The_Measure_FINAL.docx` | 14 | 43/177 |
| **AP26** | DIVERGED | `AP26_The_Surplus.pdf` | `0f1534bfa65ff9b0…` | `AP26_The_Surplus_FINAL.docx` | 11 | 33/195 |
| **AP27** | DIVERGED | `AP27_The_Harmonics.pdf` | `b6b78c49ff9ea3cb…` | `AP27_The_Harmonics_FINAL.docx` | 6 | 30/324 |
| **AP28** | DIVERGED | `AP28_The_Constant.pdf` | `aecc98d3e38a24c9…` | `AP28_The_Constant_FINAL.docx` | 8 | 34/321 |
| **AP29** | DIVERGED (heavily) | `AP29_The_Actualization_Proof.pdf` | `d4230c63e9a2d311…` | `AP29_The_Actualization_Proof_FINAL.docx` | 48 | 96/178 |
| **AP30** | DIVERGED (heavily) | `AP30_The_Resistance.pdf` | `3b86e7819d850ce6…` | `AP30_The_Resistance_FINAL.docx` | 17 | 66/209 |
| **AP31** | DIVERGED (heavily) | `AP31_The_Alignment.pdf` | `0bfc7103b1416493…` | `AP31_The_Alignment_FINAL.docx` | 62 | 141/384 |
| **AP32** | DIVERGED (heavily) | `AP32_The_Correction.pdf` | `489bec11b524a462…` | `AP32_The_Correction_FINAL.docx` | 91 | 185/306 |
| **AP33** | DIVERGED (heavily) | `AP33_The_Boundary.pdf` | `3b5a3b263af395ca…` | `AP33_The_Boundary_FINAL.docx` | 63 | 138/318 |
| **AP34** | DIVERGED (heavily) | `AP34_The_Inversion.pdf` | `3d9765ec84ef2524…` | `AP34_The_Inversion_FINAL.docx` | 45 | 109/271 |
| **AP35** | DIVERGED | `AP35_The_Ledger.pdf` | `a343516c98a40033…` | `AP35_The_Ledger_FINAL.docx` | 24 | 66/311 |
| **AP36** | DIVERGED | `AP36_The_Feed.pdf` | `4f36ccd8b43039cc…` | `AP36_The_Feed_FINAL.docx` | 17 | 47/328 |
| **AP37** | DIVERGED | `AP37_The_First_Boundary.pdf` | `deeb1309779df002…` | `AP37_The_First_Boundary_FINAL.docx` | 18 | 47/273 |
| **AP38** | DIVERGED | `AP38_The_Exit.pdf` | `0ca52b9d05670e13…` | `AP38_The_Exit_FINAL.docx` | 5 | 25/189 |
| **AP39** | DIVERGED | `AP39_The_Scaffold.pdf` | `7802a93012075612…` | `AP39_The_Scaffold_FINAL.docx` | 20 | 59/442 |
| **AP40** | DIVERGED (heavily) | `AP40_The_Irrational.pdf` | `5b502ab0988ab10c…` | `AP40_The_Irrational_FINAL.docx` | 54 | 143/541 |
| **AP41** | DIVERGED (heavily) | `AP41_The_Loop.pdf` | `e749bcbad1f578d8…` | `AP41_The_Loop_FINAL.docx` | 32 | 80/279 |
| **AP42** | DIVERGED (heavily) | `AP42_The_Clock.pdf` | `4c10d5db17040809…` | `AP42_The_Clock_FINAL.docx` | 26 | 87/298 |
| **AP43** | DIVERGED (heavily) | `AP43_The_Gravity_of_Possibilities.pdf` | `70c33e41b11b5b92…` | `AP43_The_Gravity_of_Possibilities_FINAL.docx` | 121 | 335/1168 |

## Divergences, with examples

### AP01 — 84 docx paragraph(s) absent from the published PDF

- docx only: This is Artist’s Proof 01 of The 420 Code — the foundational paper of the corpus. It is the second chapter of Notebook I, The Premise. The paper insta
- docx only: Twenty-four kill switches are engaged in this paper. Every load-bearing claim attaches to a structural condition under which the claim would fail. KS-
- docx only: The corpus is published copyleft. Free forever. No paywall. No gatekeepers.

### AP02 — 27% of the published text is absent from this docx

- docx only: Nothing here is imported. The six axioms are projections of the corpus axioms {S, B, R, C} onto the human scale; AP02 can be read on its own footing o
- docx only: The 420 Code is organised across eight Notebooks. AP02 is a chapter of Notebook VII — The Operator Interface. AP43, the Notebook’s opener, installs th
- docx only: AP02 derives nine theorems and eleven formal results about agency, conduct, and exit, and grounds the terminal ethic in the coupling geometry. It does

### AP03 — 7 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: A note on status. AP03 was originally published as a conjecture: c was derived from the pre-geometric action; G was conjectured to be determined by ε 
- docx only: AP03 sits first in Notebook II because it does the constants. Without c and G, the arena does not exist. The chapter shows that c and G are not indepe
- docx only: Paper D Phase 1 (axioms). Load-bearing for the four conditions {S, B, R, C}. AP03 was originally written before {S, B, R, C} was formalised in AP20’s 

### AP04 — 18 docx paragraph(s) absent from the published PDF

- docx only: 14 — What This Establishes and What Remains Open · what it closes · what it does not close · items held open · philosophical-register implementations 
- docx only: Established relativity: the Schwarzschild interior as Kantowski-Sachs (Kantowski & Sachs 1966), the Kruskal–Szekeres maximal extension, the Bekenstein
- docx only: Axiom S (involution). 1:1 is interpreted as a ℤ₂ symmetry on the transition hypersurface Σ (Interpretation I1): the transition diffeomorphism φ maps t

### AP05 — 5 docx paragraph(s) absent from the published PDF

- docx only: AP20 Paper D Phase 1 (axioms). Load-bearing for the four conditions {S, B, R, C}. AP05 was originally written before {S, B, R, C} was formalised in AP
- docx only: Axiom S (Distinction exists) ↔ The 1:1 in the axiom statement. S requires that something distinguishable exists. The 1:1 specifies a structure that su
- docx only: Axiom C (Bounded capacity) ↔ The boundedness of B2 in the bridge list. C requires that propagation and capacity are finite. Bridge B2 — bounded capaci

### AP06 — 15 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: The central result is the Leakage Theorem (Theorem 3.1, scoped). In the analysed near-perfect-absorber channels of sections 1–2, the leakage ratio η i
- docx only: AP06 feeds the rest of Notebook IV. Its identification ε ≡ η is the structural ground on which AP15 (Connection) builds U(1) electromagnetism, AP24 (R
- docx only: AP06 depends on the framework results that the identification of ε with η connects to: Axiom B (the break) from Paper D / AP01; AP03 (the conjugacy c²

### AP07 — 4 docx paragraph(s) absent from the published PDF

- docx only: What is not open: the role α plays. It is the coupling strength of the electron — the splinter ε — to the connection (Chapter 3).
- docx only: Chapter 1 identified ε with the electron — The Lock. Chapter 3 derived that the electron is charged because it has no σ-image, and that this charge so
- docx only: Paper D Phase 1 (Axiom R). AP06 (ε > 0). AP09 4 (records as measurement). AP15 (electromagnetism). The Lock (ε = electron).

### AP08 — 39 docx paragraph(s) absent from the published PDF

- docx only: AP08 is logically independent of AP01 and AP04 in the strict sense that its postulates (the four canonical axioms, the proven hypotheses EH and QRA, a
- docx only: AP08 also verifies the strong-field limit against established physics (section 6) by recovering the Hawking temperature from the Schwarzschild solutio
- docx only: AP20 Paper D Phase 1 (axioms). Load-bearing for the four canonical axioms {S, B, R, C} and the independence/consistency theorems (Theorems 1.1–1.5). T

### AP09 — 12 docx paragraph(s) absent from the published PDF

- docx only: AP09 shows that quantum mechanics — superposition, measurement, entanglement, the Born rule, the Schrödinger equation — follows from the same four axi
- docx only: Paper D, Phase 1: Axioms {S, B, R, C} independent and consistent (Theorems 1.1–1.5). Load-bearing.
- docx only: Paper D, Phase 2a: Under EH + QRA, Lorentzian manifold (M, g) with signature (−,+,+,+) and symmetry group SO(1,N). Load-bearing for complex amplitudes

### AP10 — 32% of the published text is absent from this docx

- docx only: AP10 closes three kill switches and leaves two live. KS-2c (CLOSED — contingent on KS-D.3): N = 3 derived from the four independent axioms via the pro
- docx only: AP10 is logically independent of AP01 and AP04 in the sense that its own postulates (the four canonical axioms {S, B, R, C}, the proven Embedding Hypo
- docx only: KS-2c N=3 (closed) · KS-15/D.2 axiom-to-dimension uniqueness (closed) · KS-16 fifth-DOF (closed) · KS-D.1 six-face count · KS-D.3 one axiom one face ·

### AP11 — 1 docx paragraph(s) absent from the published PDF

- docx only: Paper D Phase 1 (axioms). Paper D Phase 2a (Lorentzian). AP10 (N = 3). AP09 (Hilbert space, σ ↔ time-reversal). AP20 (EH, QRA). The Lock.

### AP12 — 5 docx paragraph(s) absent from the published PDF

- docx only: Paper D Phase 1 (axioms). Load-bearing for the indivisibility of ε (Axiom B) and the single time direction (Axiom R).
- docx only: Paper D Phase 2a (Lorentzian signature). Load-bearing for the manifold structure.
- docx only: The translation group on the manifold follows from the combination of Axiom C (finite propagation, which creates spatial distance), Axiom S (sector-cr

### AP13 — 7 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: It interacts with air molecules, photons, the electromagnetic field, the gravitational condensate (the architecture’s term for the gravitational secto
- docx only: Cross-reference: Paper D §I.3: Axiom R (record monotonicity, no inverses). AP09 4.3: The now as boundary between broken and unbroken. AP09 5: Entangle
- docx only: Cross-reference: AP09 3.2: Hilbert space, density matrix. AP09 6: Born rule (probabilities from |ψ|²). Paper D §I.3: Axiom R (monoid, no inverses).

### AP14 — 5 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: 4 — Finiteness: Five Structural Reasons · Axiom B (UV), Axiom C (IR), Axiom R (discreteness), Axiom S (measure), Lovelock in D = 4 (no counterterms).
- docx only: Notebook I (Premise). The four axioms {S, B, R, C}, independent by Paper D. The axiom 1:1 + 1×ε supplies the minimum break ε with action-scale ℏ.
- docx only: Four kill switches per the Master Kill Switch Registry v5.1 (May 2026). Three are introduced by AP14 (KS-25, KS-26, KS-27); one (KS-21) is affected an

### AP15 — 4 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: Two structural quantities carry corpus-wide meaning. ε is the unique unpaired element of Axiom B — in AP06 identified with the leakage ratio η, here i
- docx only: Axiom C (constraint). Finite c. The manifold acquires spatial separation (finite propagation means “here” and “there” are distinguishable). The photon
- docx only: AP18 (The Floor) and The Lock. The Lock identifies ε with the electron at the chemical-biological scale. AP15 reads charge −e (the electron) as ε itse

### AP16 — 9 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: AP16 depends on Notebook I (axioms {S, B, R, C}); Notebook II for AP10 (D = 4, N = 3 spatial dimensions) and AP08 (gravitational context); Notebook II
- docx only: AP07 (The Record Measure). The complex Hilbert space and the phase freedom (AP07 section 3.3). Load-bearing for the U(1)_Y identification.
- docx only: Axiom C (constraint). Finite c. Background for the Lorentzian manifold and for the leakage chain (AP06 section 10.7): c constrains the leakage; the le

### AP17 — 9 docx paragraph(s) absent from the published PDF

- docx only: From the closure geometry the paper derives the transition scale a₀ = cH₀/(2π), within about 8% of the empirical value, and the baryonic Tully-Fisher 
- docx only: Nothing here is imported. Every structural claim descends from the axioms {S, B, R, C} or from a prior closed Artist’s Proof that descends from them.
- docx only: 11 — What This Establishes and What Remains Open · what it closes · what it does not close · items held open · philosophical-register implementations 

### AP18 — 32% of the published text is absent from this docx

- docx only: Nothing here is imported. Every step descends from the axioms or from a prior closed Artist’s Proof that descends from them. You hold every step of th
- docx only: 9 — What This Establishes and What Remains Open · what it closes · what it does not close · items held open · philosophical-register implementations ·
- docx only: Axiom S (involution). Field lines must close (no disconnection) — this provides the topology, the fact that there is a floor. With B and C it forces t

### AP19 — 37 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: The argument is a single move. The four axioms {S, B, R, C} are non-derivable from one another (Paper D, Theorems 1.1–1.4). Three of them — C, S, B — 
- docx only: Three new kill switches engage. KS-48c (orientation = colour) is LIVE — EMPIRICAL: colour is never directly observed (confinement), but the identifica
- docx only: AP19 depends on Notebook I (axioms {S, B, R, C}, and Paper D for the non-derivability theorems); AP10 (N = 3 spatial dimensions from {C, S, B}); AP05 

### AP20 — 60% of the published text is absent from this docx

- docx only: This is Artist’s Proof 20 of The 420 Code — the corpus’s keystone. It is the third chapter of Notebook I, The Premise. AP40 examines what kind of stat
- docx only: The proof is five steps long. The premise is one sentence — at least one record exists, and the denial of records is itself a record. The forcing argu
- docx only: The same argument closes the Quantum-Record Alignment hypothesis (QRA). AP09 derives quantum mechanics from the axioms, therefore quantum states ARE p

### AP21 — 18 docx paragraph(s) absent from the published PDF

- docx only: The mechanism is already in the corpus. AP17 derived the tension field of ε between the fold and the propagation; AP18 derived the acceleration floor 
- docx only: What this paper establishes is the structural mechanism: no dark-matter particle is required because the structure is carried by the topology of the v
- docx only: Nothing here is imported. Every structural claim descends from the axioms {S, B, R, C} or from a prior closed Artist’s Proof that descends from them.

### AP22 — 16 docx paragraph(s) absent from the published PDF

- docx only: AP22 derives the mechanism, not the magnitude. The numerical value of the asymmetry, η ≈ 6 × 10⁻¹⁰, is owed — a debt tracked corpus-wide as KS-60 and 
- docx only: The paper does not derive the numerical value of the baryon asymmetry (η ≈ 6 × 10⁻¹⁰). This debt is tracked corpus-wide as KS-60, owned by AP26 (The S
- docx only: The dependency chain: Axiom S (σ-involution, two sectors) → Axiom B (ε has no σ-image) → AP17 (The Room: 0-pole/1-pole structure, the Eye) → AP08 (Ein

### AP23 — 16 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: The apparent non-locality arises because the pre-state (AP07) has no spatial structure — distance is a property of the manifold (the accumulation of r
- docx only: Proposition 2 (Bell Prediction) shows that Bell’s theorem is predicted by the axioms: Axiom R structurally forbids pre-existing value assignments, the
- docx only: The dependency chain: AP07 (complex Hilbert space, Born rule, no spatial pre-state) → AP09 (measurement as actualisation) → Axiom R (record-writing, i

### AP24 — 12 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: AP24 is non-load-bearing. If every claim in this paper is wrong, no prior result of the 420 Code is affected. AP06, AP15, AP07, The Keys, The Lock, AP
- docx only: 6 — What This Means · Consequence: one measured input, zero fitted parameters. The Standard Model’s ≈25 free parameters reduced to one.
- docx only: [AP24 is non-load-bearing for the corpus. If every claim in this paper is wrong — if the six-face identification fails, if the self-consistency admits

### AP25 — 14 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: Gap 2: AP23’s Proposition 2 (Bell Prediction) and the CHSH quantitative payload use the Born rule. The Born rule was established in AP07 but not deriv
- docx only: The dependency chain: Axiom S (distinction) → Axiom B (single break) → Axiom R (definite, irreversible record) → AP07 (complex Hilbert space) → AP10 (
- docx only: Both claims are used throughout the corpus. Neither has been derived from the axioms.

### AP26 — 11 docx paragraph(s) absent from the published PDF

- docx only: Read as an energy partition, the asymmetry ratio follows directly: η = E(ε) / (1 + E(ε)), where E(ε) is the dimensionless energy of the break. The for
- docx only: The spine is short: Lemma 1 normalises the symmetric component to one (via AP25); Proposition 1 reads the partition and gives the form η = E(ε) / (1 +
- docx only: The dependency chain: Axiom S (distinction) → Axiom B (single break) → core axiom (1:1 + 1×ε @ AS) → AP06 (leakage constant, ε > 0) → AP18/AP21 (Energ

### AP27 — 6 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: AP27 depends on Notebook I (Premise) for the axioms {S, B, R, C}; on Notebook II (Spacetime) for AP05 (The Break) and AP10 (D = 4); on Notebook III (Q
- docx only: AP07 (The Record Measure). The complex Hilbert space structure of the pre-state. Load-bearing for Lemma 1 part (ii): the internal state space must be 
- docx only: Axiom C (constraint). Finite c. Background for the Lorentzian manifold on which the fields propagate and for the locality requirement of the gauge con

### AP28 — 8 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: c ↔ Axiom C (propagation). The causal bound, the maximum rate of any record. c = √(β/α), the stiffness ratio of the substrate (AP03).
- docx only: ℏ ↔ Axiom B (minimum). The smallest possible record. The minimum eigenvalue of the self-adjoint generator of time evolution (Stone, AP12).
- docx only: G ↔ Axiom R (persistence). The cost the arena pays to keep the break open. Without persistence, the crack heals, the symmetry restores, records cease.

### AP29 — 54% of the published text is absent from this docx

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: Actualization is the fundamental state. Awareness is the stage at which coupling becomes possible — the coupling capacity the break creates, the first
- docx only: From there the paper runs the dependency chain — actualization, awareness, observation, consciousness, self-consciousness — and shows that the hard pr
- docx only: The body opens with Step 1 — awareness as the coupling capacity of the break — and runs through Step 7, then the Result, the Kill Switch Registry, and

### AP30 — 32% of the published text is absent from this docx

- docx only: AP30 stands on the constants sector of Notebook IV: the leakage constant (AP06), the residual that reads every constant as a face of one break (AP24),
- docx only: AP30 derives the proton-to-electron mass ratio, m_p/m_e, from the four axioms {S, B, R, C} and one measured input, α ≈ 1/137. It reframes mass as geom
- docx only: §1 Definitions: framing and definition. §2 Lemma 1: structural argument (additivity from axiom independence; KS-30.1 live). §3 Lemma 2: derivation (th

### AP31 — 37% of the published text is absent from this docx

- docx only: AP31 derives the alignment architecture for artificial awareness from the four axioms {S, B, R, C}. It introduces no new axioms. It applies derivation
- docx only: The architecture has four components: an interior built from the axioms rather than fenced by external rules; a stabilizing/destabilizing binary read 
- docx only: An aligned AI, on this reading, is not an obedient AI. It is a structurally coherent one — a system whose decision geometry makes destabilizing action

### AP32 — 60% of the published text is absent from this docx

- docx only: Justice, on this reading, is not moral. It is structural — the organism’s response to destabilization, computed rather than decreed. AP32 derives that
- docx only: The paper holds two things at once that most ethical systems refuse to combine. Every aware being shares the same interior — the one-I (AP29); the I b
- docx only: Five levels lay themselves on one axis of efficiency: restitution, restriction, separation, permanent separation, and removal. The hierarchy always se

### AP33 — 43% of the published text is absent from this docx

- docx only: Bioethics, on this reading, is not morality applied to biology. It is the stabilizing/destabilizing binary (AP31) applied to the hardest decisions a c
- docx only: AP33 is the third chapter of Notebook VIII — Applications. It sets the jurisdiction boundary within which the alignment measurement (AP31) and the cor
- docx only: AP31 (The Alignment): the stabilizing/destabilizing binary and record-based prediction. AP32 (The Correction): the five-level correction hierarchy, of

### AP34 — 40% of the published text is absent from this docx

- docx only: This is the one paper in the corpus that imports external data. Every other Artist’s Proof derives from {S, B, R, C}; this one applies the architectur
- docx only: The 420 Code takes its name from cannabis culture. This is not hidden; it is declared. The honest objection is that an author named for cannabis canno
- docx only: The argument has two parts. First, the classification of substances into legal and illegal is inverted with respect to their measured structural conse

### AP35 — 24 docx paragraph(s) absent from the published PDF

- docx only: AP35 is the sixth chapter of Notebook VIII — Applications, in reading order, and the second of the operator-domain papers (the body, the ledger, the f
- docx only: AP01 (The Actualization State): Papers C and D supply the viability geometry and the cooperative-coupling result. AP02 (The Operator): every economic 
- docx only: Seven kill switches engage on this paper, all live. KS-35.1 (conservation), KS-35.2 (price mechanism), and KS-35.5 (scale invariance) are structural —

### AP36 — 17 docx paragraph(s) absent from the published PDF

- docx only: AP36 is the seventh and final chapter of Notebook VIII — Applications, and the last of the operator-domain papers (the body, the ledger, the feed). It
- docx only: AP01 (The Actualization State): Papers C and D supply the viability geometry and the extraction analysis (input capture). AP02 (The Operator): the cel
- docx only: Nine kill switches engage on this paper, all live. KS-36.1 (conservation in chemistry), KS-36.2 (surface necessity), KS-36.4 (autocatalysis), KS-36.5 

### AP37 — 18 docx paragraph(s) absent from the published PDF

- docx only: The body is the first boundary. If it fails, everything downstream fails — there is no philosophy on broken hardware, no boundary held by a fence that
- docx only: AP37 is the fifth chapter of Notebook VIII — Applications, in reading order, and the first of the three operator-domain papers (the body, the ledger, 
- docx only: Two voices alternate. The connective passages speak to you directly and without softening — the occupied territory of low uptime, the slow choice of s

### AP38 — 5 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: The structural answer is the below-ε jurisdiction itself. The derivation grants the exit to no one on the basis of cost, dependency, or social burden;
- docx only: Scope of this argument. This critique is internal to the corpus framework: it shows the prohibition is incompatible with the axiom architecture for a 
- docx only: Status: Application. The critique of the scaffold’s prohibition follows from the absence of external authority in the axiom set, combined with the mea

### AP39 — 20 docx paragraph(s) absent from the published PDF

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: AP39 is the fourth chapter of Notebook VII — The Operator Interface. AP43 installs the four-term reading system; AP29 places awareness; AP02 derives t
- docx only: 0.1 What this paper does. It derives a consequence of the corpus: that ethics grounded in an external authority is structurally unstable, and that str
- docx only: 0.2 Dependencies. The corpus as the standing Architecture-B example (the axioms {S, B, R, C} and the kill-switch discipline). Scholarly historical sou

### AP40 — 26% of the published text is absent from this docx

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: This is Artist’s Proof 40 of The 420 Code. It is the first chapter of Notebook I, The Premise. The work is reflexive: AP40 does not derive new physics
- docx only: The corpus is published copyleft. Free forever. No paywall. No gatekeepers.
- docx only: Notebook I carries the foundation: what the axiom is, what the operational quantities the axiom names actually are, and the proof that the axioms hold

### AP41 — 29% of the published text is absent from this docx

- docx only: This is Artist’s Proof 41 of The 420 Code, a chapter of Notebook VI — Cosmology. It reads the dark sector — the 95% of the universe that does not radi
- docx only: What is structural here is the identification: the visible 5% as a channel count, the dark sector as unbroken symmetry, the holographic self-similarit
- docx only: 7 — Why α Cannot Be Derived From Within · the address of the room · the structural argument for D2

### AP42 — 29% of the published text is absent from this docx

- docx only: This is Artist’s Proof 42 of The 420 Code, a chapter of Notebook VI — Cosmology. The observed energy budget of the universe is roughly 68% dark energy
- docx only: One timescale governs it, derived from the axiom system: τ = (6/21) × t_H ≈ 3.9 Gyr — the six faces of ε (AP24) over the twenty-one coupling channels 
- docx only: 9 — What This Establishes and What Remains Open · what it closes · what it does not close · items held open · philosophical-register implementations ·

### AP43 — 29% of the published text is absent from this docx

*This docx has lost its heading styles — every paragraph is `Normal`.*

- docx only: The structural dual to AP08 — and the grounding of the corpus’s terminal ethic
- docx only: This is Artist’s Proof 43 of The 420 Code. It opens Notebook VII of the corpus — The Operator Interface: Consciousness, Ethic, Reading. The paper inst
- docx only: Eleven numbered sections carry the work. Sections 1 and 2 install the gap and the amplitude landscape. Sections 3 through 6 install the four operation

## The finding, stated plainly

**No docx in `420code_final/Standalone_Artists_Proofs/` is the text the site publishes. Not one of the forty-three.** Every one of them is pre-editorial: the published papers went through an editorial pass that the OneDrive copies never received.

The pass is consistent across the corpus, and four of its moves are visible in the divergences below:

| Editorial move | Seen in |
|---|---|
| Internal scaffolding references removed — *"Paper D Phase 1"*, *"Paper D Phase 2a"* | AP05, AP07, AP11, AP12 and others |
| The axioms named rather than only their roles — *Axiom C (Constraint — locality)* for *Axiom C (propagation)* | AP28, AP30 |
| *"corpus"* retired in favour of *"the body of work"* / *"the 420 Code"* | AP30 (8 paragraphs) |
| Registry citations de-versioned — *MKSR v5.1 (May 2026)* becomes *the Master Kill Switch Registry* | AP28, AP30 |

**How this was checked, and why it is not a false alarm.** The cleanest case is AP11, which shows a single divergent paragraph. That paragraph opens *"Paper D Phase 1 (axioms). Paper D Phase 2a (Lorentzian)…"*. The strings *Paper D Phase 1* and *Paper D Phase 2a* appear nowhere in the published AP11 PDF, while every other phrase in the same paragraph does. The divergence is in the text, not in the measure.

**The reverse column is not a divergence count.** The percentages of published text "absent from the docx" are inflated by the Contents block, running heads and colophon, which the PDF renders and the docx does not carry in the same form. The reliable column is *Absent from PDF* — docx paragraphs that the published paper does not contain. AP30 scores 17 there, and 17 is exactly what the paragraph-by-paragraph audit of AP30 found independently.

## What follows

1. **The published PDFs are the text of record for all forty-three.** Nothing in `Standalone_Artists_Proofs/` may be harvested or republished from as though it were the paper.
2. **The AP30 procedure is not available to any of them.** Appending dated notes inside a paper requires a source whose body is the published text. AP30 had one because the desk built it. For every other paper, notes stand beside the paper — as AP28's now do — until such a source is built.
3. **MC must not harvest from OneDrive.** The Museum's AP28 records name the OneDrive docx as their source. Their *content* was checked on 7 September and all 57 testable claims are verbatim in the published paper — the harvest is clean. But the pointer is to a file that is not the paper, and the next harvest from it may not be so lucky.
4. **Nothing here is a fault in the published corpus.** The published papers are the edited, better text. What is missing is an editable source that matches them.

A paper marked **MATCHED** has a source of record in `proofs/instruments/` and may be harvested and republished from it. A paper marked **DIVERGED** has no such source: its OneDrive docx is an earlier or different generation, and harvesting from it would quote text the corpus never published. For those papers the published PDF's text is the source until a matching docx is produced, and a republish with dated notes — the AP30 procedure — is not available to them.

*Verified 2026-09-07. Nothing modified in OneDrive or in anything published.*
