import { getStore } from "@netlify/blobs";

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

  // GET /.netlify/functions/download-counter?stats=1
  // Returns per-PDF breakdown for the site owner
  if (req.method === "GET" && url.searchParams.get("stats") === "1") {
    const raw = await store.get("per-file");
    const perFile = raw ? JSON.parse(raw) : {};
    const totalRaw = await store.get("downloads");
    const total = totalRaw ? parseInt(totalRaw, 10) : 0;
    return new Response(JSON.stringify({ total, files: perFile }), { headers });
  }

  // GET /.netlify/functions/download-counter
  // Returns total download count
  if (req.method === "GET") {
    const raw = await store.get("downloads");
    const count = raw ? parseInt(raw, 10) : 0;
    return new Response(JSON.stringify({ count }), { headers });
  }

  // POST /.netlify/functions/download-counter
  // Body: { "file": "AP01_The_Actualization_State.pdf" }
  // Increments total + per-file counter
  if (req.method === "POST") {
    let filename = "unknown";
    try {
      const body = await req.json();
      if (body.file) {
        // Sanitize: take only the filename, strip path components
        filename = body.file.replace(/.*\//, "").replace(/[^a-zA-Z0-9_.\-()]/g, "_");
      }
    } catch (e) {
      // If no body or invalid JSON, still increment total
    }

    // Increment total
    const totalRaw = await store.get("downloads");
    const total = (totalRaw ? parseInt(totalRaw, 10) : 0) + 1;
    await store.set("downloads", String(total));

    // Increment per-file
    const perFileRaw = await store.get("per-file");
    const perFile = perFileRaw ? JSON.parse(perFileRaw) : {};
    perFile[filename] = (perFile[filename] || 0) + 1;
    await store.set("per-file", JSON.stringify(perFile));

    return new Response(JSON.stringify({ count: total, file: filename, fileCount: perFile[filename] }), { headers });
  }

  return new Response("Method not allowed", { status: 405, headers });
};
