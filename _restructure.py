import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# === STEP 1: Build proofs/index.html ===

# Extract proofs section (lines 583-1719, 0-indexed 582-1718)
proofs_lines = lines[582:1719]

# Extract styles
styles = re.findall(r'<style[^>]*>.*?</style>', content[:content.index('</head>')], re.DOTALL)
styles_str = '\n'.join(styles)

proofs_page = '<!DOCTYPE html>\n'
proofs_page += '<html lang="en" style="scroll-padding-top:56px"><head>\n'
proofs_page += '<meta charset="UTF-8">\n'
proofs_page += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
proofs_page += "<title>the 420 code \u2014 43 Artist\u2019s Proofs</title>\n"
proofs_page += '<meta name="description" content="43 Artist\'s Proofs deriving ethics from physics. One measured input. Zero free parameters. 560 kill switches. Copyleft.">\n'
proofs_page += '<link rel="canonical" href="https://the420code.org/proofs/">\n'
proofs_page += '<meta name="robots" content="index, follow">\n'
proofs_page += '<meta name="theme-color" content="#111111">\n'
proofs_page += '<meta name="author" content="G \u2014 Studio G">\n'
proofs_page += '<link rel="icon" type="image/jpeg" href="../Eye_of_the_Universe.jpg">\n'
proofs_page += '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
proofs_page += '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
proofs_page += '<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap" rel="stylesheet">\n'
proofs_page += styles_str + '\n'
proofs_page += '</head>\n<body>\n<div class="c">\n\n'
proofs_page += '<nav class="nav">\n'
proofs_page += '  <a class="nav-title" href="/">the 420 code</a>\n'
proofs_page += '  <a href="/">Home</a>\n'
proofs_page += '  <a href="/proofs/">Proofs</a>\n'
proofs_page += '  <a href="/#confirm-the-math">Verify</a>\n'
proofs_page += '  <a href="/#killswitch">Kill Switches</a>\n'
proofs_page += '</nav>\n\n'
proofs_page += ''.join(proofs_lines)
proofs_page += '\n\n<div class="footer">\n'
proofs_page += '  <p style="text-align:center;margin:0 0 1rem"><img src="../Eye_of_the_Universe.jpg" alt="the 420 code" style="height:40px"></p>\n'
proofs_page += "  <p style=\"font-weight:700\">Don\u2019t be a cunt. Be kind.</p>\n"
proofs_page += '  <p>the420code.org \u00b7 Copyleft 2026</p>\n'
proofs_page += '  <p>the lifestyle 1980-08-05 \u2013 2025-12-25</p>\n'
proofs_page += '</div>\n\n</div>\n\n'
proofs_page += '<script>\n'
proofs_page += "function toggleAP(r){r.classList.toggle('open')}\n"
proofs_page += "function togglePart(h){h.nextElementSibling.classList.toggle('collapsed')}\n"
proofs_page += "function scrollToAP(id){var el=document.getElementById(id);if(!el)return;var list=el.closest('.ap-list');if(list&&list.classList.contains('collapsed'))list.classList.remove('collapsed');el.classList.add('open');setTimeout(function(){var y=el.getBoundingClientRect().top+window.pageYOffset-80;window.scrollTo({top:y,behavior:'smooth'})},100)}\n"
proofs_page += '</script>\n</body></html>\n'

# Fix relative PDF links (proofs page is in /proofs/ subfolder)
proofs_page = proofs_page.replace('href="AP', 'href="../AP')
proofs_page = proofs_page.replace('href="Master_Kill_Switch_Registry.pdf"', 'href="../Master_Kill_Switch_Registry.pdf"')

with open('proofs/index.html', 'w', encoding='utf-8') as f:
    f.write(proofs_page)
print('Created proofs/index.html')

# === STEP 2: Replace proofs section in main page with compact notebooks ===

notebooks = """<!-- ════════════════════════════════════════ -->
<!-- Ø NOTEBOOKS                              -->
<!-- ════════════════════════════════════════ -->

<h2 id="proofs" style="font-size:26px;font-weight:700;margin:3rem 0 1rem">Ø Notebooks</h2>
<p style="font-size:16px;color:var(--g4);margin:0 0 2rem">One measured input (α<sub>em</sub>). Zero free parameters. 43 papers. 560 kill switches.</p>

<div class="stats">
  <div><span class="stat-num">43</span><span class="stat-label">Artist's Proofs</span></div>
  <div><span class="stat-num">560</span><span class="stat-label">Kill switches</span></div>
  <div><span class="stat-num">8</span><span class="stat-label">Notebooks</span></div>
</div>

<div class="spine" style="margin-top:2rem">

<div class="part" id="p1"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p1'"><span class="part-num">Notebook I</span><span class="part-name">The Premise</span><span class="part-desc">One record exists. Everything else is consequence. The axiom, its logical proof, and the four conditions that any record requires.</span><span class="part-count">3 papers · AP40, AP01, AP20</span></div></div>

<div class="part" id="p2"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p2'"><span class="part-num">Notebook II</span><span class="part-name">Spacetime</span><span class="part-desc">The arena the break creates. The speed of light, three spatial dimensions, and Einstein's field equations — all derived from the axioms.</span><span class="part-count">4 papers · AP03, AP05, AP10, AP08</span></div></div>

<div class="part" id="p3"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p3'"><span class="part-num">Notebook III</span><span class="part-name">Quantum Mechanics</span><span class="part-desc">The measurement structure of the break. Superposition, uncertainty, decoherence, the Born rule, and entanglement — derived from the empty set and four axioms.</span><span class="part-count">7 papers · AP09, AP07, AP11, AP12, AP13, AP25, AP23</span></div></div>

<div class="part" id="p4"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p4'"><span class="part-num">Notebook IV</span><span class="part-name">Forces &amp; Constants</span><span class="part-desc">The interactions the break permits. Electromagnetism, the electroweak force, the strong force, quantum gravity, and the gravitational constant — all as faces of a single break.</span><span class="part-count">8 papers · AP06, AP15, AP27, AP16, AP19, AP24, AP14, AP28</span></div></div>

<div class="part" id="p5"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p5'"><span class="part-num">Notebook V</span><span class="part-name">Particles &amp; Matter</span><span class="part-desc">The building blocks the break produces. The proton mass ratio to five parts per billion, antimatter segregation, and the baryon asymmetry of the universe.</span><span class="part-count">3 papers · AP30, AP22, AP26</span></div></div>

<div class="part" id="p6"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p6'"><span class="part-num">Notebook VI</span><span class="part-name">Cosmology</span><span class="part-desc">The universe the break inhabits. Galactic rotation curves without dark matter particles, the MOND acceleration scale, the dark energy partition, and the cyclic cosmology.</span><span class="part-count">6 papers · AP21, AP17, AP18, AP41, AP42, AP04</span></div></div>

<div class="part" id="p7"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p7'"><span class="part-num">Notebook VII</span><span class="part-name">The Operator Interface</span><span class="part-desc">The four-term system, the lean, the structural ethic. Pattern coherence as the body's commitment along the amplitude landscape.</span><span class="part-count">5 papers · AP43, AP29, AP02, AP39, AP38</span></div></div>

<div class="part" id="p8"><div class="part-dot"></div>
<div class="part-header" onclick="window.location.href='/proofs/#p8'"><span class="part-num">Notebook VIII</span><span class="part-name">Consequences</span><span class="part-desc">The ethic applied to civilisation. AI alignment, structural justice, bioethics, drug policy, economics, biology, and the body — all derived from the same four axioms.</span><span class="part-count">7 papers · AP31, AP32, AP33, AP34, AP37, AP35, AP36</span></div></div>

</div><!-- /spine -->

<p style="margin:2rem 0 0"><a href="/proofs/" style="font-size:16px;font-weight:700">Read all 43 Artist's Proofs →</a></p>

"""

# Find boundaries
marker_start = '<!-- ════════════════════════════════════════ -->\n<!-- Ø PROOFS'
idx_start = content.index(marker_start)
marker_end = '</div><!-- /spine -->'
idx_end = content.index(marker_end) + len(marker_end)

new_content = content[:idx_start] + notebooks + content[idx_end:]

# Add Proofs link to nav if not already there
if '<a href="/proofs/">Proofs</a>' not in new_content:
    new_content = new_content.replace(
        '<a href="#killswitch">Kill Switches</a>',
        '<a href="/proofs/">Proofs</a>\n  <a href="#killswitch">Kill Switches</a>'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Count lines saved
old_lines = len(content.split('\n'))
new_lines = len(new_content.split('\n'))
print(f'Updated index.html: {old_lines} -> {new_lines} lines (removed {old_lines - new_lines})')
