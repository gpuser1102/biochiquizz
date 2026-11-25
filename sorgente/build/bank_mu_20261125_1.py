"""Giro 2026-11-25, blocco 1 – riempimento degli argomenti scarni di Biologia molecolare,
lezioni 6 e 7: volemia, recettori intracellulari, organi di senso, nucleotidi."""
from bank_common import q as _q

S = "Biologia molecolare"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


L6, L7 = "lezione 6", "lezione 7"

# ── Vitamina D3 e VDR (lezione 7) ───────────────────────────────────────────
C = "bm7-vitd"

q("u1125-001", C, "f", L7, "Dove avvengono le due idrossilazioni che attivano la vitamina D3?", [
  "In posizione 25 nel fegato e in posizione 1 nel rene",
  "In posizione 1 nel fegato e in posizione 25 nel rene",
  "Entrambe nella pelle, subito dopo l'esposizione al sole",
  "In posizione 25 nell'intestino e in posizione 1 nell'osso",
  "Entrambe nel fegato, a carico di due diversi citocromi",
  ], 0,
  "Il colecalciferolo formato nella pelle viene idrossilato in 25 nel fegato (calcidiolo) e in 1 nel rene, dove si forma il calcitriolo, la forma attiva.")

q("u1125-002", C, "l", L7, "Nello schema della lezione, con quale partner il VDR si lega al suo elemento di risposta sul DNA?", [
  "Con il recettore dei retinoidi RXR",
  "Con il recettore dei glucocorticoidi",
  "Con la proteina inibitoria Hsp90",
  "Con un secondo VDR, come omodimero",
  "Con il recettore degli estrogeni",
  ], 0,
  "Nella figura il VDR forma un eterodimero con RXR sull'HRE e recluta coattivatori (p160, CBP/p300) e il complesso Mediator con la RNA polimerasi II.")

q("u1125-003", C, "m", L7, "Quali geni attiva il recettore della vitamina D3 secondo la lezione?", [
  "Quelli delle calbindine e delle ATPasi Ca²⁺-dipendenti",
  "Quelli del paratormone e della calcitonina della tiroide",
  "Quelli della 25-idrossilasi epatica e del colesterolo",
  "Quelli dell'osteocalcina e della sola fosfatasi acida",
  "Quelli dei canali del Na⁺ e della pompa Na⁺/K⁺",
  ], 0,
  "Il VDR con il ligando riconosce i VDRE e aumenta l'espressione di calbindine e ATPasi del Ca²⁺: più assorbimento intestinale di Ca²⁺ e fosfati, riassorbimento renale, mineralizzazione ossea.")

q("u1125-004", C, "h", L7, "Un paziente con insufficienza renale cronica sviluppa ipocalcemia pur avendo un calcidiolo (25-OH-D3) normale. Qual è la spiegazione più probabile?", [
  "Il rene danneggiato non idrossila più in posizione 1: manca il calcitriolo",
  "Il fegato non idrossila più in posizione 25: manca il calcidiolo",
  "La pelle non forma più colecalciferolo dal 7-deidrocolesterolo",
  "Il VDR intestinale viene degradato in assenza di filtrazione",
  "Il calcidiolo viene perso con le urine insieme alle proteine filtrate dal glomerulo",
  ], 0,
  "L'1α-idrossilazione avviene nel rene: se il rene non funziona il calcidiolo non diventa calcitriolo e cala l'assorbimento intestinale di Ca²⁺. L'esempio clinico non è nelle sbobine (Lehninger).")

# ── Olfatto (lezione 7) ────────────────────────────────────────────────────
C = "bm7-olfatto"

q("u1125-005", C, "l", L7, "Quanti tipi diversi di recettori olfattivi sono presenti, secondo la lezione, nei neuroni olfattivi?", [
  "Circa 1000",
  "Circa 10",
  "Circa 50",
  "Circa 100 000",
  "Uno solo, con molte isoforme",
  ], 0,
  "La combinazione di circa 1000 tipi di recettori permette di distinguere moltissimi odori. Non è nelle sbobine: nell'uomo i geni funzionanti sono circa 350, gli altri sono pseudogeni (Lehninger).")

q("u1125-006", C, "m", L7, "Come si spegne il segnale nel neurone olfattivo, secondo la lezione?", [
  "Il Ca²⁺ entrato fa chiudere gli stessi canali da cui è entrato",
  "Il cAMP viene esportato fuori dalla cellula attraverso le ciglia",
  "La molecola odorosa viene idrolizzata dal recettore stesso",
  "Il Cl⁻ uscito fa riaprire i canali del K⁺ a riposo",
  "La proteina G viene degradata nel proteasoma dopo ogni stimolo",
  ], 0,
  "Il Ca²⁺ apre i canali del Cl⁻ (depolarizzazione) e insieme chiude i canali controllati dal cAMP, spegnendo il segnale. Nel Lehninger l'effetto passa per Ca²⁺-calmodulina, che riduce l'affinità del canale per il cAMP.")

q("u1125-007", C, "a", L7, "Nel neurone olfattivo l'apertura dei canali del Cl⁻ depolarizza la cellula. Perché?", [
  "Il Cl⁻ è più concentrato dentro: uscendo porta fuori cariche negative",
  "Il Cl⁻ è più concentrato fuori: entrando porta dentro cariche positive",
  "Il Cl⁻ si lega al cAMP e lo rende più affine per i canali cationici",
  "Il Cl⁻ attiva l'adenilato ciclasi, che produce altro cAMP",
  "Il Cl⁻ esce insieme al Ca²⁺ e ne aumenta la concentrazione interna",
  ], 0,
  "Nella lezione: il Ca²⁺ apre i canali del Cl⁻, che fuoriesce e depolarizza. Il motivo (Cl⁻ interno alto in questi neuroni) non è nelle sbobine (Lehninger).")

q("u1125-008", C, "h", L7, "La lezione dice che i due enantiomeri del carvone hanno l'odore della menta verde e del vino. Che cosa è corretto?", [
  "Uno sa di menta verde, l'altro di cumino dei prati (carvi)",
  "Uno sa di vino, l'altro di menta piperita: la lezione è giusta",
  "Hanno lo stesso odore, perché sono riconosciuti dallo stesso recettore",
  "Uno solo dei due è odoroso; l'altro non lega alcun recettore",
  "Uno sa di limone, l'altro di arancia, come il limonene",
  ], 0,
  "⚠️ Errore nella sbobina (che scrive anche «carbone»): l'(R)-carvone sa di menta verde, l'(S)-carvone di cumino dei prati (carvi). Il concetto della lezione resta valido: recettori diversi riconoscono i due enantiomeri (Lehninger).",
  note="La sbobina di Biologia molecolare (lezione 7) scrive «R carbone e S carbone … menta verde e vino»: il secondo odore è quello del carvi.")

# ── Gusto (lezione 7) ──────────────────────────────────────────────────────
C = "bm7-gusto"

q("u1125-009", C, "f", L7, "Che cosa sono le «taste receptor cells» descritte nella lezione?", [
  "Cellule epiteliali con proprietà neuronali, come sinapsi e depolarizzazione",
  "Neuroni sensoriali veri e propri, con assoni che arrivano al cervello",
  "Cellule muscolari della lingua che si contraggono a contatto con il cibo",
  "Cellule ghiandolari che secernono la saliva e i suoi enzimi digestivi, come l'amilasi",
  "Cellule immunitarie che riconoscono le molecole estranee nel cibo",
  ], 0,
  "Sono cellule epiteliali specializzate che formano sinapsi e si depolarizzano; esprimono recettori a 7 eliche e la gustducina.")

q("u1125-010", C, "m", L7, "Come viene percepito un dolcificante artificiale, secondo la lezione?", [
  "Le βγ della gustducina attivano PLC e PKC, che chiude i canali del K⁺",
  "La Gα della gustducina attiva l'adenilato ciclasi e la PKA, come lo zucchero",
  "Il dolcificante entra nella cellula e apre direttamente i canali del Na⁺",
  "La gustducina attiva una fosfodiesterasi che abbassa il cAMP",
  "Il dolcificante lega un recettore tirosin-chinasico e attiva Ras",
  ], 0,
  "Lo zucchero usa la via Gα-cAMP-PKA; il dolcificante artificiale usa le subunità βγ → PLC → PKC: i canali del K⁺ si chiudono e si aprono quelli del Ca²⁺, rinforzando la depolarizzazione.")

q("u1125-011", C, "l", L7, "Nella percezione del dolce, in quale parte della cellula del gusto la PKA chiude i canali del K⁺?", [
  "Nella membrana basolaterale",
  "Nella membrana apicale",
  "Nella membrana del reticolo",
  "Nella membrana mitocondriale interna",
  "Nella membrana nucleare",
  ], 0,
  "Il cAMP si forma nella porzione apicale, diffonde e attiva la PKA, che fosforila e chiude i canali del K⁺ della membrana basolaterale.")

q("u1125-012", C, "h", L7, "Nella via dell'amaro la lezione scrive che l'IP₃ «determina un incremento del calcio nel reticolo endoplasmatico». Che cosa è corretto?", [
  "L'IP₃ apre canali del reticolo e fa uscire Ca²⁺ nel citosol",
  "L'IP₃ attiva la pompa SERCA e accumula Ca²⁺ dentro il reticolo",
  "L'IP₃ apre i canali del Ca²⁺ della membrana plasmatica",
  "L'IP₃ lega la calmodulina e sequestra il Ca²⁺ nel citosol",
  "L'IP₃ attiva la PKC, che porta il Ca²⁺ dentro il reticolo",
  ], 0,
  "⚠️ Imprecisione della sbobina: il recettore dell'IP₃ è un canale del reticolo; aprendosi aumenta il Ca²⁺ citosolico, non quello nel reticolo. Ne segue la depolarizzazione della cellula.",
  note="La sbobina di Biologia molecolare (lezione 7) parla di aumento del calcio «nel reticolo endoplasmatico»: è il Ca²⁺ citosolico che sale.")

# ── Vista (lezione 7) ──────────────────────────────────────────────────────
C = "bm7-vista"

q("u1125-013", C, "f", L7, "Come si chiama la proteina G attivata dalla rodopsina?", [
  "Transducina",
  "Gustducina",
  "Arrestina",
  "Gαs",
  "Gαq",
  ], 0,
  "La transducina è una proteina G trimerica (α, β, γ) che interagisce con il loop citosolico 3 della rodopsina.")

q("u1125-014", C, "f", L7, "In quale parte del bastoncello si trova la rodopsina?", [
  "Nei dischi membranosi del segmento esterno",
  "Nella membrana del segmento interno, vicino al nucleo",
  "Nelle sinapsi con i neuroni bipolari",
  "Nella membrana mitocondriale interna",
  "Nel citosol, legata ai microtubuli",
  ], 0,
  "Il segmento esterno è formato da dischi impilati che contengono la rodopsina; nel segmento interno stanno nucleo, mitocondri e reticolo.")

q("u1125-015", C, "m", L7, "Con quale legame l'11-cis-retinale è unito all'opsina?", [
  "Una base di Schiff protonata con l'ammino di una lisina",
  "Un legame estere con il carbossile di un aspartato",
  "Un ponte disolfuro con una cisteina dell'elica 7",
  "Un legame tioestere con una cisteina palmitoilata della coda",
  "Un legame glicosidico con lo zucchero N-terminale",
  ], 0,
  "Il gruppo aldeidico del retinale forma una base di Schiff (aldimmina) con il gruppo ε-amminico della Lys296; la base di Schiff è protonata.")

q("u1125-016", C, "m", L7, "Che cosa succede al potenziale di membrana del bastoncello quando arriva la luce?", [
  "Scende verso −75 mV perché i canali cationici si chiudono",
  "Sale verso 0 mV perché i canali cationici si aprono",
  "Scende verso −75 mV perché si aprono i canali del Cl⁻",
  "Resta a −45 mV, ma aumenta il rilascio di neurotrasmettitore",
  "Sale verso +30 mV con un potenziale d'azione completo",
  ], 0,
  "La luce abbassa il cGMP: il cGMP si stacca dai canali cationici, che si chiudono; Na⁺ e Ca²⁺ non entrano più e la membrana si iperpolarizza (circa −75 mV) per circa un secondo.")

q("u1125-017", C, "a", L7, "Dopo l'attivazione da parte della luce, come si riforma la rodopsina?", [
  "Il retinale tutto-trans si stacca e torna 11-cis prima di rilegarsi",
  "Il retinale tutto-trans resta legato e torna 11-cis sul posto",
  "L'opsina viene degradata e risintetizzata con un nuovo retinale",
  "Il retinale viene ossidato ad acido retinoico e poi rilegato",
  "La metarodopsina torna rodopsina per semplice defosforilazione della coda",
  ], 0,
  "La metarodopsina libera opsina (che resta in membrana) e tutto-trans-retinale; questo viene ri-isomerizzato a 11-cis-retinale e si rilega alla Lys296.")

q("u1125-018", C, "l", L7, "Come si chiama l'incapacità di percepire il rosso?", [
  "Protanopia",
  "Deuteranopia",
  "Tritanopia",
  "Acromatopsia",
  "Emeralopia",
  ], 0,
  "Protanopia = rosso, deuteranopia = verde (quella di Dalton), tritanopia = blu.")

q("u1125-019", C, "h", L7, "La lezione dice che i geni di tutti i pigmenti visivi stanno sul cromosoma X. Che cosa è corretto?", [
  "Solo i pigmenti rosso e verde sono sull'X; quello blu è autosomico",
  "Tutti e tre sono sull'X, quindi ogni daltonismo colpisce i maschi",
  "Solo il pigmento blu è sull'X; rosso e verde sono autosomici",
  "Sono tutti autosomici: il daltonismo non è mai legato al sesso",
  "Sono tutti sul cromosoma Y, per questo le donne non si ammalano",
  ], 0,
  "⚠️ Imprecisione della sbobina: i geni dei pigmenti rosso e verde sono sull'X (protanopia e deuteranopia sono recessive legate all'X); il gene del pigmento blu è sul cromosoma 7, quindi la tritanopia non è legata al sesso (Stryer).",
  note="La sbobina di Biologia molecolare (lezione 7) mette sull'X i geni di tutti i pigmenti visivi: vale solo per rosso e verde.")

q("u1125-020", C, "h", L7, "La lezione scrive che il retinale si rilega al «gruppo amminico in epsilon dell'allisina» dell'opsina. Che cosa è corretto?", [
  "Si lega a una lisina: l'allisina ha un'aldeide al posto dell'ammino",
  "Si lega davvero a un'allisina, come nei legami crociati del collagene",
  "Si lega a un'arginina, il cui guanidinio forma la base di Schiff",
  "Si lega a un'istidina, che coordina l'aldeide del retinale",
  "Si lega a una cisteina, con un legame tioemiacetale",
  ], 0,
  "⚠️ Errore nella sbobina: la base di Schiff si forma con il gruppo ε-amminico della Lys296. L'allisina è una lisina il cui ammino è stato ossidato ad aldeide (legami crociati del collagene), quindi non potrebbe formarla.",
  note="La sbobina di Biologia molecolare (lezione 7) scrive «allisina» per la Lys296 dell'opsina.")

q("u1125-021", C, "f", L7, "La lezione scrive che l'immagine «si crea a livello della cornea». Dove si forma davvero?", [
  "Sulla retina, dove stanno coni e bastoncelli",
  "Sul cristallino, che la mette a fuoco sul fondo",
  "Sulla cornea, come scrive la lezione",
  "Sull'iride, che regola la luce entrante",
  "Nel corpo vitreo, prima della retina",
  ], 0,
  "⚠️ Errore nella sbobina: cornea e cristallino focalizzano la luce, ma l'immagine si forma sulla retina, dove i fotorecettori trasducono il segnale.",
  note="La sbobina di Biologia molecolare (lezione 7) dice che l'immagine si crea a livello della cornea.")

# ── Nucleotidi: struttura e nomenclatura (lezione 7) ───────────────────────
C = "bm7-nucleotidi"

q("u1125-022", C, "f", L7, "Che cos'è un nucleoside?", [
  "Una base azotata legata a uno zucchero pentoso, senza fosfato",
  "Una base azotata legata a uno zucchero pentoso e a uno o più fosfati",
  "Uno zucchero pentoso legato a un fosfato, senza la base",
  "Una base azotata libera, non legata ad alcuno zucchero",
  "Un dinucleotide unito da un legame fosfodiestere",
  ], 0,
  "Nucleoside = base + zucchero; aggiungendo il fosfato si ha il nucleotide (es. adenosina → AMP).")

q("u1125-023", C, "f", L7, "Quale base azotata si trova normalmente solo nell'RNA?", [
  "Uracile",
  "Timina",
  "Citosina",
  "Adenina",
  "Guanina",
  ], 0,
  "La citosina è sia nel DNA sia nell'RNA; l'uracile è solo nell'RNA; la timina (uracile con un metile in 5) sta nel DNA.")

q("u1125-024", C, "m", L7, "Come è fatto l'anello delle purine?", [
  "Un anello pirimidinico fuso con un anello imidazolico",
  "Un anello pirimidinico fuso con un anello benzenico aromatico",
  "Due anelli pirimidinici fusi lungo un lato",
  "Un solo anello a sei atomi con due azoti",
  "Un anello imidazolico fuso con un anello furanico",
  ], 0,
  "Le pirimidine hanno un solo anello a 6 atomi con due azoti; le purine hanno un anello a 6 e uno a 5 (imidazolico) fusi.")

q("u1125-025", C, "l", L7, "Quale base è la 2,6-diossipurina?", [
  "Xantina",
  "Ipoxantina",
  "Guanina",
  "Adenina",
  "Acido urico",
  ], 0,
  "Ipoxantina = 6-ossipurina, xantina = 2,6-diossipurina: non sono negli acidi nucleici ma sono intermedi di sintesi e degradazione delle purine. L'acido urico è la 2,6,8-triossipurina.")

q("u1125-026", C, "m", L7, "Quali batteri chiudono il ciclo dell'azoto riportando N₂ nell'atmosfera?", [
  "I denitrificanti, che riducono i nitrati a N₂",
  "I nitrificanti, che ossidano l'ammoniaca a nitriti",
  "I nitratatori, che ossidano i nitriti a nitrati",
  "Gli azotofissatori, che riducono N₂ ad ammoniaca",
  "I degradatori, che liberano ammoniaca dai resti",
  ], 0,
  "Ciclo: fissatori (N₂ → NH₃) → nitrificanti (nitriti) → nitratatori (nitrati, assimilati dalle piante) → … → denitrificanti, che riformano N₂ dai nitrati.")

q("u1125-027", C, "m", L7, "Attraverso quali composti l'ammoniaca entra nei composti organici azotati delle piante?", [
  "Glutammato e glutammina",
  "Aspartato e asparagina, ammidata",
  "Glicina e serina",
  "Urea e ornitina",
  "Alanina e piruvato",
  ], 0,
  "Le piante riducono il nitrato ad ammoniaca, che viene incorporata nei punti di ingresso glutammato e glutammina; glutammato e glutammina sono anche i principali trasportatori di azoto.")

q("u1125-028", C, "l", L7, "In quale RNA si possono trovare timine, secondo la lezione?", [
  "Nel tRNA, nelle regioni ad ansa",
  "Nell'mRNA, nella coda di poli(A)",
  "Nell'rRNA, nel sito peptidiltransferasico",
  "Nei microRNA, nella regione seme",
  "In nessun RNA: la timina è solo nel DNA",
  ], 0,
  "Il tRNA contiene molti nucleotidi modificati e nei loop può presentare timine (es. la ribotimidina dell'ansa TψC; il nome non è nelle sbobine).")

# ── Peptide natriuretico atriale (lezione 6) ───────────────────────────────
C = "bm6-anp"

q("u1125-029", C, "m", L6, "In quale condizione l'atrio secerne l'ANP?", [
  "Quando aumentano volume ematico, pressione o concentrazione dei sali",
  "Quando diminuiscono volume ematico, pressione o concentrazione dei sali",
  "Quando la renina aumenta per un calo della pressione renale",
  "Quando la vasopressina sale per un aumento dell'osmolarità",
  "Quando la frequenza cardiaca scende sotto i valori di riposo",
  ], 0,
  "L'ANP risponde a un eccesso di volume/pressione/sali: fa perdere Na⁺ e acqua, l'opposto di vasopressina e aldosterone.")

q("u1125-030", C, "l", L6, "Che cosa dà all'ANP la sua forma ad anello («a lazo»)?", [
  "Un ponte disolfuro tra due cisteine della sequenza",
  "Un legame isopeptidico tra una lisina e un glutammato",
  "Un legame peptidico tra l'N- e il C-terminale",
  "Uno ione zinco coordinato da quattro cisteine",
  "Un ponte salino tra due arginine e un aspartato",
  ], 0,
  "L'ANP nasce come precursore di 50 amminoacidi e viene tagliato a 28; due cisteine formano un ponte disolfuro che chiude l'anello.")

q("u1125-031", C, "a", L6, "Che cosa distingue la guanilato ciclasi che fa da recettore all'ANP da quella attivata dall'NO?", [
  "Quella dell'ANP è transmembrana; quella dell'NO è intracellulare",
  "Quella dell'ANP è intracellulare; quella dell'NO è transmembrana",
  "Quella dell'ANP produce cAMP; quella dell'NO produce cGMP",
  "Quella dell'ANP è un GPCR; quella dell'NO è un canale ionico",
  "Sono identiche: entrambe sono enzimi di membrana dimerici",
  ], 0,
  "Il recettore dell'ANP è un dimero con un'elica transmembrana, dominio extracellulare di legame e dominio citosolico guanilato ciclasico (come gli RTK); il recettore dell'NO è intracellulare (solubile).")

q("u1125-032", C, "h", L6, "Che cosa ci si aspetta, sulle cellule bersaglio dell'ANP, da un farmaco che rallenta la degradazione del cGMP?", [
  "Un effetto simile all'ANP: più natriuresi, meno renina e aldosterone",
  "Un effetto opposto all'ANP: più riassorbimento di Na⁺ e più renina",
  "Nessun effetto, perché l'ANP agisce attraverso il cAMP e la PKA",
  "Un aumento della vasopressina, perché il cGMP attiva la neuroipofisi",
  "Un blocco del recettore dell'ANP, che viene desensibilizzato dal cGMP",
  ], 0,
  "L'ANP agisce tramite cGMP e PKG: più filtrazione, meno Na⁺ riassorbito, meno renina; il cGMP blocca anche la sintesi di aldosterone. Mantenere alto il cGMP potenzia questi effetti. Lo scenario farmacologico non è nelle sbobine.")

# ── Vasopressina (lezione 6) ───────────────────────────────────────────────
C = "bm6-vasopressina"

q("u1125-033", C, "f", L6, "Da dove viene immessa in circolo la vasopressina?", [
  "Dalla neuroipofisi, dove arriva per via assonale",
  "Dall'adenoipofisi, tramite il sistema portale",
  "Dalla corticale del surrene, insieme all'aldosterone",
  "Dai miociti dell'atrio, come l'ANP",
  "Dal rene, dove viene sintetizzata",
  ], 0,
  "È sintetizzata nei nuclei sopraottico e paraventricolare dell'ipotalamo e trasportata lungo gli assoni alla neuroipofisi, che la libera nel sangue.")

q("u1125-034", C, "h", L6, "La lezione dice che l'acquaporina, fosforilata dalla PKA, «funziona aprendosi». Che cosa è più corretto?", [
  "La fosforilazione fa inserire in membrana le vescicole con acquaporina",
  "La fosforilazione apre un cancello dell'acquaporina già in membrana",
  "La fosforilazione chiude l'acquaporina e fa trattenere l'acqua",
  "La fosforilazione fa endocitare l'acquaporina dalla membrana",
  "La fosforilazione aumenta la trascrizione del gene dell'acquaporina 2",
  ], 0,
  "⚠️ Imprecisione della sbobina: l'acquaporina 2 è un canale sempre aperto; la PKA (ancorata da AKAP) fa fondere le vescicole con la membrana apicale, aumentando il numero di canali e quindi il riassorbimento d'acqua (Lehninger).",
  note="La sbobina di Biologia molecolare (lezione 6) dice che l'acquaporina fosforilata «funziona aprendosi»: in realtà la fosforilazione ne promuove l'inserimento in membrana.")

q("u1125-035", C, "f", L6, "Quale effetto hanno vasopressina e ANP sul volume delle urine?", [
  "La vasopressina lo riduce; l'ANP lo aumenta",
  "La vasopressina lo aumenta; l'ANP lo riduce",
  "Entrambi lo riducono, con meccanismi diversi",
  "Entrambi lo aumentano, ma in tempi diversi",
  "Nessuno dei due: agiscono solo sui vasi",
  ], 0,
  "La vasopressina fa riassorbire acqua (urine scarse e concentrate); l'ANP aumenta filtrazione ed escrezione di Na⁺ e acqua. I fattori natriuretici antagonizzano la vasopressina.")

# ── Sistema renina-angiotensina-aldosterone (lezione 6) ────────────────────
C = "bm6-raa"

q("u1125-036", C, "m", L6, "Come si forma l'angiotensina III?", [
  "Un'aminopeptidasi toglie l'Asp N-terminale dell'angiotensina II",
  "Una carbossipeptidasi toglie la Phe C-terminale dell'angiotensina II",
  "La renina taglia direttamente l'angiotensinogeno in un altro punto",
  "L'ACE toglie un dipeptide dall'angiotensina II",
  "Un'endopeptidasi taglia a metà l'angiotensina I",
  ], 0,
  "L'angiotensina II perde l'aspartato N-terminale per azione di un'aminopeptidasi: si forma l'angiotensina III, anch'essa attiva sulla sintesi di aldosterone.")

q("u1125-037", C, "l", L6, "Quale proteasi della cellula ospite taglia per prima la spike di SARS-CoV-2 in S1 e S2, secondo la lezione?", [
  "La furina",
  "La TMPRSS2",
  "La renina",
  "La catepsina D",
  "L'ACE2",
  ], 0,
  "La furina taglia la spike in S1 (che lega ACE2) e S2 (processata dalla serin-proteasi TMPRSS2, che facilita la fusione).")

q("u1125-038", C, "a", L6, "Perché la forma solubile dell'ACE2, data per infusione, riduce l'infettività di SARS-CoV-2?", [
  "Lega la spike in circolo e la sottrae all'ACE2 di membrana",
  "Taglia la spike in S1 e S2 prima che il virus raggiunga la cellula",
  "Inibisce la TMPRSS2 e impedisce la fusione con la membrana",
  "Blocca la furina e impedisce la maturazione della spike",
  "Produce angiotensina II, che riduce l'espressione dell'ACE2",
  ], 0,
  "Le strategie citate sono anticorpi monoclonali contro ACE2, ACE2 solubile che sequestra il virus e inibitori della TMPRSS2.")

# ── Ormoni idrofobici (lezione 6) ──────────────────────────────────────────
C = "bm6-idrofobici"

q("u1125-039", C, "a", L6, "Nelle cellule steroidogeniche, oltre a indurre la proteina StAR, che cosa fa la PKA attivata dall'ormone tropico?", [
  "Attiva un'idrolasi che libera colesterolo dagli esteri di deposito",
  "Attiva la HMG-CoA reduttasi per sintetizzare colesterolo nuovo nel citosol",
  "Inibisce la desmolasi per accumulare colesterolo nel mitocondrio",
  "Fosforila il recettore steroideo e lo fa entrare nel nucleo",
  "Attiva l'ACAT per esterificare il colesterolo in eccesso",
  ], 0,
  "La PKA fa due cose: induce StAR (ingresso del colesterolo nel mitocondrio, dove la desmolasi P450 lo converte in pregnenolone) e attiva l'idrolasi degli esteri del colesterolo.")

q("u1125-040", C, "h", L6, "Come bloccano i glucocorticoidi l'NF-κB che è già entrato nel nucleo?", [
  "Il recettore con l'ormone si lega all'NF-κB e gli impedisce di trascrivere",
  "Il recettore con l'ormone induce IκBα, che va a prendere NF-κB nel nucleo",
  "L'ormone degrada direttamente la subunità p65 di NF-κB",
  "Il recettore fosforila NF-κB e lo fa uscire dal nucleo verso il citosol, inattivo",
  "L'annessina A1 entra nel nucleo e stacca NF-κB dal DNA",
  ], 0,
  "Due meccanismi: induzione di IκBα (trattiene NF-κB nel citosol, a monte) e, se NF-κB è già nel nucleo, formazione di un complesso recettore-ormone/NF-κB che ne blocca l'attività trascrizionale.")

q("u1125-041", C, "m", L6, "Quale affermazione sui recettori degli ormoni steroidei è corretta?", [
  "Il dominio N-terminale è variabile e attiva la trascrizione",
  "Il dominio N-terminale lega l'ormone, quello C-terminale il DNA",
  "Il dominio centrale lega l'ormone tramite una tasca idrofobica",
  "Il dominio C-terminale riconosce il DNA con dita di zinco",
  "Tutti e tre i domini sono identici tra i diversi recettori",
  ], 0,
  "N-terminale variabile (attivazione della trascrizione), centrale con dita di zinco Cys4 (legame al DNA), C-terminale specifico per l'ormone e sede del legame della Hsp inibitoria.")

# ── Adrenalina e istamina (lezione 6) ──────────────────────────────────────
C = "bm6-adrenalina"

q("u1125-042", C, "m", L6, "Quale coenzima usa la DOPA decarbossilasi che forma la dopamina?", [
  "Piridossal fosfato",
  "Tetraidrobiopterina",
  "Ascorbato e rame",
  "S-adenosilmetionina",
  "Tiamina pirofosfato",
  ], 0,
  "La decarbossilasi degli amminoacidi aromatici è un dimero, ogni monomero lega un PLP (vitamina B6). BH₄ serve alla tirosina idrossilasi, ascorbato/Cu alla dopamina β-idrossilasi, SAM alla PNMT.")

q("u1125-043", C, "l", L6, "Quali antistaminici citati nella lezione sono più affini per il recettore H2?", [
  "Ranitidina e cimetidina",
  "Loratadina e cetirizina",
  "Fexofenadina e loratadina",
  "Tioperamide e JNJ",
  "Cetirizina e cimetidina",
  ], 0,
  "Loratadina, cetirizina, fexofenadina: H1 (allergie). Ranitidina e cimetidina: H2 (iperacidità gastrica). Tioperamide e JNJ: H3/H4.")

q("u1125-044", C, "m", L6, "Perché i β-bloccanti si usano nelle aritmie e nell'angina?", [
  "Sono antagonisti dei recettori β e riducono la forza di contrazione",
  "Sono agonisti dei recettori β e aumentano la portata coronarica",
  "Sono antagonisti dei recettori α e dilatano le arteriole cutanee",
  "Inibiscono la sintesi di adrenalina nella midollare del surrene e nel cuore",
  "Degradano le catecolammine circolanti prima che arrivino al cuore",
  ], 0,
  "Le cellule cardiache hanno recettori β che aumentano frequenza e forza di contrazione; i β-bloccanti (es. practololo) li antagonizzano e riducono il lavoro del cuore.")

q("u1125-045", C, "a", L6, "Perché l'isoproterenolo si può usare come farmaco al posto dell'adrenalina?", [
  "Lega il recettore β con affinità più alta del ligando naturale",
  "Lega il recettore β senza attivarlo, bloccando l'adrenalina",
  "Non lega i recettori ma inibisce la ricaptazione dell'adrenalina",
  "Viene convertito in adrenalina dalla PNMT nelle cellule bersaglio",
  "Attiva direttamente l'adenilato ciclasi senza passare dal recettore",
  ], 0,
  "È un agonista: ha struttura simile all'adrenalina e affinità circa 10 volte maggiore. La lezione dice che ha «due metili sul carbonio primario»: in realtà porta un isopropile sull'azoto (non è nelle sbobine).")
