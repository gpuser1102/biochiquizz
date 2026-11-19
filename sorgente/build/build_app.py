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

# Icona: fondo indaco sfumato con alone, esagono bianco pieno appena sollevato (ombra morbida),
# anello aromatico arancione. Disegnata a 4x e ridotta (bordi morbidi). Stesso disegno di LOGO_SVG in app.js.
def icon(size, maskable=False):
    import math
    import numpy as np
    from PIL import ImageFilter, ImageChops
    S = size * 4
    yy, xx = np.mgrid[0:S, 0:S] / S
    def rgba(arr, alpha):
        return Image.fromarray(np.dstack([np.clip(arr, 0, 255), np.clip(alpha, 0, 255)]).astype("uint8"), "RGBA")
    # fondo: indaco diagonale + alone chiaro in alto a sinistra + leggera vignetta in basso
    t = ((xx * .45 + yy * .55))[..., None]
    rgb = np.array([118, 108, 255]) * (1 - t) + np.array([52, 44, 186]) * t
    g = np.clip(1 - np.hypot(xx - .2, yy - .1) / .8, 0, 1)[..., None] ** 2 * .3
    rgb = rgb * (1 - g) + 255 * g
    img = rgba(rgb, np.full((S, S, 1), 255))
    k = 0.8 if maskable else 1.0
    cx, cy, R = S / 2, S / 2 + S * .01 * k, S * .31 * k
    hexpts = lambda r, ox=0, oy=0: [(cx + ox + r * math.cos(math.radians(a)), cy + oy + r * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    def mask(draw_fn):
        m = Image.new("L", (S, S), 0); draw_fn(ImageDraw.Draw(m)); return m
    def rounded_hex(d, r, fill, ox=0, oy=0, rad=None):
        rad = rad or r * .16
        pts = hexpts(r - rad / math.cos(math.radians(30)) * 0, ox, oy)
        d.polygon(pts, fill=fill); w = int(rad * 2)
        d.line(pts + [pts[0]], fill=fill, width=w, joint="curve")
        for p in pts: d.ellipse([p[0] - rad, p[1] - rad, p[0] + rad, p[1] + rad], fill=fill)
    rr = R * .86  # raggio dell'esagono "pieno", gli angoli arrotondati arrivano a ~R
    # ombra morbida sotto il vetro
    sh = mask(lambda d: rounded_hex(d, rr, 255, 0, S * .03 * k)).filter(ImageFilter.GaussianBlur(S * .035))
    img.alpha_composite(rgba(np.zeros((S, S, 3)) + [20, 12, 90], np.array(sh)[..., None] * .3))
    # vetro: bianco traslucido più denso in alto
    body = mask(lambda d: rounded_hex(d, rr, 255))
    a = np.array(body)[..., None] / 255 * 0.09
    img.alpha_composite(rgba(np.full((S, S, 3), 255), a * 255))
    # bordo luminoso: anello tra esagono e versione interna, più chiaro in alto a sinistra
    inner = mask(lambda d: rounded_hex(d, rr - S * .036 * k, 255))
    rim = np.array(ImageChops.subtract(body, inner))[..., None] / 255
    tint = np.array([255, 255, 255]) * (1 - yy[..., None] * .25) + np.array([226, 224, 255]) * (yy[..., None] * .25)
    img.alpha_composite(rgba(tint, rim * 255))
    # riflesso speculare: ellisse sfumata nella metà alta del vetro
    spec = mask(lambda d: d.ellipse([cx - rr * .95, cy - rr * 1.25, cx + rr * .6, cy - rr * .05], fill=255)).filter(ImageFilter.GaussianBlur(S * .03))
    sa = np.minimum(np.array(spec), np.array(inner))[..., None] / 255 * .0
    img.alpha_composite(rgba(np.full((S, S, 3), 255), sa * 255))
    # anello aromatico arancione: alone, anello con sfumatura, filo di luce in alto
    ring_r, ring_w = rr * .47, S * .052 * k
    ring = lambda d, col, w, r=ring_r: d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=int(w))
    glow = mask(lambda d: ring(d, 255, ring_w * 1.6)).filter(ImageFilter.GaussianBlur(S * .03))
    img.alpha_composite(rgba(np.zeros((S, S, 3)) + [255, 120, 40], np.array(glow)[..., None] * .22))
    rm = np.array(mask(lambda d: ring(d, 255, ring_w)))[..., None] / 255
    tt = np.clip((yy[..., None] - (cy - ring_r) / S) / (2 * ring_r / S), 0, 1)
    rcol = np.array([255, 140, 50]) * (1 - tt) + np.array([245, 105, 20]) * tt
    img.alpha_composite(rgba(rcol, rm * 255))
    hl = mask(lambda d: d.arc([cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r], 200, 290, fill=255, width=int(ring_w * .35))).filter(ImageFilter.GaussianBlur(S * .004))
    img.alpha_composite(rgba(np.full((S, S, 3), 255), np.array(hl)[..., None] * .0))
    # filo di luce sul bordo alto del quadrato (effetto vetro anche sul fondo)
    edge = np.clip(1 - yy / .018, 0, 1)[..., None] * 0
    img.alpha_composite(rgba(np.full((S, S, 3), 255), edge * 255))
    return img.resize((size, size), Image.LANCZOS).convert("RGB")
# Schermate di avvio per iPhone (al posto del lampo bianco): sfondo del tema, icona e nome al centro.
# (larghezza CSS, altezza CSS, densità) dei modelli più diffusi, in verticale.
SPLASH = [(375, 667, 2), (414, 896, 2), (375, 812, 3), (414, 896, 3), (390, 844, 3), (428, 926, 3),
          (393, 852, 3), (430, 932, 3), (402, 874, 3), (440, 956, 3), (360, 780, 3)]
splash_links = []
_ICON_BIG = []
def splash(w, h, dpr, dark):
    from PIL import ImageFont
    W, H = w * dpr, h * dpr
    img = Image.new("RGB", (W, H), (11, 11, 18) if dark else (245, 245, 250))
    n = int(96 * dpr)
    if not _ICON_BIG: _ICON_BIG.append(icon(640))
    ic = _ICON_BIG[0].resize((n, n), Image.LANCZOS)
    m = Image.new("L", (n * 4, n * 4), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, n * 4 - 1, n * 4 - 1], radius=int(n * 4 * .225), fill=255)
    img.paste(ic, ((W - n) // 2, int(H * .42) - n // 2), m.resize((n, n), Image.LANCZOS))
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(26 * dpr))
        d = ImageDraw.Draw(img); tw = d.textlength("Biochiquiz", font=f)
        d.text(((W - tw) / 2, int(H * .42) + n // 2 + 18 * dpr), "Biochiquiz", font=f, fill=(238, 238, 246) if dark else (22, 22, 42))
    except OSError: pass
    return img
for w, h, dpr in SPLASH:
    for dark in (False, True):
        fn = f"splash-{w * dpr}x{h * dpr}{'-dark' if dark else ''}.png"
        splash(w, h, dpr, dark).save(os.path.join(ROOT, "dist", "pwa", "icons", fn), optimize=True)
        media = f"(device-width: {w}px) and (device-height: {h}px) and (-webkit-device-pixel-ratio: {dpr}) and (orientation: portrait) and (prefers-color-scheme: {'dark' if dark else 'light'})"
        splash_links.append(f'<link rel="apple-touch-startup-image" media="{media}" href="icons/{fn}">')

head = """<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" type="image/png" href="icons/icon-192.png">
""" + "\n".join(splash_links)
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
    "background_color": "#f5f5fa", "theme_color": "#f5f5fa",
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

for sz in (180, 192, 512):
    icon(sz).save(os.path.join(ROOT, "dist", "pwa", "icons", f"icon-{sz}.png"))
icon(512, True).save(os.path.join(ROOT, "dist", "pwa", "icons", "icon-512-maskable.png"))
print("ok", len(page) // 1024, "KB")
