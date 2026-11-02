"""Assembla l'app: dist/artifact.html (anteprima su claude.ai) e dist/pwa/ (da pubblicare su GitHub Pages/Netlify)."""
import json, os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = lambda *p: open(os.path.join(ROOT, *p), encoding="utf-8").read()
mols = json.loads(src("data", "molecules.json"))
content = json.loads(src("data", "content.json"))
content["exam"] = [x for x in json.loads(src("data", "exam.json")) if not x["pending"]]
content["bank"] = json.loads(src("data", "bank.json"))
data = json.dumps({"molecules": mols, "content": content}, ensure_ascii=False, separators=(",", ":"))

page = (src("src", "index.template.html")
        .replace("/*__CSS__*/", src("src", "app.css"))
        .replace("/*__DATA__*/", data)
        .replace("/*__JS__*/", src("src", "app.js")))

os.makedirs(os.path.join(ROOT, "dist", "pwa", "icons"), exist_ok=True)
open(os.path.join(ROOT, "dist", "artifact.html"), "w", encoding="utf-8").write(page.replace("<!--PWA_HEAD-->", ""))

head = """<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" type="image/png" href="icons/icon-192.png">"""
pwa = ('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + page.replace("<!--PWA_HEAD-->", head).replace("<div class=\"app\">", "</head>\n<body>\n<div class=\"app\">", 1)
       + "</body>\n</html>\n")
# :root padding del contenitore claude.ai non c'è qui: lo gestisce già .app con le safe-area
open(os.path.join(ROOT, "dist", "pwa", "index.html"), "w", encoding="utf-8").write(pwa)

manifest = {
    "name": "Biochiquiz", "short_name": "Biochiquiz", "lang": "it",
    "description": "Quiz di Biochimica dalle sbobine del corso",
    "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
    "background_color": "#f4f6fa", "theme_color": "#f4f6fa",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-512-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
}
json.dump(manifest, open(os.path.join(ROOT, "dist", "pwa", "manifest.webmanifest"), "w"), ensure_ascii=False, indent=1)

sw = """// Service worker: app offline. Cambia VERSION a ogni aggiornamento del database.
const VERSION = "bq-%s";
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
""" % content["version"]
open(os.path.join(ROOT, "dist", "pwa", "sw.js"), "w").write(sw)
json.dump({"version": content["version"]}, open(os.path.join(ROOT, "dist", "pwa", "version.json"), "w"))

# Icone: quadrato amaranto con esagono e legame (stile "riquadro pastello" invertito)
def icon(size, maskable=False):
    s = size
    img = Image.new("RGBA", (s, s), (242, 78, 42, 255))
    d = ImageDraw.Draw(img)
    import math
    cx, cy, r = s / 2, s / 2, s * (0.24 if maskable else 0.3)
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    w = max(2, int(s * 0.045))
    d.line(pts + [pts[0]], fill=(255, 255, 255, 255), width=w, joint="curve")
    # doppio legame interno su un lato
    k = 0.72
    a, b = pts[1], pts[2]
    ia = (cx + (a[0] - cx) * k, cy + (a[1] - cy) * k); ib = (cx + (b[0] - cx) * k, cy + (b[1] - cy) * k)
    d.line([ia, ib], fill=(255, 255, 255, 255), width=w)
    dot = s * 0.05
    d.ellipse([cx - dot, cy - dot, cx + dot, cy + dot], fill=(14, 26, 51, 255))
    return img
for sz in (180, 192, 512):
    icon(sz).save(os.path.join(ROOT, "dist", "pwa", "icons", f"icon-{sz}.png"))
icon(512, True).save(os.path.join(ROOT, "dist", "pwa", "icons", "icon-512-maskable.png"))
print("ok", len(page) // 1024, "KB")
