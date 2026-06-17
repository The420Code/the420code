import requests, json, os, sys, io, glob, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TOKEN = 'xNS9Mk0xRebs2A7hVg7ozYxgFpJz33EZnd4qUs66Ty37oHpxY564yvq47FdwFSrGTIUkfh'
BASE = 'https://api.osf.io/v2'
HEADERS = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
DST = r'C:\Users\info\the420code'

# Step 1: Create project
print('Creating OSF project...')
project_data = {
    'data': {
        'type': 'nodes',
        'attributes': {
            'title': 'The 420 Code - 42 Artist\'s Proofs in 13 Languages',
            'description': (
                'The 420 Code is a 42-paper physics framework deriving the speed of light, '
                'quantum mechanics, Einstein\'s field equations, the proton mass ratio to 5 parts per billion, '
                'the gravitational constant, the MOND acceleration scale, the Standard Model gauge group, '
                'and a terminal ethic - all from four axioms and one measured input (the fine-structure '
                'constant alpha = 1/137). 258 kill switches published. Zero fitted parameters. '
                'Includes The Illusion of the Other in 13 languages. '
                'Full exhibition: https://the420code.org | '
                'Zenodo DOI: 10.5281/zenodo.19208226 | '
                'Internet Archive: https://archive.org/details/the-420-code-artist-proofs | '
                'Copyleft. Free forever.'
            ),
            'category': 'project',
            'public': True,
            'tags': ['physics', 'unified theory', 'quantum mechanics', 'general relativity',
                     'ethics', 'the 420 code', 'fine-structure constant', 'proton mass',
                     'kill switches', 'copyleft', 'multilingual', 'open science'],
        }
    }
}

r = requests.post(f'{BASE}/nodes/', headers=HEADERS, data=json.dumps(project_data))
if r.status_code not in (200, 201):
    print(f'FAIL creating project: {r.status_code} {r.text[:300]}')
    sys.exit(1)

project = r.json()
project_id = project['data']['id']
upload_url = project['data']['links']['upload']
print(f'Project created: {project_id}')
print(f'URL: https://osf.io/{project_id}/')

# Step 2: Get storage provider (osfstorage)
r = requests.get(f'{BASE}/nodes/{project_id}/files/', headers=HEADERS)
providers = r.json()
storage_link = None
for p in providers['data']:
    if p['attributes']['provider'] == 'osfstorage':
        storage_link = p['links']['upload']
        break

if not storage_link:
    print('Could not find osfstorage')
    sys.exit(1)

print(f'Storage found')

# Step 3: Upload PDFs
pdfs = sorted(glob.glob(os.path.join(DST, '*.pdf')))
print(f'Uploading {len(pdfs)} PDFs...')

uploaded = 0
failed = 0
for pdf in pdfs:
    filename = os.path.basename(pdf)
    filesize = os.path.getsize(pdf)

    upload_headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/octet-stream',
    }

    with open(pdf, 'rb') as f:
        r = requests.put(
            f'{storage_link}?kind=file&name={filename}',
            headers=upload_headers,
            data=f,
            timeout=120
        )

    if r.status_code in (200, 201):
        uploaded += 1
        if uploaded % 10 == 0:
            print(f'  ... {uploaded}/{len(pdfs)}')
    else:
        failed += 1
        if failed <= 3:
            print(f'  FAIL {filename}: {r.status_code}')

    sys.stdout.flush()

print(f'\nDone: {uploaded} uploaded, {failed} failed')
print(f'OSF Project: https://osf.io/{project_id}/')
