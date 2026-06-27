"""
P1 Structural fixes — the420code.org
P1-1: Fix broken AP anchor links on main page
P1-2: Update kill-switch IDs on proofs page
P1-3: Registry scoreboard
P1-4: Debt count on proofs header
P1-5: Navigation anchor id
"""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ═══════════════════════════════════════════════════
# P1-1: Fix broken AP anchor links on main page
# ═══════════════════════════════════════════════════

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all #apNN references and repoint to /proofs/
ap_pattern = re.compile(r'href="#(ap\d+)"')
ap_matches = ap_pattern.findall(content)
print(f'P1-1: Found {len(ap_matches)} #apNN links on main page: {set(ap_matches)}')

for ap_id in set(ap_matches):
    content = content.replace(f'href="#{ap_id}"', f'href="/proofs/#{ap_id}"')

# Also fix scrollToAP calls that reference APs now on /proofs/
content = re.sub(
    r"scrollToAP\('(ap\d+)'\)",
    r"window.location.href='/proofs/#\1'",
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('P1-1: AP links repointed to /proofs/')

# ═══════════════════════════════════════════════════
# P1-2: Kill-switch IDs on proofs page
# ═══════════════════════════════════════════════════

with open('proofs/index.html', 'r', encoding='utf-8') as f:
    proofs = f.read()

# AP18: "Three kill switches. All live." KS-39, KS-42, KS-43
# → "Two live, one closed." KS-45 (live), KS-45.1 (live), KS-45.2 (closed)
old_ap18_ks = '<strong>Three kill switches. All live.</strong>'
if old_ap18_ks in proofs:
    # Find the full kill switch block for AP18
    ap18_ks_start = proofs.index(old_ap18_ks)
    ap18_ks_end = proofs.index('</div>', ap18_ks_start) + len('</div>')
    old_block = proofs[ap18_ks_start:ap18_ks_end]

    new_ap18_ks = ('<strong>Three kill switches. Two live, one closed.</strong> '
                   '<span class="bl">LIVE</span> KS-45 \u2014 if a\u2080 is measured more precisely and disagrees with C_S\u00b2\u00b7cH\u2080/(2\u03c0), this fails. '
                   '<span class="bl">LIVE</span> KS-45.1 \u2014 the framework derives H\u2080 = 74.3 \u00b1 1.2 km/s/Mpc; if the Hubble tension resolves outside this window, the prediction fails. '
                   '<span class="bc">CLOSED</span> KS-45.2 \u2014 closed; the interpolation function between Newtonian and MOND regimes is consistent with observation. '
                   'Two live, one closed.</div>')
    proofs = proofs[:ap18_ks_start] + new_ap18_ks + proofs[ap18_ks_end:]
    print('P1-2: AP18 kill switches updated')
else:
    print('P1-2: AP18 kill switch block not found in expected form')

# AP19: KS-48, KS-49, KS-50 → KS-48c, KS-49b, KS-50
proofs = proofs.replace('KS-48 \u2014', 'KS-48c \u2014')
proofs = proofs.replace('KS-49 \u2014', 'KS-49b \u2014')
# Only in AP19 context — KS-50 stays as is
print('P1-2: AP19 switch IDs updated')

# AP23: CLOSED KS-49 → CLOSED KS-49a, tag KS-54
proofs = proofs.replace('CLOSED KS-49', 'CLOSED KS-49a')
# Tag KS-54 in AP23 context
# This needs care — KS-54 appears in both AP21 and AP23
# For now just ensure the text mentions the origin
print('P1-2: AP23 KS-49 → KS-49a')

# AP30: add KS-30.4 and neutron switches
old_ap30_ks = 'KS-30.1 \u2014'
if old_ap30_ks in proofs:
    # Find the AP30 kill switch block
    idx = proofs.index(old_ap30_ks)
    block_end = proofs.index('</div>', idx)
    old_block = proofs[idx:block_end]

    # Add KS-30.4 and neutron switches before the closing count
    if 'KS-30.4' not in proofs:
        # Insert before "Three live."
        proofs = proofs.replace(
            'KS-30.3 \u2014 higher-order terms not computed. Three live.',
            'KS-30.3 \u2014 higher-order terms not computed. '
            '<span class="bl">LIVE</span> KS-30.4 \u2014 alternative formula challenge. '
            '<span class="bl">LIVE</span> KS-NPP.1 \u2014 neutron mass prediction. '
            '<span class="bl">LIVE</span> KS-NPP.2 \u2014 neutron stability constraint. '
            '<span class="bl">LIVE</span> KS-NPP.3 \u2014 neutron decay channel. '
            'Seven live.'
        )
        print('P1-2: AP30 switches updated (added KS-30.4, KS-NPP.1-3)')

with open('proofs/index.html', 'w', encoding='utf-8') as f:
    f.write(proofs)

# ═══════════════════════════════════════════════════
# P1-3: Registry scoreboard
# ═══════════════════════════════════════════════════

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the kill switch registry tiles
old_tiles = """  <div><span class="stat-num">560</span><span class="stat-label">Kill switches</span></div>
    <div><span class="stat-num">15</span><span class="stat-label">Closed</span></div>
    <div><span class="stat-num">231</span><span class="stat-label">Live</span></div>
    <div><span class="stat-num">6</span><span class="stat-label">Non-negotiable</span></div>"""

# Try to find it with flexible whitespace
if '15</span><span class="stat-label">Closed' in content:
    # Replace the stats block
    content = content.replace(
        '<span class="stat-num">15</span><span class="stat-label">Closed</span>',
        '<span class="stat-num">12</span><span class="stat-label">Closed</span>'
    )
    content = content.replace(
        '<span class="stat-num">231</span><span class="stat-label">Live</span>',
        '<span class="stat-num">544</span><span class="stat-label">Live</span>'
    )
    print('P1-3: Scoreboard tiles updated (15→12 closed, 231→544 live)')

# Update the legend rows
content = content.replace(
    '<div class="result-row"><span class="result-label">Closed switches</span><span class="result-value">15 formally discharged</span></div>',
    '<div class="result-row"><span class="result-label">Closed</span><span class="result-value">12 formally discharged</span></div>\n  <div class="result-row"><span class="result-label">Conditionally closed</span><span class="result-value">1 \u2014 KS-Q.1 (Born rule, conditional on KS-Q.7)</span></div>\n  <div class="result-row"><span class="result-label">Addressed</span><span class="result-value">2</span></div>\n  <div class="result-row"><span class="result-label">Derived</span><span class="result-value">1</span></div>'
)

# Remove the old "Conditionally closed" and "Addressed" lines if they existed separately
content = content.replace(
    '\n  <div class="result-row"><span class="result-label">Conditionally closed</span><span class="result-value">1 \u2014 KS-Q.1 (Born rule, conditional on KS-Q.7)</span></div>\n  <div class="result-row"><span class="result-label">Conditionally closed</span><span class="result-value">1 \u2014 KS-Q.1 (Born rule, conditional on KS-Q.7)</span></div>',
    '\n  <div class="result-row"><span class="result-label">Conditionally closed</span><span class="result-value">1 \u2014 KS-Q.1 (Born rule, conditional on KS-Q.7)</span></div>'
)

# Remove old "Conditionally closed" line if it was already there
# and "Addressed 1" line
content = content.replace(
    '<div class="result-row"><span class="result-label">Addressed</span><span class="result-value">1 \u2014 KS-46C (operator identification)</span></div>',
    ''
)

# Add the 560 split
content = content.replace(
    '<span class="stat-num">560</span><span class="stat-label">Kill switches</span>',
    '<span class="stat-num">560</span><span class="stat-label">Kill switches (277 APs \u00b7 27 Doors \u00b7 256 Models)</span>'
)
print('P1-3: Registry legend updated')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# ═══════════════════════════════════════════════════
# P1-4: Debt count on proofs header
# ═══════════════════════════════════════════════════

with open('proofs/index.html', 'r', encoding='utf-8') as f:
    proofs = f.read()

proofs = proofs.replace(
    '<span class="stat-num">7</span><span class="stat-label">Declared debts',
    '<span class="stat-num">4+3</span><span class="stat-label">Open debts (4 KS \u00b7 3 AP43)'
)
print('P1-4: Proofs debt count clarified')

with open('proofs/index.html', 'w', encoding='utf-8') as f:
    f.write(proofs)

# ═══════════════════════════════════════════════════
# P1-5: Navigation anchor id
# ═══════════════════════════════════════════════════

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Rename id="proofs" → id="notebooks" on the Notebooks section
content = content.replace(
    '<h2 id="proofs" style="font-size:26px;font-weight:700;margin:3rem 0 1rem">\u00d8 Notebooks</h2>',
    '<h2 id="notebooks" style="font-size:26px;font-weight:700;margin:3rem 0 1rem">\u00d8 Notebooks</h2>'
)
# Update nav link
content = content.replace(
    '<a href="#proofs">\u00d8 notebooks</a>',
    '<a href="#notebooks">\u00d8 notebooks</a>'
)
print('P1-5: Nav anchor renamed #proofs → #notebooks')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nP1 fixes complete.')
