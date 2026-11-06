"""Formula condensata verticale (stile Fischer/Lehninger) dalle SMILES di PubChem.

Ogni carbonio della catena è una riga: [sinistra] — C(Hn) — [destra], legame verticale singolo o doppio
verso il carbonio sotto. Negli stereocentri la posizione destra/sinistra di OH, NH3+ ecc. è calcolata
dalla chiralità della SMILES (proiezione di Fischer: verticali indietro, orizzontali verso chi guarda).
"""
import re

TOKEN = re.compile(r"\[[^\]]+\]|Cl|Br|[BCNOPSFI]|\(|\)|=|#|\d")
VAL = {"C": 4, "N": 3, "O": 2, "P": 5, "S": 2}


def parse(smiles):
    atoms, bonds = [], {}
    stack, prev, rings, order = [], None, {}, 1
    for tok in TOKEN.findall(smiles):
        if tok == "(":
            stack.append(prev); continue
        if tok == ")":
            prev = stack.pop(); continue
        if tok == "=":
            order = 2; continue
        if tok == "#":
            order = 3; continue
        if tok.isdigit():
            if tok in rings:
                other, o2 = rings.pop(tok)
                atoms[prev]["nbrs"].append(other)
                idx = atoms[other]["nbrs"].index(("ring", tok))
                atoms[other]["nbrs"][idx] = prev
                bonds[frozenset((prev, other))] = max(order, o2)
            else:
                rings[tok] = (prev, order)
                atoms[prev]["nbrs"].append(("ring", tok))
            order = 1
            continue
        el, chiral, h, bracket = tok, None, None, False
        if tok.startswith("["):
            bracket = True
            m = re.match(r"\[([A-Z][a-z]?)(@@|@)?(H(\d)?)?", tok)
            el, chiral = m.group(1), m.group(2)
            h = int(m.group(4) or 1) if m.group(3) else 0
        a = {"el": el, "chiral": chiral, "nbrs": [], "i": len(atoms), "h": h}
        atoms.append(a)
        i = a["i"]
        if prev is not None:
            a["nbrs"].append(prev)
            atoms[prev]["nbrs"].append(i)
            bonds[frozenset((prev, i))] = order
        if bracket and h:
            a["nbrs"].append("H")
        prev, order = i, 1
    for a in atoms:  # idrogeni impliciti degli atomi organici
        if a["h"] is None:
            used = sum(bonds[frozenset((a["i"], n))] for n in a["nbrs"] if isinstance(n, int))
            a["h"] = max(0, VAL.get(a["el"], 0) - used)
    return atoms, bonds


def parity(seq, ref):
    s = [ref.index(x) for x in seq]
    p = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            p ^= s[i] > s[j]
    return p


CAL = 0
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def fischer(smiles, top=None):
    atoms, bonds = parse(smiles)
    B = lambda a, b: bonds.get(frozenset((a, b)), 0)
    C = [a["i"] for a in atoms if a["el"] == "C"]
    cn = {i: [n for n in atoms[i]["nbrs"] if isinstance(n, int) and atoms[n]["el"] == "C"] for i in C}
    ends = [i for i in C if len(cn[i]) <= 1]

    def ox(i):  # "grado di ossidazione" del carbonio: legami verso O
        return sum(B(i, n) for n in atoms[i]["nbrs"] if isinstance(n, int) and atoms[n]["el"] == "O")

    def has_P(i):
        return any(isinstance(n, int) and atoms[n]["el"] == "O" and any(isinstance(m, int) and atoms[m]["el"] == "P" for m in atoms[n]["nbrs"]) for n in atoms[i]["nbrs"])

    def nN(i):
        return sum(1 for n in atoms[i]["nbrs"] if isinstance(n, int) and atoms[n]["el"] == "N")

    def longest(start):
        """Catena di carboni più lunga a partire da un'estremità (per molecole ramificate come il citrato)."""
        best = [start]
        def dfs(path):
            nonlocal best
            if len(path) > len(best): best = list(path)
            for n in cn[path[-1]]:
                if n not in path: dfs(path + [n])
        dfs([start])
        return best

    def score(e):
        nb = cn[e][0] if cn[e] else None
        s = (len(longest(e)), ox(e), ox(nb) if nb is not None else 0, nN(nb) if nb is not None else 0)
        if top == "P":
            s = (has_P(e),) + s
        elif top == "OH":
            s = (not has_P(e),) + s
        return s
    start = max(ends, key=score) if len(ends) > 1 else ends[0]
    chain = longest(start)

    def grp(o, side):
        """Etichetta di un sostituente legato con legame singolo (ionizzato a pH 7,4)."""
        a = atoms[o]
        if a["el"] == "O":
            onb = [n for n in a["nbrs"] if isinstance(n, int)]
            if any(atoms[n]["el"] == "P" for n in onb):
                return "OPO₃²⁻" if side == "R" else "²⁻O₃PO"
            return "OH" if side == "R" else "HO"
        if a["el"] == "N":
            return "NH₃⁺" if side == "R" else "⁺H₃N"
        if a["el"] == "C":
            oo = [n for n in a["nbrs"] if isinstance(n, int) and atoms[n]["el"] == "O"]
            if len(oo) == 2:
                return "COO⁻" if side == "R" else "⁻OOC"
            hh = a["h"]
            return ("CH" + (str(hh).translate(SUB) if hh > 1 else "")) if side == "R" else ("H" + (str(hh).translate(SUB) if hh > 1 else "") + "C")
        return a["el"]

    rows = []
    for k, i in enumerate(chain):
        a = atoms[i]
        up = chain[k - 1] if k else None
        dn = chain[k + 1] if k + 1 < len(chain) else None
        subs = [n for n in a["nbrs"] if isinstance(n, int) and n not in (up, dn)]
        dbl = [n for n in subs if B(i, n) == 2 and atoms[n]["el"] == "O"]
        sgl = [n for n in subs if n not in dbl]
        hn = a["h"]
        row = {"c": "C", "l": "", "r": "", "lb": 1, "rb": 1}
        terminal = up is None or dn is None
        if terminal and dbl and len(sgl) == 1 and atoms[sgl[0]]["el"] == "O" and len([m for m in atoms[sgl[0]]["nbrs"] if isinstance(m, int)]) == 1:
            row["c"] = "COO⁻"                                  # carbossilato
        elif terminal and dbl and len(sgl) == 1:
            row.update(l="O", lb=2, r=grp(sgl[0], "R"))         # acil fosfato (1,3-BPG)
        elif terminal and dbl and hn == 1:
            row.update(l="H", r="O", rb=2)                       # aldeide: H—C═O
        elif terminal and not dbl and hn >= 2:
            row["c"] = "CH" + (str(hn).translate(SUB) if hn > 1 else "") + (grp(sgl[0], "R") if sgl else "")
        elif dbl:                                                # chetone interno
            row.update(r="O", rb=2)
        elif hn == 2 and not sgl:
            row["c"] = "CH₂"
        elif hn == 1 and len(sgl) == 1:                          # stereocentro (o CHOH achirale)
            X = sgl[0]
            right = True
            if a["chiral"] and up is not None and dn is not None:
                right = (parity([up, dn, X, "H"], a["nbrs"]) ^ (a["chiral"] == "@@") ^ CAL) == 1
            row.update(l="H" if right else grp(X, "L"), r=grp(X, "R") if right else "H")
        elif hn == 0 and len(sgl) == 1:                          # es. C2 del PEP
            row["r"] = grp(sgl[0], "R")
        elif hn == 0 and len(sgl) == 2:                          # es. C3 del citrato: OH e COO⁻
            o = [n for n in sgl if atoms[n]["el"] == "O"]
            c = [n for n in sgl if n not in o]
            if o and c:
                row.update(l=grp(o[0], "L"), r=grp(c[0], "R"))
            else:
                row.update(l=grp(sgl[0], "L"), r=grp(sgl[1], "R"))
        else:
            row["c"] = "C" + ("H" + (str(hn).translate(SUB) if hn > 1 else "") if hn else "")
        if not row["l"]: row["lb"] = 0
        if not row["r"]: row["rb"] = 0
        row["down"] = B(i, dn) if dn is not None else 0
        rows.append(row)
    return rows
