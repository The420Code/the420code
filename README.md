# The 420 Code

**Ethics derived from physics.** One axiom. One measured input. Zero free parameters.

[![Verify](https://github.com/The420Code/the420code/actions/workflows/verify.yml/badge.svg)](https://github.com/The420Code/the420code/actions/workflows/verify.yml)

Live site: **[the420code.org](https://the420code.org)**

---

## The claim

One record exists. Trying to deny it produces another record, which proves at
least one record exists. From that single self-instantiating fact, four
conditions follow — symmetry, break, record, constraint — and from those four
conditions all of physics and one ethic are derived.

The 420 Code takes a single measured number, the fine-structure constant
α ≈ 1/137, and re-derives its headline results with **zero free parameters** — and shows the two that died:

| Result | Predicted | Measured | Agreement | Paper |
|---|---|---|---|---|
| Proton–electron mass ratio, the series closed | 1836.152673445 | 1836.152673426(32) | 10.3 ppt · +0.59σ | AP49 / AP30 |
| Gravitational constant G, realised | 6.6719 × 10⁻¹¹ | 6.6743 × 10⁻¹¹ (CODATA); 6.67191 × 10⁻¹¹ (atom interferometry) | −0.036 % against CODATA; +1 ppm against atom interferometry (AP28’s first reading, +0.69 %, withdrawn 21 September 2026) | AP44 |
| Neutron–proton mass difference, realised | 2.53098857035 mₑ | 2.53098857(74) mₑ | −0.005σ (the bare row, 2.53099393 mₑ, FIRED at 7.24σ on 2026-08-02 — KS-NPP.1, shown) | AP47 / AP30 |
| Age of the universe, one cycle | 13.830 Gyr | 13.787 ± 0.020 Gyr | +0.31 %, one lane-time wide | AP46 |
| Expansion rate H₀, the closure | 67.45 km/s/Mpc (window 64.4–70.8) | 67.4 ± 0.5 (Planck) | 0.1σ; the floor’s inversion 74.3 ± 1.2 FIRED on 2026-09-03 (KS-45.1, shown) | AP48 / AP18 |
| MOND acceleration a₀ at the corpus’s H₀ | 1.089 × 10⁻¹⁰ m/s² | 1.20 ± 0.24 × 10⁻¹⁰ (systematic) | 0.46σ (9.2 % low) | AP18 |
| Dark energy / dark matter / visible matter | 68.85 / 26.39 / 4.76 % | 68.89 / 26.07 / ≈ 4.885 % | −0.07σ / +0.8σ / −2.46σ | AP42 / AP41 |

> Every forward prediction is frozen and timestamped before the measurement that
> will test it, with the condition under which it dies, at
> [`/prereg/`](https://the420code.org/prereg/).

Every claim in the corpus carries a **kill switch** — an explicit, published
condition under which it dies. 604 of them, every one on one page at
[the420code.org/killswitches](https://the420code.org/killswitches/); two have fired and are shown, never repaired.

## Verify it yourself

Don't take anyone's word for it. The verification suite uses the Python standard
library only and runs in well under a second:

```bash
python verify.py
```

It re-derives the headline results from α, prints a scorecard and the two
corpses, and exits non-zero if any live derivation drifts outside its published
tolerance. The badge above runs this
on every push.

## Independent verification

The numbers here are confirmed by an **independent re-derivation** built by
AJ Greyling — a separate program that takes the single axiom and one measured
number, re-derives the constants from scratch, and checks its working against the
original published script. They match to machine precision.

→ **[github.com/ajgreyling/the420code-proof](https://github.com/ajgreyling/the420code-proof)**

## What's in this repository

This repo is the full source of [the420code.org](https://the420code.org): the
exhibition pages, all 54 Artist's Proofs and 8 Notebooks as PDFs, the Structural
Glossary, the Master Kill Switch Registry, the instruments beside each new proof
(`proofs/instruments/`), the frozen predictions (`prereg/`), the verification
code, and twelve language editions.

## License

This work is **Copyleft** (CC BY-ND 4.0). You are free to download, print, share,
and distribute. You are not free to alter the source. Keep the signal clean.

---

*Artist: G · Studio G, Cape Town · Free forever.*

*Don't be a cunt. Be kind.*
