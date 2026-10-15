# -*- coding: utf-8 -*-
"""the420code.org in every language, the whole English site word for word: what every tool here shares.

G, 12 October 2026: "get the translations on the420code.org done ... make sure the english website is translated in
full - word for word - in each language ... if anything on a translation is in dispute, the english is always the
version to default back to. English is canon - translations are translations. - one language at a time - lets start
with German". Text only.

A page's address in a language is the English address with the language in front: /de/killswitches/,
/de/five-doors/illusion/03-.../. Nothing else moves. The English pages are the front door, three-ways-of-being-sure,
and every page under the site's rooms (ORDER); the museum's work folder and the language folders are not English
pages.

The engine is the one that put whybekind.org into twelve languages (github.com/The420Code/whybekind, tools/i18n),
brought here and pointed at this site.
"""
import glob, os

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = REPO                                               # the site is the repository's root
MEMORY = os.path.join(REPO, "i18n", "site")               # the translation memory, one file per language (committed)
WORK = os.environ.get("T420_I18N_WORK", r"C:\Users\info\the420code-i18n-work")   # slices and patches (not committed)
HOST = "https://the420code.org"

LANGS = ["ar", "de", "es", "fr", "hi", "it", "ja", "ko", "nl", "pt", "ru", "zh"]
RTL = {"ar"}
NATIVE = {"en": "English", "ar": "العربية", "de": "Deutsch", "es": "Español", "fr": "Français", "hi": "हिंदी",
          "it": "Italiano", "ja": "日本語", "ko": "한국어", "nl": "Nederlands", "pt": "Português", "ru": "Русский",
          "zh": "中文"}
ENGLISH_NAME = {"ar": "Arabic", "de": "German", "es": "Spanish", "fr": "French", "hi": "Hindi", "it": "Italian",
                "ja": "Japanese", "ko": "Korean", "nl": "Dutch", "pt": "Portuguese", "ru": "Russian",
                "zh": "Chinese (Simplified)"}
# the rooms of the site, in reading order
ORDER = ["", "what-is-the-420-code", "axiom", "method", "one-awareness", "why-21-is-forced", "three-ways-of-being-sure",
         "physics", "prereg", "killswitches", "proofs", "notebooks", "glossary", "five-doors", "models", "films",
         "exhibition"]


def page_order(paths):
    def key(p):
        top = p.split("/")[0] if "/" in p else ("" if p == "index.html" else p.replace(".html", ""))
        return (ORDER.index(top) if top in ORDER else 99, p.count("/"), p)
    return sorted(paths, key=key)


def en_pages():
    """Every English page, as a path from the site's root (index.html, killswitches/index.html, ...). The sitemap is
    not the list: it leaves out eleven of the frozen predictions' documents under prereg/doc/, which /prereg/ links."""
    out = ["index.html"] + [f for f in os.listdir(SITE) if f.endswith(".html") and f != "index.html" and not f.startswith("yandex_")]
    for top in ORDER[1:]:
        if os.path.isdir(os.path.join(SITE, top)):
            out += [x.replace(os.sep, "/") for x in glob.glob(top + "/**/*.html", root_dir=SITE, recursive=True)]
    return page_order(dict.fromkeys(out))
