# -*- coding: utf-8 -*-
"""The site header's two drop-downs, as every page with the drop-down header carries it.

Rooms, then the language: a button carrying the name of the language being read,
in that language's own script, the same kind of button as Rooms, with the same arrow,
opening a list of all thirteen. Since 24 September 2026 there are no flags: a flag is a
nation, not a language, and one of them carried a creed. An entry takes the reader to the
same page in that language wherever the page exists in it -- a front door to a front door,
a home page to a home page, the Proofs page to that edition's proofs room. A page that exists only in English (Predictions, its frozen
documents, Three Ways of Being Sure) sends each other language to its edition's home.

One row at every width: the logo and both buttons keep their size, and the door's name
wraps inside its own box when a phone is narrow, never splitting "The 420 Code".

Used by build.py for the twelve editions, and for every English page that carries the
header, so all of them are made by the same code."""

#          code  flag  the language's own name   "Language", in that language
# the flag column is kept for the record and is no longer used anywhere (24 September 2026)
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
KINDS = ("home", "door", "proofs", "en-only")


def target(code, kind, here=None):
    """Where a flag leads from a page of this kind."""
    base = "/" if code == "en" else f"/{code}/"
    if kind == "home":
        return base
    if kind == "door":
        return base + "what-is-the-420-code/"
    if kind == "proofs":
        return "/proofs/" if code == "en" else f"/{code}/#proofs"
    if kind == "en-only":
        assert here, "an English-only page names itself"
        return here if code == "en" else base
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
    _flag, name, word = BY_CODE[lang]
    return (f'<button class="nav-flag" aria-expanded="false" aria-label="{word}: {name}" '
            f'onclick="{_toggle("lang-open")}">{name}</button>')


def lang_menu(lang, kind, here=None):
    rows = []
    for code, flag, name, _ in LANGS:
        cur = ' aria-current="page"' if code == lang else ""
        rows.append(f'<a href="{target(code, kind, here)}" class="nav-lang" hreflang="{code}" lang="{code}"{cur}>'
                    f'{name}</a>')
    return '<div class="nav-langs">\n    ' + "\n    ".join(rows) + "\n  </div>"


def language_parts(lang, kind, here=None):
    """The flag button and its list, as they sit in the header after the rooms menu."""
    return f"  {flag_button(lang)}\n  {lang_menu(lang, kind, here)}\n"


def english_header(rooms_menu, kind, here=None):
    """The whole English header, for a page outside the generated set. rooms_menu is the
    English front door's own rooms block, taken from it verbatim, so the rooms can never
    drift from the pages that define them."""
    return ('<nav class="nav">\n'
            '  <a href="/" class="nav-logo"><img src="/Eye_of_the_Universe.jpg" alt="the 420 code" style="height:37px"></a>\n'
            f'  <a href="/what-is-the-420-code/" class="nav-door">{keep_name("What Is The 420 Code")}</a>\n'
            + SEARCH
            + f'  {rooms_button("Rooms")}\n'
            f'{rooms_menu}\n'
            + language_parts("en", kind, here) + '</nav>')


SEARCH = """  <form class="nav-search" role="search" onsubmit="return false"><label class="vh" for="nav-q">Search the work</label><input id="nav-q" class="nav-q" type="search" placeholder="Search the work" autocomplete="off" spellcheck="false"><div class="nav-results" role="listbox" aria-label="Search results"></div></form>
  <button class="nav-search-btn" aria-expanded="false" aria-label="Search" onclick="var n=this.closest('.nav');n.classList.remove('open','lang-open');var o=!n.classList.contains('search-open');n.classList.toggle('search-open',o);this.setAttribute('aria-expanded',o?'true':'false');if(o){var q=n.querySelector('.nav-q');q.focus()}"><svg width="17" height="17" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8.5" cy="8.5" r="5.5"/><line x1="12.8" y1="12.8" x2="18" y2="18" stroke-linecap="round"/></svg></button>
"""

DOOR_CSS = ".nav a.nav-door{font-weight:700;color:#1a1a1a}\n.nav a.nav-door:hover{color:#8B6914}"

# the rules the header stands on, exactly as the home page has them, for a page that was
# built with a header of its own
BASE_MARK = "/* ── the header's base, as the home page has it ── */"
BASE_END = "/* ── end of the header's base ── */"
BASE_CSS = BASE_MARK + """
.nav{position:sticky;top:0;background:rgba(255,255,255,0.95);backdrop-filter:blur(8px);z-index:100;display:flex;flex-wrap:wrap;gap:1.5rem;align-items:center;padding:.7rem 0;border-bottom:1px solid var(--g3);margin:0 0 3rem;line-height:1.65}
html{scroll-padding-top:86px}
@media(max-width:640px){html{scroll-padding-top:126px}}
.nav a:not(.nav-title){font-size:16px;color:var(--g5);text-decoration:none}
.nav a:not(.nav-title):hover{color:var(--bk);text-decoration:underline}
@media(max-width:600px){.nav{gap:.75rem;padding:.75rem 0}}
""" + DOOR_CSS + "\n" + BASE_END

CSS_MARK = "/* ── the header: one row, with the rooms"
CSS_END = "  .nav a.nav-door{font-size:16px}\n}"

CSS = """/* ── the header: one row, with the rooms and the languages behind two drop-downs ── */
.nav{position:sticky;top:0;z-index:100;overflow:visible;flex-wrap:nowrap}
.nav a.nav-room{display:none}
/* one row at every width: the logo and the buttons keep their size; the door's name wraps
   inside its own box instead, never splitting The 420 Code, never pushing a button down */
.nav-logo,.nav-toggle,.nav-flag{flex-shrink:0}
.nav a.nav-door{min-width:0;word-break:keep-all}
.nav .nw{white-space:nowrap}
.nav-toggle,.nav-flag{display:inline-flex;align-items:center;gap:.45rem;
  background:none;border:1px solid var(--edge);border-radius:3px;font-family:inherit;
  font-size:16px;font-weight:700;color:#1a1a1a;padding:5px 11px;cursor:pointer;line-height:1.2}
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
  background:#fff;border:1px solid var(--edge);border-top:none;border-radius:0 0 4px 4px;
  box-shadow:0 8px 24px rgba(0,0,0,.10);padding:.65rem 0 .5rem;z-index:200}
.nav.open .nav-menu,.nav.lang-open .nav-langs{display:block}
.nav.open .nav-menu a.nav-room,.nav.lang-open .nav-langs a.nav-lang{display:block;padding:.42rem 1.15rem;font-size:16px;
  text-decoration:none;color:#1a1a1a;white-space:nowrap}
.nav.lang-open .nav-langs a.nav-lang{display:flex;align-items:center;gap:.7rem}
.nav-langs a.nav-lang img{width:20px;height:15px;border-radius:2px;flex-shrink:0}
.nav.open .nav-menu a.nav-room:hover,.nav.lang-open .nav-langs a.nav-lang:hover{background:var(--g1);color:#8B6914}
.nav.lang-open .nav-langs a.nav-lang[aria-current]{font-weight:700;color:#8B6914}
/* the search, in the header: one field, and the whole work answers (G, 22 September 2026) */
.vh{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.nav-search{position:relative;flex:1 1 170px;min-width:0;max-width:340px;margin:0}
.nav-q{width:100%;font-family:inherit;font-size:16px;line-height:1.2;color:#1a1a1a;background:#fff;
  border:1px solid var(--edge);border-radius:3px;padding:6px 11px;-webkit-appearance:none;appearance:none}
.nav-q::placeholder{color:var(--g5);opacity:1}
.nav-q:focus{outline:none;border-color:#8B6914}
.nav-search-btn{display:none;align-items:center;background:none;border:1px solid var(--edge);border-radius:3px;
  color:#1a1a1a;padding:6px 9px;cursor:pointer;line-height:1;flex-shrink:0}
.nav-search-btn:hover,.nav.search-open .nav-search-btn{border-color:#8B6914;color:#8B6914}
.nav-results{display:none;position:absolute;top:calc(100% + 6px);left:0;right:0;max-height:min(70vh,560px);
  overflow-y:auto;background:#fff;border:1px solid var(--edge);border-radius:0 0 4px 4px;
  box-shadow:0 8px 24px rgba(0,0,0,.10);z-index:200;text-align:left}
.nav-results.on{display:block}
.nav .nav-results a{display:block;padding:.6rem 1rem;border-bottom:1px solid var(--g2);
  text-decoration:none;color:#1a1a1a;font-size:16px;line-height:1.45}
.nav .nav-results a:last-child{border-bottom:0}
.nav .nav-results a:hover,.nav .nav-results a.on{background:var(--g1);text-decoration:none}
.nr-t{display:block;font-weight:700}
.nr-k{display:block;color:var(--g5)}
.nr-s{display:block;color:var(--g5);margin-top:.1rem}
.nav-results mark{background:none;color:#8B6914;font-weight:700}
.nr-note{margin:0;padding:.7rem 1rem;font-size:16px;color:var(--g5)}
@media(max-width:400px){.nav{gap:.6rem}}
/* on a small phone the work's name takes the first row and the three buttons the second, so the
   name is never squeezed to a column of letters by the magnifier beside it */
@media(max-width:470px){.nav{flex-wrap:wrap;row-gap:.5rem}.nav a.nav-door{flex:1 0 calc(100% - 4rem)}
  .nav-search-btn{margin-left:auto}.nav-toggle{margin-left:0}}
@media(max-width:359px){.nav .nw{white-space:normal}}
@media(max-width:700px){
  .nav-menu,.nav-langs{left:0;right:0;max-width:none;border-radius:0}
  .nav-search{display:none;position:absolute;top:100%;left:0;right:0;max-width:none;background:#fff;
    border-bottom:1px solid var(--g3);padding:.65rem 0 .8rem}
  .nav.search-open .nav-search{display:block}
  .nav-search-btn{display:inline-flex}
  .nav-results{position:static;border:0;box-shadow:none;margin-top:.55rem;max-height:min(60vh,420px)}
  .nav a.nav-door{line-height:1.25}
  .nav a.nav-door{font-size:16px}
}"""

RTL_MARK = "/* ── right-to-left: the header and the front door ── */"
RTL_CSS = RTL_MARK + """
[dir="rtl"] .nav{flex-direction:row}
[dir="rtl"] .nav-toggle{margin-left:0;margin-right:auto}
@media(min-width:701px){[dir="rtl"] .nav-menu,[dir="rtl"] .nav-langs{right:auto;left:0}}
[dir="rtl"] .fd ol.chain li{padding:0 2.6rem 1.1rem 0}
[dir="rtl"] .fd ol.chain li::before{left:auto;right:0}
[dir="rtl"] .fd blockquote{border-left:none;border-right:3px solid #8B6914}
[dir="rtl"] .fd .axiom{direction:ltr}
bdi{unicode-bidi:isolate}
/* ── end right-to-left ── */"""
# the block as build.py wrote it before 11 September, which it replaces where found
RTL_CSS_OLD = """
[dir="rtl"] .nav-toggle{margin-left:0;margin-right:auto}
[dir="rtl"] .nav-menu{right:auto;left:0}
[dir="rtl"] .fd ol.chain li{padding:0 2.6rem 1.1rem 0}
[dir="rtl"] .fd ol.chain li::before{left:auto;right:0}
[dir="rtl"] .fd blockquote{border-left:none;border-right:3px solid #8B6914}
[dir="rtl"] .fd .axiom{direction:ltr}
bdi{unicode-bidi:isolate}
"""

JS = r"""<script id="nav-menu-close">
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
</script>
<script id="nav-search">
// The search: /search-index.json holds one record per room, chapter, kill switch, glossary entry,
// paper and frozen document. It is fetched when the reader first reaches for the field, not before,
// and kept for the session. Every term must be present; the last one matches as a prefix, so results
// arrive while the word is still being typed. Title hits weigh most, then the book or room it is in.
(function(){
  var form=document.querySelector('.nav-search'); if(!form) return;
  var q=form.querySelector('.nav-q'), out=form.querySelector('.nav-results'), nav=form.closest('.nav');
  var docs=null, state='', sel=-1, timer=0;
  var W={room:3,book:2,chapter:1,epilogue:1,paper:2,'kill switch':1,glossary:1,'frozen document':1};
  function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function rx(t,last){var e=t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    try{return new RegExp('(^|[^\\p{L}\\p{N}])'+e+(last?'':'(?![\\p{L}\\p{N}])'),'giu')}
    catch(err){return new RegExp('(^|[^a-z0-9])'+e,'gi')}}
  function note(html){out.innerHTML='<p class="nr-note">'+html+'</p>';out.classList.add('on')}
  function load(){
    if(docs||load.busy) return; load.busy=true;
    fetch('/search-index.json').then(function(r){return r.json()}).then(function(d){
      docs=d.docs; docs.forEach(function(x){x.tl=x.t.toLowerCase();x.xl=x.x.toLowerCase();x.bl=(x.b||'').toLowerCase()});
      load.busy=false; if(q.value.trim()) run();
    }).catch(function(){load.busy=false; note('The search could not load. Every room is in the menu beside this field.')});
  }
  function count(re,s){var n=0; re.lastIndex=0; while(re.exec(s)){n++; if(re.lastIndex>s.length||n>40)break} return n}
  function run(){
    var query=q.value.trim(); state=query;
    if(query.length<2){out.classList.remove('on');out.innerHTML='';return}
    if(!docs){load();note('Searching…');return}
    var terms=query.toLowerCase().split(/[^\p{L}\p{N}]+/u).filter(Boolean).slice(0,6);
    if(!terms.length){out.classList.remove('on');return}
    var res=[];
    for(var i=0;i<docs.length;i++){
      var d=docs[i], score=0, ok=true, first=-1;
      for(var j=0;j<terms.length;j++){
        var last=(j===terms.length-1), re=rx(terms[j],last);
        var inT=count(re,d.tl), inB=count(re,d.bl), inX=count(re,d.xl);
        if(!inT&&!inB&&!inX){ok=false;break}
        score+=inT*14+inB*4+Math.min(inX,8);
        if(first<0&&inX){re.lastIndex=0;var m=re.exec(d.xl); if(m) first=m.index}
      }
      if(!ok) continue;
      score+=W[d.k]||0;
      if(d.tl===query.toLowerCase()) score+=30;
      res.push([score,d,first]);
    }
    res.sort(function(a,b){return b[0]-a[0]});
    if(!res.length){note('Nothing for <b>'+esc(query)+'</b> yet.');return}
    var html='', n=Math.min(res.length,12);
    for(var k=0;k<n;k++){
      var d=res[k][1], at=res[k][2], x=d.x;
      var from=at<0?0:Math.max(0,x.lastIndexOf(' ',Math.max(0,at-70))+1);
      var cut=esc(x.slice(from,from+190))+(from+190<x.length?'…':'');
      var lead=(from>0?'…':'');
      for(var j=0;j<terms.length;j++) cut=cut.replace(rx(terms[j],j===terms.length-1),function(m,p1){return p1+'<mark>'+m.slice(p1.length)+'</mark>'});
      var where=d.b&&d.b!==d.t?esc(d.b)+' · '+esc(d.k):esc(d.k);
      html+='<a href="'+d.u+'" role="option"><span class="nr-t">'+esc(d.t)+'</span><span class="nr-k">'+where+'</span><span class="nr-s">'+lead+cut+'</span></a>';
    }
    if(res.length>n) html+='<p class="nr-note">'+n+' of '+res.length+' places. Keep typing to narrow it.</p>';
    out.innerHTML=html; out.classList.add('on'); sel=-1;
  }
  function move(step){
    var as=out.querySelectorAll('a'); if(!as.length) return;
    if(sel>=0&&as[sel]) as[sel].classList.remove('on');
    sel=(sel+step+as.length)%as.length; as[sel].classList.add('on'); as[sel].scrollIntoView({block:'nearest'});
  }
  q.addEventListener('focus',load);
  q.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,110)});
  q.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();move(1)}
    else if(e.key==='ArrowUp'){e.preventDefault();move(-1)}
    else if(e.key==='Enter'){var as=out.querySelectorAll('a'); if(as.length){e.preventDefault();(as[sel>=0?sel:0]).click()}}
    else if(e.key==='Escape'){out.classList.remove('on');q.blur();nav.classList.remove('search-open')}
  });
  document.addEventListener('click',function(e){ if(!e.target.closest('.nav-search')&&!e.target.closest('.nav-search-btn')) out.classList.remove('on') });
})();
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
    """The header's scripts, current, exactly once. JS has been two blocks since 22 September 2026 --
    the one that closes the menus, and the search -- so any search block already on the page is taken
    out before the swap; otherwise a second pass leaves the first one standing behind the new pair."""
    import re
    page = re.sub(r'\s*<script id="nav-search">.*?</script>', "", page, flags=re.S)
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
