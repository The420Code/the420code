# Pre-registration: the proton–electron mass ratio at order α³

**Freeze date:** 2026-08-02
**Author:** G · Studio G · the420code.org
**Scope:** AP30 (*The Resistance*) and Ø Predictions Part I
**Status:** frozen for commit. The commit hash is the timestamp. Every condition in §7 is binding on any later claim made from the values below.
**Reproduction:** `verify_prereg.py` in this directory recomputes every number here from CODATA 2022 inputs. Nothing below is quoted from memory.

---

## 1. What this document registers, and what it does not

It registers **one number**: the value the AP30 formula produces when the series is truncated where AP30 truncates it, at order α².

It does **not** register a value for the order-α³ coefficient. As of this freeze date the corpus contains no derivation of that coefficient, and none is claimed here. §5 explains why any value stated today would be a fit rather than a prediction.

This is a narrower claim than earlier drafts of this document made. The narrowing is deliberate.

---

## 2. Inputs (CODATA 2022, NIST, retrieved 2026-08-02)

| Quantity | Value | Relative uncertainty |
|---|---|---|
| α⁻¹ | 137.035999177(21) | 1.5 × 10⁻¹⁰ |
| m_p/m_e | 1836.152673426(32) | 1.7 × 10⁻¹¹ (17 ppt) |
| m_μ/m_e | 206.7682827(46) | 2.2 × 10⁻⁸ |

Earlier drafts used α⁻¹ = 137.035999084. That is the CODATA **2018** value. The correction moves the frozen value by 0.013 ppt — numerically irrelevant against a 10 ppt effect, but the label was wrong and is corrected here.

---

## 3. The formula, with its epistemic ledger

    m_p/m_e = 21²×4 + 21×3 + 3²
            + α · 21 · (1 − 1/(84π))
            + α² · 21 · 16/1836
            + O(α³)

What each term rests on, stated as the corpus itself states it:

| Term | Status in the corpus |
|---|---|
| 1764 + 63 + 9 = 1836 | Derived from {21, 3, 4}. Additivity of the three layers is **argued, not proved** — KS-30.1, the paper's named standing debt (shared axiom S appears in all three layer subsets). |
| α · 21 · (1 − 1/(84π)) | Derived. Isotropy of the leakage is an assumption — KS-30.2. |
| α² · 21 · 16/1836 | **The integer 16 is not derived.** AP30 §6 states its structural decomposition from {21, 3, 4} is owed under KS-30.3, and that it is not Layer 3 (which is 9). Any presentation of 16 as "rank-2 (μ,ν) pairs over 4 dimensions" is a gloss, not a derivation. **But its value is no longer free — see §4a.** |
| O(α³) | Not computed. No coefficient, no sign. |

The integers 21, 3, 4 are fixed in AP10/AP28, upstream of any mass calculation. That ordering is the load-bearing fact and it is checkable against the corpus's own dependency graph.

---

## 4. The frozen value

Evaluated at CODATA 2022 α:

| | |
|---|---|
| 21²×4 + 21×3 + 3² | 1836 |
| α · 21 · (1 − 1/(84π)) | 0.152663698984911 |
| α² · 21 · 16/1836 | 0.00000974534591208 |
| **D (frozen)** | **1836.152673444331** |
| propagated uncertainty from α | 0.013 ppt |

Against measurement:

| | |
|---|---|
| D − measured | +1.833 × 10⁻⁸ = **+9.98 ppt** (0.00998 ppb) |
| measurement uncertainty | 17.4 ppt |
| **discrepancy** | **0.57 σ** |

D lies **above** the measured value. Any order-α³ term that closes the gap must therefore be **negative**, while the α and α² terms are both positive.

**D is the registered prediction.** It was fixed by structure, not by the measurement, and it is the only value in this document not selected with the residual in view.

---

## 4a. The α² coefficient is empirically pinned (registered 2026-08-02)

This was not previously computed anywhere in the corpus. Subtracting the exactly known 1836 and O(α) terms from the measurement and dividing by α²:

| | |
|---|---|
| coefficient required by measurement | **0.1826623 ± 0.000601** — a **0.33 %** constraint |
| corpus value 21 × 16 / 1836 | 0.1830065 |
| agreement | **0.57 σ** |
| implied value of the owed integer | **16 = 15.97 ± 0.05** |

Written as an integer numerator over the static count 1836, the measurement requires **335.4 ± 1.1**. The integers inside the 3σ window are 332 … 339. Exactly one of them is a product of non-negative integer powers of {21, 3, 4}:

> **336 = 21 × 16 = 84 × 4 = 4² × 21**

**Consequence for KS-30.3.** The switch changes character. It is no longer *"the coefficient is unknown and owed"* — the coefficient is measured to 0.33 %, the target integer is 336, and 336 is the only structurally reachable integer within 3σ. What remains owed is the **decomposition**: why 336, and under which of its three readings. A derivation returning 15 or 17 is wrong on arrival.

**Consequence for the recursion.** If the order-α² count is rank-2 over spacetime (4² = 16), the naive rank-3 continuation is 4³ = 64, giving c₃ = 21 × 64/1836 = 0.732 — **excluded at 9.5σ** continuing with the same (positive) sign as the α² term, or 8.3σ if the sign reverses. Dead either way. Any derivation that produces 16 at second order must therefore *not* produce 64 at third order. That is a hard, two-sided constraint on the mechanism and it did not exist before this freeze.

This section is a strengthening of the corpus, not a correction, and it is the only claim in this document that improves on what AP30 states.

---

## 5. Why no α³ coefficient is registered

Write the third-order term as c₃α³. The measurement constrains c₃ to:

> **c₃ = −0.047 ± 0.082 (1σ)**, i.e. the interval **[−0.129, +0.035]**

The uncertainty is 1.7× the magnitude of the central value. The interval contains zero. It contains 1/21 = 0.0476 with either sign attached. It contains 21×4/1836 = 0.0458. It contains a dense set of ratios of the corpus integers {3, 4, 6, 21, 84, 1836} and π — a bounded enumeration over exponents in [−1, 2] returns **910 distinct admissible values inside 1σ**.

Three separate problems follow, and each must be solved before an α³ prediction exists:

**(a) The sign is undetermined.** The recursion sketched in Ø Predictions — at order n, a structural count × 21, normalised by 1836, times αⁿ — generates only positive terms. Ø Predictions §6 acknowledges the sign is open ("resolving both its magnitude and its sign"). Fixing the sign to negative in order to close the residual is a fit, and a large one: c₃ = −1/21 sits 0.005σ from measurement, c₃ = +1/21 sits 1.15σ on the wrong side.

**(b) The coefficient is unconstrained.** With c₃ free across [−0.129, +0.035], no measurement at present precision can select among candidates. A registration naming two branches out of a continuum is not a closed menu, and a kill condition over an open menu does not bind.

**(c) The generating rule is owed.** The order-2 coefficient 16 is itself undecomposed (KS-30.3). A rule that has not reproduced order 2 cannot be trusted to produce order 3.

**The honest position: the framework predicts D. It does not yet predict anything at order α³.**

---

## 6. Correction to the uniqueness claim, and the condition that closes it

Ø Predictions Part I states three conditions on the decomposition of 1836 — three terms summing to 1836; each term a product of non-negative integer powers of {21, 3, 4}; the exponent of 21 strictly decreasing across the terms — and reports that eleven sums satisfy the first two and **exactly one** satisfies all three.

Independent enumeration (`verify_prereg.py`) reproduces the eleven exactly. It returns **two** under all three conditions:

| Decomposition | 21-exponents | structural factors per term |
|---|---|---|
| 21²×4 + 21×3 + 3² = 1764 + 63 + 9 | 2, 1, 0 | 3, 2, 2 |
| 21²×3 + 21×3² + 3⁴×4 = 1323 + 189 + 324 | 2, 1, 0 | 3, 3, 5 |

**Condition 4 (formalised here).** *The number of structural factors per term, counted with multiplicity, must be non-increasing across the ordered triple.* The hierarchy sheds structure; it never accretes it. A last layer more complex than the first is not a hierarchy.

Under conditions 1–4 the enumeration returns **exactly one** decomposition: 1764 + 63 + 9. Both conditions 3 and 4 are load-bearing — condition 4 alone leaves 1764 + 36 + 36, condition 3 alone leaves the 1323 alternative.

**Declared, because it matters more than the fix:** condition 4 was formalised on 2026-08-02, *after* the alternative surfaced. It is not invented for the purpose — AP30 §3 already states the criterion in prose ("each successive term using fewer body of work numbers"), predating this freeze. But AP30's wording is strictly decreasing, and the adopted decomposition is 3, 2, 2 — non-increasing, not strictly decreasing. **AP30's prose is too strong and is corrected here to "no more than."** What is new is the formalisation and the multiplicity count; what pre-exists is the criterion.

**Standing of the fix.** Condition 4 cannot currently be tested anywhere else in the corpus — 1836 is the only hierarchical integer decomposition of this form in the body of work. A condition that closes exactly the case that motivated it, and can be checked nowhere else, is weaker than one recovered from independent use. It is offered as a formalisation, labelled as post-hoc, and KS-30.4's within-family limb is recorded as **reopened 2026-08-02 and closed the same day by condition 4, with the ordering disclosed.**

---

## 7. Binding conditions

1. **KILL D.** D dies at 3σ once the measurement uncertainty reaches **3.3 ppt** with the central value unchanged, and at 5σ at **2.0 ppt**. Current best is 17.4 ppt (CODATA 2022) / 20.2 ppt (HD⁺) / 25.6 ppt (H₂⁺). Projected molecular-hydrogen-ion and Penning-trap precision reaches this range within 3–5 years. **This is a real kill condition and it arrives soon.**

2. **CONFIRM D.** The measurement converges on 1836.152673444 as uncertainty falls below 5 ppt. The series terminates at α², KS-30.3 closes for the proton, and the present 0.57σ offset was measurement scatter.

3. **NO POST-HOC c₃.** If D dies, the framework may not repair itself with a coefficient chosen against the residual. Any α³ coefficient offered in defence must be derived from the AP24/AP28 recursion, published before the measurement it is defended against, and must state its sign in advance.

4. **KS-30.4 stays open** until §6 is resolved.

5. **No retro-editing.** This file's hash and date are the record. Superseding versions must reference this hash and state what changed.

---

## 8. Circularity declaration

CODATA 2022 and all measurements predating this freeze **cannot confirm anything in §5**. The interval in §5 was computed from them.

They *can* test D, because D was not derived from them. That asymmetry is the whole content of this registration.

**Author's testimony on derivation order, offered as testimony and not as evidence:** the integers were fixed from the axiom chain (one record exists → {S, B, R, C} → the manifold → 21, 3, 4) before any measured ratio was consulted, and the agreement with m_p/m_e was noticed only after the terms were written. This is checkable in principle against draft history and the corpus's internal dependency order; it is not checkable from this document, and no reader is asked to take it on trust. It is recorded here because if it is true it matters, and because stating it now makes it falsifiable later.

---

## 9. The muon: a domain boundary, registered

The construction does not reach the muon, and the reason is structural rather than numerical.

A three-term sum with strictly decreasing 21-exponents requires a leading term of at least 21² = 441, a second of at least 21, and a third of at least 1. **The construction has a floor of 463.** m_μ/m_e = 206.77 lies below that floor and is unreachable at any exponents. This is not a failed search over a large space; it is an impossibility over the whole space.

Two readings, both stated:

**As a domain restriction.** AP30 §3 says, before any lepton question arises, that the proton "integrates all 21 channels — it is not a 1-channel object like the electron," and §1 sets the electron as the *unit* of resistance rather than a member of the series. The three-layer construction is therefore a construction for a 21-channel, three-face bound state. The muon is a lepton. Applying the rule to it was never licensed by the corpus, and the floor at 463 is the construction declining to leave its stated domain. This restriction predates the question and is not a rescue.

**As an owed debt.** That reading buys nothing predictive. The corpus does not derive the lepton masses, does not derive the generation structure, and carries both as an open debt (KS-66, AP27). A framework that derives one mass ratio and cannot reach the second-lightest charged fermion has derived one number, not a mass spectrum. The corpus should say so in that plain form.

**The falsifier this creates.** If anyone derives m_μ/m_e from the same nested rule over {21, 3, 4}, the channel-count reading fails — because the rule would then apply to leptons, and the proton's "integrates all 21" story loses the content that made 1764 mean anything. **The floor is itself a kill condition, and it is registered as one.**

---

## 10. What this establishes and what it does not

**Establishes:** a single frozen number, derived from structure fixed in advance, currently 0.57σ from the best measurement, with a kill condition that binds within roughly five years and cannot be evaded by adjusting a free coefficient — because the registered claim contains no free coefficient.

**Does not establish:** that the decomposition is unique (§6 — it is not, under the stated conditions); that the α² coefficient is derived (KS-30.3); that the layers add (KS-30.1); that any α³ structure exists; or that a match at 17 ppt selects this construction over the many others that survive at the same precision. A confirmation can only remove rivals. It can never establish uniqueness.

---

## 11. References

- E. Tiesinga, P. J. Mohr, D. B. Newell, B. N. Taylor, *CODATA recommended values of the fundamental physical constants: 2022*, Rev. Mod. Phys. **97**, 025002 (2025). Values retrieved from NIST, 2026-08-02.
- S. Alighanbari, M. R. Schenkel, V. I. Korobov, S. Schiller, *High-accuracy laser spectroscopy of H₂⁺ and the proton–electron mass ratio*, **Nature 644, 69–75 (2025)**, doi:10.1038/s41586-025-09306-2. m_p/m_e = 1836.152673414(47), 26 ppt. *(Earlier drafts of this document cited "Nature 625". That was wrong.)*
- J.-Ph. Karr, S. Schiller, V. I. Korobov, S. Alighanbari, *Determination of a set of fundamental constants from molecular hydrogen ion spectroscopy: a modeling study*, Phys. Rev. A **112**, 022809 (2025), published 11 August 2025.
- S. Schiller, J.-Ph. Karr, *Prospects for the determination of fundamental constants with beyond-state-of-the-art uncertainty using molecular hydrogen ion spectroscopy*, Phys. Rev. A **109**, 042825 (2024). — the projection source for future precision; **the specific improvement factor quoted in earlier drafts has not been verified against either paper and is not asserted here.**

---

*Copyleft 2026. Don't be a cunt. Be kind.*
