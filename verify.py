#!/usr/bin/env python3
"""
The 420 Code — verification suite.

One measured input: the fine-structure constant alpha (CODATA 2022).
Zero free parameters.

This script re-derives the headline results the corpus stands behind at the
wave of September 2026 and checks each against measurement, within the
tolerance published at https://the420code.org. It prints a scorecard, then the
two corpses — the switches that fired, shown and never repaired — and asserts
every live result is inside its published tolerance.

Exit code 0  -> every live check passed (the published claims still hold).
Exit code 1  -> at least one check drifted outside its published tolerance.

Standard library only. Runs in well under a second:

    python verify.py

Canonical source ........ the "Confirm the Math" section of https://the420code.org
Independent re-derivation  https://github.com/ajgreyling/the420code-proof
"""

from math import pi, log, exp, cos, tan, sqrt, asinh

# ── ONE MEASURED INPUT ───────────────────────────────────────────────────────
ALPHA = 1 / 137.035999177          # fine-structure constant (CODATA 2022)

# ── PHYSICAL CONSTANTS (CODATA 2022) ─────────────────────────────────────────
HBAR     = 1.054571817e-34         # reduced Planck constant (J*s), exact
C        = 299792458               # speed of light (m/s), exact
M_E      = 9.1093837139e-31        # electron mass (kg)
G_MEAS   = 6.67430e-11             # gravitational constant (N*m^2/kg^2)
RATIO_PE = 1836.152673426          # m_p/m_e (CODATA 2022)
RATIO_NE = 1838.68366200           # m_n/m_e (CODATA 2022)
DELTA_U  = 7.4e-7                  # 1-sigma bar on m_n/m_e - m_p/m_e (0.29 ppm)
KM_PER_MPC = 3.0857e19             # km in a megaparsec
GYR      = 365.25 * 86400 * 1e9    # seconds in a gigayear (Julian)

# Each check is (name, paper, predicted_str, measured_str, error_value, unit, tolerance).
# A check passes when error_value <= tolerance.
checks = []
corpses = []


def rel_pct(pred, meas):
    return abs(pred - meas) / meas * 100.0


# ── CLAIM 1: Proton-electron mass ratio — the series closed (AP49) ───────────
# AP30 stopped at a^2 with a coefficient of sixteen it declared owed under KS-30.3. AP49 The Hold
# paid that switch on 6 September 2026: the repair's share is r = 16a/1836, the series closes as a
# chain of holders, and every order follows from the ruling instead of being truncated. KS-HOLD.1.
scaffold    = 21**2 * 4 + 21 * 3 + 3**2          # = 1836
maintenance = ALPHA * 21 * (1 - 1 / (84 * pi))    # dynamic term
hold_share  = 16 * ALPHA / 1836                   # r, the repair's share of the previous order
correction  = 21 * ALPHA * hold_share / (1 - hold_share)   # all orders, not truncated at a^2
ratio_pred  = scaffold + maintenance + correction
ratio_err   = abs(ratio_pred - RATIO_PE) / RATIO_PE * 1e9
checks.append(("Proton-electron mass ratio", "AP49",
               f"{ratio_pred:.10f}", f"{RATIO_PE:.10f}", ratio_err, "ppb", 5.0))

# ── CLAIM 2: Gravitational constant G — realised (AP44) and structural (AP28) ─
alpha_G  = ALPHA**21 * (1 + 1 / pi)               # AP28: the provisioned coupling
G_struct = alpha_G * HBAR * C / M_E**2            # AP28: the structural value, +0.69%
G_real   = G_struct / (1 + ALPHA)                 # AP44: the arena's held epsilon, once
checks.append(("Gravitational constant G, realised", "AP44",
               f"{G_real:.4e}", f"{G_MEAS:.4e}", rel_pct(G_real, G_MEAS), "%", 1.0))
checks.append(("Gravitational constant G, structural (provisioned)", "AP28",
               f"{G_struct:.4e}", f"{G_MEAS:.4e}", rel_pct(G_struct, G_MEAS), "%", 1.0))

# ── CLAIM 3: Neutron-proton mass difference — realised (AP47) ────────────────
delta_bare = 3 * (1 - 1 / (2 * pi)) + ALPHA * (1 + 1 / (2 * pi))   # AP30: the flip priced as free — FIRED
delta_real = delta_bare / (1 + ALPHA**2 / (8 * pi))                  # AP47: the held distinction's cost
delta_meas = RATIO_NE - RATIO_PE
delta_sig  = abs(delta_real - delta_meas) / DELTA_U
checks.append(("Neutron-proton mass difference, realised", "AP47",
               f"{delta_real:.11f} m_e", f"{delta_meas:.9f} m_e", delta_sig, "sigma", 1.0))
corpses.append(("Neutron-proton mass difference, bare row", "AP30 / KS-NPP.1", "2026-08-02",
                f"{delta_bare:.8f} m_e", f"{delta_meas:.9f} m_e (CODATA 2022)",
                abs(delta_bare - delta_meas) / DELTA_U))

# ── CLAIM 4: Dark sector partition (AP42) and visible fraction (AP41) ────────
f_DM_dark = (6 / 21) * (1 - exp(-21 / 6))
f_DE_dark = 1 - f_DM_dark
f_vis     = 1 / 21
f_DM      = f_DM_dark * 20 / 21
f_DE      = f_DE_dark * 20 / 21

# ── CLAIM 5: The age of everything — one cycle (AP46) ────────────────────────
tau_C    = HBAR / (M_E * C**2)                    # the tick: the electron's reduced Compton time
t_cycle  = (21 / 18) * ALPHA**-18 * tau_C         # one escape through eighteen doors, at the duty 18/21
age_pred = t_cycle / GYR
age_meas = 13.787                                 # Gyr, Planck 2018 (TT,TE,EE+lowE+lensing+BAO), +/- 0.020
checks.append(("Age of the universe, one cycle", "AP46",
               f"{age_pred:.3f} Gyr", f"{age_meas:.3f} Gyr", abs(age_pred - age_meas), "Gyr", 0.66))

# ── CLAIM 6: The expansion rate — the closure (AP48) ─────────────────────────
omega_L = f_DE                                    # the reservoir, AP42's own count
omega_m = f_DM + f_vis                            # the held share, 31.15%
H0t0    = (2 / (3 * sqrt(omega_L))) * asinh(sqrt(omega_L / omega_m))   # the balance: rate x age, a pure number
H0_pred = H0t0 / t_cycle * KM_PER_MPC             # km/s/Mpc
H0_meas = 67.4                                    # Planck 2018 (TT,TE,EE+lowE+lensing), +/- 0.5
checks.append(("Expansion rate H0, the closure", "AP48",
               f"{H0_pred:.2f} km/s/Mpc", f"{H0_meas:.1f} km/s/Mpc", abs(H0_pred - H0_meas), "km/s/Mpc", 3.1))
corpses.append(("Hubble constant from the floor inverted", "AP18 / KS-45.1", "2026-09-03",
                "74.30 km/s/Mpc (+/- 1.2 as registered)", f"{H0_pred:.2f} km/s/Mpc (the corpus's own rate)",
                abs(74.3 - H0_pred) / 1.2))

# ── CLAIM 7: MOND acceleration scale a0 at the corpus's rate (AP18 / AP48) ──
CS2     = 2 * log(1 / cos(0.5) + tan(0.5))        # C_S^2 ~ 1.0445 (not the fine-structure constant)
H0_si   = H0_pred / KM_PER_MPC                    # s^-1
a0_pred = CS2 * C * H0_si / (2 * pi)
a0_meas = 1.20e-10                                # m/s^2 (McGaugh 2016; Lelli 2017)
a0_unc  = sqrt(0.02e-10**2 + 0.24e-10**2)         # random (+/-0.02) and systematic (+/-0.24), honestly
checks.append(("MOND acceleration a0 at the corpus's H0", "AP18",
               f"{a0_pred:.4e}", f"{a0_meas:.4e} +/- {a0_unc:.2e}", abs(a0_pred - a0_meas) / a0_unc, "sigma", 3.0))

checks.append(("Dark energy fraction", "AP42",
               f"{f_DE * 100:.2f}%", "68.89%", rel_pct(f_DE * 100, 68.89), "%", 0.5))
checks.append(("Dark matter fraction", "AP42",
               f"{f_DM * 100:.2f}%", "26.07%", rel_pct(f_DM * 100, 26.07), "%", 3.0))
checks.append(("Visible matter fraction (1/21)", "AP41",
               f"{f_vis * 100:.2f}%", "~4.885 +/- 0.05%", rel_pct(f_vis * 100, 4.885), "%", 5.0))


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

    print("-" * 72)
    print("CORPSES - switches that fired. Shown, never repaired, not counted.")
    print("-" * 72)
    for name, switch, date, pred, meas, sig in corpses:
        print(f"[FIRED] {name}  ({switch}, {date})")
        print(f"        registered: {pred}")
        print(f"        against   : {meas}")
        print(f"        offset    : {sig:.2f} sigma")
        print()

    print("=" * 72)
    if failures == 0:
        print(f"ALL {len(checks)} CHECKS PASSED. The published derivations hold. {len(corpses)} fired switches shown.")
        print("=" * 72)
        return 0
    print(f"{failures} of {len(checks)} CHECKS FAILED - a derivation drifted past tolerance.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
