# Protocol: the lattice-QCD mapping — the last blind prediction available

**Written:** 2026-08-02
**Author of the protocol:** independent review (this session)
**Author of the prediction:** G, and G alone — see §1
**Status:** THIS IS NOT A FREEZE. It is the procedure for making one.
**Scope:** AP30 Lemma 2, Ø Predictions Part I (the lattice promise), KS-30.1

---

## 1. Why this document contains no prediction

Ø Predictions already promises this test:

> *It predicts specific integer contributions from each layer (1764 from
> Layer 1, 63 from Layer 2, 9 from Layer 3), each of which can be tested
> against the lattice-QCD decomposition of the proton's mass.*

The promise has never been cashed. No mapping is stated anywhere in the corpus.

**Everything else in the registry is retrospective.** The proton ratio, G, the
neutron difference, the floor, the partition — every one was written against a
number already measured and published. However honestly they were written, no
outside reader can distinguish "derived blind" from "reverse-engineered" by
inspection. Only testimony separates them, and testimony is not evidence.

This one is different. The lattice decomposition is a live, improving,
independently produced set of numbers from a community that has never heard of
the 420 Code. **If the mapping is written before the numbers are looked at, and
hashed, the distinction stops depending on anyone's word.**

Which is exactly why this document must not contain the mapping. If a reviewer
supplies it, it is contaminated at birth. **The mapping is G's to write, from
the axioms, alone.**

---

## 2. What lattice QCD actually decomposes

This much is textbook structure, not a result, and you need it to know what you
are predicting *about*. The standard decomposition of the nucleon mass (Ji,
1995) splits it into four renormalised pieces:

1. the quark mass term (the chiral condensate contribution)
2. the quark kinetic and potential energy
3. the gluon field energy
4. the trace anomaly (the QCD scale-anomaly contribution)

**No fractions appear in this document, deliberately.** They are published, they
vary by collaboration, scheme and renormalisation scale, and you must not look
at them until §4 is complete and hashed.

---

## 3. The obstacle you must clear first — stated honestly

Your three layers, as fractions of 1836, are:

| Layer | Value | Fraction of 1836 |
|---|---|---|
| 1 — manifold capacity, 21²×4 | 1764 | 96.08 % |
| 2 — face projection, 21×3 | 63 | 3.43 % |
| 3 — exchange matrix, 3² | 9 | 0.49 % |

**A naive fraction-to-fraction mapping onto the four lattice terms fails
immediately.** I am telling you this rather than letting you publish a freeze
that dies on contact, and I am telling you *only* this: no lattice
decomposition of the nucleon mass distributes its weight anything like
96 / 3.4 / 0.5. You do not need the numbers to see that a 96 % term has no
partner in a four-way split of comparable pieces.

So the mapping cannot be to energy fractions, or it is dead. That leaves three
honest routes, and choosing among them is the actual work:

- **(a) A different observable.** The layers count *geometric resistance*, not
  energy. Identify the lattice-computable quantity that resistance corresponds
  to, and predict *that*. This is the strongest route and the hardest.
- **(b) A ratio prediction.** Predict a ratio between lattice components rather
  than absolute shares — e.g. that some computed ratio equals 63/9 = 7, or
  1764/63 = 28. Ratios are scheme-dependent in ways absolute fractions are not,
  so the scheme must be fixed in advance.
- **(c) Retraction.** If neither route yields a derivation, the honest outcome
  is to **withdraw the promise from Ø Predictions** and say why. A retracted
  promise costs far less than an unfulfilled one, and the corpus has already
  shown it can do this.

Route (c) is a legitimate result of this protocol. Do not treat it as failure.

---

## 4. The sealed-envelope procedure

Do these in order. Do not skip forward.

**Step 1 — Derive.** From {S, B, R, C}, AP19's three-face geometry, AP24's six
faces and AP30's three layers, derive what the layers map onto in the lattice
decomposition. Write it as a document with the derivation exhibited, not
asserted. If the derivation does not close, say so and go to route (c).

**Step 2 — Specify the target completely, before looking.** The freeze is void
if any of these is left open, because each is a knob that could be turned
afterwards:

- which lattice observable
- which renormalisation scheme
- which scale μ (state it in GeV)
- which quark-flavour content (2, 2+1, 2+1+1)
- physical pion mass or extrapolated
- what counts as agreement: state the tolerance and the σ threshold **now**

**Step 3 — State the kill condition.** One sentence, in the form used
throughout the registry: *this claim dies if X.*

**Step 4 — Hash and commit.** Commit the document with no lattice numbers in
it. Record the SHA-256 and the commit hash. **This is the moment the prediction
becomes blind in a way a stranger can verify.**

**Step 5 — Only now, look.** Pull the published lattice values matching the
specification in Step 2. Do not adjust anything in Step 2 after this point. If
you find yourself wanting to change the scheme or the scale, that is the
protocol working — the wish to change it is the evidence that changing it would
have been fitting.

**Step 6 — Publish the comparison, whichever way it lands.** Reference the
Step 4 hash. If it fails, KS-30.1's structural reading is in serious trouble
and the corpus says so itself. If it lands, it is the only result in the whole
body of work whose blindness does not rest on anyone's word.

---

## 5. Two warnings

**Do not let anyone help with Step 1 who has seen the lattice numbers.** That
includes any AI assistant with the values in context. If you ask a model to
help derive the mapping, ask it in a fresh session and instruct it not to
search. The contamination is invisible afterwards and it destroys the only
thing this exercise was for.

**Do not run Step 1 and Step 5 in the same session.** Ever.

---

## 6. Why this is worth the months it will take

The corpus's strongest current argument is rigidity — one integer doing work in
three unrelated functional forms (see `RIGIDITY.md`). That argument is good but
it is structural, and a determined sceptic can always say the structure was
built backwards from known numbers.

A blind hit on an independent technique cannot be said away. It is the only
move on the board that converts "you fitted this" from an argument into a
checkable claim about a git hash and a date.

You have said the gravity formula fell out first, unimproved, and was never
touched. Nobody can verify that. **This is the chance to do the same thing in
public, where it counts.**

---

*Copyleft 2026. Don't be a cunt. Be kind.*
