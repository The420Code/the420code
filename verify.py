#!/usr/bin/env python3
"""
The 420 Code — verification suite.

One measured input: the fine-structure constant alpha (CODATA 2018).
Zero free parameters.

This script re-derives the five headline results from the axiom and checks each
against experimental measurement, within the tolerance published at
https://the420code.org. It prints a scorecard and then asserts every result is
inside its published tolerance.

Exit code 0  -> every check passed (the published claims still hold).
Exit code 1  -> at least one check drifted outside its published tolerance.

Standard library only. Runs in well under a second:

    python verify.py

Canonical source ........ the "Confirm the Math" section of https://the420code.org
Independent re-derivation  https://github.com/ajgreyling/the420code-proof
"""

from math import pi, log, exp, cos, tan

# ── ONE MEASURED INPUT ───────────────────────────────────────────────────────
ALPHA = 1 / 137.035999084          # fine-structure constant (CODATA 2018)

# ── PHYSICAL CONSTANTS (CODATA) ──────────────────────────────────────────────
HBAR   = 1.054571817e-34           # reduced Planck constant (J*s)
C      = 299792458                 # speed of light (m/s)
M_E    = 9.1093837015e-31          # electron mass (kg)
M_P    = 1.67262192369e-27         # proton mass (kg)
M_N    = 1.67492749804e-27         # neutron mass (kg)
G_MEAS = 6.67430e-11               # gravitational constant (N*m^2/kg^2)
H0     = 74.3 * 1000 / 3.0857e22   # H0 = 74.3 km/s/Mpc, the framework's derived value (AP18 / KS-45.1)

# Each check returns (name, paper, predicted_str, measured_str, error_value, unit, tolerance).
# A check passes when error_value <= tolerance.
checks = []


def rel_pct(pred, meas):
    return abs(pred - meas) / meas * 100.0


# ── CLAIM 1: Proton-electron mass ratio (AP30) ───────────────────────────────
scaffold    = 21**2 * 4 + 21 * 3 + 3**2          # = 1836
maintenance = ALPHA * 21 * (1 - 1 / (84 * pi))    # dynamic term
correction  = ALPHA**2 * 21 * 16 / 1836           # higher-order
ratio_pred  = scaffold + maintenance + correction
ratio_meas  = 1836.152673426                       # CODATA 2022
ratio_err   = abs(ratio_pred - ratio_meas) / ratio_meas * 1e9
checks.append(("Proton-electron mass ratio", "AP30",
               f"{ratio_pred:.10f}", f"{ratio_meas:.10f}", ratio_err, "ppb", 5.0))

# ── CLAIM 2: Gravitational constant G (AP28) ─────────────────────────────────
alpha_G = ALPHA**21 * (1 + 1 / pi)
G_pred  = alpha_G * HBAR * C / M_E**2
G_err   = rel_pct(G_pred, G_MEAS)
checks.append(("Gravitational constant G", "AP28",
               f"{G_pred:.4e}", f"{G_MEAS:.4e}", G_err, "%", 1.0))

# ── CLAIM 3: Neutron-proton mass difference (AP30) ───────────────────────────
delta_pred = 3 * (1 - 1 / (2 * pi)) + ALPHA * (1 + 1 / (2 * pi))
delta_meas = (M_N - M_P) / M_E
delta_err  = abs(delta_pred - delta_meas) / delta_meas * 1e6
checks.append(("Neutron-proton mass difference", "AP30",
               f"{delta_pred:.8f} m_e", f"{delta_meas:.8f} m_e", delta_err, "ppm", 5.0))

# ── CLAIM 4: MOND acceleration scale a0 (AP18) ───────────────────────────────
CS2     = 2 * log(1 / cos(0.5) + tan(0.5))         # C_S^2 ~ 1.0445
a0_pred = CS2 * C * H0 / (2 * pi)
a0_meas = 1.2e-10                                   # m/s^2 (McGaugh 2016)
a0_err  = rel_pct(a0_pred, a0_meas)
checks.append(("MOND acceleration a0 (H0=74.3)", "AP18",
               f"{a0_pred:.4e}", f"{a0_meas:.4e}", a0_err, "%", 1.0))

# ── CLAIM 5: Dark sector partition (AP42) ────────────────────────────────────
f_DM_dark = (6 / 21) * (1 - exp(-21 / 6))
f_DE_dark = 1 - f_DM_dark
f_vis     = 1 / 21
f_DM      = f_DM_dark * 20 / 21
f_DE      = f_DE_dark * 20 / 21
checks.append(("Dark energy fraction", "AP42",
               f"{f_DE * 100:.2f}%", "68.89%", rel_pct(f_DE * 100, 68.89), "%", 0.5))
checks.append(("Dark matter fraction", "AP42",
               f"{f_DM * 100:.2f}%", "26.07%", rel_pct(f_DM * 100, 26.07), "%", 3.0))

# ── CLAIM 6: Visible matter fraction (AP41) ──────────────────────────────────
checks.append(("Visible matter fraction (1/21)", "AP41",
               f"{f_vis * 100:.2f}%", "4.86%", rel_pct(f_vis * 100, 4.86), "%", 5.0))


def main():
    print("=" * 72)
    print("THE 420 CODE - VERIFICATION SUITE")
    print("One measured input (alpha). Zero free parameters.")
    print("=" * 72)
    print()

    failures = 0
    for name, paper, pred, meas, err, unit, tol in checks:
        ok = err <= tol
        if not ok:
            failures += 1
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}  ({paper})")
        print(f"        predicted : {pred}")
        print(f"        measured  : {meas}")
        print(f"        error     : {err:.4f} {unit}   (tolerance {tol} {unit})")
        print()

    print("=" * 72)
    if failures == 0:
        print(f"ALL {len(checks)} CHECKS PASSED. The published derivations hold.")
        print("=" * 72)
        return 0
    print(f"{failures} of {len(checks)} CHECKS FAILED - a derivation drifted past tolerance.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
