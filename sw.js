// Service worker: app offline. Cambia VERSION a ogni aggiornamento del database.
const VERSION = "bq-0.7.1";
const SHELL = ["./", "index.html", "manifest.webmanifest", "icons/icon-180.png", "icons/icon-192.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  if (new URL(e.request.url).pathname.endsWith("version.json")) return; // sempre dalla rete
  // pagina: prima la rete (per ricevere le domande nuove), poi la cache se offline
  if (e.request.mode === "navigate") {
    e.respondWith(fetch(e.request).then(r => { const cp = r.clone(); caches.open(VERSION).then(c => c.put("index.html", cp)); return r; })
      .catch(() => caches.match("index.html")));
    return;
  }
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
    if (r.ok || r.type === "opaque") { const cp = r.clone(); caches.open(VERSION).then(c => c.put(e.request, cp)); }
    return r;
  })));
});
