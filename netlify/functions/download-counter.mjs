import { getStore } from "@netlify/blobs";

export default async (req, context) => {
  const store = getStore("downloads");

  if (req.method === "GET") {
    const raw = await store.get("total");
    const count = raw ? parseInt(raw, 10) : 0;
    return new Response(JSON.stringify({ count }), {
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }

  if (req.method === "POST") {
    const raw = await store.get("total");
    const count = (raw ? parseInt(raw, 10) : 0) + 1;
    await store.set("total", String(count));
    return new Response(JSON.stringify({ count }), {
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
    });
  }

  return new Response("Method not allowed", { status: 405 });
};

export const config = {
  path: "/.netlify/functions/download-counter",
  method: ["GET", "POST"]
};
