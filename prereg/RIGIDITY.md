# Rigidity: the answer to "this is numerology"

**Date:** 2026-08-02 · **Reproduction:** `verify_rigidity.py`
**Author:** G · Studio G · the420code.org

---

## 1. The charge, stated at full strength

*You have a handful of small integers — 3, 4, 6, 21 — and π, and a free choice
of where to put them. With that much freedom you can hit any target you like.
Matching a measured number to eleven digits is not evidence; it is what happens
when you have enough knobs and a number to aim at.*

That charge is correct as a general principle, and this document does not
dispute it. Precision alone proves nothing. **The question is not how close the
numbers land. The question is how much freedom was available when they were
written.** That is a computable quantity, and this document computes it.

---

## 2. The integer is not free

21 is not chosen. It is built:

    21 = 6 × 3 + 3

Six faces of the break (AP24) across three spatial dimensions (AP10), plus
three actualisation couplings. Both inputs are derived upstream — the dimension
count from four axioms giving four faces, one uniquely irreversible; the six
faces from the residual reading — and both were fixed **before any mass ratio,
gravitational constant or dark-sector split was computed.** That ordering is
checkable against the corpus's dependency graph: AP10 and AP28 precede AP30,
AP41 and AP42.

So the perturbations available to a fitter are not "any integer near 21." They
are: change the face count, or change the dimension count. Those give
21 → 18 (five faces), 24 (seven faces), 28 (four dimensions), 14 (two
dimensions). Everything else is ad hoc.

---

## 3. What breaks when the integer moves

Substituting N for 21 consistently everywhere it appears — the static count
N²·4 + N·3 + 3², the leakage denominator 4Nπ, the α² normalisation, the
exponent in G, and the visible fraction 1/N:

| N | where it comes from | m_p/m_e error | G error | visible fraction error |
|---|---|---|---|---|
| 14 | 2 dimensions | −54.5 % | 9 × 10¹⁴ × too big | +46 % |
| 18 | 5 faces | −26.0 % | 2.6 × 10⁶ × too big | +13.7 % |
| 20 | ad hoc | −9.10 % | **138 × too big** | +2.4 % |
| **21** | **6 faces, 3 dimensions** | **1 × 10⁻⁹ %** | **+0.69 %** | **−2.5 %** |
| 22 | ad hoc | +9.53 % | −99.3 % | −7.0 % |
| 24 | 7 faces | +29.9 % | −100 % | −14.7 % |
| 28 | 4 dimensions | +75.9 % | −100 % | −26.9 % |

**Read the G column.** N sits in an exponent: α^N. One step changes G by a
factor of 137. Not 137 %, a factor of 137. N = 20 overshoots by two orders of
magnitude; N = 22 undershoots by two.

That is the argument, and it is a single sentence:

> **The same integer is pinned to eleven decimal places by a polynomial, to
> within a factor of 1.007 by an exponential, and to within a few percent by a
> reciprocal — three different functional forms, three unrelated observables,
> and no value but 21 survives all three.**

A fitter tuning the proton mass has a target width of order 10 % in N — 20 and
22 are both within 10 % on the mass ratio. The exponential in G closes that
window to a single integer, because being wrong by one costs a factor of 137.
There is no adjustment available. You cannot slide N to improve one number
without annihilating another by two orders of magnitude.

---

## 4. Where the argument is weak — stated first, not last

**(a) Rigidity is not uniqueness.** This shows that *within the corpus's own
family* the integer cannot move. It says nothing about whether a completely
different family of formulas, built from different primitives, would also work.
That is KS-30.4's between-family limb, and it is **open and unclosed.** The
corpus's within-family uniqueness claim was itself found wrong on 2026-08-02
and corrected (see `ERRATA-2026-08-02.md`).

**(b) Four of the five numbers are retrospective.** Every one was written
against a measurement that already existed. However honestly derived, no
outside reader can distinguish that from reverse engineering by inspection.
Only the frozen forward predictions — the proton at order α³, KS-45.1, KS-42.6,
KS-41.1 — and the lattice protocol can carry that weight, and they carry it
only in the future.

**(c) The digit count proves less than it looks.** Roughly: the proton formula
at order α involves a small number of discrete structural choices and returns
about nine significant figures. That ratio is good but it is not overwhelming,
and last night's α³ analysis showed exactly why — at third order the
measurement admits **910** grammar-consistent coefficients within 1σ. Freedom
expands fast once the constraint loosens. The defence does not rest on the
proton's digit count and should never be presented as if it does.

**(d) One coefficient is still owed.** The α² coefficient 16 has no structural
decomposition (KS-30.3). It is carried in the verified formula and its
provenance is an open debt.

---

## 5. The evidence numerology cannot produce

A framework built by fitting produces a characteristic signature: everything
lands, nothing is ever wrong, and the errors are all comfortably inside
whatever tolerance was quoted. This corpus does not have that signature.

- **G lands at 0.69 %** — about 31σ against the measurement's formal bar, and
  roughly 14 times the historical scatter between G experiments. It passes
  KS-R.7's pre-stated 1 % tolerance and nothing more. **A fitter would have
  done better.** An unrepaired 0.69 % that has never been touched is stronger
  evidence of non-fitting than the proton's eleven digits, precisely because
  it is a poor result.
- **The neutron–proton difference fails at 7.24σ.** Predicted 2.53099393,
  measured 2.530988574 ± 0.00000074. The corpus quoted the offset as "about two
  parts per million" without stating that the measurement's own bar is 0.29 ppm.
  KS-NPP.1 has fired on its empirical limb. **Found, computed and published by
  the corpus itself.**
- **The uniqueness claim was wrong.** Two decompositions survive the three
  stated conditions, not one. Corrected the same day, with the fourth condition
  labelled post-hoc and dated.
- **The visible fraction is at 2.5σ, not the 2.0 % the corpus quoted**, because
  the observed value had been taken from the bottom of its scheme-dependent
  range. Corrected.
- **The muon is unreachable.** The three-layer construction has a floor of
  21² + 21 + 1 = 463. m_μ/m_e = 206.77 lies below it at any exponents. The
  lepton sector is not derived and the corpus says so.

Five negative results, four of them found by the corpus and published before
anyone outside asked. **That is not what fitting looks like. Fitting has no
mechanism for producing its own counter-evidence.**

---

## 6. What would actually settle it

Not another decimal place. Three things, in order of strength:

1. **The lattice mapping written blind and hashed before the numbers are
   looked at** (`PROTOCOL-lattice-qcd-mapping.md`). The only move that removes
   testimony from the argument entirely.
2. **The frozen forward predictions executing.** m_p/m_e at 3.3 ppt precision;
   H₀ converging above or below 71.9; Ω_b/Ω_total above or below 4.81 %;
   Ω_DM/Ω_b at z ≳ 4. Each has a stated kill condition and an execution window
   inside five years.
3. **KS-30.4's between-family limb closed** — a systematic search over
   alternative primitive sets showing how many other families reach 1836 at
   comparable precision. If the answer is "many," the corpus should say so.

Until at least one of those lands, the honest position is the one this document
takes: **the structure is rigid, the rigidity is real and computable, and
rigidity is not proof.**

---

*Copyleft 2026. Don't be a cunt. Be kind.*
