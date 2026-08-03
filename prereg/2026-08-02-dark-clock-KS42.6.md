# Pre-registration: the dark-sector clock (KS-42.6)

**Freeze date:** 2026-08-02
**Author:** G · Studio G · the420code.org
**Scope:** AP42 (*The Clock*), AP41 (*The Loop*), Rosin Ø Proofs ch. 14
**Switches engaged:** KS-42.6 (timescale ratio), KS-42.1 (dark-matter particle), KS-42.4 (equation of state), KS-40, KS-41
**Reproduction:** `verify_cosmology.py`
**Status:** frozen for commit.

---

## 1. What is registered, and what deliberately is not

**Registered — the timescale:**

> **τ / t_H = 6/21**, giving τ = 3.94 Gyr at t_H = 13.797 Gyr

**Registered — the direction:**

> **Ω_DM / Ω_b increases with cosmic time.**
> Dark matter is records still defragmenting behind horizons; dark energy is
> content that has completed defragmentation and returned to the 1:1 rest state.
> The dark-matter share is therefore a **clock reading** — the fraction of a
> process caught mid-way — not a fixed inventory.

**Not registered — the curve.** The corpus cannot yet compute Ω_DM(z). The
formation-history convolution that sets the feeding rate is an open joint
(debt D48) and the equation-of-state tension with supernova-plus-DESI fits is
already logged (KS-42.4). **Registering a redshift curve today would be
inventing one.** The sign and the timescale are what the structure gives, and
they are all that is frozen here.

t_H is an **input**, not a derivation (AP42 states this). The freeze is the
ratio 6/21, not the 3.94 Gyr, which moves with t_H.

---

## 2. Why this is the most exposed cosmological claim in the corpus

ΛCDM holds that the comoving densities of baryons and cold dark matter have
been fixed since recombination. Their ratio is a constant of the model.

The clock reading says the opposite: the ratio evolves, on a characteristic
scale of order 4 Gyr, because dark matter is being *produced* by a late-time
process rather than inherited from the early universe.

**These are not two parameterisations of the same thing. They contradict.**
That is the whole value of this freeze, and it is why it is worth registering
even though the curve is missing.

Note what the structure already answers without a free parameter: the twenty
mirror channels are geometric channels of the substrate, not radiating species,
so they contribute nothing to N_eff and do not disturb nucleosynthesis or the
CMB. That is a structural answer, not a computed bound, and it is stated as
such.

---

## 3. Kill and confirm conditions (binding)

1. **KILL — no evolution.** A determination of Ω_DM/Ω_b at z ≳ 4 consistent
   with the z = 0 value at 3σ, with systematics under control, kills the clock
   reading. High-redshift galaxy dynamics and gas kinematics (JWST, ALMA) are
   the natural instruments, and the measurement is being attempted now.
2. **KILL — the wrong sign.** Any credible determination that Ω_DM/Ω_b was
   *higher* in the early universe than today kills it outright.
3. **KILL — a particle.** Detection of a dark-matter particle with the
   abundance to account for the observed density (KS-42.1). This is the
   sharpest blade and the corpus names it as such.
4. **KILL — the ratio itself.** If the feeding rate that fits the observed
   split departs from 6/21 beyond the formation-history correction, KS-42.6
   fires. This condition cannot bite until D48 is discharged, and that is
   stated as a limitation, not hidden as a hedge.
5. **NO CURVE-FITTING LATER.** When the formation-history convolution is
   derived, the resulting Ω_DM(z) must be published *before* being compared
   against any high-z determination, referencing this file's hash. A curve
   produced after the data is not a prediction and will not be presented as one.

---

## 4. Standing declaration on the live tension

Current supernova-plus-DESI fits prefer an evolving dark-energy equation of
state that the constant-feeding model does not produce. **This is a live
tension, not a nuisance.** It is logged as KS-42.4 and the missing piece is the
same formation-history convolution named above. If the convolution is derived
and still fails to produce the observed w(z), the clock reading is wrong and
this file is the record that the corpus said so in advance.

---

## 5. What this does and does not establish

**Does:** commit the corpus to a falsifiable disagreement with the standard
cosmological model on a quantity that is being measured now, with the
limitation named and the escape route closed off.

**Does not:** establish the partition values (those are KS-41.1's business and
carry their own tension); establish that dark matter has no particle
explanation; or provide a redshift curve. The clock is Derived-Conditional on
D48, and the grade is not softened.

---

*Copyleft 2026. Don't be a cunt. Be kind.*
