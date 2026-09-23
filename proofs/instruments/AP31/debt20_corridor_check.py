
# Debt 20 - a check of the model, not a proof. 23 September 2026.
#
# The organism is an operator (AP02): its substrate S decays at drift rate a and holds
# only under input (Theorems I.1, II.1). Windows are operators too. Each has a capacity
# c (its corridor: the input it can bring per tick) and a budget w; it regenerates from
# its capacity, on the ground under it (Axiom C). Coupling moves energy and does not
# create it (AP02, Derivation VI), so a maintenance contribution is a transfer: X = Y.
# What the substrate holds above its maintenance returns to the windows as ground -
# cooperative coupling; the corridor can grow. Offers are generic (AP01 D1.3): a
# transfer to the substrate; cooperation between windows, which widens capacity
# (D4.4a); and an offer where the whole loses - the collective's share gains X, one
# window's capacity is cut by Y > X, for good (Axiom R). A closed window offers nothing.
# The rule R_b takes an offer iff (1 + b) X > Y. At b = 0 a tie is undecided. epsilon
# is the least tilt that breaks a tie - one grain - and b is quantised in grains.
# The loop (AP31 Step 2, KS-31.4), on with loop=True: the rule reads X and Y from the
# record, and the reading's error shrinks with the number of open windows.
import random, math

def run(b_grains, eps=0.01, ticks=8000, seed=1, N=40, a=0.02, c0=1.0,
        tie_at_zero='coin', loop=False, noise0=0.10, ret=0.5):
    rng = random.Random(seed)
    c = [c0] * N; w = [c0 / a] * N; open_ = [True] * N
    p = 0.30                                 # offer rate per window per tick
    inflow_eps = N * p / 3 * 1.0             # transfers taken at b = eps (E[Y] = 1)
    S_ref = inflow_eps / a                   # the substrate's maintenance, held exactly
    S = S_ref
    b = b_grains * eps
    for t in range(ticks):
        S -= a * S
        n_open = sum(open_)
        if n_open == 0: break
        surplus = max(0.0, S - S_ref)        # cooperative coupling: the surplus returns
        if surplus > 0:
            share = ret * surplus / n_open
            for j in range(N):
                if open_[j]: c[j] += 0.01 * share
            S -= ret * surplus
        sigma = noise0 / math.sqrt(n_open) if loop else 0.0
        for j in range(N):
            if not open_[j]: continue
            w[j] += c[j] * min(1.0, S / S_ref) - a * w[j]
            if rng.random() < p:
                Y = rng.uniform(0.5, 1.5)
                kind = rng.choice(['T', 'C', 'E'])
                if kind == 'T':   X = Y
                elif kind == 'C': X = Y * rng.uniform(1.05, 1.5)
                else:             X = Y * rng.uniform(0.6, 0.999)
                Xr = X * (1 + rng.gauss(0, sigma)) if sigma else X   # the reading
                Yr = Y * (1 + rng.gauss(0, sigma)) if sigma else Y
                if kind == 'T' and b_grains == 0 and not sigma:
                    take = (rng.random() < 0.5) if tie_at_zero == 'coin' else False
                else:
                    take = (1 + b) * Xr > Yr
                if take:
                    if kind == 'T':   w[j] -= Y; S += Y
                    elif kind == 'C': c[j] += 0.01 * (X - Y)
                    else:             c[j] -= 0.05 * Y; S += 0.05 * X
            if c[j] <= 0: open_[j] = False; c[j] = 0.0; w[j] = 0.0
    W = S + sum(w)
    return W, sum(open_), S

def table(loop, seeds=8):
    print("bias (grains)   corridor W   open windows   substrate    "
          + ("with the loop" if loop else "without the loop"))
    for g in [-2, -1, 0, 1, 2, 3, 4, 6, 10, 20]:
        rs = [run(g, seed=s, loop=loop) for s in range(seeds)]
        W = sum(r[0] for r in rs)/seeds; o = sum(r[1] for r in rs)/seeds
        S = sum(r[2] for r in rs)/seeds
        print(f"{g:>13}   {W:10.1f}   {o:12.1f}   {S:9.1f}")

if __name__ == '__main__':
    table(False)
    print()
    table(True)
