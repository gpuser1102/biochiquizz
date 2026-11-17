"""Giro 2026-11-17, blocco 2 – Biochimica I: tecniche di purificazione e analisi (p. 95–108),
enzimi: classificazione, caratteristiche e cinetica (p. 109–128)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Purificazione (p. 95–104) ──────────────────────────────────────────────
T = "d5-purificazione"
q("u1117-068", T, "m", "96", "Perché all'omogenato si aggiungono β-mercaptoetanolo o DTT?", [
  "Per tenere ridotte le cisteine ed evitare ponti disolfuro non nativi",
  "Per inibire le proteasi che gli organelli liberano durante la lisi cellulare",
  "Per mantenere il pH vicino alla neutralità durante tutta la lisi",
  "Per denaturare le proteine e renderle più solubili in acqua",
  "Per far precipitare le proteine senza alterarne la struttura",
  ], 0,
  "L'interno della cellula è riducente; a contatto con l'O₂ dell'aria le cisteine si ossiderebbero.")
q("u1117-069", T, "f", "96", "Perché l'omogenato cellulare si prepara a circa 4 °C?", [
  "Per evitare che il calore prodotto dalla lisi denaturi le proteine",
  "Per far precipitare le proteine di membrana prima della centrifuga",
  "Per attivare gli inibitori di proteasi aggiunti al tampone",
  "Per abbassare il pH dell'estratto fino al punto isoelettrico",
  "Per mantenere ossidate le cisteine e formare i ponti disolfuro",
  ], 0,
  "Le altre condizioni: pH vicino alla neutralità, inibitori di proteasi, agenti riducenti.")
q("u1117-070", T, "f", "97", "Che cosa succede alla solubilità di una proteina aumentando via via la forza ionica?", [
  "Prima aumenta (salting in), poi diminuisce fino a farla precipitare (salting out)",
  "Prima diminuisce (salting out), poi aumenta fino a scioglierla del tutto (salting in)",
  "Aumenta sempre, perché gli ioni schermano le cariche della proteina e la idratano",
  "Diminuisce sempre, perché gli ioni denaturano la proteina",
  "Non cambia, perché la solubilità dipende solo dal pH della soluzione",
  ], 0,
  "Ad alta forza ionica il sale sottrae acqua alla proteina, che precipita.")
q("u1117-071", T, "m", "97", "Perché per il salting out si usa soprattutto il solfato d'ammonio?", [
  "Libera tre ioni, uno con doppia carica, e dà una forza ionica elevata",
  "Lega covalentemente le proteine e le fa precipitare in forma nativa",
  "Abbassa il pH fino al punto isoelettrico di quasi tutte le proteine",
  "È un agente riducente e protegge le cisteine durante la precipitazione",
  "Libera due ioni monovalenti molto idratati che denaturano le proteine",
  ], 0,
  "Nella forza ionica la carica dello ione conta al quadrato: il solfato (2−) pesa molto.")
q("u1117-072", T, "m", "97", "Una proteina fatta precipitare con il salting out è denaturata?", [
  "No: precipita perché il sale le sottrae l'acqua, ma resta nella conformazione nativa",
  "Sì: il sale rompe i legami a idrogeno interni e la proteina perde la sua struttura nativa",
  "Sì: il sale riduce i ponti disolfuro e la catena polipeptidica si srotola del tutto",
  "No: precipita perché il sale la porta al suo punto isoelettrico",
  "Dipende: si denatura solo se il sale usato è il solfato d'ammonio",
  ], 0,
  "Per questo il salting out si usa come primo passaggio di purificazione.")
q("u1117-073", T, "f", "99", "Nella cromatografia a esclusione molecolare, quali proteine escono per prime?", [
  "Le più grandi, che non entrano nei pori dei granuli",
  "Le più piccole, che entrano nei pori dei granuli",
  "Le più cariche, che sono respinte dalla resina",
  "Le più idrofobiche, che non legano la resina",
  "Le più piccole, che scorrono negli spazi tra i granuli",
  ], 0,
  "Le piccole fanno un percorso più lungo dentro i granuli: serve più tampone per eluirle.")
q("u1117-074", T, "m", "99", "Tre proteine da 150, 60 e 15 kDa passano su una colonna a esclusione molecolare. In che ordine escono?", [
  "150 → 60 → 15 kDa", "15 → 60 → 150 kDa", "60 → 150 → 15 kDa", "Escono tutte insieme", "150 → 15 → 60 kDa"], 0,
  "Il volume di eluizione cresce al diminuire della massa.")
q("u1117-075", T, "h", "101", "La ribonucleasi ha 10 residui acidi e 18 basici (10 Lys, 4 Arg, 4 His). Perché a pH 7 ha carica netta positiva?", [
  "Le His sono quasi neutre, ma Lys, Arg e N-terminale danno 15 cariche positive contro 11 negative",
  "Le His sono tutte protonate e danno 18 cariche positive contro le 10 negative delle catene laterali acide",
  "A pH 7 i residui acidi sono ancora protonati e quindi non portano nessuna carica negativa netta",
  "Il C-terminale è protonato a pH 7 e si somma alle cariche positive delle catene laterali",
  "A pH 7 tutti i gruppi sono neutri tranne le arginine, che restano sempre positive",
  ], 0,
  "11 negative = 10 catene laterali acide + C-terminale. Il pI si raggiunge quando cominciano a dissociare lisine, arginine ed N-terminale.",
  note="Sbobina di Biochimica I, p. 101: riporta per la ribonucleasi un pI di 8,6. In letteratura il pI della ribonucleasi A pancreatica è più alto, intorno a 9,5; il ragionamento sul calcolo resta valido.")
q("u1117-076", T, "h", "101–102", "Su uno scambiatore cationico a pH 7 carichi una proteina con pI 9 e una con pI 5. Che cosa succede?", [
  "Quella con pI 9 si lega alla resina, quella con pI 5 esce subito",
  "Quella con pI 5 si lega alla resina, quella con pI 9 esce subito",
  "Si legano entrambe, perché a pH 7 tutte le proteine sono positive",
  "Escono entrambe subito, perché a pH 7 le proteine sono neutre",
  "Si separano per dimensione: la più grande esce per prima",
  ], 0,
  "Sotto il pI la carica netta è positiva (lega le cariche negative della resina); sopra il pI è negativa.")
q("u1117-077", T, "f", "101", "Che cosa lega uno scambiatore anionico?", [
  "Molecole cariche negativamente: la resina porta cariche positive",
  "Molecole cariche positivamente: la resina porta cariche negative",
  "Molecole cariche negativamente: la resina porta cariche negative",
  "Molecole idrofobiche: la resina porta gruppi alchilici",
  "Molecole con code di istidine: la resina porta ioni nichel",
  ], 0,
  "Lo scambiatore cationico ha cariche negative e lega i cationi.")
q("u1117-078", T, "h", "102", "Come si stacca una proteina legata a uno scambiatore cationico?", [
  "Aumentando il pH o la concentrazione di NaCl del tampone",
  "Abbassando il pH o la concentrazione di NaCl del tampone",
  "Aggiungendo imidazolo o il ligando libero della proteina",
  "Aggiungendo SDS e un agente riducente come il DTT",
  "Abbassando la temperatura della colonna fino a 4 °C",
  ], 0,
  "Alzando il pH la proteina perde cariche positive; il Na⁺ compete con la proteina per i gruppi negativi della resina.")
q("u1117-079", T, "m", "103", "Nella cromatografia per affinità, come si stacca la proteina trattenuta dalla resina?", [
  "Con un tampone che contiene il ligando libero, che compete con quello legato",
  "Con un tampone ad alta forza ionica, che fa precipitare la proteina sulla resina",
  "Con un detergente come l'SDS, che denatura la proteina e la libera",
  "Con un gradiente di pH, che porta la proteina al suo punto isoelettrico",
  "Con un tampone senza sali, che rigonfia i granuli e libera la proteina",
  ], 0,
  "Le proteine senza sito di legame per quel ligando escono subito dalla colonna.")
q("u1117-080", T, "h", "104", "Hai espresso una proteina ricombinante con una coda di 6 istidine. Come la purifichi e come la stacchi?", [
  "Resina con Ni²⁺; eluizione con imidazolo",
  "Resina con anticorpo anti-His; eluizione con Ni²⁺",
  "Scambiatore anionico; eluizione con imidazolo",
  "Resina con Ni²⁺; eluizione con SDS concentrato",
  "Resina con Zn²⁺; eluizione con β-mercaptoetanolo",
  ], 0,
  "L'imidazolo è il gruppo della catena laterale dell'istidina: compete con la coda per il nichel.")
q("u1117-081", T, "a", "103", "Nella cromatografia per immunoaffinità, perché la proteina si stacca cambiando il pH e non con un competitore?", [
  "Il legame antigene–anticorpo è molto forte: il pH cambia la protonazione dei residui coinvolti",
  "L'anticorpo non lega ligandi liberi: il pH serve a staccarlo dalla resina insieme alla proteina",
  "Il competitore denaturerebbe l'anticorpo: il pH invece lo lascia sempre intatto e attivo",
  "L'anticorpo lega la proteina solo al suo pI: cambiando pH la carica netta la respinge",
  "Il legame antigene–anticorpo è covalente: il pH acido idrolizza il legame con la resina",
  ], 0,
  "Si usa di solito un anticorpo monoclonale, specifico per un solo sito della proteina.")
q("u1117-082", T, "l", "104", "Quanti nucleotidi bisogna aggiungere al gene per ottenere una coda di 6 istidine?", [
  "18", "6", "12", "24", "36"], 0,
  "6 codoni × 3 nucleotidi, all'inizio o subito prima del codone di stop.")
q("u1117-083", T, "a", "104", "Nella cromatografia a interazione idrofobica, perché si aggiunge sale al tampone?", [
  "Sottrae acqua alla proteina ed espone le sue regioni idrofobiche alla resina",
  "Aumenta la carica netta della proteina e la fa legare ai gruppi della resina",
  "Riduce i ponti disolfuro e apre la proteina, esponendo il suo interno",
  "Compete con la proteina per la resina e ne accelera l'eluizione",
  "Porta la proteina al punto isoelettrico, dove diventa tutta idrofobica",
  ], 0,
  "La resina porta gruppi idrofobici; per eluire si abbassa la concentrazione di sale (non è nelle sbobine).")

# ── Analisi (p. 104–108) ───────────────────────────────────────────────────
T = "d5-analisi"
q("u1117-084", T, "f", "105", "In base a quale proprietà l'SDS-PAGE separa le proteine?", [
  "Massa", "Carica netta", "Punto isoelettrico", "Idrofobicità", "Affinità per un ligando"], 0,
  "Le proteine migrano tutte verso il polo positivo e le più grandi sono più rallentate dal gel.")
q("u1117-085", T, "m", "105", "Perché nell'SDS-PAGE la migrazione dipende solo dalla massa?", [
  "L'SDS denatura la proteina e la riveste di cariche negative: il rapporto carica/massa è costante",
  "L'SDS neutralizza tutte le cariche: la proteina migra solo per diffusione verso il polo positivo",
  "L'SDS porta ogni proteina al suo punto isoelettrico, dove la carica netta diventa nulla e non migra",
  "L'SDS rompe i legami peptidici e lascia frammenti tutti della stessa lunghezza",
  "L'SDS lega solo le regioni idrofobiche: migra di più la proteina più idrofobica",
  ], 0,
  "Si aggiungono anche un riducente (mercaptoetanolo) e calore, per rompere ponti disolfuro e struttura terziaria.")
q("u1117-086", T, "a", "105", "A che cosa serve la metilenbisacrilammide nella preparazione del gel di poliacrilammide?", [
  "Unisce tra loro le catene di acrilammide e crea i pori del gel",
  "Denatura le proteine e le riveste di cariche negative",
  "Avvia la polimerizzazione dell'acrilammide liberando radicali liberi",
  "Riduce i ponti disolfuro delle proteine caricate nei pozzetti",
  "Colora le bande delle proteine dopo la corsa elettroforetica",
  ], 0,
  "È formata da due acrilammidi unite da un ponte metilenico. La polimerizzazione è avviata dal persolfato.")
q("u1117-087", T, "h", "105, 66", "Una proteina in SDS-PAGE senza riducente dà una banda da 150 kDa; con β-mercaptoetanolo dà due bande, da 50 e 25 kDa. Che cosa puoi concludere?", [
  "È fatta di catene diverse, unite anche da ponti disolfuro (es. 2 da 50 e 2 da 25 kDa)",
  "È un monomero da 150 kDa che il riducente taglia in due frammenti per proteolisi",
  "È fatta di subunità tutte uguali, unite solo da interazioni deboli non covalenti tra loro",
  "È un dimero da 75 kDa con un solo ponte disolfuro all'interno di ciascuna catena",
  "Il riducente ha denaturato la proteina, che senza riducente era rimasta nativa",
  ], 0,
  "È il caso di un anticorpo: due catene pesanti e due leggere tenute insieme da ponti disolfuro. Nell'SDS-PAGE la proteina è denaturata in entrambi i casi.")
q("u1117-088", T, "m", "106", "Nel Western blot, che cosa riconosce l'anticorpo secondario?", [
  "La parte comune (catene pesanti) dell'anticorpo primario",
  "Un secondo sito della proteina, diverso da quello del primario",
  "La membrana su cui sono state trasferite le proteine",
  "Il substrato dell'enzima, che diventa colorato",
  "L'SDS legato alle proteine trasferite sulla membrana",
  ], 0,
  "Il secondario porta un enzima che, col suo substrato, dà un prodotto colorato o luminescente.")
q("u1117-089", T, "f", "107", "Quali enzimi sono legati di solito all'anticorpo secondario nel Western blot?", [
  "Fosfatasi alcalina o perossidasi di rafano",
  "Tripsina o chimotripsina",
  "Luciferasi di lucciola o glucosio ossidasi",
  "DNA polimerasi o trascrittasi inversa virale",
  "Anidrasi carbonica o catalasi",
  ], 0,
  "Il prodotto della reazione è colorato o emette luce (chemiluminescenza).")
q("u1117-090", T, "m", "107", "In che ordine si separano le proteine nell'elettroforesi bidimensionale?", [
  "Prima per pI (isoelettrofocalizzazione), poi per massa (SDS-PAGE)",
  "Prima per massa (SDS-PAGE), poi per pI (isoelettrofocalizzazione)",
  "Prima per massa (gel filtrazione), poi per carica (scambio ionico)",
  "Prima per pI (scambio ionico), poi per affinità (immunoblot)",
  "Prima per idrofobicità, poi per massa in condizioni native",
  ], 0,
  "La prima dimensione non è denaturante: la proteina deve conservare la sua carica nativa per fermarsi al suo pI.")
q("u1117-091", T, "h", "107", "Due proteine hanno la stessa massa (40 kDa) ma pI 5,2 e 6,8. Quale tecnica le separa?", [
  "L'isoelettrofocalizzazione sì, l'SDS-PAGE da sola no",
  "L'SDS-PAGE sì, l'isoelettrofocalizzazione no",
  "La gel filtrazione sì, l'isoelettrofocalizzazione no",
  "Nessuna delle due: servono la dialisi e il salting out",
  "Solo la spettrometria di massa, perché hanno pI diversi",
  ], 0,
  "In SDS-PAGE migrano solo per massa e cadono nella stessa banda; nell'elettroforesi 2D si vedono come due spot.")
q("u1117-092", T, "a", "104", "Da che cosa dipende il coefficiente frizionale che rallenta una proteina in elettroforesi?", [
  "Da dimensione, forma e solvatazione della proteina e dalla viscosità del mezzo",
  "Solo dalla carica netta della proteina e dall'intensità del campo elettrico",
  "Dal punto isoelettrico della proteina e dal pH del tampone di corsa",
  "Dalla quantità di SDS legato e dalla temperatura della corsa",
  "Dalla sequenza amminoacidica e dal numero di ponti disolfuro presenti nella catena",
  ], 0,
  "All'equilibrio qE = fv: ogni proteina si muove a velocità costante, data dalla sua mobilità elettroforetica (μ = v/E = q/f).")
q("u1117-093", T, "m", "107–108", "Che cosa misura uno spettrometro MALDI-TOF?", [
  "Il tempo di volo degli ioni, che dipende dal rapporto massa/carica",
  "La velocità di sedimentazione, che dipende dalla densità della particella",
  "La migrazione in un gel, che dipende dal punto isoelettrico",
  "L'assorbimento a 280 nm, che dipende dagli aromatici",
  "La diffrazione dei raggi X, che dipende dal cristallo",
  ], 0,
  "MALDI = desorbimento/ionizzazione laser assistito da matrice; TOF = tempo di volo fino al detector.")
q("u1117-094", T, "l", "108", "In quale intervallo di masse lavora il MALDI-TOF secondo la sbobina?", [
  "Da circa 400 a 350.000 Da",
  "Da circa 10 a 1.000 Da",
  "Da circa 5.000 a 50.000 Da",
  "Da circa 1 a 10 milioni di Da",
  "Solo sopra 1 milione di Da",
  ], 0,
  "È anche molto sensibile: bastano quantità minime di campione.")
q("u1117-095", T, "a", "108", "A che cosa serve la matrice nel MALDI?", [
  "Assorbe l'energia del laser e la dissipa: la proteina si ionizza senza rompersi",
  "Lega la proteina in modo covalente e la libera solo quando arriva vicino al detector",
  "Separa le proteine per dimensione prima che entrino nell'analizzatore",
  "Fornisce gli elettroni che riducono i ponti disolfuro della proteina prima del volo",
  "Raffredda la proteina e la fa cristallizzare per l'analisi ai raggi X",
  ], 0,
  "Nell'ESI invece la proteina è nebulizzata in goccioline attraverso un capillare sotto voltaggio.")

# ── Classificazione e termodinamica (p. 109–115) ───────────────────────────
T = "d6-classificazione"
q("u1117-096", T, "f", "109", "A quale classe EC appartengono chinasi e transaminasi?", [
  "Trasferasi (EC 2)", "Ossidoreduttasi (EC 1)", "Liasi (EC 4)", "Ligasi (EC 6)", "Isomerasi (EC 5)"], 0,
  "Trasferiscono gruppi chimici (fosfato, gruppo amminico) da una molecola all'altra.")
q("u1117-097", T, "f", "109", "Che cosa indica il quarto numero del codice EC di un enzima?", [
  "Il substrato specifico: è unico per ogni enzima",
  "La classe generale della reazione catalizzata",
  "Il coenzima usato come accettore degli elettroni",
  "Il tessuto in cui l'enzima è più espresso",
  "Il numero di subunità dell'enzima attivo",
  ], 0,
  "Due enzimi possono condividere le prime tre cifre, mai la quarta.")
q("u1117-098", T, "m", "111", "La glutammato decarbossilasi ha codice EC 4.1.1.15. A quale classe appartiene?", [
  "Liasi", "Idrolasi", "Trasferasi", "Ossidoreduttasi", "Ligasi"], 0,
  "4.1 = scissione di legami C–C; 4.1.1 = decarbossilasi. La lisina decarbossilasi è 4.1.1.18.")
q("u1117-099", T, "f", "110", "Quale classe di enzimi è stata aggiunta di recente come EC 7?", [
  "Traslocasi", "Ossidoreduttasi", "Liasi", "Isomerasi", "Idrolasi"], 0,
  "Catalizzano il movimento di ioni o molecole attraverso le membrane.")
q("u1117-100", T, "a", "110", "Perché molte ATPasi di trasporto sono state spostate dalle idrolasi alla nuova classe EC 7?", [
  "La loro funzione principale è spostare ioni o molecole attraverso la membrana",
  "Non idrolizzano mai l'ATP, ma lo sintetizzano sfruttando i gradienti ionici",
  "Usano il GTP al posto dell'ATP e quindi non sono vere idrolasi",
  "Sono proteine solubili del citosol e non enzimi di membrana",
  "Trasferiscono il fosfato terminale dell'ATP a un substrato, come le chinasi",
  ], 0,
  "Le reazioni EC 7 sono scritte come trasferimenti da un lato 1 a un lato 2 della membrana; le sotto-sottoclassi indicano la reazione che fornisce l'energia.")
q("u1117-101", T, "l", "109", "Secondo la nomenclatura EC, a quale classe appartiene una fosfomutasi come la fosfoglucomutasi?", [
  "Isomerasi (EC 5)", "Trasferasi (EC 2)", "Liasi (EC 4)", "Ligasi (EC 6)", "Idrolasi (EC 3)"], 0,
  "Sposta il fosfato all'interno della stessa molecola (G1P ⇌ G6P): è una trasferasi intramolecolare, che la nomenclatura EC mette tra le isomerasi (EC 5.4).",
  note="Sbobina di Biochimica I, p. 109: elenca le fosfomutasi tra le trasferasi. Nella nomenclatura EC le mutasi sono isomerasi (sottoclasse 5.4, transferasi intramolecolari).")
q("u1117-102", T, "a", "111", "L'alcol deidrogenasi è EC 1.1.1.1 e la lattato deidrogenasi EC 1.1.1.27. Che cosa ci dicono questi codici?", [
  "Stessa classe, sottoclasse e sotto-sottoclasse (NAD⁺ accettore); substrati diversi",
  "Classi diverse: la prima è un'ossidoreduttasi, la seconda una trasferasi di elettroni",
  "Stesso substrato; la seconda usa un citocromo come accettore e non il NAD⁺",
  "Stessa reazione catalizzata: il quarto numero indica solo il tessuto di origine",
  "Stessa classe, ma la seconda usa l'O₂ come accettore, come le ossidasi",
  ], 0,
  "1 = ossidoreduttasi; 1.1 = agisce su gruppi alcolici (CH–OH); 1.1.1 = NAD(P)⁺ come accettore.",
  note="Sbobina di Biochimica I, p. 111: per la lattato deidrogenasi scrive «NAD dipendente, quindi sotto-sottoclasse 2». Il codice 1.1.1.27 indica la sotto-sottoclasse 1, la stessa dell'alcol deidrogenasi.")
q("u1117-103", T, "f", "112", "Quale classe di enzimi forma nuovi legami usando l'energia dell'idrolisi dell'ATP?", [
  "Ligasi", "Liasi", "Idrolasi", "Isomerasi", "Ossidoreduttasi"], 0,
  "Partono da tre reagenti (due substrati + ATP) e danno tre prodotti.")
q("u1117-104", T, "a", "112", "La piruvato decarbossilasi scinde un legame C–C e libera CO₂ e acetaldeide. Perché è una liasi e non un'idrolasi?", [
  "Rompe il legame senza usare l'acqua come secondo substrato",
  "Rompe il legame usando l'acqua e producendo così due prodotti",
  "Rompe il legame usando l'idrolisi dell'ATP come fonte di energia",
  "Sposta un gruppo all'interno della stessa molecola",
  "Trasferisce il gruppo carbossilico a un coenzima",
  ], 0,
  "Nelle idrolasi uno dei substrati è sempre l'acqua (es. l'ureasi: urea + H₂O → CO₂ + NH₃).")
q("u1117-105", T, "m", "113–114", "Che cosa modifica un enzima in una reazione?", [
  "Abbassa l'energia di attivazione, senza cambiare il ΔG",
  "Rende più negativo il ΔG e quindi la reazione più spontanea",
  "Sposta l'equilibrio verso i prodotti e aumenta la Keq",
  "Aumenta l'energia cinetica delle molecole che si urtano",
  "Rende possibili reazioni con ΔG positivo senza accoppiarle",
  ], 0,
  "Più molecole raggiungono lo stato di transizione alla stessa temperatura; l'equilibrio è raggiunto prima ma resta lo stesso.")
q("u1117-106", T, "h", "113–114", "Una reazione ha un ΔG molto negativo ma, senza enzima, non avviene in tempi misurabili. Come si spiega?", [
  "La velocità dipende dall'energia di attivazione, non dal ΔG",
  "Il ΔG negativo indica che la reazione procede verso i reagenti",
  "Il ΔG negativo rende la reazione lenta per definizione",
  "La reazione è all'equilibrio e quindi non procede",
  "Manca l'ATP che serve a tutte le reazioni spontanee",
  ], 0,
  "Spontaneità (ΔG) e velocità (energia di attivazione) sono indipendenti: l'equazione di Arrhenius lega la velocità a temperatura ed energia di attivazione.")
q("u1117-107", T, "m", "113–114", "Perché le cellule non possono accelerare le reazioni come si fa in laboratorio?", [
  "Lavorano a temperatura costante: per accelerare devono abbassare l'energia di attivazione",
  "Lavorano lontano dall'equilibrio: le reazioni non possono superare la velocità di diffusione",
  "Non possono variare le concentrazioni: per accelerare devono cambiare il ΔG delle reazioni",
  "Lavorano all'equilibrio: per accelerare devono consumare ATP in ogni singola reazione",
  "Non hanno catalizzatori inorganici: devono rendere positivo il ΔG con l'ATP",
  ], 0,
  "Aumentare la temperatura aumenta l'energia cinetica delle molecole, ma nella cellula non si può fare.")

# ── Caratteristiche degli enzimi (p. 115–118) ──────────────────────────────
T = "d6-caratteristiche"
q("u1117-108", T, "f", "116", "Che cosa dice il modello dell'adattamento indotto?", [
  "Il legame del substrato induce nell'enzima un cambio conformazionale che orienta i reagenti",
  "Il sito attivo è già perfettamente complementare al substrato e non cambia mai forma",
  "Il substrato cambia conformazione per adattarsi al sito attivo, mentre l'enzima resta rigido",
  "L'enzima si lega al prodotto e lo adatta al substrato successivo della via",
  "L'enzima si adatta al pH del compartimento cambiando la sua sequenza",
  ], 0,
  "Il modello chiave-serratura vale solo in parte: tutti gli enzimi cambiano conformazione per creare le condizioni della catalisi.")
q("u1117-109", T, "h", "116", "Il sito attivo occupa spesso meno del 5% della superficie dell'enzima. Perché serve comunque tutta la catena?", [
  "Il resto della catena dà forma al sito attivo e permette i cambi conformazionali della catalisi",
  "Il resto della catena serve solo a rendere l'enzima solubile e non ha ruolo nella reazione chimica",
  "Il resto della catena contiene altri siti attivi identici che lavorano a turno con il primo",
  "Il resto della catena lega l'ATP che serve a ogni ciclo catalitico",
  "Il resto della catena serve solo a far riconoscere l'enzima dal proteasoma",
  ], 0,
  "Il sito attivo è una tasca complementare al substrato, costruita dal ripiegamento dell'intera catena.")
q("u1117-110", T, "m", "117", "Come si chiama un coenzima legato in modo molto stabile o covalente all'enzima, come l'eme nei citocromi?", [
  "Gruppo prostetico", "Cosubstrato", "Apoenzima", "Effettore allosterico", "Zimogeno"], 0,
  "Altri coenzimi, come il NAD, si comportano da veri substrati che entrano ed escono dal sito attivo.")
q("u1117-111", T, "h", "117–118", "La pepsina lavora al meglio a pH molto acido, la fosfatasi alcalina intorno a pH 9. Perché lontano dall'optimum l'attività cala?", [
  "Cambia la protonazione dei residui che legano il substrato o catalizzano; a pH estremi la proteina si denatura",
  "Cambia la forza ionica della soluzione, che fa precipitare l'enzima ma non ne altera i residui catalitici del sito",
  "Il substrato si idrolizza da solo fuori dall'optimum e l'enzima non trova più niente da trasformare",
  "Il pH cambia il ΔG della reazione, che diventa positivo appena ci si allontana dall'optimum di pH dell'enzima",
  "Il pH ossida i ponti disolfuro del sito attivo e ne aumenta la Vmax, ma non l'affinità",
  ], 0,
  "Nella catalisi acido-base i residui del sito attivo donano o accettano protoni solo se hanno lo stato di protonazione giusto.",
  note="Sbobina di Biochimica I, p. 139: indica per la pepsina un optimum «di circa pH 5», mentre a p. 117 dice pH 2. L'optimum della pepsina è intorno a pH 2 (Lehninger).")
q("u1117-112", T, "a", "115", "Da dove viene in parte l'energia che favorisce la formazione del complesso enzima-substrato?", [
  "Dalle interazioni enzima-substrato e dalle molecole d'acqua che si liberano",
  "Dall'idrolisi di una molecola di ATP per ogni molecola di substrato legata",
  "Dall'aumento di temperatura locale nel sito attivo dell'enzima",
  "Dalla rottura di un legame covalente tra enzima e prodotto",
  "Dal ΔG negativo della reazione, ceduto all'enzima prima che inizi la catalisi",
  ], 0,
  "È l'energia di legame: le interazioni con l'enzima sostituiscono quelle con l'acqua, che guadagna entropia.")
q("u1117-113", T, "f", "117", "Da che cosa derivano nella maggior parte dei casi i coenzimi organici?", [
  "Vitamine idrosolubili", "Vitamine liposolubili", "Amminoacidi essenziali", "Acidi grassi essenziali", "Ormoni steroidei"], 0,
  "Molti cofattori sono invece ioni di metalli di transizione.")

# ── Cinetica enzimatica (p. 118–128) ───────────────────────────────────────
T = "d6-cinetica"
q("u1117-114", T, "m", "119", "Quando una reazione bimolecolare si comporta come una di pseudo-primo ordine?", [
  "Quando uno dei due reagenti è in grande eccesso rispetto all'altro",
  "Quando i due reagenti sono presenti alla stessa concentrazione iniziale",
  "Quando la reazione è all'equilibrio e la velocità netta è nulla",
  "Quando la reazione è catalizzata da un enzima allosterico",
  "Quando uno dei due reagenti è l'enzima e l'altro il prodotto",
  ], 0,
  "La concentrazione del reagente in eccesso cambia poco e finisce dentro la costante: v = k'[A].")
q("u1117-115", T, "m", "121", "Che cosa caratterizza lo stato stazionario di una reazione enzimatica?", [
  "La concentrazione del complesso ES resta costante nel tempo",
  "La concentrazione del substrato resta costante nel tempo",
  "Tutto l'enzima è libero e il prodotto non si forma ancora",
  "Le velocità di formazione e di consumo del prodotto si eguagliano",
  "L'enzima è tutto legato al prodotto e la reazione si ferma",
  ], 0,
  "Nei primi millisecondi (stato pre-stazionario) ES invece varia. Il substrato continua a scomparire e il prodotto a formarsi.",
  note="Sbobina di Biochimica I, p. 121: chiama k1 «costante di formazione di prodotto» e k2 «costante di decomposizione». Nello schema di Michaelis-Menten k1 è la formazione di ES, k₋1 la sua dissociazione in E + S e k2 la conversione di ES in E + P.")
q("u1117-116", T, "a", "125", "Nel grafico dei doppi reciproci (Lineweaver-Burk), dove si leggono Vmax e Km?", [
  "Intercetta sull'asse y = 1/Vmax; intercetta sull'asse x = −1/Km",
  "Intercetta sull'asse y = −1/Km; intercetta sull'asse x = 1/Vmax",
  "Intercetta sull'asse y = Vmax; pendenza della retta = Km",
  "Pendenza della retta = 1/Vmax; intercetta sull'asse x = Km",
  "Intercetta sull'asse y = Km/Vmax; intercetta sull'asse x = Vmax",
  ], 0,
  "La pendenza è Km/Vmax. La retta non passa per l'origine.")
q("u1117-117", T, "h", "127–128", "Studiando una reazione a due substrati, variando la concentrazione fissa di S2 ottieni nel grafico dei doppi reciproci rette parallele. Che cosa concludi?", [
  "Meccanismo a doppio spostamento: i due substrati non sono mai insieme nel sito attivo",
  "Meccanismo sequenziale ordinato: si forma sempre un complesso ternario con i due substrati",
  "Meccanismo sequenziale casuale: i substrati entrano nel sito attivo in ordine qualsiasi",
  "Inibizione da substrato: S2 in eccesso blocca il legame di S1 al sito attivo",
  "Cinetica allosterica: S2 è un effettore positivo che cambia la Vmax",
  ], 0,
  "Nei meccanismi sequenziali (ternari) le rette si incontrano in un punto a sinistra dell'asse y.")
q("u1117-118", T, "m", "126", "In un meccanismo sequenziale ordinato, in che ordine escono i prodotti?", [
  "In ordine inverso a quello di entrata dei substrati",
  "Nello stesso ordine di entrata dei substrati",
  "In ordine casuale, indipendente dai substrati",
  "Prima esce l'enzima modificato, poi i due prodotti",
  "Escono insieme ai substrati che non sono stati trasformati",
  ], 0,
  "Il primo substrato entrato è l'ultimo prodotto a uscire.")
q("u1117-119", T, "l", "126", "In quale gruppo di enzimi il meccanismo sequenziale ordinato è particolarmente comune?", [
  "Deidrogenasi NAD-dipendenti", "Transaminasi PLP-dipendenti", "Serin-proteasi pancreatiche", "Aspartil proteasi", "Metalloproteasi"], 0,
  "Le transaminasi seguono invece il meccanismo a doppio spostamento (ping-pong).")
q("u1117-120", T, "a", "125–126", "Perché per confrontare l'efficienza di due enzimi non basta il numero di turnover (kcat)?", [
  "Conta anche la Km: a [S] sotto la Km l'efficienza è data da kcat/Km",
  "Conta anche la Vmax: l'efficienza vera è data da kcat × Vmax",
  "La kcat cambia con la quantità di enzima e quindi non è una costante",
  "La kcat vale solo per gli enzimi allosterici, non per quelli michaeliani",
  "Conta solo la Km: la kcat è uguale per tutti gli enzimi di una classe",
  ], 0,
  "Un enzima veloce ma poco affine può essere meno efficiente di uno più lento ma con Km bassa.")
q("u1117-121", T, "h", "122", "A una [S] molto più bassa della Km, come sono distribuiti enzima libero e complesso ES?", [
  "Prevale l'enzima libero; ES è poco e v cresce quasi linearmente con [S]",
  "Prevale il complesso ES; l'enzima è saturo e v è vicina alla Vmax",
  "Enzima libero ed ES sono presenti in quantità uguali; v è metà della Vmax",
  "Tutto l'enzima è libero e la velocità della reazione è zero",
  "Prevale il complesso EP; il prodotto inibisce la reazione",
  ], 0,
  "Ad alta [S] invece tutto l'enzima è nel complesso ES: [ES] ≈ [E]totale e v = Vmax.")
q("u1117-122", T, "h", "121", "Nella cinetica di Michaelis-Menten si misura la velocità iniziale (v₀). Perché?", [
  "All'inizio il prodotto è trascurabile e la reazione inversa si può ignorare",
  "All'inizio l'enzima non è ancora legato al substrato e si misura k₋1",
  "All'inizio il substrato è esaurito e la velocità coincide con la Vmax",
  "All'inizio si è nello stato pre-stazionario, l'unico descritto dall'equazione",
  "All'inizio la reazione è all'equilibrio e la velocità netta è massima",
  ], 0,
  "Si misura nello stato stazionario precoce: [ES] costante e [P] ancora piccola.")
q("u1117-123", T, "m", "126–127", "Che cosa hanno in comune i meccanismi sequenziale ordinato e sequenziale casuale?", [
  "In entrambi i due substrati sono insieme nel sito attivo (complesso ternario)",
  "In entrambi l'enzima viene modificato (E') tra l'ingresso del primo e del secondo substrato",
  "In entrambi il primo prodotto esce prima che entri il secondo substrato",
  "In entrambi i substrati devono entrare in un ordine rigidamente fissato",
  "In entrambi le rette dei doppi reciproci risultano sempre parallele",
  ], 0,
  "Cambia solo l'ordine di ingresso: fisso nell'ordinato, qualsiasi nel casuale. Nel doppio spostamento il complesso ternario non si forma.")
