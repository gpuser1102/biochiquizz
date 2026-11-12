"""Pacchetto 2026-11-12 – Biologia molecolare, lezioni 1–5: domande Medie, Hard e 30 e lode in più
sugli argomenti che avevano pochi quesiti difficili. La sbobina non ha numeri di pagina: il riferimento è la lezione."""
from bank_common import q as _q

S = "Biologia molecolare"
L1, L2, L3, L4, L5 = "lezione 1", "lezione 2", "lezione 3", "lezione 4", "lezione 5"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Lezione 1 ─────────────────────────────────────────────────────────────
T = "bm1-comunicazione"
q("yb1c-01", T, "m", L1, "Perché le gap junction permettono le sinapsi elettriche (es. nel miocardio)?", [
  "Uniscono direttamente il citosol di due cellule e lasciano passare ioni in tempi brevissimi",
  "Liberano neurotrasmettitori nello spazio tra le due cellule adiacenti, in tempi brevissimi e mirati",
  "Lasciano passare proteine e acidi nucleici dal citosol di una cellula a quello dell'altra",
  "Formano un recettore canale che si apre soltanto quando lega un ligando extracellulare",
  "Sono pompe ATP-dipendenti che spingono attivamente gli ioni nella cellula accanto",
  ], 0,
  "Il poro del connessone fa passare ioni, amminoacidi, zuccheri e nucleotidi, ma non le proteine.")
q("yb1c-02", T, "h", L1, "In un embrione una mutazione impedisce il taglio proteolitico di Notch dopo il legame con Delta. Quale conseguenza è la più coerente?", [
  "Il frammento intracellulare non si libera: CSL non viene attivato e i geni bersaglio restano spenti",
  "Notch resta in membrana ma attiva lo stesso CSL, perché il legame con Delta basta a segnalare",
  "Delta viene secreto e agisce come segnale paracrino sulle cellule vicine, compensando il difetto",
  "Il recettore si autofosforila sulle tirosine e attiva al posto di Notch la via di Ras e delle MAPK",
  "Il frammento extracellulare di Notch entra nel nucleo al posto di quello intracellulare e attiva CSL",
  ], 0,
  "È il taglio a liberare la porzione citosolica di Notch, che passa dai pori nucleari e attiva il fattore di trascrizione CSL.")
q("yb1c-03", T, "h", L1, "Perché la presentazione dell'antigene da parte dell'MHC al linfocita T è un esempio di comunicazione juxtacrina?", [
  "Il peptide del patogeno resta esposto sulla superficie della cellula e il linfocita lo riconosce per contatto",
  "Il linfocita T secerne citochine che raggiungono la cellula infetta viaggiando nel circolo sanguigno",
  "L'antigene digerito dall'immunoproteasoma viene rilasciato nel sangue e poi lega il recettore T",
  "Cellula infetta e linfocita T si scambiano i peptidi del patogeno attraverso le gap junction",
  "L'MHC viene tagliato dalle proteasi e il suo frammento intracellulare entra nel nucleo del linfocita T",
  ], 0,
  "Nella comunicazione da contatto il segnale resta sulla cellula che lo produce: qui il complesso MHC-peptide esposto in superficie.")
q("yb1c-04", T, "l", L1, "Quale regione della connessina ha un ruolo importante nella regolazione del poro?", [
  "Il dominio N-terminale", "Il lungo dominio C-terminale", "I due loop extracellulari", "L'ansa citoplasmatica centrale", "La seconda elica transmembrana",
  ], 0,
  "I due loop extracellulari regolano l'attracco tra gli emicanali; ansa citoplasmatica e coda C-terminale variano molto tra i sottotipi.")

T = "bm1-recettore-ligando"
q("yb1r-01", T, "m", L1, "In una curva di saturazione recettore-ligando, come si riconosce il legame aspecifico?", [
  "Cresce lentamente con il ligando aggiunto e non raggiunge mai un plateau",
  "Cresce molto rapidamente e si satura già a basse concentrazioni di ligando aggiunto",
  "Raggiunge un plateau che corrisponde al Bmax dei siti del recettore",
  "Diminuisce man mano che aumenta la concentrazione del ligando libero",
  "Compare come l'unica retta utile nel grafico di Scatchard del recettore",
  ], 0,
  "Il legame specifico invece sale in fretta e si appiattisce quando tutti i siti sono occupati.")
q("yb1r-02", T, "h", L1, "Nel grafico di Scatchard di un recettore la retta ha pendenza −0,5 nM⁻¹. Quanto vale la Kd?", [
  "2 nM", "0,5 nM", "−2 nM", "5 nM", "0,2 nM",
  ], 0,
  "Pendenza = −1/Kd, quindi Kd = 1/0,5 = 2 nM.")
q("yb1r-03", T, "h", L1, "Due tessuti danno rette di Scatchard parallele, che però incontrano l'asse del legato in punti diversi. Che cosa significa?", [
  "Stessa affinità (stessa Kd) ma un numero diverso di recettori (Bmax)",
  "Affinità diversa ma lo stesso numero di siti di legame per ciascuna cellula",
  "In uno dei due tessuti il ligando lega solo in modo aspecifico",
  "Ka diversa ma Kd uguale, perché le due costanti sono indipendenti",
  "Uno dei due tessuti ha recettori cooperativi con più siti di legame",
  ], 0,
  "La pendenza (−1/Kd) misura l'affinità; il punto d'incontro con l'asse del legato dà Bmax, cioè il numero di siti saturabili.")
q("yb1r-04", T, "l", L1, "Come si esprime la costante di associazione Ka con le costanti di velocità della reazione R + L ⇄ RL?", [
  "k₊₁ / k₋₁", "k₋₁ / k₊₁", "k₊₁ · k₋₁", "1 / k₊₁", "k₋₁ − k₊₁",
  ], 0,
  "Ka = [RL]/[R][L] = k₊₁/k₋₁, e Kd = 1/Ka.")

T = "bm1-intra-superficie"
q("yb1i-01", T, "m", L1, "Arrivato alla cellula bersaglio, perché un ormone steroideo lascia la sua proteina di trasporto?", [
  "Ha un'affinità per il recettore così alta da staccarsi dal trasportatore ed entrare",
  "Il trasportatore viene degradato dalle proteasi presenti sulla membrana bersaglio",
  "Lega un recettore di superficie che lo stacca dal trasportatore e lo internalizza",
  "Il trasportatore entra con lui nella cellula e lo rilascia direttamente nel nucleo",
  "Il pH acido del liquido extracellulare denatura la proteina di trasporto e lo libera",
  ], 0,
  "Una volta dentro, l'ormone lega il recettore nel citosol o nel nucleo e il complesso regola la trascrizione.")
q("yb1i-02", T, "h", L1, "Una proteina adattatrice ha un dominio SH2 e un dominio SH3. Che cosa può fare?", [
  "Legare una fosfotirosina con SH2 e una sequenza ricca di prolina di un'altra chinasi con SH3",
  "Legare il fosfatidilinositolo di membrana con SH2 e le fosfotirosine del recettore attivato con SH3",
  "Fosforilare tirosine con il dominio SH2 e defosforilare serine con il dominio SH3",
  "Legare il DNA nel nucleo con SH2 e la membrana plasmatica con il dominio SH3",
  "Riconoscere poliproline con il dominio SH2 e fosfoserine con il dominio SH3",
  ], 0,
  "Così l'adattatore avvicina due partner della cascata: è la funzione scaffold.")
q("yb1i-03", T, "h", L1, "Una proteina della cascata dell'insulina ha un dominio PTB e un dominio PH. Quale combinazione di funzioni ne deriva?", [
  "Trattiene una proteina fosforilata in tirosina (PTB) e si ancora alla membrana legando il fosfatidilinositolo (PH)",
  "Fosforila le tirosine del recettore (PTB) e idrolizza il fosfatidilinositolo bisfosfato della membrana plasmatica (PH)",
  "Lega le sequenze ricche di prolina (PTB) e i nucleotidi ciclici prodotti dalle ciclasi nel citosol (PH)",
  "Riconosce le fosfoserine fosforilate dalla PKA (PTB) e il diacilglicerolo liberato in membrana (PH)",
  "Si ancora alla membrana con il fosfatidilinositolo (PTB) e trattiene le fosfotirosine del recettore (PH)",
  ], 0,
  "PTB = phosphotyrosine-binding; PH riconosce il fosfatidilinositolo e porta la proteina sulla membrana dove sta il recettore.")
q("yb1i-04", T, "l", L1, "Da quale proteina prendono il nome i domini SH2 e SH3?", [
  "SRC", "Ras", "Raf", "Grb2", "JAK",
  ], 0,
  "SH = Src homology: SH2 lega le fosfotirosine, SH3 le sequenze poliproliniche.")

# ── Lezione 2 ─────────────────────────────────────────────────────────────
T = "bm2-canali"
q("yb2c-01", T, "m", L2, "Che cosa rende il recettore nicotinico selettivo per i cationi?", [
  "Residui acidi carichi negativamente esposti verso il poro dalle cinque subunità",
  "Residui basici carichi positivamente esposti verso il poro sull'elica 2 di ogni subunità",
  "Il ponte disolfuro che si trova nella regione N-terminale extracellulare",
  "Il diametro esterno di 9 nm, troppo largo per far passare gli anioni",
  "Il legame di due acetilcoline alle interfacce tra le subunità α e β",
  ], 0,
  "Le due acetilcoline si legano alle interfacce α-δ e α-γ; il ponte disolfuro N-terminale fa parte del sito di legame.")
q("yb2c-02", T, "h", L2, "Il recettore GABA-A e il nicotinico hanno un'architettura simile (5 subunità con 4 eliche). Perché il primo inibisce e il secondo eccita?", [
  "L'elica 2 del GABA-A è ricca di residui basici e fa entrare Cl⁻; quella del nicotinico ha residui acidi e fa entrare cationi",
  "Il GABA-A è accoppiato a una proteina G che chiude i canali del Ca²⁺ e apre quelli del K⁺; il nicotinico è un canale che fa entrare Na⁺",
  "Il GABA-A ha l'elica 2 ricca di residui acidi e fa uscire K⁺; il nicotinico ha residui basici e fa entrare Na⁺",
  "Il GABA-A è un dimero di subunità a 7 eliche; il nicotinico è un pentamero con il poro rivestito dall'elica 2",
  "Il GABA-A depolarizza solo i neuroni, mentre il nicotinico iperpolarizza la cellula muscolare a riposo",
  ], 0,
  "L'ingresso di anioni iperpolarizza (inibizione); l'ingresso di Na⁺ e Ca²⁺ depolarizza (eccitazione). Il dimero a 7 eliche è il GABA-B.")
q("yb2c-03", T, "h", L2, "Dopo la succinilcolina compaiono prima fascicolazioni e poi paralisi flaccida. Perché?", [
  "È un agonista che resta legato a lungo: prima depolarizza, poi desensibilizza il recettore",
  "È un antagonista che blocca il recettore, poi viene idrolizzato e libera acetilcolina",
  "Inibisce l'acetilcolinesterasi: l'acetilcolina si accumula e poi viene ricaptata tutta dal neurone",
  "Blocca i canali del Ca²⁺ presinaptici, quindi l'acetilcolina non viene più rilasciata",
  "Apre i canali del Cl⁻ della placca motrice, iperpolarizzando la fibra muscolare",
  ], 0,
  "È il curaro depolarizzante; i curari veri (es. pancuronio) sono invece antagonisti e danno subito paralisi flaccida.")
q("yb2c-04", T, "h", L2, "L'acetilcolina rallenta il cuore attraverso il recettore muscarinico M2. Quale meccanismo è coerente con le sbobine?", [
  "M2 attiva una proteina G che inibisce l'adenilato ciclasi e apre i canali del K⁺, iperpolarizzando",
  "M2 è un canale per cationi che si apre con l'acetilcolina e depolarizza la cellula cardiaca",
  "M2 attiva la via dei fosfoinositidi e aumenta il Ca²⁺ citosolico tramite il recettore dell'IP₃ del RE",
  "M2 attiva la Gs, aumenta il cAMP e così riduce la forza di contrazione del miocardio",
  "M2 è un recettore tirosin-chinasico che attiva la via di Ras e i fattori fos e jun",
  ], 0,
  "I muscarinici pari (M2, M4) inibiscono l'adenilato ciclasi; i dispari (M1, M3, M5) usano i fosfoinositidi. Nella lezione 3 la Gα attivata dall'acetilcolina apre i canali del K⁺.")
q("yb2c-05", T, "l", L2, "Quali sono il diametro esterno e il diametro del poro del recettore nicotinico?", [
  "9 nm e 2 nm", "2 nm e 9 nm", "9 nm e 0,2 nm", "20 nm e 9 nm", "4 nm e 1 nm",
  ], 0,
  "Il poro è rivestito dall'elica 2 di ciascuna delle 5 subunità (2α, β, γ, δ).")
q("yb2c-06", T, "l", L2, "Nel recettore GABA-B, quale subunità lega il neurotrasmettitore?", [
  "GABA-B1", "GABA-B2", "Entrambe, una molecola ciascuna", "Nessuna: lo lega la proteina G", "La subunità βγ associata",
  ], 0,
  "GABA-B2 serve a formare il dimero funzionale, ha i siti per i modulatori allosterici e il sito per la proteina G.")

T = "bm2-rtk"
q("yb2r-01", T, "m", L2, "Com'è fatto in genere un recettore tirosin-chinasico?", [
  "Dominio extracellulare di legame, una sola α-elica transmembrana, dominio tirosin chinasico citosolico",
  "Sette α-eliche transmembrana, con il loop citosolico C3 che interagisce con la proteina G trimerica",
  "Cinque subunità con quattro eliche ciascuna, che formano un poro selettivo per i cationi",
  "Dominio extracellulare di legame, una sola elica transmembrana, coda citosolica senza attività enzimatica",
  "Quattro subunità con sei eliche ciascuna, nella membrana del reticolo endoplasmatico",
  ], 0,
  "Il recettore senza enzima che recluta una chinasi è quello per le citochine (JAK). Di solito l'RTK è un monomero che dimerizza col ligando; quello dell'insulina è già un tetramero.")
q("yb2r-02", T, "h", L2, "In un tumore il recettore dell'EGF dimerizza anche senza ligando. Quale passaggio serve comunque perché si attivi la MAP chinasi?", [
  "Il reclutamento di SOS tramite un adattatore SH2 e lo scambio del GDP con GTP su Ras",
  "Il legame dell'EGF, senza il quale la cascata a valle del recettore non procede comunque",
  "La fosforilazione diretta di Ras da parte del recettore su un residuo di tirosina",
  "Il taglio proteolitico del recettore e l'ingresso della sua coda nel nucleo della cellula",
  "L'attivazione di JAK, che fosforila direttamente Ras e poi MEK sulle loro tirosine",
  ], 0,
  "Dimerizzazione → autofosforilazione → adattatore SH2 → SOS (GEF) → Ras-GTP → Raf → MEK → MAPK.")
q("yb2r-03", T, "h", L2, "Che cosa succede alle regioni switch I e switch II di Ras quando il GTP viene idrolizzato?", [
  "Perdono i legami a H con il fosfato γ, si allontanano e Ras non lega più i bersagli a valle",
  "Si avvicinano tra loro e permettono a Ras di legare Raf con un'affinità molto più alta di prima",
  "Vengono fosforilate da GAP e diventano il sito di legame per la proteina SOS",
  "Si staccano dalla membrana, perché l'idrolisi rimuove la coda prenilica di Ras",
  "Restano immobili, mentre a cambiare conformazione è soltanto il sito del Mg²⁺",
  ], 0,
  "Con il GTP la Thr35 e la Gly60 legano il fosfato γ e la struttura è «tesa»; con il GDP collassa e diventa più lassa.")
q("yb2r-04", T, "h", L2, "Perché GEF e GAP non possono agire su Ras nello stesso momento?", [
  "Legano Ras nella stessa posizione: agisce o l'una o l'altra",
  "La GAP degrada la GEF ogni volta che Ras è legata al GDP",
  "La GEF lavora solo nel nucleo e la GAP solo in membrana",
  "Agiscono in sequenze obbligate separate da un'ora",
  "Una lega il GTP libero e l'altra il GDP libero, non Ras",
  ], 0,
  "La GEF (SOS) favorisce l'ingresso del GTP al posto del GDP; la GAP accende l'attività GTPasica di Ras.")
q("yb2r-05", T, "l", L2, "Quali residui di Ras legano il fosfato γ del GTP e quale residuo ne determina la specificità per il GTP?", [
  "Thr35 e Gly60; Ala146", "Thr183 e Tyr185; Ala146", "Thr35 e Gly60; Ser14", "Gly12 e Gln61; Thr35", "Ser32 e Gly60; Ala146",
  ], 0,
  "Se l'Ala146 è mutata Ras può legare ATP. Thr183 e Tyr185 sono invece i residui fosforilati della MAP chinasi.")

T = "bm2-terapia"
q("yb2t-01", T, "m", L2, "Che cosa accomuna i recettori della famiglia HER (erb)?", [
  "Sono recettori tirosin-chinasici per fattori simili all'EGF, mutati in diversi tumori",
  "Sono recettori serin/treonin-chinasici per il TGF-β, mutati in diversi tumori",
  "Sono GPCR per le chemochine, sfruttati dal virus HIV per richiamare e infettare i leucociti",
  "Sono recettori per le citochine che usano la via JAK-STAT nelle cellule tumorali",
  "Sono recettori canale per il Ca²⁺, iperespressi nelle cellule del glioblastoma",
  ], 0,
  "HER1 (vescica, seno, rene, prostata, glioblastoma), HER2 (forma eterodimeri), HER3 (mammella), HER4 (ovaio).")
q("yb2t-02", T, "h", L2, "In un carcinoma mammario con HER2 iperespresso, perché bloccare HER2 riduce anche la segnalazione partita da HER1 e HER3?", [
  "HER2 attiva gli altri HER formando eterodimeri: senza HER2 quei dimeri non segnalano",
  "HER2 è il recettore che lega l'EGF e poi lo passa a HER1 e HER3 come se fosse un trasportatore",
  "L'anticorpo anti-HER2 riconosce anche HER1 e HER3, che hanno lo stesso epitopo",
  "HER2 fosforila il fattore di crescita, che solo così riesce a legare HER1 e HER3",
  "Bloccando HER2 la cellula smette di trascrivere i geni di HER1 e di HER3",
  ], 0,
  "HER2 non lega fattori di crescita ma dimerizza con HER1, HER3 e HER4 e li attiva: per questo è il bersaglio del trastuzumab.")
q("yb2t-03", T, "l", L2, "Secondo la sbobina, a quale tumore è associato HER4?", [
  "Al tumore dell'ovaio", "Al carcinoma mammario", "Al glioblastoma", "Al cancro della vescica", "Al tumore della prostata",
  ], 0,
  "HER3 è associato al carcinoma mammario; HER1 a vescica, seno, rene, prostata e glioblastomi.")

T = "bm2-sertre"
q("yb2s-01", T, "m", L2, "Com'è fatto un recettore serin/treonin-chinasico per il TGF-β?", [
  "Una sola elica transmembrana, N-terminale extracellulare che lega il fattore, C-terminale catalitico",
  "Sette eliche transmembrana, N-terminale extracellulare che lega il fattore, loop C3 per la proteina G",
  "Una sola elica transmembrana, N-terminale citosolico catalitico, C-terminale che lega il fattore",
  "Cinque subunità con quattro eliche ciascuna, che formano un canale per anioni dopo il legame",
  "Un tetramero 2α + 2β già assemblato senza ligando, con attività chinasica sulle tirosine",
  ], 0,
  "Col ligando dimerizza e si autofosforila su serina e treonina, poi fosforila le Smad.")
q("yb2s-02", T, "h", L2, "Una mutazione impedisce alle Smad fosforilate di formare eterodimeri. Che effetto ha sulla risposta al TGF-β?", [
  "Le Smad restano a bassa affinità per il DNA e i geni bersaglio non vengono attivati",
  "Le Smad entrano nel nucleo e attivano i geni anche senza essere fosforilate",
  "Il recettore non dimerizza più e smette di autofosforilarsi su serina e treonina",
  "Il segnale passa alla via JAK-STAT, che attiva gli stessi geni al posto delle Smad",
  "Le Smad diventano chinasi e fosforilano il recettore, che così resta sempre acceso",
  ], 0,
  "Fosforilazione ed eterodimerizzazione aumentano molto l'affinità delle Smad per il DNA; poi migrano nel nucleo.")
q("yb2s-03", T, "h", L2, "Che cosa hanno in comune recettori del TGF-β e recettori tirosin-chinasici, e che cosa li distingue?", [
  "Entrambi dimerizzano e si autofosforilano col ligando, ma su serina/treonina anziché su tirosina",
  "Entrambi usano JAK per fosforilarsi, ma uno attiva le STAT e l'altro attiva le proteine Smad nel citosol",
  "Entrambi sono già dimeri senza ligando, ma uno fosforila tirosine e l'altro serine e treonine",
  "Entrambi attivano Ras tramite SOS, ma uno agisce nel nucleo e l'altro solo nel citosol",
  "Entrambi hanno sette eliche transmembrana, ma solo uno è accoppiato a una proteina G",
  ], 0,
  "Il TGF-β passa il segnale alle Smad; gli RTK reclutano proteine con domini SH2 (es. via di Ras).")
q("yb2s-04", T, "l", L2, "Che cosa sono le BMP, ligandi dei recettori serin/treonin-chinasici?", [
  "Bone morphogenetic proteins", "Basic membrane proteins", "Binding motif peptides", "Bone matrix phosphatases", "B-cell maturation proteins",
  ], 0,
  "Insieme al TGF-β (transforming growth factor-β). Mutazioni di questi recettori favoriscono alcuni tumori.")

T = "bm2-citochine"
q("yb2k-01", T, "m", L2, "Com'è fatto un recettore per le citochine nella forma attiva?", [
  "Un complesso etero-oligomerico di subunità con una sola elica transmembrana ciascuna",
  "Un monomero con sette eliche transmembrana accoppiato a una proteina G trimerica",
  "Un omodimero con un dominio tirosin chinasico intrinseco nella porzione citosolica",
  "Un pentamero di subunità a quattro eliche che forma un canale per i cationi",
  "Un tetramero 2α + 2β tenuto insieme da ponti disolfuro, come il recettore dell'insulina",
  ], 0,
  "La porzione citosolica non ha attività enzimatica: ha domini di interazione che reclutano le chinasi JAK.")
q("yb2k-02", T, "h", L2, "Perché la via JAK-STAT può dare risposte molto diverse in cellule diverse?", [
  "Recettori diversi usano JAK diverse, che fosforilano STAT diverse capaci di formare eterodimeri",
  "Ogni cellula ha una sola JAK, ma questa fosforila in modo casuale tutte le STAT disponibili nel citosol",
  "Le STAT entrano nel nucleo senza essere fosforilate e scelgono i geni in base al pH del nucleo",
  "Il recettore cambia ligando a seconda del tessuto, mentre JAK e STAT restano sempre le stesse",
  "JAK attiva Ras in alcune cellule e la PKA in altre, mentre STAT non partecipa mai al segnale",
  ], 0,
  "La combinazione ligando-recettore-JAK-STAT rende selettiva l'espressione del gene nella cellula specifica.")
q("yb2k-03", T, "h", L2, "In un paziente con poca eritropoietina, quale passaggio della via manca nei precursori dei globuli rossi?", [
  "Senza ligando il recettore non dimerizza, JAK non lo fosforila e STAT non attiva i geni del ciclo cellulare",
  "Il recettore non si autofosforila sulle tirosine e quindi non recluta Grb2 e SOS né attiva la via di Ras",
  "La proteina Gs non scambia il GDP con il GTP e l'adenilato ciclasi non produce cAMP",
  "Le Smad non vengono fosforilate e non riescono a entrare nel nucleo dei precursori",
  "Il recettore canale resta chiuso e il Ca²⁺ non entra nei precursori dei globuli rossi",
  ], 0,
  "Il recettore dell'eritropoietina segue la via JAK-STAT e controlla la proliferazione dei globuli rossi.")
q("yb2k-04", T, "l", L2, "In quali processi è coinvolta la via JAK-STAT secondo la sbobina?", [
  "Processi immunitari, controllo della divisione cellulare e, se deregolata, tumori",
  "Glicogenolisi epatica, contrazione cardiaca e, se deregolata, diabete di tipo 1",
  "Trasmissione sinaptica, visione e, se deregolata, malattie neurodegenerative gravi",
  "Controllo della pressione, volume ematico e, se deregolata, ipertensione",
  "Coagulazione, riparazione delle ferite e, se deregolata, malattie del collagene",
  ], 0,
  "Le citochine (interleuchine, interferoni) agiscono in modo autocrino e paracrino come regolatori di crescita e differenziamento.")

# ── Lezione 3 ─────────────────────────────────────────────────────────────
T = "bm3-gpcr"
q("yb3g-01", T, "m", L3, "Quali sono i due principali effettori attivati dai GPCR secondo la sbobina?", [
  "Adenilato ciclasi e fosfolipasi C", "Guanilato ciclasi e fosfolipasi A2", "PKA e PKC", "Ras e la MAP chinasi", "JAK e STAT",
  ], 0,
  "L'adenilato ciclasi apre la via del cAMP, la fosfolipasi C quella di IP₃ e DAG.")
q("yb3g-02", T, "h", L3, "Dopo lo scambio GDP/GTP la Gα si separa da βγ. Come raggiunge l'adenilato ciclasi?", [
  "Scorre sul versante citosolico della membrana, a cui resta ancorata dalla coda prenilica",
  "Diffonde liberamente nel citosol fino al reticolo, dove si trova l'adenilato ciclasi",
  "Viene trasportata dalla β-arrestina fino all'effettore scorrendo lungo il citoscheletro",
  "Resta legata al recettore, che la porta all'adenilato ciclasi con un'endocitosi",
  "Entra nel nucleo, dove attiva la trascrizione del gene dell'adenilato ciclasi",
  ], 0,
  "α e γ hanno un'ancora prenilica; β resta in membrana legata a γ. Così tutto il sistema rimane sulla membrana.")
q("yb3g-03", T, "h", L3, "Le affinità dei GPCR per i loro ligandi vanno dal nanomolare al millimolare. Perché?", [
  "Mediano segnali sinaptici, autocrini, paracrini ed endocrini, con concentrazioni locali molto diverse",
  "Sono tutti recettori endocrini, ma i ligandi più grandi e idrofilici si legano con un'affinità più bassa",
  "L'affinità dipende soltanto dal tipo di proteina G accoppiata, non dalla distanza del segnale",
  "Sono tutti recettori sinaptici, e l'affinità cambia con la frequenza dei potenziali d'azione",
  "L'affinità cresce con il numero di eliche transmembrana, che varia molto tra i diversi GPCR",
  ], 0,
  "Più il segnale viaggia e si diluisce (endocrino), più serve affinità alta; nelle sinapsi la concentrazione locale è alta.")
q("yb3g-04", T, "l", L3, "Quale classe di GPCR è indicata come bersaglio terapeutico contro l'HIV?", [
  "I recettori per le chemochine", "I recettori β-adrenergici", "I recettori muscarinici", "I recettori della rodopsina", "I recettori della dopamina",
  ], 0,
  "Le chemochine sono citochine chemotattiche che richiamano i leucociti; il virus le sfrutta e si cercano farmaci antirecettore.")

T = "bm3-camp"
q("yb3c-01", T, "m", L3, "Come forma il cAMP l'adenilato ciclasi?", [
  "Lega il fosfato α dell'ATP al suo 3'-OH, ciclizzandolo e liberando pirofosfato",
  "Lega il fosfato γ dell'ATP al suo 5'-OH, ciclizzandolo e liberando ADP",
  "Lega il fosfato α del GTP al suo 3'-OH, ciclizzandolo e liberando il pirofosfato",
  "Lega il fosfato dell'AMP al suo 2'-OH, ciclizzandolo e liberando acqua",
  "Lega il fosfato β dell'ATP al suo 3'-OH, ciclizzandolo e liberando fosfato",
  ], 0,
  "La fosfodiesterasi spegne il segnale rompendo il legame 3'-fosfato: il cAMP diventa AMP.")
q("yb3c-02", T, "h", L3, "Nella sonda FRET per l'attività della PKA (CFP sulla sequenza bersaglio, YFP sul dominio che lega le fosfoserine), eccitando a 433 nm si vede emissione a 527 nm. Che cosa indica?", [
  "La PKA è attiva: ha fosforilato la serina e il dominio di legame ha avvicinato le due sonde",
  "La PKA è inattiva: la serina non è fosforilata e la sonda ciano emette nell'azzurro senza trasferimento",
  "Il cAMP è basso: subunità regolatrice e catalitica sono rimaste associate tra loro",
  "La PKA ha fosforilato la sonda gialla, che emette direttamente quando viene eccitata",
  "Una fosfatasi ha staccato il fosfato e le due sonde fluorescenti si sono allontanate",
  ], 0,
  "Con la serina fosforilata CFP e YFP sono vicine: la luce emessa dalla CFP eccita la YFP, che emette nel giallo (527 nm).")
q("yb3c-03", T, "h", L3, "Quante molecole di cAMP servono per liberare entrambe le subunità catalitiche della PKA, e come si legano?", [
  "Quattro, due per ogni subunità regolatrice, con legame cooperativo",
  "Due, una per ogni subunità regolatrice, con legame indipendente",
  "Quattro, due per ogni subunità catalitica, con legame competitivo",
  "Una sola, che si lega tra le due subunità regolatrici del tetramero",
  "Otto, due per ognuna delle quattro subunità, con legame cooperativo",
  ], 0,
  "Legato il cAMP, la subunità regolatrice passa da una forma «a manubrio» a una forma «a conca» e perde affinità per la catalitica.")
q("yb3c-04", T, "h", L3, "La PKA controlla in modo reciproco il metabolismo del glicogeno. Quale combinazione è corretta?", [
  "Fosforila la fosforilasi chinasi (degradazione attivata) e la glicogeno sintasi (sintesi inattivata)",
  "Fosforila la glicogeno sintasi (sintesi attivata) e la fosforilasi chinasi (degradazione inattivata)",
  "Defosforila la glicogeno fosforilasi (degradazione attivata) e la glicogeno sintasi (sintesi attivata)",
  "Fosforila direttamente la glicogeno fosforilasi sulla Ser14 e attiva la PP1 sul granulo",
  "Fosforila la PP1, che a sua volta attiva sia la glicogeno sintasi sia la glicogeno fosforilasi",
  ], 0,
  "Tra i bersagli della PKA ci sono anche la piruvato chinasi e il fattore di trascrizione CREB.",
  note="Sbobina di Biologia molecolare, lezione 3: mette la glicogeno sintasi tra le proteine «attivate» dalla PKA; la fosforilazione la inattiva (lo dicono le lezioni 4 e 5).")
q("yb3c-05", T, "l", L3, "Quanti segmenti transmembrana ha l'adenilato ciclasi e dove si forma il sito catalitico?", [
  "12; dall'incontro del loop tra le eliche 6 e 7 con la porzione C-terminale",
  "7; dall'incontro del loop citosolico C3 con la porzione C-terminale",
  "12; dall'incontro delle estremità N- e C-terminali, entrambe extracellulari",
  "1; nel dominio citosolico che segue l'unica elica transmembrana",
  "6; dall'incontro del loop tra le eliche 2 e 3 con la porzione N-terminale",
  ], 0,
  "Le estremità N- e C-terminali sono entrambe citosoliche.")
q("yb3c-06", T, "l", L3, "Quali residui compaiono di solito nelle sequenze consenso fosforilate dalla PKA?", [
  "Una serina, con residui basici (arginina) e piccoli apolari (alanina, glicina) vicini",
  "Una tirosina, con residui acidi (aspartato) e aromatici (fenilalanina) vicini",
  "Una treonina, con residui di prolina che la precedono e la seguono",
  "Una serina, preceduta da una fosfoserina di innesco messa in precedenza dalla caseina chinasi II",
  "Una cisteina, con residui basici (lisina) e una glicina in posizione −1",
  ], 0,
  "La fosfoserina di innesco della caseina chinasi II serve invece alla GSK3 (lezione 5).")

T = "bm3-spegnimento"
q("yb3s-01", T, "m", L3, "Quali meccanismi spengono la segnalazione dei GPCR secondo la sbobina?", [
  "Attività GTPasica della Gα, fosforilazione del recettore con β-arrestina, fosfatasi richiamate vicino alla PKA",
  "Idrolisi del GTP da parte di GAP, taglio proteolitico del recettore, esportazione del cAMP fuori dalla cellula",
  "Defosforilazione della Gα, internalizzazione dell'adenilato ciclasi, degradazione della PKA nel proteasoma",
  "Legame della calmodulina al recettore, chiusura dei canali del Ca²⁺, sintesi di nuovo GDP nel citosol",
  "Ubiquitinazione dell'agonista, fosforilazione delle subunità βγ, apertura dei canali del K⁺",
  ], 0,
  "A questi si aggiungono l'inattivazione dell'agonista e la fosfodiesterasi che degrada il cAMP.")
q("yb3s-02", T, "h", L3, "Perché la β-arrestina impedisce l'attivazione della proteina G anche se l'adrenalina resta legata al recettore?", [
  "Si lega sulla stessa superficie citosolica del recettore a cui dovrebbe legarsi la proteina G",
  "Idrolizza il GTP della Gα appena questa si stacca dalle subunità β e γ del trimero inattivo in membrana",
  "Sposta l'adrenalina dal sito di legame extracellulare e prende il suo posto",
  "Fosforila la Gα sulla coda prenilica e la stacca dalla membrana plasmatica",
  "Lega l'adenilato ciclasi e la tiene lontana dalla Gα attivata dal recettore",
  ], 0,
  "Il recettore fosforilato dalla βARK lega la β-arrestina, viene endocitato e poi riciclato in membrana o degradato.")
q("yb3s-03", T, "h", L3, "Dopo l'idrolisi del GTP, perché la Gα torna ad associarsi a βγ?", [
  "Persa il fosfato γ, la sua affinità per βγ aumenta moltissimo e si riforma il trimero inattivo",
  "La β-arrestina riporta βγ sulla Gα e le lega con un legame covalente in membrana",
  "Le subunità βγ vengono fosforilate dalla PKA e così riacquistano affinità per la Gα",
  "La Gα-GDP si stacca dalla membrana e βγ la cattura nel citosol prima che diffonda",
  "Il recettore, agendo da GEF, lega insieme Gα e βγ dopo aver rimosso il GDP dalla Gα attivata",
  ], 0,
  "È il meccanismo di spegnimento intrinseco della proteina G: la stessa Gα che scambia il nucleotide lo idrolizza.")
q("yb3s-04", T, "l", L3, "Quale meccanismo di spegnimento agisce a livello dell'agonista?", [
  "La sua inattivazione o metabolizzazione, come per l'acetilcolina",
  "La sua fosforilazione da parte della βARK sulla coda C-terminale",
  "Il suo legame alla β-arrestina, che lo porta nella vescicola",
  "La sua ADP-ribosilazione da parte di una tossina batterica",
  "Il suo trasporto nel nucleo, dove regola la sintesi del recettore",
  ], 0,
  "Gli altri livelli sono il recettore (desensibilizzazione, internalizzazione) e la proteina G (GTPasi).")

T = "bm3-cgmp"
q("yb3m-01", T, "m", L3, "Quali processi controlla il cGMP secondo la sbobina?", [
  "Contrattilità muscolare, visione, omeostasi del volume ematico",
  "Glicogenolisi epatica, lipolisi, secrezione di insulina",
  "Proliferazione dei globuli rossi, risposta immunitaria, apoptosi",
  "Trasmissione sinaptica eccitatoria, memoria, sonno",
  "Sintesi del collagene, coagulazione, riparazione delle ferite",
  ], 0,
  "Si forma dal GTP per opera della guanilato ciclasi (di membrana o citosolica) e attiva la PKG.")
q("yb3m-02", T, "h", L3, "Quali effetti della PKG concorrono al rilassamento della muscolatura liscia dei vasi?", [
  "Riduce il Ca²⁺ dal RE, attiva la fosfatasi delle catene leggere della miosina e apre canali K⁺",
  "Aumenta il Ca²⁺ dal RE, attiva la chinasi delle catene leggere della miosina e chiude canali K⁺",
  "Riduce il cAMP, inibisce la fosfatasi delle catene leggere della miosina e apre canali Cl⁻",
  "Aumenta l'IP₃, fosforila le catene leggere della miosina e apre i canali del Ca²⁺ di membrana",
  "Riduce il cGMP, attiva la PKA nel citosol e apre i canali del Ca²⁺ voltaggio-dipendenti",
  ], 0,
  "L'apertura dei canali K⁺ iperpolarizza e inibisce i canali del Ca²⁺ voltaggio-dipendenti: altro Ca²⁺ in meno.")
q("yb3m-03", T, "h", L3, "Cellule stimolate con NO e ristimolate un'ora dopo producono molto meno cGMP. Quale intervento ripristinerebbe meglio la risposta?", [
  "Un inibitore della fosfodiesterasi del cGMP, che la PKG ha attivato durante la prima stimolazione",
  "Un inibitore della guanilato ciclasi solubile, per evitare che si desensibilizzi una seconda volta",
  "Un attivatore della PKA, perché il cAMP stimola direttamente la guanilato ciclasi solubile",
  "Un chelante del ferro, per liberare il sito dell'eme e far legare più molecole di NO",
  "Un inibitore della PKG, così il cGMP prodotto resta libero e non viene usato dalla chinasi",
  ], 0,
  "La fosfodiesterasi attivata resta attiva anche dopo la desensibilizzazione: è lo stesso principio del sildenafil (PDE5).")
q("yb3m-04", T, "l", L3, "Com'è fatta la PKG?", [
  "Un omodimero, in due isoforme (PKG-1 e PKG-2), con tre domini funzionali per subunità",
  "Un tetramero di due subunità catalitiche e due regolatrici che legano il cGMP, come la PKA",
  "Un monomero con un dominio PH che la ancora al fosfatidilinositolo",
  "Un eterodimero di una subunità che lega il cGMP e una catalitica",
  "Un omotrimero con un gruppo eme per subunità che lega l'NO",
  ], 0,
  "L'eme che lega l'NO sta nella guanilato ciclasi solubile, non nella PKG.")

# ── Lezione 4 ─────────────────────────────────────────────────────────────
T = "bm4-calcio"
q("yb4c-01", T, "m", L4, "Perché il Ca²⁺ libero nel citosol è bassissimo a riposo?", [
  "È pompato fuori e negli organelli, e quello rimasto è legato da proteine leganti il calcio",
  "Il Ca²⁺ non attraversa mai la membrana plasmatica, nemmeno attraverso i canali",
  "Viene trasformato in un secondo messaggero organico, come l'IP₃, appena entra nel citosol",
  "È tutto legato all'ATP, che lo trasporta nei mitocondri senza consumare energia",
  "Il reticolo endoplasmatico lo rilascia solo quando il citosol è già molto alcalino",
  ], 0,
  "Ca²⁺-ATPasi di membrana e del reticolo, antiporto Na⁺/Ca²⁺ e Calcium Binding Proteins mantengono l'omeostasi.")
q("yb4c-02", T, "h", L4, "Il Ca²⁺ è ≈10⁻³ M fuori dalla cellula e nel RE, ≈10⁻⁷ M nel citosol. Quale conseguenza funzionale ha questo gradiente?", [
  "Basta aprire dei canali per far salire rapidamente il Ca²⁺ citosolico e generare il segnale",
  "Serve sempre ATP per far entrare il Ca²⁺ nel citosol quando arriva un segnale",
  "Il Ca²⁺ entra nella cellula solo per diffusione semplice attraverso il doppio strato fosfolipidico",
  "Il segnale nasce dalla diminuzione del Ca²⁺ citosolico, non dal suo aumento",
  "Il Ca²⁺ si muove solo dal citosol verso il RE, mai nella direzione opposta",
  ], 0,
  "Sono i secondi messaggeri a variare: la variazione del Ca²⁺ citosolico è ciò che innesca la risposta.")
q("yb4c-03", T, "h", L4, "Che differenza c'è tra recettore per l'IP₃ e recettore per la rianodina nel modo in cui si aprono?", [
  "Il primo si apre legando l'IP₃; il secondo è aperto fisiologicamente dal Ca²⁺ stesso",
  "Il primo si apre legando il Ca²⁺; il secondo è aperto fisiologicamente dalla rianodina",
  "Il primo si apre con il DAG in membrana; il secondo con l'IP₃ che diffonde nel citosol",
  "Il primo si apre quando la membrana si depolarizza; il secondo con il legame della calmodulina",
  "Entrambi si aprono solo legando l'IP₃, ma il secondo si trova nella membrana plasmatica",
  ], 0,
  "La rianodina è un alcaloide vegetale, non una molecola endogena. Anche la Ca²⁺-calmodulina favorisce la riapertura del recettore per la rianodina.")
q("yb4c-04", T, "l", L4, "Che cos'è la rianodina?", [
  "Un alcaloide vegetale con attività insetticida", "Un peptide endogeno del reticolo sarcoplasmatico", "Un fosfolipide di membrana derivato dal PIP₂",
  "Una tossina batterica che ADP-ribosila la Gq", "Un nucleotide ciclico prodotto dalle cellule muscolari",
  ], 0,
  "A basse concentrazioni blocca il canale semiaperto (contrazione massiva), a concentrazioni µM lo chiude (paralisi).")

T = "bm4-calmodulina"
q("yb4m-01", T, "m", L4, "Con quali enzimi interagisce direttamente la Ca²⁺-calmodulina secondo la sbobina?", [
  "Fosfodiesterasi, adenilato ciclasi, Ca²⁺-ATPasi, chinasi delle catene leggere, fosforilasi chinasi",
  "Guanilato ciclasi, PKA, Na⁺/K⁺-ATPasi, fosfatasi delle catene leggere della miosina, glicogeno fosforilasi",
  "Fosfolipasi C, PI3-chinasi, PKB, glicogeno sintasi chinasi 3, proteina fosfatasi 1",
  "Adenilato ciclasi, Ras, Raf, MEK, MAP chinasi, fattori di trascrizione fos e jun",
  "Esochinasi, fosfofruttochinasi, piruvato chinasi, piruvato deidrogenasi, citrato sintasi",
  ], 0,
  "Così il Ca²⁺ controlla nucleotidi ciclici, trasporto del Ca²⁺, contrazione liscia e metabolismo del glicogeno.")
q("yb4m-02", T, "h", L4, "In una cellula sale il Ca²⁺ citosolico. Quale catena porta alla trascrizione di geni specifici?", [
  "Ca²⁺-calmodulina → CaM chinasi → fosforilazione di CREB → trascrizione",
  "Ca²⁺-calmodulina → PKA → fosforilazione delle Smad → trascrizione",
  "Ca²⁺ → PKC → fosforilazione di STAT → dimerizzazione di STAT → trascrizione",
  "Ca²⁺-calmodulina → adenilato ciclasi → cAMP → STAT → trascrizione",
  "Ca²⁺ → guanilato ciclasi → cGMP → fos e jun → trascrizione",
  ], 0,
  "CREB è lo stesso fattore fosforilato dalla PKA nella via del cAMP.")
q("yb4m-03", T, "h", L4, "Perché la calmodulina può amplificare un segnale partito dall'IP₃?", [
  "Legata al Ca²⁺ si lega ai recettori per la rianodina e ne favorisce la riapertura",
  "Legata al Ca²⁺ attiva la fosfolipasi C e fa produrre altro IP₃ dal PIP₂",
  "Senza Ca²⁺ chiude le pompe Ca²⁺-ATPasi, così il Ca²⁺ resta nel citosol",
  "Legata al Ca²⁺ si lega al recettore dell'IP₃ e lo trasforma in un canale aperto per il Na⁺",
  "Senza Ca²⁺ attiva la PKC, che fosforila e apre i canali del Ca²⁺ di membrana",
  ], 0,
  "Il Ca²⁺ uscito dal recettore dell'IP₃ attiva i recettori per la rianodina e i canali voltaggio-dipendenti: il segnale si amplifica.")
q("yb4m-04", T, "l", L4, "Nel loop della mano EF, quanti legami di coordinazione forma il Ca²⁺ e con che geometria?", [
  "7, bipiramide pentagonale", "6, ottaedrica", "4, tetraedrica", "7, prisma trigonale", "8, antiprisma quadrato",
  ], 0,
  "I legami si formano con altrettanti residui acidi; la calmodulina ha due domini EF, ognuno lega 2 Ca²⁺ (4 in tutto).")

T = "bm4-fosfoinositidi"
q("yb4p-01", T, "m", L4, "Quale legame taglia ciascuna fosfolipasi?", [
  "A1: estere al C1; A2: estere al C2; C: tra C3 e fosfato; D: libera la testa polare",
  "A1: estere al C2; A2: estere al C1; C: libera la testa polare; D: tra C3 e fosfato",
  "A1: tra C3 e fosfato; A2: estere al C2; C: estere al C1; D: libera la testa polare",
  "A1: estere al C1; A2: tra C3 e fosfato; C: estere al C2; D: libera la testa polare",
  "A1: estere al C1; A2: estere al C2; C: libera la testa polare; D: tra C3 e fosfato",
  ], 0,
  "La PLC sul PIP₂ libera DAG (resta in membrana) e IP₃; la PLD lascia l'acido fosfatidico; la A2 di solito libera l'arachidonato.")
q("yb4p-02", T, "h", L4, "Come si attiva la PKC passo per passo?", [
  "Il Ca²⁺ la porta in membrana sulla fosfatidilserina; lì il DAG le scopre il sito catalitico",
  "Il DAG la porta in membrana sulla fosfatidilserina; lì il Ca²⁺ le scopre il sito catalitico",
  "Il cAMP libera le sue subunità catalitiche, che poi si legano al DAG nella membrana",
  "L'IP₃ la lega nel citosol e la trasporta nel reticolo, dove viene fosforilata dal Ca²⁺",
  "Il PIP₃ la richiama con il dominio PH e la PI3-chinasi la fosforila in membrana",
  ], 0,
  "Servono entrambi i secondi messaggeri: il Ca²⁺ liberato dall'IP₃ e il DAG, presente solo se la PLC è stata attivata.")
q("yb4p-03", T, "h", L4, "PIP₃ e IP₃ derivano entrambi dal PIP₂. Che differenza c'è tra i due?", [
  "Il PIP₃ resta in membrana, non è substrato della PLC e attiva la PKB; l'IP₃ diffonde e libera Ca²⁺",
  "Il PIP₃ diffonde nel citosol e libera Ca²⁺ dal RE; l'IP₃ resta in membrana e attiva la PKB",
  "Il PIP₃ nasce dal taglio della PLC sul PIP₂; l'IP₃ dalla fosforilazione del PIP₂ in posizione 3",
  "Entrambi restano in membrana, ma il PIP₃ attiva la PKC e l'IP₃ attiva la PKA",
  "Il PIP₃ è prodotto dalla PLCγ degli RTK; l'IP₃ dalla PI3-chinasi attivata dalla Gq",
  ], 0,
  "La PI3-chinasi aggiunge un fosfato in posizione 3 dell'inositolo; la PLC taglia tra C3 del glicerolo e fosfato.")
q("yb4p-04", T, "l", L4, "Oltre che dalla Gq, da che cosa può essere attivata la PLCβ?", [
  "Dal dimero βγ delle proteine Gi", "Dalla fosforilazione da parte degli RTK", "Dal legame del PIP₃ al dominio PH", "Dalla PKA attivata dal cAMP", "Dal Ca²⁺-calmodulina",
  ], 0,
  "La PLCγ è quella attivata per fosforilazione dai recettori tirosin-chinasici.")

T = "bm4-asse"
q("yb4a-01", T, "m", L4, "Su quale bersaglio agiscono, nell'ordine, ACTH, TSH e LH/FSH secondo la sbobina?", [
  "Corteccia surrenale, tiroide, ovaio", "Midollare del surrene, tiroide, utero", "Tiroide, corteccia surrenale, ovaio",
  "Corteccia surrenale, ipotalamo, ghiandola mammaria", "Fegato, tiroide, ovaio",
  ], 0,
  "Ne derivano cortisolo, T3/T4 e progesterone. La midollare del surrene (adrenalina) è controllata direttamente dal SNC.")
q("yb4a-02", T, "h", L4, "Un paziente assume da mesi cortisolo ad alte dosi. Che cosa ti aspetti per l'ACTH e per l'ormone ipotalamico che lo regola?", [
  "Entrambi ridotti, per il feedback lungo dell'ormone periferico su ipofisi e ipotalamo",
  "Entrambi aumentati, perché il cortisolo stimola ipofisi e ipotalamo a produrre di più",
  "ACTH ridotto ma ormone ipotalamico aumentato, perché il feedback agisce solo sull'ipofisi",
  "ACTH aumentato ma ormone ipotalamico ridotto, per il solo feedback ultrabreve",
  "Nessuna variazione, perché il cortisolo esogeno non partecipa ai circuiti di feedback",
  ], 0,
  "Gli ormoni periferici agiscono con feedback a lungo termine su ipofisi e ipotalamo, come T3/T4 su TSH e TRH.",
  note="Il caso del cortisolo farmacologico non è nella sbobina: applica il feedback lungo spiegato con gli ormoni tiroidei.")
q("yb4a-03", T, "h", L4, "Nel dosaggio radioimmunologico, perché il rapporto tra ormone marcato legato e libero cala aggiungendo ormone non marcato?", [
  "L'ormone non marcato compete per lo stesso anticorpo e sposta quello radioattivo",
  "L'ormone non marcato degrada l'anticorpo e libera così l'ormone radioattivo legato",
  "L'ormone radioattivo decade più in fretta quando aumenta la concentrazione totale",
  "L'ormone non marcato si lega a un secondo anticorpo che porta un enzima colorato",
  "L'anticorpo lega con più affinità l'ormone non marcato perché è più piccolo",
  ], 0,
  "Con una curva standard si legge la concentrazione di un campione ignoto dal valore del rapporto.")
q("yb4a-04", T, "l", L4, "Come si forma il piroglutammato all'N-terminale del TRH?", [
  "Legame ammidico intramolecolare tra il carbossile laterale e l'α-ammino del glutammato",
  "Legame estere tra il carbossile laterale del glutammato e l'ossidrile dell'istidina",
  "Decarbossilazione del glutammato seguita da chiusura ad anello sul carbonio γ",
  "Legame ammidico tra l'α-carbossile del glutammato e l'azoto dell'istidina vicina",
  "Ossidazione del glutammato a chetone e successiva ciclizzazione con l'ammoniaca libera",
  ], 0,
  "Il TRH è piroglutammato-istidina-prolina ammidata; la sua scoperta è valsa il Nobel a Guillemin e Schally.")

# ── Lezione 5 ─────────────────────────────────────────────────────────────
T = "bm5-insulina"
q("yb5i-01", T, "m", L5, "Quale sequenza porta il glucosio a far secernere insulina dalla cellula β?", [
  "GLUT2 → glucochinasi → ↑ATP → chiusura dei canali K⁺-ATP → depolarizzazione → ingresso di Ca²⁺",
  "GLUT4 → esochinasi I → ↓ATP → apertura dei canali K⁺-ATP → iperpolarizzazione → ingresso di Ca²⁺",
  "GLUT2 → glucochinasi → ↑ATP → apertura dei canali K⁺-ATP → depolarizzazione → uscita di Ca²⁺",
  "GLUT2 → glucochinasi → ↑cAMP → PKA → fosforilazione dei granuli → esocitosi senza Ca²⁺",
  "GLUT4 → glucochinasi → ↑ATP → chiusura dei canali Na⁺ → iperpolarizzazione → ingresso di Ca²⁺",
  ], 0,
  "Il Ca²⁺ entrato stimola, attraverso i recettori rianodinici, il rilascio di altro Ca²⁺ e l'esocitosi dei granuli.")
q("yb5i-02", T, "h", L5, "Come fa la PKB a inattivare la GSK3?", [
  "Fosforila un sito di pseudosubstrato N-terminale che la GSK3 lega al posto del substrato, mascherando il sito catalitico",
  "Fosforila il sito catalitico della GSK3, che così non riesce più a legare l'ATP necessario alla fosforilazione dei substrati",
  "Lega la GSK3 con il dominio PH e la trasporta nel nucleo, lontano dalla glicogeno sintasi",
  "Defosforila la serina di innesco messa dalla caseina chinasi II sulla glicogeno sintasi",
  "Attiva la PP1, che stacca dalla GSK3 i fosfati necessari alla sua attività catalitica",
  ], 0,
  "La GSK3 riconosce i substrati tramite una fosfoserina di innesco; fosforilata dalla PKB si richiude su sé stessa.")
q("yb5i-03", T, "h", L5, "Durante uno stress acuto la glicemia sale ma l'insulina non aumenta come ci si aspetterebbe. Quale spiegazione è coerente con la sbobina?", [
  "Fibre simpatiche e adrenalina della midollare surrenale inibiscono il rilascio di insulina",
  "L'adrenalina degrada l'insulina già secreta nel sangue tramite la PKA epatica",
  "Lo stress chiude i GLUT2 della cellula β, che non riesce più a percepire il glucosio",
  "Il parasimpatico, attivo nello stress, blocca l'esocitosi tramite l'acetilcolina",
  "L'iperglicemia da stress inibisce la glucochinasi e abbassa così l'ATP prodotto nella cellula β",
  ], 0,
  "Il parasimpatico (acetilcolina, IP₃, Ca²⁺) stimola invece la secrezione durante la digestione.")
q("yb5i-04", T, "h", L5, "Quale di questi effetti dell'insulina è mediato dalla PKB nella via Ras-indipendente?", [
  "Traslocazione di GLUT4 in membrana nel muscolo e nel tessuto adiposo",
  "Attivazione dei fattori fos e jun da parte della MAP chinasi nel nucleo",
  "Fosforilazione di IRS1 da parte del recettore su residui di tirosina",
  "Reclutamento di Grb2 e SOS sulla IRS1 fosforilata in membrana",
  "Fosforilazione della glicogeno sintasi, che diventa così più attiva",
  ], 0,
  "La PKB inibisce anche la GSK3, attiva la PP1 e una fosfodiesterasi del cAMP. IRS1 fosforilata è comune alle due vie.")
q("yb5i-05", T, "l", L5, "Qual è la massa del substrato 1 del recettore dell'insulina (IRS1)?", [
  "≈ 130 kDa", "≈ 5,8 kDa", "≈ 51 kDa", "≈ 30 kDa", "≈ 300 kDa",
  ], 0,
  "5,8 kDa (5.808) è invece il peso molecolare dell'insulina.")
q("yb5i-06", T, "l", L5, "Secondo la sbobina, come si dividono in percentuale il diabete insulino-dipendente e quello non insulino-dipendente?", [
  "10% e 90%", "90% e 10%", "50% e 50%", "30% e 70%", "1% e 99%",
  ], 0,
  "Il primo (giovanile) è da bassa secrezione di insulina; il secondo (età adulta) è legato al recettore.")
