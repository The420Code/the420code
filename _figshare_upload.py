import requests, json, os, sys, io, glob, time, hashlib
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TOKEN = '572ccb9f5717c3307318ef9189be6f251575f17ac71623762d87d5afa655f16268d66376b9fee633096720091e0dff1b4e4c4a1cc27c5f7c6cdce3b339a961c7'
BASE = 'https://api.figshare.com/v2'
HEADERS = {'Authorization': f'token {TOKEN}'}
DST = r'C:\Users\info\the420code'

# Create article
print('Creating figshare article...')
article_data = {
    'title': 'The 420 Code - 42 Artist\'s Proofs in 13 Languages (AP01-AP42)',
    'description': (
        '<p><strong>The 420 Code</strong> is a 42-paper physics framework deriving the speed of light, '
        'quantum mechanics, Einstein\'s field equations, the proton mass ratio to 5 parts per billion, '
        'the gravitational constant, the MOND acceleration scale, the Standard Model gauge group, '
        'and a terminal ethic - all from four axioms and one measured input (the fine-structure constant '
        'alpha = 1/137).</p>'
        '<p>258 kill switches published. Zero fitted parameters.</p>'
        '<p>This deposit contains all 42 Artist\'s Proofs in English, plus translated editions '
        '(AP01, AP10, AP20, AP21, AP22, AP23) in Spanish, French, German, Portuguese, Dutch, Italian, '
        'Chinese, Japanese, Korean, Russian, Arabic, and Hindi. Also included: The Illusion of the Other '
        'in all 13 languages and the Master Kill Switch Registry.</p>'
        '<p>Full exhibition: <a href="https://the420code.org">the420code.org</a></p>'
        '<p>Copyleft. Free forever.</p>'
    ),
    'tags': [
        'physics', 'unified theory', 'quantum mechanics', 'general relativity',
        'fine-structure constant', 'proton mass', 'gravitational constant',
        'ethics', 'kill switches', 'falsifiability', 'the 420 code',
        'multilingual', 'copyleft', 'open science'
    ],
      # Mathematical Physics
    'license': 1,  # CC-BY 4.0
    'defined_type': 'preprint',
    'references': [
        'https://the420code.org',
        'https://doi.org/10.5281/zenodo.19208226',
        'https://archive.org/details/the-420-code-artist-proofs'
    ],
}

r = requests.post(f'{BASE}/account/articles', headers={**HEADERS, 'Content-Type': 'application/json'},
                   data=json.dumps(article_data))
if r.status_code != 201:
    print(f'FAIL creating article: {r.status_code} {r.text[:300]}')
    sys.exit(1)

article_url = r.json()['location']
r2 = requests.get(article_url, headers=HEADERS)
article = r2.json()
article_id = article['id']
print(f'Article {article_id} created')

# Upload all PDFs
pdfs = sorted(glob.glob(os.path.join(DST, '*.pdf')))
print(f'Uploading {len(pdfs)} PDFs...')

uploaded = 0
for pdf in pdfs:
    filename = os.path.basename(pdf)
    filesize = os.path.getsize(pdf)

    # Compute MD5
    md5 = hashlib.md5()
    with open(pdf, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
    md5_hash = md5.hexdigest()

    # Initiate upload
    file_data = {'name': filename, 'size': filesize, 'md5': md5_hash}
    r = requests.post(f'{BASE}/account/articles/{article_id}/files',
                      headers={**HEADERS, 'Content-Type': 'application/json'},
                      data=json.dumps(file_data))
    if r.status_code != 201:
        print(f'  FAIL init {filename}: {r.status_code}')
        continue

    file_info = r.json()
    upload_url = file_info['location']

    # Get upload parts info
    r = requests.get(upload_url, headers=HEADERS)
    upload_info = r.json()
    parts_url = upload_info['upload_url']

    # Get parts
    r = requests.get(parts_url, headers=HEADERS)
    parts = r.json()['parts']

    # Upload each part
    with open(pdf, 'rb') as f:
        for part in parts:
            offset = part['startOffset']
            size = part['endOffset'] - offset
            f.seek(offset)
            data = f.read(size)
            r = requests.put(f'{parts_url}/{part["partNo"]}', data=data)

    # Complete upload
    r = requests.post(upload_url, headers=HEADERS)
    uploaded += 1
    if uploaded % 10 == 0:
        print(f'  ... {uploaded}/{len(pdfs)}')

print(f'  {uploaded} files uploaded')

# Publish
print('Publishing...')
r = requests.post(f'{BASE}/account/articles/{article_id}/publish', headers=HEADERS)
if r.status_code == 201:
    # Get public URL
    r2 = requests.get(f'{BASE}/account/articles/{article_id}', headers=HEADERS)
    pub = r2.json()
    doi = pub.get('doi', 'N/A')
    url = pub.get('url_public_html', 'N/A')
    print(f'\nPUBLISHED!')
    print(f'DOI: {doi}')
    print(f'URL: {url}')
else:
    print(f'Publish FAIL: {r.status_code} {r.text[:300]}')
