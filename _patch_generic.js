// Generic AP translation patcher
// Usage: node _patch_generic.js <translation_file> <AP_number> <requires_string>
// Example: node _patch_generic.js ap12_translations.js AP12 "Requires: AP09, AP11, AP20"

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 3) {
  console.log('Usage: node _patch_generic.js <translation_file> <AP_number> <requires_string>');
  process.exit(1);
}

const translationFile = args[0];
const apNumber = args[1];
const requiresStr = args[2];

// Load translations
const src = fs.readFileSync(translationFile, 'utf8');
// Extract the array by evaluating the const declaration
const match = src.match(/const \w+ = (\[[\s\S]*\]);/);
if (!match) { console.error('Could not parse translation array'); process.exit(1); }
const translations = eval(match[1]);

const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

function buildEssayHTML(lang, data) {
  let lines = [];
  for (const entry of data) {
    const text = entry[lang];
    if (!text) continue;
    if (entry.type === 'subtitle') continue;
    if (entry.type === 'p') lines.push('<p>' + text + '</p>');
    if (entry.type === 'ks') lines.push('<div class="ks">' + text + '</div>');
    if (entry.type === 'breath') lines.push('<p class="breath">' + text + '</p>');
  }
  return lines.join('\n');
}

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');

  const startMarker = '<div class="ap-header"><span class="ap-number">' + apNumber + '</span>';
  const startIdx = h.indexOf(startMarker);
  if (startIdx === -1) {
    console.log('  ' + lang + ' — ' + apNumber + ' NOT FOUND, skipping');
    return;
  }

  // Replace subtitle
  const subtitle = translations[0][lang];
  const subtitleEn = translations[0].en;
  const detailTag = '<div class="ap-detail"><p>';
  const detailStart = h.indexOf(detailTag, startIdx);
  const contentOffset = detailStart + detailTag.length;
  const detailPEnd = h.indexOf('</p>', contentOffset);
  h = h.substring(0, contentOffset) + subtitle + h.substring(detailPEnd);

  // Find essay body boundaries
  const essayTag = '<div class="ap-essay">';
  const essayStart = h.indexOf(essayTag, h.indexOf(startMarker));
  const contentStart = h.indexOf('\n', essayStart);
  const metaMarker = '</div><div class="ap-meta"><span>' + requiresStr + '</span>';
  const contentEnd = h.indexOf(metaMarker, contentStart);

  if (contentStart === -1 || contentEnd === -1) {
    console.log('  ' + lang + ' — ' + apNumber + ' could not find essay boundaries, skipping');
    return;
  }

  const essayHTML = buildEssayHTML(lang, translations);
  h = h.substring(0, contentStart + 1) + essayHTML + '\n' + h.substring(contentEnd);

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + apNumber + ' translated');
});

console.log('Done — ' + apNumber);
