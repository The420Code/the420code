#!/usr/bin/env node
// build-i18n.js — Generate 12 language variants of the420code.org
// Run: node build-i18n.js
// Outputs: /es/index.html, /fr/index.html, etc.

const fs = require('fs');
const path = require('path');
const T = require('./translations_shell.js');

const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];
const SOURCE = path.join(__dirname, 'index_en.html');
const OUT_DIR = path.join(__dirname, 'output');

// Font imports for non-Latin scripts
const EXTRA_FONTS = {
  zh: '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">',
  ja: '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">',
  ko: '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">',
  ru: '', // Atkinson Hyperlegible supports Cyrillic
  ar: '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;700&display=swap" rel="stylesheet">',
  hi: '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;700&display=swap" rel="stylesheet">',
};

// Font-family overrides for CJK/Arabic/Devanagari
const FONT_OVERRIDE = {
  zh: "--f:'Noto Sans SC','Atkinson Hyperlegible',sans-serif",
  ja: "--f:'Noto Sans JP','Atkinson Hyperlegible',sans-serif",
  ko: "--f:'Noto Sans KR','Atkinson Hyperlegible',sans-serif",
  ar: "--f:'Noto Sans Arabic','Atkinson Hyperlegible',sans-serif",
  hi: "--f:'Noto Sans Devanagari','Atkinson Hyperlegible',sans-serif",
};

function t(key, lang) {
  if (!T[key]) { console.warn(`Missing key: ${key}`); return T[key]?.en || ''; }
  return T[key][lang] || T[key].en;
}

// Country codes for flag images (flagcdn.com)
const FLAG_CODES = {
  en: 'gb', es: 'es', fr: 'fr', de: 'de', pt: 'br', nl: 'nl',
  it: 'it', zh: 'cn', ja: 'jp', ko: 'kr', ru: 'ru', ar: 'sa', hi: 'in',
};

function flagImg(lang) {
  const cc = FLAG_CODES[lang];
  return `<img src="https://flagcdn.com/w40/${cc}.png" width="20" height="15" alt="${lang}" style="border-radius:2px;vertical-align:middle">`;
}

// Build language selector HTML
function langSelector(currentLang) {
  let html = '<div class="lang-sel" style="display:flex;gap:6px;align-items:center;flex-wrap:wrap">';
  const enActive = currentLang === 'en' ? ' class="active"' : '';
  html += `<a href="/"${enActive} title="English">${flagImg('en')}</a>`;
  LANGS.forEach(l => {
    const isActive = l === currentLang ? ' class="active"' : '';
    html += `<a href="/${l}/"${isActive} title="${t('lang_selector', l)}">${flagImg(l)}</a>`;
  });
  html += '</div>';
  return html;
}

// Build language selector for English root
function langSelectorEN() {
  let html = '<div class="lang-sel" style="display:flex;gap:6px;align-items:center;flex-wrap:wrap">';
  html += `<a href="/" class="active" title="English">${flagImg('en')}</a>`;
  LANGS.forEach(l => {
    html += `<a href="/${l}/" title="${t('lang_selector', l)}">${flagImg(l)}</a>`;
  });
  html += '</div>';
  return html;
}

// Simple string replacer — replaces first occurrence
function rep(html, search, replace) {
  const idx = html.indexOf(search);
  if (idx === -1) {
    // Try with smart quotes converted
    return html;
  }
  return html.substring(0, idx) + replace + html.substring(idx + search.length);
}

// Replace ALL occurrences
function repAll(html, search, replace) {
  return html.split(search).join(replace);
}

function buildLang(sourceHtml, lang) {
  let h = sourceHtml;

  // 1. HTML lang attribute + dir for Arabic
  if (lang === 'ar') {
    h = h.replace('<html lang="en"', '<html lang="ar" dir="rtl"');
  } else {
    h = h.replace(`lang="en"`, `lang="${lang}"`);
  }

  // 2. Page title
  h = rep(h, '<title>the 420 code — ethics derived from physics</title>',
            `<title>${t('page_title', lang)}</title>`);

  // 3. Meta description
  h = rep(h, 'content="Can ethics be derived from physics? The 420 Code says yes. 42 Artist\'s Proofs. Over a million words. One measured input. Zero fitted parameters. Copyleft. Free forever."',
            `content="${t('meta_description', lang)}"`);

  // 4. Add extra font import if needed
  if (EXTRA_FONTS[lang]) {
    h = h.replace('</head>', EXTRA_FONTS[lang] + '\n</head>');
  }

  // 5. Font family override for non-Latin scripts
  if (FONT_OVERRIDE[lang]) {
    h = h.replace("--f:'Atkinson Hyperlegible',sans-serif", FONT_OVERRIDE[lang]);
  }

  // 6. Add RTL CSS adjustments for Arabic
  if (lang === 'ar') {
    const rtlCSS = `<style>
body{direction:rtl;text-align:right}
.nav{flex-direction:row-reverse}
.nav-title{margin-left:auto;margin-right:0}
.ap-header{flex-direction:row-reverse}
.ap-detail{padding-left:0;padding-right:32px}
.spine{padding-left:0;padding-right:32px}
.spine::before{left:auto;right:7px}
.part-dot{left:auto;right:-32px}
.steps li{padding-left:0;padding-right:2rem}
.steps li::before{left:auto;right:0}
.dl-list{padding-left:0;padding-right:32px}
.result-row{flex-direction:row-reverse}
.lang-sel{direction:ltr}
</style>`;
    h = h.replace('</head>', rtlCSS + '\n</head>');
  }

  // 7. Language selector CSS
  const langCSS = `<style>
.lang-sel a{text-decoration:none;opacity:.5;transition:opacity .15s;line-height:1}
.lang-sel a:hover{opacity:1}
.lang-sel a.active{opacity:1}
</style>`;
  h = h.replace('</head>', langCSS + '\n</head>');

  // 8. Nav — add language selector and translate links
  h = rep(h, '<a href="#exhibition">exhibition</a>',
            `<a href="#exhibition">${t('nav_exhibition', lang)}</a>`);
  h = rep(h, '<a href="#proofs">proofs</a>',
            `<a href="#proofs">${t('nav_proofs', lang)}</a>`);

  // Add language selector after proofs link in nav
  h = rep(h, '</nav>',
            langSelector(lang) + '\n</nav>');

  // 9. Hero section
  h = rep(h, '<h1>Can ethics be derived from physics?</h1>',
            `<h1>${t('hero_h1', lang)}</h1>`);
  h = rep(h, 'The 420 Code says <b>yes</b>.',
            t('hero_lead', lang));
  h = rep(h, 'One record exists — and from that single fact, all of physics and one ethic are derived.',
            t('hero_intro', lang));

  // 10. Ten Lines
  h = rep(h, '<li>One record exists.</li>', `<li>${t('line_1', lang)}</li>`);
  h = rep(h, '<li>One record requires four conditions: symmetry, break, record, constraint.</li>', `<li>${t('line_2', lang)}</li>`);
  h = rep(h, '<li>From those four conditions, all physics is derived.</li>', `<li>${t('line_3', lang)}</li>`);
  h = rep(h, '<li>The cracking and the seeing are the same event.</li>', `<li>${t('line_4', lang)}</li>`);
  h = rep(h, '<li>The inside is singular.</li>', `<li>${t('line_5', lang)}</li>`);
  h = rep(h, '<li>Every aware being is a window in one building.</li>', `<li>${t('line_6', lang)}</li>`);
  h = rep(h, '<li>The line between self and other is a tool mistaken for a measurement.</li>', `<li>${t('line_7', lang)}</li>`);
  h = rep(h, '<li>Any ethics derived from an authority external to the structure of reality is manipulable. Manipulable systems collapse into violence.</li>', `<li>${t('line_8', lang)}</li>`);
  h = rep(h, '<li>Kindness is not a commandment. Kindness is a derivation.</li>', `<li>${t('line_9', lang)}</li>`);
  // Line 10 uses smart apostrophe
  h = rep(h, "<li>Don\u2019t be a cunt. Be kind.</li>", `<li>${t('line_10', lang)}</li>`);
  // Also try ASCII apostrophe version
  h = rep(h, "<li>Don't be a cunt. Be kind.</li>", `<li>${t('line_10', lang)}</li>`);

  // 11. Physics section
  h = rep(h, '<h2>The Physics</h2>', `<h2>${t('physics_title', lang)}</h2>`);
  h = rep(h, 'One measured input. Zero fitted parameters. Everything else derived.',
            t('physics_intro', lang));
  // Physics sub (careful — long string)
  h = rep(h, 'The fine-structure constant α ≈ 1/137 is the one number measured from experiment. From that single input and four axioms, the following results are derived — not fitted, not adjusted, not tuned.',
            t('physics_sub', lang));
  // Physics card labels
  h = rep(h, '<div class="p-name">Proton-electron mass ratio</div>',
            `<div class="p-name">${t('phys_proton', lang)}</div>`);
  h = rep(h, '<div class="p-name">Gravitational constant G</div>',
            `<div class="p-name">${t('phys_grav', lang)}</div>`);
  h = rep(h, '<div class="p-name">Neutron-proton mass difference</div>',
            `<div class="p-name">${t('phys_neutron', lang)}</div>`);
  h = rep(h, '<div class="p-name">MOND acceleration a₀</div>',
            `<div class="p-name">${t('phys_mond', lang)}</div>`);
  h = rep(h, '<div class="p-name">Dark sector partition</div>',
            `<div class="p-name">${t('phys_dark', lang)}</div>`);
  h = rep(h, '<strong>Confirm it yourself.</strong>', `<strong>${t('confirm_yourself', lang)}</strong>`);
  h = rep(h, 'Run the code →', t('run_the_code', lang));

  // 12. Exhibition section
  h = rep(h, '>The Exhibition</h2>', `>${t('exhibition_title', lang)}</h2>`);
  h = rep(h, 'One argument. Five doors. Every door opens onto the same room.',
            t('exhibition_p1', lang));
  h = rep(h, 'The 420 Code is not a book. It is an exhibition — over one million words saying one thing in every way it can be said. The argument never changes. The voice does.',
            t('exhibition_p2', lang));
  h = rep(h, 'Five voices run through the entire exhibition. Prose tells the story. Conversation argues it at a bar. Metaphor shows it with coins, gardens, rivers, and buildings. Nursery Rhyme strips it to the bone. Proofs hand you the mathematics and a blade.',
            t('exhibition_p3', lang));
  h = rep(h, 'You do not need to read everything. You need to find the door that opens.',
            t('exhibition_p4', lang));
  // How to read
  h = rep(h, '<b>How to read.</b> Pick a door. If it grips you, go deeper. If it doesn\'t, try another. The argument is the same in all of them. The door that opens is the right door.',
            t('how_to_read', lang));

  // 13. Book titles
  h = rep(h, '<h3 class="cat-title">The Illusion of the Other</h3>',
            `<h3 class="cat-title">${t('illusion_title', lang)}</h3>`);
  h = rep(h, '<h3 class="cat-title">The Rosin</h3>',
            `<h3 class="cat-title">${t('rosin_title', lang)}</h3>`);
  h = rep(h, '<h3 class="cat-title">The Editions</h3>',
            `<h3 class="cat-title">${t('editions_title', lang)}</h3>`);
  h = rep(h, '<h3 class="cat-title">The Notebooks</h3>',
            `<h3 class="cat-title">${t('notebooks_title', lang)}</h3>`);
  h = rep(h, '<h3 class="cat-title">The Records</h3>',
            `<h3 class="cat-title">${t('records_title', lang)}</h3>`);

  // Book descriptions
  h = rep(h, 'You have drawn a line between yourself and every person you have ever met. This book erases it. Ten chapters. No jargon. No equations. No prerequisites. The entire 420 Code was written as support for this one book. If you read one thing, read this.',
            t('illusion_desc', lang));

  // 14. Proofs section
  h = rep(h, '>The Proofs</h2>', `>${t('proofs_title', lang)}</h2>`);
  h = rep(h, '>Artist\'s Proofs</span>', `>${t('stat_aps', lang)}</span>`);
  // Kill switches stat label (appears multiple times, only replace in stats section)
  h = rep(h, '<span class="stat-label">Kill switches</span>',
            `<span class="stat-label">${t('stat_ks', lang)}</span>`);
  h = rep(h, '>Open debts</span>', `>${t('stat_debts', lang)}</span>`);
  h = rep(h, '>Proton mass</span>', `>${t('stat_proton', lang)}</span>`);
  h = rep(h, '>Where to start</p>', `>${t('where_to_start', lang)}</p>`);
  h = rep(h, '>Jump to Part</p>', `>${t('jump_to_part', lang)}</p>`);

  // Reader type cards
  h = rep(h, '>General reader</span>', `>${t('reader_general', lang)}</span>`);
  h = rep(h, '>Physicist</span>', `>${t('reader_physicist', lang)}</span>`);
  h = rep(h, '>Philosopher</span>', `>${t('reader_philosopher', lang)}</span>`);
  h = rep(h, '>AI researcher</span>', `>${t('reader_ai', lang)}</span>`);

  // Jump to Part cards
  h = rep(h, '<span class="entry-card-desc">The Premise</span>', `<span class="entry-card-desc">${t('part_premise', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Spacetime</span>', `<span class="entry-card-desc">${t('part_spacetime', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Quantum Mechanics</span>', `<span class="entry-card-desc">${t('part_qm', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Forces &amp; Constants</span>', `<span class="entry-card-desc">${t('part_forces', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Particles &amp; Matter</span>', `<span class="entry-card-desc">${t('part_particles', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Cosmology</span>', `<span class="entry-card-desc">${t('part_cosmology', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Consciousness &amp; Ethic</span>', `<span class="entry-card-desc">${t('part_consciousness', lang)}</span>`);
  h = rep(h, '<span class="entry-card-desc">Applications</span>', `<span class="entry-card-desc">${t('part_applications', lang)}</span>`);

  // Part headers in spine
  h = rep(h, '<span class="part-name">The Premise</span>', `<span class="part-name">${t('part_premise', lang)}</span>`);
  h = rep(h, '<span class="part-name">Spacetime</span>', `<span class="part-name">${t('part_spacetime', lang)}</span>`);
  h = rep(h, '<span class="part-name">Quantum Mechanics</span>', `<span class="part-name">${t('part_qm', lang)}</span>`);
  h = rep(h, '<span class="part-name">Forces &amp; Constants</span>', `<span class="part-name">${t('part_forces', lang)}</span>`);
  h = rep(h, '<span class="part-name">Particles &amp; Matter</span>', `<span class="part-name">${t('part_particles', lang)}</span>`);
  h = rep(h, '<span class="part-name">Cosmology</span>', `<span class="part-name">${t('part_cosmology', lang)}</span>`);
  h = rep(h, '<span class="part-name">Consciousness &amp; The Ethic</span>', `<span class="part-name">${t('part_consciousness', lang)}</span>`);
  h = rep(h, '<span class="part-name">Applications</span>', `<span class="part-name">${t('part_applications', lang)}</span>`);

  // 15. Headline Results
  h = rep(h, '>Headline Results</h2>', `>${t('headline_title', lang)}</h2>`);
  h = rep(h, '<p>Also derived:</p>', `<p>${t('also_derived', lang)}</p>`);

  // 16. Confirm the Math
  h = rep(h, '>Confirm the Math</h2>', `>${t('confirm_math_title', lang)}</h2>`);

  // 17. Kill Switch Registry
  h = rep(h, '>Kill Switch Registry</h2>', `>${t('ks_title', lang)}</h2>`);
  h = rep(h, 'Every claim carries a stated condition under which it dies. The switches are not hidden. They are published.',
            t('ks_desc', lang));

  // 18. Subscribe
  h = rep(h, '>Stay in the Loop</h2>', `>${t('stay_in_loop', lang)}</h2>`);
  h = rep(h, 'When something new lands, you\'ll know first. Your details will not be added unless you click the confirmation link to be emailed.',
            t('subscribe_desc', lang));
  // Subscribe button
  h = rep(h, '>Subscribe</button>', `>${t('subscribe_btn', lang)}</button>`);
  h = rep(h, 'Check your inbox — a confirmation email is on its way.',
            t('subscribe_success', lang));
  h = rep(h, 'Your subscription could not be saved. Please try again.',
            t('subscribe_error', lang));

  // 19. About + Footer
  h = rep(h, '<b>Artist:</b>', `<b>${t('about_artist', lang)}</b>`);
  h = rep(h, '<b>Duration:</b>', `<b>${t('about_duration', lang)}</b>`);
  h = rep(h, '<b>Exhibition:</b>', `<b>${t('about_exhibition_label', lang)}</b>`);
  h = rep(h, 'over a million words across 23 volumes', t('about_million', lang));
  h = rep(h, 'This work is Copyleft. You are free to download, print, share, and distribute. You are not free to alter the source. Keep the signal clean.',
            t('copyleft_notice', lang));
  h = rep(h, 'downloads</p>', `${t('downloads', lang)}</p>`);

  // Footer ethic line
  h = rep(h, "<p style=\"font-weight:700\">Don\u2019t be a cunt. Be kind.</p>",
            `<p style="font-weight:700">${t('footer_ethic', lang)}</p>`);
  h = rep(h, "<p style=\"font-weight:700\">Don't be a cunt. Be kind.</p>",
            `<p style="font-weight:700">${t('footer_ethic', lang)}</p>`);

  // 20. Toast
  h = repAll(h, '>Publishing Soon</div>', `>${t('publishing_soon', lang)}</div>`);
  h = repAll(h, "'Publishing Soon'", `'${t('publishing_soon', lang)}'`);

  // 21. Fix asset paths — point up one level since we're in /es/, /fr/, etc.
  h = repAll(h, 'src="Eye_of_the_Universe.jpg"', 'src="../Eye_of_the_Universe.jpg"');
  h = repAll(h, 'src="StudioG_Logo_Web.jpg"', 'src="../StudioG_Logo_Web.jpg"');
  h = repAll(h, 'href="Master_Kill_Switch_Registry.pdf"', 'href="../Master_Kill_Switch_Registry.pdf"');
  h = repAll(h, 'href="Illusion_of_the_Other.pdf"', 'href="../Illusion_of_the_Other.pdf"');

  // 21b. Swap localised book PDFs where available
  const BOOK_PDF = {
    es: { file: 'La_Ilusion_del_Otro.pdf', title: 'La Ilusión del Otro' },
    fr: { file: 'L_Illusion_de_l_Autre.pdf', title: "L'Illusion de l'Autre" },
    de: { file: 'Die_Illusion_des_Anderen.pdf', title: 'Die Illusion des Anderen' },
  };
  if (BOOK_PDF[lang]) {
    const b = BOOK_PDF[lang];
    h = rep(h, '../Illusion_of_the_Other.pdf">The Illusion of the Other',
              `../${b.file}">${b.title}`);
  }

  // 22. Fix download counter path
  h = repAll(h, "'/.netlify/functions/download-counter'", "'/../.netlify/functions/download-counter'");

  return h;
}

// Also build an updated English root with the language selector
function buildEnglishRoot(sourceHtml) {
  let h = sourceHtml;
  // Add language selector CSS
  const langCSS = `<style>
.lang-sel a{text-decoration:none;opacity:.5;transition:opacity .15s;line-height:1}
.lang-sel a:hover{opacity:1}
.lang-sel a.active{opacity:1}
</style>`;
  h = h.replace('</head>', langCSS + '\n</head>');

  // Add language selector to nav
  h = rep(h, '</nav>', langSelectorEN() + '\n</nav>');
  return h;
}

// ═══════════════════════════════════════════
// RUN
// ═══════════════════════════════════════════

console.log('Reading source HTML...');
const source = fs.readFileSync(SOURCE, 'utf8');

// Create output directory
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

// Build English root with language selector
console.log('Building EN (root with language selector)...');
const enHtml = buildEnglishRoot(source);
fs.writeFileSync(path.join(OUT_DIR, 'index.html'), enHtml);
console.log('  → output/index.html');

// Build each language
LANGS.forEach(lang => {
  console.log(`Building ${lang.toUpperCase()}...`);
  const langDir = path.join(OUT_DIR, lang);
  if (!fs.existsSync(langDir)) fs.mkdirSync(langDir, { recursive: true });
  const html = buildLang(source, lang);
  fs.writeFileSync(path.join(langDir, 'index.html'), html);
  console.log(`  → output/${lang}/index.html`);
});

console.log(`\nDone. ${LANGS.length + 1} files generated in output/`);
console.log('Next: AP essays (Part by Part) — Phase 2');
