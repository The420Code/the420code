#!/usr/bin/env python3
"""Patch the Exhibition section in 12 language pages.

For each language, replace blocks with English brand names
(Rosin / Editions / Notebooks) per spec, while keeping
translated descriptions and translated voice/subject names.
"""
import io, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# Per-language config:
# Each entry contains:
#   rosin_old_h3, rosin_new_h3
#   rosin_old_links (5 strings, each the old link text inside <a>)
#   rosin_new_links (5 strings)
#   rosin_desc_replacements: list of (old, new) for description paragraphs
#   editions_old_h3, editions_new_h3
#   editions_old_links / new_links
#   editions_desc_replacements
#   notebooks_old_h3, notebooks_new_h3
#   notebooks_old_links_voices (5 originals incl proofs line - we'll remove proofs)
#   notebooks_new_links_voices (4 new strings - the kept ones)
#   notebooks_old_subjects (8 strings beginning with Ø.N)
#   notebooks_new_subjects (8 strings beginning with the translated "Notebooks Ø ...")
#   notebooks_desc_replacements

# Helper: voice translations per language
# voices order: prose, conversation, metaphor, nursery rhyme, proofs

LANGS = {}

# ----------------- FRENCH -----------------
LANGS['fr'] = dict(
    rosin_h3=('La Colophane', 'Rosin'),
    rosin_old_links=[
        'La Résine — Prose',
        'La Résine — Conversation',
        'La Résine — Métaphore',
        'La Résine — Comptine',
        'La Résine — Preuves',
    ],
    rosin_new_links=[
        'Rosin Ø Prose',
        'Rosin Ø Conversation',
        'Rosin Ø Métaphore',
        'Rosin Ø Comptine',
        'Rosin Ø Preuves',
    ],
    rosin_desc=[],  # nothing referencing "La Résine" inside the desc
    editions_h3=('Les Éditions', 'Editions'),
    editions_old_links=[
        'Les Éditions — Prose',
        'Les Éditions — Conversation',
        'Les Éditions — Métaphore',
        'Les Éditions — Comptine',
        'Les Éditions — Preuves',
    ],
    editions_new_links=[
        'Editions Ø Prose',
        'Editions Ø Conversation',
        'Editions Ø Métaphore',
        'Editions Ø Comptine',
        'Editions Ø Preuves',
    ],
    editions_desc=[
        ('La Colophane les photographie. Les Cahiers les indexent. Les Archives documentent comment elles ont été faites. Les Éditions sont ce qui a été fait.',
         'Rosin les photographie. Notebooks les indexent. Les Archives documentent comment elles ont été faites. Editions sont ce qui a été fait.'),
    ],
    notebooks_h3=('Les Cahiers', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">Les Cahiers Ø Prose <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Les Cahiers Ø Conversation <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Les Cahiers Ø Métaphore <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Les Cahiers Ø Comptine <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Les Cahiers Ø Preuves <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Prose <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Conversation <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Métaphore <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Comptine <span class="fmt">PDF</span></a></li>',
    ],  # proofs removed
    notebooks_old_subjects=[
        'Ø.1 La Prémisse',
        'Ø.2 Espace-temps',
        'Ø.3 Mécanique quantique',
        'Ø.4 Forces et constantes',
        'Ø.5 Particules et matière',
        'Ø.6 Cosmologie',
        "Ø.7 Conscience et l'éthique",
        'Ø.8 Applications',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø La Prémisse',
        'Notebooks Ø Espace-temps',
        'Notebooks Ø Mécanique quantique',
        'Notebooks Ø Forces et constantes',
        'Notebooks Ø Particules et matière',
        'Notebooks Ø Cosmologie',
        "Notebooks Ø Conscience et l'éthique",
        'Notebooks Ø Applications',
    ],
    notebooks_desc=[
        ("Les Éditions construisent l'argument en entier. Les Cahiers le démontent et posent chaque pièce sur la table.",
         "Editions construisent l'argument en entier. Notebooks le démontent et posent chaque pièce sur la table."),
    ],
)

# ----------------- GERMAN -----------------
LANGS['de'] = dict(
    rosin_h3=('Das Kolophonium', 'Rosin'),
    rosin_old_links=[
        'Das Harz — Prosa',
        'Das Harz — Gespräch',
        'Das Harz — Metapher',
        'Das Harz — Kinderreim',
        'Das Harz — Beweise',
    ],
    rosin_new_links=[
        'Rosin Ø Prosa',
        'Rosin Ø Gespräch',
        'Rosin Ø Metapher',
        'Rosin Ø Kinderreim',
        'Rosin Ø Beweise',
    ],
    rosin_desc=[],
    editions_h3=('Die Editionen', 'Editions'),
    editions_old_links=[
        'Die Ausgaben — Prosa',
        'Die Ausgaben — Gespräch',
        'Die Ausgaben — Metapher',
        'Die Ausgaben — Kinderreim',
        'Die Ausgaben — Beweise',
    ],
    editions_new_links=[
        'Editions Ø Prosa',
        'Editions Ø Gespräch',
        'Editions Ø Metapher',
        'Editions Ø Kinderreim',
        'Editions Ø Beweise',
    ],
    editions_desc=[
        ('Das Kolophonium fotografiert sie. Die Notizbücher indexieren sie. Die Aufzeichnungen dokumentieren, wie sie entstanden. Die Editionen sind das, was geschaffen wurde.',
         'Rosin fotografiert sie. Notebooks indexieren sie. Die Aufzeichnungen dokumentieren, wie sie entstanden. Editions sind das, was geschaffen wurde.'),
    ],
    notebooks_h3=('Die Notizbücher', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">Die Notizbücher Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Die Notizbücher Ø Gespräch <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Die Notizbücher Ø Metapher <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Die Notizbücher Ø Kinderreim <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Die Notizbücher Ø Beweise <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Gespräch <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Metapher <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Kinderreim <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 Die Prämisse',
        'Ø.2 Raumzeit',
        'Ø.3 Quantenmechanik',
        'Ø.4 Kräfte und Konstanten',
        'Ø.5 Teilchen und Materie',
        'Ø.6 Kosmologie',
        'Ø.7 Bewusstsein und die Ethik',
        'Ø.8 Anwendungen',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø Die Prämisse',
        'Notebooks Ø Raumzeit',
        'Notebooks Ø Quantenmechanik',
        'Notebooks Ø Kräfte und Konstanten',
        'Notebooks Ø Teilchen und Materie',
        'Notebooks Ø Kosmologie',
        'Notebooks Ø Bewusstsein und die Ethik',
        'Notebooks Ø Anwendungen',
    ],
    notebooks_desc=[
        ('Die Editionen bauen das Argument als Ganzes. Die Notizbücher nehmen es auseinander und legen jedes Teil auf den Tisch.',
         'Editions bauen das Argument als Ganzes. Notebooks nehmen es auseinander und legen jedes Teil auf den Tisch.'),
    ],
)

# ----------------- SPANISH -----------------
LANGS['es'] = dict(
    rosin_h3=('La Resina', 'Rosin'),
    rosin_old_links=[
        'La Resina — Prosa',
        'La Resina — Conversación',
        'La Resina — Metáfora',
        'La Resina — Canción infantil',
        'La Resina — Pruebas',
    ],
    rosin_new_links=[
        'Rosin Ø Prosa',
        'Rosin Ø Conversación',
        'Rosin Ø Metáfora',
        'Rosin Ø Canción infantil',
        'Rosin Ø Pruebas',
    ],
    rosin_desc=[],
    editions_h3=('Las Ediciones', 'Editions'),
    editions_old_links=[
        'Las Ediciones — Prosa',
        'Las Ediciones — Conversación',
        'Las Ediciones — Metáfora',
        'Las Ediciones — Canción infantil',
        'Las Ediciones — Pruebas',
    ],
    editions_new_links=[
        'Editions Ø Prosa',
        'Editions Ø Conversación',
        'Editions Ø Metáfora',
        'Editions Ø Canción infantil',
        'Editions Ø Pruebas',
    ],
    editions_desc=[
        ('La Resina las fotografía. Los Cuadernos las indexan. Los Registros documentan cómo se hicieron. Las Ediciones son lo que se hizo.',
         'Rosin las fotografía. Notebooks las indexan. Los Registros documentan cómo se hicieron. Editions son lo que se hizo.'),
    ],
    notebooks_h3=('Los Cuadernos', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">Los Cuadernos Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Los Cuadernos Ø Conversación <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Los Cuadernos Ø Metáfora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Los Cuadernos Ø Canción infantil <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Los Cuadernos Ø Pruebas <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Conversación <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Metáfora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Canción infantil <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 La Premisa',
        'Ø.2 Espaciotiempo',
        'Ø.3 Mecánica cuántica',
        'Ø.4 Fuerzas y constantes',
        'Ø.5 Partículas y materia',
        'Ø.6 Cosmología',
        'Ø.7 Consciencia y la ética',
        'Ø.8 Aplicaciones',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø La Premisa',
        'Notebooks Ø Espaciotiempo',
        'Notebooks Ø Mecánica cuántica',
        'Notebooks Ø Fuerzas y constantes',
        'Notebooks Ø Partículas y materia',
        'Notebooks Ø Cosmología',
        'Notebooks Ø Consciencia y la ética',
        'Notebooks Ø Aplicaciones',
    ],
    notebooks_desc=[
        ('Las Ediciones construyen el argumento entero. Los Cuadernos lo desarman y ponen cada pieza sobre la mesa.',
         'Editions construyen el argumento entero. Notebooks lo desarman y ponen cada pieza sobre la mesa.'),
    ],
)

# ----------------- ITALIAN -----------------
LANGS['it'] = dict(
    rosin_h3=('La Colofonia', 'Rosin'),
    rosin_old_links=[
        'La Resina — Prosa',
        'La Resina — Conversazione',
        'La Resina — Metafora',
        'La Resina — Filastrocca',
        'La Resina — Prove',
    ],
    rosin_new_links=[
        'Rosin Ø Prosa',
        'Rosin Ø Conversazione',
        'Rosin Ø Metafora',
        'Rosin Ø Filastrocca',
        'Rosin Ø Prove',
    ],
    rosin_desc=[],
    editions_h3=('Le Edizioni', 'Editions'),
    editions_old_links=[
        'Le Edizioni — Prosa',
        'Le Edizioni — Conversazione',
        'Le Edizioni — Metafora',
        'Le Edizioni — Filastrocca',
        'Le Edizioni — Prove',
    ],
    editions_new_links=[
        'Editions Ø Prosa',
        'Editions Ø Conversazione',
        'Editions Ø Metafora',
        'Editions Ø Filastrocca',
        'Editions Ø Prove',
    ],
    editions_desc=[
        ('La Colofonia le fotografa. I Quaderni le indicizzano. I Registri documentano come sono state fatte. Le Edizioni sono ciò che è stato fatto.',
         'Rosin le fotografa. Notebooks le indicizzano. I Registri documentano come sono state fatte. Editions sono ciò che è stato fatto.'),
    ],
    notebooks_h3=('I Quaderni', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">I Quaderni Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">I Quaderni Ø Conversazione <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">I Quaderni Ø Metafora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">I Quaderni Ø Filastrocca <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">I Quaderni Ø Prove <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Conversazione <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Metafora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Filastrocca <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 La Premessa',
        'Ø.2 Spaziotempo',
        'Ø.3 Meccanica quantistica',
        'Ø.4 Forze e costanti',
        'Ø.5 Particelle e materia',
        'Ø.6 Cosmologia',
        "Ø.7 Coscienza e l'etica",
        'Ø.8 Applicazioni',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø La Premessa',
        'Notebooks Ø Spaziotempo',
        'Notebooks Ø Meccanica quantistica',
        'Notebooks Ø Forze e costanti',
        'Notebooks Ø Particelle e materia',
        'Notebooks Ø Cosmologia',
        "Notebooks Ø Coscienza e l'etica",
        'Notebooks Ø Applicazioni',
    ],
    notebooks_desc=[
        ("Le Edizioni costruiscono l'argomento intero. I Quaderni lo smontano e posano ogni pezzo sul tavolo.",
         "Editions costruiscono l'argomento intero. Notebooks lo smontano e posano ogni pezzo sul tavolo."),
    ],
)

# ----------------- PORTUGUESE -----------------
LANGS['pt'] = dict(
    rosin_h3=('A Resina', 'Rosin'),
    rosin_old_links=[
        'A Resina — Prosa',
        'A Resina — Conversa',
        'A Resina — Metáfora',
        'A Resina — Cantiga',
        'A Resina — Provas',
    ],
    rosin_new_links=[
        'Rosin Ø Prosa',
        'Rosin Ø Conversa',
        'Rosin Ø Metáfora',
        'Rosin Ø Cantiga',
        'Rosin Ø Provas',
    ],
    rosin_desc=[],
    editions_h3=('As Edições', 'Editions'),
    editions_old_links=[
        'As Edições — Prosa',
        'As Edições — Conversa',
        'As Edições — Metáfora',
        'As Edições — Cantiga',
        'As Edições — Provas',
    ],
    editions_new_links=[
        'Editions Ø Prosa',
        'Editions Ø Conversa',
        'Editions Ø Metáfora',
        'Editions Ø Cantiga',
        'Editions Ø Provas',
    ],
    editions_desc=[
        ('A Resina as fotografa. Os Cadernos as indexam. Os Registros documentam como foram feitas. As Edições são o que foi feito.',
         'Rosin as fotografa. Notebooks as indexam. Os Registros documentam como foram feitas. Editions são o que foi feito.'),
    ],
    notebooks_h3=('Os Cadernos', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">Os Cadernos Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Os Cadernos Ø Conversa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Os Cadernos Ø Metáfora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Os Cadernos Ø Cantiga <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Os Cadernos Ø Provas <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Prosa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Conversa <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Metáfora <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Cantiga <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 A Premissa',
        'Ø.2 Espaço-tempo',
        'Ø.3 Mecânica quântica',
        'Ø.4 Forças e constantes',
        'Ø.5 Partículas e matéria',
        'Ø.6 Cosmologia',
        'Ø.7 Consciência e a ética',
        'Ø.8 Aplicações',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø A Premissa',
        'Notebooks Ø Espaço-tempo',
        'Notebooks Ø Mecânica quântica',
        'Notebooks Ø Forças e constantes',
        'Notebooks Ø Partículas e matéria',
        'Notebooks Ø Cosmologia',
        'Notebooks Ø Consciência e a ética',
        'Notebooks Ø Aplicações',
    ],
    notebooks_desc=[
        ('As Edições constroem o argumento inteiro. Os Cadernos o desmontam e colocam cada peça sobre a mesa.',
         'Editions constroem o argumento inteiro. Notebooks o desmontam e colocam cada peça sobre a mesa.'),
    ],
)

# ----------------- DUTCH -----------------
LANGS['nl'] = dict(
    rosin_h3=('De Hars', 'Rosin'),
    rosin_old_links=[
        'De Hars — Proza',
        'De Hars — Gesprek',
        'De Hars — Metafoor',
        'De Hars — Kinderrijm',
        'De Hars — Bewijzen',
    ],
    rosin_new_links=[
        'Rosin Ø Proza',
        'Rosin Ø Gesprek',
        'Rosin Ø Metafoor',
        'Rosin Ø Kinderrijm',
        'Rosin Ø Bewijzen',
    ],
    rosin_desc=[],
    editions_h3=('De Edities', 'Editions'),
    editions_old_links=[
        'De Edities — Proza',
        'De Edities — Gesprek',
        'De Edities — Metafoor',
        'De Edities — Kinderrijm',
        'De Edities — Bewijzen',
    ],
    editions_new_links=[
        'Editions Ø Proza',
        'Editions Ø Gesprek',
        'Editions Ø Metafoor',
        'Editions Ø Kinderrijm',
        'Editions Ø Bewijzen',
    ],
    editions_desc=[
        ('De Hars fotografeert ze. De Notitieboeken indexeren ze. De Verslagen documenteren hoe ze gemaakt zijn. De Edities zijn wat er gemaakt is.',
         'Rosin fotografeert ze. Notebooks indexeren ze. De Verslagen documenteren hoe ze gemaakt zijn. Editions zijn wat er gemaakt is.'),
    ],
    notebooks_h3=('De Schriften', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">De Notitieboeken Ø Proza <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">De Notitieboeken Ø Gesprek <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">De Notitieboeken Ø Metafoor <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">De Notitieboeken Ø Kinderrijm <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">De Notitieboeken Ø Bewijzen <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Proza <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Gesprek <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Metafoor <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Kinderrijm <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 De Premisse',
        'Ø.2 Ruimtetijd',
        'Ø.3 Kwantummechanica',
        'Ø.4 Krachten en constanten',
        'Ø.5 Deeltjes en materie',
        'Ø.6 Kosmologie',
        'Ø.7 Bewustzijn en de ethiek',
        'Ø.8 Toepassingen',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø De Premisse',
        'Notebooks Ø Ruimtetijd',
        'Notebooks Ø Kwantummechanica',
        'Notebooks Ø Krachten en constanten',
        'Notebooks Ø Deeltjes en materie',
        'Notebooks Ø Kosmologie',
        'Notebooks Ø Bewustzijn en de ethiek',
        'Notebooks Ø Toepassingen',
    ],
    notebooks_desc=[
        ('De Edities bouwen het argument als geheel. De Notitieboeken nemen het uit elkaar en leggen elk stuk op tafel.',
         'Editions bouwen het argument als geheel. Notebooks nemen het uit elkaar en leggen elk stuk op tafel.'),
    ],
)

# ----------------- RUSSIAN -----------------
LANGS['ru'] = dict(
    rosin_h3=('Канифоль', 'Rosin'),
    rosin_old_links=[
        'Канифоль — Проза',
        'Канифоль — Диалог',
        'Канифоль — Метафора',
        'Канифоль — Считалка',
        'Канифоль — Доказательства',
    ],
    rosin_new_links=[
        'Rosin Ø Проза',
        'Rosin Ø Диалог',
        'Rosin Ø Метафора',
        'Rosin Ø Считалка',
        'Rosin Ø Доказательства',
    ],
    rosin_desc=[],
    editions_h3=('Издания', 'Editions'),
    editions_old_links=[
        'Издания — Проза',
        'Издания — Диалог',
        'Издания — Метафора',
        'Издания — Считалка',
        'Издания — Доказательства',
    ],
    editions_new_links=[
        'Editions Ø Проза',
        'Editions Ø Диалог',
        'Editions Ø Метафора',
        'Editions Ø Считалка',
        'Editions Ø Доказательства',
    ],
    editions_desc=[
        ('Канифоль их фотографирует. Тетради их индексируют. Записи документируют, как они были созданы. Издания — это то, что было создано.',
         'Rosin их фотографирует. Notebooks их индексируют. Записи документируют, как они были созданы. Editions — это то, что было создано.'),
    ],
    notebooks_h3=('Тетради', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">Тетради Ø Проза <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Тетради Ø Диалог <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Тетради Ø Метафора <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Тетради Ø Считалка <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Тетради Ø Доказательства <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø Проза <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Диалог <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Метафора <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø Считалка <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 Предпосылка',
        'Ø.2 Пространство-время',
        'Ø.3 Квантовая механика',
        'Ø.4 Силы и константы',
        'Ø.5 Частицы и материя',
        'Ø.6 Космология',
        'Ø.7 Сознание и этика',
        'Ø.8 Приложения',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø Предпосылка',
        'Notebooks Ø Пространство-время',
        'Notebooks Ø Квантовая механика',
        'Notebooks Ø Силы и константы',
        'Notebooks Ø Частицы и материя',
        'Notebooks Ø Космология',
        'Notebooks Ø Сознание и этика',
        'Notebooks Ø Приложения',
    ],
    notebooks_desc=[
        ('Издания строят аргумент целиком. Тетради разбирают его и раскладывают каждую деталь на столе.',
         'Editions строят аргумент целиком. Notebooks разбирают его и раскладывают каждую деталь на столе.'),
    ],
)

# ----------------- CHINESE -----------------
LANGS['zh'] = dict(
    rosin_h3=('松香', 'Rosin'),
    rosin_old_links=[
        '松香 — 散文',
        '松香 — 对话',
        '松香 — 隐喻',
        '松香 — 童谣',
        '松香 — 证明',
    ],
    rosin_new_links=[
        'Rosin Ø 散文',
        'Rosin Ø 对话',
        'Rosin Ø 隐喻',
        'Rosin Ø 童谣',
        'Rosin Ø 证明',
    ],
    rosin_desc=[],
    editions_h3=('版本', 'Editions'),
    editions_old_links=[
        '版本 — 散文',
        '版本 — 对话',
        '版本 — 隐喻',
        '版本 — 童谣',
        '版本 — 证明',
    ],
    editions_new_links=[
        'Editions Ø 散文',
        'Editions Ø 对话',
        'Editions Ø 隐喻',
        'Editions Ø 童谣',
        'Editions Ø 证明',
    ],
    editions_desc=[
        ('松香为它们拍照。笔记本为它们编索引。记录记载了它们如何被制作。版本就是被制作出来的东西。',
         'Rosin为它们拍照。Notebooks为它们编索引。记录记载了它们如何被制作。Editions就是被制作出来的东西。'),
    ],
    notebooks_h3=('笔记本', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">笔记本 Ø 散文 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">笔记本 Ø 对话 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">笔记本 Ø 隐喻 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">笔记本 Ø 童谣 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">笔记本 Ø 证明 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø 散文 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 对话 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 隐喻 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 童谣 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 前提',
        'Ø.2 时空',
        'Ø.3 量子力学',
        'Ø.4 力与常数',
        'Ø.5 粒子与物质',
        'Ø.6 宇宙学',
        'Ø.7 意识与伦理',
        'Ø.8 应用',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø 前提',
        'Notebooks Ø 时空',
        'Notebooks Ø 量子力学',
        'Notebooks Ø 力与常数',
        'Notebooks Ø 粒子与物质',
        'Notebooks Ø 宇宙学',
        'Notebooks Ø 意识与伦理',
        'Notebooks Ø 应用',
    ],
    notebooks_desc=[
        ('版本将论证构建为整体。笔记本将其拆开，把每一块都摆在桌上。',
         'Editions将论证构建为整体。Notebooks将其拆开，把每一块都摆在桌上。'),
    ],
)

# ----------------- JAPANESE -----------------
LANGS['ja'] = dict(
    rosin_h3=('ロジン', 'Rosin'),
    rosin_old_links=[
        'ロジン — 散文',
        'ロジン — 対話',
        'ロジン — 比喩',
        'ロジン — 童謡',
        'ロジン — 証明',
    ],
    rosin_new_links=[
        'Rosin Ø 散文',
        'Rosin Ø 対話',
        'Rosin Ø 比喩',
        'Rosin Ø 童謡',
        'Rosin Ø 証明',
    ],
    rosin_desc=[],
    editions_h3=('エディション', 'Editions'),
    editions_old_links=[
        'エディション — 散文',
        'エディション — 対話',
        'エディション — 比喩',
        'エディション — 童謡',
        'エディション — 証明',
    ],
    editions_new_links=[
        'Editions Ø 散文',
        'Editions Ø 対話',
        'Editions Ø 比喩',
        'Editions Ø 童謡',
        'Editions Ø 証明',
    ],
    editions_desc=[
        ('ロジンがそれを撮影する。ノートブックがそれを索引する。レコードがそれがどう作られたかを記録する。エディションが作られたものそのものだ。',
         'Rosinがそれを撮影する。Notebooksがそれを索引する。レコードがそれがどう作られたかを記録する。Editionsが作られたものそのものだ。'),
    ],
    notebooks_h3=('ノートブック', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">ノートブック Ø 散文 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">ノートブック Ø 対話 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">ノートブック Ø 比喩 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">ノートブック Ø 童謡 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">ノートブック Ø 証明 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø 散文 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 対話 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 比喩 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 童謡 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 前提',
        'Ø.2 時空',
        'Ø.3 量子力学',
        'Ø.4 力と定数',
        'Ø.5 粒子と物質',
        'Ø.6 宇宙論',
        'Ø.7 意識と倫理',
        'Ø.8 応用',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø 前提',
        'Notebooks Ø 時空',
        'Notebooks Ø 量子力学',
        'Notebooks Ø 力と定数',
        'Notebooks Ø 粒子と物質',
        'Notebooks Ø 宇宙論',
        'Notebooks Ø 意識と倫理',
        'Notebooks Ø 応用',
    ],
    notebooks_desc=[
        ('エディションは論証を全体として構築する。ノートブックはそれを分解し、すべての部品をテーブルに並べる。',
         'Editionsは論証を全体として構築する。Notebooksはそれを分解し、すべての部品をテーブルに並べる。'),
    ],
)

# ----------------- KOREAN -----------------
LANGS['ko'] = dict(
    rosin_h3=('로진', 'Rosin'),
    rosin_old_links=[
        '로진 — 산문',
        '로진 — 대화',
        '로진 — 은유',
        '로진 — 동요',
        '로진 — 증명',
    ],
    rosin_new_links=[
        'Rosin Ø 산문',
        'Rosin Ø 대화',
        'Rosin Ø 은유',
        'Rosin Ø 동요',
        'Rosin Ø 증명',
    ],
    rosin_desc=[],
    editions_h3=('에디션', 'Editions'),
    editions_old_links=[
        '에디션 — 산문',
        '에디션 — 대화',
        '에디션 — 은유',
        '에디션 — 동요',
        '에디션 — 증명',
    ],
    editions_new_links=[
        'Editions Ø 산문',
        'Editions Ø 대화',
        'Editions Ø 은유',
        'Editions Ø 동요',
        'Editions Ø 증명',
    ],
    editions_desc=[
        ('로진이 그것을 촬영한다. 노트북이 그것을 색인한다. 기록이 그것이 어떻게 만들어졌는지를 기록한다. 에디션이 만들어진 것 자체다.',
         'Rosin이 그것을 촬영한다. Notebooks이 그것을 색인한다. 기록이 그것이 어떻게 만들어졌는지를 기록한다. Editions이 만들어진 것 자체다.'),
    ],
    notebooks_h3=('노트북', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">노트북 Ø 산문 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">노트북 Ø 대화 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">노트북 Ø 은유 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">노트북 Ø 동요 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">노트북 Ø 증명 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø 산문 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 대화 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 은유 <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø 동요 <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 전제',
        'Ø.2 시공간',
        'Ø.3 양자역학',
        'Ø.4 힘과 상수',
        'Ø.5 입자와 물질',
        'Ø.6 우주론',
        'Ø.7 의식과 윤리',
        'Ø.8 응용',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø 전제',
        'Notebooks Ø 시공간',
        'Notebooks Ø 양자역학',
        'Notebooks Ø 힘과 상수',
        'Notebooks Ø 입자와 물질',
        'Notebooks Ø 우주론',
        'Notebooks Ø 의식과 윤리',
        'Notebooks Ø 응용',
    ],
    notebooks_desc=[
        ('에디션은 논증을 전체로 세운다. 노트북은 그것을 분해하고 모든 조각을 테이블 위에 펼친다.',
         'Editions은 논증을 전체로 세운다. Notebooks은 그것을 분해하고 모든 조각을 테이블 위에 펼친다.'),
    ],
)

# ----------------- HINDI -----------------
LANGS['hi'] = dict(
    rosin_h3=('रोज़िन', 'Rosin'),
    rosin_old_links=[
        'रोज़िन — गद्य',
        'रोज़िन — संवाद',
        'रोज़िन — रूपक',
        'रोज़िन — लोरी',
        'रोज़िन — प्रमाण',
    ],
    rosin_new_links=[
        'Rosin Ø गद्य',
        'Rosin Ø संवाद',
        'Rosin Ø रूपक',
        'Rosin Ø लोरी',
        'Rosin Ø प्रमाण',
    ],
    rosin_desc=[],
    editions_h3=('संस्करण', 'Editions'),
    editions_old_links=[
        'संस्करण — गद्य',
        'संस्करण — संवाद',
        'संस्करण — रूपक',
        'संस्करण — लोरी',
        'संस्करण — प्रमाण',
    ],
    editions_new_links=[
        'Editions Ø गद्य',
        'Editions Ø संवाद',
        'Editions Ø रूपक',
        'Editions Ø लोरी',
        'Editions Ø प्रमाण',
    ],
    editions_desc=[
        ('रोज़िन उनकी तस्वीरें लेता है। नोटबुक उन्हें सूचीबद्ध करती हैं। अभिलेख दर्ज करते हैं कि वे कैसे बनीं। संस्करण वही हैं जो बनाया गया।',
         'Rosin उनकी तस्वीरें लेता है। Notebooks उन्हें सूचीबद्ध करती हैं। अभिलेख दर्ज करते हैं कि वे कैसे बनीं। Editions वही हैं जो बनाया गया।'),
    ],
    notebooks_h3=('नोटबुक', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">नोटबुक Ø गद्य <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">नोटबुक Ø संवाद <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">नोटबुक Ø रूपक <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">नोटबुक Ø लोरी <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">नोटबुक Ø प्रमाण <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø गद्य <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø संवाद <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø रूपक <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø लोरी <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 आधारवाक्य',
        'Ø.2 दिक्काल',
        'Ø.3 क्वांटम यांत्रिकी',
        'Ø.4 बल और स्थिरांक',
        'Ø.5 कण और पदार्थ',
        'Ø.6 ब्रह्मांड विज्ञान',
        'Ø.7 चेतना और नैतिकता',
        'Ø.8 अनुप्रयोग',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø आधारवाक्य',
        'Notebooks Ø दिक्काल',
        'Notebooks Ø क्वांटम यांत्रिकी',
        'Notebooks Ø बल और स्थिरांक',
        'Notebooks Ø कण और पदार्थ',
        'Notebooks Ø ब्रह्मांड विज्ञान',
        'Notebooks Ø चेतना और नैतिकता',
        'Notebooks Ø अनुप्रयोग',
    ],
    notebooks_desc=[
        ('संस्करण तर्क को समग्र रूप में बनाते हैं। नोटबुक उसे खोलती हैं और हर टुकड़ा मेज़ पर रख देती हैं।',
         'Editions तर्क को समग्र रूप में बनाते हैं। Notebooks उसे खोलती हैं और हर टुकड़ा मेज़ पर रख देती हैं।'),
    ],
)

# ----------------- ARABIC -----------------
LANGS['ar'] = dict(
    rosin_h3=('الصنوبرية', 'Rosin'),
    rosin_old_links=[
        'الصمغ — نثر',
        'الصمغ — حوار',
        'الصمغ — استعارة',
        'الصمغ — أنشودة أطفال',
        'الصمغ — براهين',
    ],
    rosin_new_links=[
        'Rosin Ø نثر',
        'Rosin Ø حوار',
        'Rosin Ø استعارة',
        'Rosin Ø أنشودة أطفال',
        'Rosin Ø براهين',
    ],
    rosin_desc=[],
    editions_h3=('الطبعات', 'Editions'),
    editions_old_links=[
        'الطبعات — نثر',
        'الطبعات — حوار',
        'الطبعات — استعارة',
        'الطبعات — أنشودة أطفال',
        'الطبعات — براهين',
    ],
    editions_new_links=[
        'Editions Ø نثر',
        'Editions Ø حوار',
        'Editions Ø استعارة',
        'Editions Ø أنشودة أطفال',
        'Editions Ø براهين',
    ],
    editions_desc=[
        ('الصنوبرية تصوّرها. الدفاتر تفهرسها. السجلات توثّق كيف صُنعت. الطبعات هي ما صُنع.',
         'Rosin تصوّرها. Notebooks تفهرسها. السجلات توثّق كيف صُنعت. Editions هي ما صُنع.'),
    ],
    notebooks_h3=('الدفاتر', 'Notebooks'),
    notebooks_old_voice_lines=[
        '<li><a href="#">الدفاتر Ø نثر <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">الدفاتر Ø حوار <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">الدفاتر Ø استعارة <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">الدفاتر Ø أنشودة أطفال <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">الدفاتر Ø براهين <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_new_voice_lines=[
        '<li><a href="#">Notebooks Ø نثر <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø حوار <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø استعارة <span class="fmt">PDF</span></a></li>',
        '<li><a href="#">Notebooks Ø أنشودة أطفال <span class="fmt">PDF</span></a></li>',
    ],
    notebooks_old_subjects=[
        'Ø.1 المقدّمة',
        'Ø.2 الزمكان',
        'Ø.3 ميكانيكا الكمّ',
        'Ø.4 القوى والثوابت',
        'Ø.5 الجسيمات والمادة',
        'Ø.6 علم الكونيات',
        'Ø.7 الوعي والأخلاق',
        'Ø.8 التطبيقات',
    ],
    notebooks_new_subjects=[
        'Notebooks Ø المقدّمة',
        'Notebooks Ø الزمكان',
        'Notebooks Ø ميكانيكا الكمّ',
        'Notebooks Ø القوى والثوابت',
        'Notebooks Ø الجسيمات والمادة',
        'Notebooks Ø علم الكونيات',
        'Notebooks Ø الوعي والأخلاق',
        'Notebooks Ø التطبيقات',
    ],
    notebooks_desc=[
        ('الطبعات تبني الحجة كاملة. الدفاتر تفكّكها وتضع كل قطعة على الطاولة.',
         'Editions تبني الحجة كاملة. Notebooks تفكّكها وتضع كل قطعة على الطاولة.'),
    ],
)


def patch_file(lang_code, cfg):
    path = os.path.join(ROOT, lang_code, 'index.html')
    with io.open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    original = text

    # H3 replacements (use full <h3 class="cat-title">OLD</h3>)
    for old, new in [cfg['rosin_h3'], cfg['editions_h3'], cfg['notebooks_h3']]:
        old_h3 = f'<h3 class="cat-title">{old}</h3>'
        new_h3 = f'<h3 class="cat-title">{new}</h3>'
        if old_h3 not in text:
            print(f"WARN [{lang_code}] missing h3: {old_h3}")
        text = text.replace(old_h3, new_h3, 1)

    # Rosin links: 5
    for old, new in zip(cfg['rosin_old_links'], cfg['rosin_new_links']):
        old_li = f'<li><a href="#">{old} <span class="fmt">PDF</span></a></li>'
        new_li = f'<li><a href="#">{new} <span class="fmt">PDF</span></a></li>'
        if old_li not in text:
            print(f"WARN [{lang_code}] missing rosin link: {old_li}")
        text = text.replace(old_li, new_li, 1)

    # Rosin desc replacements
    for old, new in cfg['rosin_desc']:
        if old not in text:
            print(f"WARN [{lang_code}] missing rosin desc: {old[:60]}")
        text = text.replace(old, new)

    # Editions links: 5
    for old, new in zip(cfg['editions_old_links'], cfg['editions_new_links']):
        old_li = f'<li><a href="#">{old} <span class="fmt">PDF</span></a></li>'
        new_li = f'<li><a href="#">{new} <span class="fmt">PDF</span></a></li>'
        if old_li not in text:
            print(f"WARN [{lang_code}] missing editions link: {old_li}")
        text = text.replace(old_li, new_li, 1)

    # Editions desc
    for old, new in cfg['editions_desc']:
        if old not in text:
            print(f"WARN [{lang_code}] missing editions desc: {old[:60]}")
        text = text.replace(old, new)

    # Notebooks voice lines: replace first 4 in place, remove the 5th (proofs)
    olds = cfg['notebooks_old_voice_lines']
    news = cfg['notebooks_new_voice_lines']
    for i in range(4):
        if olds[i] not in text:
            print(f"WARN [{lang_code}] missing notebooks voice line {i}: {olds[i]}")
        text = text.replace(olds[i], news[i], 1)
    # Remove proofs line (and its trailing newline + indent)
    proofs_line = olds[4]
    # Remove the line including leading spaces and newline
    import re
    pattern = r'[ \t]*' + re.escape(proofs_line) + r'\n'
    new_text, n = re.subn(pattern, '', text, count=1)
    if n == 0:
        print(f"WARN [{lang_code}] could not delete proofs line")
    text = new_text

    # Notebooks subjects: 8
    for old, new in zip(cfg['notebooks_old_subjects'], cfg['notebooks_new_subjects']):
        old_li = f'<li><a href="#">{old} <span class="fmt">PDF</span></a></li>'
        new_li = f'<li><a href="#">{new} <span class="fmt">PDF</span></a></li>'
        if old_li not in text:
            print(f"WARN [{lang_code}] missing subject: {old_li}")
        text = text.replace(old_li, new_li, 1)

    # Notebooks desc
    for old, new in cfg['notebooks_desc']:
        if old not in text:
            print(f"WARN [{lang_code}] missing notebooks desc: {old[:60]}")
        text = text.replace(old, new)

    if text == original:
        print(f"NO CHANGE [{lang_code}]")
    else:
        with io.open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"OK [{lang_code}]")


def main():
    order = ['ar', 'de', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh']
    for code in order:
        if code in LANGS:
            patch_file(code, LANGS[code])
        else:
            print(f"SKIP [{code}] no config")


if __name__ == '__main__':
    main()
