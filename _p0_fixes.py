"""
P0 Critical fixes — the420code.org
Applies P0-1 through P0-6 from the fix brief.
"""
import sys, io, os, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def fix_file(path, replacements, label=""):
    """Apply a list of (old, new) replacements to a file. Returns count of changes."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    changes = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes += count
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    return changes

# ═══════════════════════════════════════════════════
# P0-1: Proton measured value 2018 → 2022
# Change 1836.15267343 → 1836.152673426 everywhere
# BUT preserve 1836.15267344 (the prediction) and 1836.1526734444
# ═══════════════════════════════════════════════════

proton_replacements = [
    # Short code block: measured = 1836.15267343
    ('measured  = 1836.15267343', 'measured  = 1836.152673426   # CODATA 2022'),
    # Full verification block: ratio_meas = m_p / m_e → direct value
    ('ratio_meas  = m_p / m_e', 'ratio_meas  = 1836.152673426   # CODATA 2022'),
    # Physics card
    ('Measured 1836.15267343', 'Measured 1836.152673426 (CODATA 2022)'),
    # Confirm table (measured column)
    ('<td>1836.15267343</td>', '<td>1836.152673426</td>'),
    # Proofs page AP30 entry
    ('Measured: 1836.15267343', 'Measured: 1836.152673426 (CODATA 2022)'),
    # JSON-LD
    ('CODATA measured: 1836.15267343', 'CODATA 2022 measured: 1836.152673426'),
    ('Predicted: 1836.15267344. CODATA measured: 1836.15267343. Accuracy: 5 parts per billion',
     'Predicted: 1836.15267344. CODATA 2022 measured: 1836.152673426. Accuracy: 0.010 ppb (full formula); ~5 ppb at leading order'),
]

# ═══════════════════════════════════════════════════
# P0-2: Proton residual in AP30 (proofs page only)
# ═══════════════════════════════════════════════════

ap30_replacements = [
    ('The residual is 0.008 parts per billion \u2014 7.5 times smaller than the experimental uncertainty.',
     'The residual is 0.010 parts per billion \u2014 comfortably inside the CODATA 2022 error bar, at 0.6\u03c3.'),
    # AP30 heading/lede
    ('Proton mass ratio: predicted 1836.15267344 vs measured 1836.15267343. Five parts per billion.',
     'Proton mass ratio: predicted 1836.15267344 vs measured 1836.152673426. About five parts per billion at leading order; the full formula matches to 0.010 ppb \u2014 finer than the measurement.'),
    ('This paper derives it. And lands within 5 parts per billion.',
     'This paper derives it. About five parts per billion at leading order; the full formula matches to 0.010 ppb \u2014 finer than the measurement.'),
    # AP30 breath line
    ("Mass is not stuff. It is how hard the substrate resists you. The proton\u2019s mass is derived to 5 parts per billion.",
     "Mass is not stuff. It is how hard the substrate resists you. The proton\u2019s mass is derived to 0.010 ppb."),
    # If the simpler form exists
    ("The proton's mass is derived to 5 parts per billion.",
     "The proton's mass is derived to 0.010 ppb."),
]

# ═══════════════════════════════════════════════════
# P0-3: Dark sector 68/27/5 → 69/26/5
# ═══════════════════════════════════════════════════

dark_sector_replacements = [
    # AP42 subtitle
    ('The 68/27/5 partition derived', 'The 69/26/5 partition derived'),
    # AP42 opening hook
    ('68% dark energy. 27% dark matter.', '69% dark energy. 26% dark matter.'),
    # Any remaining 68/27/5
    ('68/27/5', '69/26/5'),
    # Visible matter observed in confirm table
    ('<td>~4.9%</td>', '<td>4.86%</td>'),
    ('Observed:  ~4.9%', 'Observed:  4.86%'),
    # Physics card badge: show honest breakdown instead of just 0.06%
    ('<div class="p-error">0.06%</div></div>\n  </div>', '<div class="p-error">DE 0.06%</div></div>\n  </div>'),
]

# ═══════════════════════════════════════════════════
# P0-4: Definition of C (Constraint)
# ═══════════════════════════════════════════════════

constraint_replacements = [
    ('The bounded propagation through which the record reaches anywhere. In our universe, the speed of light.',
     'A record is somewhere, not everywhere \u2014 the condition of locality, what makes here different from there. Bounded propagation is what Constraint produces, not what it is. In our universe, the speed of light.'),
]

# ═══════════════════════════════════════════════════
# P0-5: Chiral coupling: KS-15 → KS-63, not closed
# ═══════════════════════════════════════════════════

chiral_replacements = [
    # Headline Results on main page
    ('Chiral coupling Derived, KS-15 closed (AP16)',
     'Chiral coupling \u2014 structural argument given, formal theorem owed; KS-63 live (AP27)'),
    ('chiral coupling derived. KS-15 closed \u2014 unexplained since 1956.',
     'chiral coupling \u2014 structural argument via Axiom R + CPT; KS-63 remains the principal open problem.'),
    # Also check for variant phrasings
    ('KS-15 closed', 'KS-63 live'),
]

# ═══════════════════════════════════════════════════
# P0-6: MOND code H0 = 70 → 74.3
# ═══════════════════════════════════════════════════

mond_replacements = [
    # Full verification block
    ('H0   = 70 * 1000 / 3.0857e22  # Hubble constant at 70 km/s/Mpc',
     'H0   = 74.3 * 1000 / 3.0857e22  # H0 = 74.3 km/s/Mpc \u2014 the framework\'s derived value (AP18 / KS-45.1)'),
    # Also the print label
    ('(at H\u2080 = 70)', '(at H\u2080 = 74.3)'),
    # Confirm table MOND row
    ('5.8% (at H\u2080=70)', '0.3% (at H\u2080 = 74.3)'),
    ('<td>5.8% (at H₀=70)</td>', '<td>0.3% (at H₀ = 74.3)</td>'),
    # Headline results
    ('0.3%, parameter-free (AP18)', '0.3% at H₀ = 74.3, parameter-free (AP18)'),
]

# ═══════════════════════════════════════════════════
# Apply all P0 fixes
# ═══════════════════════════════════════════════════

all_replacements = (proton_replacements + ap30_replacements + dark_sector_replacements +
                    constraint_replacements + chiral_replacements + mond_replacements)

# Main page
c = fix_file('index.html', all_replacements, 'main')
print(f'index.html: {c} replacements')

# Proofs page
c = fix_file('proofs/index.html', all_replacements, 'proofs')
print(f'proofs/index.html: {c} replacements')

# Translation files (formula/number fixes only — not prose)
number_fixes = proton_replacements + dark_sector_replacements + mond_replacements
for lang in ['ar','de','es','fr','hi','it','ja','ko','nl','pt','ru','zh']:
    path = f'{lang}/index.html'
    if os.path.exists(path):
        c = fix_file(path, number_fixes, lang)
        if c > 0:
            print(f'{path}: {c} replacements')

# Output files
for path in glob.glob('output/**/index.html', recursive=True):
    c = fix_file(path, number_fixes)
    if c > 0:
        print(f'{path}: {c} replacements')

if os.path.exists('index_en.html'):
    c = fix_file('index_en.html', number_fixes)
    if c > 0:
        print(f'index_en.html: {c} replacements')

# Now add the H0 bridging note after the confirm table
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add note after the MOND table row
mond_note = '\n  <p style="font-size:14px;color:var(--g4);margin:1rem 0 0;font-style:italic">The 0.3% result uses the framework\u2019s derived H\u2080 = 74.3 km/s/Mpc (AP18). At an external H\u2080 = 70 the same formula gives 5.8% \u2014 the dependence is real and stated.</p>'

# Insert after the verify table closing tag
if '</table>\n</div>' in content and mond_note not in content:
    # Find the first </table> that follows the confirm-the-math section
    idx = content.index('confirm-the-math')
    table_end = content.index('</table>', idx)
    insert_pos = content.index('\n', table_end)
    content = content[:insert_pos] + mond_note + content[insert_pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Added H0 bridging note after confirm table')

print('\nP0 fixes complete.')
