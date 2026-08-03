# Pre-registration: the visible fraction (KS-41.1)

**Freeze date:** 2026-08-02
**Author:** G · Studio G · the420code.org
**Scope:** AP41 (*The Loop*), AP28 (channel count), Rosin Ø Proofs ch. 14 / ch. 16
**Switches engaged:** KS-41.1 (visible fraction), KS-R.8 (channel count)
**Reproduction:** `verify_cosmology.py`
**Status:** frozen for commit. **Contains a correction to the corpus's own quoted comparison — see §3.**

---

## 1. The registered value

> **Ω_visible = 1/21 = 4.76190 %**

Exactly one twenty-first. No rounding, no tolerance, no fitted quantity. The
21 is the channel count of AP28 — 6 faces × 3 dimensions + 3 actualisation
couplings — fixed before any cosmological quantity was computed.

The structural reading: the twenty-one channels admit two cuts. By coupling
type, 18 paired + 3 actualisation, which fixes G. By symmetry, **one asymmetric
channel plus twenty symmetric ones that the involution σ pairs into the 10:10
mirror** — and only the asymmetric channel radiates. The visible universe is
that one channel. It is one set of channels read two ways, not two counts.

---

## 2. Why this is the sharpest of the three dark-sector numbers

Of the partition — dark energy 68.85 %, dark matter 26.39 %, visible 4.76 % —
the visible fraction is the one measured best and predicted most rigidly.
Ω_b is constrained two independent ways, by the CMB acoustic peaks and by
primordial deuterium abundance, and the two agree. There is nowhere to hide.

The other two carry model-dependence the visible fraction does not.

---

## 3. Correction: the agreement is worse than the corpus states

The site, the README and Ø Proofs all quote the observed visible fraction as
**4.86 %** and report the deviation as about 2 %.

Recomputing from Planck 2018 (TT,TE,EE+lowE+lensing+BAO: Ω_b h² = 0.02242,
Ω_c h² = 0.11933, h = 0.6766, Ω_m = 0.3111, Ω_Λ = 0.6889):

| Route | Ω_visible |
|---|---|
| Ω_b = Ω_b h² / h² | 4.8975 % |
| same, renormalised so the three sum to unity | 4.9046 % |
| taking Ω_c = Ω_m − Ω_b instead | 4.8975 % |

**The observed value is 4.86–4.91 % depending on the data column and the
normalisation convention, not 4.86 %.** The corpus has been quoting the bottom
of that range, which flatters the agreement.

Against the middle of the range with a conservative ±0.05 absolute:

> **predicted 4.7619 % vs observed ≈ 4.885 ± 0.05 % → 2.46 σ**, a deviation of
> 2.5 %, not the 2.0 % the corpus reports.

This is not fatal — 2.5σ is tension, not death — but it must be stated at the
correct size, and the scheme dependence must be stated with it. **The
comparison figure in AP41, Ø Proofs ch. 14, the site and the README is
corrected to a range with its convention named.**

---

## 4. Kill and confirm conditions (binding)

1. **KILL.** A determination of Ω_b/Ω_total with total uncertainty below 0.5 %
   whose central value lies above 4.81 % (3σ from 1/21 at that precision) fires
   KS-41.1. DESI, CMB-S4 and improved deuterium abundances reach this range
   within roughly five years. **At present precision the claim is already at
   2.5σ, so this switch is close to firing and this document says so before
   the data does.**
2. **CONFIRM.** The observed fraction converges toward 4.76 % as systematics
   and the normalisation convention are settled.
3. **NO CONVENTION-SHOPPING.** The comparison must be made against a stated
   Planck data column with a stated normalisation. Selecting whichever
   convention gives the smallest deviation is the failure mode this clause
   exists to prevent, and the corpus has already committed it once (§3).
4. **NO CHANNEL-COUNT ADJUSTMENT.** 21 is frozen. It is load-bearing in three
   places — the proton's static count, the exponent of α in G, and this
   fraction. Moving it to improve this number destroys the other two by
   enormous margins; see `RIGIDITY.md`. If 21 is ever revised, every prediction
   it touches must be recomputed and re-registered together.

---

## 5. What this does and does not establish

**Does:** register an exact rational with no tolerance against a well-measured
quantity, at a precision that will discriminate within five years, with the
current tension stated at its true size.

**Does not:** establish the internal dark split (KS-42.6); establish that the
twenty mirror channels exist; or survive on its own. It is currently the
weakest-standing of the frozen numbers and is registered anyway, because a
registry that contains only the comfortable results is not a registry.

---

*Copyleft 2026. Don't be a cunt. Be kind.*
