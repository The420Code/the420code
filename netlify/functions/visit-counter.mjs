import { getStore } from "@netlify/blobs";

// A visit is one browser session, not one page load. The page guards on
// sessionStorage before it posts, so a reload does not inflate the number and
// the figure keeps meaning something. Counted from every page; shown on one.

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

  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers });
  }

  // GET ?stats=1 — the per-page and per-language breakdown, for the site owner
  if (req.method === "GET" && url.searchParams.get("stats") === "1") {
    const [totalRaw, pagesRaw, langsRaw] = await Promise.all([
      store.get("visits"),
      store.get("visits-per-page"),
      store.get("visits-per-lang"),
    ]);
    return new Response(JSON.stringify({
      total: totalRaw ? parseInt(totalRaw, 10) : 0,
      pages: pagesRaw ? JSON.parse(pagesRaw) : {},
      languages: langsRaw ? JSON.parse(langsRaw) : {},
    }), { headers });
  }

  // GET — the total
  if (req.method === "GET") {
    const raw = await store.get("visits");
    return new Response(JSON.stringify({ count: raw ? parseInt(raw, 10) : 0 }), { headers });
  }

  // POST { "path": "/proofs/" } — one visit
  if (req.method === "POST") {
    let path = "/";
    try {
      const body = await req.json();
      if (typeof body.path === "string") {
        // keep a short, safe path; never a query string, never a fragment
        path = body.path.split("?")[0].split("#")[0].slice(0, 64)
                        .replace(/[^a-zA-Z0-9/_.\-]/g, "");
        if (!path.startsWith("/")) path = "/" + path;
      }
    } catch (e) {
      // no body, or bad JSON: still count the visit against "/"
    }

    // the language edition is the first path segment when it is a known one
    const seg = path.split("/")[1] || "";
    const lang = ["ar","de","es","fr","hi","it","ja","ko","nl","pt","ru","zh"]
                   .includes(seg) ? seg : "en";

    const [totalRaw, pagesRaw, langsRaw] = await Promise.all([
      store.get("visits"),
      store.get("visits-per-page"),
      store.get("visits-per-lang"),
    ]);

    const total = (totalRaw ? parseInt(totalRaw, 10) : 0) + 1;
    const pages = pagesRaw ? JSON.parse(pagesRaw) : {};
    const langs = langsRaw ? JSON.parse(langsRaw) : {};
    pages[path] = (pages[path] || 0) + 1;
    langs[lang] = (langs[lang] || 0) + 1;

    await Promise.all([
      store.set("visits", String(total)),
      store.set("visits-per-page", JSON.stringify(pages)),
      store.set("visits-per-lang", JSON.stringify(langs)),
    ]);

    return new Response(JSON.stringify({ count: total }), { headers });
  }

  return new Response("Method not allowed", { status: 405, headers });
};
