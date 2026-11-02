"""Banca domande per livelli. Ogni modulo bank_mX.py chiama q(...) e restituisce BANK.

Livelli:
  f = facile  (definizioni e fatti di base: nome dell'enzima, prodotto, sede)
  m = medio   (collegamenti: perché, bilanci, regolazione di base)
  a = alta    (padronanza: ragionamento su scenari, calcoli, interazioni tra vie)
  l = 30 e lode (rifiniture tecniche: nome esatto di enzimi e composti, numerazioni, sigle, isoenzimi)

ans = indice della risposta giusta in opts. fixed=True se l'ordine delle opzioni non va mescolato
(es. "Tutte le precedenti"). src = sbobina di riferimento.
Gli ID non vanno mai rinominati: sono la chiave dei progressi salvati sui telefoni.
"""

BANK = []


def q(id, topic, level, page, text, opts, ans, why, note=None, fixed=False, src="Biochimica II"):
    assert level in "fmal" and len(level) == 1, id
    assert 0 <= ans < len(opts), id
    assert len(set(opts)) == len(opts), id
    BANK.append(dict(id=id, topic=topic, level=level, page=page, src=src, q=text, opts=opts, ans=ans,
                     why=why, note=note, fixed=fixed))
