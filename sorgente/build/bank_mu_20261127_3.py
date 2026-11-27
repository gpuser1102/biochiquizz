"""Giro 2026-11-27, blocco 3 – ultimi fatti non ancora coperti: biosintesi dei lipidi (Biochimica II),
dettagli degli appunti 2023/24 di Biologia molecolare, un fatto di Biochimica I."""
from bank_common import q

BII, BM, BI = "Biochimica II", "Biologia molecolare", "Biochimica I"


def A(p):
    return f"appunti 2023/24, p. {p}"


# ── Biochimica II: lipidi (p. 199–209) ─────────────────────────────────────
q("u1127-301", "m7-biosintesi", "m", "204", "Quali sistemi allungano gli acidi grassi oltre il palmitato e con quale donatore di unità bicarboniose?", [
  "Il reticolo endoplasmatico con il malonil-CoA e il mitocondrio con l'acetil-CoA",
  "Il reticolo endoplasmatico con l'acetil-CoA e il mitocondrio con il malonil-CoA",
  "Solo l'acido grasso sintasi citosolica, che ripete il ciclo con altro malonil-CoA",
  "Il perossisoma con il propionil-CoA e il citosol con il succinil-CoA",
  "Il mitocondrio con la carnitina e il reticolo con l'acetoacetil-CoA",
  ], 0,
  "L'acido grasso sintasi si ferma a 16 atomi di carbonio. L'allungamento avviene soprattutto nel reticolo endoplasmatico, con il malonil-CoA come donatore; nel mitocondrio il donatore è l'acetil-CoA.",
  src=BII)

q("u1127-302", "m7-biosintesi", "l", "202", "In quale dominio dell'acido grasso sintasi avvengono riduzione, deidratazione e seconda riduzione?", [
  "Nel dominio II, dove arriva il gruppo legato all'ACP",
  "Nel dominio I, dove la KS lega l'acetile alla cisteina",
  "Nel dominio III, dove agisce la tioesterasi",
  "Nella regione interdominio, dove si lega il malonil-CoA",
  "In tutti e tre i domini, uno per ciascuna reazione",
  ], 0,
  "Nel dominio I avvengono il caricamento (MAT) e la condensazione (KS); il braccio fosfopanteteinico dell'ACP porta l'intermedio nel dominio II per le due riduzioni con NADPH e la deidratazione; nel dominio III la tioesterasi libera il prodotto a 16 C.",
  src=BII)

q("u1127-303", "m7-colesterolo", "f", "209", "Da quali alimenti si assume il colesterolo?", [
  "Solo da cibi animali, come carne, pesce, formaggi e uova",
  "Soprattutto da cereali e legumi, poco dai cibi animali",
  "Da tutti gli alimenti, in quantità simili",
  "Soprattutto da oli vegetali come quello di oliva e di semi",
  "Solo da frutta e verdura, che contengono fitosteroli",
  ], 0,
  "I vegetali non contengono colesterolo (hanno altri steroli). Quello assunto con la dieta entra nell'enterocita con NPC1L1, viene esterificato e parte con i chilomicroni.",
  src=BII)

# ── Biologia molecolare: appunti 2023/24 ───────────────────────────────────
q("u1127-304", "bm10-rnr", "l", A(85), "Come generano il radicale alcune ribonucleotide reduttasi di batteri anaerobi, che non possono usare l'ossigeno?", [
  "Con un cluster ferro-zolfo o con un centro binucleare a manganese",
  "Con un radicale tirosilico generato dal centro diferrico e dall'O₂",
  "Con il NADPH che cede direttamente un elettrone al C2' del ribosio",
  "Con la tioredossina, che forma il radicale sulle sue due cisteine",
  "Con una flavina legata all'enzima che si riduce alla luce",
  ], 0,
  "La classe I usa l'O₂ e il centro diferrico di R2 per formare il radicale tirosilico. Altre classi, anche in anaerobiosi, hanno cluster Fe-S o un centro binucleare a manganese.",
  src=BM)

q("u1127-305", "bm1-comunicazione", "l", A(7), "Perché le connessine sono studiate in oncologia e nella cura delle ferite?", [
  "La loro sovra- o sottoespressione è legata ad alcuni tumori e la loro espressione può frenare la guarigione",
  "Sono recettori tirosin-chinasici bersaglio di anticorpi come il trastuzumab nei tumori della mammella umana",
  "Formano canali per il Ca²⁺ voltaggio-dipendenti che controllano la contrazione dei miofibroblasti",
  "Producono il segnale Notch che decide il destino delle cellule staminali della cute",
  "Sono enzimi che degradano la matrice e permettono la migrazione delle cellule tumorali",
  ], 0,
  "Gli appunti ricordano che alterazioni nell'espressione delle connessine sono correlate all'insorgenza di tumori, che la loro espressione può frenare la guarigione delle ferite e che mutazioni del gene sono legate ad anomalie dello sviluppo.",
  src=BM)

q("u1127-306", "bm2-canali", "f", A(16), "Quale farmaco usato in medicina si lega al recettore muscarinico dell'acetilcolina?", [
  "Atropina",
  "Tubocurarina",
  "Succinilcolina",
  "Neostigmina",
  "α-bungarotossina",
  ], 0,
  "L'atropina è un antagonista muscarinico. Tubocurarina e α-bungarotossina bloccano il recettore nicotinico, la succinilcolina è un curaro depolarizzante, la neostigmina inibisce l'acetilcolinesterasi.",
  src=BM)

q("u1127-307", "bm11-bilirubina", "f", A(93), "Dove vengono lisati normalmente i globuli rossi senescenti?", [
  "Fuori dai vasi, nei macrofagi di milza, fegato e midollo osseo",
  "Dentro i vasi, per l'azione del complemento e degli anticorpi nel plasma",
  "Nel rene, durante la filtrazione glomerulare",
  "Nei polmoni, per lo stress meccanico dei capillari",
  "Nell'intestino, dove l'emoglobina viene digerita",
  ], 0,
  "Dopo 60–120 giorni i globuli rossi vengono fagocitati dai macrofagi di milza, fegato (cellule di Kupffer) e midollo; l'emolisi intravascolare avviene solo per cause chimiche, termiche o meccaniche.",
  src=BM)

q("u1127-308", "bm11-eme", "a", A(92), "Che differenza c'è nella regolazione della sintesi dell'eme tra fegato e precursori eritroidi?", [
  "Fegato: turnover rapido degli enzimi e feedback sull'ALA sintasi; precursori eritroidi: sintesi alta e sensibile al ferro",
  "Nel fegato sintesi costante e insensibile all'eme; nei precursori eritroidi forte feedback dell'eme sull'ALA sintasi epatica",
  "Nel fegato la sintesi dipende dall'eritropoietina; nei precursori eritroidi dipende solo dal citocromo P450",
  "In entrambi la sintesi è regolata solo dal piombo, che inibisce la porfobilinogeno sintasi",
  "Nel fegato la sintesi avviene solo nel citosol; nei precursori eritroidi solo nel mitocondrio",
  ], 0,
  "Nel fegato gli enzimi hanno un turnover rapido e l'ALA sintasi è sotto feedback dell'eme, per adattarsi in fretta (es. induzione del P450). Nei precursori eritroidi la sintesi resta alta, sincronizzata con le globine dall'EPO, e dipende dal ferro (IRE sull'ALA sintasi eritroide).",
  src=BM)

q("u1127-309", "bm4-fosfoinositidi", "m", A(35), "Da che cosa viene attivata la PI3-chinasi secondo gli appunti?", [
  "Da recettori tirosin-chinasici, recettori per le citochine e dimeri βγ delle proteine G",
  "Solo dalla Gq attivata, insieme alla fosfolipasi Cβ, dopo il legame di un ormone al GPCR",
  "Solo dal Ca²⁺ liberato dal reticolo attraverso il recettore per l'IP₃",
  "Dal DAG e dalla fosfatidilserina, come la proteina chinasi C",
  "Dal cAMP, che la stacca da una subunità regolatrice inibitoria come avviene nella PKA",
  ], 0,
  "La PI3-chinasi fosforila il PIP₂ in posizione 3 formando PIP₃, che attiva la PKB. È attivata da RTK (come il recettore dell'insulina tramite IRS1), da recettori per le citochine e da dimeri βγ.",
  src=BM)

q("u1127-310", "bm6-idrofobici", "l", A(52), "Come sono fatte le sequenze HRE riconosciute dai recettori degli ormoni steroidei?", [
  "Ripetizioni invertite o dirette, riconosciute dal recettore in forma dimerica",
  "Sequenze ricche di AT nel solco minore, riconosciute da un recettore monomerico",
  "Forcine dell'mRNA al 5', riconosciute da proteine regolatrici del ferro",
  "Sequenze CRE riconosciute da CREB fosforilato dalla PKA",
  "Sequenze casuali, riconosciute grazie alla sola carica positiva del recettore",
  ], 0,
  "Gli elementi di risposta (ERE, GRE, TRE, VDRE, RARE) sono ripetizioni invertite o dirette, adatte al recettore dimerico che le lega con le dita di zinco nel solco maggiore.",
  src=BM)

# ── Biochimica I ───────────────────────────────────────────────────────────
q("u1127-311", "d1-metabolismo", "f", "10", "Perché, secondo la sbobina, le proteine sono le macromolecole biologiche più versatili?", [
  "Svolgono funzioni molto diverse: anticorpi, fibrinogeno, enzimi, actina e miosina",
  "Sono la principale riserva di energia dell'organismo, più dei lipidi",
  "Sono le uniche molecole che conservano e trasmettono l'informazione genetica",
  "Si accumulano come riserva nel fegato e nel muscolo, proprio come il glicogeno",
  "Sono le sole molecole che formano la parte strutturale delle membrane",
  ], 0,
  "Carboidrati e lipidi sono le principali fonti di energia e di riserva; le proteine si sono adattate a moltissime funzioni (difesa, coagulazione, catalisi, contrazione).",
  src=BI)
