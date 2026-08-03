#!/usr/bin/env python3
"""Upload the corpus PDFs to the Internet Archive (archive.org).

Credentials come from the environment, never the source:

    export IA_ACCESS_KEY=...      # S3 access key
    export IA_SECRET_KEY=...      # S3 secret key
    python3 scripts/archive_upload.py [path-to-pdfs]

[path-to-pdfs] defaults to the repository root (the parent of scripts/).
"""
import requests, os, sys, io, time, glob

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ACCESS = os.environ.get('IA_ACCESS_KEY')
SECRET = os.environ.get('IA_SECRET_KEY')
if not ACCESS or not SECRET:
    sys.exit('IA_ACCESS_KEY and IA_SECRET_KEY must both be set. Export them in your shell; never write them in a file.')

DST = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create one item for the entire 420 Code collection
ITEM_ID = 'the-420-code-artist-proofs'

# Collect all PDFs
pdfs = sorted(glob.glob(os.path.join(DST, '*.pdf')))
print(f'Found {len(pdfs)} PDFs to upload')

# Upload metadata with first file, then add rest
headers_base = {
    'Authorization': f'LOW {ACCESS}:{SECRET}',
    'x-archive-auto-make-bucket': '1',
    'x-amz-auto-make-bucket': '1',
    # Metadata
    'x-archive-meta-collection': 'opensource',
    'x-archive-meta-mediatype': 'texts',
    'x-archive-meta-title': 'The 420 Code -- 42 Artist\'s Proofs in 13 Languages',
    'x-archive-meta-creator': 'G (Studio G, Strand, Cape Town)',
    'x-archive-meta-description': 'The 420 Code is a 42-paper physics framework deriving the speed of light, quantum mechanics, Einstein\'s field equations, the proton mass ratio to 5 parts per billion, the gravitational constant, the MOND acceleration scale, the Standard Model gauge group, and a terminal ethic -- all from four axioms and one measured input (the fine-structure constant alpha approx 1/137). 258 kill switches published. Zero fitted parameters. Copyleft. Free forever. Full exhibition: https://the420code.org',
    'x-archive-meta-subject': 'physics;unified theory;quantum mechanics;general relativity;ethics;the 420 code;fine-structure constant;proton mass;kill switches;copyleft',
    'x-archive-meta-licenseurl': 'https://creativecommons.org/licenses/by/4.0/',
    'x-archive-meta-language': 'eng;spa;fra;deu;por;nld;ita;zho;jpn;kor;rus;ara;hin',
    'x-archive-meta-date': '2026-03-24',
    'x-archive-meta-identifier-doi': '10.5281/zenodo.19208226',
    'x-archive-meta-external-identifier': 'urn:doi:10.5281/zenodo.19208226',
    'x-archive-meta-source': 'https://the420code.org',
    'x-archive-meta-rights': 'Copyleft. You may download, print, share, and distribute freely. You may not alter the source.',
}

uploaded = 0
failed = 0

for pdf in pdfs:
    filename = os.path.basename(pdf)
    url = f'https://s3.us.archive.org/{ITEM_ID}/{filename}'

    headers = dict(headers_base) if uploaded == 0 else {
        'Authorization': f'LOW {ACCESS}:{SECRET}',
    }

    with open(pdf, 'rb') as f:
        r = requests.put(url, headers=headers, data=f)

    if r.status_code in (200, 201):
        print(f'  OK {filename}')
        uploaded += 1
    else:
        print(f'  FAIL {filename}: {r.status_code} {r.text[:100]}')
        failed += 1

    # Small delay to be nice
    if uploaded % 10 == 0:
        time.sleep(1)

print(f'\nDone: {uploaded} uploaded, {failed} failed')
print(f'URL: https://archive.org/details/{ITEM_ID}')
