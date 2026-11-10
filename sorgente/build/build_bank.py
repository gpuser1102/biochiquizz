"""Raccoglie tutte le banche bank_m*.py in data/bank.json e controlla gli ID."""
import json, os, sys, importlib, glob, difflib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bank_common
for f in sorted(glob.glob(os.path.join(HERE, "bank_m*.py"))):
    importlib.import_module(os.path.basename(f)[:-3])
B = bank_common.BANK
ids = [x["id"] for x in B]; dup = {i for i in ids if ids.count(i) > 1}
assert not dup, dup
# revisione opzioni: 5 per domanda, risposta giusta non riconoscibile dalla lunghezza
ADD, NEW, LONG = {}, {}, {}
for f in sorted(glob.glob(os.path.join(HERE, "opts_v2_*.py"))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    for k in m.ADD: assert k not in ADD and k not in NEW, k
    for k in m.NEW: assert k not in ADD and k not in NEW, k
    ADD.update(m.ADD); NEW.update(m.NEW); LONG.update(getattr(m, "LONG", {})); LONG2 = getattr(m, "LONG2", None) or globals().get("LONG2", {})
byid = {x["id"]: x for x in B}
for k in list(ADD) + list(NEW) + list(LONG): assert k in byid, k
for x in B:
    if x["id"] in NEW:
        o = NEW[x["id"]]
        assert len(o) == 5 and len(set(o)) == 5, x["id"]
        x["opts"], x["ans"] = list(o), 0
    elif x["id"] in ADD:
        assert ADD[x["id"]] not in x["opts"], x["id"]
        x["opts"] = x["opts"] + [ADD[x["id"]]]
for x in B:
    if x["id"] in LONG:
        dis = [i for i in range(len(x["opts"])) if i != x["ans"]]
        new = LONG[x["id"]]
        if new in x["opts"]: print("DUP", x["id"]); continue
        # se il distrattore lungo estende uno già presente, sostituisce quello; altrimenti il più corto
        # se il distrattore lungo è una variante di uno già presente, sostituisce quello; altrimenti il più corto
        sim = {i: difflib.SequenceMatcher(None, new.lower(), x["opts"][i].lower()).ratio() for i in dis}
        best = max(dis, key=lambda i: sim[i])
        target = best if sim[best] > 0.6 else min(dis, key=lambda i: len(x["opts"][i]))
        x["opts"][target] = new
for x in B:
    if x["id"] in LONG2:
        dis = [i for i in range(len(x["opts"])) if i != x["ans"]]
        new = LONG2[x["id"]]
        assert new not in x["opts"], x["id"]
        # se il distrattore lungo è una variante di uno già presente, sostituisce quello; altrimenti il più corto
        sim = {i: difflib.SequenceMatcher(None, new.lower(), x["opts"][i].lower()).ratio() for i in dis}
        best = max(dis, key=lambda i: sim[i])
        target = best if sim[best] > 0.6 else min(dis, key=lambda i: len(x["opts"][i]))
        x["opts"][target] = new
# revisione 3: distrattori riscritti con lunghezza e struttura simili alla giusta (la giusta resta invariata)
FIX = {}
for f in sorted(glob.glob(os.path.join(HERE, "opts_v3_*.py"))):
    m = importlib.import_module(os.path.basename(f)[:-3])
    F = getattr(m, "FIX", {})
    for k in F: assert k not in FIX, k
    FIX.update(F)
for f in sorted(glob.glob(os.path.join(HERE, "opts_v3_*.py"))):
    FIX.update(getattr(importlib.import_module(os.path.basename(f)[:-3]), "OVERRIDE", {}))
for k, d in FIX.items():
    x = byid[k]; c = x["opts"][x["ans"]]
    assert not x["fixed"] and len(d) == 4 and len(set(d)) == 4 and c not in d, k
    x["opts"], x["ans"] = [c] + list(d), 0
PATCH = {}
for f in sorted(glob.glob(os.path.join(HERE, "opts_v3_*.py"))):
    for k, v in getattr(importlib.import_module(os.path.basename(f)[:-3]), "PATCH", {}).items():
        assert k not in PATCH, k
        PATCH[k] = v
for k, rep in PATCH.items():
    x = byid[k]
    for old_t, new_t in rep.items():
        assert old_t in x["opts"], (k, old_t)
        i = x["opts"].index(old_t)
        assert i != x["ans"] and new_t not in x["opts"], k
        x["opts"][i] = new_t
miss = [x["id"] for x in B if len(x["opts"]) != 5]
assert all(len(x["opts"]) in (4, 5) for x in B)
if miss: print(f"ancora a 4 opzioni: {len(miss)} domande (da completare)")
lun = [x for x in B if len(x["opts"][x["ans"]]) > max(len(o) for i, o in enumerate(x["opts"]) if i != x["ans"])]
pos = {}
for x in B:
    L = sorted((len(o) for o in x["opts"]), reverse=True); pos[L.index(len(x["opts"][x["ans"]]))] = pos.get(L.index(len(x["opts"][x["ans"]])), 0) + 1
print("posizione della giusta per lunghezza (0 = la più lunga):", dict(sorted(pos.items())))
print(f"giusta strettamente più lunga: {len(lun)}/{len(B)} ({len(lun)/len(B):.0%})")
for x in lun:
    print("  LUNGA", x["id"], len(x["opts"][x["ans"]]), max(len(o) for i, o in enumerate(x["opts"]) if i != x["ans"]))
json.dump(B, open(os.path.join(os.path.dirname(HERE), "data", "bank.json"), "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(B), "domande", dict(Counter(x["level"] for x in B)))
print(dict(Counter(x["topic"] for x in B)))
