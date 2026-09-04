#!/usr/bin/env python3
"""
The 420 Code — the wave of September 2026: the four frozen results of the cost
family and the Assembly, recomputed from CODATA 2022 at 50 digits.

    python3 verify_family.py

Reproduces, to every printed digit:
  AP44  the realised gravitational constant (KS-CCC.3)      2026-09-04-G-KS-CCC.3.md
  AP47  the neutron-proton difference, realised (KS-FLIP.1) 2026-09-04-neutron-KS-FLIP.1.md
  AP46  the age of everything, one cycle (KS-STRETCH.3)     2026-09-04-age-KS-STRETCH.3.md
  AP48  the expansion rate, the closure (KS-ASM.1)          2026-09-04-H0-KS-ASM.1.md
and the two corpses beside them (KS-NPP.1, KS-45.1), shown, never repaired.

The one external dependency is mpmath (pip install mpmath).
Copyleft 2026. Don't be a cunt. Be kind.
"""
from mpmath import mp, mpf, pi, sqrt, log, exp, cos, tan, asinh

mp.dps = 50

# ── Inputs: CODATA 2022 (NIST) ────────────────────────────────────────────────
AINV   = mpf('137.035999177')            # 1/alpha
ALPHA  = 1 / AINV
HBAR   = mpf('1.054571817e-34')          # J s, exact
C      = mpf('299792458')                # m/s, exact
M_E    = mpf('9.1093837139e-31')         # kg
G_MEAS = mpf('6.67430e-11')              # N m^2 kg^-2 (CODATA 2018, unchanged 2022)
MP_ME  = mpf('1836.152673426')
MN_ME  = mpf('1838.68366200')
DELTA_U = mpf('7.4e-7')                  # 1-sigma bar on m_n/m_e - m_p/m_e
KM_PER_MPC = mpf('3.0857e19')
GYR    = mpf('365.25') * 86400 * mpf('1e9')

def s(x, n):
    return mp.nstr(x, n, strip_zeros=False)

out = []
P = out.append

# ── AP44: the realised G ─────────────────────────────────────────────────────
alpha_G  = ALPHA**21 * (1 + 1/pi)
G_struct = alpha_G * HBAR * C / M_E**2
G_real   = G_struct / (1 + ALPHA)
P('AP44 — THE SNAP: the gravitational constant, realised (KS-CCC.3)')
P('  alpha_G  = alpha^21 (1 + 1/pi)          = ' + s(alpha_G, 8))
P('  G_struct = alpha_G hbar c / m_e^2        = ' + s(G_struct, 6) + '   (AP28, provisioned: ' + s((G_struct/G_MEAS - 1)*100, 3) + ' %)')
P('  1/(1 + alpha)                            = ' + s(1/(1+ALPHA), 7))
P('  G_real   = G_struct / (1 + alpha)        = ' + s(G_real, 6) + '   (' + s((G_real/G_MEAS - 1)*100, 3) + ' % against CODATA ' + s(G_MEAS, 5) + ')')
P('  the fork (KS-CCC.3): the adjusted value migrates toward 6.672e-11, or stays at 6.6743e-11 and the commitment dies.')
P('')

# ── AP47: the neutron, realised — and the corpse ─────────────────────────────
d_bare = 3*(1 - 1/(2*pi)) + ALPHA*(1 + 1/(2*pi))
f2     = ALPHA**2 / (8*pi)
d_real = d_bare / (1 + f2)
d_meas = MN_ME - MP_ME
P('AP47 — THE FLIP: the neutron-proton mass difference, realised (KS-FLIP.1)')
P('  delta_bare = 3(1 - 1/2pi) + alpha(1 + 1/2pi) = ' + s(d_bare, 9) + '   [KS-NPP.1: FIRED 2026-08-02 at ' + s((d_bare - d_meas)/DELTA_U, 3) + ' sigma — shown, never repaired]')
P('  f2 = alpha^2 / (8 pi)                       = ' + s(f2, 6))
P('  delta_real = delta_bare / (1 + f2)          = ' + s(d_real, 12))
P('  measured (CODATA 2022 ratio difference)     = ' + s(d_meas, 10) + ' +/- ' + s(DELTA_U, 2) + '  (0.29 ppm)')
P('  residual                                    = ' + s((d_real - d_meas)/DELTA_U, 2) + ' sigma')
P('  KS-FLIP.3: the absent alpha^3 term would sit at ' + s(d_bare*ALPHA**3/(8*pi), 2) + ' m_e — ' + s(d_bare*ALPHA**3/(8*pi)/DELTA_U*100, 2) + ' % of the bar; adjudication waits on ~20x better B_d metrology.')
P('')

# ── AP46: the cycle ──────────────────────────────────────────────────────────
tau_C   = HBAR / (M_E * C**2)
escape  = ALPHA**-18 * tau_C
t_cycle = escape * 21 / 18
lane    = t_cycle / 21
AGE_MEAS, AGE_U = mpf('13.787'), mpf('0.020')
P('AP46 — THE STRETCH: the age of everything, one cycle (KS-STRETCH.3)')
P('  tau_C = hbar / (m_e c^2)                    = ' + s(tau_C, 11) + ' s   (the tick)')
P('  alpha^-18 ticks                             = ' + s(ALPHA**-18, 6))
P('  alpha^-18 tau_C (the thread)                = ' + s(escape, 5) + ' s = ' + s(escape/GYR, 5) + ' Gyr')
P('  x 21/18 (the duty)                          = ' + s(t_cycle/GYR, 5) + ' Gyr   (one cycle)')
P('  measured age (Planck 2018)                  = ' + s(AGE_MEAS, 5) + ' +/- ' + s(AGE_U, 2) + ' Gyr;  landing ' + s((t_cycle/GYR/AGE_MEAS - 1)*100, 2) + ' %')
P('  the lane (cycle/21)                         = ' + s(lane/GYR, 4) + ' Gyr;  the window ' + s((t_cycle - lane)/GYR, 4) + ' to ' + s((t_cycle + lane)/GYR, 4) + ' Gyr')
P('')

# ── AP48: the closure ────────────────────────────────────────────────────────
f_DM_dark = (mpf(6)/21) * (1 - exp(-mpf(21)/6))
f_DE = (1 - f_DM_dark) * 20/21
f_DM = f_DM_dark * 20/21
f_vis = mpf(1)/21
om_L, om_m = f_DE, f_DM + f_vis
H0t0 = (2/(3*sqrt(om_L))) * asinh(sqrt(om_L/om_m))
H0   = H0t0 / t_cycle * KM_PER_MPC
H0_lo = H0t0 / (t_cycle + lane) * KM_PER_MPC
H0_hi = H0t0 / (t_cycle - lane) * KM_PER_MPC
settled = H0 * sqrt(om_L)
Lam = 3 * (settled / KM_PER_MPC)**2 / C**2
P('AP48 — THE ASSEMBLY: the expansion rate, the closure (KS-ASM.1)')
P('  Omega_L, Omega_m (AP42, the corpus\'s count) = ' + s(om_L, 5) + ', ' + s(om_m, 5))
P('  H0 t0 = (2/(3 sqrt(Omega_L))) asinh sqrt(Omega_L/Omega_m) = ' + s(H0t0, 5) + '   (the pure number)')
P('  1 / cycle                                   = ' + s(KM_PER_MPC / t_cycle, 5) + ' km/s/Mpc')
P('  H0 = H0t0 / cycle                           = ' + s(H0, 5) + ' km/s/Mpc;  window ' + s(H0_lo, 4) + ' to ' + s(H0_hi, 4))
P('  Planck 2018 (TT,TE,EE+lowE+lensing)         = 67.4 +/- 0.5;  Cepheid ladder (JWST, SH0ES) 73.49 +/- 0.93 — outside the window')
P('  settled rate = H0 sqrt(Omega_L)             = ' + s(settled, 4) + ' km/s/Mpc = ' + s(settled/(KM_PER_MPC/t_cycle), 4) + ' of the cycle\'s inverse')
P('  Lambda = 3 H_inf^2 / c^2                    = ' + s(Lam, 4) + ' m^-2   (the same closure in other units)')
P('')

# ── The floor at the corpus's rate; the corpse of 74.3 ───────────────────────
CS2 = 2*log(1/cos(mpf('0.5')) + tan(mpf('0.5')))
a0  = CS2 * C * (H0/KM_PER_MPC) / (2*pi)
A0_MEAS = mpf('1.20e-10'); A0_U = sqrt(mpf('0.02e-10')**2 + mpf('0.24e-10')**2)
P('AP18 — THE FLOOR at the corpus\'s rate, and the corpse of KS-45.1')
P('  C_S^2 = 2 ln(sec 1/2 + tan 1/2)             = ' + s(CS2, 11))
P('  a0 = C_S^2 c H0 / (2 pi) at H0 = ' + s(H0, 4) + '     = ' + s(a0, 5) + ' m/s^2')
P('  empirical scale                             = 1.20e-10 +/- 0.02 (random) +/- 0.24 (systematic):  ' + s((A0_MEAS - a0)/A0_U, 2) + ' sigma low  (' + s((1 - a0/A0_MEAS)*100, 2) + ' %)')
P('  KS-45 (the coefficient 0.1662 vs the sky\'s 0.183 +/- 0.037): ' + s((A0_MEAS/(C*H0/KM_PER_MPC) - CS2/(2*pi))/mpf('0.037'), 2) + ' sigma — live')
P('  KS-45.1 as registered: 74.3 +/- 1.2;  (74.3 - H0)/1.2 = ' + s((mpf('74.3') - H0)/mpf('1.2'), 3) + ' sigma — FIRED 2026-09-03, shown, never repaired')
P('  honest width of the inversion: 74.3 +/- ' + s(mpf('74.3') * mpf('0.24')/mpf('1.20'), 3) + '   (the registered +/- 1.2 omitted the systematic)')
P('')
P('One measured input (alpha). Zero free parameters. Two corpses on the board.')

if __name__ == '__main__':
    print('\n'.join(out))
