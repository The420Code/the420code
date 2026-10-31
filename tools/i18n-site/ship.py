# -*- coding: utf-8 -*-
"""Put a language on the site: merge, the gate, build, verify, commit. One command per language.

    python ship.py <lang> [<lang> ...]        e.g. python ship.py es fr

For each language, in order: merge.py (patches and reviews into i18n/<lang>.json), qa.py (the gate; a failure
stops that language and names the segments), build.py (the pages, llms.txt, the sitemap, the rules), then
verify_i18n.py and tools/check_site.py on the whole site. If everything passes, the change is committed on the
current branch, signed G. Pushing is a separate, deliberate step:

    git push origin HEAD:main        (a push to main publishes the site)

A language already on the site is rebuilt from its memory, so a later patch or review changes the live words
only after this is run again.
"""
import os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import REPO, LANGS, ENGLISH_NAME

HERE = os.path.dirname(os.path.abspath(__file__))


def run(*args, check=True):
    print(">", " ".join(args))
    r = subprocess.call(list(args), cwd=REPO, env=dict(os.environ, PYTHONUTF8="1"))
    if check and r != 0: raise SystemExit("failed: %s" % " ".join(args))
    return r


def main():
    langs = [l for l in sys.argv[1:] if l in LANGS]
    if not langs: raise SystemExit("which language? one of " + " ".join(LANGS))
    for l in langs:
        run(sys.executable, os.path.join(HERE, "merge.py"), l)
        run(sys.executable, os.path.join(HERE, "qa.py"), l)
    run(sys.executable, os.path.join(HERE, "build.py"), *langs)
    run(sys.executable, os.path.join(HERE, "verify_i18n.py"))
    run(sys.executable, os.path.join(REPO, "tools", "check_site.py"))
    run("git", "add", "site", "i18n", "netlify.toml", "netlify", "tools/i18n")
    names = ", ".join(ENGLISH_NAME[l] for l in langs)
    msg = ("whybekind.global in %s: every page, in the language's own folder (10 October 2026)\n\n"
           "Built by tools/i18n from the English pages and i18n/<lang>.json. The menu and the footer carry the languages "
           "built so far; every page has its hreflang links.\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>") % names
    run("git", "-c", "user.name=G", "-c", "user.email=g@studiog.global", "commit", "-q", "-m", msg)
    run("git", "log", "--oneline", "-1")
    print("\nshipped on this branch:", names, "\nto publish: git push origin HEAD:main")


if __name__ == "__main__":
    main()
