"""Mini parser SMILES per ricavare la proiezione di Haworth dalla stereochimica di PubChem.

Supporta il sottoinsieme di SMILES usato dagli zuccheri fosforilati (atomi organici,
parentesi quadre, rami, chiusure d'anello a una cifra, @/@@).
Per ogni carbonio dell'anello calcola se il sostituente principale sta SOPRA o SOTTO
il piano, con l'anello percorso come in Haworth (O dietro a destra, carbonio anomerico a destra).
"""
import re

TOKEN = re.compile(r"\[[^\]]+\]|Cl|Br|[BCNOPSFI]|[cnops]|\(|\)|=|#|\d|-|\+")


def parse(smiles):
    atoms = []  # dict: el, chiral, hcount, nbrs (ordered, 'H' for implicit H in brackets)
    stack, prev, rings = [], None, {}
    for tok in TOKEN.findall(smiles):
        if tok == "(":
            stack.append(prev)
        elif tok == ")":
            prev = stack.pop()
        elif tok in "=#-":
            continue
        elif tok.isdigit():
            if tok in rings:
                other = rings.pop(tok)
                atoms[prev]["nbrs"].append(other)
                # nell'atomo che ha aperto l'anello, il vicino occupa il posto della cifra
                idx = atoms[other]["nbrs"].index(("ring", tok))
                atoms[other]["nbrs"][idx] = prev
            else:
                rings[tok] = prev
                atoms[prev]["nbrs"].append(("ring", tok))
        else:
            el, chiral, h = tok, None, 0
            if tok.startswith("["):
                m = re.match(r"\[([A-Z][a-z]?)(@@|@)?(H(\d)?)?", tok)
                el, chiral = m.group(1), m.group(2)
                if m.group(3):
                    h = int(m.group(4) or 1)
            a = {"el": el, "chiral": chiral, "nbrs": [], "i": len(atoms)}
            atoms.append(a)
            i = a["i"]
            if prev is not None:
                a["nbrs"].append(prev)
                atoms[prev]["nbrs"].append(i)
            if h:
                a["nbrs"].append("H")
            prev = i
    return atoms


def perm_parity(seq, ref):
    """0 se seq è una permutazione pari di ref, 1 se dispari."""
    s = [ref.index(x) for x in seq]
    p = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                p ^= 1
    return p


def ring_atoms(atoms):
    """Trova l'anello (5 o 6 atomi) con un ossigeno."""
    adj = {a["i"]: [n for n in a["nbrs"] if isinstance(n, int)] for a in atoms}
    for start in adj:
        if atoms[start]["el"] != "O":
            continue
        # BFS per il ciclo più corto che passa da start
        for first in adj[start]:
            path = [start, first]
            def dfs(p):
                if len(p) > 6:
                    return None
                for n in adj[p[-1]]:
                    if n == start and len(p) >= 5:
                        return p
                    if n not in p:
                        r = dfs(p + [n])
                        if r:
                            return r
                return None
            r = dfs(path)
            if r:
                return r
    return None


def haworth(smiles, labels):
    """labels: funzione (atom_index, atoms) -> etichetta del sostituente esociclico.
    Ritorna {'size':5|6, 'positions':[{'up':str,'down':str}, ...]} partendo dal C anomerico."""
    atoms = parse(smiles)
    ring = ring_atoms(atoms)
    o = ring[0]
    # orienta: dopo l'O viene il carbonio anomerico (quello con un O esociclico legato all'O dell'anello)
    def exo(i):
        return [n for n in atoms[i]["nbrs"] if n == "H" or (isinstance(n, int) and n not in ring)]
    c_a, c_b = ring[1], ring[-1]
    def has_exo_O(i):
        return any(isinstance(n, int) and atoms[n]["el"] == "O" for n in exo(i))
    if not has_exo_O(c_a) and has_exo_O(c_b):
        ring = [o] + ring[1:][::-1]
    out = []
    n = len(ring)
    for k in range(1, n):
        i = ring[k]
        P, N = ring[k - 1], ring[(k + 1) % n]
        ex = exo(i)
        a = atoms[i]
        # sostituente "principale" X e l'altro Y (H o secondo gruppo)
        heavy = [e for e in ex if e != "H"]
        if len(ex) == 1:  # nessuno stereocentro (es. CH2 dell'anello) - non capita qui
            out.append({"up": labels(heavy[0], atoms), "down": "H"})
            continue
        if "H" in ex:
            X, Y = heavy[0], "H"
        else:  # carbonio anomerico chetosio: X = OH, Y = CH2OR
            X = next(e for e in heavy if atoms[e]["el"] == "O")
            Y = next(e for e in heavy if e != X)
        par = perm_parity([P, N, X, Y], a["nbrs"])
        cw = 1 if a["chiral"] == "@@" else 0
        # costante calibrata sull'alfa-D-glucopiranosio (C1-OH in basso)
        up = (par ^ cw ^ CAL) == 1
        lx, ly = labels(X, atoms), (labels(Y, atoms) if Y != "H" else "H")
        out.append({"up": lx if up else ly, "down": ly if up else lx})
    return {"size": n, "positions": out}


CAL = 0
