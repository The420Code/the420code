# -*- coding: utf-8 -*-
"""The site header's two drop-downs, as every page with the drop-down header carries it.

Rooms, then the language: a button showing the flag of the language being read, the
same kind of button as Rooms, with the same arrow, opening a list of all thirteen.
A flag takes the reader to the same page in that language wherever the page exists
in it -- a front door to a front door, a home page to a home page, the Proofs page to
that edition's proofs room -- so changing language never changes what is being read.

One row at every width: the logo and both buttons keep their size, and the door's name
wraps inside its own box when a phone is narrow, never splitting "The 420 Code".

Used by build.py for the twelve editions, and for the three English pages that carry
the header (home, front door, Proofs), so all twenty-seven are made by the same code."""

FLAGCDN = "https://flagcdn.com/w40/{}.png"

#          code  flag  the language's own name   "Language", in that language
LANGS = [("en", "gb", "English",    "Language"),
         ("es", "es", "Español",    "Idioma"),
         ("fr", "fr", "Français",   "Langue"),
         ("de", "de", "Deutsch",    "Sprache"),
         ("pt", "br", "Português",  "Idioma"),
         ("nl", "nl", "Nederlands", "Taal"),
         ("it", "it", "Italiano",   "Lingua"),
         ("zh", "cn", "中文",        "语言"),
         ("ja", "jp", "日本語",      "言語"),
         ("ko", "kr", "한국어",      "언어"),
         ("ru", "ru", "Русский",    "Язык"),
         ("ar", "sa", "العربية",     "اللغة"),
         ("hi", "in", "हिंदी",       "भाषा")]
BY_CODE = {c: (f, n, w) for c, f, n, w in LANGS}
KINDS = ("home", "door", "proofs")


def target(code, kind):
    """Where a flag leads from a page of this kind."""
    base = "/" if code == "en" else f"/{code}/"
    if kind == "home":
        return base
    if kind == "door":
        return base + "what-is-the-420-code/"
    if kind == "proofs":
        return "/proofs/" if code == "en" else f"/{code}/#proofs"
    raise ValueError(kind)


def keep_name(s):
    """The work's name never breaks across a line in the header."""
    return s.replace("The 420 Code", '<span class="nw">The 420 Code</span>', 1)


def _toggle(state):
    """Open one drop-down and close the other; a second click closes it again."""
    return ("var n=this.closest('.nav'),o=!n.classList.contains('%s');"
            "n.classList.remove('open','lang-open');"
            "n.querySelectorAll('.nav-toggle,.nav-flag').forEach(function(b){b.setAttribute('aria-expanded','false')});"
            "if(o){n.classList.add('%s');this.setAttribute('aria-expanded','true')}") % (state, state)


def rooms_button(label):
    return (f'<button class="nav-toggle" aria-expanded="false" aria-label="{label}" '
            f'onclick="{_toggle("open")}">{label}</button>')


def flag_button(lang):
    flag, name, word = BY_CODE[lang]
    return (f'<button class="nav-flag" aria-expanded="false" aria-label="{word}: {name}" '
            f'onclick="{_toggle("lang-open")}"><img src="{FLAGCDN.format(flag)}" width="20" height="15" alt=""></button>')


def lang_menu(lang, kind):
    rows = []
    for code, flag, name, _ in LANGS:
        cur = ' aria-current="page"' if code == lang else ""
        rows.append(f'<a href="{target(code, kind)}" class="nav-lang" hreflang="{code}" lang="{code}"{cur}>'
                    f'<img src="{FLAGCDN.format(flag)}" width="20" height="15" alt="">{name}</a>')
    return '<div class="nav-langs">\n    ' + "\n    ".join(rows) + "\n  </div>"


def language_parts(lang, kind):
    """The flag button and its list, as they sit in the header after the rooms menu."""
    return f"  {flag_button(lang)}\n  {lang_menu(lang, kind)}\n"


CSS_MARK = "/* ── the header: one row, with the rooms"
CSS_END = "  .nav a.nav-door{font-size:15px}\n}"

CSS = """/* ── the header: one row, with the rooms and the languages behind two drop-downs ── */
.nav{position:sticky;top:0;z-index:100;overflow:visible;flex-wrap:nowrap}
.nav a.nav-room{display:none}
/* one row at every width: the logo and the buttons keep their size; the door's name wraps
   inside its own box instead, never splitting The 420 Code, never pushing a button down */
.nav-logo,.nav-toggle,.nav-flag{flex-shrink:0}
.nav a.nav-door{min-width:0;word-break:keep-all}
.nav .nw{white-space:nowrap}
.nav-toggle,.nav-flag{display:inline-flex;align-items:center;gap:.45rem;
  background:none;border:1px solid var(--g3);border-radius:3px;font-family:inherit;
  font-size:14px;font-weight:700;color:#1a1a1a;padding:5px 11px;cursor:pointer;line-height:1.2}
.nav-toggle{margin-left:auto}
/* the flag button is exactly as tall as Rooms: one 14px line, 10px padding, 2px border */
.nav-flag{height:calc(1.2em + 12px)}
.nav-flag img{display:block;width:20px;height:15px;border-radius:2px}
.nav-toggle:hover,.nav-flag:hover{border-color:#8B6914;color:#8B6914}
.nav-toggle::after,.nav-flag::after{content:"";display:inline-block;width:0;height:0;
  border-left:4px solid transparent;border-right:4px solid transparent;
  border-top:5px solid currentColor;transition:transform .15s}
.nav.open .nav-toggle,.nav.lang-open .nav-flag{border-color:#8B6914;color:#8B6914}
.nav.open .nav-toggle::after,.nav.lang-open .nav-flag::after{transform:rotate(180deg)}
.nav-menu,.nav-langs{display:none;position:absolute;top:100%;right:0;min-width:270px;max-width:min(92vw,340px);
  background:#fff;border:1px solid var(--g3);border-top:none;border-radius:0 0 4px 4px;
  box-shadow:0 8px 24px rgba(0,0,0,.10);padding:.65rem 0 .5rem;z-index:200}
.nav.open .nav-menu,.nav.lang-open .nav-langs{display:block}
.nav.open .nav-menu a.nav-room,.nav.lang-open .nav-langs a.nav-lang{display:block;padding:.42rem 1.15rem;font-size:15px;
  text-decoration:none;color:#1a1a1a;white-space:nowrap}
.nav.lang-open .nav-langs a.nav-lang{display:flex;align-items:center;gap:.7rem}
.nav-langs a.nav-lang img{width:20px;height:15px;border-radius:2px;flex-shrink:0}
.nav.open .nav-menu a.nav-room:hover,.nav.lang-open .nav-langs a.nav-lang:hover{background:var(--g1);color:#8B6914}
.nav.lang-open .nav-langs a.nav-lang[aria-current]{font-weight:700;color:#8B6914}
@media(max-width:400px){.nav{gap:.6rem}}
@media(max-width:359px){.nav .nw{white-space:normal}}
@media(max-width:700px){
  .nav-menu,.nav-langs{left:0;right:0;max-width:none;border-radius:0}
  .nav a.nav-door{line-height:1.25}
  .nav a.nav-door{font-size:15px}
}"""

RTL_MARK = "/* ── right-to-left: the header and the front door ── */"
RTL_CSS = RTL_MARK + """
[dir="rtl"] .nav{flex-direction:row}
[dir="rtl"] .nav-toggle{margin-left:0;margin-right:auto}
@media(min-width:701px){[dir="rtl"] .nav-menu,[dir="rtl"] .nav-langs{right:auto;left:0}}
[dir="rtl"] .fd ol.chain li{padding:0 2.6rem 1.1rem 0}
[dir="rtl"] .fd ol.chain li::before{left:auto;right:0}
[dir="rtl"] .fd blockquote{padding:0 1.25rem 0 0;border-left:none;border-right:3px solid #8B6914}
[dir="rtl"] .fd .axiom{direction:ltr}
bdi{unicode-bidi:isolate}
/* ── end right-to-left ── */"""
# the block as build.py wrote it before 11 September, which it replaces where found
RTL_CSS_OLD = """
[dir="rtl"] .nav-toggle{margin-left:0;margin-right:auto}
[dir="rtl"] .nav-menu{right:auto;left:0}
[dir="rtl"] .fd ol.chain li{padding:0 2.6rem 1.1rem 0}
[dir="rtl"] .fd ol.chain li::before{left:auto;right:0}
[dir="rtl"] .fd blockquote{padding:0 1.25rem 0 0;border-left:none;border-right:3px solid #8B6914}
[dir="rtl"] .fd .axiom{direction:ltr}
bdi{unicode-bidi:isolate}
"""

JS = """<script id="nav-menu-close">
// A choice in either list closes it and lets the link do its work; a click anywhere
// outside the header's drop-downs, or Escape, closes whichever is open.
document.addEventListener('click',function(e){
  var n=document.querySelector('.nav');
  if(!n||!(n.classList.contains('open')||n.classList.contains('lang-open')))return;
  var chose=e.target.closest('.nav-menu a,.nav-langs a');
  if(!chose&&e.target.closest('.nav-menu,.nav-langs,.nav-toggle,.nav-flag'))return;
  n.classList.remove('open','lang-open');
  n.querySelectorAll('.nav-toggle,.nav-flag').forEach(function(b){b.setAttribute('aria-expanded','false')});
});
document.addEventListener('keydown',function(e){
  if(e.key!=='Escape')return;
  var n=document.querySelector('.nav'); if(!n)return;
  n.classList.remove('open','lang-open');
  n.querySelectorAll('.nav-toggle,.nav-flag').forEach(function(b){b.setAttribute('aria-expanded','false')});
});
</script>"""


def replace_css(page):
    """Swap the header's CSS block for the current one; insert it if the page has none."""
    i = page.find(CSS_MARK)
    if i < 0:
        j = page.rindex("</style>")
        return page[:j] + "\n" + CSS + "\n" + page[j:]
    j = page.index(CSS_END, i) + len(CSS_END)
    return page[:i] + CSS + page[j:]


def replace_js(page):
    import re
    if 'id="nav-menu-close"' in page:
        return re.sub(r'<script id="nav-menu-close">.*?</script>', lambda m: JS, page, count=1, flags=re.S)
    return page.replace("</body>", JS + "\n</body>", 1)


def replace_rtl(page):
    """The right-to-left block, current, exactly once, after every other style."""
    import re
    page = re.sub(re.escape(RTL_MARK) + r".*?/\* ── end right-to-left ── \*/\n?", "", page, flags=re.S)
    page = page.replace(RTL_CSS_OLD, "\n")
    j = page.rindex("</style>")
    return page[:j] + RTL_CSS + "\n" + page[j:]
