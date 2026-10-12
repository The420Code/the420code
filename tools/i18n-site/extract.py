# -*- coding: utf-8 -*-
"""Take every English page of the420code.org apart into a template and its text.

A page is read as a stream of tags and text. Every run of text between two block-level tags is one segment; the
inline tags inside it (a, b, span, br, svg, ...) become numbered tokens such as ⟦a1⟧...⟦/a1⟧ and ⟦br2⟧, so a
translator moves words around the tokens and never touches a tag. Attributes that carry words (aria-label, title,
the meta descriptions) and the strings inside the JSON-LD are segments too. The same text on many pages (the
menu, the footer, the book titles) is ONE segment, so it is translated once and reads the same everywhere.

    python extract.py            writes WORK/en/templates.json, instances.json, segments.json
    python extract.py --check    also rebuilds every English page from its template and compares byte for byte

The segment's key is its text with the tokens, whitespace collapsed. The templates hold \\x00iid\\x00 placeholders,
one per instance; an instance names its segment key and the tags its tokens stand for.
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SITE, WORK, en_pages

BLOCK = set("""html head body main header footer nav section article aside div ul ol li p h1 h2 h3 h4 h5 h6 details
summary figure figcaption blockquote pre table thead tbody tfoot tr td th dl dt dd form fieldset legend label button
title video audio hr script style noscript template iframe source link meta base track picture img""".split())
# attributes whose value is read aloud or shown: translated
TEXT_ATTRS = ("aria-label", "title", "alt", "placeholder", "data-copied")
META_NAMES = {"description", "twitter:title", "twitter:description", "twitter:image:alt"}
META_PROPS = {"og:title", "og:description", "og:image:alt", "og:site_name"}
JSONLD_KEYS = {"name", "description", "alternateName", "headline", "caption", "jobTitle", "text"}
VOID = {"br", "wbr", "img", "source", "track", "link", "meta", "hr", "input", "use", "path"}

TAG = re.compile(r"<!--.*?-->|<!doctype[^>]*>|<\?[^>]*>|</?[a-zA-Z][a-zA-Z0-9-]*(?:\s+[^<>]*?)?/?>", re.S)
PH = "\x00%s\x00"
TOKEN = re.compile(r"⟦(/?[a-z0-9-]+)⟧")


def tagname(tag):
    m = re.match(r"</?([a-zA-Z][a-zA-Z0-9-]*)", tag)
    return m.group(1).lower() if m else None


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


class Page:
    def __init__(self, path, html):
        self.path, self.html = path, html
        self.instances = {}          # iid -> {"key","kind","tags":{tok:[open,close]}}
        self.n = 0
        self.segments = {}           # key -> kind  (first kind seen)

    def iid(self):
        self.n += 1
        return "i%d" % self.n

    def add(self, text, kind, tags=None):
        key = norm(text)
        i = self.iid()
        self.instances[i] = {"key": key, "kind": kind, "tags": tags or {}}
        if text != key: self.instances[i]["raw"] = text          # the English keeps its own line breaks
        self.segments.setdefault(key, kind)
        return PH % i

    # 1. attributes with words, anywhere on the page (including inside tags that will become tokens)
    def attrs(self, html):
        def one(m):
            tag = m.group(0)
            if tag.startswith("<!") or tag.startswith("</"): return tag
            name = tagname(tag)
            if name == "meta":
                nm = re.search(r'\bname="([^"]*)"', tag); pr = re.search(r'\bproperty="([^"]*)"', tag)
                ok = (nm and nm.group(1) in META_NAMES) or (pr and pr.group(1) in META_PROPS)
                if not ok: return tag
                return re.sub(r'(\bcontent=")([^"]+)(")',
                              lambda a: a.group(1) + self.add(a.group(2), "meta:" + (nm or pr).group(1)) + a.group(3), tag, count=1)
            for at in TEXT_ATTRS:
                tag = re.sub(r'(\s%s=")([^"]+)(")' % at,
                             lambda a: a.group(1) + self.add(a.group(2), "attr:" + at) + a.group(3), tag, count=1)
            return tag
        return TAG.sub(one, html)

    # 2. the JSON-LD: its names and descriptions
    def jsonld(self, html):
        def one(m):
            raw = m.group(2)
            try: data = json.loads(raw)
            except Exception: return m.group(0)
            found = []
            def walk(o):
                if isinstance(o, dict):
                    for k, v in o.items():
                        if k in JSONLD_KEYS and isinstance(v, str) and not v.startswith("http"): found.append(v)
                        else: walk(v)
                elif isinstance(o, list):
                    for v in o: walk(v)
            walk(data)
            for v in dict.fromkeys(found):
                lit = json.dumps(v, ensure_ascii=False)[1:-1]
                if lit not in raw: raise SystemExit("JSON-LD literal not found verbatim: %r in %s" % (v, self.path))
                raw = raw.replace('"%s"' % lit, '"%s"' % self.add(v, "jsonld"))
            return m.group(1) + raw + m.group(3)
        return re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', one, html, flags=re.S)

    # 3. the text between block tags, inline tags tokenised
    def blocks(self, html):
        out, pos = [], 0
        chunk = []              # pieces of the current run: ("t", text) | ("tag", tagstring, name, kind)
        skip = None             # inside <svg>: its insides ride along, then collapse to one token
        def flush():
            if not chunk: return
            if not any(p[0] == "t" and p[1].strip() for p in chunk):
                out.extend(p[1] for p in chunk); chunk.clear(); return
            # leading and trailing whitespace stay in the template
            lead = trail = ""
            if chunk[0][0] == "t":
                s = chunk[0][1]; lead = s[:len(s) - len(s.lstrip())]; chunk[0] = ("t", s.lstrip())
            if chunk[-1][0] == "t":
                s = chunk[-1][1]; trail = s[len(s.rstrip()):]; chunk[-1] = ("t", s.rstrip())
            toks, text, stack, n = {}, [], [], 0
            for p in chunk:
                if p[0] == "t": text.append(p[1]); continue
                tag, name, kind = p[1], p[2], p[3]
                if kind == "open":
                    n += 1; tok = "%s%d" % (name, n); stack.append((name, tok)); toks[tok] = [tag, None]
                    text.append("⟦%s⟧" % tok)
                elif kind == "close":
                    if not any(nm == name for nm, _ in stack):
                        # an inline tag that opened before this block began (a link round a heading): its close
                        # rides as a marker of its own
                        n += 1; tok = "x%s%d" % (name, n); toks[tok] = [tag, None]; text.append("⟦%s⟧" % tok)
                        continue
                    while stack and stack[-1][0] != name: stack.pop()
                    _, tok = stack.pop(); toks[tok][1] = tag; text.append("⟦/%s⟧" % tok)
                else:
                    n += 1; tok = "%s%d" % (name, n); toks[tok] = [tag, None]; text.append("⟦%s⟧" % tok)
            for name_, tok in stack:
                # an inline tag that closes after this block ends: its opening rides as a marker of its own
                k = "".join(text).index("⟦%s⟧" % tok)
                joined = "".join(text)
                text = [joined[:k] + "⟦x%s⟧" % tok + joined[k + len("⟦%s⟧" % tok):]]
                toks["x" + tok] = toks.pop(tok)
            out.append(lead + self.add("".join(text), "block", toks) + trail)
            chunk.clear()
        for m in TAG.finditer(html):
            if m.start() < pos: continue          # inside a script or a style already taken whole
            if m.start() > pos: chunk.append(("t", html[pos:m.start()]))
            tag = m.group(0); pos = m.end()
            name = tagname(tag)
            if skip:
                chunk.append(("t", tag))
                if tag.startswith("</") and name == skip:
                    skip = None
                    j = len(chunk) - 1
                    while chunk[j] != ("svgstart",): j -= 1
                    whole = "".join(p[1] for p in chunk[j + 1:]); del chunk[j:]
                    chunk.append(("tag", whole, "svg", "void"))
                continue
            if tag.startswith("<!") or tag.startswith("<?"):          # comments, doctype: a boundary, kept
                flush(); out.append(tag); continue
            if name == "svg" and not tag.startswith("</"):
                chunk.append(("svgstart",)); chunk.append(("t", tag)); skip = "svg"; continue
            if name in BLOCK:
                flush(); out.append(tag)
                if name in ("script", "style") and not tag.startswith("</"):
                    end = html.find("</%s>" % name, pos)
                    out.append(html[pos:end]); pos = end
                continue
            kind = "close" if tag.startswith("</") else ("void" if (name in VOID or tag.endswith("/>")) else "open")
            chunk.append(("tag", tag, name, kind))
        if pos < len(html): chunk.append(("t", html[pos:]))
        flush()
        return "".join(out)

    def run(self):
        t = self.attrs(self.html)
        t = self.jsonld(t)
        t = self.blocks(t)
        self.template = t
        return self


def rebuild(template, instances, lookup):
    """Fill a template: lookup(key, instance) -> text with tokens; the tokens become the instance's tags."""
    def fill(m):
        inst = instances[m.group(1)]
        text = lookup(inst["key"], inst)
        tags = inst["tags"]
        if not tags: return text
        def tok(t):
            name = t.group(1)
            if name.startswith("/"): return tags[name[1:]][1]
            return tags[name][0]
        return TOKEN.sub(tok, text)
    out = template
    while "\x00" in out:          # an attribute inside a tokenised tag is a placeholder inside a placeholder
        out = re.sub("\x00(i\\d+)\x00", fill, out)
    return out


def extract_llms(text):
    """llms.txt line by line: a heading keeps its #, a quote its >, a list item its dash; URLs and blank lines stay."""
    inst, lines, n = {}, [], 0
    for line in text.split("\n"):
        m = re.match(r"^(#+ |> |- |\* )?(.*)$", line)
        pre, body = m.group(1) or "", m.group(2)
        if not body.strip() or re.fullmatch(r"https?://\S+", body.strip()):
            lines.append(line); continue
        n += 1; i = "i%d" % n
        inst[i] = {"key": norm(body), "kind": "txt", "tags": {}}
        if body != norm(body): inst[i]["raw"] = body
        lines.append(pre + PH % i)
    return "\n".join(lines), inst


def strip_builder(html):
    """Take off what build.py adds to an English page (the per-page language links), so the page reads as the source
    again. Safe on a page the builder never touched."""
    html = re.sub(r'\n<link rel="alternate" hreflang="[^"]+" href="[^"]+">(?=\n)', "", html) if "<!-- i18n-site -->" in html else html
    html = html.replace("<!-- i18n-site -->", "")
    return html


def main():
    check = "--check" in sys.argv
    os.makedirs(os.path.join(WORK, "en"), exist_ok=True)
    templates, instances, segments = {}, {}, {}
    for path in en_pages():
        html = strip_builder(io.open(os.path.join(SITE, path), encoding="utf-8", newline="").read())
        p = Page(path, html).run()
        templates[path] = p.template; instances[path] = p.instances
        for key, kind in p.segments.items():
            s = segments.setdefault(key, {"t": key, "k": kind, "pages": []})
            s["pages"].append(path)
        if check:
            back = rebuild(p.template, p.instances, lambda key, inst: inst.get("raw", key))
            if back != html:
                i = next(i for i in range(min(len(back), len(html))) if back[i] != html[i])
                raise SystemExit("%s does not rebuild: ...%r... vs ...%r..." % (path, back[i-80:i+80], html[i-80:i+80]))
    txt = io.open(os.path.join(SITE, "llms.txt"), encoding="utf-8", newline="").read()
    tpl, inst = extract_llms(txt)
    templates["llms.txt"] = tpl; instances["llms.txt"] = inst
    for i, v in inst.items():
        segments.setdefault(v["key"], {"t": v["key"], "k": "txt", "pages": []})["pages"].append("llms.txt")
    if check:
        back = rebuild(tpl, inst, lambda key, inst: inst.get("raw", key))
        assert back == txt, "llms.txt does not rebuild"
    for name, obj in (("templates", templates), ("instances", instances), ("segments", segments)):
        json.dump(obj, io.open(os.path.join(WORK, "en", name + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    words = sum(len(TOKEN.sub(" ", k).split()) for k in segments)
    inst_n = sum(len(v) for v in instances.values())
    print("%d pages + llms.txt: %d instances, %d unique segments, %d words to translate%s"
          % (len(templates) - 1, inst_n, len(segments), words, "; every page rebuilds" if check else ""))
    kinds = {}
    for s in segments.values():
        k = s["k"].split(":")[0]; kinds[k] = kinds.get(k, 0) + 1
    print("kinds:", kinds)


if __name__ == "__main__":
    main()
