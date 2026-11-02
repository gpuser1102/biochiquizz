import haworth as H
def lab(i, atoms):
    a=atoms[i]
    if a["el"]=="O":
        nb=[n for n in a["nbrs"] if isinstance(n,int)]
        return "OPO3" if any(atoms[n]["el"]=="P" for n in nb) else "OH"
    if a["el"]=="C":
        for n in a["nbrs"]:
            if isinstance(n,int) and atoms[n]["el"]=="O":
                return "CH2"+lab(n,atoms)
    return a["el"]
S={"aGlc":"C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O",
"bGlc":"C([C@@H]1[C@H]([C@@H]([C@H]([C@@H](O1)O)O)O)O)O",
"aG6P":"C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)OP(=O)(O)O",
"bF6P":"C([C@@H]1[C@H]([C@@H]([C@](O1)(CO)O)O)O)OP(=O)(O)O",
"bFBP":"C([C@@H]1[C@H]([C@@H]([C@](O1)(COP(=O)(O)O)O)O)O)OP(=O)(O)O"}
for cal in (0,1):
    H.CAL=cal; print("CAL",cal)
    for k,s in S.items():
        r=H.haworth(s,lab); print(" ",k,[("C%d"%(j+1), p["up"],p["down"]) for j,p in enumerate(r["positions"])])
