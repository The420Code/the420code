#!/usr/bin/env python3
"""Split the Interior manuscript into the library generator's source format.

In:  interior/00_front.txt … 07_part6.txt  (the book's own source, one text)
Out: interior_site/00_front.txt   title lines, dedication, Artist's Note, Orientation
     interior_site/chNN.txt       "# NN — Title", "> The Interior, version 2.0, Chapter NN.", body
     interior_site/99_epilogue.txt  the Closing
     interior_site/back.txt       References, Notes on Vocabulary
     interior_site/parts.json     [{label, title, epigraphs, first}]
Nothing is rewritten. Separator lines (---) are dropped; every other paragraph is carried as it stands.
"""
import re, os, glob, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'interior')
OUT = os.path.join(HERE, 'interior_site')
os.makedirs(OUT, exist_ok=True)
for f in glob.glob(os.path.join(OUT, '*')):
    os.remove(f)

text = '\n\n'.join(open(f, encoding='utf8').read().strip() for f in sorted(glob.glob(os.path.join(SRC, '*.txt'))))
blocks = [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]

# the book ends at the colophon, which the web page does not carry
end = next(i for i, b in enumerate(blocks) if b.startswith('~ This work is published for free'))
blocks = blocks[:end]

units = []          # (kind, heading, [paras])
cur = ['title', '', []]
for b in blocks:
    if b == '---':
        continue
    if b.startswith('# '):
        units.append(cur)
        cur = ['unit', b[2:].strip(), []]
    else:
        cur[2].append(b)
units.append(cur)

title_block = units[0][2]          # ~ lines: title, subtitle, door, byline, site, dedication
front, chapters, parts, back, closing = [], [], [], [], None
for kind, head, ps in units[1:]:
    m = re.match(r'(Part [0IVX]+) — (.+)$', head)
    if m:
        parts.append(dict(label=m.group(1), title=m.group(2),
                          epigraphs=[p[2:] for p in ps if p.startswith('~ ')],
                          first=len(chapters) + 1))
        assert all(p.startswith('~ ') for p in ps), head
        continue
    m = re.match(r'Chapter (\d+) — (.+)$', head)
    if m:
        chapters.append((int(m.group(1)), m.group(2), ps))
        continue
    if head in ("Artist's Note", 'Orientation'):
        front.append((head, ps))
    elif head == 'Closing':
        closing = ps
    elif head in ('References', 'Notes on Vocabulary'):
        back.append((head, ps))
    else:
        raise SystemExit('unplaced heading: ' + head)

tl = [p for p in title_block if p.startswith('~ ')]
# title, subtitle, door first (the generator reads tl[1] and tl[2]); the dedication after the first ---
dedication = [p for p in tl if p[2:].startswith(('For everyone', '— where', 'the millions', 'A kinder'))]
head_lines = [p for p in tl if p not in dedication]

def join(ps):
    return '\n\n'.join(ps)

with open(os.path.join(OUT, '00_front.txt'), 'w') as f:
    f.write(join(head_lines) + '\n\n---\n\n' + join(dedication) + '\n\n')
    for h, ps in front:
        f.write(f'# {h}\n\n{join(ps)}\n\n')

for n, title, ps in chapters:
    with open(os.path.join(OUT, f'ch{n:02d}.txt'), 'w') as f:
        f.write(f'# {n} — {title}\n\n> The Interior, version 2.0.5, Chapter {n}.\n\n{join(ps)}\n')

with open(os.path.join(OUT, '99_epilogue.txt'), 'w') as f:
    f.write(f'# Closing\n\n> The Interior, version 2.0.5, Closing.\n\n{join(closing)}\n')

with open(os.path.join(OUT, 'back.txt'), 'w') as f:
    for h, ps in back:
        f.write(f'# {h}\n\n{join(ps)}\n\n')

json.dump(parts, open(os.path.join(OUT, 'parts.json'), 'w'), ensure_ascii=False, indent=1)

# fidelity: every paragraph of the book, minus separators, title block and colophon, lands in exactly one file
out_paras = []
for f in sorted(glob.glob(os.path.join(OUT, '*.txt'))):
    out_paras += [b.strip() for b in re.split(r'\n\s*\n', open(f).read()) if b.strip()]
src_paras = [b for b in blocks if b != '---' and not b.startswith('# ')]
added = [p for p in out_paras if p.startswith(('# ', '> ', '---'))]
carried = [p for p in out_paras if not p.startswith(('# ', '> ', '---'))]
part_paras = sum(len(p['epigraphs']) for p in parts)
missing = [p for p in src_paras if p not in carried and not (p.startswith('~ ') and any(p[2:] in q['epigraphs'] for q in parts))]
print('chapters', len(chapters), '| parts', len(parts), '| front', [h for h, _ in front], '| back', [h for h, _ in back])
print('source paragraphs', len(src_paras), '| carried', len(carried), '| part epigraphs', part_paras, '| missing', len(missing))
for p in missing[:5]:
    print('  MISSING:', p[:100])
