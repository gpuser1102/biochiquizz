"""Genera data/molecules.json: SMILES da PubChem (CID fissati a mano e formula verificata),
forma ionizzata a pH fisiologico e dati Haworth per gli zuccheri ciclici."""
import json, re, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import haworth as H
import fischer as F
F.CAL = 0  # calibrato sulla D-gliceraldeide 3-fosfato (OH a destra)

H.CAL = 1  # calibrato sull'alfa-D-glucopiranosio

# Risposta del 01/11/2026 a /rest/pug/compound/cid/<cids>/property/SMILES,MolecularFormula
PUBCHEM = {
    79025: ("C6H12O6", "C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O"),
    439284: ("C6H13O9P", "C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)OP(=O)(O)O"),
    440641: ("C6H13O9P", "C([C@@H]1[C@H]([C@@H]([C@](O1)(CO)O)O)O)OP(=O)(O)O"),
    10267: ("C6H14O12P2", "C([C@@H]1[C@H]([C@@H]([C@](O1)(COP(=O)(O)O)O)O)O)OP(=O)(O)O"),
    668: ("C3H7O6P", "C(C(=O)COP(=O)(O)O)O"),
    439168: ("C3H7O6P", "C([C@H](C=O)O)OP(=O)(O)O"),
    439191: ("C3H8O10P2", "C([C@H](C(=O)OP(=O)(O)O)O)OP(=O)(O)O"),
    439183: ("C3H7O7P", "C([C@H](C(=O)O)O)OP(=O)(O)O"),
    439278: ("C3H7O7P", "C([C@H](C(=O)O)OP(=O)(O)O)O"),
    1005: ("C3H5O6P", "C=C(C(=O)O)OP(=O)(O)O"),
    1060: ("C3H4O3", "CC(=O)C(=O)O"),
    970: ("C4H4O5", "C(C(=O)C(=O)O)C(=O)O"),
    222656: ("C4H6O5", "C([C@@H](C(=O)O)O)C(=O)O"),
    107689: ("C3H6O3", "C[C@@H](C(=O)O)O"),
    5950: ("C3H7NO2", "C[C@@H](C(=O)O)N"),
    753: ("C3H8O3", "C(C(CO)O)O"),
    439162: ("C3H9O6P", "C([C@H](COP(=O)(O)O)O)O"),
    # Risposta del 06/11/2026 (PubChem PUG REST, nome → CID, SMILES, formula)
    311: ("C6H8O7", "C(C(=O)O)C(CC(=O)O)(C(=O)O)O"),
    5318532: ("C6H8O7", "C([C@@H]([C@H](C(=O)O)O)C(=O)O)C(=O)O"),
    51: ("C5H6O5", "C(CC(=O)O)C(=O)C(=O)O"),
    1110: ("C4H6O4", "C(CC(=O)O)C(=O)O"),
    444972: ("C4H4O4", "C(=C/C(=O)O)\\C(=O)O"),
    65533: ("C6H13O9P", "C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)OP(=O)(O)O)O)O)O)O"),
    439709: ("C6H12O6", "C([C@@H]1[C@H]([C@@H]([C@](O1)(CO)O)O)O)O"),
    439357: ("C6H12O6", "C([C@@H]1[C@@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O"),
    185698: ("C6H12O6", "C([C@@H]1[C@H]([C@@H]([C@@H]([C@H](O1)O)O)O)O)O"),
    447634: ("C5H11O8P", "C([C@@H]1[C@H]([C@H]([C@@H](O1)O)O)O)OP(=O)(O)O"),
    439184: ("C5H11O8P", "C([C@H]([C@H](C(=O)CO)O)O)OP(=O)(O)O"),
    439190: ("C5H11O8P", "C([C@H]([C@@H](C(=O)CO)O)O)OP(=O)(O)O"),
    91493: ("C6H13O10P", "C([C@H]([C@H]([C@@H]([C@H](C(=O)O)O)O)O)O)OP(=O)(O)O"),
    122357: ("C4H9O7P", "C([C@H]([C@H](C=O)O)O)OP(=O)(O)O"),
    165007: ("C7H15O10P", "C([C@H]([C@H]([C@H]([C@@H](C(=O)CO)O)O)O)O)OP(=O)(O)O"),
    177: ("C2H4O", "CC=O"),
    702: ("C2H6O", "CCO"),
    5960: ("C4H7NO4", "C([C@@H](C(=O)O)N)C(=O)O"),
    33032: ("C5H9NO4", "C(CC(=O)O)[C@@H](C(=O)O)N"),
}

# id, nome (terminologia delle sbobine), CID, sinonimi accettati, primo C dell'anello (Haworth)
MOLS = [
    ("glc", "Glucosio", 79025, ["glucosio", "d-glucosio", "alfa-d-glucosio", "α-d-glucosio", "glucopiranosio", "alfa-d-glucopiranosio", "glc", "destrosio"], 1),
    ("g6p", "Glucosio 6-fosfato", 439284, ["glucosio 6-fosfato", "glucosio-6-p", "glucosio 6p", "g6p", "g-6-p", "alfa-d-glucosio 6-fosfato"], 1),
    ("f6p", "Fruttosio 6-fosfato", 440641, ["fruttosio 6-fosfato", "fruttosio-6-p", "f6p", "f-6-p", "beta-d-fruttosio 6-fosfato"], 2),
    ("fbp", "Fruttosio 1,6-bisfosfato", 10267, ["fruttosio 1,6-bisfosfato", "fruttosio 1-6 bisfosfato", "fruttosio bisfosfato", "fruttosio 1,6-difosfato", "fruttosio difosfato", "fbp", "f1,6bp", "f16bp", "f-1,6-bp", "f1,6p2"], 2),
    ("dhap", "Diidrossiacetone fosfato", 668, ["diidrossiacetone fosfato", "diidrossiacetone 3-fosfato", "diidrossiacetone-p", "dhap", "dap"], None),
    ("ga3p", "Gliceraldeide 3-fosfato", 439168, ["gliceraldeide 3-fosfato", "gliceraldeide-3-p", "d-gliceraldeide 3-fosfato", "ga3p", "gap", "g3p"], None),
    ("bpg13", "1,3-bisfosfoglicerato", 439191, ["1,3-bisfosfoglicerato", "1,3 bisfosfoglicerato", "1,3-bpg", "13bpg", "bpg", "1,3-difosfoglicerato", "acido 1,3-bisfosfoglicerico"], None),
    ("pg3", "3-fosfoglicerato", 439183, ["3-fosfoglicerato", "3 fosfoglicerato", "3pg", "3-pg", "acido 3-fosfoglicerico"], None),
    ("pg2", "2-fosfoglicerato", 439278, ["2-fosfoglicerato", "2 fosfoglicerato", "2pg", "2-pg", "acido 2-fosfoglicerico"], None),
    ("pep", "Fosfoenolpiruvato", 1005, ["fosfoenolpiruvato", "fosfoenol piruvato", "pep", "acido fosfoenolpiruvico"], None),
    ("pyr", "Piruvato", 1060, ["piruvato", "acido piruvico"], None),
    ("oaa", "Ossalacetato", 970, ["ossalacetato", "ossaloacetato", "oaa", "acido ossalacetico"], None),
    ("mal", "Malato", 222656, ["malato", "l-malato", "acido malico"], None),
    ("lac", "Lattato", 107689, ["lattato", "l-lattato", "acido lattico"], None),
    ("ala", "Alanina", 5950, ["alanina", "l-alanina", "ala"], None),
    ("gly", "Glicerolo", 753, ["glicerolo", "glicerina"], None),
    ("gro3p", "Glicerolo 3-fosfato", 439162, ["glicerolo 3-fosfato", "glicerolo-3-p", "glicerolo 3p", "glicerolo fosfato", "l-glicerolo 3-fosfato", "glicerolo 1-fosfato"], None),
    ("cit", "Citrato", 311, ["citrato", "acido citrico"], None),
    ("icit", "Isocitrato", 5318532, ["isocitrato", "acido isocitrico", "d-isocitrato", "treo-d-isocitrato"], None),
    ("akg", "α-chetoglutarato", 51, ["alfa-chetoglutarato", "α-chetoglutarato", "a-chetoglutarato", "chetoglutarato", "2-ossoglutarato", "ossoglutarato", "akg", "acido alfa-chetoglutarico"], None),
    ("suc", "Succinato", 1110, ["succinato", "acido succinico"], None),
    ("fum", "Fumarato", 444972, ["fumarato", "acido fumarico"], None),
    ("g1p", "Glucosio 1-fosfato", 65533, ["glucosio 1-fosfato", "glucosio-1-p", "glucosio 1p", "g1p", "g-1-p", "alfa-d-glucosio 1-fosfato"], 1),
    ("fru", "Fruttosio", 439709, ["fruttosio", "d-fruttosio", "beta-d-fruttosio", "fruttofuranosio", "beta-d-fruttofuranosio", "levulosio"], 2),
    ("gal", "Galattosio", 439357, ["galattosio", "d-galattosio", "alfa-d-galattosio", "galattopiranosio", "alfa-d-galattopiranosio"], 1),
    ("man", "Mannosio", 185698, ["mannosio", "d-mannosio", "alfa-d-mannosio", "mannopiranosio", "alfa-d-mannopiranosio"], 1),
    ("r5p", "Ribosio 5-fosfato", 447634, ["ribosio 5-fosfato", "ribosio-5-p", "ribosio 5p", "r5p", "beta-d-ribosio 5-fosfato", "d-ribosio 5-fosfato"], 1),
    ("ru5p", "Ribulosio 5-fosfato", 439184, ["ribulosio 5-fosfato", "ribulosio-5-p", "ribulosio 5p", "ru5p", "d-ribulosio 5-fosfato"], None),
    ("xu5p", "Xilulosio 5-fosfato", 439190, ["xilulosio 5-fosfato", "xilulosio-5-p", "xilulosio 5p", "xu5p", "d-xilulosio 5-fosfato"], None),
    ("pg6", "6-fosfogluconato", 91493, ["6-fosfogluconato", "6 fosfogluconato", "fosfogluconato", "6pg", "6-pg", "acido 6-fosfogluconico"], None),
    ("e4p", "Eritrosio 4-fosfato", 122357, ["eritrosio 4-fosfato", "eritrosio-4-p", "eritrosio 4p", "e4p", "d-eritrosio 4-fosfato"], None),
    ("s7p", "Sedoeptulosio 7-fosfato", 165007, ["sedoeptulosio 7-fosfato", "sedoeptulosio-7-p", "sedoeptulosio 7p", "s7p", "sedoeptulosio"], None),
    ("acal", "Acetaldeide", 177, ["acetaldeide", "etanale", "aldeide acetica"], None),
    ("etoh", "Etanolo", 702, ["etanolo", "alcol etilico", "alcool etilico"], None),
    ("asp", "Aspartato", 5960, ["aspartato", "l-aspartato", "acido aspartico", "asp"], None),
    ("glu", "Glutammato", 33032, ["glutammato", "l-glutammato", "acido glutammico", "glu", "glutamato"], None),
]


def ionize(s):
    s = re.sub(r"P\(=O\)\(O\)O(?=\)|$)", "P(=O)([O-])[O-]", s)   # fosfato monoestere -> 2-
    s = re.sub(r"C\(=O\)O(?=\)|$)", "C(=O)[O-]", s)               # carbossile -> carbossilato
    s = re.sub(r"N$", "[NH3+]", s)                                  # ammina primaria terminale
    return s


def label(i, atoms):
    a = atoms[i]
    if a["el"] == "O":
        nb = [n for n in a["nbrs"] if isinstance(n, int)]
        return "OPO₃²⁻" if any(atoms[n]["el"] == "P" for n in nb) else "OH"
    if a["el"] == "C":
        for n in a["nbrs"]:
            if isinstance(n, int) and atoms[n]["el"] == "O":
                return "CH₂" + label(n, atoms)
    return a["el"]


out = []
for mid, name, cid, syn, c0 in MOLS:
    formula, smi = PUBCHEM[cid]
    m = {"id": mid, "name": name, "cid": cid, "formula": formula, "smiles": smi,
         "smilesIon": ionize(smi), "aliases": syn}
    if c0:
        hw = H.haworth(smi, label)
        hw["firstC"] = c0
        m["haworth"] = hw
    else:
        m["fischer"] = F.fischer(smi, {"dhap": "P", "gro3p": "OH"}.get(mid))
    out.append(m)

json.dump(out, open(__file__.rsplit("/", 2)[0] + "/data/molecules.json", "w"), ensure_ascii=False, indent=1)
for m in out:
    print(m["id"], "haworth" if "haworth" in m else "fischer", len(m.get("fischer", [])))
