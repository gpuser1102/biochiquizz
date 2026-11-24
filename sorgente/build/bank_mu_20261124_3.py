"""Giro 2026-11-24, blocco 3 – argomenti meno coperti: coagulazione (Biochimica I, p. 175–181)
e metabolismo del ferro (Biologia molecolare, lezione sul ferro)."""
from bank_common import q as _q


def q(*a, **k):
    _q(*a, **k)


# ── Fibrina e fibrinogeno (Biochimica I, p. 175–176) ────────────────────────
F = "d8-fibrina"
S1 = "Biochimica I"

q("u1124-106", F, "f", "176", "Come si chiamano i peptidi rimossi dalla trombina per attivare il fibrinogeno?", [
  "Fibrinopeptide A e fibrinopeptide B",
  "Fibrinopeptide A e fibrinopeptide C",
  "Fibrinopeptide α e fibrinopeptide γ",
  "Peptide attivatore della protrombina",
  "Peptide di von Willebrand A e B",
  ], 0,
  "Sono i primi 16 amminoacidi della regione N-terminale delle catene; sono ricchi di amminoacidi acidi e modificati, quindi carichi negativamente.", src=S1,
  note="Imprecisione nella sbobina (Biochimica I, p. 175): attribuisce «i primi 16 aa» sia alle catene α sia alle catene β. Nei testi di riferimento il fibrinopeptide A conta 16 residui, il fibrinopeptide B 14.")

q("u1124-107", F, "f", "176", "Quale enzima stabilizza il coagulo con legami crociati?", [
  "Il fattore XIIIa, una transglutamminasi",
  "Il fattore XIIa, una proteasi a serina",
  "La trombina, una proteasi a serina",
  "La plasmina, una transglutamminasi",
  "Il fattore X attivato, una idrolasi dei legami peptidici",
  ], 0,
  "È rilasciato dalle piastrine e fa reagire la catena laterale di una lisina con quella di una glutammina di due molecole di fibrina affacciate.", src=S1)

q("u1124-108", F, "m", "175", "Com'è fatta strutturalmente la molecola di fibrinogeno?", [
  "Bastoncellare, con estremità globulari in cui sporgono le catene β e γ",
  "Globulare compatta, con le sei catene avvolte in un unico dominio centrale",
  "Bastoncellare, con le catene α raccolte alle due estremità della molecola",
  "A forma di Y, con due bracci identici uniti da una regione cerniera",
  "Ad anello chiuso, stabilizzato da ponti disolfuro fra catene adiacenti",
  ], 0,
  "Le catene α si ripiegano lungo la molecola sulle estremità globulari; i ponti disolfuro tengono unite le sei catene, come in tutte le proteine extracellulari multicatena.", src=S1)

q("u1124-109", F, "m", "176", "Come si dispongono le molecole di fibrina quando polimerizzano?", [
  "Sfalsate l'una rispetto all'altra di mezza molecola",
  "Allineate testa-coda, con le estremità perfettamente affacciate",
  "Appaiate in parallelo, senza alcuno sfalsamento reciproco",
  "Avvolte l'una sull'altra a formare una tripla elica",
  "Disposte a raggiera intorno a un nucleo di fattore XIII",
  ], 0,
  "Lo sfalsamento di mezza molecola dà la struttura a bandeggio; le estremità delle catene stabilizzano i contatti, poi rinforzati dai legami crociati.", src=S1)

q("u1124-110", F, "a", "176", "Perché la rimozione dei fibrinopeptidi permette la polimerizzazione?", [
  "La regione centrale perde cariche negative e diventa globalmente positiva",
  "La regione centrale acquista cariche negative e respinge le estremità",
  "Le estremità perdono la carica negativa e si neutralizzano a vicenda",
  "La molecola si accorcia e riesce a inserirsi fra due molecole già adiacenti",
  "Si espongono i ponti disolfuro che saldano le molecole fra loro",
  ], 0,
  "Le due estremità restano a carica −4, ma il centro diventa positivo: centro positivo ed estremità negative si attraggono e le molecole si associano.", src=S1)

q("u1124-111", F, "a", "175", "Che cosa espone il fattore di von Willebrand quando subisce lo shear stress?", [
  "Il sito per il suo recettore piastrinico, quello per il collagene e quello per un altro fattore",
  "Soltanto il sito di legame per il collagene della parete vasale danneggiata",
  "Soltanto il sito di legame per il recettore GPIb-V/IX delle piastrine già attivate dal collagene",
  "I siti di taglio per la trombina, che lo converte nella forma attiva",
  "I residui di γ-carbossiglutammato necessari al legame con il calcio",
  ], 0,
  "La turbolenza srotola la proteina e rende visibili siti che nella forma ripiegata non lo sono.", src=S1)

q("u1124-112", F, "l", "175", "Quali sono le caratteristiche genetiche del fattore di von Willebrand?", [
  "Gene con 52 esoni sul braccio corto del cromosoma 12, glicoproteina da 250 kDa",
  "Gene con 26 esoni sul braccio lungo del cromosoma 12, glicoproteina da 250 kDa",
  "Gene con 52 esoni sul braccio corto del cromosoma 11, glicoproteina da 150 kDa",
  "Gene con 12 esoni sul braccio lungo del cromosoma 52, glicoproteina da 78 kDa",
  "Gene con 26 esoni sul cromosoma X, glicoproteina da 250 kDa prodotta nel fegato",
  ], 0,
  "È sintetizzata da cellule endoteliali e megacariociti. I tipi 1 e 2 della malattia sono autosomici dominanti, il tipo 3 autosomico recessivo.", src=S1)

q("u1124-114", F, "h", "176", "Perché il fibrinogeno circola in grande quantità senza formare coaguli spontanei?", [
  "Ha carica netta negativa e le molecole si respingono fra loro",
  "È legato all'albumina, che ne impedisce l'associazione in fibre",
  "È mantenuto in forma monomerica dall'antitrombina circolante",
  "Viene degradato di continuo dalla plasmina presente nel plasma",
  "È troppo diluito perché due molecole si incontrino con frequenza",
  ], 0,
  "È la repulsione elettrostatica a tenerlo in soluzione: serve il taglio della trombina per invertire la carica della regione centrale.", src=S1)


# ── Vitamina K (Biochimica I, p. 179–181) ───────────────────────────────────
K = "d8-vitk"

q("u1124-115", K, "f", "179", "Come si chiama la vitamina K2 e dove viene prodotta?", [
  "Menachinone, prodotto a livello del colon",
  "Menachinone, assorbito a livello dell'ileo",
  "Filochinone, prodotto a livello del colon",
  "Filochinone, assorbito a livello dell'ileo",
  "Idrochinone, prodotto a livello del fegato",
  ], 0,
  "Le due forme differiscono per la catena laterale: la K1 (filochinone) viene assorbita nell'ileo, la K2 (menachinone) è di produzione batterica nel colon.", src=S1)

q("u1124-116", K, "m", "180", "Che cosa fa esattamente la γ-glutammil-carbossilasi?", [
  "Incorpora una molecola di CO₂ sul carbonio γ di residui di acido glutammico",
  "Incorpora una molecola di CO₂ sul carbonio α di residui di acido glutammico",
  "Rimuove un gruppo carbossilico dal carbonio γ dei residui di glutammato",
  "Trasferisce un gruppo carbossilico dalla biotina al residuo di glutammato",
  "Lega uno ione calcio ai residui di glutammato dei fattori della coagulazione",
  ], 0,
  "È un enzima epatico vitamina K-dipendente; il prodotto è il γ-carbossiglutammato (GLA).", src=S1)

q("u1124-117", K, "m", "180", "Qual è la forma attiva della vitamina K?", [
  "L'idrochinone, cioè la forma ridotta",
  "L'epossido, cioè la forma con il ponte ossigeno",
  "Il chinone, cioè la forma completamente ossidata",
  "Il menachinone, cioè la forma a catena laterale lunga",
  "Il carbanione, cioè la forma con carica negativa",
  ], 0,
  "È una struttura chinonica in cui entrambi i gruppi in para sono ossidrilici; durante la carbossilazione si ossida a epossido.", src=S1)

q("u1124-118", K, "a", "180", "Quale meccanismo chimico permette la carbossilazione del glutammato?", [
  "Si forma un carbanione in γ che attacca il carbonio elettrofilo della CO₂",
  "Si forma un carbocatione in γ che attacca l'ossigeno nucleofilo della CO₂",
  "Si forma un radicale in γ che si addiziona a un doppio legame della CO₂",
  "Si forma un intermedio fosforilato che trasferisce il gruppo carbossilico",
  "Si forma un legame estere fra il glutammato e la vitamina K ridotta",
  ], 0,
  "Il sito attivo crea le condizioni per allontanare il protone e attivare il carbonio γ; la reazione richiede ossigeno ed è accompagnata dall'ossidazione della vitamina a epossido.", src=S1)

q("u1124-119", K, "a", "180", "Quale enzima rigenera la forma attiva della vitamina K, e come?", [
  "La vitamina K ossidoreduttasi, che usa cisteine come donatori di elettroni",
  "La vitamina K ossidoreduttasi, che usa il NADPH come donatore di elettroni",
  "La γ-glutammil-carbossilasi stessa, al termine di ogni ciclo di reazione",
  "Una perossidasi mitocondriale, che riduce l'epossido usando il glutatione",
  "Una deidrogenasi epatica, che ossida l'idrochinone a epossido stabile",
  ], 0,
  "Dall'epossido si torna prima al chinone e poi, con un'ulteriore riduzione, all'idrochinone attivo.", src=S1)

q("u1124-120", K, "m", "181", "Qual è l'origine naturale del dicumarolo?", [
  "Il trifoglio dolce",
  "La corteccia di salice",
  "Il veleno di serpente",
  "Un fungo del genere Penicillium",
  "Le foglie di digitale",
  ], 0,
  "È un anticoagulante naturale; la warfarina, strutturalmente simile alla vitamina K, nasce invece come veleno per topi ed è usata come farmaco.", src=S1)

q("u1124-121", K, "a", "180", "Quali fattori, oltre alla protrombina, hanno bisogno della carbossilazione vitamina K-dipendente?", [
  "I fattori VII, IX e X",
  "I fattori V, VIII e XIII",
  "I fattori XI, XII e XIII",
  "I fattori V, VII e VIII",
  "I fattori VIII, IX e XI",
  ], 0,
  "Appartengono sia alla via intrinseca sia alla via estrinseca; i residui di γ-carbossiglutammato permettono loro, con calcio e fosfolipidi, di legarsi alle piastrine nel sito di lesione.", src=S1)

q("u1124-122", K, "l", "180", "Perché la reazione della γ-glutammil-carbossilasi richiede ossigeno?", [
  "Perché l'ossidazione della vitamina K a epossido fornisce l'energia del processo",
  "Perché l'ossigeno è il substrato che viene incorporato nel glutammato carbossilato",
  "Perché l'ossigeno ossida la cisteina del sito attivo, che attiva poi il substrato",
  "Perché l'ossigeno serve a rimuovere il protone dal carbonio γ del glutammato",
  "Perché l'ossigeno rigenera direttamente l'idrochinone a partire dall'epossido",
  ], 0,
  "L'ossidazione dell'idrochinone a epossido è accoppiata alla formazione del carbanione, che poi attacca spontaneamente la CO₂.", src=S1)


# ── Fibrinolisi e inibitori (Biochimica I, p. 181) ──────────────────────────
FL = "d8-fibrinolisi"

q("u1124-123", FL, "f", "181", "Da quale precursore si forma la plasmina?", [
  "Dal plasminogeno",
  "Dal fibrinogeno",
  "Dalla protrombina",
  "Dal plasminogeno tissutale",
  "Dall'antitrombina",
  ], 0,
  "È una proteasi a serina; l'attivatore fisiologico è il t-PA, l'attivatore tissutale.", src=S1)

q("u1124-124", FL, "m", "181", "Quale organo produce l'urochinasi?", [
  "Il rene",
  "Il fegato",
  "Il polmone",
  "La milza",
  "L'endotelio dei vasi",
  ], 0,
  "Accanto al t-PA, che è l'attivatore fisiologico, hanno un ruolo nella fibrinolisi anche l'urochinasi e la streptochinasi.", src=S1)

q("u1124-125", FL, "m", "181", "Che fine fanno i frammenti prodotti dalla degradazione della rete di fibrina?", [
  "Vengono trascinati dal sangue ed eliminati a livello epatico",
  "Vengono riassemblati in nuovo fibrinogeno dalle piastrine",
  "Vengono eliminati con le urine dopo filtrazione glomerulare",
  "Vengono fagocitati sul posto dai macrofagi della parete vasale",
  "Vengono degradati dall'antitrombina insieme ai fattori attivati",
  ], 0,
  "La plasmina taglia la rete in piccoli frammenti solubili che il circolo porta al fegato.", src=S1)

q("u1124-126", FL, "a", "181", "Quale complesso attiva la proteina C e quali fattori vengono poi inattivati?", [
  "Trombina-trombomodulina; inattiva i fattori Va e VIIIa",
  "Trombina-trombomodulina; inattiva i fattori IXa e Xa",
  "Antitrombina-eparina; inattiva i fattori Va e VIIIa",
  "Plasmina-plasminogeno; inattiva i fattori Va e VIIIa",
  "Fattore Xa-fattore Va; inattiva la trombina e il fattore IXa",
  ], 0,
  "La proteina C attivata si associa al suo cofattore, la proteina S, e inattiva per proteolisi limitata i cofattori Va e VIIIa. L'antitrombina agisce invece su trombina, IXa e Xa.", src=S1)

q("u1124-127", FL, "a", "181", "A che cosa servono, nel complesso, gli inibitori fisiologici della coagulazione?", [
  "A contenere il coagulo, limitarne le dimensioni e poi rimuoverlo",
  "A impedire del tutto la formazione del coagulo all'interno dei vasi integri",
  "A degradare il fibrinogeno in eccesso presente nel plasma",
  "A favorire l'adesione delle piastrine al collagene esposto",
  "A sostituire la vitamina K nella maturazione dei fattori",
  ], 0,
  "Evitano che la coagulazione parta quando non serve e che si formino trombi capaci di otturare il vaso mentre il tessuto si rigenera.", src=S1)

q("u1124-128", FL, "h", "181", "Un paziente riceve streptochinasi dopo un infarto. Su quale passaggio agisce il farmaco?", [
  "Sull'attivazione del plasminogeno, aumentando la produzione di plasmina",
  "Sull'inattivazione della trombina, potenziando l'azione dell'antitrombina",
  "Sulla polimerizzazione della fibrina, impedendo i legami crociati",
  "Sulla maturazione dei fattori, bloccando la vitamina K ossidoreduttasi",
  "Sull'aggregazione piastrinica, bloccando il recettore del trombossano",
  ], 0,
  "È uno degli attivatori del plasminogeno citati accanto al t-PA e all'urochinasi: più plasmina significa più degradazione della rete di fibrina già formata.", src=S1)


# ── Metabolismo del ferro (Biologia molecolare) ─────────────────────────────
FE = "bm11-ferro"
S2 = "Biologia molecolare"

q("u1124-129", FE, "f", "lezione 11", "Quali prodotti si formano nella reazione di Fenton?", [
  "Fe³⁺, ione idrossido e radicale ossidrilico",
  "Fe²⁺, ione idrossido e perossido di idrogeno",
  "Fe³⁺, acqua e ossigeno molecolare",
  "Fe²⁺, radicale superossido e acqua",
  "Fe³⁺, anione superossido e ossigeno singoletto",
  ], 0,
  "Il Fe²⁺ reagisce con l'acqua ossigenata; il radicale ossidrilico è una specie molto pericolosa, ed è il motivo per cui la disponibilità di ferro libero va controllata.", src=S2)

q("u1124-130", FE, "f", "lezione 11", "Quale percentuale del ferro corporeo si trova nell'emoglobina?", [
  "Circa il 65%",
  "Circa il 20%",
  "Circa il 45%",
  "Circa l'85%",
  "Circa il 6%",
  ], 0,
  "Il 6% sta nella mioglobina, il 20% del ferro non-eme è di deposito in ferritina ed emosiderina, meno dell'1% nei citocromi.", src=S2)

q("u1124-131", FE, "m", "lezione 11", "Perché il Fe³⁺ è poco biodisponibile anche quando è chelato da citrato o EDTA?", [
  "Perché i chelanti aumentano la solubilità ma non rilasciano il ferro",
  "Perché i chelanti ossidano ulteriormente il ferro a Fe⁴⁺ inutilizzabile",
  "Perché i complessi con i chelanti sono troppo grandi per i trasportatori",
  "Perché i chelanti precipitano come idrossido ferrico a pH fisiologico",
  "Perché i chelanti competono con la transferrina per il sito di legame",
  ], 0,
  "La velocità di scambio dell'acqua, e quindi dei leganti, è bassa: il ferro resta legato e non può essere captato. Per renderlo disponibile bisogna ridurlo.", src=S2)

q("u1124-132", FE, "m", "lezione 11", "Perché la riduzione a Fe²⁺ rende il ferro più disponibile?", [
  "Aumenta la velocità di scambio dell'acqua e riduce l'affinità per i chelanti",
  "Aumenta l'affinità per i chelanti e rallenta lo scambio dei leganti",
  "Riduce la solubilità dell'idrossido e favorisce la precipitazione del metallo",
  "Permette il legame diretto alla transferrina, che lega solo il ferro ridotto",
  "Impedisce la formazione di specie reattive dell'ossigeno nella cellula",
  ], 0,
  "Anche l'idrossido ferroso è più solubile di quello ferrico, e a pH 7 la solubilità del Fe²⁺ idratato è molto più alta.", src=S2)

q("u1124-133", FE, "m", "lezione 11", "Quanto ferro viene liberato ogni giorno dall'emolisi degli eritrociti e riutilizzato?", [
  "Circa 20 mg",
  "Circa 1–2 mg",
  "Circa 300 mg",
  "Circa 1 g",
  "Circa 2,5 g",
  ], 0,
  "È molto più di quello assorbito con la dieta (1–2 mg al giorno, pari a quello perso): la maggior parte del ferro disponibile viene dal riciclo nei macrofagi.", src=S2)

q("u1124-134", FE, "a", "lezione 11", "Quali sono i due «regolatori» dell'assorbimento del ferro?", [
  "Il fegato come storage regulator e il midollo osseo come erythroid regulator",
  "Il duodeno come storage regulator e la milza come erythroid regulator",
  "Il midollo osseo come storage regulator e il fegato come erythroid regulator",
  "Il rene come storage regulator e il fegato come erythroid regulator",
  "La milza come storage regulator e il duodeno come erythroid regulator",
  ], 0,
  "Il fegato è anche il deposito più grande di ferro, quello a cui la transferrina cede la quota maggiore.", src=S2)

q("u1124-135", FE, "a", "lezione 11", "Perché la carenza di ferro peggiora la prestazione fisica e dà fatica?", [
  "Calano gli enzimi a ferro della catena respiratoria e del ciclo di Krebs",
  "Cala la sintesi di DNA nelle fibre muscolari in rapida proliferazione",
  "Cala la produzione di ossido nitrico, con vasocostrizione del muscolo",
  "Aumentano le specie reattive dell'ossigeno prodotte nel mitocondrio",
  "Diminuisce il numero dei recettori per la dopamina nel sistema nervoso centrale",
  ], 0,
  "Il ferro è nei citocromi, nelle ferredossine, nella proteina di Rieske e nell'aconitasi: con poco ferro il metabolismo energetico rende meno. L'effetto sulla dopamina riguarda invece il metabolismo neuronale.", src=S2)

q("u1124-136", FE, "l", "lezione 11", "Quale quota del ferro corporeo è presente come ferro libero nel plasma?", [
  "Circa 4 mg",
  "Circa 40 mg",
  "Circa 300 mg",
  "Circa 1 g",
  "Circa 20 mg",
  ], 0,
  "È una quantità piccolissima, in equilibrio con tutte le altre forme: 2,5 g nell'emoglobina, circa 1 g nei depositi, circa 300 mg negli enzimi ad eme.", src=S2)

q("u1124-137", FE, "h", "lezione 11", "Perché il ferro è contemporaneamente essenziale e pericoloso?", [
  "Le stesse reazioni redox che lo rendono utile possono generare ROS",
  "Si accumula nei tessuti perché l'organismo non ha una via di escrezione",
  "È insolubile e precipita nei tessuti come idrossido ferrico",
  "Compete con lo zinco nei siti attivi di molti enzimi essenziali",
  "Viene sottratto dai patogeni, che lo usano per moltiplicarsi nei tessuti",
  ], 0,
  "Passando fra Fe²⁺, Fe³⁺ e Fe⁴⁺ media processi redox in cui donatore o accettore è spesso l'ossigeno: da qui radicali liberi e specie reattive dell'ossigeno, con danno cellulare.", src=S2)


# ── Proteine del ferro (Biologia molecolare) ────────────────────────────────
PR = "bm11-proteine"

q("u1124-138", PR, "f", "lezione 11", "Da quante subunità è formata la ferritina?", [
  "24",
  "12",
  "6",
  "48",
  "4",
  ], 0,
  "Sono di due tipi, H (pesanti) e L (leggere), e formano una sfera cava di 12 nm di diametro esterno e 8 nm interno.", src=S2)

q("u1124-139", PR, "f", "lezione 11", "Quanto pesa la catena polipeptidica della transferrina?", [
  "78 kDa",
  "250 kDa",
  "12 kDa",
  "150 kDa",
  "45 kDa",
  ], 0,
  "È un'unica catena con due siti distinti di legame per lo ione ferrico.", src=S2)

q("u1124-140", PR, "m", "lezione 11", "Quale ione deve accompagnare obbligatoriamente il legame del ferro alla transferrina?", [
  "Lo ione carbonato",
  "Lo ione fosfato",
  "Lo ione cloruro",
  "Lo ione solfato",
  "Lo ione calcio bivalente",
  ], 0,
  "Ogni sito lega uno ione ferrico insieme a uno ione carbonato; l'affinità è altissima, con Ka fra 10¹⁹ e 10³¹ M⁻¹.", src=S2)

q("u1124-141", PR, "m", "lezione 11", "Che differenza c'è fra le subunità H e L della ferritina?", [
  "Solo la H ha il centro ferrossidasico che ossida il Fe²⁺ entrato",
  "Solo la L ha il centro ferrossidasico che ossida il Fe²⁺ entrato",
  "Solo la H forma i pori di accesso per i cationi ferro",
  "Solo la L è in grado di legare il ferro nella forma minerale",
  "Solo la H è presente nelle cellule che depositano molto ferro",
  ], 0,
  "Entrambe sono fasci di quattro α-eliche antiparallele; ciò che cambia è il centro attivo, presente solo nella catena pesante.", src=S2)

q("u1124-142", PR, "m", "lezione 11", "Quale proteina plasmatica lega l'emoglobina libera?", [
  "L'aptoglobina",
  "L'emopessina",
  "La lattoferrina",
  "L'α1-microglobulina",
  "La perossiredossina I",
  ], 0,
  "Il complesso viene riconosciuto dal recettore CD163 dei macrofagi ed endocitato; l'emopessina lega invece l'eme libero, riconosciuto dal recettore CD91.", src=S2,
  note="Contraddizione interna alla sbobina (Biologia molecolare, lezione sul ferro): il recettore per il complesso emoglobina-aptoglobina è indicato prima come CD163 e poi come CD63. Quello corretto è CD163.")

q("u1124-143", PR, "a", "lezione 11", "Come entra ed esce il ferro dalla ferritina?", [
  "Entra come Fe²⁺ dai pori rivestiti di amminoacidi acidi ed esce ridotto",
  "Entra come Fe³⁺ dai pori rivestiti di amminoacidi basici ed esce ossidato",
  "Entra come Fe²⁺ e resta tale, perché la ferritina non ha attività redox",
  "Entra legato alla transferrina, che lo cede direttamente nel guscio",
  "Entra e esce liberamente, perché la sfera è permeabile ai cationi",
  ], 0,
  "I canali carichi negativamente richiamano i cationi; dentro, il Fe²⁺ viene ossidato a Fe³⁺ e costituisce un minerale, forma di deposito che non dà stress ossidativo. Per mobilizzarlo servono agenti riducenti.", src=S2)

q("u1124-144", PR, "a", "lezione 11", "Perché la transferrina è saturata solo in parte e che senso ha?", [
  "La riserva di siti liberi sottrae ferro ai patogeni e contrasta le infezioni",
  "La riserva di siti liberi serve a legare il rame in eccesso presente nel plasma",
  "I siti liberi impediscono alla proteina di legarsi al proprio recettore",
  "I siti liberi riducono il rischio che la proteina precipiti nel plasma",
  "La saturazione parziale rallenta la cessione del ferro ai tessuti",
  ], 0,
  "Un nono della proteina è saturo in entrambi i siti, quattro noni in uno solo e quattro noni ha siti liberi: l'altissima affinità per il Fe³⁺ le permette di catturare il ferro libero prima dei microrganismi.", src=S2)

q("u1124-145", PR, "a", "lezione 11", "Che cosa cambia nell'affinità della transferrina per il suo recettore?", [
  "La forma olo lega bene il TFR, la forma apo viene rilasciata in circolo",
  "La forma apo lega bene il TFR, la forma olo viene rilasciata in circolo",
  "Entrambe le forme legano il TFR con la stessa affinità elevata",
  "Solo la forma satura in entrambi i siti riesce a legare il recettore",
  "L'affinità dipende dallo ione carbonato e non dal ferro legato",
  ], 0,
  "Dopo l'internalizzazione il ferro viene rilasciato nella cellula; il recettore torna in superficie con la transferrina apo, che a quel punto si stacca e riparte.", src=S2)

q("u1124-146", PR, "l", "lezione 11", "Quali proteine plasmatiche formano lo «scavenging buffer» per l'eme libero, prima dell'emopessina?", [
  "Albumina, lipoproteine e α1-microglobulina",
  "Albumina, aptoglobina e lattoferrina",
  "Transferrina, ferritina e α1-microglobulina",
  "Lipoproteine, aptoglobina e perossiredossina I",
  "Albumina, transferrina e ceruloplasmina",
  ], 0,
  "Quando l'emoglobina libera supera la quantità di aptoglobina, viene ossidata fuori dalla cellula e libera l'eme, che viene tamponato da queste proteine e poi ceduto all'emopessina, che lo lega ad altissima affinità.", src=S2)

q("u1124-147", PR, "h", "lezione 11", "Quale proteina sfrutta lo stesso principio della transferrina per difendere le mucose dalle infezioni?", [
  "La lattoferrina, che sottrae ferro ai microrganismi",
  "La ferritina, che deposita il ferro in forma minerale",
  "L'aptoglobina, che lega l'emoglobina libera nel plasma",
  "L'emopessina, che lega l'eme libero ad altissima affinità",
  "La ceruloplasmina, che ossida il ferro esportato dalla cellula",
  ], 0,
  "È una proteina che lega il ferro con un ruolo analogo a quello della transferrina: togliendo ferro libero all'ambiente, impedisce ai patogeni di proliferare.", src=S2)


# ── Ferro a livello cellulare (Biologia molecolare) ─────────────────────────
CE = "bm11-cellule"

q("u1124-148", CE, "f", "lezione 11", "Quale trasportatore fa entrare il ferro nell'enterocita?", [
  "Il DMT1, specifico per i cationi bivalenti",
  "La ferroportina, specifica per i cationi bivalenti",
  "Il TFR, il recettore della transferrina",
  "L'HCP1, il trasportatore dell'eme",
  "L'Abcb6, trasportatore del coproporfirinogeno",
  ], 0,
  "Entra in forma ridotta Fe²⁺; sulla membrana ci sono anche ferro reduttasi che riducono il Fe³⁺ per facilitarne l'assorbimento.", src=S2)

q("u1124-149", CE, "m", "lezione 11", "Che cosa fa la ferroportina nell'enterocita?", [
  "Esporta il ferro, che viene poi ossidato e caricato sulla transferrina",
  "Importa il ferro dal lume intestinale nella forma ridotta Fe²⁺",
  "Deposita il ferro all'interno dell'enterocita legandolo alla ferritina",
  "Ossida il ferro nel citosol prima che venga depositato nella ferritina",
  "Trasporta l'eme intatto attraverso la membrana basolaterale",
  ], 0,
  "Una volta entrato, il ferro può essere depositato nell'enterocita oppure esportato, a seconda delle necessità dell'organismo.", src=S2)

q("u1124-150", CE, "a", "lezione 11", "Attraverso quali trasportatori si muove l'eme dentro e fuori la cellula?", [
  "HCP1 sulla membrana plasmatica, Abcb6 e ANT nel mitocondrio",
  "DMT1 sulla membrana plasmatica, ferroportina nel mitocondrio",
  "TFR sulla membrana plasmatica, DMT1 nell'endosoma",
  "Ferroportina sulla membrana plasmatica, HCP1 nel mitocondrio",
  "Abcb6 sulla membrana plasmatica, DMT1 nel mitocondrio",
  ], 0,
  "Abcb6 riporta il coproporfirinogeno III nel mitocondrio, ANT porta l'eme finito nel citoplasma; HCP1 permette l'ingresso di eme dall'esterno.", src=S2)

q("u1124-151", CE, "h", "lezione 11", "Perché l'eme libero nel citosol è un problema per la cellula?", [
  "È pro-ossidante per il ferro, genera radicali ed è fotosensibile",
  "Precipita nel citosol e forma aggregati insolubili tossici",
  "Compete con il ferro per il legame alla ferritina di deposito",
  "Inibisce l'ALA sintasi e blocca la propria stessa sintesi",
  "Lega l'ossigeno e lo sottrae alla catena respiratoria mitocondriale",
  ], 0,
  "Per questo viene legato nel citosol dalla perossiredossina I, che ne limita la citotossicità; l'eccesso induce la sintesi di proteine che lo incorporano e viene poi degradato.", src=S2)


# ── Sintesi e degradazione dell'eme (Biologia molecolare) ───────────────────
EM = "bm11-eme"

q("u1124-153", EM, "m", "lezione 11", "Quali prodotti libera l'eme ossigenasi?", [
  "Ferro, monossido di carbonio e biliverdina",
  "Ferro, anidride carbonica e biliverdina",
  "Ferro, monossido di carbonio e bilirubina",
  "Ferro, monossido di carbonio e protoporfirina IX",
  "Zinco, monossido di carbonio e biliverdina",
  ], 0,
  "L'enzima linearizza l'anello tagliando fra gli anelli A e B, con NADPH come donatore di elettroni e ossigeno. Il ferro va nella ferritina, la biliverdina viene poi ridotta a bilirubina.", src=S2)

q("u1124-154", EM, "a", "lezione 11", "Che ruolo ha il monossido di carbonio liberato dalla degradazione dell'eme?", [
  "Modula le emoproteine legando il ferro e previene il rilascio dell'eme",
  "Ossida il ferro ferroso a ferrico prima del deposito nella ferritina",
  "Attiva l'isoforma eme ossigenasi 1 nelle condizioni di stress metabolico",
  "Riduce la biliverdina a bilirubina insieme al NADPH",
  "Favorisce il legame della bilirubina all'albumina plasmatica",
  ], 0,
  "Legando il ferro dell'eme impedisce l'ossidazione delle proteine e ne previene il rilascio: non è solo un prodotto di scarto.", src=S2)

q("u1124-155", EM, "l", "lezione 11", "Perché in carenza di ferro si misura la zinco-protoporfirina?", [
  "La ferrochelatasi inserisce lo zinco quando il ferro non è disponibile",
  "Lo zinco sostituisce il ferro nell'emoglobina matura dei globuli rossi",
  "Lo zinco si accumula perché la sua escrezione dipende dal ferro",
  "La protoporfirina lega lo zinco spontaneamente, senza alcun enzima",
  "Lo zinco inibisce la ferrochelatasi, come fa anche il piombo",
  ], 0,
  "L'enzima tende comunque a trasferire un catione per stabilizzare la protoporfirina: è un indicatore clinico importante del deficit di ferro. Il piombo, invece, inibisce l'enzima in modo competitivo senza essere incorporato.", src=S2)
