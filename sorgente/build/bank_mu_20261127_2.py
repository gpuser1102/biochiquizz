"""Giro 2026-11-27, blocco 2 – Biochimica II, pp. 259–310: difetti degli amminoacidi, folato e B12,
vie specializzate, neuroipofisi e adenoipofisi, tiroide, calcio, steroidi, mediatori locali."""
from bank_common import q as _q

S = "Biochimica II"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Tiroide (p. 289–293) ───────────────────────────────────────────────────
C = "m9-tiroide"

q("u1127-101", C, "l", "290", "Quale trasportatore porta lo ioduro dalla cellula follicolare alla colloide?", [
  "La pendrina",
  "Il simporto Na⁺/I⁻",
  "La transtiretina",
  "La tireoglobulina",
  "L'acquaporina 3",
  ], 0,
  "Lo ioduro entra dal sangue con il simporto Na⁺/I⁻ (il Na⁺ viene poi espulso dalla Na⁺/K⁺-ATPasi) e passa nella colloide con la pendrina, dove viene ossidato e legato alla tireoglobulina.")

q("u1127-102", C, "m", "290", "Come vengono liberati T3 e T4 dalla tireoglobulina?", [
  "La tireoglobulina iodata rientra per endocitosi e viene degradata dalle proteasi lisosomiali",
  "Una deiodinasi della colloide taglia T3 e T4 dalla proteina e li libera direttamente nel sangue",
  "La tiroide perossidasi idrolizza i legami peptidici delle tirosine già iodate",
  "Il TSH si lega alla tireoglobulina e ne stacca gli ormoni sulla membrana apicale",
  "La tireoglobulina viene secreta intera nel sangue e scissa poi nel fegato",
  ], 0,
  "Nella colloide la tiroide perossidasi iodina e accoppia le tirosine della tireoglobulina; la proteina rientra nella cellula per endocitosi e pinocitosi e viene completamente degradata nei lisosomi, liberando T3 e T4.")

q("u1127-103", C, "m", "291", "A che cosa serve la deiodinasi della cellula follicolare, oltre a trasformare il T4 in T3?", [
  "Recupera lo iodio dalle tirosine iodate che non sono diventate ormoni",
  "Aggiunge iodio in posizione 3 e 5 alle tirosine della tireoglobulina",
  "Ossida lo ioduro a iodio usando l'acqua ossigenata prodotta dalla cellula",
  "Trasforma il T3 in reverse T3 per spegnere l'ormone nella tiroide",
  "Lega il T4 nel sangue e lo porta ai tessuti insieme alla TBG",
  ], 0,
  "Dalla degradazione della tireoglobulina escono anche tirosine mono- e diiodate non accoppiate: la deiodinasi ne toglie lo iodio, che viene riciclato. La iodinazione è opera della tiroide perossidasi.")

q("u1127-104", C, "h", "292", "Per la piena azione degli ormoni tiroidei la sbobina cita tre microelementi. Quale abbinamento è corretto?", [
  "Iodio negli ormoni, selenio nelle deiodinasi, zinco nelle dita di zinco del recettore",
  "Iodio nelle deiodinasi, selenio negli ormoni, zinco nella tiroide perossidasi",
  "Iodio negli ormoni, zinco nelle deiodinasi, selenio nelle dita di zinco del recettore",
  "Ferro negli ormoni, selenio nella pendrina, zinco nella tireoglobulina",
  "Iodio negli ormoni, rame nelle deiodinasi, zinco nella transtiretina",
  ], 0,
  "Lo iodio è nell'ormone; il selenio sta nelle deiodinasi (e nella glutatione perossidasi); lo zinco serve al motivo a dita di zinco con cui il recettore nucleare lega il DNA. Il ferro è nella tiroide perossidasi.")

q("u1127-105", C, "a", "293", "Che effetto hanno gli ormoni tiroidei sul rapporto tra ATP prodotto e ossigeno consumato?", [
  "Lo abbassano: una parte maggiore dell'energia viene dissipata come calore",
  "Lo alzano: la catena respiratoria diventa più efficiente e produce meno calore",
  "Non lo cambiano: aumentano solo la quantità di mitocondri per cellula",
  "Lo alzano: inibiscono le proteine disaccoppianti UCP2 e UCP3",
  "Lo abbassano: bloccano l'ATP sintasi e la cellula passa alla glicolisi",
  ], 0,
  "Aumentando UCP2, UCP3 e Na⁺/K⁺-ATPasi, gli ormoni tiroidei riducono l'ATP formato per molecola di O₂ e aumentano il calore: per questo l'ipertiroideo ha caldo e l'ipotiroideo tende ad aumentare di peso.")

q("u1127-106", C, "m", "293", "Che cosa caratterizza la tiroidite di Hashimoto secondo la sbobina?", [
  "Anticorpi contro tireoglobulina o tiroide perossidasi, con ipotiroidismo",
  "Anticorpi che attivano il recettore del TSH, con ipertiroidismo e gozzo",
  "Carenza alimentare di iodio, con gozzo e ipertiroidismo",
  "Anticorpi contro la TBG, con ormoni liberi molto aumentati",
  "Un adenoma ipofisario che secerne TSH, con ipertiroidismo",
  ], 0,
  "Hashimoto è autoimmune e distrugge la tiroide (ipotiroidismo, mixedema, gozzo). Gli anticorpi che stimolano il recettore del TSH sono quelli del morbo di Graves-Basedow.")

q("u1127-107", C, "l", "291", "Dove avviene in gran parte la conversione periferica del T4 in T3?", [
  "Nel fegato, ad opera di una deiodinasi selenio-dipendente",
  "Nel rene, ad opera di una deiodinasi zinco-dipendente",
  "Nel sangue, ad opera della transtiretina che toglie lo iodio",
  "Nel tessuto adiposo, ad opera della tiroide perossidasi",
  "Nell'ipofisi, ad opera di una deiodinasi ferro-dipendente",
  ], 0,
  "Una parte del T3 si forma già nella cellula follicolare, ma gran parte della conversione avviene nel fegato. Se la deiodinasi toglie lo iodio dall'anello interno si forma il reverse T3, inattivo.")

# ── Calcio e vitamina D (p. 294–298) ───────────────────────────────────────
C = "m9-calcio"

q("u1127-108", C, "m", "294", "Come percepiscono le paratiroidi la calcemia e sotto quale soglia secernono il paratormone?", [
  "Con un recettore di membrana sensibile al Ca²⁺; sotto circa 1 mM",
  "Con un recettore nucleare che lega il Ca²⁺ libero; sotto circa 10 mM",
  "Attraverso l'asse ipotalamo-ipofisi e il TSH; sotto circa 1 mM",
  "Misurando il fosfato nel sangue; sopra circa 2 mM",
  "Con un recettore per il calcitriolo; sotto circa 0,1 mM",
  ], 0,
  "Le paratiroidi non dipendono dall'asse ipotalamo-ipofisario: un recettore di membrana sensibile al calcio fa secernere paratormone quando la calcemia scende sotto circa 1 mM.")

q("u1127-109", C, "f", "294", "Con quale secondo messaggero agisce il paratormone?", [
  "cAMP",
  "IP₃ e DAG",
  "cGMP",
  "JAK/STAT",
  "Nessuno: ha un recettore nucleare",
  ], 0,
  "Il paratormone è un ormone peptidico (84 amminoacidi) che agisce su un recettore di membrana con il cAMP come secondo messaggero.")

q("u1127-110", C, "a", "297", "Perché, secondo la sbobina, il calcio non può restare libero nel citoplasma?", [
  "Formerebbe sali insolubili con il fosfato ed è un secondo messaggero molto potente",
  "Inibirebbe la glicolisi legandosi all'ATP e bloccando l'esochinasi",
  "Attraverserebbe la membrana nucleare e attiverebbe in modo incontrollato la duplicazione del DNA",
  "Ossiderebbe i gruppi tiolici delle proteine come fa il ferro libero",
  "Verrebbe subito espulso dalla Na⁺/K⁺-ATPasi insieme al sodio",
  ], 0,
  "Il Ca²⁺ precipiterebbe con il fosfato e, essendo un segnale potente, deve restare compartimentato nel reticolo endoplasmatico e nei mitocondri, da cui viene liberato quando serve.")

q("u1127-111", C, "m", "296", "Quanto contribuisce la dieta alla vitamina D dell'organismo secondo la sbobina?", [
  "Circa il 10%: il resto si forma nella pelle a partire dal colesterolo",
  "Circa il 90%: nella pelle se ne forma solo una piccola parte",
  "Circa la metà: l'altra metà viene sintetizzata dalla flora intestinale",
  "Tutta: l'uomo non sa sintetizzare la vitamina D",
  "Circa il 10%: il resto viene prodotto dal fegato a partire dai carotenoidi",
  ], 0,
  "La vitamina D dei cibi animali copre solo circa il 10%; il resto è colecalciferolo formato nella pelle con la luce. Per questo d'inverno e negli anziani che escono poco i livelli calano.")

# ── Steroidi (p. 299–305) ──────────────────────────────────────────────────
C = "m9-steroidi"

q("u1127-112", C, "l", "299", "Come inizia la steroidogenesi dal colesterolo?", [
  "Idrossilazioni in 20 e 22 da un P450 mitocondriale con adrenodossina, poi il taglio della desmolasi",
  "Riduzione del doppio legame in 5 da una reduttasi citosolica, poi l'aromatasi apre l'anello A",
  "Idrossilazione in 11 nel reticolo, poi la 21-idrossilasi forma direttamente il cortisolo dal colesterolo",
  "Esterificazione dell'OH in 3 con un acido grasso, poi una lipasi libera il pregnenolone",
  "Ossidazione della catena laterale nel perossisoma, poi la tiolasi stacca i carboni in eccesso",
  ], 0,
  "Un citocromo P450 mitocondriale (con adrenodossina e NADPH) idrossila la catena laterale in 20 e 22 e la desmolasi la taglia: si forma il pregnenolone, a 21 atomi di carbonio.")

q("u1127-113", C, "m", "301", "In quali condizioni viene prodotto il cortisolo secondo la sbobina?", [
  "Ipoglicemia, dolore, paura, infezione e stress",
  "Iperglicemia dopo un pasto ricco di carboidrati",
  "Aumento della calcemia e della vitamina D",
  "Ipotensione, con l'attivazione della renina",
  "Esposizione al freddo, tramite il TSH",
  ], 0,
  "Il cortisolo, ormone dello stress, è prodotto tramite l'asse CRH–ACTH in ipoglicemia, dolore, paura, infezione e stress; agisce soprattutto su muscolo, fegato e tessuto adiposo.")

q("u1127-114", C, "a", "301", "Perché il cortisolo aumenta l'acidità gastrica, secondo la sbobina?", [
  "Per scindere più proteine e avere amminoacidi per la gluconeogenesi",
  "Per uccidere i batteri ingeriti durante lo stress e le infezioni",
  "Per attivare la vitamina B12 e liberarla dalle proteine della dieta",
  "Per ridurre l'assorbimento del glucosio e abbassare la glicemia",
  "Per neutralizzare il bicarbonato secreto dal pancreas in eccesso",
  ], 0,
  "Nella lettura della sbobina l'acidità serve a digerire più proteine e mettere a disposizione amminoacidi per la gluconeogenesi; l'effetto collaterale è la gastrite da stress.")

q("u1127-115", C, "m", "303", "Quale quadro elettrolitico è tipico del morbo di Addison?", [
  "Iposodiemia e iperkaliemia, con calo di gittata e pressione",
  "Ipersodiemia e ipokaliemia, con aumento della pressione arteriosa",
  "Iposodiemia e ipokaliemia, con pressione normale",
  "Ipercalcemia e ipofosfatemia, con calcoli renali",
  "Ipersodiemia e iperkaliemia, con edemi periferici",
  ], 0,
  "Senza aldosterone il rene riassorbe meno Na⁺ e trattiene K⁺: il liquido extracellulare cala con gittata e pressione. Senza cortisolo compare anche ipoglicemia grave.")

q("u1127-116", C, "a", "303", "Oltre a formare l'angiotensina II, quale altra azione dell'ACE contribuisce all'effetto degli ACE-inibitori?", [
  "L'ACE degrada la bradichinina vasodilatatrice, che con l'inibitore resta attiva",
  "L'ACE produce aldosterone nel surrene, che con l'inibitore non si forma più",
  "L'ACE attiva la renina con un taglio proteolitico, che con l'inibitore manca del tutto",
  "L'ACE forma il peptide natriuretico atriale, che con l'inibitore aumenta",
  "L'ACE degrada l'ossido nitrico nei vasi, che con l'inibitore si accumula",
  ], 0,
  "La bradichinina, antagonista dell'ACE, produce vasodilatazione e viene inattivata dall'ACE stesso: bloccando l'enzima cala l'angiotensina II e sale la bradichinina.")

q("u1127-117", C, "l", "304", "Che ruoli distingue la sbobina tra diidrotestosterone e testosterone?", [
  "Il diidrotestosterone agisce nello sviluppo embrionale, il testosterone alla pubertà",
  "Il testosterone agisce nello sviluppo embrionale, il diidrotestosterone alla pubertà",
  "Il diidrotestosterone è inattivo e serve solo come forma di deposito",
  "Il testosterone agisce solo nelle femmine dopo la conversione in estradiolo",
  "Hanno lo stesso ruolo e differiscono solo per l'emivita plasmatica",
  ], 0,
  "La 5α-reduttasi (NADPH) forma il diidrotestosterone, necessario allo sviluppo dei genitali esterni maschili nell'embrione; senza di essa si hanno quadri intersessuali. Il testosterone agisce alla pubertà.")

# ── Mediatori locali e acidi grassi alimentari (p. 306–310) ────────────────
C = "m9-locali"

q("u1127-118", C, "f", "306", "Quali ormoni intestinali danno il senso di sazietà secondo la sbobina?", [
  "GLP-1 e GLP-2",
  "Grelina e motilina",
  "Gastrina e secretina",
  "Leptina e neuropeptide Y",
  "Somatostatina e grelina",
  ], 0,
  "GLP-1 e GLP-2, prodotti dall'intestino, danno sazietà; la grelina stimola la fame.")

q("u1127-119", C, "l", "309", "Quale olio è indicato dalla sbobina come ricco di ω-3?", [
  "Olio di semi di lino",
  "Olio di semi di girasole",
  "Olio di semi di mais",
  "Olio di oliva",
  "Olio di palma",
  ], 0,
  "Gli ω-3 (acido linolenico) abbondano nell'olio di lino e nel grasso di salmone; girasole e mais hanno pochissimi ω-3 e molti ω-6; l'olio d'oliva ha un rapporto ω-6/ω-3 accettabile (circa 11:1).")

q("u1127-120", C, "m", "309", "Che effetto hanno grassi saturi e monoinsaturi sulle LDL secondo la sbobina?", [
  "I saturi le aumentano, i monoinsaturi le riducono",
  "I saturi le riducono, i monoinsaturi le aumentano",
  "Entrambi le aumentano, ma i saturi molto di più",
  "Nessuno dei due le modifica: agiscono solo sulle HDL",
  "Entrambi le riducono, ma i monoinsaturi molto di più",
  ], 0,
  "I saturi alzano le LDL e il rischio coronarico; i monoinsaturi (olio d'oliva) le abbassano. I peggiori sono i trans, che alzano le LDL e abbassano le HDL.")

q("u1127-121", C, "f", "307", "Quali derivati dell'acido arachidonico agiscono soprattutto nella coagulazione?", [
  "I trombossani",
  "I leucotrieni",
  "Le prostaglandine gastriche",
  "Le lipossine",
  "Gli endocannabinoidi",
  ], 0,
  "Dall'acido arachidonico (liberato dalla fosfolipasi A2) derivano prostaglandine (infiammazione), trombossani (coagulazione) e leucotrieni.")

q("u1127-122", C, "l", "308", "Quali derivati importanti per il sistema nervoso centrale si formano dall'acido linolenico?", [
  "EPA e DHA",
  "Acido arachidonico e prostaglandine",
  "Acido oleico e acido palmitoleico",
  "Ceramide e sfingomielina",
  "Acido linoleico e leucotrieni",
  ], 0,
  "L'acido linolenico (ω-3, 18 C) forma EPA e DHA, importanti per il sistema nervoso centrale. L'arachidonico deriva invece dal linoleico (ω-6).")

# ── Neuroipofisi e adenoipofisi (p. 279–288) ───────────────────────────────
C = "m9-neuroipofisi"

q("u1127-123", C, "m", "281", "Che differenza c'è tra l'acquaporina 2 e l'acquaporina 3 del rene?", [
  "La 2 sta su vescicole e va in membrana con la vasopressina; la 3 è basolaterale e costitutiva",
  "La 3 sta su vescicole e va in membrana con la vasopressina; la 2 è basolaterale e costitutiva",
  "Sono entrambe costitutive sulla membrana apicale e differiscono solo per la massa",
  "La 2 trasporta solo urea, la 3 solo acqua, ed entrambe sono regolate dall'aldosterone",
  "La 2 è nel tubulo prossimale, la 3 nell'ansa di Henle, ed entrambe sono costitutive",
  ], 0,
  "L'acquaporina 2 non è costitutivamente in membrana: è su vescicole che la vasopressina fa fondere con la membrana luminale. L'acquaporina 3 è sulla membrana basolaterale ed è sempre presente.")

q("u1127-124", C, "l", "281", "Che cos'è la gliceroloporina?", [
  "Un'acquaporina che lascia passare anche il glicerolo",
  "Una lipasi che libera glicerolo dai trigliceridi",
  "Una chinasi che fosforila il glicerolo nel fegato",
  "Un trasportatore del glicerolo 3-fosfato nel mitocondrio",
  "Una proteina che lega il glicerolo nel sangue",
  ], 0,
  "Delle 12–15 acquaporine dei mammiferi alcune trasportano anche altre molecole: la gliceroloporina il glicerolo, altre isoforme l'urea.")

C = "m9-adenoipofisi"

q("u1127-125", C, "l", "279", "Quale abbinamento tra fattore di rilascio ipotalamico e lunghezza è corretto?", [
  "GnRH – 10 amminoacidi",
  "TRH – 10 amminoacidi",
  "GHRH – 3 amminoacidi",
  "CRH – 44 amminoacidi",
  "GHRH – 41 amminoacidi",
  ], 0,
  "TRH 3 amminoacidi (modificati alle estremità), GnRH 10, CRH 41, GHRH 44.")

q("u1127-126", C, "l", "288", "Quali vie di segnalazione attiva il GHRH secondo la sbobina?", [
  "Sia il cAMP (con CREB) sia IP₃/DAG",
  "Solo JAK/STAT, come il GH",
  "Solo il cGMP, tramite una guanilato ciclasi",
  "Solo IP₃/DAG, come gli altri fattori ipotalamici",
  "Solo la via di Ras, tramite un recettore tirosin-chinasico",
  ], 0,
  "I fattori di rilascio usano in genere Gq e IP₃/DAG; il GHRH usa due vie, cAMP (con CREB) e IP₃/DAG. GH e prolattina usano invece JAK/STAT e Ras.")

q("u1127-127", C, "f", "284", "Quali quadri può dare un eccesso di GH secondo la sbobina?", [
  "Gigantismo o acromegalia",
  "Nanismo o cretinismo",
  "Diabete insipido o mixedema",
  "Morbo di Addison o di Cushing",
  "Osteoporosi o rachitismo",
  ], 0,
  "La carenza di GH dà nanismo; l'eccesso dà gigantismo o acromegalia (crescita di ossa di viso e mani). Il GH ricombinante si usa nella carenza.")

q("u1127-128", C, "m", "285", "Quali frammenti si ottengono dal taglio della proopiomelanocortina (POMC)?", [
  "ACTH, β-lipotropina, γ-MSH e α-MSH",
  "TSH, LH, FSH e prolattina",
  "Vasopressina, ossitocina e neurofisina",
  "GH, prolattina e somatostatina",
  "CRH, ACTH e cortisolo",
  ], 0,
  "La POMC, nell'adenoipofisi, viene tagliata in ACTH, β-lipotropina, γ-MSH e α-MSH. L'α-MSH ha un ruolo nel controllo dell'appetito.")

# ── Difetti amminoacidici, folato e B12, anemie (p. 259–272) ───────────────
C = "m8-difetti"

q("u1127-129", C, "m", "260", "Quali difetti possono causare fenilchetonuria secondo la sbobina?", [
  "Della fenilalanina idrossilasi, della sintesi di BH₄ o della diidrobiopterina reduttasi",
  "Della tirosinasi, della sintesi di melanina o della dopamina β-idrossilasi",
  "Dell'omogentisato diossigenasi, della fumarilacetoacetasi o della tirosina transaminasi",
  "Della deidrogenasi degli α-chetoacidi ramificati, della E3 o della tiamina",
  "Del trasportatore intestinale degli amminoacidi neutri o di quello renale",
  ], 0,
  "La reazione fenilalanina → tirosina richiede l'idrossilasi, la tetraidrobiopterina e la sua rigenerazione da parte della reduttasi (NADPH). La causa più frequente è il deficit dell'idrossilasi.")

q("u1127-130", C, "a", "261", "Perché la dieta povera di fenilalanina nella PKU va mantenuta per tutta la vita?", [
  "Anche a cervello formato, un aumento di fenilalanina abbassa il quoziente intellettivo",
  "Dopo l'infanzia l'enzima si riattiva da solo, ma solo se la dieta resta ben controllata",
  "Serve a evitare l'accumulo di omogentisato nelle articolazioni dell'adulto",
  "Il fegato adulto non sintetizza più tirosina e senza dieta si sviluppa albinismo",
  "La fenilalanina in eccesso blocca la sintesi di urea e dà iperammoniemia",
  ], 0,
  "Si è visto che anche dopo lo sviluppo cerebrale completo un aumento della fenilalanina riduce il QI: la dieta, con una quota di fenilalanina non accumulabile, è a vita.")

q("u1127-131", C, "m", "259", "Come si tratta la malattia di Hartnup secondo la sbobina?", [
  "Con nicotinammide, perché manca la niacina formata dal triptofano",
  "Con una dieta povera di triptofano, perché si accumula nel sangue",
  "Con vitamina B6, perché serve a riassorbire gli amminoacidi neutri",
  "Con cisteina, perché il difetto riguarda il trasporto della cistina",
  "Con tetraidrobiopterina, perché il difetto blocca l'idrossilazione",
  ], 0,
  "Nella Hartnup manca il trasportatore intestinale e renale degli amminoacidi neutri: si assorbe poco triptofano, da cui si forma una parte della niacina, e i sintomi ricordano la pellagra. Si somministra nicotinammide.")

q("u1127-132", C, "l", "261", "Quale enzima manca nell'alcaptonuria?", [
  "Omogentisato 1,2-diossigenasi",
  "Fenilalanina idrossilasi",
  "Tirosina transaminasi",
  "Fumarilacetoacetato idrolasi",
  "Diidrobiopterina reduttasi",
  ], 0,
  "Nella via di degradazione della fenilalanina, il deficit di omogentisato 1,2-diossigenasi fa accumulare omogentisato: urine scure e, col tempo, artrite delle grandi articolazioni.")

C = "m8-folato"

q("u1127-133", C, "l", "271", "Per quanto tempo le riserve epatiche possono coprire il fabbisogno di vitamina B12, secondo la sbobina?", [
  "Circa tre anni",
  "Circa tre settimane",
  "Circa tre mesi",
  "Circa tre giorni",
  "Non esistono riserve di B12",
  ], 0,
  "Il fabbisogno è di pochi microgrammi al giorno e la B12 è trattenuta fortemente nelle cellule e riassorbita a livello intestinale: le riserve del fegato bastano per circa tre anni.")

q("u1127-134", C, "a", "263", "Perché l'acido folico va assunto con la dieta, anche se la sua pteridina somiglia alla biopterina che sintetizziamo?", [
  "Non sappiamo sintetizzare il PABA, con il suo anello aromatico",
  "Non sappiamo unire il glutammato alla pteridina con un legame peptidico",
  "Non sappiamo ridurre il folato a tetraidrofolato senza la flora intestinale",
  "Non sappiamo trattenere il folato nelle cellule senza assumerlo di continuo",
  "Non sappiamo formare l'anello pteridinico, che è solo vegetale",
  ], 0,
  "Piante e batteri sintetizzano l'acido p-amminobenzoico; noi no, perché non sappiamo formare quell'anello aromatico. Per questo i sulfamidici, che bloccano la sintesi batterica del PABA, non colpiscono le nostre cellule.")

q("u1127-135", C, "h", "270", "Un paziente ha omocisteina alta per la variante alanina → valina della metilen-THF reduttasi. Perché la supplementazione di folato può aiutarlo?", [
  "Il folato stabilizza il legame del FAD all'enzima mutato, che torna più efficiente",
  "Il folato sostituisce la vitamina B12 nella reazione della metionina sintasi",
  "Il folato attiva la cistationina β-sintasi e smaltisce l'omocisteina in cisteina",
  "Il folato inibisce la metionina adenosiltransferasi e riduce la formazione di omocisteina",
  "Il folato rende reversibile la reazione della reduttasi e libera il THF intrappolato",
  ], 0,
  "La mutazione (presente in circa il 47% della popolazione) aumenta la dissociazione del FAD e rende l'enzima meno efficiente; un apporto maggiore di folato ne ripristina le caratteristiche. La reazione resta irreversibile.")

q("u1127-136", C, "a", "272", "Perché le infezioni croniche causano anemia, secondo la sbobina?", [
  "L'IL-6 fa salire l'epcidina, che trattiene il ferro nei depositi, e cala l'eritropoietina",
  "L'IL-6 inibisce la metionina sintasi e causa una carenza funzionale di folato nel midollo",
  "I batteri consumano la vitamina B12 intestinale e manca la sintesi del DNA",
  "L'infiammazione distrugge il fattore intrinseco e la B12 non viene assorbita",
  "L'IL-6 blocca la glucosio 6-fosfato deidrogenasi e i globuli rossi si rompono",
  ], 0,
  "Nell'infiammazione cronica l'IL-6 aumenta l'epcidina (il ferro resta nei depositi e non arriva al midollo) e diminuisce l'EPO. Anche l'insufficienza renale riduce l'EPO.")

C = "m8-vie"

q("u1127-137", C, "m", "275", "Come si forma la melatonina dalla serotonina?", [
  "Acetilazione con acetil-CoA e poi metilazione con la S-adenosilmetionina",
  "Idrossilazione con BH₄ e poi decarbossilazione con il PLP",
  "Metilazione con il metil-THF e poi ossidazione con una monoamminossidasi",
  "Transaminazione con l'α-chetoglutarato e poi riduzione con NADPH",
  "Decarbossilazione con il PLP e poi acetilazione con acetil-CoA",
  ], 0,
  "La serotonina acetiltransferasi la acetila (acetilserotonina), poi la SAM dona un metile: si forma la melatonina, prodotta dall'epifisi soprattutto al buio.")

q("u1127-138", C, "f", "275", "Dove si produce la melatonina e quando aumenta?", [
  "Nell'epifisi, con il buio",
  "Nell'ipofisi, con la luce",
  "Nella retina, durante il giorno",
  "Nel surrene, durante lo stress",
  "Nelle piastrine, dopo i pasti",
  ], 0,
  "La melatonina è prodotta dalla ghiandola pineale (epifisi), aumenta con il buio e regola il ritmo sonno-veglia.")

q("u1127-139", C, "a", "276", "Perché la creatina chinasi del muscolo si trova vicino ai mitocondri?", [
  "Usa subito l'ATP appena uscito dalla traslocasi per fosforilare la creatina",
  "Fosforila l'ADP nella matrice per alimentare direttamente l'ATP sintasi",
  "Trasporta la creatina nella matrice mitocondriale, dove viene ossidata a CO₂",
  "Cede il fosfato al citocromo c e accelera la catena respiratoria",
  "Lega la fosfocreatina alla membrana interna per tenerla di riserva",
  ], 0,
  "La creatina chinasi, la chinasi più abbondante vicino ai mitocondri nel muscolo, capta l'ATP appena esportato dalla traslocasi e forma fosfocreatina, il primo donatore di fosfati ad alta energia.")

q("u1127-140", C, "l", "274", "Perché alcuni lavori collegano la vitamina D alla depressione, secondo la sbobina?", [
  "Controlla la sintesi di un enzima della via che forma la serotonina",
  "È il precursore diretto della serotonina nei neuroni del rafe",
  "Inibisce la monoamminossidasi e alza le catecolammine cerebrali",
  "Serve come coenzima alla triptofano idrossilasi al posto della BH₄ nel cervello",
  "Si lega ai recettori della serotonina e ne imita l'effetto",
  ], 0,
  "La sintesi di un enzima della via della serotonina (dal triptofano) è sotto il controllo della vitamina D; una carenza potrebbe ridurre la serotonina. La sbobina lo presenta come ipotesi.")
