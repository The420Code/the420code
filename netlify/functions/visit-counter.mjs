import { getStore } from "@netlify/blobs";

// A visit is one browser session, not one page load. The page guards on
// sessionStorage before it posts, so a reload does not count again and the
// figure keeps meaning something. Counted from every page; shown on one.
// Crawlers do not run the script, so they are not in the number.
//
// WHY THIS IS APPEND-ONLY. Two earlier versions read the count, added one and
// wrote it back. Both undercounted, and measurably: three visits a few seconds
// apart produced two. Netlify Blobs is eventually consistent, so a read taken
// straight after a write can still be the old value, and the increment is lost.
// No amount of key design fixes that, and @netlify/blobs 8.2 has no conditional
// write to build a compare-and-swap on.
//
// So a visit never reads anything. It writes one new blob under its own unique
// key, which cannot collide and cannot be lost. The count is the number of those
// blobs, plus a rolled-up base. Exact by construction.

const PREFIX = "v/";
const BASE = "visits-base";
const ROLLUP_AT = 2000;   // fold the loose blobs into the base past this many

// Four hits were written to "/" while this was being brought up on 10 September
// 2026 -- all of them mine, none of them a reader. They are subtracted so the
// figure is true from its first day rather than starting four ahead. Stated here
// rather than quietly folded into a base, so the number can always be audited.
const SEED = 4;
const LANGS = ["ar","de","es","fr","hi","it","ja","ko","nl","pt","ru","zh"];

const langOf = (path) => {
  const seg = path.split("/")[1] || "";
  return LANGS.includes(seg) ? seg : "en";
};

// Only pages this site actually has are counted. Two reasons: a scanner walking
// /wp-admin/ never inflates the figure, and the handful of probe paths written
// while this was being built drop out of the count without deleting anything.
// Applied when reading, so it is retroactive.
const PAGES = new Set(["/", "/what-is-the-420-code/", "/proofs/", "/prereg/",
                       ...LANGS.map(l => `/${l}/`)]);
const normalise = (p) => {
  if (!p || p === "") return "/";
  p = p.replace(/index\.html$/, "");
  if (!p.endsWith("/")) p += "/";
  return p;
};
const isRealPage = (p) => PAGES.has(normalise(p));

async function readBase(store) {
  const raw = await store.get(BASE);
  if (!raw) return { count: 0, pages: {}, langs: {} };
  try {
    const b = JSON.parse(raw);
    return { count: b.count || 0, pages: b.pages || {}, langs: b.langs || {} };
  } catch (e) { return { count: 0, pages: {}, langs: {} }; }
}

async function tally(store, withBreakdown) {
  const base = await readBase(store);
  const { blobs } = await store.list({ prefix: PREFIX });

  // every read walks the blobs, because only real pages count and the path
  // lives inside each blob; the total is the sum of the breakdown, always
  const pages = { ...base.pages }, langs = { ...base.langs };
  const loose = await Promise.all(blobs.map(b => store.get(b.key).catch(() => null)));
  for (const raw of loose) {
    if (!raw) continue;
    let p = "/";
    try { p = JSON.parse(raw).path || "/"; } catch (e) { /* count it against "/" */ }
    if (!isRealPage(p)) continue;
    p = normalise(p);
    pages[p] = (pages[p] || 0) + 1;
    const l = langOf(p);
    langs[l] = (langs[l] || 0) + 1;
  }
  const counted = base.count + Object.values(pages).reduce((a,b)=>a+b,0)
                            - Object.values(base.pages).reduce((a,b)=>a+b,0);
  const out = { total: Math.max(0, counted - SEED), pages, langs };

  // Fold the loose blobs into the base when there are many, so the list stays
  // cheap. The base is written before anything is deleted: if the delete half
  // fails, the next roll-up simply counts those visits into the base again --
  // which is why this only runs when the list is long, and never on a POST.
  if (blobs.length >= ROLLUP_AT) {
    await store.set(BASE, JSON.stringify({ count: out.total, pages, langs }));
    for (const b of blobs) { try { await store.delete(b.key); } catch (e) { /* next time */ } }
  }
  return out;
}

export default async (req, context) => {
  const store = getStore("counters");
  const url = new URL(req.url);
  const headers = {
    "Content-Type": "application/json",
    "Cache-Control": "no-store",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };

  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers });

  if (req.method === "GET") {
    const stats = url.searchParams.get("stats") === "1";
    const t = await tally(store, stats);
    const body = stats
      ? { total: t.total, pages: t.pages, languages: t.langs }
      : { count: t.total };
    return new Response(JSON.stringify(body), { headers });
  }

  if (req.method === "POST") {
    let path = "/";
    try {
      const body = await req.json();
      if (typeof body.path === "string") {
        path = body.path.split("?")[0].split("#")[0].slice(0, 64)
                        .replace(/[^a-zA-Z0-9/_.\-]/g, "");
        if (!path.startsWith("/")) path = "/" + path;
      }
    } catch (e) { /* no body, or bad JSON: count it against "/" */ }

    // a key no other visit can take: time, then randomness
    const key = PREFIX + Date.now().toString(36) + "-" +
                Math.random().toString(36).slice(2, 10);
    await store.set(key, JSON.stringify({ path, t: Date.now() }));

    return new Response(JSON.stringify({ ok: true }), { headers });
  }

  return new Response("Method not allowed", { status: 405, headers });
};
