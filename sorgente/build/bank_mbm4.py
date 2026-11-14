"""Biologia molecolare – sintesi de novo delle purine (lezione 8), degradazione, salvataggio, gotta e SCID (lezione 9)."""
from bank_common import q as _q

S = "Biologia molecolare"
L8, L9 = "lezione 8", "lezione 9"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Sintesi de novo delle purine (lezioni 8–9) ─────────────────────────────
T = "bm8-denovo"
q("bp8-01", T, "f", L8, "Qual è il primo nucleotide purinico completo della sintesi de novo?", [
  "IMP", "AMP", "GMP", "XMP", "UMP"], 0,
  "Dall'IMP la via si biforca verso AMP e GMP.")
q("bp8-02", T, "f", L8, "Da dove proviene il ribosio 5-fosfato per la sintesi delle purine?", [
  "Dai pentoso fosfati", "Dalla glicolisi", "Dal ciclo di Krebs", "Dalla gluconeogenesi", "Dal glicogeno"], 0,
  "Viene attivato a PRPP dalla PRPP sintetasi.")
q("bp8-03", T, "f", L8, "Quali molecole forniscono gli atomi di azoto dell'anello purinico?", [
  "Glutammina (2), aspartato (1), glicina (1)", "Glutammina (1), asparagina (2), glicina (1)", "Aspartato (2), glicina (2)", "Glutammina (3), aspartato (1)", "Glicina (2), serina (1), glutammina (1)"], 0,
  "I carboni: 2 dalla glicina, 2 dall'N10-formil-THF, 1 dalla CO₂.")
q("bp8-04", T, "m", L8, "Come si costruisce l'anello purinico?", [
  "A partire dal C1' dello zucchero già fosforilato",
  "Come base libera, poi legata al ribosio 5-P",
  "A partire dall'uracile, per aggiunta di un anello",
  "A partire dall'istidina, che fornisce l'imidazolo",
  "Come base libera, poi legata al desossiribosio",
  ], 0,
  "Le pirimidine invece si costruiscono come anello e poi si legano al PRPP.",
  note="Il confronto con le pirimidine non è in questa lezione ma nella successiva.")
q("bp8-05", T, "m", L8, "Da dove viene l'energia per il trasferimento dell'ammino della glutammina sul PRPP?", [
  "Dal pirofosfato già legato al C1' del PRPP",
  "Dall'idrolisi di un ATP nel sito dell'enzima",
  "Dall'idrolisi di un GTP nel sito dell'enzima",
  "Dall'ossidazione della glutammina con NAD⁺",
  "Dal gradiente di Na⁺ della membrana",
  ], 0,
  "Si libera PPi e si forma 5-fosforibosilammina (il futuro N9), con inversione da α a β.")
q("bp8-06", T, "m", L8, "Quale enzima della sintesi de novo carbossila senza usare la biotina?", [
  "AIR carbossilasi", "Piruvato carbossilasi", "Acetil-CoA carbossilasi", "Propionil-CoA carbossilasi", "GAR sintetasi"], 0,
  "Usa CO₂ e forma il CAIR.")
q("bp8-07", T, "m", L8, "Come entra l'azoto dell'aspartato nell'anello purinico?", [
  "Si lega tutto, poi esce come fumarato",
  "L'aspartato cede l'ammino per transaminazione",
  "L'aspartato viene decarbossilato ad alanina",
  "L'aspartato viene prima convertito in asparagina",
  "L'aspartato libera ammoniaca che si lega al C6",
  ], 0,
  "Lo stesso meccanismo si ripete in IMP → AMP e nel ciclo dell'urea (argininosuccinato).")
q("bp8-08", T, "a", L8, "Che cosa serve per passare da IMP ad AMP e da IMP a GMP?", [
  "AMP: Asp e GTP. GMP: NAD⁺, Gln e ATP",
  "AMP: glutammina e ATP. GMP: aspartato e GTP",
  "AMP: NAD⁺ e aspartato. GMP: glutammina e GTP",
  "AMP: glicina e ATP. GMP: aspartato e NADPH",
  "Entrambi: aspartato e ATP, senza ossidazioni",
  ], 0,
  "Ogni via usa il nucleotide trifosfato dell'altra: così la produzione di A e G resta bilanciata.")
q("bp8-09", T, "a", L8, "Quanti ATP costa formare GMP de novo a partire dal PRPP, secondo la lezione?", [
  "Circa 7", "Circa 2", "Nessuno", "Circa 15", "Circa 4"], 0,
  "5 fino all'IMP (glicina, glutammina, chiusura, carbossilazione, aspartato) + 2 equivalenti per IMP → GMP. Con il salvataggio: 0 ATP.")
q("bp8-10", T, "l", L8, "Come si chiama l'intermedio che si forma aggiungendo la glicina alla fosforibosilammina?", [
  "Glicinammide ribonucleotide (GAR)", "Formilglicinammide ribonucleotide (FGAR)", "Amminoimidazolo ribonucleotide (AIR)", "AICAR", "SAICAR"], 0,
  "La glicina fornisce N7, C4 e C5.")
q("bp8-11", T, "l", L8, "Quale enzima chiude l'ultimo anello formando l'IMP?", [
  "IMP cicloidrolasi", "AIR sintetasi", "AICAR formiltransferasi", "Adenilosuccinato liasi", "GAR transformilasi"], 0,
  "A differenza della chiusura dell'anello imidazolico (AIR sintetasi), non richiede ATP.")
q("bp8-12", T, "h", L8, "La lezione assegna gli atomi della purina con una numerazione propria (es. «N2 dalla glicina»). Quale assegnazione è corretta nella numerazione standard?", [
  "N1 dall'aspartato; N3 e N9 dalla glutammina; N7 dalla glicina",
  "N1 dalla glicina; N3 dall'aspartato; N7 e N9 dalla glutammina",
  "N1 e N3 dalla glutammina; N7 dall'aspartato; N9 dalla glicina",
  "N1 dalla glutammina; N3 dalla glicina; N7 e N9 dall'aspartato",
  "Tutti e quattro gli azoti dalla glutammina",
  ], 0,
  "C2 e C8 dal formil-THF, C6 dalla CO₂, C4 e C5 dalla glicina.",
  note="Sbobina di Biologia molecolare, lezione 8: indica «N1 e N4 dalla glutammina, N2 dalla glicina, N6 dall'aspartato, C3 e C7 dal formil-THF, C5 dalla CO₂». Non è la numerazione standard della purina; nella lezione successiva la stessa sbobina dice correttamente che la glicina fornisce N7, C4 e C5.")

# ── Folato e unità monocarboniose (lezione 8) ──────────────────────────────
T = "bm8-folato"
q("bf8-01", T, "f", L8, "Quale forma del folato dona i carboni C2 e C8 della purina?", [
  "N10-formil-THF", "N5-metil-THF", "N5,N10-metilen-THF", "N5-formimino-THF", "Diidrofolato"], 0,
  "Il metilen-THF serve per dUMP → dTMP, il metil-THF per la metionina.")
q("bf8-02", T, "f", L8, "Quale unità monocarboniosa non può trasportare il folato?", [
  "La CO₂", "Il formile", "Il metile", "Il metilene", "Il metenile"], 0,
  "La CO₂ (livello più ossidato) è trasportata dalla biotina.")
q("bf8-03", T, "m", L8, "Come sono legati i glutammati della coda del folato?", [
  "Con legami isopeptidici sul carbossile γ",
  "Con legami peptidici normali tra carbossile α e ammino",
  "Con legami estere tra carbossile e ossidrile",
  "Con ponti disolfuro tra cisteine aggiunte",
  "Con legami fosfodiestere tramite un fosfato",
  ], 0,
  "Le cariche negative trattengono il folato nella cellula.")
q("bf8-04", T, "m", L8, "Da quali fonti viene caricato il THF di unità monocarboniose?", [
  "Serina, glicina, formiato e istidina",
  "Alanina, glutammato, acetato e lisina",
  "Metionina, cisteina, CO₂ e treonina",
  "Leucina, valina, piruvato e prolina",
  "Triptofano, tirosina, urea e arginina",
  ], 0,
  "La serina idrossimetiltransferasi (serina → glicina) è la fonte principale.")
q("bf8-05", T, "a", L8, "Perché il metil-THF ha un solo destino?", [
  "Serve solo alla metionina e non torna metilene",
  "Serve solo per le purine e si ossida subito a formile",
  "Serve solo per la timina e si riduce subito a metile",
  "Viene subito eliminato con le urine come metilfolato",
  "Si lega all'emoglobina e non è più disponibile",
  ], 0,
  "È la specie più ridotta; la sua formazione è irreversibile (alla base della trappola dei folati).")
q("bf8-06", T, "l", L8, "Quale enzima forma l'N10-formil-THF direttamente dal formiato?", [
  "Formil-THF sintetasi", "Metenil-THF cicloidrolasi", "Metilen-THF reduttasi", "Serina idrossimetiltransferasi", "Diidrofolato reduttasi"], 0,
  "In alternativa si passa da metilen → metenil → formil (deidrogenasi e cicloidrolasi).")
q("bf8-07", T, "h", L8, "Sul coenzima della metilen-THF reduttasi le sbobine non concordano. Che cosa è corretto?", [
  "Usa NADPH (come dice Biochimica II); la reazione è irreversibile",
  "Usa NADH (come dice Biologia molecolare); la reazione è reversibile",
  "Usa FADH₂ come unico donatore; la reazione è reversibile",
  "Non usa coenzimi; la reazione è un'isomerizzazione",
  "Usa NAD⁺ e ossida il metilene a formile",
  ], 0,
  "L'enzima contiene FAD legato; il donatore di elettroni è il NADPH.",
  note="Sbobina di Biologia molecolare, lezione 8: la metilen-THF reduttasi usa «il NADH» e la conversione metilene → metenile è attribuita a una «metenil THF reduttasi che utilizza NADP». Nei testi di riferimento la reduttasi usa NADPH (come la sbobina di Biochimica II, p. 266) e la seconda reazione è della metilen-THF deidrogenasi.")

# ── Regolazione della sintesi delle purine (lezioni 8–9) ───────────────────
T = "bm8-regolazione"
q("brg8-01", T, "f", L8, "Qual è il passaggio più regolato della sintesi de novo delle purine?", [
  "L'amidotransferasi", "La PRPP sintetasi", "La GAR sintetasi", "L'IMP cicloidrolasi", "L'AIR carbossilasi"], 0,
  "È il primo passaggio specifico e quello che limita la velocità.")
q("brg8-02", T, "m", L8, "Come viene regolata l'amidotransferasi dai nucleotidi e dal PRPP?", [
  "I nucleotidi favoriscono il dimero inattivo, il PRPP il monomero attivo",
  "AMP, GMP, IMP la spingono verso il monomero attivo; il PRPP verso il dimero",
  "AMP e GMP la fosforilano; il PRPP la defosforila",
  "Il PRPP la inibisce in modo competitivo; i nucleotidi la attivano",
  "Viene regolata solo dalla concentrazione di glutammina",
  ], 0,
  "Ha due siti allosterici: uno per i nucleotidi ossipurinici (IMP, XMP, GMP), uno per gli amminopurinici (AMP). L'inibizione è sinergica.")
q("brg8-03", T, "m", L9, "Come viene regolata la biforcazione dall'IMP?", [
  "Il GMP inibisce l'IMP deidrogenasi; l'AMP l'adenilosuccinato sintetasi",
  "Il GMP inibisce l'adenilosuccinato sintetasi; l'AMP l'IMP deidrogenasi",
  "L'ATP inibisce entrambi gli enzimi in modo allosterico",
  "Il PRPP attiva l'IMP deidrogenasi e inibisce l'altra via",
  "Non è regolata: dipende solo dalla disponibilità di IMP",
  ], 0,
  "Inibizioni competitive dei rispettivi prodotti.")
q("brg8-04", T, "a", L9, "Perché la concentrazione di PRPP controlla l'amidotransferasi più di quella di glutammina?", [
  "Il PRPP varia molto ed è sotto la Km; la glutammina è stabile",
  "La glutammina è un inibitore e il PRPP un attivatore",
  "Il PRPP lega il sito attivo con cinetica iperbolica, la glutammina sigmoide",
  "La glutammina viene consumata dal ciclo dell'urea e non arriva all'enzima",
  "Il PRPP è prodotto dall'enzima stesso e ne amplifica l'attività",
  ], 0,
  "Cinetica iperbolica per la glutammina, sigmoide per il PRPP; il PRPP dipende dalla via dei pentoso fosfati.")
q("brg8-05", T, "a", L9, "Secondo la lezione, quale rapporto deve restare costante tra nucleotidi adenilici e guanilici?", [
  "Gli adenilici sono 4–6 volte i guanilici",
  "Adenilici e guanilici sono sempre in rapporto 1:1",
  "I guanilici sono 4–6 volte gli adenilici",
  "L'ATP è sempre 100 volte il GTP",
  "Non c'è un rapporto fisso tra i due gruppi",
  ], 0,
  "Possono cambiare le quote di mono-, di- e trifosfati, non il rapporto tra le somme.")
q("brg8-06", T, "l", L9, "Quali isoforme della IMP deidrogenasi esistono?", [
  "Una costitutiva e una proliferativa",
  "IMPDH I epatica e IMPDH II muscolare",
  "IMPDH I mitocondriale e IMPDH II citosolica",
  "IMPDH I attivata dal GMP e IMPDH II inibita",
  "IMPDH I a NAD⁺ e IMPDH II a NADP⁺",
  ], 0,
  "L'isoforma II è un bersaglio di farmaci antiproliferativi.",
  note="L'uso dell'IMPDH II come bersaglio farmacologico non è nella sbobina.")
q("brg8-07", T, "h", L9, "Quale regolazione dell'AMP deaminasi descrive la lezione?", [
  "Attivata da K⁺ e ATP, inibita da Pi, GTP e GDP",
  "Attivata da GTP, inibita da ATP; il K⁺ aumenta la Vmax",
  "Attivata da Pi e GDP, inibita da K⁺; cinetica sempre iperbolica",
  "Inibita dall'AMP stesso; il K⁺ non ha effetto",
  "Attivata dal PRPP come l'amidotransferasi",
  ], 0,
  "Senza K⁺ la curva v/[AMP] è sigmoide.")

# ── Degradazione delle purine (lezione 9) ──────────────────────────────────
T = "bm9-degradazione"
q("bdg9-01", T, "f", L9, "Qual è il prodotto finale della degradazione delle purine nell'uomo?", [
  "Urato", "Urea", "Allantoina", "β-alanina", "Ammoniaca"], 0,
  "Altre specie lo trasformano in composti più solubili (allantoina); noi no.")
q("bdg9-02", T, "f", L9, "Quale enzima ossida l'ipoxantina a xantina e la xantina ad acido urico?", [
  "Xantina ossidasi", "Guanina deaminasi", "Purina nucleoside fosforilasi", "Adenosina deaminasi", "IMP deidrogenasi"], 0,
  "Usa O₂ e produce H₂O₂.")
q("bdg9-03", T, "m", L9, "Che cosa fa la purina nucleoside fosforilasi?", [
  "Scinde il nucleoside in base e ribosio 1-P",
  "Scinde il nucleotide in nucleoside e fosfato",
  "Rimuove il gruppo amminico dall'adenosina",
  "Ossida la base a xantina con O₂",
  "Lega la base al PRPP formando il nucleotide",
  ], 0,
  "Per esempio inosina → ipoxantina + ribosio 1-P.")
q("bdg9-04", T, "m", L9, "Quali cofattori contiene la xantina ossidasi?", [
  "FAD, molibdeno e cluster Fe-S",
  "NAD⁺, rame e un eme",
  "PLP, zinco e biotina",
  "FMN, selenio e un cluster 4Fe-4S",
  "TPP, magnesio e lipoato",
  ], 0,
  "È un omodimero; l'accettore finale degli elettroni è l'O₂.")
q("bdg9-05", T, "a", L9, "In quali due punti si toglie l'ammino delle purine adeniliche?", [
  "AMP → IMP oppure adenosina → inosina",
  "IMP → XMP (IMP deidrogenasi) o xantina → urato",
  "Ipoxantina → xantina o guanina → guanosina",
  "AMP → adenina (nucleosidasi) o adenina → urato",
  "GMP → IMP (GMP reduttasi) o guanina → xantina",
  ], 0,
  "Il primo enzima agisce sul nucleotide, il secondo sul nucleoside. Le guaniliche perdono l'ammino con la guanina deaminasi.")
q("bdg9-06", T, "a", L9, "Che cosa ottiene il muscolo dal ciclo dei nucleotidi purinici?", [
  "Fumarato per il ciclo di Krebs, al costo di un GTP",
  "ATP direttamente dalla reazione dell'AMP deaminasi",
  "Glucosio dall'aspartato per la gluconeogenesi",
  "Urea per eliminare l'azoto in eccesso",
  "NADPH per la sintesi di acidi grassi",
  ], 0,
  "Il risultato netto è la deaminazione dell'aspartato a fumarato con liberazione di NH₄⁺.",
  note="La sbobina dice che l'ossidazione del malato produce «NADPH» e «tre molecole di ATP». Si produce NADH (circa 2,5 ATP con i valori attuali).")
q("bdg9-07", T, "l", L9, "In che cosa si trasforma la xantina ossidasi quando diventa deidrogenasi?", [
  "In un enzima che cede elettroni al NAD⁺",
  "In un enzima che usa il NADPH al posto del FAD",
  "In un enzima che produce superossido invece di H₂O₂",
  "In un enzima che ossida l'acido urico ad allantoina",
  "In un enzima che non contiene più molibdeno",
  ], 0,
  "È lo stesso enzima con una diversa modifica post-traduzionale (ossidazione di un SH o proteolisi).",
  note="Sbobina di Biologia molecolare, lezione 9: c'è scritto che la forma deidrogenasi usa «come accettore di elettroni il NADH». L'accettore è il NAD⁺, che viene ridotto a NADH.")
q("bdg9-08", T, "h", L9, "Quale ordine descrive la digestione degli acidi nucleici della dieta?", [
  "Nucleasi → fosfodiesterasi → nucleotidasi → nucleosidasi",
  "Nucleosidasi → nucleotidasi → fosfodiesterasi → nucleasi",
  "Fosfodiesterasi → nucleasi → nucleosidasi → nucleotidasi",
  "Nucleotidasi → nucleasi → nucleosidasi → fosfodiesterasi",
  "Nucleasi → nucleosidasi → fosfodiesterasi → nucleotidasi",
  ], 0,
  "Oligonucleotidi → mononucleotidi → nucleosidi + fosfato → basi + pentosi.")

# ── Vie di salvataggio (lezione 9) ─────────────────────────────────────────
T = "bm9-salvataggio"
q("bsv9-01", T, "f", L9, "Quale enzima recupera ipoxantina e guanina?", [
  "HGPRT", "APRT", "PNP", "ADA", "IMPDH"], 0,
  "L'adenina è recuperata dall'APRT; entrambe usano il PRPP.")
q("bsv9-02", T, "f", L9, "Quale quota dei nucleotidi purinici giornalieri viene dal salvataggio, secondo la lezione?", [
  "Circa il 90%", "Circa il 10%", "Circa il 50%", "Circa il 25%", "Quasi lo 0%"], 0,
  "Il salvataggio costa molta meno energia della sintesi de novo.")
q("bsv9-03", T, "m", L9, "Perché gli eritrociti dipendono dal salvataggio?", [
  "Manca loro l'amidotransferasi",
  "Non hanno la PRPP sintetasi",
  "Non hanno la via dei pentoso fosfati",
  "Non hanno l'HGPRT né l'APRT",
  "Non hanno la xantina ossidasi",
  ], 0,
  "La sintesi de novo avviene soprattutto nel fegato.")
q("bsv9-04", T, "m", L9, "Come viene regolato il salvataggio?", [
  "IMP e GMP frenano l'HGPRT, l'AMP l'APRT",
  "L'AMP inibisce l'HGPRT; IMP e GMP l'APRT",
  "Il PRPP inibisce entrambi gli enzimi",
  "L'acido urico inibisce entrambi gli enzimi",
  "Non è regolato: dipende solo dalle basi",
  ], 0,
  "Inibizioni competitive rispetto al PRPP.")
q("bsv9-05", T, "a", L9, "Perché un salvataggio ridotto accelera la sintesi de novo?", [
  "Resta più PRPP e mancano gli inibitori",
  "Le basi libere attivano l'amidotransferasi",
  "Il fegato riceve un segnale ormonale dalle cellule",
  "L'acido urico attiva la PRPP sintetasi",
  "La xantina ossidasi produce PRPP",
  ], 0,
  "Più attivatore (PRPP) e meno inibitori (AMP, IMP, GMP) sull'amidotransferasi.")
q("bsv9-06", T, "a", L9, "Come nasce l'adenina recuperata dopo la sintesi delle poliammine?", [
  "Dalla metiltioadenosina lasciata dalla SAM decarbossilata",
  "L'ornitina decarbossilasi libera adenina dalla putrescina",
  "La spermina viene ossidata ad adenina dalla xantina ossidasi",
  "La putrescina si lega al PRPP e forma adenina",
  "La metionina viene trasformata direttamente in adenina",
  ], 0,
  "La 5'-metiltioadenosina fosforilasi dà adenina + metiltioribosio 1-P; l'APRT riforma AMP.")
q("bsv9-07", T, "l", L9, "Quale mutazione dell'HGPRT, citata nella lezione, causa la sindrome di Lesch-Nyhan?", [
  "G69E", "D134G", "D193N", "E6V", "C677T"], 0,
  "D134G la inattiva in parte (artrite gottosa); D193N non lega il Mg²⁺.")
q("bsv9-08", T, "h", L9, "Quale coppia descrive le due vie di salvataggio?", [
  "Base + PRPP oppure nucleoside + ATP",
  "Base + ribosio 1-P (fosforilasi) oppure nucleotide + PPi",
  "Base + ATP (chinasi) oppure nucleoside + PRPP (transferasi)",
  "Nucleotide + H₂O (nucleotidasi) oppure base + CO₂",
  "Base + glutammina (amidotransferasi) oppure nucleoside + GTP",
  ], 0,
  "Entrambe conservano energia rispetto alla sintesi de novo.")

# ── Gotta (lezione 9) ──────────────────────────────────────────────────────
T = "bm9-gotta"
q("bgo9-01", T, "f", L9, "Sopra quale valore si parla di iperuricemia?", [
  "7 mg/dl", "3 mg/dl", "1 mg/dl", "20 mg/dl", "70 mg/dl"], 0,
  "Normale 3–7 mg/dl, ottimale sotto 5.")
q("bgo9-02", T, "f", L9, "Su quale enzima agisce l'allopurinolo?", [
  "Xantina ossidasi", "HGPRT", "PRPP sintetasi", "Adenosina deaminasi", "IMP deidrogenasi"], 0,
  "È un analogo dell'ipoxantina con N7 e C8 scambiati.")
q("bgo9-03", T, "m", L9, "Come agisce la colchicina nella gotta?", [
  "Blocca la fagocitosi dei cristalli",
  "Inibisce la xantina ossidasi come l'allopurinolo",
  "Aumenta l'escrezione renale dell'acido urico",
  "Scioglie i cristalli di urato nelle articolazioni",
  "Inibisce la PRPP sintetasi nel fegato",
  ], 0,
  "È un antimitotico: riduce l'infiammazione. Gli uricosurici aumentano l'escrezione.")
q("bgo9-04", T, "a", L9, "Perché un'iperattività della PRPP sintetasi causa gotta?", [
  "Più PRPP accelera la sintesi de novo",
  "Il PRPP inibisce la xantina ossidasi e l'urato si accumula",
  "Il PRPP precipita nelle articolazioni insieme all'urato",
  "Il PRPP blocca l'escrezione renale dell'acido urico",
  "Il PRPP viene convertito direttamente in acido urico",
  ], 0,
  "Lo stesso vale per un deficit parziale di HGPRT, che lascia PRPP non consumato.")
q("bgo9-05", T, "a", L9, "Perché nella malattia di von Gierke compare iperuricemia?", [
  "Il G6P va nei pentoso fosfati e aumenta il PRPP",
  "Manca la xantina ossidasi epatica e l'urato non si elimina",
  "Il glicogeno in eccesso inibisce l'escrezione renale",
  "Manca l'HGPRT e le basi non vengono recuperate",
  "Il glucosio in eccesso si trasforma in acido urico",
  ], 0,
  "Manca la glucosio 6-fosfatasi.")
q("bgo9-06", T, "a", L9, "Oltre a bloccare la xantina ossidasi, quale altro effetto utile ha l'allopurinolo?", [
  "Le basi recuperate consumano PRPP e frenano la sintesi de novo",
  "Aumenta l'escrezione renale dell'acido urico già formato",
  "Inibisce direttamente l'amidotransferasi epatica",
  "Trasforma l'urato in allantoina più solubile",
  "Blocca la fagocitosi dei cristalli da parte dei leucociti",
  ], 0,
  "Ipoxantina e xantina sono più solubili dell'urato.",
  note="Sbobina di Biologia molecolare, lezione 9: c'è scritto che l'ossipurinolo «rimane legato all'ipoxantina e ne blocca l'attività». Resta legato alla xantina ossidasi (al molibdeno del sito attivo) e ne blocca l'attività.")
q("bgo9-07", T, "l", L9, "In cosa viene convertito l'allopurinolo dalla xantina ossidasi?", [
  "Ossipurinolo", "Acido urico", "Xantina", "Allantoina", "Ipoxantina"], 0,
  "È un inibitore suicida: l'enzima stesso produce il composto che lo blocca.")
q("bgo9-08", T, "h", L9, "Quale di queste non è una causa di iperuricemia citata nella lezione?", [
  "Deficit di adenosina deaminasi",
  "Terapia radiante con distruzione cellulare",
  "Ridotta escrezione renale di acido urico",
  "Iperattività della PRPP sintetasi",
  "Deficit di glucosio 6-fosfatasi",
  ], 0,
  "Il deficit di ADA causa la SCID.")

# ── SCID (lezione 9) ───────────────────────────────────────────────────────
T = "bm9-scid"
q("bsc9-01", T, "f", L9, "Quale enzima manca nella SCID descritta nella lezione?", [
  "Adenosina deaminasi", "Purina nucleoside fosforilasi", "HGPRT", "Xantina ossidasi", "Ribonucleotide reduttasi"], 0,
  "Severe Combined ImmunoDeficiency.")
q("bsc9-02", T, "m", L9, "Quale metabolita si accumula nei linfociti nella SCID e che cosa inibisce?", [
  "dATP, che blocca la ribonucleotide reduttasi",
  "Acido urico, che inibisce la DNA polimerasi",
  "dGTP, che inibisce la timidilato sintasi",
  "IMP, che inibisce l'amidotransferasi",
  "Adenina, che inibisce l'APRT",
  ], 0,
  "Senza deossiribonucleotidi i linfociti non replicano il DNA.")
q("bsc9-03", T, "a", L9, "Perché la SCID colpisce soprattutto i linfociti?", [
  "Hanno molte chinasi e si dividono attivamente",
  "Sono le uniche cellule che hanno l'adenosina deaminasi",
  "Non hanno la via di salvataggio delle purine",
  "Dipendono dall'acido urico come antiossidante",
  "Non hanno mitocondri e dipendono dalla glicolisi",
  ], 0,
  "I bambini affetti devono vivere in condizioni di sterilità.")
q("bsc9-04", T, "h", L9, "La lezione descrive l'adenosina deaminasi come un enzima che taglia il legame glicosidico. Che cosa fa davvero?", [
  "Toglie l'ammino: adenosina → inosina",
  "Scinde l'adenosina in adenina e ribosio",
  "Fosforila l'adenosina ad AMP",
  "Ossida l'adenosina a xantosina",
  "Lega l'adenosina al PRPP",
  ], 0,
  "Agisce anche sulla deossiadenosina, che senza l'enzima viene fosforilata a dATP.",
  note="Sbobina di Biologia molecolare, lezione 9: c'è scritto che l'ADA converte l'adenosina in inosina «tagliando il legame glucidico». Il legame glicosidico resta intatto; l'enzima idrolizza il gruppo amminico in C6.")
