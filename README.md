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

The framework takes a single measured number, the fine-structure constant
α ≈ 1/137, and re-derives five fundamental results with **zero free parameters**:

| Result | Predicted | Measured | Error | Paper |
| --- | --- | --- | --- | --- |
| Proton-electron mass ratio | 1836.1526734444 | 1836.152673426 | 0.01 ppb | AP30 |
| Gravitational constant G | 6.7206 × 10⁻¹¹ | 6.6743 × 10⁻¹¹ | 0.69 % | AP28 |
| Neutron-proton mass difference | 2.53099393 mₑ | 2.53098829 mₑ | 2.2 ppm | AP30 |
| MOND acceleration a₀ (H₀ = 74.3) | 1.2000 × 10⁻¹⁰ | 1.2000 × 10⁻¹⁰ | 0.002 % | AP18 |
| Dark sector partition (DE/DM/Vis) | 68.85 / 26.39 / 4.76 % | 68.89 / 26.07 / 4.86 % | ≤ 1.2 % | AP41/42 |

Every claim in the corpus carries a **kill switch** — an explicit, published
condition under which it dies. 560 of them.

## Verify it yourself

Don't take anyone's word for it. The verification suite uses the Python standard
library only and runs in well under a second:

```bash
python verify.py
```

It re-derives all five results from α, prints a scorecard, and exits non-zero if
any derivation drifts outside its published tolerance. The badge above runs this
on every push.

## Independent verification

The numbers here are confirmed by an **independent re-derivation** built by
AJ Greyling — a separate program that takes the single axiom and one measured
number, re-derives the constants from scratch, and checks its working against the
original published script. They match to machine precision.

→ **[github.com/ajgreyling/the420code-proof](https://github.com/ajgreyling/the420code-proof)**

## What's in this repository

This repo is the full source of [the420code.org](https://the420code.org): the
exhibition pages, all 43 Artist's Proofs and 8 Notebooks as PDFs, the Structural
Glossary, the Master Kill Switch Registry, the verification code, and twelve
language editions.

## License

This work is **Copyleft**. You are free to download, print, share, and
distribute. You are not free to alter the source. Keep the signal clean.

---

*Artist: G · Studio G, Cape Town · Free forever.*

*Don't be a cunt. Be kind.*
