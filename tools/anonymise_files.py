# -*- coding: utf-8 -*-
"""The author is G, everywhere, in what a file says of itself as much as in its text (the anonymity rule).

    python tools/anonymise_files.py --check        list every published file whose hidden properties carry a name
    python tools/anonymise_files.py FILE ...       put "G" in its place

A Word file: the author fields (and any other part that carries the name) are rewritten inside the package; the
document's text, styles and images are byte for byte the same. A PDF: the name in the document information and in
its XMP metadata is replaced by "G" at exactly the same length, so every other byte, and every offset the file
keeps, is unchanged. A file whose hash is published as its source of record is never changed here: that is the
author's ruling to make, with a dated note beside it.
"""
import io, os, re, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NAME = re.compile(rb"Gerhard\s+van\s+Niekerk|Gerhard|van\s+Niekerk|Niekerk", re.I)


def docx(path):
    zin = zipfile.ZipFile(path)
    items = [(i, zin.read(i.filename)) for i in zin.infolist()]
    zin.close()
    changed = False
    out = []
    for info, data in items:
        if NAME.search(data) and info.filename.endswith((".xml", ".rels")):
            data = NAME.sub(b"G", data)
            changed = True
        out.append((info, data))
    if not changed:
        return False
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for info, data in out:
            z.writestr(info, data, compress_type=info.compress_type)
    open(path, "wb").write(buf.getvalue())
    return True


def pdf(path):
    b = open(path, "rb").read()
    def same_len(m):
        s = m.group(0)
        if s.startswith(b"("):                                   # the document information: (G) and spaces after it
            return b"(G)" + b" " * (len(s) - 3)
        inner = re.match(rb"(<[^>]+>)(.*?)(</[^>]+>)", s, re.S)  # XMP: <rdf:li>G</rdf:li> and spaces after it
        if inner:
            t = inner.group(1) + b"G" + inner.group(3)
            return t + b" " * (len(s) - len(t))
        return s
    # Only the entries themselves: "/Author (...)" with plain text inside, and an XMP element with text inside, each
    # at most a few hundred bytes, so a match can never reach into a stream. (14 October 2026: a looser pattern, a
    # bracket anywhere before the name, once overwrote compressed data in two files; both were restored.)
    c = re.sub(rb"(?<=/Author)\((?:[^()\\\r\n]|\\.){0,200}\)",
               lambda m: same_len(m) if re.search(rb"Gerhard|Niekerk", m.group(0), re.I) else m.group(0), b)
    c = re.sub(rb"(?<=/Author )\((?:[^()\\\r\n]|\\.){0,200}\)",
               lambda m: same_len(m) if re.search(rb"Gerhard|Niekerk", m.group(0), re.I) else m.group(0), c)
    # the author written in hex, UTF-16 (LibreOffice writes it so): <FEFF0047...> -> <FEFF0047> and spaces after it
    def hex_entry(m):
        h = m.group(1)
        try:
            text = bytes.fromhex(h.decode()).decode("utf-16")
        except Exception:
            return m.group(0)
        if not re.search("Gerhard|Niekerk", text, re.I):
            return m.group(0)
        t = b"<FEFF0047>"
        return t + b" " * (len(m.group(0)) - len(t))
    c = re.sub(rb"(?<=/Author)<([0-9A-Fa-f]{4,800})>", hex_entry, c)
    c = re.sub(rb"(?<=/Author )<([0-9A-Fa-f]{4,800})>", hex_entry, c)
    c = re.sub(rb"<rdf:li[^<>]{0,40}>[^<]{0,200}(?:Gerhard|Niekerk)[^<]{0,200}</rdf:li>", same_len, c, flags=re.I)
    c = re.sub(rb"<(dc:creator|xmp:Author|pdf:Author)>[^<]{0,200}(?:Gerhard|Niekerk)[^<]{0,200}</\1>", same_len, c, flags=re.I)
    assert len(c) == len(b), path
    changed = sum(1 for x, y in zip(b, c) if x != y)
    assert changed <= 400, "%s: %d bytes would change; only the author entries may" % (path, changed)
    if c == b:
        return False
    open(path, "wb").write(c)
    return True


def carries(path):
    if path.lower().endswith(".docx"):
        try:
            z = zipfile.ZipFile(path)
            return any(NAME.search(z.read(n)) for n in z.namelist() if n.endswith((".xml", ".rels")))
        except Exception:
            return False
    if path.lower().endswith(".pdf"):
        b = open(path, "rb").read()
        if re.search(rb"Gerhard|Niekerk", b, re.I):
            return True
        for h in re.findall(rb"/Author\s*<([0-9A-Fa-f]{4,800})>", b):     # the author in hex, UTF-16
            try:
                if re.search("Gerhard|Niekerk", bytes.fromhex(h.decode()).decode("utf-16"), re.I):
                    return True
            except Exception:
                pass
        return False
    return False


if __name__ == "__main__":
    os.chdir(REPO)
    if "--check" in sys.argv:
        files = [f for f in subprocess.run(["git", "ls-files", "*.docx", "*.pdf"], capture_output=True, text=True,
                                           encoding="utf-8").stdout.split("\n") if f and os.path.exists(f)]
        found = [f for f in files if carries(f)]
        for f in found:
            print("  ", f)
        print(len(found), "published files carry the name")
        sys.exit(1 if found else 0)
    for f in sys.argv[1:]:
        done = docx(f) if f.lower().endswith(".docx") else pdf(f)
        print("G in its place:" if done else "nothing to change:", f, "| still carries it" if carries(f) else "")
