import requests, json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TOKEN = 'i5PEMeDsWDCNnrYC8lemZsNPSA0y0cSm6i6wLyUcTPvDZXhGTxnYDjFSJqaq'
BASE = 'https://zenodo.org/api'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}
DST = r'C:\Users\info\the420code'

# Create a new deposit
print('Creating deposit...')
r = requests.post(f'{BASE}/deposit/depositions', headers=HEADERS, json={})
if r.status_code != 201:
    print(f'FAIL creating deposit: {r.status_code} {r.text}')
    sys.exit(1)

dep = r.json()
dep_id = dep['id']
bucket_url = dep['links']['bucket']
print(f'Deposit {dep_id} created')

# Upload all 42 English AP PDFs
AP_FILES = [
    ('AP01_The_Actualization_State.pdf', 'AP01 — The Actualization State'),
    ('AP02_The_Operator.pdf', 'AP02 — The Operator'),
    ('AP03_The_Ratio.pdf', 'AP03 — The Ratio'),
    ('AP04_The_Loop_Hypothesis.pdf', 'AP04 — The Loop Hypothesis'),
    ('AP05_The_Break.pdf', 'AP05 — The Break'),
    ('AP06_The_Leakage_Constant.pdf', 'AP06 — The Leakage Constant'),
    ('AP07_The_Record_Measure.pdf', 'AP07 — The Record Measure'),
    ('AP08_The_Identity.pdf', 'AP08 — The Identity'),
    ('AP09_The_Break_Empty_Set.pdf', 'AP09 — The Break (Empty Set)'),
    ('AP10_The_Dimension.pdf', 'AP10 — The Dimension'),
    ('AP11_The_Spin.pdf', 'AP11 — The Spin'),
    ('AP12_The_Limit.pdf', 'AP12 — The Limit'),
    ('AP13_The_Grain.pdf', 'AP13 — The Grain'),
    ('AP14_The_Correction.pdf', 'AP14 — The Correction'),
    ('AP15_The_Connection.pdf', 'AP15 — The Connection'),
    ('AP16_The_Break_Electroweak.pdf', 'AP16 — The Break (Electroweak)'),
    ('AP17_The_Room.pdf', 'AP17 — The Room'),
    ('AP18_The_Floor.pdf', 'AP18 — The Floor'),
    ('AP19_The_Direction.pdf', 'AP19 — The Direction'),
    ('AP20_The_Proof.pdf', 'AP20 — The Proof'),
    ('AP21_The_Web.pdf', 'AP21 — The Web'),
    ('AP22_The_Ledger.pdf', 'AP22 — The Ledger'),
    ('AP23_The_Single_Record.pdf', 'AP23 — The Single Record'),
    ('AP24_The_Residual.pdf', 'AP24 — The Residual'),
    ('AP25_The_Measure.pdf', 'AP25 — The Measure'),
    ('AP26_The_Surplus.pdf', 'AP26 — The Surplus'),
    ('AP27_The_Harmonics.pdf', 'AP27 — The Harmonics'),
    ('AP28_The_Constant.pdf', 'AP28 — The Constant'),
    ('AP29_The_Actualization_Proof.pdf', 'AP29 — The Actualization Proof'),
    ('AP30_The_Resistance.pdf', 'AP30 — The Resistance'),
    ('AP31_The_Alignment.pdf', 'AP31 — The Alignment'),
    ('AP32_The_Correction_Ethics.pdf', 'AP32 — The Correction (Ethics)'),
    ('AP33_The_Boundary.pdf', 'AP33 — The Boundary'),
    ('AP34_The_Inversion.pdf', 'AP34 — The Inversion'),
    ('AP35_The_Ledger_Economics.pdf', 'AP35 — The Ledger (Economics)'),
    ('AP36_The_Feed.pdf', 'AP36 — The Feed'),
    ('AP37_The_First_Boundary.pdf', 'AP37 — The First Boundary'),
    ('AP38_The_Exit.pdf', 'AP38 — The Exit'),
    ('AP39_The_Scaffold.pdf', 'AP39 — The Scaffold'),
    ('AP40_The_Irrational.pdf', 'AP40 — The Irrational'),
    ('AP41_The_Loop.pdf', 'AP41 — The Loop'),
    ('AP42_The_Clock.pdf', 'AP42 — The Clock'),
]

print(f'Uploading {len(AP_FILES)} PDFs...')
for filename, title in AP_FILES:
    filepath = os.path.join(DST, filename)
    if not os.path.exists(filepath):
        print(f'  SKIP {filename} (not found)')
        continue
    with open(filepath, 'rb') as f:
        r = requests.put(
            f'{bucket_url}/{filename}',
            headers={'Authorization': f'Bearer {TOKEN}'},
            data=f
        )
    if r.status_code in (200, 201):
        print(f'  OK {filename}')
    else:
        print(f'  FAIL {filename}: {r.status_code}')

# Set metadata
print('Setting metadata...')
metadata = {
    'metadata': {
        'title': 'The 420 Code — 42 Artist\'s Proofs (AP01–AP42)',
        'upload_type': 'publication',
        'publication_type': 'workingpaper',
        'description': (
            '<p><strong>The 420 Code</strong> is a 42-paper physics framework that derives '
            'the speed of light, quantum mechanics, Einstein\'s field equations, the proton mass ratio '
            'to five parts per billion, the gravitational constant, the MOND acceleration scale, '
            'the Standard Model gauge group, and a terminal ethic — all from four axioms and one '
            'measured input (the fine-structure constant α ≈ 1/137).</p>'
            '<p>258 kill switches are published. Zero fitted parameters. Every claim carries a stated '
            'condition under which it dies.</p>'
            '<p>Full exhibition: <a href="https://the420code.org">the420code.org</a></p>'
            '<p>Copyleft. Free forever.</p>'
        ),
        'creators': [{'name': 'G', 'affiliation': 'Studio G, Strand, Cape Town'}],
        'keywords': [
            'physics', 'unified theory', 'quantum mechanics', 'general relativity',
            'fine-structure constant', 'proton mass', 'gravitational constant',
            'ethics', 'kill switches', 'falsifiability', 'the 420 code'
        ],
        'license': 'cc-by-4.0',
        'access_right': 'open',
        'related_identifiers': [
            {'identifier': 'https://the420code.org', 'relation': 'isSupplementedBy', 'scheme': 'url'}
        ],
        'notes': 'Copyleft. You may download, print, share, and distribute freely. You may not alter the source. Keep the signal clean.',
    }
}

r = requests.put(
    f'{BASE}/deposit/depositions/{dep_id}',
    headers={**HEADERS, 'Content-Type': 'application/json'},
    data=json.dumps(metadata)
)

if r.status_code == 200:
    print('Metadata set successfully')
else:
    print(f'Metadata FAIL: {r.status_code} {r.text[:500]}')

# Publish
print('Publishing...')
r = requests.post(
    f'{BASE}/deposit/depositions/{dep_id}/actions/publish',
    headers=HEADERS
)

if r.status_code == 202:
    pub = r.json()
    doi = pub.get('doi', 'N/A')
    url = pub.get('links', {}).get('html', 'N/A')
    print(f'\nPUBLISHED!')
    print(f'DOI: {doi}')
    print(f'URL: {url}')
else:
    print(f'Publish FAIL: {r.status_code} {r.text[:500]}')
