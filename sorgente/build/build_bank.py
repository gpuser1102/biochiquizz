"""Raccoglie tutte le banche bank_m*.py in data/bank.json e controlla gli ID."""
import json, os, sys, importlib, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bank_common
for f in sorted(glob.glob(os.path.join(HERE, "bank_m*.py"))):
    importlib.import_module(os.path.basename(f)[:-3])
B = bank_common.BANK
ids = [x["id"] for x in B]; dup = {i for i in ids if ids.count(i) > 1}
assert not dup, dup
json.dump(B, open(os.path.join(os.path.dirname(HERE), "data", "bank.json"), "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(B), "domande", dict(Counter(x["level"] for x in B)))
print(dict(Counter(x["topic"] for x in B)))
