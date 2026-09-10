import { getStore } from "@netlify/blobs";

// A visit is one browser session, not one page load. The page guards on
// sessionStorage before it posts, so a reload does not count again and the
// figure keeps meaning something. Counted from every page; shown on one.
//
// One key, one write. The total is DERIVED from the per-page map rather than
// stored beside it, so the total can never disagree with its own breakdown.
// The first version kept three keys and three writes, and a rapid pair of
// visits lost one: the total said 2 while the pages summed to 3.
//
// This is still not atomic — @netlify/blobs 8.2 has no conditional write, so
// two genuinely simultaneous visits can still collapse into one. At this site's
// traffic that is rare, and the number is honest about what it is: sessions
// that reached a page and ran the script. Crawlers do not run it.

const KEY = "visits-v2";
const LANGS = ["ar","de","es","fr","hi","it","ja","ko","nl","pt","ru","zh"];

const total = (state) => Object.values(state.pages).reduce((a, b) => a + b, 0);

async function read(store) {
  const raw = await store.get(KEY);
  if (raw) {
    try { const s = JSON.parse(raw); return { pages: s.pages || {}, langs: s.langs || {} }; }
    catch (e) { /* fall through and start clean rather than throw */ }
  }
  // carry over whatever the first version recorded, once
  const old = await store.get("visits-per-page");
  if (old) {
    try {
      const pages = JSON.parse(old);
      const langs = {};
      for (const [p, n] of Object.entries(pages)) {
        const seg = (p.split("/")[1] || "");
        const l = LANGS.includes(seg) ? seg : "en";
        langs[l] = (langs[l] || 0) + n;
      }
      return { pages, langs };
    } catch (e) { /* ignore */ }
  }
  return { pages: {}, langs: {} };
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
    const state = await read(store);
    const body = url.searchParams.get("stats") === "1"
      ? { total: total(state), pages: state.pages, languages: state.langs }
      : { count: total(state) };
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

    const seg = path.split("/")[1] || "";
    const lang = LANGS.includes(seg) ? seg : "en";

    const state = await read(store);
    state.pages[path] = (state.pages[path] || 0) + 1;
    state.langs[lang] = (state.langs[lang] || 0) + 1;
    await store.set(KEY, JSON.stringify(state));

    return new Response(JSON.stringify({ count: total(state) }), { headers });
  }

  return new Response("Method not allowed", { status: 405, headers });
};
