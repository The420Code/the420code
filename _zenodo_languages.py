import requests, json, os, sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TOKEN = 'i5PEMeDsWDCNnrYC8lemZsNPSA0y0cSm6i6wLyUcTPvDZXhGTxnYDjFSJqaq'
BASE = 'https://zenodo.org/api'
HEADERS = {'Authorization': f'Bearer {TOKEN}'}
DST = r'C:\Users\info\the420code'

LANGUAGES = {
    'es': {
        'name': 'Spanish', 'native': 'Español',
        'illusion': 'La_Ilusion_del_Otro.pdf',
        'aps': {
            'AP01': 'AP01_El_Estado_de_Actualizacion_ES.pdf',
            'AP10': 'AP10_La_Dimension_ES.pdf',
            'AP20': 'AP20_La_Prueba_ES.pdf',
            'AP21': 'AP21_ES.pdf',
        }
    },
    'fr': {
        'name': 'French', 'native': 'Français',
        'illusion': 'L_Illusion_de_l_Autre.pdf',
        'aps': {
            'AP01': 'AP01_LEtat_dActualisation_FR.pdf',
            'AP10': 'AP10_La_Dimension_FR.pdf',
            'AP20': 'AP20_La_Preuve_FR.pdf',
            'AP21': 'AP21_FR.pdf',
        }
    },
    'de': {
        'name': 'German', 'native': 'Deutsch',
        'illusion': 'Die_Illusion_des_Anderen.pdf',
        'aps': {
            'AP01': 'AP01_Der_Aktualisierungszustand_DE.pdf',
            'AP10': 'AP10_Die_Dimension_DE.pdf',
            'AP20': 'AP20_Der_Beweis_DE.pdf',
            'AP21': 'AP21_DE.pdf',
        }
    },
    'pt': {
        'name': 'Portuguese', 'native': 'Português',
        'illusion': 'A_Ilusao_do_Outro.pdf',
        'aps': {
            'AP01': 'AP01_O_Estado_de_Atualizacao_PT.pdf',
            'AP10': 'AP10_A_Dimensao_PT.pdf',
            'AP20': 'AP20_A_Prova_PT.pdf',
            'AP21': 'AP21_PT.pdf',
        }
    },
    'nl': {
        'name': 'Dutch', 'native': 'Nederlands',
        'illusion': 'De_Illusie_van_de_Ander.pdf',
        'aps': {
            'AP01': 'AP01_De_Actualisatietoestand_NL.pdf',
            'AP10': 'AP10_De_Dimensie_NL.pdf',
            'AP20': 'AP20_Het_Bewijs_NL.pdf',
            'AP21': 'AP21_NL.pdf',
        }
    },
    'it': {
        'name': 'Italian', 'native': 'Italiano',
        'illusion': 'L_Illusione_dell_Altro.pdf',
        'aps': {
            'AP01': 'AP01_Lo_Stato_di_Attualizzazione_IT.pdf',
            'AP10': 'AP10_La_Dimensione_IT.pdf',
            'AP20': 'AP20_La_Prova_IT.pdf',
            'AP21': 'AP21_IT.pdf',
        }
    },
    'zh': {
        'name': 'Chinese', 'native': '中文',
        'illusion': 'Illusion_of_the_Other_ZH.pdf',
        'aps': {
            'AP01': 'AP01_ZH.pdf',
            'AP10': 'AP10_Wei_Du_ZH.pdf',
            'AP20': 'AP20_ZH.pdf',
            'AP21': 'AP21_ZH.pdf',
        }
    },
    'ja': {
        'name': 'Japanese', 'native': '日本語',
        'illusion': 'Illusion_of_the_Other_JA.pdf',
        'aps': {
            'AP01': 'AP01_JA.pdf',
            'AP10': 'AP10_Jigen_JA.pdf',
            'AP20': 'AP20_JA.pdf',
            'AP21': 'AP21_JA.pdf',
        }
    },
    'ko': {
        'name': 'Korean', 'native': '한국어',
        'illusion': 'Illusion_of_the_Other_KO.pdf',
        'aps': {
            'AP01': 'AP01_KO.pdf',
            'AP10': 'AP10_Chawon_KO.pdf',
            'AP20': 'AP20_KO.pdf',
            'AP21': 'AP21_KO.pdf',
        }
    },
    'ru': {
        'name': 'Russian', 'native': 'Русский',
        'illusion': 'Illusion_of_the_Other_RU.pdf',
        'aps': {
            'AP10': 'AP10_Izmerenie_RU.pdf',
            'AP20': 'AP20_Dokazatelstvo_RU.pdf',
            'AP21': 'AP21_RU.pdf',
        }
    },
    'ar': {
        'name': 'Arabic', 'native': 'العربية',
        'illusion': 'Illusion_of_the_Other_AR.pdf',
        'aps': {
            'AP10': 'AP10_Al_Bud_AR.pdf',
            'AP20': 'AP20_AR.pdf',
            'AP21': 'AP21_AR.pdf',
        }
    },
    'hi': {
        'name': 'Hindi', 'native': 'हिंदी',
        'illusion': 'Illusion_of_the_Other_HI.pdf',
        'aps': {
            'AP01': 'AP01_HI.pdf',
            'AP10': 'AP10_Aayam_HI.pdf',
            'AP20': 'AP20_HI.pdf',
            'AP21': 'AP21_HI.pdf',
        }
    },
}

results = []

for lang, info in LANGUAGES.items():
    name = info['name']
    native = info['native']
    print(f'\n=== {name} ({native}) ===')

    # Create deposit
    r = requests.post(f'{BASE}/deposit/depositions', headers=HEADERS, json={})
    if r.status_code != 201:
        print(f'  FAIL creating deposit: {r.status_code}')
        continue

    dep = r.json()
    dep_id = dep['id']
    bucket_url = dep['links']['bucket']
    print(f'  Deposit {dep_id} created')

    # Upload Illusion of the Other
    uploaded = 0
    illusion_file = info['illusion']
    illusion_path = os.path.join(DST, illusion_file)
    if os.path.exists(illusion_path):
        with open(illusion_path, 'rb') as f:
            r = requests.put(f'{bucket_url}/{illusion_file}', headers=HEADERS, data=f)
        if r.status_code in (200, 201):
            print(f'  OK {illusion_file}')
            uploaded += 1
        else:
            print(f'  FAIL {illusion_file}: {r.status_code}')

    # Upload AP PDFs
    for ap, filename in info['aps'].items():
        filepath = os.path.join(DST, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                r = requests.put(f'{bucket_url}/{filename}', headers=HEADERS, data=f)
            if r.status_code in (200, 201):
                print(f'  OK {filename}')
                uploaded += 1
            else:
                print(f'  FAIL {filename}: {r.status_code}')

    # Count APs
    ap_list = ', '.join(info['aps'].keys())

    # Set metadata
    metadata = {
        'metadata': {
            'title': f'The 420 Code — {name} Edition ({native})',
            'upload_type': 'publication',
            'publication_type': 'workingpaper',
            'description': (
                f'<p><strong>The 420 Code — {name} Edition</strong></p>'
                f'<p>Translated Artist\'s Proofs ({ap_list}) and The Illusion of the Other '
                f'in {name}.</p>'
                f'<p>The 420 Code is a 42-paper physics framework deriving the speed of light, '
                f'quantum mechanics, Einstein\'s field equations, the proton mass ratio to 5 ppb, '
                f'and a terminal ethic — from four axioms and one measured input (alpha approx 1/137).</p>'
                f'<p>258 kill switches published. Zero fitted parameters.</p>'
                f'<p>Full exhibition: <a href="https://the420code.org/{lang}/">the420code.org/{lang}/</a></p>'
                f'<p>English edition DOI: <a href="https://doi.org/10.5281/zenodo.19208226">10.5281/zenodo.19208226</a></p>'
                f'<p>Copyleft. Free forever.</p>'
            ),
            'creators': [{'name': 'G', 'affiliation': 'Studio G, Strand, Cape Town'}],
            'keywords': [
                'physics', 'unified theory', 'quantum mechanics', 'general relativity',
                'the 420 code', name.lower(), 'translation', 'ethics',
                'fine-structure constant', 'kill switches', 'falsifiability'
            ],
            'license': 'cc-by-4.0',
            'access_right': 'open',
            'language': lang if len(lang) == 2 else lang[:2],
            'related_identifiers': [
                {'identifier': f'https://the420code.org/{lang}/', 'relation': 'isSupplementedBy', 'scheme': 'url'},
                {'identifier': '10.5281/zenodo.19208226', 'relation': 'isTranslationOf', 'scheme': 'doi'},
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
        print(f'  Metadata set')
    else:
        print(f'  Metadata FAIL: {r.status_code} {r.text[:200]}')
        continue

    # Publish
    r = requests.post(f'{BASE}/deposit/depositions/{dep_id}/actions/publish', headers=HEADERS)
    if r.status_code == 202:
        pub = r.json()
        doi = pub.get('doi', 'N/A')
        url = pub.get('links', {}).get('html', 'N/A')
        print(f'  PUBLISHED! DOI: {doi}')
        results.append((name, doi, url, uploaded))
    else:
        print(f'  Publish FAIL: {r.status_code} {r.text[:200]}')

    time.sleep(1)  # Be nice to Zenodo

print('\n\n=== SUMMARY ===')
for name, doi, url, count in results:
    print(f'{name:12s} | {count} files | DOI: {doi} | {url}')
