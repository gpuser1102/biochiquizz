"""Blocco 7 – Metabolismo dei lipidi (sbobina di Biochimica II, p. 171–225)."""
from bank_common import q

# ── Digestione dei lipidi, bile, sali biliari, bilirubina (p. 171–175) ──────────
T = "m7-digestione"
q("m7d-01", T, "f", "172", "Dove avviene la digestione dei trigliceridi della dieta?", [
  "Nell'intestino tenue, a opera della lipasi pancreatica",
  "Soprattutto nello stomaco, a opera della lipasi gastrica acida",
  "Nella bocca, a opera della lipasi linguale e salivare",
  "Nel fegato, dopo l'assorbimento come trigliceridi intatti",
  "Nel colon, a opera delle lipasi dei batteri intestinali",
  ], 0,
  "La piccola digestione gastrica è trascurabile: la lipasi pancreatica agisce nel duodeno, con l'aiuto della bile.")
q("m7d-02", T, "f", "172", "Che cosa producono la lipasi pancreatica a partire da un trigliceride?", [
  "Due acidi grassi e un 2-monoacilglicerolo",
  "Tre acidi grassi e una molecola di glicerolo",
  "Un acido grasso e un 1,2-diacilglicerolo",
  "Due acidi grassi e un glicerolo 3-fosfato",
  "Un acil-CoA e un 2-monoacilglicerolo",
  ], 0,
  "Taglia i due acidi grassi periferici (posizioni 1 e 3); il monoacilglicerolo e gli acidi grassi entrano nell'enterocita, dove il trigliceride viene ricostituito.")
q("m7d-03", T, "f", "172", "Quale residuo si trova nel sito attivo della lipasi pancreatica?", [
  "Serina", "Cisteina", "Aspartato", "Lisina", "Tirosina"], 0,
  "È un'esterasi: come le serin proteasi usa una serina nucleofila (triade Ser-His-Asp).",
  note="La triade Ser-His-Asp non è nominata nella sbobina, che cita solo la serina.")
q("m7d-04", T, "m", "172", "A che cosa serve la colipasi?", [
  "Sposta il coperchio che chiude il sito attivo della lipasi pancreatica",
  "Idrolizza gli esteri del colesterolo che la lipasi pancreatica non riesce a tagliare",
  "Emulsiona i trigliceridi al posto dei sali biliari quando la bile è insufficiente",
  "Attiva la lipasi pancreatica per proteolisi, come la enteropeptidasi con il tripsinogeno",
  "Trasporta i monoacilgliceroli prodotti dalla lipasi dentro l'enterocita",
  ], 0,
  "Prende contatto con l'ambiente idrofobico e trascina il coperchio: l'ansa si sposta e il sito attivo si libera per il trigliceride.")
q("m7d-05", T, "m", "173", "Qual è il precursore dei sali biliari e qual è la reazione limitante della loro sintesi?", [
  "Il colesterolo; l'idrossilazione in 7α, con citocromo P450, NADPH e O₂",
  "Il colesterolo; l'esterificazione in posizione 3 con un acido grasso, a opera dell'ACAT",
  "La bilirubina; la coniugazione con glucuronato",
  "Lo squalene; la ciclizzazione a lanosterolo, che richiede NADPH e ossigeno molecolare",
  "Il mevalonato; la fosforilazione in posizione 5, che consuma ATP e richiede magnesio",
  ], 0,
  "La colesterolo 7α-idrossilasi (CYP7A1) è un citocromo P450. Poi si formano acido colico (OH in 7 e 12) e chenodeossicolico (OH in 7).",
  note="Sbobina di Biochimica II, p. 173: l'enzima è chiamato «colesterolo 7-α idrolasi». Il nome corretto è colesterolo 7α-idrossilasi: aggiunge un OH, non idrolizza.")
q("m7d-06", T, "m", "173–174", "Che cosa distingue un sale biliare secondario da uno primario?", [
  "I batteri intestinali hanno rimosso l'OH in posizione 7",
  "Il fegato lo ha coniugato con taurina invece che con glicina",
  "Il fegato vi ha aggiunto un OH in più, in posizione 12",
  "L'enterocita lo ha esterificato con un acido grasso",
  "I batteri lo hanno coniugato con acido glucuronico",
  ], 0,
  "I primari (colico, chenodeossicolico) li fa il fegato; i secondari si formano nell'intestino per azione batterica e in parte tornano al fegato con il circolo portale.")
q("m7d-07", T, "m", "174–175", "Come si passa dall'eme alla bilirubina?", [
  "Eme → biliverdina (con liberazione di CO e Fe) → bilirubina per riduzione",
  "Eme → bilirubina per ossidazione → biliverdina per coniugazione nel fegato",
  "Eme → protoporfirina per perdita del ferro → bilirubina per riduzione con NADH",
  "Eme → biliverdina per riduzione → bilirubina per coniugazione con glucuronato",
  "Eme → urobilinogeno nella milza → bilirubina per ossidazione nel fegato",
  ], 0,
  "L'eme ossigenasi apre l'anello liberando CO e ferro e formando biliverdina; la biliverdina reduttasi la riduce a bilirubina, che va al fegato legata all'albumina.",
  note="Sbobina di Biochimica II, p. 175: l'enzima è chiamato «bilirubina reduttasi». Si chiama biliverdina reduttasi, perché il suo substrato è la biliverdina. Il nome dell'eme ossigenasi non è nella sbobina.")
q("m7d-08", T, "a", "175", "Un paziente con grave insufficienza epatica sviluppa edemi. Quale funzione del fegato descritta nella sbobina spiega il sintomo?", [
  "La sintesi dell'albumina, che mantiene la pressione oncotica del plasma",
  "La coniugazione della bilirubina, che altrimenti richiama acqua nei tessuti",
  "La sintesi dei sali biliari, che mantengono l'acqua nel lume intestinale",
  "La produzione di VLDL, che trasportano acqua insieme ai trigliceridi",
  "La gluconeogenesi, perché l'ipoglicemia riduce la pressione osmotica",
  ], 0,
  "L'albumina è la proteina più abbondante del siero: regola la pressione oncotica e trasporta sostanze idrofobiche (bilirubina, acidi grassi).")
q("m7d-09", T, "a", "172–175", "Una ostruzione completa delle vie biliari altera soprattutto:", [
  "La digestione dei grassi, perché senza sali biliari la lipasi lavora male",
  "La digestione delle proteine, perché manca la tripsina",
  "L'assorbimento del glucosio, perché la bile fornisce il Na⁺ al trasportatore SGLT1",
  "La digestione dell'amido, perché la bile neutralizza l'acidità che inattiva l'amilasi",
  "L'assorbimento degli amminoacidi, perché la bile solubilizza i dipeptidi idrofobici",
  ], 0,
  "I sali biliari sono detergenti anfipatici: abbassano la tensione superficiale e creano l'interfaccia su cui lavorano lipasi e colipasi. Si perdono anche le vitamine liposolubili.")
q("m7d-10", T, "l", "173", "Come si chiama il sale biliare formato dall'acido colico coniugato con la glicina?", [
  "Acido glicocolico", "Acido taurocolico", "Acido glicochenodeossicolico", "Acido desossicolico", "Acido litocolico"], 0,
  "Coniugazione con glicina → glico-; con taurina → tauro-. Desossicolico e litocolico sono secondari.")
q("m7d-11", T, "l", "175", "Con che cosa viene coniugata la bilirubina nel fegato?", [
  "Glucuronato", "Glicina", "Taurina", "Glutatione", "Solfato"], 0,
  "La bilirubina coniugata (diglucuronide) è più solubile ed è quella secreta con la bile.")
q("m7d-12", T, "h", "172–175", "Quale affermazione sulla digestione dei lipidi è corretta?", [
  "La lipasi è idrofilica e lavora sull'interfaccia creata dai sali biliari",
  "La lipasi è idrofobica e penetra nelle micelle, mentre i sali biliari ne proteggono il sito attivo",
  "I sali biliari derivano dalla bilirubina e sono riassorbiti quasi tutti come bilirubina coniugata",
  "La colipasi idrolizza gli esteri del colesterolo",
  "I trigliceridi entrano intatti nell'enterocita",
  ], 0,
  "Enzima idrofilico, substrato idrofobico: servono un detergente (sali biliari, dal colesterolo) e la colipasi. Il trigliceride viene ricostituito nell'enterocita.",
  note="Sbobina di Biochimica II, p. 175: attribuisce anche alla bilirubina il ruolo di abbassare la tensione superficiale delle micelle. La bilirubina nella bile è un prodotto di escrezione dell'eme; i detergenti sono i sali biliari (e i fosfolipidi). Non sono sicuro di come sia stato detto a lezione: all'esame attribuisci l'emulsione ai sali biliari.")
q("m7d-13", T, "h", "174", "Secondo la sbobina, perché nell'emoglobina c'è l'istidina distale?", [
  "Per ridurre l'affinità per il CO, prodotto dalla degradazione dell'eme",
  "Per legare il 2,3-bisfosfoglicerato nel canale centrale e stabilizzare la forma T",
  "Per ossidare il ferro a Fe³⁺ e permettere il rilascio dell'O₂ nei tessuti",
  "Per legare la CO₂ come carbammato e trasportarla dai tessuti ai polmoni",
  "Per legare direttamente il ferro dell'eme come quinto ligando di coordinazione",
  ], 0,
  "Il CO lega il ferro con altissima affinità; l'istidina distale impone un legame piegato che ne riduce l'affinità. Il quinto ligando è l'istidina prossimale.")

# ── Trasporto e mobilizzazione (p. 175–180) ─────────────────────────────────
T = "m7-trasporto"
q("m7t-01", T, "f", "175", "Qual è l'apolipoproteina strutturale dei chilomicroni?", [
  "ApoB-48", "ApoB-100", "ApoA-I", "ApoC-II", "ApoE"], 0,
  "ApoB-48 nei chilomicroni (intestino), ApoB-100 in VLDL, IDL e LDL (fegato).")
q("m7t-02", T, "f", "176", "Dove si trova la lipoproteina lipasi?", [
  "Sull'endotelio dei capillari, dal lato del lume",
  "Nel citosol degli adipociti",
  "Nel lume intestinale, secreta dal pancreas insieme alla colipasi",
  "Sulla superficie dei chilomicroni, come apolipoproteina strutturale",
  "Nella matrice mitocondriale degli epatociti, accanto alla CPT II",
  ], 0,
  "È a contatto con il sangue nei capillari di tessuto adiposo, cuore, muscolo e grasso bruno.")
q("m7t-03", T, "f", "179", "Quale proteina trasporta gli acidi grassi liberi nel sangue?", [
  "Albumina", "ApoB-100", "Transferrina", "Ceruloplasmina", "Aptoglobina"], 0,
  "Come la bilirubina, gli acidi grassi sono idrofobici e viaggiano legati all'albumina.")
q("m7t-04", T, "m", "176", "Quale ormone aumenta l'espressione della lipoproteina lipasi nel tessuto adiposo?", [
  "L'insulina, perché dopo il pasto il tessuto adiposo deve accumulare trigliceridi",
  "Il glucagone, perché a digiuno il tessuto adiposo deve liberare acidi grassi per il fegato",
  "L'adrenalina, perché durante lo sforzo il tessuto adiposo deve accumulare trigliceridi",
  "Il cortisolo, perché di notte il tessuto adiposo deve accumulare i trigliceridi delle VLDL",
  "Gli ormoni tiroidei, perché il metabolismo basale richiede più trigliceridi di riserva",
  ], 0,
  "Nel tessuto adiposo l'LPL serve ad accumulare dopo i pasti; in altri distretti (muscolo) sono adrenalina o glucagone ad aumentarla.")
q("m7t-05", T, "m", "178–179", "Nella lipolisi stimolata dalla PKA, quale è la sequenza corretta delle lipasi?", [
  "ATGL (TG → DAG), lipasi ormone-sensibile (DAG → MAG), MGL (MAG → acido grasso + glicerolo)",
  "Lipasi ormone-sensibile (TG → DAG), ATGL (DAG → MAG), MGL (MAG → acido grasso + glicerolo)",
  "Lipoproteina lipasi (TG → DAG), ATGL (DAG → MAG), lipasi ormone-sensibile (MAG → glicerolo)",
  "MGL (TG → DAG), lipasi ormone-sensibile (DAG → MAG), ATGL (MAG → acido grasso + glicerolo)",
  "ATGL (TG → MAG in un solo passaggio), poi lipasi ormone-sensibile (MAG → glicerolo)",
  ], 0,
  "La PKA fosforila le perilipine, che liberano CGI-58: questo attiva l'ATGL. La PKA fosforila e attiva anche la lipasi ormone-sensibile.")
q("m7t-06", T, "m", "178", "Che cosa fanno le perilipine quando la PKA le fosforila?", [
  "Liberano CGI-58, che si lega all'ATGL e la attiva",
  "Si staccano dalla goccia e degradano direttamente i trigliceridi",
  "Legano la lipasi ormone-sensibile e la tengono inattiva",
  "Trasportano gli acidi grassi liberati fino alla membrana",
  "Richiamano i trasportatori CD36 sulla membrana plasmatica",
  ], 0,
  "Non fosforilate tengono legato CGI-58 e proteggono la goccia lipidica; fosforilate lo liberano.")
q("m7t-07", T, "m", "179", "Come agisce un livello basale di catecolammine sui recettori α2 dell'adipocita?", [
  "Attiva una proteina Gi che inibisce l'adenilato ciclasi e frena la lipolisi",
  "Attiva una proteina Gs che stimola l'adenilato ciclasi e avvia la lipolisi",
  "Attiva la fosfolipasi C e libera Ca²⁺, che stimola la lipasi ormone-sensibile",
  "Attiva la PKB, che fosforila e attiva la fosfodiesterasi del cAMP",
  "Non ha effetto: gli α2 rispondono solo a concentrazioni molto alte",
  ], 0,
  "Il tono catecolaminergico basale blocca la lipolisi; quando l'adrenalina sale prevalgono i recettori β (Gs).")
q("m7t-08", T, "a", "177", "Che fine fa il glicerolo liberato dalla lipoproteina lipasi, di giorno e di notte?", [
  "Va al fegato: di giorno fa trigliceridi, di notte entra in gluconeogenesi",
  "Entra nell'adipocita: di giorno forma trigliceridi, di notte viene ossidato a CO₂",
  "Va al muscolo: di giorno entra nella glicolisi, di notte forma corpi chetonici",
  "Va al fegato: di giorno entra nella gluconeogenesi, di notte forma trigliceridi",
  "Resta nel plasma e viene eliminato con le urine sia di giorno sia di notte",
  ], 0,
  "L'adipocita non ha glicerolo chinasi; nel fegato il glicerolo 3-P va dove decide l'assetto insulina/glucagone.")
q("m7t-09", T, "a", "179", "Perché il trasportatore CD36 viene paragonato al GLUT4?", [
  "Sta in vescicole e va in membrana su stimolo di insulina o adrenalina",
  "Trasporta gli acidi grassi in simporto con il Na⁺",
  "È espresso solo nel fegato e lavora con una Km molto alta per gli acidi grassi",
  "È inibito dal suo prodotto, l'acil-CoA, come l'esochinasi dal glucosio 6-fosfato",
  "Trasporta gli acidi grassi già legati al CoA, come il GLUT4 il glucosio 6-fosfato",
  ], 0,
  "Muscolo, cuore e tessuto adiposo: le vescicole si fondono con la membrana su segnale ormonale. Il flip-flop spontaneo è troppo lento per i flussi necessari.")
q("m7t-10", T, "a", "176", "Un deficit di lipoproteina lipasi causa:", [
  "Ipertrigliceridemia, perché chilomicroni e VLDL non si svuotano",
  "Ipercolesterolemia isolata, perché le LDL non vengono captate dal fegato",
  "Ipoglicemia a digiuno, perché manca il glicerolo per la gluconeogenesi",
  "Steatorrea, perché i trigliceridi della dieta non vengono digeriti",
  "Chetoacidosi, perché gli acidi grassi liberi aumentano nel fegato",
  ], 0,
  "I trigliceridi ristagnano nelle lipoproteine circolanti. La steatorrea è invece tipica del deficit di lipasi pancreatica o di bile.")
q("m7t-11", T, "l", "178", "Come si chiama la lipasi che avvia la lipolisi del trigliceride nell'adipocita?", [
  "ATGL", "HSL", "MGL", "LPL", "HL"], 0,
  "ATGL: TG → DAG; HSL: DAG → MAG; MGL: MAG → acido grasso + glicerolo.")
q("m7t-12", T, "h", "178–180", "Di notte il glucagone attiva la lipolisi. Quale effetto contemporaneo sul fegato è coerente?", [
  "Abbassa il fruttosio 2,6-bisfosfato e inattiva la piruvato chinasi L: il glicerolo fa glucosio",
  "Alza il fruttosio 2,6-bisfosfato e attiva la piruvato chinasi L, così il glicerolo va in glicolisi",
  "Attiva l'acetil-CoA carbossilasi, così gli acidi grassi in arrivo vengono riesterificati",
  "Inibisce la glicerolo chinasi, così il glicerolo resta nel sangue fino al mattino",
  "Attiva la lipoproteina lipasi epatica, così il fegato capta i trigliceridi delle VLDL",
  ], 0,
  "Mentre libera acidi grassi e glicerolo dall'adipocita, il glucagone spegne la glicolisi epatica: il glicerolo diventa glucosio, gli acidi grassi corpi chetonici.")
q("m7t-13", T, "h", "177", "Che cosa resta nei residui dei chilomicroni che arrivano al fegato?", [
  "Colesterolo della dieta e vitamine liposolubili",
  "Trigliceridi intatti e acidi grassi a catena corta",
  "Glicerolo e monoacilgliceroli non assorbiti dall'adipe",
  "Apolipoproteina B-100 e colesterolo neosintetizzato",
  "Fosfolipidi e sali biliari riassorbiti nell'ileo",
  ], 0,
  "L'LPL ha tolto gran parte dei trigliceridi; il fegato riconosce i residui tramite ApoE e trattiene il colesterolo alimentare.")

# ── β-ossidazione (p. 181–189) ──────────────────────────────────────────────
T = "m7-betaox"
q("m7b-01", T, "f", "181", "Dove avviene la β-ossidazione degli acidi grassi?", [
  "Nella matrice mitocondriale", "Nel citosol", "Nel reticolo endoplasmatico liscio", "Nello spazio intermembrana", "Nel nucleo"], 0,
  "È un catabolismo ossidativo: avviene nella matrice, dopo il trasporto con la carnitina.")
q("m7b-02", T, "f", "183–184", "Quale è l'ordine delle quattro reazioni di un giro di β-ossidazione?", [
  "Deidrogenazione (FAD) → idratazione → deidrogenazione (NAD⁺) → tiolisi",
  "Deidrogenazione (NAD⁺) → idratazione → deidrogenazione (FAD) → tiolisi",
  "Idratazione → deidrogenazione (FAD) → deidrogenazione (NAD⁺) → tiolisi",
  "Tiolisi → deidrogenazione (FAD) → idratazione → deidrogenazione (NAD⁺)",
  "Deidrogenazione (FAD) → deidrogenazione (NAD⁺) → idratazione → tiolisi",
  ], 0,
  "Acil-CoA → trans-Δ²-enoil-CoA → L-β-idrossiacil-CoA → β-chetoacil-CoA → acetil-CoA + acil-CoA (n−2). Come succinato → fumarato → malato → ossalacetato.")
q("m7b-03", T, "f", "182", "Che cosa serve per far entrare l'acil-CoA nella matrice mitocondriale?", [
  "La carnitina", "La biotina", "L'acido lipoico", "La creatina", "La taurina"], 0,
  "CPT I (esterna) forma acil-carnitina, la traslocasi la porta dentro, la CPT II riforma l'acil-CoA.")
q("m7b-04", T, "m", "181–182", "Come viene attivato un acido grasso prima della β-ossidazione?", [
  "Con ATP e CoA si forma acil-CoA; escono AMP + PPi: costa due legami ad alta energia",
  "Con ATP e CoA si forma acil-CoA; si libera ADP + Pi, quindi costa un legame ad alta energia",
  "Con GTP e carnitina si forma acil-carnitina; si libera GDP, quindi costa un legame",
  "Con NAD⁺ e CoA si forma acil-CoA per ossidazione, senza consumo di ATP",
  "Con biotina e bicarbonato si forma malonil-CoA, consumando un ATP",
  ], 0,
  "Intermedio acil-adenilato legato all'enzima, poi tioestere con il CoA; l'idrolisi del PPi rende la reazione irreversibile.",
  note="Sbobina di Biochimica II, p. 181: l'enzima è chiamato «Acetil-CoA sintetasi». Quello che attiva gli acidi grassi è l'acil-CoA sintetasi (tiochinasi).")
q("m7b-05", T, "m", "184", "Dove finiscono gli elettroni del FADH₂ dell'acil-CoA deidrogenasi?", [
  "Passano all'ETF, a una ferro-zolfo proteina e poi al coenzima Q",
  "Passano al NAD⁺ della matrice e poi entrano nel complesso I",
  "Passano direttamente al citocromo c senza toccare il coenzima Q",
  "Passano all'O₂ formando acqua ossigenata, poi demolita dalla catalasi",
  "Passano al complesso II, che li cede direttamente al complesso IV",
  ], 0,
  "Come succinato deidrogenasi e glicerolo 3-P deidrogenasi mitocondriale, l'acil-CoA deidrogenasi cede elettroni al CoQ (circa 1,5 ATP).")
q("m7b-06", T, "m", "186", "Come viene completata la degradazione di un acido grasso a numero dispari di atomi di carbonio?", [
  "Il propionil-CoA residuo viene carbossilato e convertito in succinil-CoA",
  "Il propionil-CoA residuo viene ossidato a lattato e usato dalla gluconeogenesi nel fegato",
  "Il propionil-CoA residuo viene decarbossilato ad acetil-CoA dalla piruvato deidrogenasi",
  "Il malonil-CoA residuo viene idrolizzato ad acetato e CO₂ dalla tioesterasi mitocondriale",
  "Il frammento a tre atomi viene eliminato con le urine",
  ], 0,
  "Propionil-CoA carbossilasi (biotina) → D-metilmalonil-CoA → epimerasi → L-metilmalonil-CoA → mutasi (B12) → succinil-CoA.")
q("m7b-07", T, "m", "188", "Che cosa ha di diverso il primo enzima della β-ossidazione perossisomiale?", [
  "È un'acil-CoA ossidasi: il FADH₂ cede gli elettroni direttamente all'O₂ e si forma H₂O₂",
  "È un'acil-CoA deidrogenasi a NAD⁺: il NADH viene riossidato dalla catena respiratoria",
  "È un'acil-CoA idratasi che non richiede coenzimi e lavora solo su acidi grassi insaturi",
  "È una tiolasi a biotina che accorcia gli acidi grassi di tre atomi di carbonio per volta",
  "È un'acil-CoA ossidasi che cede gli elettroni al citocromo b5 del reticolo endoplasmatico",
  ], 0,
  "Nel perossisoma non c'è catena respiratoria: l'O₂ riossida il FAD, la catalasi demolisce l'H₂O₂. Si perdono circa 1,5 ATP per ogni giro.")
q("m7b-08", T, "a", "185–186", "Quanti ATP netti si ottengono dall'ossidazione completa del palmitato secondo la sbobina?", [
  "106: 108 dal palmitoil-CoA meno 2 per l'attivazione",
  "108: l'attivazione costa un solo ATP, già sottratto",
  "129: 131 dal palmitoil-CoA meno 2 per l'attivazione",
  "104: 108 dal palmitoil-CoA meno 4 per l'attivazione",
  "80: solo gli 8 acetil-CoA producono ATP nel ciclo",
  ], 0,
  "7 FADH₂ × 1,5 = 10,5; 7 NADH × 2,5 = 17,5; 8 acetil-CoA × 10 = 80 → 108; l'attivazione rompe due legami fosfoanidridici → 106. Il 129 è il vecchio conteggio con 3 e 2 ATP.")
q("m7b-09", T, "a", "185", "Un bambino con deficit di MCAD dopo un digiuno prolungato presenta:", [
  "Ipoglicemia con pochi corpi chetonici, perché i tessuti consumano più glucosio",
  "Iperglicemia con chetoacidosi, perché gli acidi grassi si accumulano e diventano corpi chetonici",
  "Ipoglicemia con molti corpi chetonici, perché il fegato li produce dagli acidi grassi a catena media",
  "Glicemia normale, perché le altre isoforme compensano",
  "Iperammoniemia isolata, perché gli acidi grassi a catena media inibiscono il ciclo dell'urea",
  ], 0,
  "Senza β-ossidazione mancano acetil-CoA per i corpi chetonici ed energia per la gluconeogenesi; i tessuti consumano glucosio. Si accumulano ottanoato e grasso nel fegato.",
  note="La sbobina cita ipoglicemia, sonnolenza, vomito e coma; il fatto che i corpi chetonici siano bassi (ipoglicemia ipochetotica) non è detto esplicitamente.")
q("m7b-10", T, "a", "186–187", "Per ossidare l'oleoil-CoA (cis-Δ⁹), quale enzima in più serve rispetto a un acido grasso saturo?", [
  "Un'isomerasi che sposta il doppio legame cis-Δ³ in trans-Δ²",
  "La 2,4-dienoil-CoA reduttasi (NADPH)",
  "La propionil-CoA carbossilasi, che carbossila il frammento a tre atomi",
  "La metilmalonil-CoA mutasi, che richiede la vitamina B12 come coenzima",
  "L'acil-CoA ossidasi perossisomiale, che forma H₂O₂ al posto del FADH₂",
  ], 0,
  "Per un monoinsaturo basta l'isomerasi; la 2,4-dienoil-CoA reduttasi (NADPH) serve per i polinsaturi.")
q("m7b-11", T, "a", "181", "Perché la β-ossidazione nel muscolo procede solo se c'è anche un po' di catabolismo del glucosio?", [
  "Perché l'acetil-CoA ha bisogno di ossalacetato, che deriva dal piruvato",
  "Perché la carnitina viene sintetizzata a partire da intermedi della glicolisi muscolare",
  "Perché l'acil-CoA sintetasi usa come substrato il fosfoenolpiruvato invece dell'ATP",
  "Perché il FADH₂ della β-ossidazione viene riossidato dalla lattato deidrogenasi",
  "Perché la glicolisi produce il NADPH necessario all'acil-CoA deidrogenasi",
  ], 0,
  "Il piruvato fornisce ossalacetato tramite la piruvato carbossilasi (anaplerosi): senza ossalacetato l'acetil-CoA non viene ossidato.")
q("m7b-12", T, "l", "183", "Come si chiama l'enzima che catalizza l'idratazione nella β-ossidazione?", [
  "Enoil-CoA idratasi", "Fumarasi", "Aconitasi", "β-idrossiacil-CoA deidratasi", "Crotonasi dell'ACP"], 0,
  "Forma L-β-idrossiacil-CoA dal trans-Δ²-enoil-CoA (è chiamata anche crotonasi).")
q("m7b-13", T, "l", "186", "Che cosa catalizza la metilmalonil-CoA mutasi e quale coenzima usa?", [
  "L-metilmalonil-CoA → succinil-CoA; 5'-deossiadenosilcobalamina (B12)",
  "D-metilmalonil-CoA → L-metilmalonil-CoA; biotina legata a una lisina",
  "Propionil-CoA → D-metilmalonil-CoA; biotina, ATP e bicarbonato",
  "Succinil-CoA → succinato; GDP e fosfato inorganico",
  "L-metilmalonil-CoA → propionil-CoA; tiamina pirofosfato",
  ], 0,
  "Il cobalto genera un radicale 5'-deossiadenosilico che riarrangia lo scheletro carbonioso.")
q("m7b-14", T, "l", "189", "Quale malattia è dovuta al mancato assemblaggio dei perossisomi?", [
  "Sindrome di Zellweger", "Malattia di Tangier", "Deficit di MCAD", "Sindrome di Lesch-Nyhan", "Malattia di von Gierke"], 0,
  "Difetti di migrazione neuronale, dismorfismi craniofacciali, ipotonia, convulsioni e disfunzione epatica; si accumulano VLCFA e acidi grassi ramificati.")
q("m7b-15", T, "h", "182–183", "Quale coppia «enzima – posizione» del sistema della carnitina è corretta?", [
  "CPT I sulla membrana esterna; CPT II sulla membrana interna, lato matrice",
  "CPT I nella matrice; CPT II sulla membrana mitocondriale esterna, rivolta verso il citosol",
  "CPT I nel citosol, libera; CPT II nello spazio intermembrana, libera",
  "CPT I e CPT II entrambe sulla membrana esterna, una per l'ingresso e una per l'uscita",
  "CPT I sulla membrana interna; la traslocasi sulla membrana esterna, con la CPT II",
  ], 0,
  "La CPT I (bersaglio del malonil-CoA) forma acil-carnitina; la traslocasi scambia acil-carnitina e carnitina; la CPT II riforma l'acil-CoA nella matrice.")
q("m7b-16", T, "h", "181", "La sbobina indica la quantità di NADH mitocondriale come regolatore principale della β-ossidazione. Quale altro regolatore, descritto più avanti nella sbobina, blocca l'ingresso degli acidi grassi nel mitocondrio?", [
  "Il malonil-CoA, che inibisce la carnitina aciltrasferasi I",
  "Il citrato, che inibisce la carnitina aciltrasferasi II",
  "L'acetil-CoA, che inibisce la carnitina-acilcarnitina traslocasi",
  "L'AMP, che inibisce l'acil-CoA sintetasi della membrana esterna",
  "Il palmitoil-CoA, che inibisce l'enoil-CoA idratasi nella matrice",
  ], 0,
  "Quando si sintetizzano acidi grassi, il malonil-CoA impedisce che vengano subito ossidati.",
  note="Sbobina di Biochimica II, p. 181: indica come livello principale di regolazione la quantità di NADH. Nel Lehninger il punto di controllo principale è la CPT I, inibita dal malonil-CoA (che la sbobina descrive a p. 203). Anche NADH/NAD⁺ e acetil-CoA/CoA alti rallentano le deidrogenasi e la tiolasi.")

# ── Corpi chetonici (p. 189–192) ────────────────────────────────────────────
T = "m7-chetoni"
q("m7k-01", T, "f", "189", "Quale organo produce i corpi chetonici?", [
  "Solo il fegato", "Fegato e cervello", "Il muscolo scheletrico", "Il rene e il cuore", "Il tessuto adiposo"], 0,
  "Il fegato li produce e li distribuisce, ma non li usa perché non ha la β-chetoacil-CoA transferasi.")
q("m7k-02", T, "f", "190", "Quali sono i due corpi chetonici usati come fonte di energia?", [
  "Acetoacetato e β-idrossibutirrato", "Acetone e acetoacetato", "Acetone e β-idrossibutirrato", "Acetoacetil-CoA e HMG-CoA", "Acetato e propionato"], 0,
  "L'acetone si forma per decarbossilazione dell'acetoacetato, è volatile e viene espirato: non serve per l'energia.")
q("m7k-03", T, "m", "189", "Perché di notte l'acetil-CoA epatico va verso i corpi chetonici invece che nel ciclo di Krebs?", [
  "Perché l'ossalacetato è usato dalla gluconeogenesi e manca per il citrato",
  "Perché il glucagone inibisce la citrato sintasi fosforilandola tramite la PKA",
  "Perché di notte il fegato non ha mitocondri attivi e lavora solo in anaerobiosi",
  "Perché l'acetil-CoA della β-ossidazione è nel citosol, lontano dal ciclo di Krebs",
  "Perché i corpi chetonici producono più ATP nel fegato del ciclo di Krebs",
  ], 0,
  "L'ossalacetato diventa malato → PEP. Lo stesso accade nel diabete non trattato, dove il fegato continua a fare gluconeogenesi.")
q("m7k-04", T, "m", "190", "Qual è la sequenza della chetogenesi?", [
  "2 acetil-CoA → acetoacetil-CoA → HMG-CoA → acetoacetato → β-idrossibutirrato",
  "2 acetil-CoA → acetoacetato → acetoacetil-CoA → HMG-CoA → β-idrossibutirrato",
  "Acetil-CoA → malonil-CoA → acetoacetil-CoA → acetoacetato → β-idrossibutirrato",
  "3 acetil-CoA → mevalonato → HMG-CoA → acetoacetato → β-idrossibutirrato",
  "2 acetil-CoA → HMG-CoA → acetoacetil-CoA → acetone → β-idrossibutirrato",
  ], 0,
  "HMG-CoA sintasi aggiunge il terzo acetil-CoA, HMG-CoA liasi lo toglie liberando acetoacetato; la β-idrossibutirrato deidrogenasi lo riduce con NADH.")
q("m7k-05", T, "m", "191", "Perché il fegato non può usare i corpi chetonici che produce?", [
  "Perché non ha la β-chetoacil-CoA transferasi, che attiva l'acetoacetato",
  "Perché non ha la tiolasi, che scinde l'acetoacetil-CoA in due molecole di acetil-CoA",
  "Perché non ha il trasportatore dei monocarbossilati e non può riassorbirli dal sangue",
  "Perché non ha la β-idrossibutirrato deidrogenasi e non può riossidarli ad acetoacetato",
  "Perché li trasforma subito in colesterolo",
  ], 0,
  "Nei tessuti periferici: acetoacetato + succinil-CoA → acetoacetil-CoA + succinato; la tiolasi dà 2 acetil-CoA.")
q("m7k-06", T, "a", "191", "Perché la produzione notturna di corpi chetonici tende ad acidificare il sangue?", [
  "Sono acidi monocarbossilici ed escono dall'epatocita insieme a un H⁺",
  "Sono basi deboli che sottraggono bicarbonato al plasma quando vengono trasportate",
  "La loro produzione consuma CO₂ e sposta l'equilibrio del tampone bicarbonato",
  "Il β-idrossibutirrato viene convertito in acido lattico nei globuli rossi",
  "L'acetone espirato porta via ioni bicarbonato attraverso i polmoni",
  ], 0,
  "Come il lattato: trasporto elettroneutro con un protone. In eccesso (diabete di tipo 1) si arriva alla chetoacidosi.")
q("m7k-07", T, "a", "189", "Perché la gluconeogenesi si riduce drasticamente intorno al quarto giorno di digiuno?", [
  "Perché il cervello usa più corpi chetonici e si risparmiano le proteine",
  "Perché si esauriscono le scorte di glicogeno epatico necessarie alla gluconeogenesi",
  "Perché il glucagone non viene più secreto dopo tre giorni di digiuno",
  "Perché il fegato perde la piruvato carbossilasi per mancanza di biotina",
  "Perché i corpi chetonici inibiscono direttamente la PEP carbossichinasi",
  ], 0,
  "Il calo del glucosio prodotto viene compensato dall'aumento dei corpi chetonici, soprattutto β-idrossibutirrato.")
q("m7k-08", T, "a", "191", "Quanti ATP rende al neurone una molecola di acetoacetato secondo la sbobina, e quale costo nascosto ha la sua attivazione?", [
  "Circa 20 (due acetil-CoA); per attivarlo si consuma un succinil-CoA, che non forma GTP",
  "Circa 10 (un acetil-CoA); per attivarlo si consumano due ATP come per gli acidi grassi",
  "Circa 20 (due acetil-CoA); l'attivazione non ha alcun costo perché usa CoA libero",
  "Circa 32, come il glucosio; per attivarlo si consuma un NADH nella matrice",
  "Circa 2,5 (un NADH); per attivarlo si consuma un GTP nella matrice",
  ], 0,
  "Il succinil-CoA diventa succinato senza la tiochinasi: si perde il GTP del ciclo di Krebs. Il β-idrossibutirrato rende in più un NADH quando viene riossidato.",
  note="La sbobina dice «20 ATP»; il costo del succinil-CoA non è commentato. La sbobina scrive anche che l'acetoacetato «scambia l'acetil-CoA con il succinil-CoA»: si scambia il CoA.")
q("m7k-09", T, "l", "190", "Quale enzima libera l'acetoacetato dall'HMG-CoA?", [
  "HMG-CoA liasi", "HMG-CoA sintasi", "HMG-CoA reduttasi", "Tiolasi", "Acetoacetato decarbossilasi"], 0,
  "Sintasi: acetoacetil-CoA + acetil-CoA → HMG-CoA. Liasi: HMG-CoA → acetoacetato + acetil-CoA. La reduttasi è del colesterolo.")
q("m7k-10", T, "l", "190", "Quale stereoisomero del β-idrossibutirrato si forma nella chetogenesi?", [
  "D-β-idrossibutirrato", "L-β-idrossibutirrato", "Una miscela racemica", "Meso-β-idrossibutirrato", "L-β-idrossiacil-CoA"], 0,
  "Attenzione: nella β-ossidazione l'intermedio è L-β-idrossiacil-CoA, nella chetogenesi si forma il D-β-idrossibutirrato.")
q("m7k-11", T, "h", "189–191", "In un diabete di tipo 1 non trattato, quale combinazione spiega la chetoacidosi?", [
  "Lipolisi senza freno, gluconeogenesi epatica che consuma ossalacetato, corpi chetonici in eccesso",
  "Lipolisi bloccata dal glucagone, glicolisi epatica attiva, acetil-CoA in eccesso trasformato in corpi chetonici",
  "Lipolisi normale, gluconeogenesi spenta, acetil-CoA ossidato tutto nel ciclo di Krebs epatico",
  "Lipolisi senza freno, citrato sintasi attivata dall'insulina residua, corpi chetonici consumati dal fegato",
  "Lipolisi ridotta, β-ossidazione bloccata dal malonil-CoA, acetone prodotto dal muscolo",
  ], 0,
  "Senza insulina il fegato «crede» di essere a digiuno: gli acidi grassi arrivano in massa e l'ossalacetato va in gluconeogenesi.")
q("m7k-12", T, "h", "190", "Quale passaggio è in comune tra chetogenesi e sintesi del colesterolo, e dove avviene in ciascuna?", [
  "La formazione di HMG-CoA: nel mitocondrio per i corpi chetonici, nel citosol per il colesterolo",
  "La formazione di mevalonato: nel citosol per i corpi chetonici, nel mitocondrio per il colesterolo",
  "La formazione di HMG-CoA: nel citosol per entrambe le vie, sempre negli epatociti",
  "La formazione di malonil-CoA: nel mitocondrio per i corpi chetonici, nel citosol per il colesterolo",
  "La formazione di acetoacetato: nel mitocondrio per entrambe le vie, poi esce come citrato",
  ], 0,
  "Acetil-CoA → acetoacetil-CoA → HMG-CoA. Poi nel mitocondrio la liasi dà acetoacetato; nel citosol la reduttasi dà mevalonato.")

# ── Biosintesi degli acidi grassi (p. 193–204) ──────────────────────────────
T = "m7-biosintesi"
q("m7s-01", T, "f", "193", "Dove avviene la sintesi degli acidi grassi e quale coenzima fornisce il potere riducente?", [
  "Nel citosol, con il NADPH", "Nella matrice mitocondriale, con il NADH", "Nel citosol, con il NADH", "Nel reticolo endoplasmatico, con il FADH₂", "Nella matrice mitocondriale, con il NADPH"], 0,
  "Avviene soprattutto nel fegato dopo i pasti, sotto il controllo dell'insulina.")
q("m7s-02", T, "f", "197", "Qual è il prodotto finale dell'acido grasso sintasi?", [
  "Un acido grasso saturo a 16 atomi di carbonio (palmitato)",
  "Un acido grasso insaturo a 18 atomi di carbonio (oleato)",
  "Un acido grasso saturo a 18 atomi di carbonio (stearato)",
  "Un acido grasso polinsaturo a 18 atomi (linoleato)",
  "Un acido grasso saturo a 14 atomi di carbonio (miristato)",
  ], 0,
  "Allungamenti e desaturazioni avvengono dopo, su altri sistemi enzimatici.",
  note="Sbobina di Biochimica II, p. 197–201: il prodotto è indicato come palmitoil-CoA, ottenuto «aggiungendo un acetil-CoA» nel terzo dominio. Nei testi di riferimento la tioesterasi idrolizza il palmitoil-ACP e libera palmitato; il palmitato viene poi attivato a palmitoil-CoA dall'acil-CoA sintetasi.")
q("m7s-03", T, "f", "195", "Quale coenzima usa l'acetil-CoA carbossilasi?", [
  "Biotina", "Tiamina pirofosfato", "Piridossal fosfato", "Acido lipoico", "Cobalamina"], 0,
  "Acetil-CoA + HCO₃⁻ + ATP → malonil-CoA. Le tre carbossilasi a biotina della sbobina: piruvato carbossilasi, propionil-CoA carbossilasi, acetil-CoA carbossilasi.",
  note="Sbobina di Biochimica II, p. 195: c'è scritto che l'acetil-CoA «subisce una decarbossilazione per formare il malonil-CoA». È una carbossilazione: si aggiunge un carbossile dal bicarbonato.")
q("m7s-04", T, "m", "193–194", "Come arriva l'acetil-CoA mitocondriale nel citosol per la sintesi degli acidi grassi?", [
  "Come citrato, che nel citosol l'ATP-citrato liasi scinde di nuovo",
  "Come acetil-carnitina, con la traslocasi",
  "Come acetil-CoA libero, attraverso un trasportatore specifico della membrana interna",
  "Come acetoacetato, che nel citosol viene riattivato dalla tiolasi citosolica",
  "Come malonil-CoA, prodotto nel mitocondrio dall'acetil-CoA carbossilasi 2",
  ], 0,
  "Il citrato si accumula quando isocitrato e α-chetoglutarato deidrogenasi sono inibite da ATP e NADH alti, cioè dopo i pasti.")
q("m7s-05", T, "m", "195", "Da quali due fonti viene il NADPH citosolico per la sintesi degli acidi grassi?", [
  "Dall'enzima malico e dalla fase ossidativa della via dei pentoso fosfati",
  "Dalla malato deidrogenasi citosolica e dalla gliceraldeide 3-fosfato deidrogenasi",
  "Dall'isocitrato deidrogenasi mitocondriale e dalla piruvato deidrogenasi",
  "Dalla glucosio 6-fosfatasi e dalla glicerolo 3-fosfato deidrogenasi citosolica",
  "Dalla β-ossidazione perossisomiale e dalla catena respiratoria",
  ], 0,
  "L'ossalacetato del citrato diventa malato e poi piruvato con l'enzima malico, che produce NADPH; la via dei pentoso fosfati ne dà 2 per G6P.")
q("m7s-06", T, "m", "195–196", "Come regolano allostericamente l'acetil-CoA carbossilasi il citrato e il palmitoil-CoA?", [
  "Il citrato favorisce la forma polimerica attiva; il palmitoil-CoA i protomeri",
  "Il citrato favorisce la forma protomerica inattiva; il palmitoil-CoA quella polimerica attiva",
  "Entrambi favoriscono la forma polimerica, ma il palmitoil-CoA solo se l'enzima è fosforilato",
  "Il citrato fosforila l'enzima e lo inattiva; il palmitoil-CoA lo defosforila e lo attiva",
  "Il citrato inibisce; il palmitoil-CoA attiva",
  ], 0,
  "Il citrato fa due cose: fornisce il substrato (acetil-CoA) e attiva l'enzima. Il palmitoil-CoA è il prodotto finale della via: retroinibizione.")
q("m7s-07", T, "m", "196–197", "Come agisce l'insulina sull'acetil-CoA carbossilasi?", [
  "La fa defosforilare e la attiva",
  "La fa fosforilare dalla PKA e la attiva",
  "La fa fosforilare dalla PKB e la inattiva",
  "Ne aumenta la degradazione nel proteasoma",
  "La sposta nel mitocondrio dove trova il citrato",
  ], 0,
  "Glucagone e adrenalina la fanno fosforilare e la inattivano. Anche il citrato può riattivare in parte la forma fosforilata.",
  note="Sbobina di Biochimica II, p. 197: nel riepilogo c'è scritto «l'insulina favorisce la defosforilazione/inattivazione». La defosforilazione attiva l'enzima, come la sbobina stessa dice a p. 196.")
q("m7s-08", T, "a", "203", "Perché la cellula non ossida gli acidi grassi mentre li sintetizza?", [
  "Il malonil-CoA inibisce la carnitina aciltrasferasi I",
  "Il palmitoil-CoA inibisce la carnitina-acilcarnitina traslocasi della membrana interna",
  "Il NADPH prodotto dall'enzima malico inibisce l'acil-CoA deidrogenasi mitocondriale",
  "Il citrato attiva la tioesterasi mitocondriale",
  "L'insulina fa degradare la carnitina",
  ], 0,
  "È la regolazione reciproca: il primo prodotto della sintesi blocca l'ingresso degli acili nel mitocondrio.")
q("m7s-09", T, "a", "203", "Il muscolo non sintetizza acidi grassi ma ha l'acetil-CoA carbossilasi 2. A che cosa gli serve?", [
  "A produrre malonil-CoA che frena la β-ossidazione quando c'è energia",
  "A produrre malonil-CoA da allungare in acidi grassi a catena molto lunga per le membrane",
  "A produrre malonil-CoA da cui il muscolo sintetizza i corpi chetonici di notte",
  "A carbossilare il piruvato per rifornire di ossalacetato il ciclo di Krebs",
  "A produrre propionil-CoA per la gluconeogenesi muscolare durante lo sforzo",
  ], 0,
  "Nel muscolo il malonil-CoA è solo un effettore: blocca la CPT I.")
q("m7s-10", T, "a", "203", "Come fa una dieta ricca di carboidrati ad aumentare la quantità di acetil-CoA carbossilasi nel fegato?", [
  "Lo xilulosio 5-P attiva la PP2A, che defosforila ChREBP e lo manda nel nucleo",
  "Il glucosio 6-P si lega direttamente al promotore del gene dell'acetil-CoA carbossilasi",
  "Il fruttosio 2,6-bisfosfato fosforila SREBP, che entra nel nucleo e attiva il gene",
  "Il citrato si lega a ChREBP fosforilato e lo trasporta nel nucleo attraverso i pori",
  "L'insulina fosforila ChREBP tramite la PKB, permettendone l'ingresso nel nucleo",
  ], 0,
  "Molto xilulosio 5-P significa via dei pentoso fosfati attiva, quindi NADPH abbondante: è il momento giusto per sintetizzare acidi grassi.")
q("m7s-11", T, "a", "200–202", "Nell'acido grasso sintasi, dove sono legati il primo acetile e il malonile prima della condensazione?", [
  "L'acetile alla cisteina della KS; il malonile alla fosfopanteteina dell'ACP",
  "L'acetile al –SH della fosfopanteteina dell'ACP; il malonile al –SH di una cisteina della KS",
  "Entrambi a residui di cisteina della KS, uno per subunità del dimero",
  "L'acetile alla biotina della KS; il malonile al CoA libero nel citosol",
  "L'acetile a una serina della tioesterasi; il malonile a una lisina dell'ACP",
  ], 0,
  "La condensazione con perdita di CO₂ forma acetoacetil-ACP; poi riduzione (NADPH), deidratazione, riduzione (NADPH) → butirril-ACP, trasferito alla KS.",
  note="Sbobina di Biochimica II, p. 200: c'è scritto che il malonile si attacca «al residuo di cisteina dell'ACP». Sull'ACP il gruppo tiolico è quello della fosfopanteteina (lo dice la stessa sbobina a p. 199); la cisteina è quella della KS.")
q("m7s-12", T, "l", "202", "Come si chiama l'intermedio insaturo a quattro atomi di carbonio del primo giro di sintesi?", [
  "Crotonil-ACP", "Butirril-ACP", "D-β-idrossibutirril-ACP", "Acetoacetil-ACP", "Malonil-ACP"], 0,
  "Acetoacetil-ACP → (KR, NADPH) D-β-idrossibutirril-ACP → (DH) crotonil-ACP → (ER, NADPH) butirril-ACP.")
q("m7s-13", T, "l", "199", "Che cosa forma il braccio mobile dell'ACP?", [
  "La fosfopanteteina", "La biotina legata a una lisina", "L'acido lipoico legato a una lisina", "Il piridossal fosfato legato a una lisina", "La tiamina pirofosfato"], 0,
  "Lo stesso gruppo del CoA, ma legato a una serina della proteina invece che al 3'-fosfo-ADP.",
  note="Il legame della fosfopanteteina a una serina dell'ACP non è nella sbobina.")
q("m7s-14", T, "l", "204", "Come arrivano gli elettroni del NADPH alla desaturasi del reticolo endoplasmatico?", [
  "NADPH → citocromo b5 reduttasi (FAD) → citocromo b5 → desaturasi",
  "NADPH → FMN del complesso I → coenzima Q → desaturasi (con O₂)",
  "NADPH → citocromo P450 reduttasi → citocromo c → desaturasi (con O₂)",
  "NADPH → glutatione reduttasi → glutatione → desaturasi (con H₂O₂)",
  "NADPH → tioredossina → citocromo b5 → desaturasi (senza ossigeno)",
  ], 0,
  "Sistema microsomiale con O₂. L'uomo non sa inserire doppi legami oltre il C9: linoleico e linolenico sono essenziali.")
q("m7s-15", T, "h", "193–197", "Dopo un pasto ricco di carboidrati, quale insieme di eventi epatici porta alla sintesi di acidi grassi?", [
  "PDH defosforilata, citrato che esce, ATP-citrato liasi e acetil-CoA carbossilasi attive",
  "PDH fosforilata, citrato trattenuto nel mitocondrio, acetil-CoA carbossilasi fosforilata e inattiva",
  "PDH defosforilata, acetil-CoA che esce come acetil-carnitina, acetil-CoA carbossilasi fosforilata",
  "PDH fosforilata, acetil-CoA dai corpi chetonici, ATP-citrato liasi inibita dall'insulina",
  "PDH defosforilata, citrato che inibisce l'acetil-CoA carbossilasi e attiva la β-ossidazione",
  ], 0,
  "L'insulina accende glicolisi, PDH, ATP-citrato liasi e acetil-CoA carbossilasi; ATP e NADH alti bloccano il ciclo di Krebs e fanno uscire il citrato.")
q("m7s-16", T, "h", "202", "Quale confronto tra β-ossidazione e sintesi degli acidi grassi è corretto?", [
  "β-ossidazione: matrice, CoA, FAD e NAD⁺. Sintesi: citosol, ACP, NADPH, malonil-CoA",
  "β-ossidazione: citosol, ACP, NADPH. Sintesi: matrice, CoA, FAD e NAD⁺, acetil-CoA come donatore",
  "β-ossidazione: matrice, ACP, FAD e NAD⁺. Sintesi: citosol, CoA, NADH, malonil-CoA come donatore",
  "β-ossidazione: matrice, CoA, NADPH. Sintesi: citosol, ACP, FAD",
  "β-ossidazione: perossisoma, CoA, NAD⁺. Sintesi: reticolo, ACP, NADPH, acetil-CoA come donatore",
  ], 0,
  "Cambiano compartimento, trasportatore di acili, coenzimi e donatore/prodotto: per questo le due vie possono essere regolate in modo indipendente.")

# ── Trigliceridi e gliceroneogenesi (p. 204–206) ────────────────────────────
T = "m7-tg"
q("m7g-01", T, "f", "204", "Quale intermedio si forma per primo dal glicerolo 3-fosfato nella sintesi dei trigliceridi?", [
  "Fosfatidato", "Diacilglicerolo", "CDP-diacilglicerolo", "Monoacilglicerolo", "Fosfatidilcolina"], 0,
  "Glicerolo 3-P + 2 acil-CoA → fosfatidato → (fosfatidato fosfatasi) diacilglicerolo → + acil-CoA → trigliceride.")
q("m7g-02", T, "f", "205", "In quale lipoproteina il fegato esporta i trigliceridi che sintetizza?", [
  "VLDL", "Chilomicroni", "LDL", "HDL", "IDL"], 0,
  "I chilomicroni portano i trigliceridi della dieta dall'intestino; le VLDL quelli sintetizzati dal fegato.")
q("m7g-03", T, "m", "204", "Quale enzima trasforma il fosfatidato in diacilglicerolo?", [
  "La fosfatidato fosfatasi, che idrolizza il fosfato",
  "La diacilglicerolo chinasi, che trasferisce il fosfato all'ADP",
  "La fosfolipasi C, che libera inositolo 1,4,5-trisfosfato",
  "La glicerolo 3-fosfato deidrogenasi, che riduce il fosfatidato",
  "L'acil-CoA sintetasi, che scambia il fosfato con un acile",
  ], 0,
  "È un punto di incrocio: fosfatidato e diacilglicerolo sono anche secondi messaggeri, per questo l'enzima è finemente regolato.")
q("m7g-04", T, "m", "205", "Perché il tessuto adiposo deve produrre il glicerolo 3-fosfato senza partire dal glicerolo?", [
  "Perché non ha la glicerolo chinasi e lo ricava dal DHAP",
  "Perché il glicerolo non attraversa la membrana dell'adipocita senza insulina",
  "Perché la glicerolo chinasi adiposa è inibita dagli acidi grassi liberi",
  "Perché il glicerolo viene subito ossidato a CO₂ nei mitocondri dell'adipocita",
  "Perché lo riceve già pronto dal fegato",
  ], 0,
  "Il DHAP viene dalla glicolisi oppure dalla gliceroneogenesi; la glicerolo 3-P deidrogenasi lo riduce con NADH.")
q("m7g-05", T, "a", "205–206", "Che cos'è la gliceroneogenesi?", [
  "Una gluconeogenesi abbreviata nell'adipocita, dal piruvato al glicerolo 3-P",
  "La sintesi di glicerolo libero nel fegato a partire dai trigliceridi delle VLDL",
  "La fosforilazione del glicerolo plasmatico da parte della glicerolo chinasi muscolare",
  "La sintesi di glucosio a partire dal glicerolo liberato dalla lipolisi notturna",
  "La conversione del glicerolo 3-P in DHAP per alimentare la glicolisi adiposa",
  ], 0,
  "Serve all'adipocita a riesterificare gli acidi grassi anche a digiuno, quando entra poco glucosio.")
q("m7g-06", T, "a", "206", "Come agisce il cortisolo sulla PEP carbossichinasi nei due tessuti?", [
  "Nel fegato la induce; nel tessuto adiposo la inibisce",
  "Nel fegato la inibisce; nel tessuto adiposo la induce, aumentando la riesterificazione",
  "La induce in entrambi",
  "La inibisce in entrambi i tessuti",
  "Non agisce sulla PEPCK, ma sulla glicerolo chinasi di entrambi i tessuti",
  ], 0,
  "Con meno glicerolo 3-P l'adipocita riesterifica meno: aumentano gli acidi grassi liberi nel sangue.")
q("m7g-07", T, "a", "206", "Perché attivare la PEPCK del tessuto adiposo è utile nel diabete di tipo 2?", [
  "Fa riesterificare più acidi grassi e ne abbassa il livello nel sangue",
  "Aumenta la gluconeogenesi adiposa e fornisce glucosio ai tessuti insulino-resistenti",
  "Riduce la produzione di VLDL epatiche e quindi i trigliceridi plasmatici",
  "Aumenta l'ossidazione degli acidi grassi nel muscolo e riduce il peso corporeo",
  "Riduce la secrezione di cortisolo e quindi la gluconeogenesi epatica",
  ], 0,
  "Più acidi grassi liberi nel sangue → più insulino-resistenza.",
  note="La sbobina non nomina i farmaci; nei testi di riferimento sono i tiazolidinedioni (agonisti di PPARγ).")
q("m7g-08", T, "l", "205", "Quale enzima trasforma il DHAP in glicerolo 3-fosfato nell'adipocita?", [
  "Glicerolo 3-fosfato deidrogenasi citosolica (NADH)", "Glicerolo chinasi", "Trioso fosfato isomerasi", "Aldolasi", "Glicerolo 3-fosfato deidrogenasi mitocondriale (FAD)"], 0,
  "È la stessa reazione del primo passo della navetta del glicerolo fosfato.")
q("m7g-09", T, "h", "205", "Secondo la sbobina, che cosa succede di notte agli acidi grassi che arrivano al fegato in eccesso?", [
  "In parte vengono riesterificati e tornano all'adipe con le VLDL, per motivi non chiari",
  "Vengono tutti ossidati a CO₂ nel ciclo di Krebs, perché di notte l'ossalacetato è abbondante",
  "Vengono convertiti in glucosio, perché il glucagone attiva la gluconeogenesi dagli acidi grassi",
  "Vengono accumulati come trigliceridi nel fegato, che di notte non secerne lipoproteine",
  "Vengono escreti con la bile dopo coniugazione con taurina e glicina",
  ], 0,
  "Una parte va in β-ossidazione e chetogenesi, una parte rientra nel «ciclo dei trigliceridi» fegato ↔ adipe.")
q("m7g-10", T, "h", "204", "Un acido grasso prodotto dall'acido grasso sintasi entra nella sintesi dei trigliceridi. Quale affermazione è coerente con la sbobina?", [
  "Quelli già legati al CoA entrano così; quelli liberi vanno attivati dall'acil-CoA sintetasi",
  "Tutti gli acidi grassi, sintetizzati o liberi, entrano come tali senza essere legati al CoA",
  "Gli acidi grassi liberi entrano direttamente, mentre quelli sintetizzati vanno prima legati alla carnitina",
  "Tutti gli acidi grassi vanno legati all'ACP prima di essere trasferiti sul glicerolo 3-P",
  "Gli acidi grassi sintetizzati devono essere prima ossidati a malonil-CoA e poi riattivati",
  ], 0,
  "La sbobina considera palmitoil-CoA il prodotto della sintesi; gli acidi grassi liberi vanno attivati a spese di ATP.")

# ── Fosfolipidi (p. 207–208) ────────────────────────────────────────────────
T = "m7-fosfolipidi"
q("m7p-01", T, "f", "207", "Quale nucleotide attiva i precursori nella sintesi dei fosfolipidi?", [
  "CTP", "UTP", "GTP", "ATP", "TTP"], 0,
  "CDP-diacilglicerolo oppure CDP-colina / CDP-etanolammina.")
q("m7p-02", T, "f", "207", "Quale fosfolipide si forma legando l'inositolo al CDP-diacilglicerolo?", [
  "Fosfatidilinositolo", "Fosfatidilcolina", "Fosfatidilserina", "Fosfatidiletanolammina", "Sfingomielina"], 0,
  "Esce CMP. Il fosfatidilinositolo è anche il precursore dei secondi messaggeri.")
q("m7p-03", T, "m", "207", "Quali sono le due strategie di sintesi dei fosfolipidi?", [
  "Attivare il DAG come CDP-DAG e legare la testa, oppure attivare la testa come CDP-testa",
  "Attivare il diacilglicerolo come UDP-DAG e poi legare la testa, oppure attivare la testa come UDP-testa",
  "Attivare il glicerolo come CDP-glicerolo e poi legare gli acidi grassi uno alla volta",
  "Attivare la testa come acil-CoA e poi legarla al monoacilglicerolo con l'ACAT",
  "Legare la testa al fosfatidato con l'ATP, oppure al diacilglicerolo con il GTP",
  ], 0,
  "Fosfatidilinositolo (e cardiolipina) seguono la prima via; colina ed etanolammina la seconda.")
q("m7p-04", T, "m", "208", "Come si forma la fosfatidilcolina con la via di attivazione della testa?", [
  "Colina → fosfocolina (ATP) → CDP-colina (CTP) → + diacilglicerolo",
  "Colina → CDP-colina (CTP) → fosfocolina (ATP) → + fosfatidato → fosfatidilcolina + CMP",
  "Colina → fosfocolina (ATP) → + CDP-diacilglicerolo → fosfatidilcolina + CMP",
  "Colina → acetilcolina (acetil-CoA) → + diacilglicerolo → fosfatidilcolina + CoA",
  "Colina → UDP-colina (UTP) → + diacilglicerolo → fosfatidilcolina + UMP",
  ], 0,
  "La testa viene prima fosforilata, poi attivata con il CTP e infine trasferita sul DAG.")
q("m7p-05", T, "a", "207–208", "La fosfatidilcolina (lecitina) si distingue dalla fosfatidiletanolammina perché:", [
  "La colina ha tre metili sull'azoto, l'etanolammina un –NH₃⁺ libero",
  "La colina ha un carbossile in più, l'etanolammina no",
  "La colina è legata con un legame glicosidico, l'etanolammina con un estere",
  "La colina contiene un inositolo, l'etanolammina un glicerolo",
  "La colina ha due acidi grassi, l'etanolammina uno solo",
  ], 0,
  "–CH₂–CH₂–N⁺(CH₃)₃ contro –CH₂–CH₂–NH₃⁺; la serina ha anche un carbossile.")
q("m7p-06", T, "a", "208", "Perché la fosfatidato fosfatasi è un enzima finemente regolato?", [
  "Bilancia fosfatidato e DAG, che servono alle membrane e al segnale",
  "È l'unico enzima che può produrre CDP-diacilglicerolo, e consuma molto CTP",
  "Produce l'inositolo 1,4,5-trisfosfato, che libera il calcio dal reticolo",
  "Controlla l'ingresso degli acidi grassi nel mitocondrio come la CPT I",
  "È il punto di controllo della sintesi del colesterolo insieme alla HMG-CoA reduttasi",
  ], 0,
  "La via strutturale e quella del segnale si incrociano qui.")
q("m7p-07", T, "a", "207", "Dalla scissione del fosfatidilinositolo 4,5-bisfosfato da parte della fosfolipasi C si formano:", [
  "DAG e inositolo 1,4,5-trisfosfato", "Fosfatidato e inositolo libero", "Diacilglicerolo e inositolo 3-fosfato", "Acido arachidonico e lisofosfatidilinositolo", "CDP-diacilglicerolo e inositolo 4-fosfato"], 0,
  "IP₃ libera Ca²⁺ dal reticolo, il DAG attiva la PKC.",
  note="Sbobina di Biochimica II, p. 207: c'è scritto «fosfatidilinositolo-4-5-fosfato» e «inositolo 3 fosfato». I nomi corretti sono fosfatidilinositolo 4,5-bisfosfato (PIP₂) e inositolo 1,4,5-trisfosfato (IP₃).")
q("m7p-08", T, "l", "208", "Come si forma la cardiolipina?", [
  "CDP-diacilglicerolo + fosfatidilglicerolo",
  "Fosfatidilcolina + serina → cardiolipina + colina",
  "Diacilglicerolo + CDP-etanolammina → cardiolipina + CMP",
  "Fosfatidato + inositolo → cardiolipina + Pi",
  "Due diacilgliceroli + glicerolo 3-P → cardiolipina + 2 H₂O",
  ], 0,
  "È tipica della membrana mitocondriale interna.",
  note="La localizzazione nella membrana mitocondriale interna non è nella sbobina.")
q("m7p-09", T, "l", "208", "Secondo la sbobina, come si ottengono fosfatidilserina e fosfatidiletanolammina dalla fosfatidilcolina?", [
  "Per scambio della testa con serina o etanolammina",
  "Per metilazione della testa con S-adenosilmetionina",
  "Per decarbossilazione della colina a etanolammina",
  "Per idrolisi con fosfolipasi A2 e riacilazione",
  "Per ossidazione della colina a betaina e poi a serina",
  ], 0,
  "Lo scambio di testa polare avviene senza nucleotidi attivati.",
  note="Nel Lehninger, nei mammiferi la fosfatidiletanolammina si forma soprattutto dalla CDP-etanolammina, e la fosfatidilserina per scambio di testa da PE o PC. Lo schema della sbobina è una semplificazione.")
q("m7p-10", T, "h", "207–208", "Quale fosfolipide richiede l'attivazione del diacilglicerolo (CDP-DAG) e non della testa polare?", [
  "Fosfatidilinositolo", "Fosfatidilcolina", "Fosfatidiletanolammina", "Sfingomielina", "Plasmalogeno"], 0,
  "Fosfatidilinositolo e cardiolipina passano dal CDP-diacilglicerolo.")

# ── Colesterolo (p. 209–215, 221–225) ──────────────────────────────────────
T = "m7-colesterolo"
q("m7c-01", T, "f", "209", "Da quale molecola derivano tutti gli atomi di carbonio del colesterolo?", [
  "Acetil-CoA", "Malonil-CoA", "Propionil-CoA", "Succinil-CoA", "Glicerolo"], 0,
  "Acetil-CoA → HMG-CoA → mevalonato → unità isopreniche → squalene → colesterolo.")
q("m7c-02", T, "f", "213", "Qual è l'enzima chiave della sintesi del colesterolo?", [
  "HMG-CoA reduttasi", "HMG-CoA sintasi", "HMG-CoA liasi", "Squalene sintasi", "Mevalonato chinasi"], 0,
  "È regolato a molti livelli (trascrizione, degradazione, fosforilazione) ed è il bersaglio delle statine.")
q("m7c-03", T, "f", "209", "Quale di queste non è una funzione del colesterolo?", [
  "Precursore delle prostaglandine", "Componente delle membrane", "Precursore degli ormoni steroidei", "Precursore dei sali biliari", "Precursore della vitamina D"], 0,
  "Le prostaglandine derivano dall'acido arachidonico.")
q("m7c-04", T, "m", "211", "Che cosa catalizza la HMG-CoA reduttasi?", [
  "HMG-CoA + 2 NADPH → mevalonato + CoA",
  "HMG-CoA → acetoacetato + acetil-CoA",
  "HMG-CoA + 2 NADPH → squalene, unendo sei unità isopreniche",
  "Acetoacetil-CoA + acetil-CoA → HMG-CoA, con un'idratazione",
  "Mevalonato + 3 ATP → 3-fosfo-5-pirofosfomevalonato",
  ], 0,
  "Due riduzioni successive con NADPH; il CoA viene liberato.")
q("m7c-05", T, "m", "214", "Come viene attivata la trascrizione della HMG-CoA reduttasi quando il colesterolo di membrana scende?", [
  "SREBP viene tagliato da due proteasi e la parte N-terminale va nel nucleo",
  "SCAP viene fosforilato dalla PKA",
  "INSIG lega il colesterolo e trasporta la reduttasi verso i lisosomi per attivarla",
  "SREBP viene ubiquitinato e degradato, liberando il promotore della reduttasi dall'inibizione",
  "Il colesterolo si lega direttamente al promotore e ne blocca la trascrizione finché è presente",
  ], 0,
  "Con colesterolo basso il complesso SCAP–SREBP lascia il reticolo; i due tagli liberano il fattore di trascrizione.",
  note="Sbobina di Biochimica II, p. 214: c'è scritto che SCAP e SREBP «si separano parzialmente». Nei testi di riferimento SCAP e SREBP restano insieme e si staccano da INSIG; i tagli (S1P e S2P) avvengono nel Golgi.")
q("m7c-06", T, "m", "215, 221", "Quali meccanismi riducono l'attività della HMG-CoA reduttasi?", [
  "Ubiquitinazione (INSIG), fosforilazione (AMPK, glucagone), ossisteroli",
  "Defosforilazione da insulina, aumento di SREBP nucleare, degradazione da ossisteroli",
  "Attivazione da glucagone, inibizione da AMP, aumento della trascrizione da colesterolo",
  "Inibizione competitiva dal mevalonato, attivazione da AMPK, legame con LDL",
  "Ubiquitinazione da insulina, attivazione da ossisteroli, inibizione da SCAP",
  ], 0,
  "L'insulina invece stimola la formazione di mevalonato.")
q("m7c-07", T, "m", "210", "Come entra il colesterolo alimentare nell'enterocita?", [
  "Con il trasportatore NPC1L1; dentro viene esterificato dall'ACAT ed entra nei chilomicroni",
  "Con il recettore per le LDL; dentro viene ossidato a sali biliari e secreto con la bile",
  "Per diffusione semplice come estere; dentro viene idrolizzato e liberato nel sangue legato all'albumina",
  "Con il trasportatore ABCA1; dentro viene legato all'ApoA-I e secreto come HDL",
  "Con il CD36; dentro viene trasformato in vitamina D e immagazzinato",
  ], 0,
  "NPC1L1 è il bersaglio dell'ezetimibe.",
  note="Sbobina di Biochimica II, p. 210: c'è scritto che nel lume il colesterolo «viene esterificato». Nel lume gli esteri vengono invece idrolizzati (colesterolo esterasi pancreatica) e si assorbe soprattutto colesterolo libero; la riesterificazione avviene nell'enterocita.")
q("m7c-08", T, "a", "224", "Come agiscono le statine?", [
  "Somigliano al mevalonato e inibiscono in modo competitivo la HMG-CoA reduttasi",
  "Inibiscono il trasportatore NPC1L1 e riducono l'assorbimento del colesterolo alimentare",
  "Attivano la lipoproteina lipasi e riducono la produzione di VLDL da parte del fegato",
  "Legano i sali biliari nell'intestino e ne impediscono il riassorbimento enteroepatico",
  "Inibiscono in modo irreversibile la squalene sintasi e bloccano la sintesi a valle",
  ], 0,
  "Inibitore competitivo: la Vmax non cambia, la sintesi endogena non si azzera. Effetto avverso da ricordare: dolori muscolari fino alla rabdomiolisi.")
q("m7c-09", T, "a", "212", "Perché bloccare la via del mevalonato può avere effetti anche oltre il colesterolo?", [
  "Perché dalle stesse unità isopreniche si forma la coda del coenzima Q",
  "Perché dal mevalonato si formano anche gli acidi grassi polinsaturi essenziali",
  "Perché il mevalonato è il precursore diretto della vitamina B12",
  "Perché la HMG-CoA reduttasi produce anche i corpi chetonici nel mitocondrio",
  "Perché il mevalonato serve a sintetizzare la carnitina nel fegato",
  ], 0,
  "Isopentenil pirofosfato e dimetilallil pirofosfato sono le unità isopreniche.",
  note="L'idea che la riduzione del CoQ contribuisca agli effetti muscolari delle statine non è nella sbobina ed è ancora discussa.")
q("m7c-10", T, "a", "221–222", "Quando il colesterolo si accumula nella cellula, che cosa fanno LXR e gli ossisteroli?", [
  "Attivano CYP7A1, ABCA1 e ABCG1: più sali biliari e più trasporto inverso",
  "Reprimono CYP7A1 e ABCA1: meno sali biliari e meno trasporto inverso del colesterolo",
  "Attivano SREBP e la HMG-CoA reduttasi per compensare la perdita di colesterolo",
  "Aumentano il numero di recettori per le LDL sulla membrana degli epatociti",
  "Attivano la fosforilazione della LCAT nelle HDL per bloccarne l'attività",
  ], 0,
  "LXR (liver X receptor) con RXR rimuove la repressione: la cellula elimina il colesterolo in eccesso.")
q("m7c-11", T, "l", "212", "Quali sono le due unità isopreniche attivate della sintesi del colesterolo?", [
  "Isopentenil e dimetilallil pirofosfato", "Geranil pirofosfato e farnesil pirofosfato", "Mevalonato 5-fosfato e mevalonato 5-pirofosfato", "Squalene e lanosterolo", "Acetoacetil-CoA e HMG-CoA"], 0,
  "Sono isomeri a 5 atomi di carbonio; il loro assemblaggio porta a geranile, farnesile e squalene.")
q("m7c-12", T, "l", "212", "Come si chiama l'intermedio fosforilato del mevalonato citato nella sbobina?", [
  "3-fosfo-5-pirofosfomevalonato", "5-fosfo-3-pirofosfomevalonato", "Mevalonato 3,5-bisfosfato", "Fosfomevalonil-CoA", "5-pirofosfo-3-idrossimevalonato"], 0,
  "Si forma con più ATP; perdendo CO₂ e fosfato dà l'isopentenil pirofosfato.")
q("m7c-13", T, "l", "225", "Che cosa fa l'AMPK quando aumenta l'AMP?", [
  "Inibisce le vie anaboliche e attiva quelle cataboliche",
  "Attiva le vie anaboliche e inibisce l'ossidazione degli acidi grassi",
  "Attiva la sintesi di colesterolo e inibisce la glicolisi cardiaca",
  "Inibisce il trasporto di glucosio e attiva la sintesi di glicogeno",
  "Attiva l'acetil-CoA carbossilasi e la HMG-CoA reduttasi",
  ], 0,
  "AMP alto = poca energia: si spengono le sintesi, si accendono ossidazione degli acidi grassi, trasporto del glucosio e glicolisi cardiaca.")
q("m7c-14", T, "h", "209–212", "Perché la sintesi del colesterolo avviene negli stessi momenti metabolici della sintesi degli acidi grassi?", [
  "Usa acetil-CoA citosolico (dal citrato), NADPH e ATP, abbondanti dopo i pasti",
  "Usa acetil-CoA prodotto nel mitocondrio dalla β-ossidazione, abbondante a digiuno",
  "Usa malonil-CoA come donatore e quindi dipende dall'acetil-CoA carbossilasi",
  "Usa i corpi chetonici del fegato come precursori, abbondanti dopo i pasti",
  "Avviene nel mitocondrio e richiede NADH abbondante, tipico del digiuno",
  ], 0,
  "Stesso precursore citosolico (via citrato e ATP-citrato liasi) e stesso bisogno di energia e potere riducente.")
q("m7c-15", T, "h", "224–225", "Quale abbinamento farmaco/sostanza – meccanismo è corretto secondo la sbobina?", [
  "Ezetimibe – riduce l'assorbimento intestinale del colesterolo",
  "Statine – aumentano l'escrezione dei sali biliari con le feci",
  "Fibrati – inibiscono in modo competitivo la HMG-CoA reduttasi",
  "Steroli vegetali – inibiscono la sintesi epatica di VLDL",
  "Riso rosso fermentato – blocca il trasportatore NPC1L1",
  ], 0,
  "Statine (e riso rosso fermentato, che ne contiene) inibiscono la reduttasi; gli steroli vegetali competono con il colesterolo per l'assorbimento.",
  note="Sbobina di Biochimica II, p. 224: i fibrati sono descritti come farmaci che riducono le VLDL e aumentano l'escrezione dei sali biliari. Nei testi di riferimento agiscono soprattutto attivando PPARα (più ossidazione degli acidi grassi e più lipoproteina lipasi).")

# ── Lipoproteine (p. 215–224) ───────────────────────────────────────────────
T = "m7-lipoproteine"
q("m7l-01", T, "f", "216", "Da che cosa dipende soprattutto la densità di una lipoproteina?", [
  "Dal contenuto di trigliceridi: più trigliceridi, densità più bassa",
  "Dal contenuto di proteine: più proteine, densità più bassa",
  "Dal contenuto di colesterolo libero: più colesterolo, densità più bassa",
  "Dal numero di fosfolipidi: più fosfolipidi, densità più alta",
  "Dalla carica elettrica: più cariche negative, densità più alta",
  ], 0,
  "Chilomicroni < VLDL < IDL < LDL < HDL in densità.")
q("m7l-02", T, "f", "216", "Quale apolipoproteina attiva la lipoproteina lipasi?", [
  "ApoC-II", "ApoB-48", "ApoE", "ApoA-I", "ApoB-100"], 0,
  "I chilomicroni hanno ApoB-48 (strutturale) e ApoC-II (attivatrice).")
q("m7l-03", T, "f", "220", "Quale enzima esterifica il colesterolo nelle HDL?", [
  "LCAT (lecitina-colesterolo aciltrasferasi)", "ACAT (acil-CoA colesterolo aciltrasferasi)", "Lipoproteina lipasi", "Lipasi epatica", "Colesterolo esterasi"], 0,
  "Usa l'acido grasso in posizione 2 della fosfatidilcolina e libera lisolecitina.")
q("m7l-04", T, "m", "216–217", "Come si chiama il trasporto «centrifugo» del colesterolo e quale lipoproteina lo svolge?", [
  "Dal fegato ai tessuti periferici, con le LDL",
  "Dai tessuti periferici al fegato, con le LDL",
  "Dal fegato ai tessuti periferici, con le HDL",
  "Dall'intestino al tessuto adiposo, con le HDL",
  "Dai tessuti periferici all'intestino, con le VLDL",
  ], 0,
  "Le LDL sono centrifughe, le HDL centripete.")
q("m7l-05", T, "m", "217, 219", "Come si passa dalle VLDL alle LDL?", [
  "La lipoproteina lipasi toglie i trigliceridi: VLDL → IDL → LDL, con ApoB-100",
  "La LCAT aggiunge esteri del colesterolo: VLDL → HDL → LDL, con ApoA-I",
  "Il fegato aggiunge ApoB-48: VLDL → chilomicroni → LDL, ricche di trigliceridi",
  "La lipasi ormone-sensibile toglie il colesterolo: VLDL → IDL → LDL, povere di esteri",
  "L'ACAT esterifica il colesterolo delle VLDL, che diventano più leggere",
  ], 0,
  "Le VLDL ricevono ApoC-II e ApoE dalle HDL, cedono i trigliceridi nei capillari e restano con ApoB-100.")
q("m7l-06", T, "m", "218", "Che cosa succede alle LDL legate al loro recettore sull'epatocita?", [
  "Vengono internalizzate e degradate nei lisosomi; il recettore torna in membrana",
  "Cedono il colesterolo sulla membrana e vengono rilasciate intatte nel sangue",
  "Vengono trasformate in HDL nel reticolo endoplasmatico e risecrete",
  "Vengono idrolizzate dalla lipoproteina lipasi epatica senza essere internalizzate",
  "Vengono internalizzate insieme al recettore, che viene degradato con loro",
  ], 0,
  "Il colesterolo liberato viene riesterificato dall'ACAT e immagazzinato; inibisce la HMG-CoA reduttasi e la sintesi dei recettori.")
q("m7l-07", T, "m", "221", "Perché il colesterolo delle HDL è considerato «buono»?", [
  "Torna al fegato tramite SR-BI e diventa sali biliari, cioè viene eliminato",
  "Viene ossidato dalle HDL stesse a CO₂ e acqua mentre circola nel sangue",
  "Viene ceduto alle cellule endoteliali, che lo usano per riparare le placche",
  "Viene trasformato in vitamina D nella pelle senza passare dal fegato",
  "Non può essere ossidato perché le HDL non hanno apolipoproteine",
  ], 0,
  "Le LDL in eccesso possono invece ossidarsi in circolo ed essere captate dai macrofagi. Le HDL hanno anche proprietà antinfiammatorie.")
q("m7l-08", T, "a", "220", "Come entra il colesterolo delle cellule periferiche nelle HDL?", [
  "L'ApoA-I interagisce con ABCA1, che esporta il colesterolo; la LCAT lo esterifica",
  "L'ApoB-100 si lega al recettore per le LDL e il colesterolo passa per endocitosi",
  "L'ApoE si lega al recettore SR-BI della cellula periferica e assorbe il colesterolo",
  "Il colesterolo diffonde nelle HDL dopo essere stato esterificato dall'ACAT",
  "Il CD36 trasferisce il colesterolo alle HDL insieme agli acidi grassi",
  ], 0,
  "Le HDL nascenti sono dischi appiattiti; prendendo colesterolo diventano sferiche.")
q("m7l-09", T, "a", "222–223", "Nell'ipercolesterolemia familiare omozigote, che cosa manca e che cosa succede alla sintesi epatica di colesterolo?", [
  "Mancano recettori LDL funzionanti: il fegato non capta le LDL e continua la sintesi",
  "Manca l'ApoA-I: le HDL non si formano e il colesterolo resta nelle cellule periferiche",
  "Manca la LCAT: il colesterolo delle HDL non si esterifica e la sintesi epatica si blocca",
  "Manca la lipoproteina lipasi: i chilomicroni restano in circolo e la sintesi si blocca",
  "Manca la HMG-CoA reduttasi: il colesterolo plasmatico viene tutto dalla dieta",
  ], 0,
  "LDL in circolo: circa 680 mg/dl negli omozigoti, 300 negli eterozigoti. Le cellule hanno poco colesterolo e non frenano la sintesi.")
q("m7l-10", T, "a", "223", "Nella malattia di Tangier manca il trasportatore ABCA1. Che cosa ne consegue?", [
  "Il colesterolo entra con le LDL ma non riesce a uscire verso le HDL",
  "Il colesterolo non entra nelle cellule e si accumula nelle LDL plasmatiche",
  "Le LDL non vengono più prodotte dal fegato e il colesterolo plasmatico crolla",
  "I chilomicroni non cedono i trigliceridi e si accumulano nel plasma",
  "Le HDL captano troppo colesterolo e lo depositano nelle arterie",
  ], 0,
  "Il difetto è sul trasporto inverso: HDL molto basse e colesterolo accumulato nei tessuti.")
q("m7l-11", T, "a", "223–224", "Secondo la sbobina, quale fattore della dieta alza di più il colesterolo LDL?", [
  "I grassi saturi, che riducono sintesi e riciclo dei recettori epatici per le LDL",
  "Il colesterolo alimentare, che contribuisce per circa il 90% della colesterolemia",
  "I carboidrati semplici, che attivano direttamente la HMG-CoA reduttasi",
  "Le proteine animali, che aumentano la produzione di ApoB-100",
  "I grassi insaturi vegetali, che inibiscono la LCAT delle HDL",
  ], 0,
  "Il colesterolo esogeno pesa per circa il 10% (dato ancora discusso).")
q("m7l-12", T, "l", "218", "Che cosa catalizza l'ACAT?", [
  "Colesterolo + acil-CoA → estere del colesterolo + CoA, nelle cellule",
  "Colesterolo + fosfatidilcolina → estere del colesterolo + lisolecitina, nelle HDL",
  "Estere del colesterolo + H₂O → colesterolo + acido grasso, nel lume",
  "Colesterolo + NADPH + O₂ → 7α-idrossicolesterolo, nel fegato",
  "Acetil-CoA + acetoacetil-CoA → HMG-CoA, nel citosol",
  ], 0,
  "ACAT = acil-CoA:colesterolo aciltrasferasi (intracellulare); LCAT è quella delle HDL.")
q("m7l-13", T, "l", "221", "Come si chiama il recettore epatico che capta il colesterolo delle HDL?", [
  "SR-BI", "Recettore per le LDL", "LRP (recettore dei residui)", "ABCA1", "NPC1L1"], 0,
  "Indirizza il colesterolo delle HDL verso la sintesi dei sali biliari.")
q("m7l-14", T, "l", "219", "Quale apolipoproteina permette al fegato di riconoscere i residui dei chilomicroni?", [
  "ApoE", "ApoB-48", "ApoC-II", "ApoA-I", "ApoB-100"], 0,
  "Le LDL vengono invece riconosciute tramite l'ApoB-100.")
q("m7l-15", T, "h", "222", "Come si arriva dalle LDL in eccesso alla placca aterosclerotica, secondo la sbobina?", [
  "Le LDL in circolo si ossidano e richiamano monociti, che diventano macrofagi carichi di colesterolo",
  "Le LDL vengono captate dalle cellule endoteliali tramite ABCA1 e ne causano la necrosi",
  "Le LDL attivano la LCAT sull'endotelio, che deposita esteri del colesterolo nella parete",
  "Le LDL vengono trasformate in HDL nella parete del vaso, che vi trattengono il colesterolo",
  "Le LDL inibiscono la lipoproteina lipasi e i trigliceridi si depositano sotto l'endotelio",
  ], 0,
  "I depositi restringono il lume e favoriscono trombosi e stenosi, come nella malattia coronarica.")
q("m7l-16", T, "h", "216–221", "Quale abbinamento lipoproteina – origine – funzione principale è corretto?", [
  "HDL – intestino e fegato – trasporto del colesterolo dai tessuti al fegato",
  "LDL – intestino – trasporto dei trigliceridi alimentari al tessuto adiposo",
  "Chilomicroni – fegato – trasporto del colesterolo endogeno ai tessuti",
  "VLDL – intestino – trasporto del colesterolo periferico al fegato",
  "IDL – tessuto adiposo – trasporto degli acidi grassi liberi al muscolo",
  ], 0,
  "Chilomicroni dall'intestino (TG alimentari), VLDL dal fegato (TG endogeni), LDL centrifughe, HDL centripete.",
  note="La sbobina dice che le HDL sono prodotte dall'intestino; nei testi di riferimento sono prodotte sia dal fegato sia dall'intestino.")
