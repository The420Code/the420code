(function () {
  var V = '/.netlify/functions/visit-counter', D = '/.netlify/functions/download-counter';
  function fill(id, url) {
    var el = document.getElementById(id);
    if (!el) return;
    fetch(url).then(function (r) { return r.json(); }).then(function (d) {
      el.textContent = (d.count || 0).toLocaleString();
    }).catch(function () {});
  }
  if (!document.getElementById('visit-counter')) {
    try {
      if (!sessionStorage.getItem('v420')) {
        sessionStorage.setItem('v420', '1');
        fetch(V, {method: 'POST', headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({path: location.pathname, ref: document.referrer})}).catch(function () {});
      }
    } catch (e) {}
  }
  fill('visit-count', V);
  fill('dl-count', D);
})();
