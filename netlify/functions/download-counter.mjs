import { getStore } from "@netlify/blobs";

export default async (req, context) => {
  const store = getStore("counters");
  const key = "downloads";

  if (req.method === "GET") {
    const raw = await store.get(key);
    const count = raw ? parseInt(raw, 10) : 0;
    return new Response(JSON.stringify({ count }), {
      headers: { "Content-Type": "application/json" },
    });
  }

  if (req.method === "POST") {
    const raw = await store.get(key);
    const count = (raw ? parseInt(raw, 10) : 0) + 1;
    await store.set(key, String(count));
    return new Response(JSON.stringify({ count }), {
      headers: { "Content-Type": "application/json" },
    });
  }

  return new Response("Method not allowed", { status: 405 });
};
