#!/usr/bin/env python3
"""
The sealed-envelope machinery for PROTOCOL-lattice-qcd-mapping.md.

The protocol reserves Step 1 — the derivation of the mapping — to the author, alone, from
the axioms, and forbids any assistant that has seen lattice numbers from helping with it
(§1, §5). This script does not touch Step 1. It does everything around it, so that when the
derivation exists, sealing it is mechanical and cannot be fumbled.

    python seal_lattice_freeze.py --new         write the Step 2/3 template to fill in
    python seal_lattice_freeze.py --check FILE  refuse the seal if the file is not ready
    python seal_lattice_freeze.py --seal  FILE  digest it, write the receipt, print the
                                                git commands that make the timestamp public

The seal is refused if the document contains any lattice number, if any Step 2 field is
still blank, or if the kill condition is missing — the three ways a freeze dies at birth.

Copyleft 2026. Don't be a cunt. Be kind.
"""
import argparse, hashlib, os, re, sys, io, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

TEMPLATE = """# Freeze: the lattice-QCD mapping — {date}

**Freeze date:** {date}
**Author:** G · Studio G · the420code.org
**Protocol:** `PROTOCOL-lattice-qcd-mapping.md`, Steps 1–4
**Status:** frozen for commit. The commit hash is the timestamp.
**Contains no lattice numbers. That is the point.**

---

## 1. The derivation

<!-- Step 1. From {{S, B, R, C}}, AP19's three-face geometry, AP24's six faces and AP30's
     three layers, derive what the layers map onto. Exhibit the derivation; do not assert
     it. If it does not close, stop and take route (c) — withdraw the promise from
     Ø Predictions and say why. Route (c) is a legitimate outcome, not a failure. -->

## 2. The route taken

<!-- (a) a different observable — the lattice-computable quantity that geometric
         resistance corresponds to; the strongest route and the hardest
     (b) a ratio between lattice components rather than absolute shares
     (c) retraction
     Name one. -->

ROUTE:

## 3. The target, specified completely

Every field must be filled. Each blank left here is a knob that could be turned afterwards,
and one blank voids the freeze.

| Field | Value |
|---|---|
| lattice observable | |
| renormalisation scheme | |
| scale μ (in GeV) | |
| quark-flavour content (2, 2+1, 2+1+1) | |
| physical pion mass or extrapolated | |
| what counts as agreement (tolerance) | |
| σ threshold | |

## 4. The predicted value

<!-- The number your derivation produces, stated to the precision you are claiming.
     Not a range chosen to be safe. -->

PREDICTED:

## 5. The kill condition

<!-- One sentence, the registry's form: this claim dies if X. -->

DIES IF:

## 6. Provenance

<!-- What was fixed before this document, and where it can be checked. -->

---

*Frozen files are never edited; corrections supersede, dated, in the open.*
*Copyleft 2026. Don't be a cunt. Be kind.*
"""

FIELDS = ["lattice observable", "renormalisation scheme", "scale μ (in GeV)",
          "quark-flavour content (2, 2+1, 2+1+1)", "physical pion mass or extrapolated",
          "what counts as agreement (tolerance)", "σ threshold"]

# words that betray a look at the numbers before the seal
CONTAMINANTS = [r"\bMeV\b", r"\bGeV\b(?!\s*\)\s*\|)", r"\blattice (?:says|gives|finds)\b",
                r"\bwe (?:find|found|see)\b", r"\bagrees? with\b", r"\bpublished value\b"]

def strip_comments(t):
    return re.sub(r"<!--.*?-->", "", t, flags=re.S)

def check(path):
    t = open(path, encoding="utf-8").read()
    body = strip_comments(t)
    problems, notes = [], []

    for f in FIELDS:
        m = re.search(r"\|\s*" + re.escape(f) + r"\s*\|(.*?)\|", body)
        if not m: problems.append(f"Step 3 field missing entirely: {f}")
        elif not m.group(1).strip(): problems.append(f"Step 3 field left blank: {f}")
    for label, pat in (("ROUTE", r"ROUTE:\s*(\S.*)"), ("PREDICTED", r"PREDICTED:\s*(\S.*)"),
                       ("DIES IF", r"DIES IF:\s*(\S.*)")):
        if not re.search(pat, body): problems.append(f"{label} is empty — the freeze is void without it")

    sec1 = body.split("## 2.")[0]
    if len(re.sub(r"[#*\s|-]", "", sec1)) < 400:
        problems.append("Step 1 (the derivation) is thin — exhibit it, do not assert it")

    for pat in CONTAMINANTS:
        for m in re.finditer(pat, body, re.I):
            line = body[:m.start()].count("\n") + 1
            notes.append(f"line {line}: {m.group(0)!r} — a lattice number may have been seen")
    if re.search(r"\d+\s*(?:MeV|GeV)\b", body):
        problems.append("a lattice-scale energy appears in the document — a sealed freeze carries none")

    return problems, notes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new", action="store_true")
    ap.add_argument("--check", metavar="FILE")
    ap.add_argument("--seal", metavar="FILE")
    a = ap.parse_args()
    today = datetime.date.today().isoformat()

    if a.new:
        out = f"FREEZE-{today}-lattice-mapping.md"
        if os.path.exists(out): print(f"{out} already exists — not overwritten."); return 1
        open(out, "w", encoding="utf-8", newline="\n").write(TEMPLATE.format(date=today))
        print(f"wrote {out}")
        print("Fill Steps 1–6. Do not look at any lattice number until it is sealed and committed.")
        print(f"Then: python seal_lattice_freeze.py --seal {out}")
        return 0

    path = a.check or a.seal
    if not path: ap.print_help(); return 1
    problems, notes = check(path)

    print("=" * 72); print(f"SEAL CHECK — {path}"); print("=" * 72)
    for n in notes: print(f"  [look] {n}")
    if problems:
        print(f"\n  NOT READY. {len(problems)} problem(s):")
        for pr in problems: print(f"    - {pr}")
        print("\n  The seal is refused. Each of these is a way the freeze dies on contact.")
        return 1
    print("  every Step 3 field filled · route named · prediction stated · kill condition stated")
    print("  no lattice number present")
    if not a.seal:
        print("\n  READY TO SEAL."); return 0

    data = open(path, "rb").read()
    digest = hashlib.sha256(data).hexdigest()
    receipt = f"{path}.sha256"
    open(receipt, "w", encoding="utf-8", newline="\n").write(f"{digest}  {os.path.basename(path)}\n")
    print(f"\n  SHA-256  {digest}")
    print(f"  receipt  {receipt}")
    print("\n  Now make the timestamp public — this is the moment the prediction becomes blind")
    print("  in a way a stranger can verify:\n")
    print(f"    git add {path} {receipt}")
    print(f'    git commit -m "freeze: the lattice mapping, sealed before the numbers ({today})"')
    print(f"    git tag lattice-freeze-{today}")
    print("    git push origin main --tags\n")
    print("  Record the commit hash beside the digest. Only then open Step 5, and not in the")
    print("  same session that wrote Step 1.")
    print("=" * 72)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
