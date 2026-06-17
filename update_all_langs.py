#!/usr/bin/env python3
"""Apply all 6 changes to 12 non-English language versions."""
import shutil
from pathlib import Path

root = Path(r'C:\Users\info\the420code')

LANGS = {
    'es': {
        'physics_old': 'La Física', 'physics_new': 'Ø Física',
        'doors_old': 'Las Cinco Puertas', 'doors_new': 'Ø Cinco Puertas',
        'exhibition_old': 'La Exposición', 'exhibition_new': 'Ø Exposición',
        'proofs_old': 'Las Pruebas', 'proofs_new': 'Ø Pruebas',
        'records_old': 'Los Registros', 'records_new': 'Ø Registros',
        'axiom_title': '1 Axioma',
        'models_title': 'Ø Modelos',
        'hero_old': 'Un registro existe — y de ese único hecho, toda la física y una ética son derivadas.',
        'hero_new': 'Un registro existe. Intentar negarlo produce otro registro, lo que demuestra que al menos un registro existe. De ese único hecho auto-instanciante, toda la física y una ética son derivadas.',
    },
    'fr': {
        'physics_old': 'La Physique', 'physics_new': 'Ø Physique',
        'doors_old': 'Les Cinq Portes', 'doors_new': 'Ø Cinq Portes',
        'exhibition_old': "L'Exposition", 'exhibition_new': 'Ø Exposition',
        'proofs_old': 'Les Preuves', 'proofs_new': 'Ø Preuves',
        'records_old': 'Les Archives', 'records_new': 'Ø Archives',
        'axiom_title': '1 Axiome',
        'models_title': 'Ø Modèles',
        'hero_old': "Un enregistrement existe \u2014 et de ce seul fait, toute la physique et une \u00e9thique en sont d\u00e9riv\u00e9es.",
        'hero_new': "Un enregistrement existe. Tenter de le nier produit un autre enregistrement, ce qui prouve qu'au moins un enregistrement existe. De ce seul fait auto-instanciant, toute la physique et une \u00e9thique en sont d\u00e9riv\u00e9es.",
    },
    'de': {
        'physics_old': 'Die Physik', 'physics_new': 'Ø Physik',
        'doors_old': 'Die F\u00fcnf T\u00fcren', 'doors_new': 'Ø F\u00fcnf T\u00fcren',
        'exhibition_old': 'Die Ausstellung', 'exhibition_new': 'Ø Ausstellung',
        'proofs_old': 'Die Beweise', 'proofs_new': 'Ø Beweise',
        'records_old': 'Die Aufzeichnungen', 'records_new': 'Ø Aufzeichnungen',
        'axiom_title': '1 Axiom',
        'models_title': 'Ø Modelle',
        'hero_old': '', 'hero_new': '',
    },
    'pt': {
        'physics_old': 'A F\u00edsica', 'physics_new': 'Ø F\u00edsica',
        'doors_old': 'As Cinco Portas', 'doors_new': 'Ø Cinco Portas',
        'exhibition_old': 'A Exposi\u00e7\u00e3o', 'exhibition_new': 'Ø Exposi\u00e7\u00e3o',
        'proofs_old': 'As Provas', 'proofs_new': 'Ø Provas',
        'records_old': 'Os Registros', 'records_new': 'Ø Registos',
        'axiom_title': '1 Axioma',
        'models_title': 'Ø Modelos',
        'hero_old': 'Um registro existe \u2014 e desse \u00fanico fato, toda a f\u00edsica e uma \u00e9tica s\u00e3o derivadas.',
        'hero_new': 'Um registro existe. Tent\u00e1-lo negar produz outro registro, o que prova que pelo menos um registro existe. Desse \u00fanico fato auto-instanciante, toda a f\u00edsica e uma \u00e9tica s\u00e3o derivadas.',
    },
    'nl': {
        'physics_old': 'De Fysica', 'physics_new': 'Ø Fysica',
        'doors_old': 'De Vijf Deuren', 'doors_new': 'Ø Vijf Deuren',
        'exhibition_old': 'De Tentoonstelling', 'exhibition_new': 'Ø Tentoonstelling',
        'proofs_old': 'De Bewijzen', 'proofs_new': 'Ø Bewijzen',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 Axioma',
        'models_title': 'Ø Modellen',
        'hero_old': '', 'hero_new': '',
    },
    'it': {
        'physics_old': 'La Fisica', 'physics_new': 'Ø Fisica',
        'doors_old': 'Le Cinque Porte', 'doors_new': 'Ø Cinque Porte',
        'exhibition_old': "L'Esposizione", 'exhibition_new': 'Ø Esposizione',
        'proofs_old': 'Le Prove', 'proofs_new': 'Ø Prove',
        'records_old': 'I Registri', 'records_new': 'Ø Registri',
        'axiom_title': '1 Assioma',
        'models_title': 'Ø Modelli',
        'hero_old': '', 'hero_new': '',
    },
    'zh': {
        'physics_old': '\u7269\u7406\u5b66', 'physics_new': '\u00d8 \u7269\u7406\u5b66',
        'doors_old': '\u4e94\u6247\u95e8', 'doors_new': '\u00d8 \u4e94\u6247\u95e8',
        'exhibition_old': '\u5c55\u89c8', 'exhibition_new': '\u00d8 \u5c55\u89c8',
        'proofs_old': '\u8bc1\u660e', 'proofs_new': '\u00d8 \u8bc1\u660e',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \u516c\u7406',
        'models_title': '\u00d8 \u6a21\u578b',
        'hero_old': '', 'hero_new': '',
    },
    'ja': {
        'physics_old': '\u7269\u7406\u5b66', 'physics_new': '\u00d8 \u7269\u7406\u5b66',
        'doors_old': '', 'doors_new': '',
        'exhibition_old': '\u5c55\u793a', 'exhibition_new': '\u00d8 \u5c55\u793a',
        'proofs_old': '\u8a3c\u660e', 'proofs_new': '\u00d8 \u8a3c\u660e',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \u516c\u7406',
        'models_title': '\u00d8 \u30e2\u30c7\u30eb',
        'hero_old': '\u4e00\u3064\u306e\u8a18\u9332\u304c\u5b58\u5728\u3059\u308b\u2014\u2014\u305d\u306e\u4e00\u3064\u306e\u4e8b\u5b9f\u304b\u3089\u3001\u3059\u3079\u3066\u306e\u7269\u7406\u5b66\u3068\u4e00\u3064\u306e\u502b\u7406\u304c\u5c0e\u304b\u308c\u308b\u3002',
        'hero_new': '\u4e00\u3064\u306e\u8a18\u9332\u304c\u5b58\u5728\u3059\u308b\u3002\u305d\u308c\u3092\u5426\u5b9a\u3057\u3088\u3046\u3068\u3059\u308b\u3068\u3001\u3082\u3046\u4e00\u3064\u306e\u8a18\u9332\u304c\u751f\u307e\u308c\u3001\u5c11\u306a\u304f\u3068\u3082\u4e00\u3064\u306e\u8a18\u9332\u304c\u5b58\u5728\u3059\u308b\u3053\u3068\u304c\u8a3c\u660e\u3055\u308c\u308b\u3002\u305d\u306e\u81ea\u5df1\u5b9f\u73fe\u7684\u306a\u4e8b\u5b9f\u304b\u3089\u3001\u3059\u3079\u3066\u306e\u7269\u7406\u5b66\u3068\u4e00\u3064\u306e\u502b\u7406\u304c\u5c0e\u304b\u308c\u308b\u3002',
    },
    'ko': {
        'physics_old': '\ubb3c\ub9ac\ud559', 'physics_new': '\u00d8 \ubb3c\ub9ac\ud559',
        'doors_old': '\ub2e4\uc12f \uac1c\uc758 \ubb38', 'doors_new': '\u00d8 \ub2e4\uc12f \uac1c\uc758 \ubb38',
        'exhibition_old': '\uc804\uc2dc', 'exhibition_new': '\u00d8 \uc804\uc2dc',
        'proofs_old': '\uc99d\uba85', 'proofs_new': '\u00d8 \uc99d\uba85',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \uacf5\ub9ac',
        'models_title': '\u00d8 \ubaa8\ub378',
        'hero_old': '\ud558\ub098\uc758 \uae30\ub85d\uc774 \uc874\uc7ac\ud55c\ub2e4 \u2014 \uadf8 \ud558\ub098\uc758 \uc0ac\uc2e4\ub85c\ubd80\ud130 \ubaa8\ub4e0 \ubb3c\ub9ac\ud559\uacfc \ud558\ub098\uc758 \uc724\ub9ac\uac00 \ub3c4\ucd9c\ub41c\ub2e4.',
        'hero_new': '\ud558\ub098\uc758 \uae30\ub85d\uc774 \uc874\uc7ac\ud55c\ub2e4. \uc774\ub97c \ubd80\uc815\ud558\ub824 \ud558\uba74 \ub610 \ub2e4\ub978 \uae30\ub85d\uc774 \uc0dd\uae30\uba70, \uc801\uc5b4\ub3c4 \ud558\ub098\uc758 \uae30\ub85d\uc774 \uc874\uc7ac\ud568\uc744 \uc99d\uba85\ud55c\ub2e4. \uadf8 \uc790\uae30 \uc2e4\ud604\uc801 \uc0ac\uc2e4\ub85c\ubd80\ud130 \ubaa8\ub4e0 \ubb3c\ub9ac\ud559\uacfc \ud558\ub098\uc758 \uc724\ub9ac\uac00 \ub3c4\ucd9c\ub41c\ub2e4.',
    },
    'ru': {
        'physics_old': '\u0424\u0438\u0437\u0438\u043a\u0430', 'physics_new': '\u00d8 \u0424\u0438\u0437\u0438\u043a\u0430',
        'doors_old': '\u041f\u044f\u0442\u044c \u0434\u0432\u0435\u0440\u0435\u0439', 'doors_new': '\u00d8 \u041f\u044f\u0442\u044c \u0434\u0432\u0435\u0440\u0435\u0439',
        'exhibition_old': '\u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0430', 'exhibition_new': '\u00d8 \u0412\u044b\u0441\u0442\u0430\u0432\u043a\u0430',
        'proofs_old': '\u0414\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430', 'proofs_new': '\u00d8 \u0414\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \u0410\u043a\u0441\u0438\u043e\u043c\u0430',
        'models_title': '\u00d8 \u041c\u043e\u0434\u0435\u043b\u0438',
        'hero_old': '\u041e\u0434\u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442 \u2014 \u0438 \u0438\u0437 \u044d\u0442\u043e\u0433\u043e \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0444\u0430\u043a\u0442\u0430 \u0432\u044b\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u0432\u0441\u044f \u0444\u0438\u0437\u0438\u043a\u0430 \u0438 \u043e\u0434\u043d\u0430 \u044d\u0442\u0438\u043a\u0430.',
        'hero_new': '\u041e\u0434\u043d\u0430 \u0437\u0430\u043f\u0438\u0441\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442. \u041f\u043e\u043f\u044b\u0442\u043a\u0430 \u043e\u0442\u0440\u0438\u0446\u0430\u0442\u044c \u044d\u0442\u043e \u043f\u043e\u0440\u043e\u0436\u0434\u0430\u0435\u0442 \u0435\u0449\u0451 \u043e\u0434\u043d\u0443 \u0437\u0430\u043f\u0438\u0441\u044c, \u0447\u0442\u043e \u0434\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e\u0432\u0430\u043d\u0438\u0435 \u0445\u043e\u0442\u044f \u0431\u044b \u043e\u0434\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438. \u0418\u0437 \u044d\u0442\u043e\u0433\u043e \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u0430\u043c\u043e\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e\u0449\u0435\u0433\u043e\u0441\u044f \u0444\u0430\u043a\u0442\u0430 \u0432\u044b\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u0432\u0441\u044f \u0444\u0438\u0437\u0438\u043a\u0430 \u0438 \u043e\u0434\u043d\u0430 \u044d\u0442\u0438\u043a\u0430.',
    },
    'ar': {
        'physics_old': '\u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621', 'physics_new': '\u00d8 \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621',
        'doors_old': '\u0627\u0644\u0623\u0628\u0648\u0627\u0628 \u0627\u0644\u062e\u0645\u0633\u0629', 'doors_new': '\u00d8 \u0627\u0644\u0623\u0628\u0648\u0627\u0628 \u0627\u0644\u062e\u0645\u0633\u0629',
        'exhibition_old': '\u0627\u0644\u0645\u0639\u0631\u0636', 'exhibition_new': '\u00d8 \u0627\u0644\u0645\u0639\u0631\u0636',
        'proofs_old': '\u0627\u0644\u0628\u0631\u0627\u0647\u064a\u0646', 'proofs_new': '\u00d8 \u0627\u0644\u0628\u0631\u0627\u0647\u064a\u0646',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \u0627\u0644\u0628\u062f\u064a\u0647\u064a\u0629',
        'models_title': '\u00d8 \u0627\u0644\u0646\u0645\u0627\u0630\u062c',
        'hero_old': '', 'hero_new': '',
    },
    'hi': {
        'physics_old': '\u092d\u094c\u0924\u093f\u0915\u0940', 'physics_new': '\u00d8 \u092d\u094c\u0924\u093f\u0915\u0940',
        'doors_old': '', 'doors_new': '',
        'exhibition_old': '\u092a\u094d\u0930\u0926\u0930\u094d\u0936\u0928\u0940', 'exhibition_new': '\u00d8 \u092a\u094d\u0930\u0926\u0930\u094d\u0936\u0928\u0940',
        'proofs_old': '\u092a\u094d\u0930\u092e\u093e\u0923', 'proofs_new': '\u00d8 \u092a\u094d\u0930\u092e\u093e\u0923',
        'records_old': '', 'records_new': '',
        'axiom_title': '1 \u0938\u094d\u0935\u092f\u0902\u0938\u093f\u0926\u094d\u0927',
        'models_title': '\u00d8 \u092e\u0949\u0921\u0932',
        'hero_old': '', 'hero_new': '',
    },
}

# The 1 Axiom section HTML (English — used as-is for languages without translation)
AXIOM_SECTION_EN = '''<!-- ════════════════════════════════════════ -->
<!-- 1 AXIOM                                 -->
<!-- ════════════════════════════════════════ -->

<div id="axiom" style="margin-top:3rem">

<h2 style="font-size:26px;font-weight:700;margin:0 0 1rem"><span class="section-1">1</span> {axiom_title_word}</h2>

<p style="font-size:16px;font-style:italic;margin:0 0 1.5rem">One line. Everything else follows.</p>

<p style="font-size:16px;margin:0 0 1rem">You are reading this sentence. That is a record. Trying to deny it would require the reading to happen, which would make another record, which would prove the reading happened. There is no position you can stand in where the reading has not occurred.</p>

<p style="font-size:16px;margin:0 0 1.5rem">One record exists. The proof is the reading.</p>

<p style="font-size:16px;margin:0 0 1rem">Four conditions follow. Not four assumptions \u2014 four properties the reading already has.</p>

<p style="font-size:16px;margin:0 0 .5rem"><b>Symmetry (S).</b> Two sectors held in mutual reference. The minimum structure for any distinction.</p>

<p style="font-size:16px;margin:0 0 .5rem"><b>Break (B).</b> One element of asymmetry between them. Without it, no information could ever be written.</p>

<p style="font-size:16px;margin:0 0 .5rem"><b>Record (R).</b> What has happened cannot unhappen. The reading cannot be unread.</p>

<p style="font-size:16px;margin:0 0 1.5rem"><b>Constraint (C).</b> The bounded propagation through which the record reaches anywhere. In our universe, the speed of light.</p>

<p style="font-size:16px;margin:0 0 1rem">Compressed into the smallest form S, B, R, C require, the axiom is this:</p>

<div class="axiom-display">1:1 + 1\u00d7<span class="epsilon">\u03b5</span> <span class="at-as">@ AS</span></div>

<p style="font-size:16px;margin:0 0 1rem">The 1:1 is perfect symmetry. The <i>\u03b5</i> is the break. The @ AS names where the break is \u2014 at the Actualizing Structural prior, the now where the substrate is held and the break is processed.</p>

<p style="font-size:16px;margin:0 0 1rem">Written as the cycle AS sustains: <b>1:1 + 1\u00d7\u03b5 \u2212 1\u00d7\u03b5</b>. The +\u03b5 side is actualisation: something becomes a record. The \u22121\u00d7\u03b5 side is defragmentation: a record releases its structure back into potential. Both sides run continuously at AS. A reader inhabits the +\u03b5 side, where records are being written.</p>

<p style="font-size:16px;margin:0 0 1rem">Every Artist\u2019s Proof in the corpus derives from this axiom. The 42 papers below are 42 consequences of the line above. The axiom is the seed. The proofs are the tree.</p>

<p style="font-size:16px;font-style:italic;margin:0 0 .25rem">Nothing did not hold.</p>
<p style="font-size:16px;font-style:italic;margin:0 0 0">The reading is the proof.</p>

</div>

'''

# The Ø Models section HTML
MODELS_SECTION = '''<!-- ════════════════════════════════════════ -->
<!-- Ø MODELS                                -->
<!-- ════════════════════════════════════════ -->

<div id="models" style="margin-top:3rem">

<h2 style="font-size:26px;font-weight:700;margin:0 0 1rem">{models_title}</h2>

<p style="font-size:16px;font-style:italic;margin:0 0 1rem">Five books. The corpus at Reader\u2019s Edition register.</p>

<p style="font-size:16px;margin:0 0 1rem">Five doors are entry points. The Models are the rooms inside. Each book applies the axiom to a different scale of question.</p>

<p style="font-size:16px;margin:0 0 3.5rem">Each volume is published copyleft. Every kill switch is named. Every claim is falsifiable.</p>

<div class="cat-section">
  <h3 class="cat-title">\u00d8 Predictions</h3>
  <p class="cat-desc">The falsifiable physics-facing volume. Five quantitative numbers from one axiom: the proton-to-electron mass ratio, the gravitational constant, the neutron-proton mass difference, the MOND acceleration, the dark sector partition. One measured input: \u03b1 \u2248 1/137. Zero fitted parameters.</p>
  <ul class="dl-list">
    <li><a href="#">\u00d8 Predictions <span class="fmt">Coming Soon</span></a></li>
  </ul>
</div>

<div class="cat-section">
  <h3 class="cat-title">\u00d8 Dissolutions</h3>
  <p class="cat-desc">Twelve classical philosophical problems read through the axiom. Each chapter dissolves, relocates, or closes one of the questions philosophy has asked longest.</p>
  <ul class="dl-list">
    <li><a href="#">\u00d8 Dissolutions <span class="fmt">Coming Soon</span></a></li>
  </ul>
</div>

<div class="cat-section">
  <h3 class="cat-title">\u00d8 Resolutions</h3>
  <p class="cat-desc">Thirteen further problems. Where the previous frameworks could not close, the structural reading walks through.</p>
  <ul class="dl-list">
    <li><a href="#">\u00d8 Resolutions <span class="fmt">Coming Soon</span></a></li>
  </ul>
</div>

<div class="cat-section">
  <h3 class="cat-title">\u00d8 Applications</h3>
  <p class="cat-desc">Twelve architectures of human institutional life. Each derived from the axiom, with kill switches the institutional reading must satisfy.</p>
  <ul class="dl-list">
    <li><a href="#">\u00d8 Applications <span class="fmt">Coming Soon</span></a></li>
  </ul>
</div>

<div class="cat-section">
  <h3 class="cat-title">\u00d8 Horizons</h3>
  <p class="cat-desc">Thirteen domains the structural reading projects across. The volume closes the post-Dissolutions arc.</p>
  <ul class="dl-list">
    <li><a href="#">\u00d8 Horizons <span class="fmt">Coming Soon</span></a></li>
  </ul>
</div>

</div>

'''

CSS_BLOCK = '''/* 1 Axiom section */
.axiom-display{text-align:center;font-size:32px;font-weight:700;letter-spacing:.04em;padding:2.5rem 1rem;margin:2rem 0;border-top:2px solid var(--bk);border-bottom:2px solid var(--bk);line-height:1.3}
.axiom-display .epsilon{font-style:italic}
.axiom-display .at-as{font-weight:400;font-size:24px}
.section-1{}
@media(max-width:600px){.axiom-display{font-size:22px}.axiom-display .at-as{font-size:17px}}
'''

updated = 0
for lang, data in LANGS.items():
    fpath = root / lang / 'index.html'
    if not fpath.exists():
        print(f'SKIP {lang}: not found')
        continue

    text = fpath.read_text(encoding='utf-8')
    orig = text

    # --- 1. Section header renames (in h2 tags) ---
    for prefix in ('physics', 'doors', 'exhibition', 'proofs', 'records'):
        old = data.get(f'{prefix}_old', '')
        new = data.get(f'{prefix}_new', '')
        if old and new and old in text:
            text = text.replace(f'>{old}<', f'>{new}<')

    # --- 2. Sub-section renames ---
    if '>Rosin<' in text:
        text = text.replace('>Rosin<', '>\u00d8 Rosin<')
    if '>Editions<' in text:
        text = text.replace('>Editions<', '>\u00d8 Editions<')
    if '>Notebooks<' in text:
        text = text.replace('>Notebooks<', '>\u00d8 Notebooks<')
    # Fix double prefix
    text = text.replace('>\u00d8 \u00d8 ', '>\u00d8 ')

    # --- 3. Axiom notation ---
    text = text.replace('1:1 + 1\u00d7\u03b5', '1:1 + 1\u00d7\u03b5 @ AS')
    text = text.replace('1:1 + 1\u00d7\u03b5 @ AS @ AS', '1:1 + 1\u00d7\u03b5 @ AS')

    # --- 4. Hero amplification ---
    if data['hero_old'] and data['hero_new'] and data['hero_old'] in text:
        text = text.replace(data['hero_old'], data['hero_new'])

    # --- 5. Add CSS ---
    if 'axiom-display' not in text:
        text = text.replace('/* Unavailable PDF links */', CSS_BLOCK + '/* Unavailable PDF links */')

    # --- 6. Add 1 Axiom section (after </ol> steps, before physics) ---
    if 'id="axiom"' not in text:
        # Find the insertion point: after the </ol> closing the steps list
        # and before the physics section comment or div
        import re
        # Look for </ol> followed by whitespace and a comment or div with physics
        m = re.search(r'(</ol>\s*\n)', text)
        if m:
            axiom_word = data['axiom_title'].replace('1 ', '')
            axiom_html = AXIOM_SECTION_EN.format(axiom_title_word=axiom_word)
            insert_pos = m.end()
            text = text[:insert_pos] + '\n' + axiom_html + text[insert_pos:]

    # --- 7. Add Ø Models section (after five-doors closing div, before exhibition) ---
    if 'id="models"' not in text:
        # Find the insertion point: the exhibition comment block
        exhibition_markers = [
            '<!-- THE EXHIBITION',
            '<!-- Ø EXHIBITION',
            '<!-- LA EXPOSICI',
            '<!-- L\'EXPOSITION',
            '<!-- DIE AUSSTELLUNG',
            '<!-- A EXPOSI',
            '<!-- DE TENTOONSTELLING',
            '<!-- L\'ESPOSIZIONE',
        ]
        for marker in exhibition_markers:
            if marker in text:
                models_html = MODELS_SECTION.format(models_title=data['models_title'])
                text = text.replace(marker, models_html + marker)
                break
        else:
            # Try generic approach: find id="exhibition"
            idx = text.find('id="exhibition"')
            if idx > 0:
                # Go back to find the preceding comment or div start
                line_start = text.rfind('\n', 0, idx)
                if line_start > 0:
                    # Check if there's a comment above
                    prev_lines = text[max(0, line_start-200):line_start]
                    comment_start = prev_lines.rfind('<!--')
                    if comment_start >= 0:
                        abs_comment = max(0, line_start-200) + comment_start
                        models_html = MODELS_SECTION.format(models_title=data['models_title'])
                        text = text[:abs_comment] + models_html + text[abs_comment:]

    # --- 8. Update nav ---
    # Add axiom and models links to nav
    nav_exhibition = data.get('nav_exhibition', '')
    nav_proofs = data.get('nav_proofs', '')
    nav_doors = data.get('nav_doors', '')

    # Add axiom link if not present
    if '#axiom' not in text and nav_doors:
        old_nav = f'<a href="#five-doors">{nav_doors}</a>'
        if old_nav in text:
            text = text.replace(old_nav, f'<a href="#axiom">1 axiom</a>\n  {old_nav}')
    elif '#axiom' not in text:
        # Try to add before exhibition link
        if nav_exhibition:
            old_nav = f'<a href="#exhibition">{nav_exhibition}</a>'
            if old_nav in text:
                text = text.replace(old_nav, f'<a href="#axiom">1 axiom</a>\n  {old_nav}')

    # Add models link if not present
    if '#models' not in text and nav_exhibition:
        old_nav = f'<a href="#exhibition">{nav_exhibition}</a>'
        if old_nav in text:
            text = text.replace(old_nav, f'<a href="#models">\u00d8 models</a>\n  {old_nav}')

    # Update existing nav labels to add Ø prefix
    if nav_doors and f'>{nav_doors}<' in text:
        text = text.replace(f'>{nav_doors}<', f'>\u00d8 {nav_doors}<')
    if nav_exhibition and f'>{nav_exhibition}<' in text:
        text = text.replace(f'>{nav_exhibition}<', f'>\u00d8 {nav_exhibition}<')
    if nav_proofs and f'>{nav_proofs}<' in text:
        text = text.replace(f'>{nav_proofs}<', f'>\u00d8 {nav_proofs}<')

    # Fix double Ø in nav
    text = text.replace('>\u00d8 \u00d8 ', '>\u00d8 ')

    if text != orig:
        shutil.copy2(fpath, fpath.with_suffix('.html.bak3'))
        fpath.write_text(text, encoding='utf-8')
        print(f'UPDATED: {lang}')
        updated += 1
    else:
        print(f'NO CHANGE: {lang}')

print(f'\nTotal updated: {updated}')
