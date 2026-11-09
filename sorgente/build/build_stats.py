"""Riepilogo per il pannello di controllo: card per argomento e livello (dist/stats_argomenti.json, dist/stats_versione.json)."""
import json, os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda p: json.load(open(os.path.join(ROOT, p)))
C = J("data/content.json"); M = J("data/molecules.json") if os.path.exists(os.path.join(ROOT, "data/molecules.json")) else None
bank = J("data/bank.json"); exam = [x for x in J("data/exam.json") if not x.get("pending")]
cards = []  # (topic, level, kind)
mols = M["molecules"] if isinstance(M, dict) and "molecules" in M else (M or [])
for m in mols:
    t = (C["moleculeTopics"].get(m["id"]) or [None])[0]
    if t: cards.append((t, "f", "molecola")); cards.append((t, "m", "molecola-argomento"))
for r in C["reactions"]: cards.append((r["topic"], "m", "reazione"))
for p in C["pathways"]:
    for st in p["steps"]: cards.append((st.get("topic") or p["topic"], "m", "via"))
for x in exam: cards.append((x["topic"], x.get("level", "m"), "verificata"))
for x in bank: cards.append((x["topic"], x["level"], "domanda"))
rows = []
for sub in C["topics"]:
    for b in sub["blocks"]:
        for t in b["topics"]:
            cs = [c for c in cards if c[0] == t["id"]]
            n = lambda lv: sum(1 for c in cs if c[1] == lv)
            rows.append(dict(id=t["id"], materia=sub["subject"], blocco=b["name"], argomento=t["name"], pronto="sì" if t.get("ready") else "no",
                             facile=n("f"), medio=n("m"), alta=n("a"), lode=n("l"), verificate=sum(1 for c in cs if c[2] == "verificata"),
                             totale=len(cs), aggiunto=t.get("added", "")))
os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
json.dump(rows, open(os.path.join(ROOT, "dist/stats_argomenti.json"), "w"), ensure_ascii=False)
json.dump([dict(versione=C["version"], pubblicata=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))], open(os.path.join(ROOT, "dist/stats_versione.json"), "w"))
print(len(rows), "argomenti,", sum(r["totale"] for r in rows), "card,", sum(1 for r in rows if r["pronto"] == "sì"), "pronti")
