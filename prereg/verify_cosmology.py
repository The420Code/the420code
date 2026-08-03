#!/usr/bin/env python3
"""
verify_cosmology.py — regenerates every number in the three cosmology freezes:
  2026-08-02-H0-KS45.1.md, 2026-08-02-dark-clock-KS42.6.md,
  2026-08-02-visible-fraction-KS41.1.md

    pip install mpmath  &&  python3 verify_cosmology.py

Copyleft 2026. Don't be a cunt. Be kind.
"""
from mpmath import mp, mpf, pi, log, exp, cos, tan, sqrt
mp.dps = 30

C = mpf(299792458)                       # m/s, exact
MPC = mpf('3.0856775814913673e22')       # m
A0 = mpf('1.2e-10')                      # m/s^2, empirical MOND scale (McGaugh)
T_H = mpf('13.797')                      # Gyr, input (AP42 does not derive it)
s = lambda x, n=6: mp.nstr(x, n)
rule = lambda t: print('\n' + t + '\n' + '-' * len(t))

# ------------------------------------------------------------- KS-45.1
rule('KS-45.1 — the Hubble constant from the acceleration floor')
apex = 2 * log(1 / cos(mpf('0.5')) + tan(mpf('0.5')))
print(f'  alpha_apex = 2*ln(sec(1/2)+tan(1/2)) = {s(apex,12)}')
print(f'  alpha_apex/(2*pi)                    = {s(apex/(2*pi),8)}')
H0 = 2 * pi * A0 * MPC / (apex * C * 1000)
print(f'  H0 = 2*pi*a0/(alpha_apex*c)          = {s(H0,6)} km/s/Mpc')
print('  registered: 74.3 +/- 1.2  (the bar is a0\'s, not the derivation\'s)\n')
for lab, m, u in [('H0DN 2026', '73.50', '0.81'), ('SH0ES', '73.0', '1.0'),
                  ('TRGB/CCHP', '69.8', '0.8'), ('Planck CMB', '67.4', '0.5')]:
    sig = sqrt(mpf('1.2')**2 + mpf(u)**2)
    print(f'    vs {lab:12s} {m:>6s} +/- {u}   ->  {s(abs(mpf("74.3")-mpf(m))/sig,3):>6s} sigma')
print()
for lab, H in [('H0DN 73.50', '73.50'), ('Planck 67.4', '67.4')]:
    ap = apex * C * (mpf(H) * 1000 / MPC) / (2 * pi)
    print(f'    forward at {lab:12s} -> a0 = {s(ap,5)}  ({s((ap/A0-1)*100,3)}% vs 1.2e-10)')
print(f'\n  kill threshold: converged H0 below {s(mpf("74.3")-2*mpf("1.2"),4)} fires KS-45.1')

# ------------------------------------------------------------- KS-41.1
rule('KS-41.1 — the visible fraction')
pred = mpf(1) / 21 * 100
print(f'  predicted 1/21 = {s(pred,6)} %   (exact rational, no tolerance)')
obh2, och2, h, Om, OL = (mpf('0.02242'), mpf('0.11933'), mpf('0.6766'),
                         mpf('0.3111'), mpf('0.6889'))
Ob, Oc = obh2 / h**2, och2 / h**2
print('  Planck 2018 TT,TE,EE+lowE+lensing+BAO, three defensible routes:')
print(f'    A  Ob = ob_h2/h^2                    {s(Ob*100,5)} %')
print(f'    B  renormalised so the three sum to 1 {s(Ob/(Ob+Oc+OL)*100,5)} %')
print(f'    C  Oc = Om - Ob instead               {s(Ob*100,5)} %')
mid, u = mpf('4.885'), mpf('0.05')
print(f'  observed range 4.86-4.91 %; midpoint {mid} +/- {u}')
print(f'  deviation {s((pred/mid-1)*100,3)} %   ->  {s(abs(pred-mid)/u,3)} sigma')
print(f'  NOTE: the corpus quotes 4.86 % (bottom of the range) and 2.0 %. Corrected.')
print(f'  kill threshold: central value above 4.81 % at sub-0.5 % precision')

# ------------------------------------------------------------- KS-42.6
rule('KS-42.6 — the dark-sector clock')
tau = mpf(6) / 21 * T_H
print(f'  tau/t_H = 6/21 = {s(mpf(6)/21,6)}   (this ratio is what is frozen)')
print(f'  tau = {s(tau,4)} Gyr at t_H = {T_H} Gyr (t_H is an input, not derived)')
fdm_d = (mpf(6) / 21) * (1 - exp(-mpf(21) / 6))
fde_d = 1 - fdm_d
print(f'  partition: DE {s(fde_d*20/21*100,5)} %  DM {s(fdm_d*20/21*100,5)} %  '
      f'Vis {s(mpf(1)/21*100,5)} %')
print('  registered direction: Omega_DM/Omega_b RISES with cosmic time.')
print('  LCDM holds that ratio fixed since recombination. These contradict.')
print('  NOT registered: Omega_DM(z). The convolution (D48) is owed.')
print()
