"""Giro 2026-11-19, blocco 3 – Biochimica I: lipidi e membrane (p. 198–216), vitamine A e D (p. 217–218),
digestione e trasporto dei grassi (p. 219–222)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Acidi grassi e lipidi di riserva (p. 198–201) ──────────────────────────
T = "d10-acidigrassi"
q("u1119-105", T, "f", "198", "Quale proprietà accomuna tutti i lipidi?", [
  "L'insolubilità in acqua",
  "La presenza di glicerolo",
  "La presenza di acidi grassi",
  "La funzione di riserva energetica",
  "La presenza di un gruppo fosfato",
  ], 0,
  "Sono un gruppo eterogeneo: lipidi con acidi grassi (trigliceridi, lipidi di membrana) e colesterolo con i suoi derivati.")
q("u1119-106", T, "f", "199", "Che cosa significa che un acido grasso è saturo?", [
  "Tutti i carboni della coda sono sp³, senza doppi legami",
  "Ha il gruppo carbossilico esterificato con il glicerolo",
  "Ha il numero massimo di doppi legami possibile",
  "È legato all'albumina e non può legarne altri",
  "Ha una catena di almeno 24 atomi di carbonio",
  ], 0,
  "I carboni sono al massimo stato di riduzione. L'acido stearico (18:0) fonde a circa 70 °C: i grassi saturi a temperatura ambiente sono solidi.")
q("u1119-107", T, "m", "201", "Da che cosa dipende il punto di fusione di un acido grasso?", [
  "Sale con la lunghezza della catena e scende con il numero di doppi legami",
  "Scende con la lunghezza della catena e sale con il numero di doppi legami",
  "Dipende solo dalla carica del gruppo carbossilico al pH della cellula",
  "Sale sia con la lunghezza della catena sia con il numero di doppi legami",
  "Dipende solo dalla lunghezza della catena e non dai doppi legami",
  ], 0,
  "Grado di saturazione e lunghezza della catena dettano il punto di fusione: più la molecola è satura e lunga, più è alto.")
q("u1119-108", T, "a", "201", "Perché un doppio legame cis abbassa il punto di fusione di un acido grasso?", [
  "Piega la catena e impedisce alle molecole di impacchettarsi in modo compatto",
  "Rende la catena più polare, quindi più solubile e meno compatta in acqua",
  "Aumenta la carica negativa della testa e fa respingere le molecole tra loro",
  "Mantiene la catena lineare ma più corta, quindi con meno interazioni",
  "Forma legami a idrogeno con le catene vicine, che sono più deboli",
  ], 0,
  "Un doppio legame trans lascia la catena quasi lineare. La piega dei cis dà fluidità alle membrane.",
  note="Sbobina di Biochimica I, p. 201: dice che il doppio legame cis crea una piega «di circa 109°». La deviazione della catena è di circa 30°.")
q("u1119-109", T, "f", "200", "Dove si trova di solito il primo doppio legame di un acido grasso insaturo?", [
  "Tra il C9 e il C10",
  "Tra il C2 e il C3",
  "Tra il C5 e il C6",
  "Tra il C12 e il C13",
  "Sul carbonio ω",
  ], 0,
  "La numerazione parte dal carbonio carbossilico (C1). L'eccezione più nota è l'acido arachidonico.")
q("u1119-110", T, "l", "201", "Quale acido grasso ha il primo doppio legame sul C5 invece che sul C9?", [
  "Acido arachidonico",
  "Acido oleico",
  "Acido linoleico",
  "Acido palmitoleico",
  "Acido α-linolenico",
  ], 0,
  "L'acido arachidonico (20:4) ha i doppi legami in 5, 8, 11 e 14.")
q("u1119-111", T, "f", "199", "Con quale lettera si indica l'ultimo carbonio della catena di un acido grasso, il più lontano dal carbossile?", [
  "ω (omega)",
  "α (alfa)",
  "β (beta)",
  "Δ (delta)",
  "γ (gamma)",
  ], 0,
  "Da qui la classificazione ω-3 e ω-6, in base alla distanza del doppio legame dal carbonio ω.")
q("u1119-112", T, "m", "201", "Perché i trigliceridi sono detti «grassi neutri»?", [
  "Gli OH del glicerolo e i carbossili degli acidi grassi sono impegnati in esteri: non restano cariche",
  "Contengono un gruppo fosfato neutralizzato da una colina, che bilancia esattamente la sua carica negativa",
  "Hanno solo acidi grassi saturi, che non hanno cariche, al contrario degli acidi insaturi",
  "Viaggiano sempre legati all'albumina, che ne neutralizza la carica nel plasma",
  "Il glicerolo porta una carica positiva che bilancia quella dell'unico acido grasso",
  ], 0,
  "Il glicerolo è esterificato con tre acidi grassi, uguali (trigliceridi semplici) o diversi (misti).",
  note="Sbobina di Biochimica I, p. 201: scrive «glicerolo triacetilato». Il glicerolo è triacilato (esterificato con tre acidi grassi), non legato a gruppi acetile.")

# ── Lipidi di membrana, terpeni e steroidi (p. 202–208) ────────────────────
T = "d10-membrana"
q("u1119-113", T, "f", "202", "Qual è il glicerofosfolipide più semplice, da cui derivano tutti gli altri?", [
  "Acido fosfatidico",
  "Fosfatidilcolina",
  "Diacilglicerolo",
  "Cardiolipina",
  "Sfingomielina",
  ], 0,
  "Glicerolo + due acidi grassi esterificati + fosfato sul C3. Aggiungendo un alcol al fosfato (colina, etanolammina, serina, inositolo) si hanno gli altri.")
q("u1119-114", T, "l", "202", "Quale abbinamento tra nome tradizionale e glicerofosfolipide è corretto?", [
  "Lecitine = fosfatidilcoline; cefaline = fosfatidiletanolammina e fosfatidilserina",
  "Lecitine = fosfatidiletanolammine; cefaline = fosfatidilcolina e fosfatidilserina",
  "Lecitine = fosfatidilserine; cefaline = fosfatidilcolina e fosfatidilinositolo",
  "Lecitine = sfingomieline; cefaline = fosfatidilcolina e fosfatidiletanolammina",
  "Lecitine = cardiolipine; cefaline = fosfatidilglicerolo e fosfatidilinositolo",
  ], 0,
  "La lecitina è anche il donatore dell'acile per l'esterificazione del colesterolo nelle lipoproteine.")
q("u1119-115", T, "a", "203", "Che cosa distingue il PAF (fattore di attivazione delle piastrine) da un comune glicerofosfolipide?", [
  "Sul C1 ha un alcol a lunga catena legato con un legame etere e sul C2 un acetile",
  "Sul C1 ha un acetile legato con un estere e sul C2 un alcol a lunga catena con un etere",
  "Non ha il gruppo fosfato e porta la colina legata direttamente al C3 del glicerolo",
  "Ha la sfingosina al posto del glicerolo e un acido grasso legato con un legame ammidico",
  "Ha due gruppi fosfato e due colina, uno su C1 e uno su C3, e un acido grasso sul C2",
  ], 0,
  "È un lipide etere con fosfocolina sul C3.")
q("u1119-116", T, "m", "203", "Quale di queste NON è un'azione del PAF?", [
  "Inibisce l'aggregazione delle piastrine",
  "Stimola il rilascio di serotonina",
  "Media l'infiammazione",
  "Viene rilasciato dai basofili dopo stimolazione antigenica",
  "Favorisce l'impianto dell'uovo fecondato",
  ], 0,
  "Il PAF stimola, non inibisce, l'aggregazione piastrinica.")
q("u1119-117", T, "f", "203", "Quale molecola prende il posto del glicerolo negli sfingolipidi?", [
  "La sfingosina, un amminoalcol a lunga catena",
  "Il colesterolo, uno steroide con un ossidrile",
  "L'inositolo, un polialcol ciclico",
  "La ceramide, un acido grasso con due ammine",
  "Il dolicolo, un lipide isoprenico",
  ], 0,
  "La sfingosina ha 18 C, un doppio legame trans e i primi 3 C con gruppi funzionali simili al glicerolo, con un gruppo amminico al posto di un OH. La ceramide è la sfingosina con un acido grasso.")
q("u1119-118", T, "m", "203", "Che cos'è la ceramide?", [
  "Sfingosina con un acido grasso legato con un legame ammidico al gruppo amminico",
  "Sfingosina con un acido grasso legato con un legame estere all'ossidrile del C1",
  "Glicerolo con un acido grasso sul C1 e un alcol a lunga catena legato sul C2",
  "Sfingosina con una fosfocolina legata con un legame fosfoestere al C1",
  "Sfingosina con uno zucchero legato con un legame glicosidico all'azoto",
  ], 0,
  "È la base di tutti gli sfingolipidi: l'OH del C1 resta libero per legare fosfocolina o zuccheri.")
q("u1119-119", T, "a", "203", "Che cosa si lega all'OH del C1 della ceramide per formare la sfingomielina e un glicosfingolipide?", [
  "Fosfocolina per la sfingomielina; uno zucchero, con legame glicosidico, per il glicosfingolipide",
  "Uno zucchero per la sfingomielina; una fosfocolina, con legame fosfoestere, per il glicosfingolipide",
  "Un secondo acido grasso per la sfingomielina; un fosfato, con legame fosfoestere, per il glicosfingolipide",
  "Fosfoserina per la sfingomielina; un acido sialico, con legame ammidico, per il glicosfingolipide",
  "Glicerolo 3-fosfato per la sfingomielina; il colesterolo, con legame estere, per il glicosfingolipide",
  ], 0,
  "La sfingomielina è lo sfingofosfolipide più noto; con più zuccheri e acido sialico si hanno i gangliosidi.",
  note="Sbobina di Biochimica I, p. 203: chiama «glicerosfingolipide» la ceramide legata a uno zucchero. Il termine è glicosfingolipide: negli sfingolipidi il glicerolo non c'è.")
q("u1119-120", T, "m", "204", "Che cosa caratterizza i gangliosidi?", [
  "Sono glicosfingolipidi con un oligosaccaride carico negativamente, abbondanti nella sostanza grigia",
  "Sono glicerofosfolipidi con un etere sul C1, abbondanti nella membrana mitocondriale interna",
  "Sono sfingofosfolipidi con la fosfocolina, abbondanti nella guaina mielinica dei nervi periferici",
  "Sono esteri del colesterolo con un acido grasso, abbondanti nelle placche ateromatose",
  "Sono glicoproteine con molto acido sialico, abbondanti nel plasma e rimosse dal fegato",
  ], 0,
  "La carica negativa viene dall'acido sialico dell'oligosaccaride. I gangliosidi della sostanza grigia fanno parte di siti recettoriali (neurotrasmettitori, ormoni, tossine batteriche).")
q("u1119-121", T, "m", "205", "Che cosa determina gli antigeni dei gruppi sanguigni sulla superficie dei globuli rossi?", [
  "La parte oligosaccaridica di glicolipidi, legata a una ceramide",
  "La sequenza amminoacidica di una proteina integrale di membrana",
  "Il tipo di acido grasso presente nella fosfatidilcolina",
  "La quantità di colesterolo nel foglietto esterno della membrana",
  "La fosfatidilserina esposta sul foglietto esterno della membrana",
  ], 0,
  "È la componente glucidica a conferire le proprietà antigeniche.")
q("u1119-122", T, "l", "206", "Quale fosfolipasi stacca la testa polare ma lascia il fosfato sul lipide, producendo acido fosfatidico?", [
  "Fosfolipasi D",
  "Fosfolipasi C",
  "Fosfolipasi A2",
  "Fosfolipasi A1",
  "Sfingomielinasi",
  ], 0,
  "La C stacca la testa polare insieme al fosfato (es. IP₃ dal PIP₂, lasciando il DAG); la A2 stacca l'acido grasso in posizione 2.")
q("u1119-123", T, "m", "207", "Quale di queste molecole NON deriva da unità isopreniche?", [
  "Acido palmitico",
  "Coenzima Q",
  "Vitamina K",
  "Vitamina E",
  "Squalene",
  ], 0,
  "L'isoprene ha 5 C e due doppi legami. I terpeni comprendono le vitamine A, E, K, il coenzima Q e lo squalene, da cui deriva il colesterolo.")
q("u1119-124", T, "l", "207", "Quanti atomi di carbonio ha il colesterolo e come si chiama il suo sistema di quattro anelli?", [
  "27; ciclopentanoperidrofenantrene",
  "30; ciclopentanoperidrofenantrene",
  "27; tetraidronaftalene",
  "24; ciclopentanoperidrofenantrene",
  "18; isoallosazina",
  ], 0,
  "Lo squalene e il lanosterolo hanno 30 C; gli acidi biliari 24.")
q("u1119-125", T, "m", "207", "Perché il colesterolo è una molecola anfipatica?", [
  "Ha un solo gruppo polare, l'OH in C3, mentre anelli e catena laterale sono idrofobici",
  "Ha un gruppo fosfato sulla catena laterale, mentre i quattro anelli sono idrofobici",
  "Ha due gruppi carbossilici agli estremi della molecola, separati dagli anelli idrofobici",
  "È legato a una colina sul C3, che forma una testa polare come nei fosfolipidi",
  "Ha una catena laterale polare con molti ossidrili, mentre gli anelli sono idrofobici",
  ], 0,
  "Nella membrana l'OH sta verso le teste polari dei fosfolipidi. Gli esteri del colesterolo, senza OH libero, sono completamente insolubili.")
q("u1119-126", T, "f", "210", "Quale lipide è il principale regolatore della fluidità delle membrane animali?", [
  "Colesterolo",
  "Sfingomielina",
  "Fosfatidilinositolo",
  "Cardiolipina",
  "Triacilglicerolo",
  ], 0,
  "Il colesterolo si dispone in entrambi i foglietti.")

# ── Membrane e trasporto (p. 208–216) ──────────────────────────────────────
T = "d10-trasporto"
q("u1119-127", T, "f", "208", "In quale foglietto della membrana plasmatica si trova soprattutto il fosfatidilinositolo?", [
  "Nel foglietto interno, verso il citosol",
  "Nel foglietto esterno, verso il lato extracellulare",
  "In egual misura nei due foglietti",
  "Solo nei raft del foglietto esterno",
  "Nel nucleo idrofobico tra i due foglietti",
  ], 0,
  "La distribuzione dei lipidi tra i due foglietti non è casuale: il PI e i suoi derivati servono alla segnalazione intracellulare.")
q("u1119-128", T, "a", "210", "Perché l'asimmetria tra i due foglietti della membrana può durare a lungo?", [
  "Il flip-flop spontaneo di un fosfolipide è lentissimo rispetto alla diffusione laterale e avviene soprattutto grazie alle flippasi",
  "Il flip-flop è impossibile per qualunque lipide, perché la testa polare non può mai attraversare il nucleo idrofobico",
  "I fosfolipidi non si muovono affatto nel piano della membrana, perché sono legati stabilmente alle proteine del citoscheletro",
  "Il colesterolo forma legami covalenti con i fosfolipidi di ciascun foglietto e li blocca per sempre nella loro posizione iniziale",
  "La diffusione laterale è più lenta del flip-flop, ma le flippasi riportano subito ogni lipide al suo foglietto",
  ], 0,
  "Il flip-flop richiede ore; la diffusione laterale è molto rapida. Anche le proteine diffondono lateralmente, se non sono vincolate.",
  note="Sbobina di Biochimica I, p. 210: indica per la diffusione laterale una velocità di «1 mm/s». L'ordine di grandezza corretto è circa 1 µm/s.")
q("u1119-129", T, "m", "210", "Come si ancorano alla membrana le proteine lipidate?", [
  "Con un lipide (acido grasso o unità isoprenica) legato covalentemente alla proteina",
  "Con una lunga α-elica idrofobica che attraversa più volte tutto il doppio strato",
  "Con legami ionici tra residui di lisina e l'ossidrile del colesterolo della membrana",
  "Con un ponte disolfuro tra una cisteina e la testa della fosfatidilserina",
  "Con un oligosaccaride che si inserisce tra le code dei fosfolipidi",
  ], 0,
  "L'ancora lipidica si inserisce nel doppio strato; queste proteine si concentrano spesso nei raft, coinvolti nella segnalazione.",
  note="Sbobina di Biochimica I, p. 210: dice che il lipide si lega alla proteina sempre con un legame estere. Dipende dall'ancora: tioestere per il palmitoile, ammide per il miristoile, tioetere per i gruppi isoprenici (Lehninger).")
q("u1119-130", T, "m", "211", "Che cosa permette a una proteina integrale di stare stabilmente nel doppio strato?", [
  "Le sue eliche o i suoi filamenti β espongono ai lipidi un lato almeno in parte idrofobico",
  "È legata covalentemente alle teste polari dei fosfolipidi di entrambi i foglietti",
  "Ha molti residui carichi che interagiscono direttamente con le code idrocarburiche dei lipidi",
  "È stabilizzata da ponti disolfuro con il colesterolo del foglietto interno",
  "Si lega alle code dei fosfolipidi tramite un oligosaccaride idrofobico esterno",
  ], 0,
  "Gli elementi di struttura secondaria nella membrana devono essere in parte anfipatici.")
q("u1119-131", T, "f", "211", "A quali sostanze il doppio strato lipidico è intrinsecamente impermeabile?", [
  "Agli ioni e alle molecole polari",
  "Ai gas apolari come O₂ e CO₂",
  "Agli steroidi e alle molecole idrofobiche",
  "Alle piccole molecole apolari",
  "Ai lipidi e alle vitamine liposolubili",
  ], 0,
  "Per questo il loro trasporto è mediato da proteine, secondo o contro gradiente.")
q("u1119-132", T, "f", "212", "Che differenza c'è tra simporto e antiporto?", [
  "Nel simporto due molecole vanno nella stessa direzione, nell'antiporto in direzioni opposte",
  "Nel simporto una sola molecola attraversa la membrana, nell'antiporto due insieme",
  "Il simporto è sempre passivo, mentre l'antiporto usa sempre direttamente l'idrolisi dell'ATP",
  "Nel simporto le molecole vanno in direzioni opposte, nell'antiporto nella stessa",
  "Il simporto riguarda solo ioni, l'antiporto solo molecole organiche come il glucosio",
  ], 0,
  "Sono due forme di cotrasporto; l'uniporto trasporta una sola molecola.")
q("u1119-133", T, "l", "213", "Che cosa indica la «P» delle ATPasi di tipo P, come la pompa Na⁺/K⁺?", [
  "Che si fosforilano durante il ciclo di trasporto",
  "Che si trovano solo sulla membrana plasmatica",
  "Che trasportano solo protoni",
  "Che sono formate da quattro subunità a forma di poro",
  "Che usano il pirofosfato al posto dell'ATP",
  ], 0,
  "Il fosfato dell'ATP si lega temporaneamente alla pompa (un aspartato) e la fosforilazione ne cambia la conformazione. Le V sono vacuolari, le F sono i fattori di accoppiamento come l'ATP sintasi.",
  note="Sbobina di Biochimica I, p. 213: spiega la P come «plasmatiche, costituite da 4 subunità». La P sta per fosforilazione: si trovano anche in membrane interne (es. pompa del calcio del reticolo).")
q("u1119-134", T, "a", "213", "Che effetto ha la pompa Na⁺/K⁺ sul potenziale di membrana, a ogni ciclo?", [
  "Esporta 3 Na⁺ e importa 2 K⁺: esce una carica positiva netta e l'interno resta negativo",
  "Esporta 2 Na⁺ e importa 3 K⁺: entra una carica positiva netta e l'interno diventa positivo",
  "Importa 3 Na⁺ ed esporta 2 K⁺: entra una carica positiva netta e l'interno diventa positivo",
  "Esporta 1 Na⁺ e importa 1 K⁺: lo scambio è elettroneutro e non influenza il potenziale",
  "Esporta 3 K⁺ e importa 2 Na⁺: esce una carica positiva netta e l'interno resta negativo",
  ], 0,
  "Ogni ciclo idrolizza un ATP; la defosforilazione chiude il ciclo e riporta la pompa alla conformazione iniziale.")
q("u1119-135", T, "a", "214", "Come distingui sperimentalmente la diffusione facilitata dalla diffusione semplice?", [
  "La velocità della facilitata raggiunge un massimo (saturazione), quella della semplice cresce in proporzione alla concentrazione",
  "La velocità della semplice raggiunge un massimo (saturazione), quella della facilitata cresce in proporzione alla concentrazione",
  "La facilitata consuma ATP e si blocca con gli inibitori della glicolisi, la semplice non consuma energia",
  "La facilitata avviene contro gradiente, la semplice solo secondo gradiente di concentrazione",
  "La facilitata riguarda solo gli ioni, la semplice solo le molecole organiche come il glucosio",
  ], 0,
  "Il trasportatore si comporta come un enzima: quando è tutto occupato, la velocità non può crescere oltre.")
q("u1119-136", T, "l", "214", "Quanti amminoacidi servono, almeno, perché un'α-elica attraversi tutto il doppio strato?", [
  "Circa 20 (5–6 giri d'elica)",
  "Circa 7 (2 giri d'elica)",
  "Circa 50 (14 giri d'elica)",
  "Circa 100 (28 giri d'elica)",
  "Circa 3 (un solo giro d'elica)",
  ], 0,
  "La sbobina dice almeno 21 aa. I GLUT hanno 12 eliche transmembrana.")
q("u1119-137", T, "a", "214", "Perché il GLUT1 si considera un trasportatore e non un canale?", [
  "Lega il glucosio e cambia conformazione per spostarlo, quindi mostra una velocità massima di saturazione",
  "Usa l'ATP per spostare il glucosio contro gradiente, mentre un canale lavora solo secondo gradiente",
  "Trasporta il glucosio in simporto con il Na⁺, mentre un canale trasporta una sola specie alla volta",
  "Resta sempre aperto, mentre un canale si apre solo in risposta a un ligando o al voltaggio",
  "Lascia passare ioni e glucosio insieme, mentre un canale è sempre selettivo per un solo tipo di ione",
  ], 0,
  "Il GLUT1 fa diffusione facilitata (secondo gradiente) con cinetica di saturazione; nei globuli rossi il glucosio entra solo così. Un canale lascia fluire rapidamente gli ioni attraverso un poro.",
  note="Sbobina di Biochimica I, p. 214: scrive che il GLUT1 trasporta il glucosio secondo gradiente «in quanto canale». I GLUT sono trasportatori (carrier), non canali, anche se lavorano secondo gradiente.")
q("u1119-138", T, "m", "215", "Quale di queste NON è una caratteristica dei canali ionici?", [
  "Usano ATP per spostare gli ioni contro gradiente",
  "Sono molto selettivi per particolari ioni",
  "Esistono in uno stato aperto e in uno chiuso",
  "Tornano spontaneamente allo stato chiuso",
  "Si aprono per un ligando o per il voltaggio",
  ], 0,
  "I canali permettono la libera diffusione secondo gradiente; contro gradiente lavorano le pompe.")
q("u1119-139", T, "h", "216", "Che cosa succede nel poro del recettore nicotinico quando lega l'acetilcolina?", [
  "Le eliche M2 ruotano: le leucine che occludevano il poro si spostano e verso il canale si affacciano residui polari",
  "Le eliche M2 si allungano: i residui polari che occludevano il poro escono e verso il canale si affacciano residui di leucina",
  "Le due subunità α si staccano dal pentamero e lasciano un foro centrale tra le subunità β, γ e δ restanti",
  "Il recettore si fosforila sulle leucine delle eliche M2, che diventano cariche e respingono le altre",
  "L'acetilcolina entra nel poro e si lega alle leucine, trascinando con sé gli ioni sodio nella cellula",
  ], 0,
  "Il cambiamento conformazionale si trasmette a tutte e 5 le subunità (α₂βγδ, ognuna con 4 eliche): le leucine vanno a contatto con le subunità adiacenti.")

# ── Vitamine A e D (p. 217–218) ────────────────────────────────────────────
T = "d11-vitad"
q("u1119-140", T, "l", "217", "Come si passa dal β-carotene al retinolo?", [
  "Una diossigenasi lo taglia in due molecole di retinale, ridotte poi a retinolo con NADPH",
  "Una idrolasi lo taglia in due molecole di acido retinoico, ridotte poi a retinolo con il NADH",
  "Una monoossigenasi P450 lo ossida a retinolo in un solo passaggio, senza intermedi",
  "Una diossigenasi lo taglia in due molecole di retinolo, ossidate poi a retinale con NAD⁺",
  "Una reduttasi lo riduce a retinale con NADPH, poi una diossigenasi lo taglia a metà",
  ], 0,
  "Il retinale ha un gruppo aldeidico; viene assorbito e conservato come estere del retinolo (es. con l'acido palmitico).")
q("u1119-141", T, "f", "217", "Perché le vitamine liposolubili, a differenza delle idrosolubili, possono essere accumulate?", [
  "Possono essere depositate nei tessuti, ad esempio il retinolo nel fegato",
  "Vengono eliminate più rapidamente con le urine e servono dosi maggiori",
  "Si legano all'emoglobina e restano nei globuli rossi per tutta la loro vita",
  "Sono sintetizzate dall'organismo e quindi non devono essere introdotte",
  "Non hanno bisogno di essere attivate e quindi restano sempre in circolo",
  ], 0,
  "Il retinolo viene portato nei siti di deposito del fegato.")
q("u1119-142", T, "f", "217", "Quale proteina trasporta il retinolo nel sangue verso i tessuti?", [
  "La retinol binding protein",
  "La transferrina plasmatica",
  "La ceruloplasmina",
  "La ferritina",
  "L'emopessina",
  ], 0,
  "È specifica per il retinolo.")
q("u1119-143", T, "l", "218", "Come si chiamano le vitamine D3 e D2?", [
  "D3 colecalciferolo, D2 ergocalciferolo",
  "D3 ergocalciferolo, D2 colecalciferolo",
  "D3 calcitriolo, D2 calcidiolo",
  "D3 calcidiolo, D2 calcitriolo",
  "D3 colecalciferolo, D2 calcitriolo",
  ], 0,
  "La D3 deriva dal colesterolo (7-deidrocolesterolo). Il calcidiolo (25-OH) e il calcitriolo (1,25-(OH)₂) sono le forme idrossilate.")

# ── Digestione, trasporto dei grassi e lipoproteine (p. 219–222) ───────────
T = "d12-digestione"
q("u1119-144", T, "f", "219", "Come vengono trasportati nel sangue gli acidi grassi liberati dal tessuto adiposo?", [
  "Legati all'albumina",
  "Dentro i chilomicroni",
  "Legati all'emoglobina",
  "Liberi, disciolti nel plasma",
  "Dentro le HDL",
  ], 0,
  "I chilomicroni (di origine intestinale) portano i grassi della dieta, le VLDL (epatiche) quelli sintetizzati dal fegato.")

T = "d12-lipoproteine"
q("u1119-145", T, "a", "221", "Come è organizzata una lipoproteina?", [
  "Un monostrato di fosfolipidi con le teste verso l'esterno e le apoproteine inserite; dentro trigliceridi ed esteri del colesterolo",
  "Un doppio strato di fosfolipidi come una membrana, con le apoproteine nel lume acquoso interno e il colesterolo libero nel centro",
  "Un nucleo di fosfolipidi e colesterolo libero circondato da uno strato di trigliceridi e da apoproteine globulari",
  "Un monostrato di trigliceridi con le code verso l'esterno; dentro le apoproteine e i fosfolipidi a contatto con l'acqua",
  "Un aggregato di apoproteine che legano singole molecole di colesterolo libero, senza nessuno strato di fosfolipidi",
  ], 0,
  "Le apoproteine abbracciano il nucleo lipidico grazie alle loro eliche anfipatiche.")
q("u1119-146", T, "f", "220", "Quale serie di lipoproteine è ordinata per densità crescente?", [
  "Chilomicroni < VLDL < LDL < HDL",
  "HDL < LDL < VLDL < chilomicroni",
  "VLDL < chilomicroni < HDL < LDL",
  "LDL < VLDL < HDL < chilomicroni",
  "Chilomicroni < LDL < VLDL < HDL",
  ], 0,
  "Più lipidi e meno proteine, densità più bassa: i chilomicroni sono le meno dense, le HDL le più dense (alto contenuto proteico).")

# ── Domande Hard di integrazione (p. 166–216) ──────────────────────────────
q("u1119-147", "d9-mono", "h", "186", "Le urine di un bambino danno la reazione di Fehling positiva, ma la striscia alla glucosio ossidasi è negativa. Come interpreti il risultato?", [
  "C'è uno zucchero riducente diverso dal glucosio (es. galattosio), che la glucosio ossidasi non riconosce",
  "C'è glucosio in piccola quantità, che la glucosio ossidasi non rileva ma il reattivo di Fehling sì",
  "C'è saccarosio, che riduce il rame della reazione di Fehling ma non viene ossidato dall'enzima",
  "C'è un eccesso di perossidasi nelle urine, che consuma l'acqua ossigenata prodotta dalla glucosio ossidasi",
  "C'è acido glucuronico, che riduce il rame e inibisce in modo competitivo la glucosio ossidasi",
  ], 0,
  "Fehling rileva qualsiasi zucchero con il carbonio anomerico libero; la glucosio ossidasi è specifica per il glucosio. La specificità dell'enzima e l'esempio clinico (galattosemia) non sono nelle sbobine.")
q("u1119-148", "d9-glicosidico", "h", "190", "Una molecola di glicogeno ha 50 punti di ramificazione. Quante estremità riducenti e non riducenti ha?", [
  "1 riducente e 51 non riducenti",
  "51 riducenti e 1 non riducente",
  "1 riducente e 50 non riducenti",
  "50 riducenti e 50 non riducenti",
  "2 riducenti e 50 non riducenti",
  ], 0,
  "Una catena lineare ha un'estremità riducente e una non riducente; ogni ramificazione aggiunge un'estremità non riducente. L'estremità riducente resta una sola, ed è l'unica su cui gli enzimi non agiscono.")
q("u1119-149", "d7-coenzimi", "h", "167", "Un paziente ha omocisteina plasmatica alta e acido metilmalonico nelle urine. Quale carenza è più probabile?", [
  "Vitamina B12, che serve sia alla metionina sintasi sia alla metilmalonil-CoA mutasi",
  "Acido folico, che serve sia alla metionina sintasi sia alla metilmalonil-CoA mutasi",
  "Vitamina B6, che serve alla cistationina sintasi e alla propionil-CoA carbossilasi",
  "Biotina, che serve alla propionil-CoA carbossilasi e alla rimetilazione dell'omocisteina",
  "Tiamina, che serve alla decarbossilazione del metilmalonil-CoA e al ciclo della metionina",
  ], 0,
  "Le due reazioni B12-dipendenti sono proprio queste. La carenza di folato alza l'omocisteina ma non l'acido metilmalonico.")
q("u1119-150", "d8-vitk", "h", "180", "Perché ai neonati si somministra vitamina K alla nascita?", [
  "L'intestino non è ancora colonizzato dai batteri che producono menachinone e le riserve sono scarse",
  "Il fegato del neonato non produce ancora fibrinogeno e la vitamina K ne stimola la sintesi epatica",
  "Le piastrine del neonato non producono trombossano senza vitamina K e non aggregano",
  "Il neonato ha troppa plasmina e la vitamina K serve a inibirla finché il fegato matura",
  "Il neonato non produce fattore di von Willebrand e la vitamina K ne aumenta il rilascio",
  ], 0,
  "Senza vitamina K i fattori II, VII, IX e X escono dal fegato senza Gla. La profilassi neonatale non è nelle sbobine; la sbobina dice che la K2 è prodotta dai batteri nel colon.")
q("u1119-151", "d8-fibrinolisi", "h", "181", "Perché l'eparina agisce in pochi minuti, mentre l'effetto del warfarin compare solo dopo alcuni giorni?", [
  "L'eparina potenzia subito l'antitrombina; il warfarin blocca solo i fattori nuovi e quelli già carbossilati restano attivi",
  "L'eparina inibisce subito la vitamina K epossido reduttasi; il warfarin deve prima essere attivato nel rene e nel fegato",
  "L'eparina degrada subito la fibrina; il warfarin deve prima accumularsi nelle piastrine per bloccare la COX",
  "L'eparina blocca subito la γ-carbossilasi; il warfarin agisce solo dopo aver inattivato tutta la protrombina",
  "L'eparina chela subito il calcio del plasma; il warfarin agisce solo quando la vitamina K della dieta si esaurisce",
  ], 0,
  "Il warfarin agisce sulla sintesi (rigenerazione dell'idrochinone), quindi bisogna aspettare che i fattori già in circolo vengano eliminati. Il confronto dei tempi non è nelle sbobine.")
q("u1119-152", "d10-acidigrassi", "h", "201", "Confronta l'acido oleico (18:1 cis) e il suo isomero elaidico (18:1 trans). Quale ha il punto di fusione più alto e perché?", [
  "L'elaidico: la catena trans resta quasi lineare e si impacchetta come quella di un acido saturo",
  "L'oleico: la piega del doppio legame cis permette alle catene di incastrarsi più strettamente",
  "Sono uguali: hanno lo stesso numero di carboni e lo stesso numero di doppi legami",
  "L'oleico: il doppio legame cis rende la catena più polare e aumenta i legami a idrogeno",
  "L'elaidico: il doppio legame trans rende la testa carbossilica più carica e più attratta",
  ], 0,
  "Non conta solo il numero di doppi legami ma anche la loro geometria: i grassi trans si comportano in parte come i saturi. Il nome acido elaidico non è nelle sbobine.")
q("u1119-153", "d10-trasporto", "h", "214", "Misuri l'ingresso del glucosio nei globuli rossi a concentrazioni crescenti: la velocità si appiattisce oltre una certa concentrazione. Un analogo del glucosio sposta la curva verso destra senza cambiare il valore massimo. Che cosa concludi?", [
  "Il trasporto è mediato da un trasportatore saturabile e l'analogo compete con il glucosio per il sito di legame",
  "Il trasporto è una diffusione semplice e l'analogo riduce la permeabilità della membrana ai soluti polari",
  "Il trasporto è mediato da un trasportatore e l'analogo lo inibisce in modo non competitivo legando un altro sito",
  "Il trasporto è attivo primario e l'analogo riduce l'ATP disponibile per la pompa del glucosio",
  "Il trasporto avviene tramite un canale e l'analogo ne chiude il poro solo alle basse concentrazioni",
  ], 0,
  "Saturazione = trasportatore (diffusione facilitata, GLUT1). Spostamento a destra con lo stesso massimo = come un inibitore competitivo: aumenta la costante apparente, non la velocità massima.")
q("u1119-154", "d10-membrana", "h", "206", "Il veleno di alcuni serpenti contiene una fosfolipasi A2 secretoria. Che cosa produce dalla fosfatidilcolina delle membrane dei globuli rossi?", [
  "Un acido grasso e una lisofosfatidilcolina, che agisce da detergente e danneggia la membrana",
  "Un diacilglicerolo e la fosfocolina, che attiva la protein chinasi C e fa aggregare i globuli rossi",
  "Acido fosfatidico e colina libera, che aumenta l'acetilcolina e blocca la contrazione muscolare",
  "Glicerolo 3-fosfato e due acidi grassi, che vengono ossidati subito nei globuli rossi",
  "Una ceramide e la fosfocolina, che si accumulano nella membrana e la rendono rigida",
  ], 0,
  "La PLA2 stacca solo l'acido grasso in posizione 2; resta un fosfolipide con una sola coda (liso-), che destabilizza il doppio strato. Il nome lisofosfatidilcolina e l'effetto emolitico non sono nelle sbobine.")
q("u1119-155", "d9-poli", "h", "195", "Perché il lisozima e la penicillina agiscono meglio sui batteri Gram-positivi che sui Gram-negativi?", [
  "Nei Gram+ il peptidoglicano è spesso ed esterno; nei Gram− è sottile e protetto dalla membrana esterna",
  "Nei Gram+ il peptidoglicano contiene D-amminoacidi; nei Gram− contiene solo L-amminoacidi",
  "Nei Gram− il peptidoglicano non ha NAM, quindi lisozima e penicillina non trovano il loro bersaglio",
  "Nei Gram− il legame crociato è un ponte di pentaglicina, che la transpeptidasi non riconosce",
  "Nei Gram+ manca la transpeptidasi, quindi la parete si forma solo per via spontanea e fragile",
  ], 0,
  "Nei Gram− il peptidoglicano sta nello spazio periplasmatico, tra membrana interna ed esterna. L'effetto della membrana esterna sull'accesso dei farmaci non è nelle sbobine.")
q("u1119-156", "d10-membrana", "h", "203", "Sfingomielina e fosfatidilcolina hanno scheletri diversi ma si comportano in modo simile nella membrana. Perché?", [
  "Entrambe hanno la fosfocolina come testa polare e due code idrofobiche",
  "Entrambe hanno il glicerolo come scheletro e due acidi grassi legati con legame estere, ma teste polari diverse",
  "Entrambe sono prive di testa polare e si dispongono nel nucleo idrofobico della membrana, come il colesterolo",
  "Entrambe hanno uno zucchero come testa polare e una sola coda idrofobica, legata con legame ammidico",
  "Entrambe hanno una coda sola e un gruppo fosfato libero, quindi formano micelle invece del doppio strato",
  ], 0,
  "Nella sfingomielina la sfingosina fornisce una coda e l'acido grasso (legato con legame ammidico) l'altra; i primi tre carboni della sfingosina ricordano il glicerolo.")
