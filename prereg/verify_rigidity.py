#!/usr/bin/env python3
"""
verify_rigidity.py — regenerates the table in RIGIDITY.md.

Substitutes N for 21 consistently everywhere the channel count appears:
the static count N^2*4 + N*3 + 3^2, the leakage denominator 4*N*pi, the
alpha^2 normalisation, the exponent in G, and the visible fraction 1/N.

    pip install mpmath  &&  python3 verify_rigidity.py

Copyleft 2026. Don't be a cunt. Be kind.
"""
from mpmath import mp, mpf, pi
mp.dps = 30

ALPHA = 1 / mpf('137.035999177')          # CODATA 2022, the one measured input
HBAR = mpf('1.054571817e-34')
C = mpf(299792458)
M_E = mpf('9.1093837139e-31')
MP_ME = mpf('1836.152673426')             # CODATA 2022
G_MEAS = mpf('6.67430e-11')
VIS_OBS = mpf('4.885')                    # Planck 2018, midpoint of scheme range
s = lambda x, n=4: mp.nstr(x, n)


def mass_ratio(N):
    static = N**2 * 4 + N * 3 + 9
    return (static
            + ALPHA * N * (1 - 1 / (4 * N * pi))
            + ALPHA**2 * N * 16 / static)


def gravitation(N):
    return ALPHA**N * (1 + 1 / pi) * HBAR * C / M_E**2


print('\n21 = 6 x 3 + 3   (six faces of the break, three spatial dimensions,')
print('                  three actualisation couplings) -- AP24 + AP10 + AP28,')
print('                  fixed before any mass, G or dark-sector value.\n')
print(f"{'N':>4s}  {'origin':<22s} {'m_p/m_e err':>13s} {'G err':>16s} "
      f"{'1/N':>7s} {'vis err':>9s}")
print('-' * 78)
for N, origin in [(14, '2 dimensions'), (18, '5 faces'), (20, 'ad hoc'),
                  (21, '6 faces, 3 dims'), (22, 'ad hoc'), (24, '7 faces'),
                  (28, '4 dimensions')]:
    r, G, v = mass_ratio(N), gravitation(N), mpf(100) / N
    dG = (G / G_MEAS - 1) * 100
    dG_str = f'{s(dG)}%' if abs(dG) < 1e4 else f'{s(G/G_MEAS,3)}x'
    mark = ' <--' if N == 21 else ''
    print(f'{N:>4d}  {origin:<22s} {s((r/MP_ME-1)*100):>12s}% {dG_str:>16s} '
          f'{s(v):>7s} {s((v/VIS_OBS-1)*100,3):>8s}%{mark}')

print(f'\nN sits in an exponent in G. One step multiplies G by alpha = '
      f'1/{s(1/ALPHA,9)}.')
print(f'  N -> N+1 : G x {s(ALPHA,4)}      N -> N-1 : G x {s(1/ALPHA,6)}')
print('\nThe mass ratio alone tolerates N = 20 or 22 to within 10 %.')
print('The exponential in G closes that window to a single integer.')
print('\nRigidity is not uniqueness. KS-30.4 between-family limb remains OPEN.\n')
