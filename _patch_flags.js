const fs = require('fs');
const path = require('path');

const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

const FLAG_CODES = {
  en:'gb',es:'es',fr:'fr',de:'de',pt:'br',nl:'nl',
  it:'it',zh:'cn',ja:'jp',ko:'kr',ru:'ru',ar:'sa',hi:'in'
};

const LANG_LABELS = {
  en:'EN',es:'ES',fr:'FR',de:'DE',pt:'PT',nl:'NL',
  it:'IT',zh:'中文',ja:'日本語',ko:'한국어',ru:'РУ',ar:'عربي',hi:'हिंदी'
};

function flagImg(lang) {
  const cc = FLAG_CODES[lang];
  return '<img src="https://flagcdn.com/w40/' + cc + '.png" width="20" height="15" alt="' + lang + '" style="border-radius:2px;vertical-align:middle">';
}

function buildSelector(currentLang) {
  let html = '<div class="lang-sel" style="display:flex;gap:6px;align-items:center;flex-wrap:wrap">';
  const enActive = currentLang === 'en' ? ' class="active"' : '';
  html += '<a href="/"' + enActive + ' title="English">' + flagImg('en') + '</a>';
  LANGS.forEach(l => {
    const active = l === currentLang ? ' class="active"' : '';
    html += '<a href="/' + l + '/"' + active + ' title="' + LANG_LABELS[l] + '">' + flagImg(l) + '</a>';
  });
  html += '</div>';
  return html;
}

LANGS.forEach(lang => {
  const fp = path.join('.', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');

  // Replace text-based CSS with flag CSS
  h = h.replace(
    /\.lang-sel a\{font-size:12px[^}]+\}\n\.lang-sel a:hover\{[^}]+\}/g,
    '.lang-sel a{text-decoration:none;opacity:.5;transition:opacity .15s;line-height:1}\n.lang-sel a:hover{opacity:1}\n.lang-sel a.active{opacity:1}'
  );

  // Replace text-based selector with flag version
  h = h.replace(/<div class="lang-sel"[^>]*>.*?<\/div>/g, buildSelector(lang));

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — flags applied');
});
console.log('Done');
