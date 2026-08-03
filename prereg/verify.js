/* The 420 Code — offline in-browser verifier.
 *
 * An INDEPENDENT re-derivation of the three pre-registration scripts
 * (verify_prereg.py, verify_cosmology.py, verify_rigidity.py), written in
 * JavaScript with decimal.js at 60-digit precision. It reproduces every
 * headline number with no Python, no network, no external call — it runs
 * entirely in your browser, offline. The reference Python scripts in this
 * directory agree to every digit; a second, independent implementation that
 * matches is stronger evidence than re-running one file twice.
 *
 * Copyleft 2026. Don't be a cunt. Be kind.
 */
(function (root) {
  var isNode = (typeof module !== 'undefined' && module.exports);
  var D = isNode ? require('./vendor/decimal.min.js') : root.Decimal;
  D.set({ precision: 60 });
  var PI = D.acos(-1);

  function d(x) { return new D(x); }
  function sig(x, n) { return d(x).toSignificantDigits(n).toString(); }

  // ── verify_prereg.py ──────────────────────────────────────────────────────
  function verifyPrereg() {
    var AINV = d('137.035999177'), AINV_U = d('0.000000021');
    var MP_ME = d('1836.152673426'), MP_ME_U = d('0.000000032');
    var ALPHA = d(1).div(AINV);
    var ALPHA_U = ALPHA.times(AINV_U.div(AINV));

    var T0 = d(21 * 21 * 4 + 21 * 3 + 3 * 3);                 // 1836
    var T1 = ALPHA.times(21).times(d(1).minus(d(1).div(PI.times(84))));
    var T2 = ALPHA.pow(2).times(21).times(16).div(1836);
    var Dv = T0.plus(T1).plus(T2);

    var dD = d(21).times(d(1).minus(d(1).div(PI.times(84))))
             .plus(ALPHA.times(2).times(21).times(16).div(1836));
    var D_U = dD.times(ALPHA_U);
    var U = MP_ME_U.pow(2).plus(D_U.pow(2)).sqrt();
    var resid = Dv.minus(MP_ME);
    var ppt = function (x) { return x.div(MP_ME).times('1e12'); };
    var ppb = function (x) { return x.div(MP_ME).times('1e9'); };
    var sigma = resid.div(U);

    // §4a — the alpha^2 coefficient, empirically pinned
    var c2 = MP_ME.minus(T0).minus(T1).div(ALPHA.pow(2));
    var c2u = MP_ME_U.div(ALPHA.pow(2));
    var corpus_c2 = d(21).times(16).div(1836);
    var agree = corpus_c2.minus(c2).abs().div(c2u);
    var impl16 = c2.times(1836).div(21), impl16u = c2u.times(1836).div(21);
    var num = c2.times(1836), numu = c2u.times(1836);
    var lo = Math.floor(num.minus(numu.times(3)).toNumber());
    var hi = Math.ceil(num.plus(numu.times(3)).toNumber());
    var prods = {};
    for (var i = 0; i < 3; i++) for (var j = 0; j < 7; j++) for (var k = 0; k < 6; k++) {
      var v = Math.pow(21, i) * Math.pow(3, j) * Math.pow(4, k);
      if (v <= 500) prods[v] = 1;
    }
    var window = [], hits = [];
    for (var n = lo; n <= hi; n++) { window.push(n); if (prods[n]) hits.push(n); }

    // §5 — the alpha^3 coefficient is unconstrained
    var c3 = resid.neg().div(ALPHA.pow(3)), c3u = U.div(ALPHA.pow(3));

    // §6 — decomposition enumeration
    var dec = decompCounts();

    // §9 — the muon floor
    var floor = 21 * 21 + 21 + 1;

    var out = [];
    out.push('SECTION 4 — the frozen O(alpha^2) value');
    out.push('  21^2*4 + 21*3 + 3^2          = ' + T0.toString());
    out.push('  alpha*21*(1 - 1/(84*pi))     = ' + sig(T1, 15));
    out.push('  alpha^2*21*16/1836           = ' + sig(T2, 15));
    out.push('  D                            = ' + sig(Dv, 16));
    out.push('  D - measured                 = +' + sig(ppt(resid), 4) + ' ppt  (+' + sig(ppb(resid), 4) + ' ppb)');
    out.push('  measurement uncertainty      = ' + sig(ppt(MP_ME_U), 4) + ' ppt');
    out.push('  discrepancy                  = ' + sig(sigma, 3) + ' sigma');
    out.push('  D lies ABOVE measurement -> any alpha^3 term that closes it is NEGATIVE.');
    out.push('');
    out.push('SECTION 4a — the alpha^2 coefficient is empirically pinned');
    out.push('  required by measurement      = ' + sig(c2, 7) + ' +/- ' + sig(c2u, 3) + '  (' + sig(c2u.div(c2).times(100), 3) + ' %)');
    out.push('  corpus 21*16/1836            = ' + sig(corpus_c2, 7));
    out.push('  agreement                    = ' + sig(agree, 3) + ' sigma');
    out.push('  implied owed integer 16      = ' + sig(impl16, 6) + ' +/- ' + sig(impl16u, 3));
    out.push('  numerator over 1836          = ' + sig(num, 7) + ' +/- ' + sig(numu, 3));
    out.push('  integers in 3-sigma window   = [' + window.join(', ') + ']');
    out.push('  ... products of {21,3,4}     = [' + hits.join(', ') + ']   <- 336 = 21x16 = 84x4 = 4^2x21');
    out.push('');
    out.push('SECTION 5 — the order-3 coefficient is unconstrained');
    out.push('  c3 = -(D - measured)/alpha^3 = ' + sig(c3, 4) + ' +/- ' + sig(c3u, 4) + '  (1 sigma)');
    out.push('  1 sigma interval             = [' + sig(c3.minus(c3u), 4) + ', ' + sig(c3.plus(c3u), 4) + ']');
    out.push('  -> no alpha^3 prediction is registered.');
    out.push('');
    out.push('SECTION 6 — decomposition enumeration');
    out.push('  conditions 1+2               : ' + dec.n12 + '   (O Predictions reports 11 -> reproduced)');
    out.push('  conditions 1+2+3             : ' + dec.n123 + '   (O Predictions reports 1 -> NOT reproduced)');
    out.push('  conditions 1+2+3+4           : ' + dec.n1234 + '   (condition 4 formalised 2026-08-02, declared post-hoc)');
    out.push('');
    out.push('SECTION 9 — the muon is below the construction floor');
    out.push('  21^2 + 21 + 1 = ' + floor + '   >   m_mu/m_e = 206.7682827  -> lepton sector not derived.');

    var ok = sig(Dv, 16) === '1836.152673444331' && sig(sigma, 3) === '0.573'
             && hits.length === 1 && hits[0] === 336
             && dec.n12 === 11 && dec.n123 === 2 && dec.n1234 === 1;
    return {
      out: out.join('\n'), ok: ok,
      msg: '✓ Proton freeze reproduced offline — D = 1836.152673444331 at 0.57σ; 336 is the only integer in the 3σ window; decompositions 11 / 2 / 1.'
    };
  }

  function decompCounts() {
    var terms = {};
    for (var a = 0; a < 3; a++) for (var b = 0; b < 8; b++) for (var c = 0; c < 6; c++) {
      var v = Math.pow(21, a) * Math.pow(3, b) * Math.pow(4, c);
      if (v <= 1836 && !(v in terms)) terms[v] = [a, b, c];
    }
    var vals = Object.keys(terms).map(Number).sort(function (x, y) { return x - y; });
    var c12 = [];
    for (var i = 0; i < vals.length; i++) for (var j = i; j < vals.length; j++) for (var k = j; k < vals.length; k++) {
      if (vals[i] + vals[j] + vals[k] === 1836) c12.push([vals[i], vals[j], vals[k]]);
    }
    var e21 = function (x) { return terms[x][0]; };
    var nfac = function (x) { return terms[x][0] + terms[x][1] + terms[x][2]; };
    var order21 = function (t) { return t.slice().sort(function (x, y) { return e21(y) - e21(x); }); };
    var cond3 = function (t) { var o = order21(t); return e21(o[0]) > e21(o[1]) && e21(o[1]) > e21(o[2]); };
    var cond4 = function (t) { var o = order21(t); return nfac(o[0]) >= nfac(o[1]) && nfac(o[1]) >= nfac(o[2]); };
    return {
      n12: c12.length,
      n123: c12.filter(cond3).length,
      n1234: c12.filter(function (t) { return cond3(t) && cond4(t); }).length
    };
  }

  // ── verify_cosmology.py ───────────────────────────────────────────────────
  function verifyCosmology() {
    var C = d(299792458), MPC = d('3.0856775814913673e22'), A0 = d('1.2e-10'), T_H = d('13.797');
    var apex = d(2).times(d(1).div(d('0.5').cos()).plus(d('0.5').tan()).ln());
    var H0 = d(2).times(PI).times(A0).times(MPC).div(apex.times(C).times(1000));

    var comps = [['H0DN 2026', '73.50', '0.81'], ['SH0ES', '73.0', '1.0'],
                 ['TRGB/CCHP', '69.8', '0.8'], ['Planck CMB', '67.4', '0.5']];
    var out = [];
    out.push('KS-45.1 — the Hubble constant from the acceleration floor');
    out.push('  alpha_apex = 2*ln(sec(1/2)+tan(1/2)) = ' + sig(apex, 12));
    out.push('  H0 = 2*pi*a0/(alpha_apex*c)          = ' + sig(H0, 6) + ' km/s/Mpc');
    out.push('  registered: 74.3 +/- 1.2  (the bar is a0’s, not the derivation’s)');
    var sH0DN = null, sPlanck = null;
    for (var i = 0; i < comps.length; i++) {
      var m = d(comps[i][1]), u = d(comps[i][2]);
      var s = d('74.3').minus(m).abs().div(d('1.2').pow(2).plus(u.pow(2)).sqrt());
      if (comps[i][0] === 'H0DN 2026') sH0DN = s;
      if (comps[i][0] === 'Planck CMB') sPlanck = s;
      out.push('    vs ' + comps[i][0] + '  ' + comps[i][1] + ' +/- ' + comps[i][2] + '  ->  ' + sig(s, 3) + ' sigma');
    }
    out.push('  kill: a converged H0 below 71.9 fires KS-45.1');
    out.push('');
    var visPred = d(1).div(21).times(100);
    var mid = d('4.885'), vu = d('0.05');
    var visDev = visPred.div(mid).minus(1).times(100);
    var visSig = visPred.minus(mid).abs().div(vu);
    out.push('KS-41.1 — the visible fraction');
    out.push('  predicted 1/21               = ' + sig(visPred, 6) + ' %   (exact rational)');
    out.push('  observed range 4.86-4.91 %; midpoint 4.885 +/- 0.05');
    out.push('  deviation ' + sig(visDev, 3) + ' %   ->  ' + sig(visSig, 3) + ' sigma');
    out.push('');
    var tau = d(6).div(21).times(T_H);
    var fdm = d(6).div(21).times(d(1).minus(d(21).div(6).neg().exp()));
    var fde = d(1).minus(fdm);
    out.push('KS-42.6 — the dark-sector clock');
    out.push('  tau/t_H = 6/21 = ' + sig(d(6).div(21), 6) + '   -> tau = ' + sig(tau, 4) + ' Gyr at t_H = 13.797 Gyr');
    out.push('  partition: DE ' + sig(fde.times(20).div(21).times(100), 5) + ' %  DM '
             + sig(fdm.times(20).div(21).times(100), 5) + ' %  Vis ' + sig(d(1).div(21).times(100), 5) + ' %');
    out.push('  registered direction: Omega_DM/Omega_b RISES with cosmic time (contradicts LCDM).');

    var ok = sig(H0, 6).indexOf('74.300') === 0 && sig(sH0DN, 3) === '0.553'
             && sig(sPlanck, 3) === '5.31' && sig(visSig, 3) === '2.46' && sig(tau, 4) === '3.942';
    return {
      out: out.join('\n'), ok: ok,
      msg: '✓ Cosmology freezes reproduced offline — H₀ = 74.3 (0.55σ vs H0DN, 5.31σ vs Planck); visible fraction 2.46σ; τ = 3.942 Gyr.'
    };
  }

  // ── verify_rigidity.py ────────────────────────────────────────────────────
  function verifyRigidity() {
    var ALPHA = d(1).div('137.035999177');
    var HBAR = d('1.054571817e-34'), C = d(299792458), M_E = d('9.1093837139e-31');
    var MP_ME = d('1836.152673426'), G_MEAS = d('6.67430e-11'), VIS = d('4.885');
    function massRatio(N) {
      var st = N * N * 4 + N * 3 + 9;
      return d(st).plus(ALPHA.times(N).times(d(1).minus(d(1).div(PI.times(4 * N)))))
                  .plus(ALPHA.pow(2).times(N).times(16).div(st));
    }
    function grav(N) { return ALPHA.pow(N).times(d(1).plus(d(1).div(PI))).times(HBAR).times(C).div(M_E.pow(2)); }

    var rows = [[14, '2 dimensions'], [18, '5 faces'], [20, 'ad hoc'], [21, '6 faces, 3 dims'],
                [22, 'ad hoc'], [24, '7 faces'], [28, '4 dimensions']];
    var out = [];
    out.push('21 = 6 x 3 + 3  (six faces of the break, three spatial dimensions,');
    out.push('                 three actualisation couplings) — fixed before any mass, G or dark value.');
    out.push('');
    out.push(pad('N', 4) + '  ' + pad('origin', 18) + pad('m_p/m_e err', 15) + pad('G err', 14) + pad('vis err', 10));
    out.push('-'.repeat(62));
    var n20ratio = null, n22dG = null;
    for (var r = 0; r < rows.length; r++) {
      var N = rows[r][0];
      var ratio = massRatio(N), Gv = grav(N), v = d(100).div(N);
      var gRatio = Gv.div(G_MEAS);
      var dG = gRatio.minus(1).times(100);
      var gstr;
      if (dG.abs().lt(1e4)) gstr = sig(dG, 4) + '%';
      else if (gRatio.abs().gte(1e5)) gstr = gRatio.toExponential(3) + 'x';
      else gstr = sig(gRatio, 4) + 'x';
      if (N === 20) n20ratio = gRatio;
      if (N === 22) n22dG = dG;
      var mErr = ratio.div(MP_ME).minus(1).times(100);
      var vErr = v.div(VIS).minus(1).times(100);
      var mark = N === 21 ? '  <--' : '';
      out.push(pad(String(N), 4) + '  ' + pad(rows[r][1], 18)
        + pad(sig(mErr, 4) + '%', 15) + pad(gstr, 14) + pad(sig(vErr, 3) + '%', 10) + mark);
    }
    out.push('');
    out.push('N sits in an exponent in G: one step multiplies G by alpha = 1/137.');
    out.push('The mass ratio alone tolerates N=20 or 22 to within 10 %; the exponential in G');
    out.push('closes that window to a single integer. Rigidity is not uniqueness — KS-30.4 stays OPEN.');

    var ok = n20ratio && n22dG
             && n20ratio.minus(138).abs().lt(1)      // N=20 overshoots G by ~138x
             && n22dG.plus(99.27).abs().lt(0.1);     // N=22 undershoots by ~-99.27%
    return {
      out: out.join('\n'), ok: ok,
      msg: '✓ Rigidity table reproduced offline — N=20 overshoots G by 138×, N=22 undershoots by 99.27%.'
    };
  }

  function pad(s, w) { s = String(s); while (s.length < w) s += ' '; return s; }

  var API = { verifyPrereg: verifyPrereg, verifyCosmology: verifyCosmology, verifyRigidity: verifyRigidity };
  if (isNode) module.exports = API; else root.PREREG = API;
})(typeof self !== 'undefined' ? self : this);
