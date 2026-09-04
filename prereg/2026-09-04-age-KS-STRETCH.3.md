# Registration: the age of everything — one cycle (KS-STRETCH.3)

**Freeze date:** 2026-09-04 (the paper locked 2026-09-02; anchored by the verifier the same day)
**Author:** G · Studio G · the420code.org
**Scope:** AP46 (*The Stretch*) §§5–9 and §12; AP42 (*The Clock*) §5; AP28 (*The Constant*) §§4–5
**Switches engaged:** KS-STRETCH.3 (the age chain); KS-STRETCH.1 (the clock joint, with KS-42.3/42.6); KS-STRETCH.2 (the stance, with KS-42.4); KS-STRETCH.4 (the era surface — met and closed by AP48)
**Reproduction:** `verify_family.py` in this directory
**Status:** frozen for commit. The commit hash is the timestamp.

---

## 1. The registered value

> **One cycle = (21/18) · α⁻¹⁸ · τ_C = 13.830 Gyr, one lane-time wide: the window 13.17 to 14.49 Gyr**

Measured age (Planck 2018, TT,TE,EE+lowE+lensing+BAO): 13.787 ± 0.020 Gyr. The
chain lands +0.31% above it (+0.24% against the Planck-alone 13.797 ± 0.023).
The measured age sits 0.04 inside the window's edge count — well inside.

The claim is coarse by construction: an aware observer measures *about* one
cycle, because awareness is a late-cycle product. The +0.31% landing is the
seat inside the window, not the claim's precision. Anyone who reads 0.31% as
the claim has misread the paper.

---

## 2. The chain, and what is chosen by ruling

    τ_C = ħ / (mₑ c²) = 1.2880886656 × 10⁻²¹ s      the tick: the electron's reduced Compton time (a ruling; the unreduced time would give 86.9 Gyr)
    α⁻¹⁸ ticks                                       one escape through eighteen α-transparent doors — the eighteen face-projections
    α⁻¹⁸ · τ_C = 3.7408 × 10¹⁷ s = 11.854 Gyr          the thread alone
    × 21/18                                          the duty: the faces bleed eighteen twenty-firsts of the service-cycle
    = 13.830 Gyr                                     one cycle

Inputs: α = 7.2973525643(11) × 10⁻³ and mₑ = 9.1093837139(28) × 10⁻³¹ kg, CODATA
2022. No fitted parameters; three structural choices, each ruled and named —
the eighteen (AP28's faces, fixed before the paper), the twenty-one over
eighteen (the service-cycle), and the reduced tick. The lane — one twenty-first
of the cycle, 0.659 Gyr — is one face-erasure, and AP42's dark clock is six
lane-times of the same twenty-one: consistent by construction, one
corroboration, counted once.

---

## 3. Provenance, in the order it happened

The eighteen faces and the three gates were fixed in WP-BUMP.7 FINAL
(186b0bf2…, 16 August 2026, before the session); the twenty-one and AP42's
clock were fenced in WP-COST.1 FINAL (4f7a1c6a…, 11 August). The thread alone
was computed first and gave 11.854 Gyr — a factor 0.86 short of the measured
age — and the author refused to dress the factor. That the service-cycle already
ruled enters the chain as 18/21 = 0.857 was noticed *after* the shortfall, in
the drafting; the ingredient was ruled before the arithmetic, its place in the
chain seen after. The 0.86, its refusal and this label were written into the
paper's v0.1 (5391d96f…, 17 August, early morning) within hours, and have stood
in every version since. That is the whole provenance of the 0.31%, stated where
the reader meets the number.

---

## 4. The seam, and how it closed

AP46 §9 refused H₀: read as a rate the chain would give ≈ 70.7 km/s/Mpc, and
the paper did not claim it. It stated the seam with its numbers: under the
standard history the age at H₀ = 67.4 is 13.80 Gyr and at the corpus's then-rate
74.3 it is 12.52 — two lanes below the cycle — and pre-registered that AP48 would
derive the relation reconciling them or one edge of the family would fire:
KS-45.1 or KS-STRETCH.3.

AP48 closed the seam by adjudication, not reconciliation: the relation is the
standard one; the age survives; the rate of 74.3 does not; KS-45.1 fired (see
`ERRATUM-2026-09-03-H0-KS45.1.md`). Four sentences of AP46 are superseded by
dated note (`/proofs/instruments/AP46/DATED_NOTE_AP46_2026-09-04.md`); the
landing is untouched, and no digit changes. The settled rate of the leak is
0.792 of the cycle's inverse, not one times it.

---

## 5. Kill and confirm conditions (binding)

1. **KILL — the lane.** KS-STRETCH.3 fires if the age of the universe, as the
   cosmological data settle it, differs from one cycle by more than one
   lane-time, 0.66 Gyr, in either direction. An early-dark-energy resolution
   of the Hubble tension, at an age near 12.9, fires it. The Cepheid ladder
   confirmed at 73 fires it too: the age at the corpus's partition would be
   12.78 Gyr (AP48 §10).
2. **KILL — the joint.** KS-STRETCH.1 fires with AP42's KS-42.3 and KS-42.6: if
   the locked 6/21 falls, both derivations fall together.
3. **KILL — the stance.** KS-STRETCH.2, with KS-42.4: fires if w evolves the
   wrong way — increasingly phantom at late times — or if a confirmed evolving
   w cannot be carried by the feeding history and the settling law without the
   leak's own settled rate drifting.
4. **MET — the era surface.** KS-STRETCH.4, registered by AP46 for AP48, is met
   at AP48 §9 (the shapes, the handover, the nuclei, the glow) and CLOSED,
   contingent on KS-ASM.2: if that fires, this re-opens and fires with it.
5. **NO RE-ANCHORING.** The eighteen, the twenty-one over eighteen and the
   reduced tick are frozen. Any other assembly is a new registration.

---

*Copyleft 2026. Don't be a cunt. Be kind.*
