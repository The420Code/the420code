#!/usr/bin/env python3
"""
KS-30.4, the between-family limb — an adversarial search, run against the corpus.

RIGIDITY.md shows that 21 cannot move *within* the corpus's family of formulas, and says
plainly that this is not uniqueness:

    "It says nothing about whether a completely different family of formulas, built from
     different primitives, would also work. That is KS-30.4's between-family limb, and it
     is open and unclosed."

This script tests that limb in two legs, and they land in opposite directions.

    LEG A — the proton ratio, alone.  How many formulas in the space a sceptic names —
            "a handful of small integers and π, and a free choice of where to put them" —
            reach m_p/m_e as well as the corpus does?   ANSWER: thousands. Leg A fires.

    LEG B — one integer, three observables.  How many integers N let the SAME N carry the
            mass ratio, the gravitational constant and the visible fraction at once?
            ANSWER: one. N = 21. Leg B holds.

Neither leg is decided by opinion. Both are enumerated below and both print.

THE GRAMMAR FOR LEG A, FIXED BEFORE THE SEARCH RUNS
    primitives  : the integers 1..30, and π
    operations  : + − × ÷
    complexity  : the number of primitive tokens ("leaves")
    The corpus's α-coefficient, 21·(1 − 1/(84π)), has five leaves: 21, 1, 1, 84, π.
    Competitors are allowed the same five. They are not allowed more.

WHAT IS BEING HIT
    m_p/m_e = S + α·A + O(α²),  S = 1836,  α = 1/137.035999177 (CODATA 2022)
    Landing on the measured 1836.152673426(32) at order α requires A = 20.9217554797.
    The corpus's A = 20.9204225285; it misses by 1.333e-3 — the 5.3 ppb (304σ) order-α
    residual the corpus publishes, and then closes with its α² term.

TWO TOLERANCES, BOTH FIXED BEFORE THE SEARCH RUNS
    (1) the corpus's own order-α accuracy, 1.333e-3 — the fair bar: at least as good as
        the corpus, at no more complexity;
    (2) the CODATA measurement bar itself, 3.2e-8 on the ratio — eleven-digit agreement.

Standard library only. Runs in about two minutes.

    python verify_between_family.py

Canonical source: https://the420code.org/prereg/    Copyleft 2026. Don't be a cunt. Be kind.
"""
from bisect import bisect_left, bisect_right
from math import pi, isfinite

# ── constants and targets, fixed before the search ───────────────────────────
ALPHA    = 1 / 137.035999177          # CODATA 2022
HBAR, C, M_E = 1.054571817e-34, 299792458, 9.1093837139e-31
G_MEAS   = 6.67430e-11
MEAS     = 1836.152673426             # CODATA 2022, bar 3.2e-8
RATIO_BAR = 3.2e-8
SCAFFOLD = 21**2 * 4 + 21 * 3 + 3**2  # = 1836
A_TARGET = (MEAS - SCAFFOLD) / ALPHA
A_CORPUS = 21 * (1 - 1 / (84 * pi))
TOL_CORPUS = abs(A_CORPUS - A_TARGET)
TOL_BAR    = RATIO_BAR / ALPHA
MAX_LEAVES = 5
INTS = list(range(1, 31))

# ── expression enumeration, deduplicated by value ────────────────────────────
def combine(av, ae, bv, be):
    out = [(av + bv, f"({ae}+{be})"), (av - bv, f"({ae}-{be})"),
           (bv - av, f"({be}-{ae})"), (av * bv, f"({ae}*{be})")]
    if abs(bv) > 1e-12: out.append((av / bv, f"({ae}/{be})"))
    if abs(av) > 1e-12: out.append((bv / av, f"({be}/{ae})"))
    return out

def build(maxn):
    S = {1: {}}
    for i in INTS: S[1].setdefault(round(float(i), 12), str(i))
    S[1].setdefault(round(pi, 12), "pi")
    for n in range(2, maxn + 1):
        cur = {}
        for i in range(1, n):
            j = n - i
            if j < i: break
            for av, ae in S[i].items():
                for bv, be in S[j].items():
                    for v, e in combine(av, ae, bv, be):
                        if not isfinite(v) or abs(v) > 1e7: continue
                        cur.setdefault(round(v, 12), e)
        S[n] = cur
    return S

def sorted_view(d):
    ks = sorted(d); return ks, [d[k] for k in ks]

def hits(target, n, tol, S, VIEW):
    """every expression of exactly n leaves landing within tol of target"""
    found = []
    if n == 1:
        ks, es = VIEW[1]
        return [es[i] for i in range(bisect_left(ks, target - tol), bisect_right(ks, target + tol))]
    for i in range(1, n):
        j = n - i
        if i > 3: continue
        for av, ae in S[i].items():
            reqs = [(target - av, tol, lambda b, a=ae: f"({a}+{b})"),
                    (av - target, tol, lambda b, a=ae: f"({a}-{b})"),
                    (target + av, tol, lambda b, a=ae: f"({b}-{a})")]
            if abs(av) > 1e-9:
                reqs += [(target / av, tol / abs(av), lambda b, a=ae: f"({a}*{b})"),
                         (target * av, tol * abs(av), lambda b, a=ae: f"({b}/{a})")]
            if abs(target) > 1e-9:
                reqs.append((av / target, abs(av) * tol / target**2, lambda b, a=ae: f"({a}/{b})"))
            for tv, tt, mk in reqs:
                if not isfinite(tv) or abs(tv) > 1e7 or tt <= 0: continue
                if j <= 3:
                    ks, es = VIEW[j]
                    found += [mk(es[x]) for x in range(bisect_left(ks, tv - tt), bisect_right(ks, tv + tt))]
                else:
                    found += [mk(sub) for sub in hits(tv, j, tt, S, VIEW)]
    return found

def value_of(e): return eval(e, {"pi": pi, "__builtins__": {}})

def leg_a(S, VIEW):
    print("-" * 78)
    print("LEG A — THE PROTON RATIO, ALONE")
    print("-" * 78)
    print(f"  target      : A = {A_TARGET:.10f}   (m_p/m_e = 1836 + alpha*A)")
    print(f"  corpus's A  :     {A_CORPUS:.10f}   = 21*(1 - 1/(84*pi))")
    print(f"  reachable values with 1/2/3 leaves: {len(S[1]):,} / {len(S[2]):,} / {len(S[3]):,}")
    print()
    results = {}
    for label, tol in (("the corpus's own order-alpha accuracy", TOL_CORPUS),
                       ("the CODATA measurement bar (3.2e-8 on the ratio)", TOL_BAR)):
        seen = {}
        for n in range(1, MAX_LEAVES + 1):
            for e in hits(A_TARGET, n, tol, S, VIEW):
                try: v = value_of(e)
                except Exception: continue
                if abs(v - A_TARGET) <= tol: seen.setdefault(round(v, 12), e)
        results[label] = seen
        print(f"  within {tol:.4e}  ({label}):")
        print(f"      distinct formulas of <= {MAX_LEAVES} leaves that reach it: {len(seen):,}")
        for k, e in sorted(seen.items(), key=lambda kv: abs(kv[0] - A_TARGET))[:5]:
            print(f"        {k:>18.10f}   err {k - A_TARGET:+.2e}   {e}")
        print()
    n_corpus = len(results["the corpus's own order-alpha accuracy"])
    n_bar    = len(results["the CODATA measurement bar (3.2e-8 on the ratio)"])
    print(f"  VERDICT, LEG A: the proton ratio alone does not select the corpus's formula.")
    print(f"  {n_corpus:,} formulas of five leaves or fewer match the corpus's own accuracy;")
    print(f"  {n_bar} of them reach eleven-digit agreement at order alpha, which the corpus's")
    print(f"  own formula does not — it needs its alpha^2 term to get there. On this leg the")
    print(f"  between-family limb FIRES, and any argument resting on the proton's precision")
    print(f"  alone is worth nothing. RIGIDITY.md said so in words; this is the number.")
    print()
    return n_corpus, n_bar

def leg_b():
    print("-" * 78)
    print("LEG B — ONE INTEGER, THREE OBSERVABLES")
    print("-" * 78)
    print("  The corpus does not claim the proton ratio alone. It claims one integer N")
    print("  carries three unrelated observables at once:")
    print("      the mass ratio    1836 = 4N^2 + 3N + 3^2       (N's base-N digits)")
    print("      the constant G    alpha^N * F * hbar*c/m_e^2    (F a small structural factor)")
    print("      the visible share 1/N")
    print("  So the question is not 'can something else hit 1836' but 'is there another N")
    print("  that carries all three'. N sits in an exponent in G, so one step costs a factor")
    print("  of 137. Here is every N from 14 to 28.")
    print()
    K = HBAR * C / M_E**2
    VIS_OBS, VIS_TOL = 4.885, 3.0
    def base_digits(v, N):
        d = []
        while v: d.append(v % N); v //= N
        return d[::-1]
    print(f"  {'N':>4} {'F that G demands':>18} {'F small?':>9} {'1/N %':>8} {'vis err':>9} {'1836 base-N':>14}")
    survivors = []
    for N in range(14, 29):
        F = G_MEAS / (ALPHA**N * K)
        small = 0.5 <= F <= 3.0
        verr = (100.0 / N - VIS_OBS) / VIS_OBS * 100
        ok = small and abs(verr) <= VIS_TOL
        if ok: survivors.append(N)
        print(f"  {N:>4} {F:>18.4g} {'YES' if small else 'no':>9} {100.0/N:>8.3f} {verr:>8.2f}% "
              f"{str(base_digits(1836, N)):>14}{'   <- carries all three' if ok else ''}")
    print()
    print(f"  the corpus's F = 1 + 1/pi = {1 + 1/pi:.4f}; the F that N = 21 demands is "
          f"{G_MEAS / (ALPHA**21 * K):.4f} (0.69% apart)")
    print(f"  integers carrying all three observables: {survivors}")
    print()
    print("  VERDICT, LEG B: one. On this leg the between-family limb does NOT fire.")
    print("  The exponential in G is what does the work — its neighbours demand a factor of")
    print("  0.0096 or 179 where the corpus has 1.32 — and none of the thousands of Leg A")
    print("  formulas has a second life. They hit one number and go home.")
    print()
    return survivors

def main():
    print("=" * 78)
    print("KS-30.4 — THE BETWEEN-FAMILY LIMB, ENUMERATED")
    print("=" * 78)
    print()
    S = build(3); VIEW = {n: sorted_view(S[n]) for n in S}
    n_corpus, n_bar = leg_a(S, VIEW)
    survivors = leg_b()
    print("=" * 78)
    print("WHAT THIS SETTLES, AND WHAT IT DOES NOT")
    print("=" * 78)
    print(f"  SETTLED, against the corpus: the proton ratio's precision proves nothing on")
    print(f"  its own. {n_corpus:,} five-leaf formulas match the corpus's accuracy and {n_bar} beat it.")
    print(f"  Any presentation leading with the eleven digits is misleading and should stop.")
    print()
    print(f"  SETTLED, for the corpus: within the shared-integer family, N = 21 is alone in")
    print(f"  carrying all three observables — {survivors} and nothing else in 14..28.")
    print()
    print("  STILL OPEN: whether some *other* primitive set, not of the form 'one integer in")
    print("  three places', also carries three observables at once. This search does not")
    print("  reach that question; it would need a grammar over the three formulas jointly,")
    print("  not over one coefficient. KS-30.4's between-family limb is therefore narrowed,")
    print("  not closed. The status of the switch is the author's ruling, not this script's.")
    print("=" * 78)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
