// Where a visit comes from: the country and city (Netlify's own geolocation), the organisation that holds the network
// (looked up in the public RDAP registry), and the source of the click (the page the reader came from).
// The reader's address is used for the lookup and never stored. No cookie, no identity.
//
// Each visit is its own blob in the store "where", under a key that starts with its time, so nothing can be lost.
// When the loose list grows long, the older ones are folded into one base of counts, and the points for the map.

import { getStore } from "@netlify/blobs";
import { LAND } from "./land.mjs";

const PREFIX = "w/";
const BASE = "base";
const FOLD_AT = 1500;
const SETTLE = 5 * 60e3;

const SOURCES = [
  [/(^|\.)google\./, "Google"], [/(^|\.)bing\.com$/, "Bing"], [/duckduckgo\.com$/, "DuckDuckGo"], [/(^|\.)yandex\./, "Yandex"],
  [/(^|\.)baidu\.com$/, "Baidu"], [/(^|\.)yahoo\./, "Yahoo"], [/ecosia\.org$/, "Ecosia"], [/(^|\.)naver\.com$/, "Naver"],
  [/(^|\.)facebook\.com$|^fb\.me$/, "Facebook"], [/(^|\.)instagram\.com$/, "Instagram"], [/^t\.co$|(^|\.)x\.com$|(^|\.)twitter\.com$/, "X"],
  [/(^|\.)tiktok\.com$/, "TikTok"], [/(^|\.)youtube\.com$|^youtu\.be$/, "YouTube"], [/(^|\.)linkedin\.com$|^lnkd\.in$/, "LinkedIn"],
  [/(^|\.)reddit\.com$/, "Reddit"], [/whatsapp\.com$/, "WhatsApp"], [/(^|\.)telegram\.org$|^t\.me$/, "Telegram"],
  [/chatgpt\.com$|openai\.com$/, "ChatGPT"], [/perplexity\.ai$/, "Perplexity"], [/claude\.ai$/, "Claude"],
  [/gemini\.google\.com$/, "Gemini"], [/copilot\.microsoft\.com$/, "Copilot"],
  [/(^|\.)the420code\.org$/, "the420code.org"], [/(^|\.)whybekind\.(org|global)$/, "whybekind.global"],
  [/(^|\.)zenodo\.org$/, "Zenodo"], [/(^|\.)osf\.io$/, "OSF"], [/(^|\.)github\.com$/, "GitHub"], [/lucid\.rodeo$/, "lucid.rodeo"],
];

export function sourceOf(ref, self) {
  if (!ref) return "direct";
  let host = "";
  try { host = new URL(ref).hostname.toLowerCase(); } catch (e) { return "direct"; }
  if (!host) return "direct";
  if (host === self || host === "www." + self) return "within the site";
  for (const [re, name] of SOURCES) if (re.test(host)) return name;
  return host.replace(/^www\./, "");
}

function vcard(entity, field) {
  const card = entity && entity.vcardArray && entity.vcardArray[1];
  if (!Array.isArray(card)) return null;
  const f = card.find((x) => x[0] === field);
  return f && typeof f[3] === "string" && f[3].trim() ? f[3].trim() : null;
}

function walk(entities, out = []) {
  for (const e of entities || []) { out.push(e); walk(e.entities, out); }
  return out;
}

// The organisation that holds the reader's network, from the regional registry (RDAP); null when it cannot be told.
// Only an organisation's or a group's name is ever kept, never a person's: some registries list a home connection
// under the name of the person who holds it, and those are skipped. The network's own handle is never used either.
export async function orgOf(ip) {
  if (!ip || !/^[0-9a-fA-F:.]{3,45}$/.test(ip)) return null;
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 4500);
  try {
    const r = await fetch("https://rdap.org/ip/" + ip, { signal: ctrl.signal, redirect: "follow",
      headers: { Accept: "application/rdap+json", "User-Agent": "visit counter" } });
    if (!r.ok) return null;
    const j = await r.json();
    const all = walk(j.entities);
    const kindOf = (e) => (vcard(e, "kind") || "").toLowerCase();
    const has = (e, role) => (e.roles || []).includes(role);
    const org = all.find((e) => kindOf(e) === "org" && has(e, "registrant")) || all.find((e) => kindOf(e) === "org");
    if (org) return vcard(org, "fn").slice(0, 120);
    const group = ["registrant", "administrative", "technical", "abuse"].map((role) => all.find((e) => kindOf(e) === "group" && has(e, role))).find(Boolean);
    if (group) {
      const name = vcard(group, "fn").replace(/\b(abuse|support|technical|admin|administrative|noc|role|team|contact)\b/gi, "").replace(/\s+/g, " ").trim();
      return name ? name.slice(0, 120) : null;
    }
    return null;
  } catch (e) {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

// write one visit's place and source (called by the counter after it has counted the visit)
export async function recordWhere(req, context, path, ref, self) {
  try {
    const geo = (context && context.geo) || {};
    const ip = (context && context.ip) || req.headers.get("x-nf-client-connection-ip") || "";
    const org = await orgOf(ip);
    const rec = {
      t: Date.now(), path,
      cc: (geo.country && geo.country.code) || null,
      country: (geo.country && geo.country.name) || null,
      region: (geo.subdivision && geo.subdivision.name) || null,
      city: geo.city || null,
      lat: typeof geo.latitude === "number" ? Math.round(geo.latitude * 100) / 100 : null,
      lon: typeof geo.longitude === "number" ? Math.round(geo.longitude * 100) / 100 : null,
      org, src: sourceOf(ref, self),
    };
    const key = PREFIX + Date.now().toString(36).padStart(9, "0") + "-" + Math.random().toString(36).slice(2, 10);
    await getStore("where").set(key, JSON.stringify(rec));
  } catch (e) { /* the count stands either way */ }
}

const timeOf = (key) => parseInt(key.slice(PREFIX.length, PREFIX.length + 9), 36) || 0;
const add = (m, k, n = 1) => { if (k) m[k] = (m[k] || 0) + n; };

function emptyAgg() { return { through: 0, visits: 0, countries: {}, cities: {}, orgs: {}, sources: {}, pages: {}, days: {}, points: {}, first: 0, last: 0 }; }

function addRec(a, r) {
  a.visits += 1;
  add(a.countries, r.country ? `${r.country} (${r.cc})` : "unknown");
  add(a.cities, r.city ? `${r.city}, ${r.country || r.cc || ""}` : null);
  add(a.orgs, r.org || null);
  add(a.sources, r.src || "direct");
  add(a.pages, r.path || "/");
  add(a.days, new Date(r.t).toISOString().slice(0, 10));
  if (typeof r.lat === "number" && typeof r.lon === "number") add(a.points, `${r.lat},${r.lon}`);
  a.first = a.first ? Math.min(a.first, r.t) : r.t;
  a.last = Math.max(a.last, r.t);
}

function merge(a, b) {
  const out = emptyAgg();
  out.visits = a.visits + b.visits;
  for (const f of ["countries", "cities", "orgs", "sources", "pages", "days", "points"]) {
    out[f] = { ...a[f] };
    for (const [k, v] of Object.entries(b[f])) add(out[f], k, v);
  }
  out.first = [a.first, b.first].filter(Boolean).reduce((x, y) => Math.min(x, y), 0) || a.first || b.first;
  out.last = Math.max(a.last, b.last);
  out.through = a.through;
  return out;
}

export async function whereTally() {
  const store = getStore("where");
  let base = emptyAgg();
  try { const raw = await store.get(BASE); if (raw) base = { ...emptyAgg(), ...JSON.parse(raw) }; } catch (e) { /* start clean */ }
  const { blobs } = await store.list({ prefix: PREFIX });
  const loose = blobs.filter((b) => timeOf(b.key) > base.through);
  const bodies = await Promise.all(loose.map((b) => store.get(b.key).catch(() => null)));
  const fresh = emptyAgg(), old = emptyAgg();
  const cutoff = Date.now() - SETTLE;
  let through = base.through;
  const folded = [];
  loose.forEach((b, i) => {
    let r = null;
    try { r = JSON.parse(bodies[i]); } catch (e) { /* unreadable */ }
    const t = timeOf(b.key);
    if (r) { addRec(fresh, r); if (t <= cutoff) addRec(old, r); }
    if (t <= cutoff) { folded.push(b.key); through = Math.max(through, t); }
  });
  if (loose.length >= FOLD_AT && folded.length) {
    const nb = merge(base, old); nb.through = through;
    await store.set(BASE, JSON.stringify(nb));
    for (const k of folded) { try { await store.delete(k); } catch (e) { /* skipped by through */ } }
  }
  return merge(base, fresh);
}

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

function table(title, obj, limit = 100, byKey = false) {
  const rows = Object.entries(obj).sort((a, b) => byKey ? (a[0] < b[0] ? 1 : -1) : b[1] - a[1]).slice(0, limit);
  if (!rows.length) return `<h2>${title}</h2><p class="none">Nothing yet.</p>`;
  return `<h2>${title}</h2><table>${rows.map(([k, v]) => `<tr><td>${esc(k)}</td><td>${v.toLocaleString("en-GB")}</td></tr>`).join("")}</table>`;
}

export function whereHTML(site, a) {
  const pts = Object.entries(a.points).map(([k, n]) => { const [lat, lon] = k.split(",").map(Number); return { lat, lon, n }; });
  const dots = pts.map((p) => `<circle cx="${(p.lon + 180).toFixed(2)}" cy="${(90 - p.lat).toFixed(2)}" r="${Math.min(5, 1.6 + 1.2 * Math.log2(p.n)).toFixed(2)}"><title>${p.n}</title></circle>`).join("");
  const grid = [];
  for (let x = 0; x <= 360; x += 30) grid.push(`<line x1="${x}" y1="0" x2="${x}" y2="180"/>`);
  for (let y = 0; y <= 180; y += 30) grid.push(`<line x1="0" y1="${y}" x2="360" y2="${y}"/>`);
  const since = a.first ? new Date(a.first).toISOString().slice(0, 10) : "—";
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="light"><title>Where the readers are · ${esc(site)}</title><style>
body{margin:0;padding:24px 16px 60px;font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:#fff;color:#111;max-width:980px;margin-inline:auto}
h1{font-size:28px;margin:0 0 4px}p.sub{color:#555;margin:0 0 20px}h2{font-size:18px;margin:28px 0 8px;border-bottom:1px solid #ddd;padding-bottom:4px}
table{border-collapse:collapse;width:100%}td{padding:4px 6px;border-bottom:1px solid #f0f0f0;vertical-align:top}td:last-child{text-align:right;white-space:nowrap;width:5em}
.map{width:100%;height:auto;background:#dcebf5;border:1px solid #c9dbe8;display:block}.map .land{fill:#d2d2cc;stroke:#a9a9a2;stroke-width:.15;stroke-linejoin:round}.map line{stroke:#ffffff;stroke-opacity:.5;stroke-width:.2}.map circle{fill:#e00000;fill-opacity:.9;stroke:#fff;stroke-width:.25}
.grid{display:grid;grid-template-columns:1fr;gap:0 32px}@media(min-width:760px){.grid{grid-template-columns:1fr 1fr}}.none{color:#888}
</style></head><body><h1>Where the readers are</h1>
<p class="sub">${esc(site)} · ${a.visits.toLocaleString("en-GB")} visits recorded with their place, since ${since}. Each red dot is a city a page was read from.</p>
<svg class="map" viewBox="0 0 360 180" role="img" aria-label="The world, with a red dot for every city a page was read from"><path class="land" d="${LAND}"/>${grid.join("")}${dots}</svg>
<div class="grid"><div>${table("Countries", a.countries)}${table("Cities", a.cities, 60)}</div>
<div>${table("Where the click came from", a.sources)}${table("Organisations (the network's owner)", a.orgs, 60)}</div></div>
${table("Pages", a.pages, 60)}${table("Days", a.days, 90, true)}
</body></html>`;
}
