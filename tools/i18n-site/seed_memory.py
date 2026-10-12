# -*- coding: utf-8 -*-
"""Bring in what is already translated: whybekind.org carries the same five books (the Five Doors) and many of the
same lines, translated into the same twelve languages and published (github.com/The420Code/whybekind, i18n/<lang>.json).
Where a segment of this site is exactly the same English (the same words, the same markup tokens), its translation
is taken over as it stands, marked src "whybekind". The gate checks it like every other translation.

    python seed_memory.py <lang>

Left out, to be translated afresh for this site: any translation that says "Sollbruchstelle" (this site keeps "Kill
Switch", as its own German edition prints it). A translation already in this site's memory is never replaced.
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, LANGS
from batchize import load_memory
from merge import save_memory

WBK = os.environ.get("WBK_REPO", r"C:\Users\info\whybekind")
SKIP = {"de": ["ollbruch"]}


def main():
    lang = sys.argv[1]
    assert lang in LANGS
    en = json.load(io.open(os.path.join(WORK, "en", "segments.json"), encoding="utf-8"))
    wbk = json.load(io.open(os.path.join(WBK, "i18n", lang + ".json"), encoding="utf-8"))
    mem = load_memory(lang)
    n = skipped = 0
    for key in en:
        if key in mem or key not in wbk or not wbk[key].get("t"):
            continue
        t = wbk[key]["t"]
        if any(w in t for w in SKIP.get(lang, [])):
            skipped += 1
            continue
        mem[key] = {"t": t, "src": "whybekind"}
        n += 1
    save_memory(lang, mem)
    print(lang, n, "translations taken over from whybekind.org;", skipped, "left to translate afresh")


if __name__ == "__main__":
    main()
