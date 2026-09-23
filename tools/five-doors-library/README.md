# The Five Doors online library — bundle v11

23 September 2026. Five books, ninety-eight pages, one stylesheet. Supersedes v1 to v10.

Read INSTALL.md first. It has the paths, the snippet, and the checks before deploy. WALL_UPDATE.md has the part that is not the library: AP31's republish and the two registry entries.

`source/` carries the text the pages are generated from, and the generator. The HTML is disposable; the text files are the artefact. Edit the text, rebuild, redeploy.

    source/illusion/          The Illusion of the Other — the original, in full, no short edition
    source/bar/               Being After Religion — short edition v1.1
    source/antichristos/      Antichristos — short edition v1.1
    source/corridor/          The Relationship Corridor — short edition v1.1
    source/interior/          The Interior 2.0.5 — the book's own text, as typeset
    source/interior_site/     the same text split into chapters for the generator (made by split_interior_site.py)
    source/reader/            the generator and the chapter one-lines

    site-root/The_Interior.pdf   The Interior 2.0.5, the printed book, 270 pages
    site-root/AP31_The_Alignment.pdf   AP31 with its dated notes of 23 September 2026
    site-root/proofs/instruments/AP31/   the instruments folder: dated copy, notes, the Debt 20 derivation, its script

Copyleft. Free. Forever.
