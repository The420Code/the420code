# -*- coding: utf-8 -*-
"""What the420code.org serves carries the work's words, not the notes of how it was made (G, 14 October 2026: "strip
all meta data from the site and no mention of our private discussions" - "please clean the420code.org as well").

    python tools/scrub_public.py            scrub in place
    python tools/scrub_public.py --check    report what is left; exit 1 if anything is

Taken out:
- every comment inside the pages' own <style> and <script> blocks (the structured data is left alone), read with a
  scanner that knows strings and regular expressions; every script touched is parsed by node afterwards;
- every comment in the site's own stylesheets and scripts (five-doors/reader.*, models/reader.*);
- an HTML comment that carries a date, a ruling or a quotation. The bare section labels (<!-- NAV -->, the rulers)
  stay: they say nothing, and an older tool (update_all_langs.py) finds its place by them.
Left exactly as they are, because they are the public record and are sealed by their hashes and their commits: the
frozen predictions' documents (prereg/doc/ in English), the freezes (freezes/), the proofs' instrument notes, the
verifiers (verify.py, verify.browser.js, prereg/verify.js). Working folders are not served at all: netlify.toml
answers 404 for them, so nothing in them reaches a reader.

Run it after any builder that writes pages (the libraries' build_site.py, the editions, tools/i18n-site/build.py).
"""
import io, os, re, subprocess, sys, tempfile
sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SKIP_PREFIX = ("freezes/", "node_modules/", ".claude/", "museum/", "tools/")
FROZEN = re.compile(r"^prereg/doc/[^/]+\.html$")          # the English frozen documents: never edited
FILES = ["five-doors/reader.css", "five-doors/reader.js", "models/reader.css", "models/reader.js"]
PRIVATE = re.compile(r"\b(19|20)\d\d\b|\(G\b|\bG[,:]|\bbrief\b|\bdesk\b|\bWC\b|[\"“”]", re.I)


def css(t):
    out, i, n, q = [], 0, len(t), None
    while i < n:
        c = t[i]
        if q:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(t[i + 1]); i += 2; continue
            if c == q:
                q = None
            i += 1; continue
        if c in "\"'":
            q = c; out.append(c); i += 1; continue
        if t.startswith("/*", i):
            j = t.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        out.append(c); i += 1
    return tidy("".join(out))


REGEX_AFTER = set("(,=:[!&|?{};+-*%<>~^")
REGEX_WORDS = ("return", "typeof", "case", "do", "else", "in", "of", "void", "delete", "new", "throw")


def js(t):
    out, i, n = [], 0, len(t)
    while i < n:
        c = t[i]
        if c in "\"'`":
            j = i + 1
            while j < n:
                if t[j] == "\\":
                    j += 2; continue
                if t[j] == c:
                    break
                j += 1
            out.append(t[i:j + 1]); i = j + 1; continue
        if t.startswith("//", i) and not (i > 0 and t[i - 1] == ":"):
            j = t.find("\n", i)
            i = n if j < 0 else j
            continue
        if t.startswith("/*", i):
            j = t.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        if c == "/":
            p = "".join(out[-40:]).rstrip()
            if not p or p[-1] in REGEX_AFTER or re.search(r"\b(%s)$" % "|".join(REGEX_WORDS), p):
                j, cls = i + 1, False
                while j < n:
                    if t[j] == "\\":
                        j += 2; continue
                    if t[j] == "[":
                        cls = True
                    elif t[j] == "]":
                        cls = False
                    elif t[j] == "/" and not cls:
                        break
                    elif t[j] == "\n":
                        break
                    j += 1
                k = j + 1
                while k < n and t[k].isalpha():
                    k += 1
                out.append(t[i:k]); i = k; continue
        out.append(c); i += 1
    return tidy("".join(out))


def tidy(t):
    nl = "\r\n" if "\r\n" in t else "\n"
    lines = [l.rstrip() for l in t.replace("\r\n", "\n").split("\n")]
    out = []
    for l in lines:
        if l == "" and out and out[-1] == "":
            continue
        out.append(l)
    return nl.join(out)


def page(t, scripts):
    parts = re.split(r"(<script\b.*?</script>|<style\b.*?</style>)", t, flags=re.S | re.I)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"[ \t]*<!--(.*?)-->[ \t]*(\r?\n)?",
                          lambda m: "" if PRIVATE.search(m.group(1)) else m.group(0), parts[i], flags=re.S)
    for i in range(1, len(parts), 2):
        m = re.match(r"(<(script|style)\b[^>]*>)(.*)(</\2>)$", parts[i], flags=re.S | re.I)
        if not m or "application/ld+json" in m.group(1) or not m.group(3).strip():
            continue
        if m.group(2).lower() == "script":
            body = js(m.group(3))
            if body != m.group(3):
                scripts.append(body)
        else:
            body = css(m.group(3))
        parts[i] = m.group(1) + body + m.group(4)
    return "".join(parts)


def pages():
    out = subprocess.run(["git", "ls-files", "*.html"], cwd=REPO, capture_output=True, text=True, encoding="utf-8").stdout.split("\n")
    return [p for p in out if p and not p.startswith(SKIP_PREFIX) and not FROZEN.match(p)]


def node_ok(src):
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(src)
        name = f.name
    r = subprocess.run(["node", "--check", name], capture_output=True, text=True)
    os.unlink(name)
    return r.returncode == 0, r.stderr[:300]


def run(check):
    changed, scripts = [], []
    for p in pages():
        f = os.path.join(REPO, p)
        t = io.open(f, encoding="utf-8", newline="").read()
        u = page(t, scripts)
        if u != t:
            changed.append(p)
            if not check:
                io.open(f, "w", encoding="utf-8", newline="").write(u)
    for p in FILES:
        f = os.path.join(REPO, p)
        t = io.open(f, encoding="utf-8", newline="").read()
        u = css(t) if p.endswith(".css") else js(t)
        if u != t:
            changed.append(p)
            if p.endswith(".js"):
                scripts.append(u)
            if not check:
                io.open(f, "w", encoding="utf-8", newline="").write(u)
    bad = [e for ok, e in (node_ok(s) for s in dict.fromkeys(scripts)) if not ok]
    return changed, bad


if __name__ == "__main__":
    check = "--check" in sys.argv
    changed, bad = run(check)
    print(len(changed), "files", "to scrub" if check else "scrubbed", ";", len(bad), "scripts that would not parse")
    for e in bad[:5]:
        print("  ", e)
    if bad:
        sys.exit(2)
    sys.exit(1 if (check and changed) else 0)
