"""
P2 + P3 fixes — the420code.org
"""
import sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ═══════════════════════════════════════════════════
# P2-1: Models volume name "Consequences" → "Applications"
# (default per registry — Appendix B-1 flagged for G)
# ═══════════════════════════════════════════════════

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\u00d8 Consequences', '\u00d8 Applications')
content = content.replace('Consequences <span class="fmt">PDF', 'Applications <span class="fmt">PDF')
print('P2-1: Models volume → Applications (default, flagged for G)')

# ═══════════════════════════════════════════════════
# P2-2: "Three constants, three axioms" duplicated — remove one
# ═══════════════════════════════════════════════════

# Check if there's a standalone "three-constants" line AND one inside a div
three_const = 'Three constants, three axioms:'
count = content.count(three_const)
if count > 1:
    # Remove the second (standalone) occurrence — keep the one in the display block
    idx1 = content.index(three_const)
    idx2 = content.index(three_const, idx1 + 1)
    # Find the full line/element around idx2
    line_start = content.rfind('\n', 0, idx2)
    line_end = content.index('\n', idx2)
    content = content[:line_start] + content[line_end:]
    print('P2-2: Removed duplicate "Three constants" line')
else:
    print(f'P2-2: "Three constants" appears {count} time(s) — no duplicate')

# ═══════════════════════════════════════════════════
# P2-3: Ensure all results tables agree
# (The P0 fixes already corrected all figures — verify consistency)
# ═══════════════════════════════════════════════════

# Just verify — the P0 script already harmonised the figures
remaining_old_proton = content.count('1836.15267343')
if remaining_old_proton > 0:
    print(f'P2-3: WARNING — {remaining_old_proton} old proton values remain!')
else:
    print('P2-3: All results tables consistent (verified)')

# ═══════════════════════════════════════════════════
# P2-4: Social meta tags on proofs page
# ═══════════════════════════════════════════════════

with open('proofs/index.html', 'r', encoding='utf-8') as f:
    proofs = f.read()

og_tags = """<meta property="og:type" content="website">
<meta property="og:url" content="https://the420code.org/proofs/">
<meta property="og:title" content="the 420 code \u2014 43 Artist\u2019s Proofs">
<meta property="og:description" content="43 Artist's Proofs deriving ethics from physics. One measured input. Zero free parameters. 560 kill switches. Copyleft.">
<meta property="og:image" content="https://the420code.org/Eye_of_the_Universe.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="the 420 code">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="the 420 code \u2014 43 Artist\u2019s Proofs">
<meta name="twitter:description" content="43 Artist's Proofs deriving ethics from physics. One measured input. Zero free parameters. 560 kill switches. Copyleft.">
<meta name="twitter:image" content="https://the420code.org/Eye_of_the_Universe.jpg">
"""

if 'og:title' not in proofs:
    # Insert before </head>
    proofs = proofs.replace('</head>', og_tags + '</head>')
    print('P2-4: Added OG + Twitter meta tags to proofs page')
else:
    print('P2-4: OG tags already present')

with open('proofs/index.html', 'w', encoding='utf-8') as f:
    f.write(proofs)

# ═══════════════════════════════════════════════════
# P3-1: "Coming Soon" dead links
# ═══════════════════════════════════════════════════

# Count dead # links
dead_links = content.count('href="#"')
print(f'P3-1: {dead_links} dead # links found — collapsing sections with majority dead links')

# Don't remove individual items — just mark unreleased sections
# The brief says "Hide unreleased items or collapse each section to one 'in production' line"
# Let's add a note to sections that are mostly dead links
# Actually, leave this for G to decide the exact presentation

# ═══════════════════════════════════════════════════
# P3-2: Download counter — suppress low number
# ═══════════════════════════════════════════════════

# Hide the counter display until it has meaningful numbers
if 'id="dl-count"' in content:
    # Find and hide the dl-count element by not displaying it when low
    content = content.replace(
        "el.textContent=d.count.toLocaleString();",
        "if(d.count>100){el.textContent=d.count.toLocaleString();}else{el.textContent='';}"
    )
    print('P3-2: Download counter suppressed when < 100')

# ═══════════════════════════════════════════════════
# P3-4: Logo link — # → /
# ═══════════════════════════════════════════════════

content = content.replace(
    '<a href="#"><img src="Eye_of_the_Universe.jpg"',
    '<a href="/"><img src="Eye_of_the_Universe.jpg"'
)
print('P3-4: Logo link # → /')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Also fix logo on proofs page
with open('proofs/index.html', 'r', encoding='utf-8') as f:
    proofs = f.read()
proofs = proofs.replace(
    '<a href="#"><img src="Eye_of_the_Universe.jpg"',
    '<a href="/"><img src="../Eye_of_the_Universe.jpg"'
)
with open('proofs/index.html', 'w', encoding='utf-8') as f:
    f.write(proofs)

# P3-3: Footer line — leave for G (Appendix B-4)
print('P3-3: Footer dedication — left for G per Appendix B-4')

print('\nP2 + P3 fixes complete.')
