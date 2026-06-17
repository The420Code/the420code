import re, os

AP_PDFS = {
    'AP01': 'AP01_The_Actualization_State.pdf',
    'AP02': 'AP02_The_Operator.pdf',
    'AP03': 'AP03_The_Ratio.pdf',
    'AP04': 'AP04_The_Loop_Hypothesis.pdf',
    'AP05': 'AP05_The_Break.pdf',
    'AP06': 'AP06_The_Leakage_Constant.pdf',
    'AP07': 'AP07_The_Record_Measure.pdf',
    'AP08': 'AP08_The_Identity.pdf',
    'AP09': 'AP09_The_Break_Empty_Set.pdf',
    'AP10': 'AP10_The_Dimension.pdf',
    'AP11': 'AP11_The_Spin.pdf',
    'AP12': 'AP12_The_Limit.pdf',
    'AP13': 'AP13_The_Grain.pdf',
    'AP14': 'AP14_The_Correction.pdf',
    'AP15': 'AP15_The_Connection.pdf',
    'AP16': 'AP16_The_Break_Electroweak.pdf',
    'AP17': 'AP17_The_Room.pdf',
    'AP18': 'AP18_The_Floor.pdf',
    'AP19': 'AP19_The_Direction.pdf',
    'AP20': 'AP20_The_Proof.pdf',
    'AP21': 'AP21_The_Web.pdf',
    'AP22': 'AP22_The_Ledger.pdf',
    'AP23': 'AP23_The_Single_Record.pdf',
    'AP24': 'AP24_The_Residual.pdf',
    'AP25': 'AP25_The_Measure.pdf',
    'AP26': 'AP26_The_Surplus.pdf',
    'AP27': 'AP27_The_Harmonics.pdf',
    'AP28': 'AP28_The_Constant.pdf',
    'AP29': 'AP29_The_Actualization_Proof.pdf',
    'AP30': 'AP30_The_Resistance.pdf',
    'AP31': 'AP31_The_Alignment.pdf',
    'AP32': 'AP32_The_Correction_Ethics.pdf',
    'AP33': 'AP33_The_Boundary.pdf',
    'AP34': 'AP34_The_Inversion.pdf',
    'AP35': 'AP35_The_Ledger_Economics.pdf',
    'AP36': 'AP36_The_Feed.pdf',
    'AP37': 'AP37_The_First_Boundary.pdf',
    'AP38': 'AP38_The_Exit.pdf',
    'AP39': 'AP39_The_Scaffold.pdf',
    'AP40': 'AP40_The_Irrational.pdf',
    'AP41': 'AP41_The_Loop.pdf',
    'AP42': 'AP42_The_Clock.pdf',
}

# Process English page
fp = r'C:\Users\info\the420code\index.html'
with open(fp, 'r', encoding='utf-8') as f:
    h = f.read()

# Add CSS for header PDF link
css_add = '.ap-header .ap-pdf{font-size:11px;font-weight:700;color:var(--g4);margin-left:6px;text-decoration:none;letter-spacing:.03em}.ap-header .ap-pdf:hover{color:var(--bk);text-decoration:underline}'
h = h.replace('</style>\n</head>', css_add + '</style>\n</head>', 1)

c = 0
for ap, pdf in AP_PDFS.items():
    # Pattern: ap-number">APxx</span><span class="ap-title">Title</span><span class="ap-tag">
    pattern = r'(ap-number">' + ap + r'</span><span class="ap-title">[^<]+</span>)(<span class="ap-tag">)'
    link = r'\1<a class="ap-pdf" href="' + pdf + r'" onclick="event.stopPropagation()">PDF</a>\2'
    h_new = re.sub(pattern, link, h, count=1)
    if h_new != h:
        h = h_new
        c += 1

with open(fp, 'w', encoding='utf-8') as f:
    f.write(h)

print(f'English: {c} PDF links added to headers')

# Now do non-English pages - they use ../APxx.pdf and show "Publishing Soon" toast for missing PDFs
LANGS = {
    'es': '../', 'fr': '../', 'de': '../', 'pt': '../',
    'nl': '../', 'it': '../', 'zh': '../', 'ja': '../',
    'ko': '../', 'ru': '../', 'ar': '../', 'hi': '../'
}

for lang, prefix in LANGS.items():
    fp = os.path.join(r'C:\Users\info\the420code', lang, 'index.html')
    with open(fp, 'r', encoding='utf-8') as f:
        h = f.read()

    # Add CSS if not present
    if '.ap-header .ap-pdf' not in h:
        h = h.replace('</style>\n</head>', css_add + '</style>\n</head>', 1)

    c = 0
    for ap, pdf in AP_PDFS.items():
        # Use English PDFs with ../ prefix - they'll get the toast for non-English if href="#"
        # For now, link to English PDFs from all pages (better than nothing)
        pattern = r'(ap-number">' + ap + r'</span><span class="ap-title">[^<]+</span>)(<span class="ap-tag">)'
        # Check if already has ap-pdf link
        check = re.search(pattern, h)
        if check and 'ap-pdf' not in check.group(0):
            link = r'\1<a class="ap-pdf" href="' + prefix + pdf + r'" onclick="event.stopPropagation()">PDF</a>\2'
            h_new = re.sub(pattern, link, h, count=1)
            if h_new != h:
                h = h_new
                c += 1

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(h)
    print(f'  {lang}: {c} PDF links added')

print('Done')
