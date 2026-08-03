# Research note: deriving 336 (the owed O(α²) coefficient, KS-30.3)

**Written:** 2026-08-02 · **For:** G, whenever this becomes the live front
**Status:** a brief for future work. Contains no derivation and no answer.
**Companions:** `2026-08-02-mp-me-alpha3.md` §4a, `verify_prereg.py`

---

## 1. What changed on 2026-08-02

Before that date, KS-30.3 read as *the coefficient is unknown and its
decomposition is owed*. Both halves were open, so there was nothing to aim at.

The measurement was then inverted against the exactly known lower-order terms.
It pins the coefficient hard:

| | |
|---|---|
| required by CODATA 2022 | **0.1826623 ± 0.000601** (0.33 %) |
| corpus 21 × 16 / 1836 | 0.1830065 → **0.57 σ** |
| as a numerator over 1836 | **335.4 ± 1.1** |
| integers inside 3σ | 332 … 339 |
| of those, products of powers of {21, 3, 4} | **336, and only 336** |

**336 = 21 × 16 = 84 × 4 = 4² × 21.**

So the target is no longer "some integer." It is 336, to 0.33 %, and 336 is the
only structurally reachable integer in the window. **The value is settled; the
decomposition is what is owed.** A derivation returning 15 or 17 for the inner
count is falsified before it is checked.

---

## 2. The two-sided constraint — the part that makes this hard

A derivation must clear **both** of these, and the second is the sharp one:

1. **Produce 336 at order α².**
2. **Not produce 4³ = 64 at order α³.** The naive rank-escalation continuation
   gives c₃ = 21 × 64/1836 = 0.732, which is excluded at **9.5σ** with the same
   sign as the α² term, 8.3σ with the sign reversed. The measurement permits
   only c₃ ∈ [−0.130, +0.035].

Read those together and the shape of the answer is forced: **whatever produces
16 must saturate, terminate, or reverse at third order rather than escalate.**
A mechanism whose natural continuation is 4ⁿ is already dead. That is a genuine
constraint on the space of derivations and it did not exist before this freeze.

---

## 3. Three readings of 336, and what each would have to show

The same integer decomposes three ways within {21, 3, 4}. They are not the same
physics, and the derivation must pick one and say why.

**(a) 21 × 16 — channels × spacetime index pairs.**
The leaked amplitude re-couples through spacetime; re-coupling is rank-2,
(outgoing μ, incoming ν) over 4 dimensions, giving 4² = 16; the 21 is the
channel factor carried from order α. This is the corpus's existing informal
gloss. **What it owes:** why rank-2 and not rank-1 or rank-3, and why the
escalation to 4³ does not follow at the next order. Constraint 2 makes this
route's central obligation the *termination* argument, not the 16.

**(b) 84 × 4 — dimensional expressions × dimensions.**
84 = 21 × 4 is already load-bearing at order α, in the leakage denominator
1/(84π). Reading the second-order count as 84 × 4 keeps that object alive
across orders instead of introducing a new one. **What it owes:** why the
second factor is the bare dimension count 4 rather than 84 again, and how this
relates to the 1/(84π) that already carries 84.

**(c) 4² × 21 — the same arithmetic, opposite emphasis.**
Identical number, but here the primitive is the spacetime square and the 21
is normalisation. **What it owes:** the same as (a), plus a reason to treat 21
as a normaliser here when it is a count everywhere else.

Route (b) is the one I would examine first, because it reuses a structure the
formula already contains rather than importing a new one, and reuse is exactly
what the rigidity argument rests on.

---

## 4. Three things the derivation must **not** do

1. **Must not be 3² = 9.** AP30 §6 already says so — 9 is Layer 3, the static
   face-exchange matrix. The α² term is dynamic re-coupling. If a derivation
   arrives at 9 it has confused colour space with spacetime.
2. **Must not be fitted against 0.18266.** The number in §1 is now published.
   Anyone deriving 336 after this date is working with the answer visible. The
   derivation must therefore be exhibited step by step, and each step must be
   forced by {S, B, R, C} or by a result already locked upstream. **"It comes
   out right" is not an argument once the right answer is public.**
3. **Must not quietly change the normaliser.** The measurement constrains the
   *product* 21N/1836, not N alone. Any derivation that changes the
   denominator changes the numerator correspondingly, and the freeze document's
   figure must be recomputed if so.

---

## 5. Why this is worth doing before the neutron

The neutron repair needs a mechanism nobody has, with a sign nothing in AP30
motivates, on a formula whose empirical limb has already fired. It is a rebuild.

This is not a rebuild. The number is right, the target is a single integer, and
the obligation is to explain an object the formula already uses. It is the
highest-yield open item in the physics because:

- success closes KS-30.3 and converts the proton result from
  *"parameter-free at order α, with an owed coefficient at α²"* to
  *"parameter-free through α²"* — a materially stronger headline that is
  honestly earned;
- the termination argument required by constraint 2 is very likely **the same
  argument** the α³ freeze needs. Solving one may hand you the other, and the
  α³ coefficient is currently unconstrained, so whatever the mechanism outputs
  there is a genuine forward prediction;
- and unlike the lattice mapping, it needs no new external data. It is pure
  derivation against a target already on the page.

---

## 6. Where to start when you pick this up

Not with the 16. Start with the **termination**: what in {S, B, R, C} stops the
re-coupling rank from escalating past 2? If that argument exists, the count at
order α² usually falls out of it. If it does not exist, then 16 is a coincidence
and the honest outcome is to say so and let KS-30.3 stay open with the value
pinned and the decomposition abandoned.

That is a legitimate result too. The pinning in §1 stands either way, and it is
already a strengthening of the corpus whether or not the decomposition is ever
found.

---

*Copyleft 2026. Don't be a cunt. Be kind.*
