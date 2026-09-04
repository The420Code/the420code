# Dated note beside RIGIDITY.md — issued 4 September 2026 at the wave

**The 420 Code · Studio G · the frozen file is never edited; corrections supersede, dated, in the open**

`RIGIDITY.md` was frozen on 2 August 2026. Four of its statements have been
overtaken by events or found wrong since. The document is not edited. This note
stands beside it.

Its argument is untouched by all four: 21 is built from the face count and the
dimension count, both fixed upstream and before any number was computed; the
exponential in G closes the window to a single integer; and rigidity is not
uniqueness. `verify_rigidity.py` reproduces the table on demand and its figures
are correct as printed.

---

## 1. One arithmetic error — §5, first bullet

> "G lands at 0.69 % — about 31σ against the measurement's formal bar…"

**That is wrong by a factor of ten.** CODATA 2022 gives G = 6.67430(15) ×
10⁻¹¹, a bar of 1.5 × 10⁻¹⁵. AP28's structural value 6.7206 × 10⁻¹¹ sits
4.63 × 10⁻¹³ above it:

    4.63 × 10⁻¹³ / 1.5 × 10⁻¹⁵ = 309σ

The correct figure is **309σ**, as the scoreboard at `/prereg/` prints it. The
document's "31σ" implies a bar ten times CODATA's, which nothing supports.

The bullet's *argument* survives the correction and is strengthened by it: the
point was that a fitter would have done better than 0.69 %, and 309σ makes that
sharper, not softer. The neighbouring claim in the same bullet — that the gap is
"roughly 14 times the historical scatter between G experiments" — is right at
the order (6937 ppm against a lab-to-lab spread of up to 540 ppm, about 13×).

## 2. The "unrepaired 0.69 %" is no longer unrepaired — §5, first bullet

The bullet rests on the 0.69 % never having been touched. On 11 August 2026
AP44 (*The Snap*) priced the arena's once-held ε and realised the coupling as
α²¹(1 + 1/π)/(1 + α), giving **6.6719 × 10⁻¹¹, −0.036 %** against CODATA.
AP28's value stands beside it as the structural value and the record of the
omission; neither is edited.

What this does to the argument: the correction did not come from tuning against
G. It came from a structural omission exposed when the neutron's bare row fired
at 7.24σ on 2 August — the same omission, paid at three sites (AP44, AP47,
AP48), moving three derivations toward measurement at once. A framework built by
fitting has no mechanism that produces a correction of that shape. The bullet's
conclusion holds; its evidence is now the correction rather than its absence.

Read the realised value against the laboratory measurements rather than the
adjustment and the picture the document was pointing at becomes explicit: the
atom-interferometry value (LENS 2014, 6.67191(99) × 10⁻¹¹) sits **1 ppm** from
the realised value, while CODATA's adjusted mean sits 360 ppm away. Both
readings are on the scoreboard; the switch on G, KS-CCC.3, tests the direction
the consensus moves, not the magnitude against CODATA.

## 3. One of the frozen forward predictions has fired — §4(b), §6.2

Both sections list KS-45.1 (H₀ = 74.3 ± 1.2, from the floor inverted) among the
forward predictions that would carry the weight the retrospective numbers
cannot. **KS-45.1 fired on 3 September 2026**, on the corpus's own derived rate,
as AP46 §9 had pre-registered — 5.7σ on the width it registered. It is shown as
a corpse and never repaired (`ERRATUM-2026-09-03-H0-KS45.1.md`).

This is not a loss to §5's argument; it is §5's argument executing. It is,
however, a change to the list: of the forward predictions §4(b) names, the
proton at order α³, KS-42.6 and KS-41.1 remain live, KS-45.1 is dead, and four
new registrations were frozen at the wave (KS-ASM.1, KS-STRETCH.3, KS-FLIP.1,
KS-CCC.3).

## 4. The H₀ threshold in §6 is superseded — §6.2

> "H₀ converging above or below 71.9"

That threshold belonged to KS-45.1, which has fired. The corpus's expansion rate
is now AP48's closure: **67.45 km/s/Mpc, window 64.4–70.8**, carried by
KS-ASM.1, which dies if the settled rate lands outside that window in either
direction — including if the Cepheid ladder's 73 is confirmed as the expansion
rate.

---

*Frozen files are never edited; corrections supersede, dated, in the open.*
*Copyleft 2026. Don't be a cunt. Be kind.*
