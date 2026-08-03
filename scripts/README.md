# scripts/ — automated deposit tooling

These scripts push the corpus to the four archives the 420 Code is mirrored on.
Each one reads its credential from an **environment variable** and exits
immediately if it is missing. No token is ever written into source.

| Script | Provider | Environment variable(s) |
| --- | --- | --- |
| `osf_upload.py` | OSF (osf.io) | `OSF_TOKEN` |
| `archive_upload.py` | Internet Archive | `IA_ACCESS_KEY`, `IA_SECRET_KEY` |
| `figshare_upload.py` | Figshare | `FIGSHARE_TOKEN` |
| `zenodo_upload.py` | Zenodo — English AP01–AP42 | `ZENODO_TOKEN` |
| `zenodo_languages.py` | Zenodo — per-language editions | `ZENODO_TOKEN` |

## Usage

```bash
pip install requests
cp .env.example .env          # then fill in the values
set -a; . ./.env; set +a      # load them into the shell
python3 scripts/osf_upload.py            # uploads PDFs from the repo root
python3 scripts/osf_upload.py /some/path # or from an explicit directory
```

Each script defaults to reading PDFs from the repository root (the parent of
`scripts/`). Pass a directory as the first argument to override.

## Rotating a credential

If a token is ever exposed, **rotate it at the provider** — deleting the file or
rewriting history does not invalidate a leaked credential; only the provider
revoking it does. Then update your local `.env`. Never commit `.env`.
