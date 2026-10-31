// The family's numbers, counted by each site from what it publishes (G, 31 October 2026: "All the stats").
//
// At build, each site runs:   node tools/family-stats.mjs <publish folder> --site <its address>
// and publishes <publish folder>/stats.json. studiog.global's library adds the eleven together
// (netlify/functions/family-stats.mjs). The same counting reads the two sites not built from
// GitHub, from their sitemaps (crawl()). Node only, no dependencies. The same file sits in every
// repo of the family: change it in one, copy it to all.
//
// What is counted, page by page:
//   - a page is every published .html, except 404s, redirect stubs, noindex pages and search-engine
//     verification files
//   - its language is <html lang>; English is "en" or no lang at all
//   - its words are the reading text: <main> if the page has one, else the body without its header,
//     nav and footer; scripts, styles, drawings and templates never count
//   - its links are every <a href> that stays inside the family (relative, or to one of its sites)
//   - its videos are every <video> (by its file) and every YouTube or Vimeo frame
// A translation of an English page is the page its hreflang names, or the same address under /<lang>/.
// A translated page counts at the length of its English source, so the languages compare fairly
// (Japanese and Chinese do not put spaces between words). A video counts as translated into a
// language when that language's page plays a different file in its place, or carries captions in it.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

export const FAMILY = ["the420code.org", "whybekind.global", "philosophy.global", "onereality.global", "appliedethics.global",
  "aiethics.global", "bioethics.global", "studiog.global", "artist-g.global", "studiog.co.za", "therosinbar.com"];
const ALIASES = ["whybekind.org"];   // still forwards, page for page, to whybekind.global
const HOSTS = new Set([...FAMILY, ...ALIASES].flatMap(h => [h, "www." + h]));

const ENT = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", rsquo: "’", lsquo: "‘", rdquo: "”", ldquo: "“",
  ndash: "–", mdash: "—", hellip: "…", middot: "·" };
const decode = s => s.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (m, e) =>
  e[0] === "#" ? String.fromCodePoint(e[1] === "x" || e[1] === "X" ? parseInt(e.slice(2), 16) : +e.slice(1)) : (ENT[e.toLowerCase()] ?? " "));
const strip = (h, tag) => h.replace(new RegExp(`<${tag}\\b[\\s\\S]*?</${tag}>`, "gi"), " ");
const WORD = /[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*/gu;

export function readingText(html) {
  let h = html.replace(/<!--[\s\S]*?-->/g, " ");
  for (const t of ["script", "style", "svg", "noscript", "template", "head"]) h = strip(h, t);
  const main = h.match(/<main\b[^>]*>([\s\S]*)<\/main>/i);
  if (main) h = main[1];
  else {
    const body = h.match(/<body\b[^>]*>([\s\S]*)<\/body>/i);
    if (body) h = body[1];
    for (const t of ["header", "nav", "footer"]) h = strip(h, t);
  }
  return decode(h.replace(/<[^>]+>/g, " ")).replace(/\s+/g, " ").trim();
}
export const countWords = text => (text.match(WORD) || []).length;

function langOf(html) {
  const m = html.match(/<html\b[^>]*\blang=["']?([A-Za-z-]+)/i);
  const l = m ? m[1].toLowerCase().split("-")[0] : "en";
  return l || "en";
}
function skip(html, rel) {
  const base = path.posix.basename(rel);
  if (/^404\.html$/i.test(base) || /^google[0-9a-f]+\.html$/i.test(base) || /^yandex_[0-9a-f]+\.html$/i.test(base)) return true;
  if (/<meta[^>]+http-equiv=["']?refresh/i.test(html) && countWords(readingText(html)) < 40) return true;   // a forwarding stub
  if (/<meta[^>]+name=["']?robots["']?[^>]+noindex/i.test(html)) return true;
  return false;
}
// a file's address on its site: /x/index.html -> /x/ ; /x.html stays
const addressOf = rel => "/" + rel.replace(/\\/g, "/").replace(/(^|\/)index\.html$/i, "$1");

function linksIn(html, host) {
  let n = 0;
  for (const m of html.matchAll(/<a\b[^>]*?\bhref\s*=\s*["']([^"']+)["']/gi)) {
    const href = m[1].trim();
    if (/^(mailto:|tel:|javascript:|data:|#)/i.test(href)) continue;
    const abs = href.match(/^(?:https?:)?\/\/([^/:?#]+)/i);
    if (abs ? HOSTS.has(abs[1].toLowerCase()) : true) n++;
  }
  return n;
}
function videosIn(html) {
  const out = [];
  for (const m of html.matchAll(/<video\b([^>]*)>([\s\S]*?)<\/video>/gi)) {
    const src = (m[1].match(/\bsrc=["']([^"']+)/i) || m[2].match(/<source\b[^>]*\bsrc=["']([^"']+)/i) || [])[1];
    if (!src) continue;
    const tracks = [...m[2].matchAll(/<track\b[^>]*\bsrclang=["']?([A-Za-z-]+)/gi)].map(t => t[1].toLowerCase().split("-")[0]);
    out.push({ src: src.replace(/[?#].*$/, ""), tracks });
  }
  for (const m of html.matchAll(/<iframe\b[^>]*\bsrc=["']([^"']*(?:youtube\.com|youtube-nocookie\.com|youtu\.be|vimeo\.com)[^"']*)/gi)) {
    const id = (m[1].match(/(?:embed\/|youtu\.be\/|video\/)([\w-]+)/) || [])[1] || m[1];
    const cc = (m[1].match(/[?&](?:cc_lang_pref|hl)=([a-z]{2})/i) || [])[1];
    out.push({ src: "yt:" + id, tracks: cc ? [cc.toLowerCase()] : [] });
  }
  return out;
}
function hreflangs(html) {
  const out = {};
  for (const m of html.matchAll(/<link\b[^>]*>/gi)) {
    const t = m[0];
    if (!/rel=["']?alternate/i.test(t)) continue;
    const hl = (t.match(/hreflang=["']?([A-Za-z-]+)/i) || [])[1], href = (t.match(/href=["']([^"']+)/i) || [])[1];
    if (hl && href && !/^x-default$/i.test(hl)) out[hl.toLowerCase().split("-")[0]] = href;
  }
  return out;
}
const pathOf = href => { try { return new URL(href, "https://x.invalid").pathname; } catch { return null; } };

// pages: [{ address, html }]  ->  the site's numbers
export function analyse(site, pages) {
  const seen = [];
  for (const p of pages) {
    if (skip(p.html, p.address)) continue;
    const lang = langOf(p.html);
    seen.push({ address: p.address, lang, words: countWords(readingText(p.html)), links: linksIn(p.html, site),
      videos: videosIn(p.html), alt: hreflangs(p.html) });
  }
  const by = new Map(seen.map(p => [p.address, p]));
  const en = seen.filter(p => p.lang === "en");
  const langs = [...new Set(seen.map(p => p.lang).filter(l => l !== "en"))].sort();
  const pagesByLang = {}, wordsByLang = {}, videosTranslated = {};
  for (const p of seen) pagesByLang[p.lang] = (pagesByLang[p.lang] || 0) + 1;
  const videos = new Set();
  for (const p of en) for (const v of p.videos) videos.add(v.src);
  for (const L of langs) {
    let w = 0; const vt = new Set();
    for (const p of en) {
      let t = p.alt[L] ? by.get(pathOf(p.alt[L])) : null;
      if (!t || t.lang !== L) t = by.get(`/${L}${p.address}`);
      if (!t || t.lang !== L) continue;
      w += p.words;
      p.videos.forEach((v, i) => {
        const tv = t.videos[i];
        if (v.tracks.includes(L) || (tv && (tv.src !== v.src || tv.tracks.includes(L)))) vt.add(v.src);
      });
    }
    wordsByLang[L] = w; videosTranslated[L] = [...vt].sort();
  }
  return {
    site, counted: new Date().toISOString(), rule: "https://studiog.global/library/#all-the-stats",
    pages: seen.length, pages_by_lang: pagesByLang,
    words_en: en.reduce((a, p) => a + p.words, 0),
    words_by_lang: wordsByLang,          // English words that have a translation in each language
    links: seen.reduce((a, p) => a + p.links, 0),
    videos: [...videos].sort(), videos_translated: videosTranslated,
  };
}

// every counted page's address, as the visit counters read a path: lower case, ending in "/", and a
// page.html also as page (the sites serve both). Written beside stats.json as /pages.json, which the
// site's visit counter reads: a page on it is counted, so a new room counts from its first day.
export function addressesOf(pages) {
  const out = new Set();
  for (const p of pages) {
    if (skip(p.html, p.address)) continue;
    const a = p.address.toLowerCase();
    for (const v of [a, a.replace(/\.html$/, "")]) out.add(v.endsWith("/") ? v : v + "/");
  }
  return [...out].sort();
}

// from a publish folder
export const fromFolder = (dir, site) => analyse(site, readFolder(dir));
function readFolder(dir) {
  const pages = [];
  const walk = d => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (e.name.startsWith(".") || e.name === "node_modules") continue;
      const f = path.join(d, e.name);
      if (e.isDirectory()) walk(f);
      else if (e.name.toLowerCase().endsWith(".html")) pages.push({ address: addressOf(path.relative(dir, f)), html: fs.readFileSync(f, "utf8") });
    }
  };
  walk(dir);
  return pages;
}

// from a live site's sitemap (the sites not built from GitHub)
export async function crawl(site, { limit = 400, parallel = 8, timeout = 8000 } = {}) {
  const get = async u => {
    const r = await fetch(u, { headers: { "User-Agent": "studiog.global family stats" }, signal: AbortSignal.timeout(timeout), redirect: "follow" });
    if (!r.ok) throw new Error(`${u}: ${r.status}`);
    return { url: r.url, text: await r.text(), type: r.headers.get("content-type") || "" };
  };
  const urls = new Set(), maps = [`https://${site}/sitemap.xml`];
  for (let i = 0; i < maps.length && i < 30; i++) {
    let x; try { x = (await get(maps[i])).text; } catch { if (i === 0) maps.push(`https://${site}/wp-sitemap.xml`, `https://${site}/sitemap_index.xml`); continue; }
    const locs = [...x.matchAll(/<loc>\s*([^<\s]+)\s*<\/loc>/g)].map(m => decode(m[1]));
    if (/<sitemapindex/i.test(x)) maps.push(...locs); else locs.forEach(u => urls.add(u));
  }
  if (!urls.size) urls.add(`https://${site}/`);
  const list = [...urls].filter(u => { try { return HOSTS.has(new URL(u).hostname); } catch { return false; } })
    .filter(u => !/\.(pdf|jpe?g|png|gif|webp|svg|mp4|zip|xml)$/i.test(u)).slice(0, limit);
  const pages = [];
  for (let i = 0; i < list.length; i += parallel) {
    const got = await Promise.allSettled(list.slice(i, i + parallel).map(get));
    for (const g of got) if (g.status === "fulfilled" && /html/i.test(g.value.type)) {
      const u = new URL(g.value.url);
      if (HOSTS.has(u.hostname)) pages.push({ address: u.pathname, html: g.value.text });
    }
  }
  return analyse(site, pages);
}

// the command line
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const a = process.argv.slice(2);
  const dir = a.find(x => !x.startsWith("--")) || ".";
  const site = a.includes("--site") ? a[a.indexOf("--site") + 1] : null;
  if (!site) { console.error("family-stats: give --site <address>"); process.exit(2); }
  let s;
  if (a.includes("--crawl")) { s = await crawl(site); process.stdout.write(JSON.stringify(s) + "\n"); }
  else {
    const pages = readFolder(dir);
    s = analyse(site, pages);
    fs.writeFileSync(path.join(dir, "stats.json"), JSON.stringify(s) + "\n");
    fs.writeFileSync(path.join(dir, "pages.json"), JSON.stringify(addressesOf(pages)) + "\n");
  }
  const tl = Object.values(s.words_by_lang).reduce((x, y) => x + y, 0);
  console.error(`family-stats: ${site}: ${s.pages} pages, ${s.words_en} English words, ${Object.keys(s.words_by_lang).length} other languages (${tl} words translated), ${s.links} family links, ${s.videos.length} videos`);
}
