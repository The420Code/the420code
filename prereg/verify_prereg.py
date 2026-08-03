#!/usr/bin/env python3
"""
verify_prereg.py — regenerates every number in 2026-08-02-mp-me-alpha3.md
from CODATA 2022 inputs. No fitted quantities are used as input.

    pip install mpmath
    python3 verify_prereg.py

Inputs are CODATA 2022 (NIST, physics.nist.gov/cuu/Constants, 2026-08-02).
Copyleft 2026. Don't be a cunt. Be kind.
"""
from itertools import combinations_with_replacement
from mpmath import mp, mpf, pi, sqrt

mp.dps = 50

# ------------------------------------------------------------------ inputs
AINV, AINV_U = mpf('137.035999177'), mpf('0.000000021')   # CODATA 2022
MP_ME, MP_ME_U = mpf('1836.152673426'), mpf('0.000000032')
MU_ME = mpf('206.7682827')

ALPHA = 1 / AINV
ALPHA_U = ALPHA * (AINV_U / AINV)

ppt = lambda x: x / MP_ME * mpf(1e12)
ppb = lambda x: x / MP_ME * mpf(1e9)
s = lambda x, n=6: mp.nstr(x, n)


def rule(title):
    print('\n' + title + '\n' + '-' * len(title))


# ------------------------------------------------------- §4 frozen value
rule('SECTION 4 — the frozen O(alpha^2) value')
T0 = mpf(21**2 * 4 + 21 * 3 + 3**2)
T1 = ALPHA * 21 * (1 - 1 / (84 * pi))
T2 = ALPHA**2 * 21 * mpf(16) / 1836
D = T0 + T1 + T2

dD = 21 * (1 - 1 / (84 * pi)) + 2 * ALPHA * 21 * mpf(16) / 1836
D_U = dD * ALPHA_U
U = sqrt(MP_ME_U**2 + D_U**2)
resid = D - MP_ME

print(f'  21^2*4 + 21*3 + 3^2              = {T0}')
print(f'  alpha*21*(1 - 1/(84*pi))         = {s(T1, 15)}')
print(f'  alpha^2*21*16/1836               = {s(T2, 15)}')
print(f'  D                                = {s(D, 16)}')
print(f'  u(D) propagated from alpha       = {s(ppt(D_U), 3)} ppt')
print(f'  D - measured                     = +{s(ppt(resid), 4)} ppt  (+{s(ppb(resid), 4)} ppb)')
print(f'  measurement uncertainty          = {s(ppt(MP_ME_U), 4)} ppt')
print(f'  discrepancy                      = {s(resid / U, 3)} sigma')
print(f'  sign required of any alpha^3 term to close it: NEGATIVE')
print(f'  (alpha and alpha^2 terms are both positive)')

# --------------------------------------------- §4a alpha^2 coefficient pinned
rule('SECTION 4a — the alpha^2 coefficient is empirically pinned')
c2 = (MP_ME - T0 - T1) / ALPHA**2
c2u = MP_ME_U / ALPHA**2
corpus_c2 = mpf(21) * 16 / 1836
print(f'  required by measurement          = {s(c2, 7)} +/- {s(c2u, 3)}')
print(f'  constraint                       = {s(c2u / c2 * 100, 3)} % of the value')
print(f'  corpus 21*16/1836                = {s(corpus_c2, 7)}')
print(f'  agreement                        = {s(abs(corpus_c2 - c2) / c2u, 3)} sigma')
print(f'  implied owed integer  16         = {s(c2 * 1836 / 21, 6)} +/- {s(c2u * 1836 / 21, 3)}')
num, numu = c2 * 1836, c2u * 1836
print(f'  numerator over 1836              = {s(num, 7)} +/- {s(numu, 3)}')
lo, hi = int(mp.floor(num - 3 * numu)), int(mp.ceil(num + 3 * numu))
prods = {21**i * 3**j * 4**k for i in range(3) for j in range(7) for k in range(6)
         if 21**i * 3**j * 4**k <= 500}
hits = [n for n in range(lo, hi + 1) if n in prods]
print(f'  integers in the 3-sigma window   = {list(range(lo, hi + 1))}')
print(f'  ... that are products of 21,3,4  = {hits}   <- 336 = 21x16 = 84x4 = 4^2x21')
rank3 = mpf(21 * 64) / 1836
print(f'  naive rank-3 continuation 4^3=64 -> c3 = {s(rank3, 5)}, which lands at '
      f'{s(abs(D + rank3 * ALPHA**3 - MP_ME) / U, 3)} sigma  -> EXCLUDED')
print('  any derivation giving 16 at order 2 must NOT give 64 at order 3.')

# --------------------------------------------------- §5 c3 is unconstrained
rule('SECTION 5 — the order-3 coefficient is unconstrained')
c3 = -resid / ALPHA**3
c3u = U / ALPHA**3
print(f'  alpha^3                          = {s(ALPHA**3, 8)}')
print(f'  c3 = -(D - measured)/alpha^3     = {s(c3, 4)} +/- {s(c3u, 4)}  (1 sigma)')
print(f'  1 sigma interval                 = [{s(c3 - c3u, 4)}, {s(c3 + c3u, 4)}]')
print(f'  uncertainty / |central|          = {s(c3u / abs(c3), 3)}')

hits, seen = 0, set()
for a in range(-1, 3):
    for b in range(0, 3):
        for c in range(0, 3):
            for d in range(0, 3):
                for e in range(0, 3):
                    for f in range(0, 3):
                        v = (mpf(21)**a * mpf(3)**b * mpf(4)**c * mpf(6)**d
                             / (mpf(1836)**e * pi**f))
                        for sg in (1, -1):
                            cv = sg * v
                            if abs(D + cv * ALPHA**3 - MP_ME) / U < 1:
                                k = mp.nstr(cv, 12)
                                if k not in seen:
                                    seen.add(k)
                                    hits += 1
print(f'  bounded grammar +/-21^a 3^b 4^c 6^d / (1836^e pi^f), exponents in [-1,2]:')
print(f'  distinct admissible c3 values within 1 sigma = {hits}')

rule('  named candidates (none of these is registered as a prediction)')
for lab, cv in [('D   series terminates, c3 = 0', mpf(0)),
                ('    c3 = -1/21', -mpf(1) / 21),
                ('    c3 = +1/21  (sign the stated rule implies)', mpf(1) / 21),
                ('    c3 = -21*4/1836', -mpf(84) / 1836),
                ('    c3 = -21*16/1836  (same-coefficient continuation)', -mpf(336) / 1836),
                ('    c3 = +21*16/1836', mpf(336) / 1836),
                ('    c3 = -21*64/1836  (rank-3 escalation)', -mpf(1344) / 1836)]:
    v = D + cv * ALPHA**3
    print(f'  {lab:46s} {s(v, 16)}  {s(abs(v - MP_ME) / U, 3):>7s} sigma')

# ------------------------------------------------ §6 uniqueness enumeration
rule('SECTION 6 — decomposition enumeration')
terms = {}
for a in range(0, 3):
    for b in range(0, 8):
        for c in range(0, 6):
            v = 21**a * 3**b * 4**c
            if v <= 1836:
                terms.setdefault(v, (a, b, c))

vals = sorted(terms)
c12 = [t for t in combinations_with_replacement(vals, 3) if sum(t) == 1836]

order21 = lambda t: sorted(t, key=lambda x: terms[x][0], reverse=True)
nfac = lambda x: sum(terms[x])            # structural factors, counted with multiplicity


def cond3(t):                             # 21-exponent strictly decreasing
    e = [terms[x][0] for x in order21(t)]
    return e[0] > e[1] > e[2]


def cond4(t):                             # factor count non-increasing: the hierarchy sheds
    f = [nfac(x) for x in order21(t)]
    return f[0] >= f[1] >= f[2]


def show(t):
    d = order21(t)
    return (' + '.join(f'21^{terms[x][0]}*3^{terms[x][1]}*4^{terms[x][2]}' for x in d)
            + ' = ' + ' + '.join(str(x) for x in d)
            + '   factors ' + str([nfac(x) for x in d]))


for lbl, sel in [('1+2      ', lambda t: True),
                 ('1+2+3    ', cond3),
                 ('1+2+4    ', cond4),
                 ('1+2+3+4  ', lambda t: cond3(t) and cond4(t))]:
    r = [t for t in c12 if sel(t)]
    print(f'  conditions {lbl}: {len(r)}')
    for t in r:
        print('      ', show(t))
print(f'  \u00d8 Predictions reports 11 under 1+2 -> reproduced')
print(f'  \u00d8 Predictions reports  1 under 1+2+3 -> NOT reproduced (2)')
print(f'  condition 4 formalised 2026-08-02, after the alternative surfaced; see \u00a76')

# ---------------------------------------------------------- §7 kill margins
rule('SECTION 7 — when D dies, if the central value holds')
for n in (3, 5):
    print(f'  {n} sigma reached at measurement uncertainty <= {s(ppt(resid) / n, 3)} ppt')
print(f'  current: CODATA 2022 {s(ppt(MP_ME_U), 3)} ppt | HD+ 20.2 ppt | H2+ 25.6 ppt')

# ----------------------------------------------------------------- §9 muon
rule('SECTION 9 — the muon is below the construction floor')
floor = 21**2 + 21 + 1
print(f'  minimum three-term sum with strictly decreasing 21-exponents:')
print(f'    21^2 * 1  +  21^1 * 1  +  21^0 * 1  =  441 + 21 + 1  =  {floor}')
print(f'  m_mu/m_e = {MU_ME}  <  {floor}')
print(f'  unreachable at any exponents. The lepton sector is not derived.')
print()
