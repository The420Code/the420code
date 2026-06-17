#!/usr/bin/env python3
"""Install dual-dynamic correction across all 13 language editions."""
from pathlib import Path

root = Path(r'C:\Users\info\the420code')

# The two variants of the old paragraph found on the site
OLD_EN = (
    '<p style="font-size:16px;margin:0 0 1rem">Written as the cycle AS sustains: '
    '<b>1:1 + 1\u00d7\u03b5 \u2212 1\u00d7\u03b5</b>. '
    'The +\u03b5 side is actualisation: something becomes a record. '
    'The \u22121\u00d7\u03b5 side is defragmentation: a record releases its structure back into potential. '
    'Both sides run continuously at AS. '
    'A reader inhabits the +\u03b5 side, where records are being written.</p>'
)

OLD_OTHER = (
    '<p style="font-size:16px;margin:0 0 1rem">Written as the cycle AS sustains: '
    '<b>1:1 + 1\u00d7\u03b5 \u2212 1\u00d7\u03b5</b>. '
    'The +\u03b5 side is actualisation: something becomes a record. '
    'The \u22121\u00d7\u03b5 side is defragmentation: a record releases its structure back into potential. '
    'Both sides run continuously at AS. '
    'A reader inhabits the +\u03b5 side, where records are being written.</p>'
)

# Also check for the EN variant with just −ε (no 1×)
OLD_EN_V2 = (
    '<p style="font-size:16px;margin:0 0 1rem">Written as the cycle AS sustains: '
    '<b>1:1 + 1\u00d7\u03b5 \u2212 1\u00d7\u03b5</b>. '
    'The +\u03b5 side is actualisation: something becomes a record. '
    'The \u2212\u03b5 side is defragmentation: a record releases its structure back into potential. '
    'Both sides run continuously at AS. '
    'Both sides are one operation, read from two directions. '
    'A reader inhabits the +\u03b5 side, where records are being written.</p>'
)

# The corrected paragraph
NEW = (
    '<p style="font-size:16px;margin:0 0 1rem">Written as the cycle that runs at AS: '
    '<b>1:1 + 1\u00d7\u03b5 @ AS [+1/137 / \u22121/137]</b>. '
    'The break (+1\u00d7\u03b5) is the persistent distinction potential \u2014 held by AS, irreducible, '
    'what S protects from closing. '
    'The \u03b1-flow runs around the held break \u2014 '
    '+1/137 leakage outward as actualisation (records being written), '
    '\u22121/137 replenishment back as defragmentation '
    '(records releasing their structure into potential), '
    'balanced at every AS-instant, net zero. '
    'The break does not cycle in and out; S forbids \u03b5 from closing back. '
    'What cycles is the flow. '
    'A reader inhabits the writing direction of the flow, where records are being committed at AS.</p>'
)

files = [root / 'index.html']
for lang in ['es', 'fr', 'de', 'pt', 'nl', 'it', 'zh', 'ja', 'ko', 'ru', 'ar', 'hi']:
    f = root / lang / 'index.html'
    if f.exists():
        files.append(f)

updated = 0
for fpath in files:
    text = fpath.read_text(encoding='utf-8')
    orig = text

    # Try all known variants
    for old in [OLD_EN, OLD_OTHER, OLD_EN_V2]:
        if old in text:
            text = text.replace(old, NEW)

    # Fallback: grep for any remaining cycle form substring and replace the whole <p>
    if '1:1 + 1\u00d7\u03b5 \u2212 1\u00d7\u03b5' in text:
        # Find the paragraph containing it
        import re
        pattern = re.compile(
            r'<p style="font-size:16px;margin:0 0 1rem">Written as the cycle AS sustains:.*?</p>',
            re.DOTALL
        )
        text = pattern.sub(NEW, text)

    if text != orig:
        fpath.write_text(text, encoding='utf-8')
        print(f'UPDATED: {fpath}')
        updated += 1
    else:
        print(f'NO CHANGE: {fpath}')

print(f'\nTotal updated: {updated}')
