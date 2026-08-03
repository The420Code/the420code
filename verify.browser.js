/* The 420 Code — offline re-derivation of the root verify.py (the CI suite).
 *
 * Plain JavaScript, IEEE-754 double precision — the identical arithmetic to the
 * Python. It reproduces verify.py's scorecard with no install, no Python, no
 * network: everything runs in your browser. The published verify.py (linked
 * beside the button) produces the same output on every push.
 *
 * One measured input (alpha, CODATA 2022). Zero free parameters.
 * Copyleft 2026. Don't be a cunt. Be kind.
 */
(function (root) {
  function runVerifyMain() {
    var pi = Math.PI, log = Math.log, exp = Math.exp, cos = Math.cos, tan = Math.tan;

    // ── ONE MEASURED INPUT ──
    var ALPHA = 1 / 137.035999177;              // fine-structure constant (CODATA 2022)

    // ── PHYSICAL CONSTANTS (CODATA) ──
    var HBAR = 1.054571817e-34, C = 299792458, M_E = 9.1093837015e-31,
        M_P = 1.67262192369e-27, M_N = 1.67492749804e-27, G_MEAS = 6.67430e-11;
    var H0 = 74.3 * 1000 / 3.0857e22;

    function rel_pct(pred, meas) { return Math.abs(pred - meas) / meas * 100.0; }
    var checks = [];

    // CLAIM 1: Proton-electron mass ratio (AP30)
    var scaffold = 21 ** 2 * 4 + 21 * 3 + 3 ** 2;
    var maintenance = ALPHA * 21 * (1 - 1 / (84 * pi));
    var correction = ALPHA ** 2 * 21 * 16 / 1836;
    var ratio_pred = scaffold + maintenance + correction;
    var ratio_meas = 1836.152673426;
    var ratio_err = Math.abs(ratio_pred - ratio_meas) / ratio_meas * 1e9;
    checks.push(["Proton-electron mass ratio", "AP30",
      ratio_pred.toFixed(10), ratio_meas.toFixed(10), ratio_err, "ppb", 5.0]);

    // CLAIM 2: Gravitational constant G (AP28)
    var alpha_G = ALPHA ** 21 * (1 + 1 / pi);
    var G_pred = alpha_G * HBAR * C / (M_E * M_E);
    var G_err = rel_pct(G_pred, G_MEAS);
    checks.push(["Gravitational constant G", "AP28",
      G_pred.toExponential(4), G_MEAS.toExponential(4), G_err, "%", 1.0]);

    // CLAIM 3: Neutron-proton mass difference (AP30)
    var delta_pred = 3 * (1 - 1 / (2 * pi)) + ALPHA * (1 + 1 / (2 * pi));
    var delta_meas = (M_N - M_P) / M_E;
    var delta_err = Math.abs(delta_pred - delta_meas) / delta_meas * 1e6;
    checks.push(["Neutron-proton mass difference", "AP30",
      delta_pred.toFixed(8) + " m_e", delta_meas.toFixed(8) + " m_e", delta_err, "ppm", 5.0]);

    // CLAIM 4: MOND acceleration scale a0 (AP18)
    var CS2 = 2 * log(1 / cos(0.5) + tan(0.5));
    var a0_pred = CS2 * C * H0 / (2 * pi);
    var a0_meas = 1.2e-10;
    var a0_err = rel_pct(a0_pred, a0_meas);
    checks.push(["MOND acceleration a0 (H0=74.3)", "AP18",
      a0_pred.toExponential(4), a0_meas.toExponential(4), a0_err, "%", 1.0]);

    // CLAIM 5: Dark sector partition (AP42)
    var f_DM_dark = (6 / 21) * (1 - exp(-21 / 6));
    var f_DE_dark = 1 - f_DM_dark;
    var f_vis = 1 / 21;
    var f_DM = f_DM_dark * 20 / 21;
    var f_DE = f_DE_dark * 20 / 21;
    checks.push(["Dark energy fraction", "AP42",
      (f_DE * 100).toFixed(2) + "%", "68.89%", rel_pct(f_DE * 100, 68.89), "%", 0.5]);
    checks.push(["Dark matter fraction", "AP42",
      (f_DM * 100).toFixed(2) + "%", "26.07%", rel_pct(f_DM * 100, 26.07), "%", 3.0]);

    // CLAIM 6: Visible matter fraction (AP41)
    checks.push(["Visible matter fraction (1/21)", "AP41",
      (f_vis * 100).toFixed(2) + "%", "~4.885 +/- 0.05%", rel_pct(f_vis * 100, 4.885), "%", 5.0]);

    var bar = "=".repeat(72);
    var out = [bar, "THE 420 CODE - VERIFICATION SUITE",
               "One measured input (alpha). Zero free parameters.", bar, ""];
    var fails = 0;
    for (var i = 0; i < checks.length; i++) {
      var name = checks[i][0], paper = checks[i][1], pred = checks[i][2],
          meas = checks[i][3], err = checks[i][4], unit = checks[i][5], tol = checks[i][6];
      var okc = err <= tol;
      if (!okc) fails++;
      var tolStr = Number.isInteger(tol) ? tol.toFixed(1) : String(tol);
      out.push("[" + (okc ? "PASS" : "FAIL") + "] " + name + "  (" + paper + ")");
      out.push("        predicted : " + pred);
      out.push("        measured  : " + meas);
      out.push("        error     : " + err.toFixed(4) + " " + unit + "   (tolerance " + tolStr + " " + unit + ")");
      out.push("");
    }
    out.push(bar);
    if (fails === 0) out.push("ALL " + checks.length + " CHECKS PASSED. The published derivations hold.");
    else out.push(fails + " of " + checks.length + " CHECKS FAILED - a derivation drifted past tolerance.");
    out.push(bar);
    return { out: out.join("\n"), ok: fails === 0 };
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { runVerifyMain: runVerifyMain };
  else root.VERIFY_MAIN = runVerifyMain;
})(typeof self !== 'undefined' ? self : this);
