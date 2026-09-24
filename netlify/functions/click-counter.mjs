// A count of clicks on the few buttons whose use is a question, and nothing else.
//
// G, 24 September 2026, on the mailing list: "maybe keep stay in the loop — we must just see if
// anyone ever clicked on it." Nothing on this site counted that. It does now.
//
// What is stored is a label and a number. No address, no identity, no page, no time. The labels are
// fixed below; anything else is counted as "other" and dropped. Same store as the other two
// counters, a different key, so nothing already counted moves.
import { getStore } from "@netlify/blobs";

const LABELS = new Set(["subscribe", "support-card", "support-open"]);

export default async (req, context) => {
  const store = getStore("counters");
  const url = new URL(req.url);
  const headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };

  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers });
  }

  // GET — every label and its count, for the site's owner
  if (req.method === "GET") {
    const raw = await store.get("clicks");
    const clicks = raw ? JSON.parse(raw) : {};
    const total = Object.values(clicks).reduce((a, b) => a + b, 0);
    return new Response(JSON.stringify({ total, clicks }), { headers });
  }

  // POST — Body: { "label": "subscribe" }
  if (req.method === "POST") {
    let label = "other";
    try {
      const body = await req.json();
      if (body.label && LABELS.has(String(body.label))) label = String(body.label);
    } catch (e) {
      // no body, or not JSON: it still counts as a click on something
    }
    if (label === "other") {
      return new Response(JSON.stringify({ ok: true, counted: false }), { headers });
    }
    const raw = await store.get("clicks");
    const clicks = raw ? JSON.parse(raw) : {};
    clicks[label] = (clicks[label] || 0) + 1;
    await store.set("clicks", JSON.stringify(clicks));
    return new Response(JSON.stringify({ ok: true, label, count: clicks[label] }), { headers });
  }

  return new Response("Method not allowed", { status: 405, headers });
};
