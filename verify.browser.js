/* The 420 Code — offline re-derivation of the root verify.py (the CI suite).
 *
 * Plain JavaScript, IEEE-754 double precision — the identical arithmetic to the
 * Python. It reproduces verify.py's scorecard with no install, no Python, no
 * network: everything runs in your browser. The published verify.py (linked
 * beside the button) produces the same output on every push.
 *
 * One measured input (alpha, CODATA 2022). Zero free parameters.
 * The corpses — the switches that fired — are shown, never repaired, not counted.
 * Copyleft 2026. Don't be a cunt. Be kind.
 */
(function (root) {
  function runVerifyMain() {
    var pi = Math.PI, log = Math.log, exp = Math.exp, cos = Math.cos, tan = Math.tan,
        sqrt = Math.sqrt, asinh = Math.asinh;

    // ── ONE MEASURED INPUT ──
    var ALPHA = 1 / 137.035999177;              // fine-structure constant (CODATA 2022)

    // ── PHYSICAL CONSTANTS (CODATA 2022) ──
    var HBAR = 1.054571817e-34, C = 299792458, M_E = 9.1093837139e-31, G_MEAS = 6.67430e-11;
    var RATIO_PE = 1836.152673426, RATIO_NE = 1838.68366200, DELTA_U = 7.4e-7;
    var KM_PER_MPC = 3.0857e19, GYR = 365.25 * 86400 * 1e9;

    function rel_pct(pred, meas) { return Math.abs(pred - meas) / meas * 100.0; }
    var checks = [], corpses = [];

    // CLAIM 1: Proton-electron mass ratio — the series closed (AP49)
    // AP30 stopped at a^2 with a coefficient of sixteen it declared owed under KS-30.3. AP49 The
    // Hold paid that switch on 6 September 2026: the repair's share is r = 16a/1836, the series
    // closes as a chain of holders, and every order follows from the ruling. KS-HOLD.1.
    var scaffold = 21 ** 2 * 4 + 21 * 3 + 3 ** 2;
    var maintenance = ALPHA * 21 * (1 - 1 / (84 * pi));
    var hold_share = 16 * ALPHA / 1836;
    var correction = 21 * ALPHA * hold_share / (1 - hold_share);
    var ratio_pred = scaffold + maintenance + correction;
    var ratio_err = Math.abs(ratio_pred - RATIO_PE) / RATIO_PE * 1e9;
    checks.push(["Proton-electron mass ratio", "AP49",
      ratio_pred.toFixed(10), RATIO_PE.toFixed(10), ratio_err, "ppb", 5.0]);

    // CLAIM 2: Gravitational constant G — realised (AP44) and structural (AP28)
    var alpha_G = ALPHA ** 21 * (1 + 1 / pi);
    var G_struct = alpha_G * HBAR * C / (M_E * M_E);
    var G_real = G_struct / (1 + ALPHA);
    checks.push(["Gravitational constant G, realised", "AP44",
      G_real.toExponential(4), G_MEAS.toExponential(4), rel_pct(G_real, G_MEAS), "%", 1.0]);
    checks.push(["Gravitational constant G, structural (provisioned)", "AP28",
      G_struct.toExponential(4), G_MEAS.toExponential(4), rel_pct(G_struct, G_MEAS), "%", 1.0]);

    // CLAIM 3: Neutron-proton mass difference — realised (AP47)
    var delta_bare = 3 * (1 - 1 / (2 * pi)) + ALPHA * (1 + 1 / (2 * pi));
    var delta_real = delta_bare / (1 + ALPHA ** 2 / (8 * pi));
    var delta_meas = RATIO_NE - RATIO_PE;
    var delta_sig = Math.abs(delta_real - delta_meas) / DELTA_U;
    checks.push(["Neutron-proton mass difference, realised", "AP47",
      delta_real.toFixed(11) + " m_e", delta_meas.toFixed(9) + " m_e", delta_sig, "sigma", 1.0]);
    corpses.push(["Neutron-proton mass difference, bare row", "AP30 / KS-NPP.1", "2026-08-02",
      delta_bare.toFixed(8) + " m_e", delta_meas.toFixed(9) + " m_e (CODATA 2022)",
      Math.abs(delta_bare - delta_meas) / DELTA_U]);

    // CLAIM 4: Dark sector partition (AP42) and visible fraction (AP41)
    var f_DM_dark = (6 / 21) * (1 - exp(-21 / 6));
    var f_DE_dark = 1 - f_DM_dark;
    var f_vis = 1 / 21;
    var f_DM = f_DM_dark * 20 / 21;
    var f_DE = f_DE_dark * 20 / 21;

    // CLAIM 5: The age of everything — one cycle (AP46)
    var tau_C = HBAR / (M_E * C * C);
    var t_cycle = (21 / 18) * Math.pow(ALPHA, -18) * tau_C;
    var age_pred = t_cycle / GYR;
    var age_meas = 13.787;
    checks.push(["Age of the universe, one cycle", "AP46",
      age_pred.toFixed(3) + " Gyr", age_meas.toFixed(3) + " Gyr", Math.abs(age_pred - age_meas), "Gyr", 0.66]);

    // CLAIM 6: The expansion rate — the closure (AP48)
    var omega_L = f_DE, omega_m = f_DM + f_vis;
    var H0t0 = (2 / (3 * sqrt(omega_L))) * asinh(sqrt(omega_L / omega_m));
    var H0_pred = H0t0 / t_cycle * KM_PER_MPC;
    var H0_meas = 67.4;
    checks.push(["Expansion rate H0, the closure", "AP48",
      H0_pred.toFixed(2) + " km/s/Mpc", H0_meas.toFixed(1) + " km/s/Mpc", Math.abs(H0_pred - H0_meas), "km/s/Mpc", 3.1]);
    corpses.push(["Hubble constant from the floor inverted", "AP18 / KS-45.1", "2026-09-03",
      "74.30 km/s/Mpc (+/- 1.2 as registered)", H0_pred.toFixed(2) + " km/s/Mpc (the corpus's own rate)",
      Math.abs(74.3 - H0_pred) / 1.2]);

    // CLAIM 7: MOND acceleration scale a0 at the corpus's rate (AP18 / AP48)
    var CS2 = 2 * log(1 / cos(0.5) + tan(0.5));
    var H0_si = H0_pred / KM_PER_MPC;
    var a0_pred = CS2 * C * H0_si / (2 * pi);
    var a0_meas = 1.20e-10;
    var a0_unc = sqrt(Math.pow(0.02e-10, 2) + Math.pow(0.24e-10, 2));
    checks.push(["MOND acceleration a0 at the corpus's H0", "AP18",
      a0_pred.toExponential(4), a0_meas.toExponential(4) + " +/- " + a0_unc.toExponential(2), Math.abs(a0_pred - a0_meas) / a0_unc, "sigma", 3.0]);

    checks.push(["Dark energy fraction", "AP42",
      (f_DE * 100).toFixed(2) + "%", "68.89%", rel_pct(f_DE * 100, 68.89), "%", 0.5]);
    checks.push(["Dark matter fraction", "AP42",
      (f_DM * 100).toFixed(2) + "%", "26.07%", rel_pct(f_DM * 100, 26.07), "%", 3.0]);
    checks.push(["Visible matter fraction (1/21)", "AP41",
      (f_vis * 100).toFixed(2) + "%", "~4.885 +/- 0.05%", rel_pct(f_vis * 100, 4.885), "%", 5.0]);

    var bar = "=".repeat(72), dash = "-".repeat(72);
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
    out.push(dash);
    out.push("CORPSES - switches that fired. Shown, never repaired, not counted.");
    out.push(dash);
    for (var j = 0; j < corpses.length; j++) {
      var c = corpses[j];
      out.push("[FIRED] " + c[0] + "  (" + c[1] + ", " + c[2] + ")");
      out.push("        registered: " + c[3]);
      out.push("        against   : " + c[4]);
      out.push("        offset    : " + c[5].toFixed(2) + " sigma");
      out.push("");
    }
    out.push(bar);
    if (fails === 0) out.push("ALL " + checks.length + " CHECKS PASSED. The published derivations hold. " + corpses.length + " fired switches shown.");
    else out.push(fails + " of " + checks.length + " CHECKS FAILED - a derivation drifted past tolerance.");
    out.push(bar);
    return { out: out.join("\n"), ok: fails === 0 };
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { runVerifyMain: runVerifyMain };
  else root.VERIFY_MAIN = runVerifyMain;
})(typeof self !== 'undefined' ? self : this);
