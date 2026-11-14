"""Blocco 9 – Ormoni (sbobina di Biochimica II, p. 279–310)."""
from bank_common import q

# ── Asse ipotalamo-ipofisi e neuroipofisi (p. 279–283) ──────────────────────
T = "m9-neuroipofisi"
q("m9n-01", T, "f", "279", "Quali ormoni rilascia la neuroipofisi?", [
  "ADH e ossitocina", "GH e prolattina", "ACTH e TSH", "FSH e LH", "TRH e CRH"], 0,
  "Sono sintetizzati nei neuroni ipotalamici e liberati dagli assoni nella neuroipofisi.")
q("m9n-02", T, "f", "279–280", "Che cosa hanno in comune vasopressina e ossitocina?", [
  "Sono nonapeptidi con un ponte disolfuro e differiscono per due residui",
  "Sono glicoproteine con una subunità α comune e una β specifica",
  "Sono derivati della tirosina e agiscono su recettori nucleari",
  "Sono steroidi a 21 atomi di carbonio prodotti dalla corticale",
  "Sono tripeptidi modificati alle estremità per resistere alle peptidasi",
  ], 0,
  "Hanno struttura primaria molto simile: i recettori distinguono i due residui diversi.")
q("m9n-03", T, "f", "281", "Quale acquaporina viene portata sulla membrana del tubulo dalla vasopressina?", [
  "Acquaporina 2", "Acquaporina 3", "Acquaporina 1", "Acquaporina 4", "Acquagliceroporina 7"], 0,
  "L'AQP2 sta in vescicole; l'AQP3 è costitutiva sulla membrana basolaterale.")
q("m9n-04", T, "m", "281", "Come sono fatte le acquaporine?", [
  "Omotetrameri di subunità da circa 28 kDa",
  "Monomeri da 12 eliche, come i GLUT",
  "Dimeri di subunità da 250 kDa, come l'acido grasso sintasi",
  "Eterotrimeri con una subunità α che lega il GTP",
  "Pentameri attorno a un poro carico negativamente",
  ], 0,
  "Ne esistono 12–15 isoforme: alcune trasportano anche glicerolo (acquagliceroporine) o urea.")
q("m9n-05", T, "m", "282", "Quali stimoli aumentano la secrezione di vasopressina?", [
  "Osmolarità plasmatica alta e pressione arteriosa bassa",
  "Calo dell'osmolarità plasmatica e aumento della volemia",
  "Aumento della glicemia e della concentrazione di insulina",
  "Calo della calcemia e aumento del paratormone",
  "Aumento del cortisolo e calo della concentrazione di ACTH",
  ], 0,
  "Gli osmocettori ipotalamici sentono l'osmolarità; se la vasopressina non basta compare la sete.")
q("m9n-06", T, "m", "281", "Che cos'è la neurofisina?", [
  "Il frammento che accompagna l'ormone lungo l'assone",
  "Il recettore della vasopressina sul tubulo renale",
  "L'enzima che forma il ponte disolfuro dell'ossitocina",
  "La proteasi che taglia la pre-pro-vasopressina nel nucleo",
  "Il canale che fa uscire l'ormone dalla terminazione nervosa",
  ], 0,
  "Dalla pre-pro-forma si ottengono l'ormone, la neurofisina e un glicopeptide.",
  note="Sbobina di Biochimica II, p. 281: c'è scritto che la glicoproteina deriva dalla pre-pro-ossitocina. Nei testi di riferimento il glicopeptide C-terminale (copeptina) deriva dalla pre-pro-vasopressina.")
q("m9n-07", T, "a", "282", "Una ragazza dopo un trauma cranico urina moltissimo, con urine diluite e glicemia normale. Che cosa è più probabile?", [
  "Diabete insipido, per danno alla neuroipofisi",
  "Diabete mellito di tipo 1, per danno al pancreas",
  "Iperaldosteronismo, per danno alla corticale",
  "Sindrome da inappropriata secrezione di ADH",
  "Ipertiroidismo, per danno all'adenoipofisi",
  ], 0,
  "Senza vasopressina manca il riassorbimento facoltativo di acqua. «Insipido» perché le urine non sono dolci.")
q("m9n-08", T, "a", "282", "Quale di questi meccanismi non causa diabete insipido?", [
  "Eccesso di acquaporina 2 in membrana",
  "Mancata produzione di vasopressina",
  "Mancata secrezione di vasopressina",
  "Mutazione del recettore della vasopressina",
  "Difetto funzionale dell'acquaporina 2",
  ], 0,
  "Lo schema vale per ogni ormone: produzione, secrezione, recettore, trasduzione, effettore.")
q("m9n-09", T, "a", "288", "Quali secondi messaggeri usano vasopressina (sul rene) e ossitocina?", [
  "Vasopressina cAMP; ossitocina IP₃/DAG",
  "Vasopressina IP₃/DAG; ossitocina cAMP",
  "Entrambe cGMP",
  "Entrambe JAK/STAT",
  "Vasopressina Ras/MAPK; ossitocina cAMP",
  ], 0,
  "L'ossitocina contrae la muscolatura liscia con il Ca²⁺ liberato dall'IP₃.")
q("m9n-10", T, "l", "282", "Sopra quale glicemia indicativa compare glicosuria nel diabete mellito?", [
  "Circa 180 mg/dl", "Circa 80 mg/dl", "Circa 126 mg/dl", "Circa 400 mg/dl", "Circa 18 mg/dl"], 0,
  "È la soglia renale: il glucosio nelle urine trascina acqua (poliuria).",
  note="Sbobina di Biochimica II, p. 282: c'è scritto «180 mg/L». L'unità corretta è mg/dl (180 mg/L sarebbe un'ipoglicemia grave).")
q("m9n-11", T, "l", "281", "In quali nuclei ipotalamici si sintetizzano vasopressina e ossitocina secondo la sbobina?", [
  "Paraventricolari", "Arcuato", "Soprachiasmatico", "Ventromediale", "Laterale"], 0,
  "Non è nella sbobina, ma si sintetizzano anche nei nuclei sopraottici.")
q("m9n-12", T, "h", "283", "Quale effetto dell'ossitocina non è citato dalla sbobina?", [
  "Riassorbimento di acqua nel dotto collettore",
  "Contrazione dell'utero durante il parto",
  "Eiezione del latte durante l'allattamento",
  "Aumento della fiducia negli altri",
  "Facilitazione del trasporto degli spermatozoi",
  ], 0,
  "Il riassorbimento di acqua è della vasopressina.")

# ── Adenoipofisi (p. 279–280, 284–288) ──────────────────────────────────────
T = "m9-adenoipofisi"
q("m9a-01", T, "f", "279", "Quale fattore ipotalamico è un tripeptide modificato alle estremità?", [
  "TRH", "GnRH", "CRH", "GHRH", "Somatostatina"], 0,
  "pGlu-His-Pro-NH₂: le modifiche lo proteggono dalle peptidasi. GnRH 10, CRH 41, GHRH 44 residui.")
q("m9a-02", T, "f", "284", "Quanti amminoacidi ha l'ormone della crescita?", [
  "191", "84", "44", "9", "51"], 0,
  "È un polipeptide dell'adenoipofisi; agisce con JAK/STAT.")
q("m9a-03", T, "f", "285", "Da quale precursore deriva l'ACTH?", [
  "POMC", "Proinsulina", "Tireoglobulina", "Angiotensinogeno", "Pre-pro-vasopressina"], 0,
  "Dalla POMC si ottengono anche β-lipotropina, α-MSH e γ-MSH.")
q("m9a-04", T, "m", "288", "Che cosa hanno in comune TSH, LH e FSH?", [
  "Una subunità α identica; la specificità sta nella subunità β",
  "Una subunità β identica; la specificità sta nella subunità α",
  "Lo stesso recettore, distinto solo dalla concentrazione",
  "La stessa sequenza, ma glicosilazioni diverse",
  "Il fatto di agire tutti con JAK/STAT",
  ], 0,
  "Sono glicoproteine eterodimeriche; le subunità separate non hanno effetto.")
q("m9a-05", T, "m", "284", "Quale effetto metabolico ha l'ormone della crescita?", [
  "Iperglicemizzante, anabolico, aumenta l'ossidazione dei grassi",
  "Ipoglicemizzante, catabolico proteico, aumenta la sintesi dei grassi",
  "Ipoglicemizzante, anabolico proteico, riduce l'ossidazione dei grassi",
  "Iperglicemizzante, catabolico proteico, riduce la lipolisi",
  "Nessun effetto metabolico: agisce solo sulla cartilagine",
  ], 0,
  "Agisce in sinergia con il glucagone sulla glicemia; stimola condrociti e mioblasti (crescita lineare).")
q("m9a-06", T, "m", "280", "Perché una terapia ormonale prolungata va sospesa gradualmente?", [
  "Perché l'ormone esogeno spegne la produzione endogena con il feedback negativo",
  "Perché l'ormone esogeno si accumula nel tessuto adiposo e viene rilasciato lentamente",
  "Perché i recettori aumentano di numero e servono dosi crescenti",
  "Perché il fegato smette di degradare l'ormone dopo alcune settimane",
  "Perché l'ormone esogeno induce anticorpi che bloccano quello endogeno",
  ], 0,
  "Una sospensione brusca lascia l'organismo senza ormone finché la ghiandola non riprende.")
q("m9a-07", T, "m", "288", "Quale via di segnalazione usano i fattori di rilascio ipotalamici per liberare gli ormoni ipofisari?", [
  "Gq → IP₃/DAG: il Ca²⁺ favorisce l'esocitosi delle vescicole",
  "Gs → cAMP: la PKA fosforila le vescicole e ne causa la fusione",
  "Recettore nucleare: il complesso attiva la trascrizione dell'ormone",
  "JAK/STAT: STAT fosforilato attiva l'esocitosi",
  "Canale ionico: l'ingresso di Na⁺ depolarizza la cellula",
  ], 0,
  "Il GHRH usa anche la via del cAMP (CREB).")
q("m9a-08", T, "a", "288", "Quale abbinamento ormone – via di trasduzione è corretto?", [
  "Prolattina – JAK/STAT", "ACTH – JAK/STAT", "TSH – IP₃/DAG", "GH – cAMP", "LH – recettore nucleare"], 0,
  "ACTH, TSH, FSH e LH usano cAMP; prolattina e GH usano JAK/STAT (il GH anche Ras).")
q("m9a-09", T, "a", "285", "Quale effetto viene attribuito all'ACTH nella sbobina ma nei testi di riferimento è proprio della prolattina?", [
  "Sviluppo mammario e produzione di latte",
  "Stimolazione della produzione di cortisolo",
  "Stimolazione dei melanociti",
  "Derivazione dalla proopiomelanocortina",
  "Controllo da parte del CRH ipotalamico",
  ], 0,
  "L'ACTH stimola la corticale (cortisolo) e, come l'α-MSH, i melanociti.",
  note="Sbobina di Biochimica II, p. 285: tra gli effetti dell'ACTH c'è «sviluppo della ghiandola mammaria e produzione di latte». È l'azione tipica della prolattina, non dell'ACTH.")
q("m9a-10", T, "a", "279", "Quali ormoni non sono controllati dall'asse ipotalamo-ipofisi secondo la sbobina?", [
  "Insulina e glucagone, regolati dalla glicemia",
  "Cortisolo e ormoni tiroidei, regolati dal feedback",
  "Testosterone ed estradiolo, regolati dalle gonadotropine",
  "GH e prolattina, regolati dai fattori di rilascio",
  "Vasopressina e ossitocina, regolate dai nuclei ipotalamici",
  ], 0,
  "L'adrenalina dipende dal SNC ma non dall'ipotalamo; anche paratormone e aldosterone sono fuori dall'asse.")
q("m9a-11", T, "l", "279", "Quanti amminoacidi ha il CRH?", [
  "41", "3", "10", "44", "191"], 0,
  "TRH 3, GnRH 10, CRH 41, GHRH 44.")
q("m9a-12", T, "l", "286", "Perché l'ACTH prodotto dai cheratinociti esposti al sole scurisce la pelle?", [
  "Perché stimola i melanociti a produrre melanina", "Perché inibisce la tirosinasi epidermica", "Perché stimola la corticale a produrre cortisolo", "Perché aumenta la vitamina D cutanea", "Perché ossida la melanina già presente"], 0,
  "Per lo stesso motivo nel morbo di Addison autoimmune, con ACTH alto, la pelle si pigmenta.")
q("m9a-13", T, "h", "284", "Quale uso dell'ormone della crescita è citato dalla sbobina?", [
  "Il GH ricombinante nella carenza e il GH per il latte delle mucche",
  "Il GH per ridurre la glicemia nei diabetici insulino-resistenti",
  "Il GH per ridurre la massa muscolare negli atleti con miopatia",
  "Il GH per bloccare l'acromegalia negli adulti con adenoma",
  "Il GH per aumentare la sintesi di cortisolo nell'iposurrenalismo",
  ], 0,
  "Carenza → nanismo; eccesso → gigantismo (prima della chiusura delle cartilagini) o acromegalia.")

# ── Adipochine e regolazione dell'appetito (p. 286–287) ────────────────────
T = "m9-adipochine"
q("m9k-01", T, "f", "286", "Quale ormone prodotto dal tessuto adiposo segnala la sazietà?", [
  "Leptina", "Grelina", "Neuropeptide Y", "Insulina", "Glucagone"], 0,
  "La produce l'adipocita ricco di trigliceridi; il topo ob/ob, senza leptina, ingrassa.")
q("m9k-02", T, "f", "286", "Quale peptide ipotalamico stimola l'assunzione di cibo?", [
  "Neuropeptide Y", "α-MSH", "Leptina", "CART", "GLP-1"], 0,
  "Leptina e insulina, tramite la POMC e l'α-MSH, ne bloccano la produzione.")
q("m9k-03", T, "m", "287", "Con quale via di segnalazione agisce la leptina?", [
  "JAK/STAT", "Gs/cAMP", "Gq/IP₃", "Recettore nucleare", "Canale ionico"], 0,
  "È la stessa via di GH e prolattina.")
q("m9k-04", T, "m", "286", "Come aumenta la leptina il consumo di energia nel tessuto adiposo?", [
  "Attiva il simpatico: la noradrenalina sui β3 accende lipolisi e disaccoppiamento",
  "Attiva il parasimpatico: l'acetilcolina inibisce la lipasi ormone-sensibile",
  "Agisce direttamente sull'adipocita bloccando la lipoproteina lipasi",
  "Inibisce l'insulina nel pancreas, sbloccando la gluconeogenesi",
  "Aumenta il neuropeptide Y, che stimola la termogenesi da brivido",
  ], 0,
  "Termogenesi senza brivido: il calore prodotto smaltisce l'eccesso di grassi.",
  note="Sbobina di Biochimica II, p. 286: c'è scritto che la leptina «stimola il sistema parasimpatico con la produzione di noradrenalina». La noradrenalina è il mediatore del sistema simpatico; i recettori β3 dell'adipocita sono adrenergici.")
q("m9k-05", T, "m", "286", "Dove agiscono insieme leptina e insulina per ridurre la fame?", [
  "Sui neuroni del nucleo arcuato, che producono POMC e quindi α-MSH",
  "Sulle cellule β del pancreas, che riducono la secrezione di glucagone",
  "Sugli adipociti, che riducono la produzione di leptina",
  "Sullo stomaco, dove inibiscono la secrezione di gastrina",
  "Sulla neuroipofisi, che riduce la secrezione di ossitocina",
  ], 0,
  "L'α-MSH blocca il neuropeptide Y.",
  note="La sbobina dice che la POMC viene prodotta «nell'ipofisi»; nella regolazione dell'appetito la POMC che conta è quella dei neuroni del nucleo arcuato.")
q("m9k-06", T, "a", "286–287", "Perché il topo con mutazione del gene ob, a parità di cibo, ingrassa?", [
  "Manca il segnale di sazietà e la termogenesi non si attiva",
  "Senza leptina l'adipocita non riesce a idrolizzare i trigliceridi",
  "Senza leptina il pancreas produce troppo glucagone",
  "Senza leptina il neuropeptide Y non viene più prodotto",
  "Senza leptina l'intestino assorbe più trigliceridi",
  ], 0,
  "Mangia di più e brucia meno grassi.")
q("m9k-07", T, "a", "287", "Perché cocaina e anfetamine riducono l'appetito, secondo la sbobina?", [
  "Agiscono sui trascritti CART, che frenano il neuropeptide Y",
  "Bloccano la secrezione di grelina da parte dello stomaco",
  "Aumentano direttamente la produzione di leptina negli adipociti",
  "Inibiscono il recettore della leptina nel nucleo arcuato",
  "Stimolano la secrezione di insulina dal pancreas",
  ], 0,
  "CART = cocaine- and amphetamine-regulated transcript.")
q("m9k-08", T, "l", "286", "Come si chiama il gene della leptina, mutato nei topi obesi?", [
  "OB", "DB", "POMC", "NPY", "UCP1"], 0,
  "Il topo db/db ha invece il recettore della leptina mutato.",
  note="Il topo db/db non è nella sbobina.")
q("m9k-09", T, "h", "286", "Quale catena di eventi dopo un pasto ricco porta a ridurre l'assunzione di cibo?", [
  "Più trigliceridi → leptina → arcuato → α-MSH → meno neuropeptide Y",
  "Più trigliceridi nell'adipe → grelina → arcuato → più neuropeptide Y → sazietà",
  "Più glucosio nel sangue → glucagone → ipofisi → ACTH → meno cortisolo",
  "Più leptina → parasimpatico → acetilcolina → più lipogenesi nell'adipe",
  "Più insulina → nucleo arcuato → meno POMC → più neuropeptide Y",
  ], 0,
  "In parallelo la leptina attiva il simpatico verso l'adipe (lipolisi e calore).")

# ── Ormoni tiroidei (p. 289–293) ────────────────────────────────────────────
T = "m9-tiroide"
q("m9t-01", T, "f", "289", "Da quale amminoacido derivano gli ormoni tiroidei?", [
  "Tirosina", "Triptofano", "Fenilalanina", "Istidina", "Glicina"], 0,
  "Vengono sintetizzati su residui di tirosina della tireoglobulina.")
q("m9t-02", T, "f", "290", "Quale enzima iodina le tirosine della tireoglobulina?", [
  "Tiroide perossidasi", "Deiodinasi", "Tirosina idrossilasi", "Glutatione perossidasi", "Pendrina"], 0,
  "È una perossidasi con ferro (eme) che usa H₂O₂; la pendrina trasporta lo ioduro nella colloide.")
q("m9t-03", T, "f", "289", "Quale ormone tiroideo è più potente?", [
  "T3", "T4 (tiroxina)", "Reverse T3", "Diiodotirosina", "Monoiodotirosina"], 0,
  "Il T4 viene in gran parte convertito in T3 nei tessuti (soprattutto fegato).")
q("m9t-04", T, "m", "289–290", "Come entra lo ioduro nella cellula follicolare?", [
  "In simporto con il Na⁺, grazie alla Na⁺/K⁺-ATPasi",
  "Con una pompa ATP-dipendente specifica per lo ioduro sulla membrana basale",
  "Per diffusione semplice, perché lo ioduro è liposolubile",
  "In antiporto con il cloruro, come il bicarbonato nella cellula parietale",
  "Per endocitosi legato alla tireoglobulina circolante",
  ], 0,
  "È un trasporto attivo secondario molto efficiente.",
  note="La sbobina definisce il trasporto «neutro». Nei testi di riferimento il simportatore (NIS) porta 2 Na⁺ per ogni I⁻, quindi è elettrogenico.")
q("m9t-05", T, "m", "290", "Perché la tiroide fa la via dei pentoso fosfati?", [
  "Per il NADPH che serve a produrre H₂O₂ per la perossidasi",
  "Per il ribosio 5-P necessario alla sintesi della tireoglobulina",
  "Per il NADPH che riduce lo iodio a ioduro prima della captazione",
  "Per l'eritrosio 4-P che fornisce l'anello aromatico della tiroxina",
  "Per il NADPH che serve alla deiodinasi per staccare lo iodio",
  ], 0,
  "Lo ioduro va ossidato per poter sostituire gli idrogeni delle tirosine.")
q("m9t-06", T, "m", "292", "Dove si trova il recettore degli ormoni tiroidei e come agisce?", [
  "Nel nucleo, come TR-RXR: l'ormone stacca il corepressore",
  "Nel citosol legato a Hsp70: l'ormone lo libera e il recettore entra nel nucleo",
  "Sulla membrana: attiva una Gs e il cAMP",
  "Sulla membrana: è un recettore tirosina chinasi come quello dell'insulina",
  "Nel mitocondrio: lega direttamente le proteine disaccoppianti",
  ], 0,
  "Il legame al DNA avviene con dita di zinco.")
q("m9t-07", T, "m", "292", "Quale proteina trasporta la maggior parte degli ormoni tiroidei nel sangue?", [
  "TBG", "Transtiretina", "Albumina", "Transcortina", "Transferrina"], 0,
  "Circa il 75%; il resto transtiretina e un po' di albumina.")
q("m9t-08", T, "a", "293", "Perché un paziente ipertiroideo ha sempre caldo?", [
  "Più Na⁺/K⁺-ATPasi e più proteine disaccoppianti",
  "Più glicogeno epatico, la cui sintesi libera calore",
  "Meno acidi grassi ossidati e più glucosio bruciato in glicolisi anaerobica",
  "Più colesterolo nelle membrane, che le rende meno permeabili al calore",
  "Più insulina, che stimola la termogenesi nel tessuto adiposo bianco",
  ], 0,
  "Il rapporto ATP/O scende: parte dell'energia si dissipa come calore. Aumenta il metabolismo basale.")
q("m9t-09", T, "a", "293", "Come abbassano il colesterolo plasmatico gli ormoni tiroidei?", [
  "Aumentano i recettori per le LDL nel fegato",
  "Inibiscono la HMG-CoA reduttasi in modo competitivo",
  "Bloccano l'assorbimento intestinale tramite NPC1L1",
  "Aumentano l'attività della LCAT sulle HDL",
  "Inibiscono la sintesi delle VLDL epatiche",
  ], 0,
  "Per questo l'ipotiroidismo può dare ipercolesterolemia.")
q("m9t-10", T, "a", "293", "Quale abbinamento malattia – meccanismo è corretto?", [
  "Graves – autoanticorpi che attivano il recettore del TSH",
  "Hashimoto – autoanticorpi che attivano il recettore del TSH",
  "Graves-Basedow – autoanticorpi contro la tiroide perossidasi",
  "Cretinismo – eccesso di ormoni tiroidei nello sviluppo",
  "Gozzo da carenza di iodio – eccesso di T3 circolante",
  ], 0,
  "Hashimoto: anticorpi contro tireoglobulina o perossidasi → ipotiroidismo (mixedema, gozzo, cretinismo nel bambino).")
q("m9t-11", T, "l", "291", "Quale microelemento contengono le deiodinasi?", [
  "Selenio", "Zinco", "Rame", "Molibdeno", "Manganese"], 0,
  "Il selenio è anche nella glutatione perossidasi. Lo zinco serve alle dita di zinco del recettore.")
q("m9t-12", T, "l", "291", "Che cosa si forma se la deiodinasi toglie lo iodio dall'anello interno del T4?", [
  "Reverse T3, inattivo", "T3 attivo", "T2 attivo", "Monoiodotirosina", "Tireoglobulina iodinata"], 0,
  "Togliendo lo iodio in 5' (anello esterno) si forma il T3 attivo.")
q("m9t-13", T, "h", "290", "La sbobina dice che dopo un incidente nucleare la tiroide viene danneggiata perché capta il cesio. Che cosa è corretto?", [
  "Il vero pericolo è lo iodio-131, captato come lo iodio stabile",
  "Il cesio-137 è l'unico radionuclide captato dal simportatore dello ioduro",
  "Il cesio sostituisce il selenio nelle deiodinasi e le inattiva",
  "L'uranio viene captato direttamente dalla tiroide come lo iodio",
  "Il cesio si lega alla tireoglobulina al posto dello iodio",
  ], 0,
  "Per questo si somministra iodio stabile (ioduro di potassio): satura la captazione.",
  note="Sbobina di Biochimica II, p. 290: c'è scritto che l'uranio decade in cesio e che la tiroide capta il cesio. Il radionuclide che la tiroide concentra è lo iodio-131; il cesio-137 si distribuisce soprattutto nei tessuti molli.")
q("m9t-14", T, "h", "292–293", "Quale effetto metabolico degli ormoni tiroidei è descritto correttamente?", [
  "Aumentano la mobilizzazione e l'ossidazione dei grassi",
  "Riducono la gluconeogenesi e sono ipoglicemizzanti",
  "Riducono la sintesi proteica come ormoni catabolici",
  "Riducono l'espressione della Na⁺/K⁺-ATPasi e il metabolismo basale",
  "Aumentano le LDL plasmatiche riducendo i recettori epatici",
  ], 0,
  "Sono anche iperglicemizzanti (gluconeogenesi e glicogenolisi) e anabolici proteici.")

# ── Calcio, paratormone e vitamina D (p. 294–298) ──────────────────────────
T = "m9-calcio"
q("m9c-01", T, "f", "294", "Quale ormone viene secreto quando la calcemia scende?", [
  "Paratormone", "Calcitonina", "Aldosterone", "Insulina", "Ossitocina"], 0,
  "Le paratiroidi hanno un recettore che sente il calcio; non dipendono dall'ipofisi.")
q("m9c-02", T, "f", "295", "Dove avvengono le due idrossilazioni che attivano la vitamina D?", [
  "25 nel fegato, 1 nel rene", "1 nel fegato, 25 nel rene", "Entrambe nel rene", "Entrambe nella pelle", "25 nell'intestino, 1 nel fegato"], 0,
  "Si forma il calcitriolo (1,25-diidrossicolecalciferolo); le idrossilasi sono citocromi P450.")
q("m9c-03", T, "f", "294", "Quanti amminoacidi ha il paratormone?", [
  "84", "34", "191", "9", "51"], 0,
  "Agisce con il cAMP.")
q("m9c-04", T, "m", "294", "Come libera calcio dall'osso l'osteoclasto?", [
  "Una ATPasi di tipo V acidifica la lacuna e scioglie i cristalli",
  "Una fosfatasi alcalina idrolizza il fosfato dell'idrossiapatite",
  "Una pompa Ca²⁺ ATP-dipendente estrae il calcio dai cristalli",
  "Il collagene viene idrolizzato e i cristalli si sciolgono da soli",
  "La calcitonina attiva una proteasi che scioglie i cristalli",
  ], 0,
  "La stessa ATPasi di tipo V acidifica i lisosomi.")
q("m9c-05", T, "m", "295", "Quali effetti ha il paratormone per alzare la calcemia?", [
  "Mobilizza calcio dall'osso e fa attivare la vitamina D nel rene",
  "Aumenta l'assorbimento intestinale direttamente e inibisce la vitamina D",
  "Aumenta l'escrezione renale e deposita calcio nelle ossa",
  "Inibisce gli osteoclasti e attiva la calcitonina",
  "Fa idrossilare la vitamina D in posizione 25 nel fegato",
  ], 0,
  "La vitamina D attiva aumenta poi l'assorbimento intestinale del calcio.")
q("m9c-06", T, "m", "296", "Come agisce il calcitriolo?", [
  "Su un recettore intracellulare che regola la trascrizione",
  "Su un recettore di membrana accoppiato a Gs",
  "Su un recettore tirosina chinasi dell'enterocita",
  "Legandosi direttamente al calcio nel lume intestinale",
  "Attivando la PKA nel citosol degli osteoclasti",
  ], 0,
  "Controlla circa 300 proteine: pompe del calcio intestinali, ma anche un enzima della sintesi della serotonina e proteine immunitarie.")
q("m9c-07", T, "a", "297–298", "Come aumentano la forza di contrazione cardiaca i glicosidi cardiaci?", [
  "Inibiscono la Na⁺/K⁺-ATPasi, così esce meno calcio",
  "Attivano la Na⁺/K⁺-ATPasi: con meno Na⁺ dentro, entra più calcio dai canali",
  "Aprono direttamente i canali del calcio di tipo L della membrana",
  "Inibiscono la pompa del calcio del reticolo sarcoplasmatico",
  "Aumentano il cAMP, che fosforila i canali del calcio",
  ], 0,
  "Il gradiente di Na⁺ ridotto rallenta l'estrusione di Ca²⁺ in scambio con Na⁺, quindi il calcio intracellulare sale.",
  note="Sbobina di Biochimica II, p. 298: c'è scritto che con più sodio dentro «viene favorito il rilascio del sodio all'esterno e quindi l'entrata del calcio». Più precisamente, il sodio alto riduce la forza che spinge lo scambiatore a far uscire il calcio.")
q("m9c-08", T, "a", "298", "Che cosa fa il calcio quando entra nel mitocondrio durante la contrazione?", [
  "Attiva PDH, isocitrato DH e α-chetoglutarato DH",
  "Inibisce l'ATP sintasi per risparmiare ATP durante la contrazione",
  "Attiva la PDH chinasi e riduce l'ingresso del piruvato nel ciclo",
  "Disaccoppia la catena respiratoria e produce calore",
  "Attiva la carnitina aciltrasferasi e blocca la glicolisi",
  ], 0,
  "Il calcio entra grazie al potenziale di membrana generato dalla catena respiratoria.")
q("m9c-09", T, "a", "296", "Perché insieme alla vitamina D si somministra spesso vitamina K2?", [
  "Per evitare che il calcio si depositi nei tessuti molli",
  "Perché la vitamina K2 serve all'idrossilazione in 1 della vitamina D",
  "Perché la vitamina K2 aumenta l'assorbimento intestinale della vitamina D",
  "Per evitare l'ipercoagulabilità causata dal calcio in eccesso",
  "Perché la vitamina D inattiva la vitamina K nel fegato",
  ], 0,
  "La dieta fornisce solo circa il 10% della vitamina D: il resto si forma nella pelle.")
q("m9c-10", T, "l", "294", "Quanti amminoacidi ha la calcitonina?", [
  "32", "84", "191", "9", "14"], 0,
  "Ha effetto opposto al paratormone: abbassa la calcemia.",
  note="Sbobina di Biochimica II, p. 294: la calcitonina è indicata come 34 amminoacidi. La calcitonina umana ne ha 32.")
q("m9c-11", T, "l", "295", "Come si chiama la forma non attiva della vitamina D3 sintetizzata dal colesterolo?", [
  "Colecalciferolo", "Calcitriolo", "Ergocalciferolo", "Calcidiolo", "7-deidrocolesterolo"], 0,
  "Colecalciferolo → (fegato) 25-idrossicolecalciferolo → (rene) calcitriolo.")
q("m9c-12", T, "h", "295", "La sbobina paragona l'ATPasi di tipo V all'«ATPasi di tipo 0» della fosforilazione ossidativa. Che cosa è corretto?", [
  "È simile all'ATP sintasi di tipo F, che lavora al contrario",
  "È identica alla Na⁺/K⁺-ATPasi di tipo P, che si fosforila durante il ciclo",
  "È simile alla H⁺/K⁺-ATPasi gastrica, che pompa anche potassio",
  "È una pompa ABC, come il trasportatore ABCA1 del colesterolo",
  "È simile al complesso IV, che pompa protoni senza ATP",
  ], 0,
  "Le ATPasi V e F hanno architettura rotatoria simile: la V consuma ATP per pompare H⁺, la F sintetizza ATP sfruttando il flusso di H⁺.",
  note="Sbobina di Biochimica II, p. 295: scrive «ATPasi di tipo 0». La classe giusta è il tipo F; «F₀» è il nome della sola parte di membrana.")
q("m9c-13", T, "h", "294", "Quale ruolo del calcio non è tra quelli elencati dalla sbobina?", [
  "Cofattore della glutatione perossidasi",
  "Attivatore della fosforilasi chinasi",
  "Attivatore della PDH fosfatasi",
  "Fattore della coagulazione del sangue",
  "Segnale per l'esocitosi delle vescicole",
  ], 0,
  "La glutatione perossidasi contiene selenio.")

# ── Ormoni steroidei: corticale e gonadi (p. 299–305) ──────────────────────
T = "m9-steroidi"
q("m9s-01", T, "f", "299", "Quanti atomi di carbonio hanno cortisolo, testosterone ed estradiolo?", [
  "21, 19, 18", "27, 21, 19", "19, 21, 18", "21, 18, 19", "18, 19, 21"], 0,
  "Il colesterolo ne ha 27: glucocorticoidi e mineralcorticoidi 21, androgeni 19, estrogeni 18.")
q("m9s-02", T, "f", "299", "Qual è il primo ormone steroideo che si forma dal colesterolo?", [
  "Pregnenolone", "Progesterone", "Cortisolo", "Testosterone", "Aldosterone"], 0,
  "Idrossilazioni in 20 e 22 e taglio della catena laterale (desmolasi), con NADPH e P450 mitocondriali.")
q("m9s-03", T, "f", "302", "Quale proteina trasporta il cortisolo nel sangue?", [
  "Transcortina", "TBG", "Albumina", "Transferrina", "Aptoglobina"], 0,
  "Lega circa il 90% del cortisolo (corticosteroid-binding globulin).")
q("m9s-04", T, "m", "301", "Quale effetto metabolico ha il cortisolo?", [
  "Stimola la gluconeogenesi e blocca i GLUT4",
  "Stimola la glicolisi muscolare e aumenta i GLUT4 in membrana",
  "Inibisce la proteolisi muscolare e la mobilizzazione degli acidi grassi",
  "Stimola la sintesi di glicogeno muscolare come l'insulina",
  "Riduce l'acidità gastrica per proteggere la mucosa",
  ], 0,
  "Mobilizza amminoacidi e acidi grassi; per questo la terapia cortisonica riduce la sensibilità all'insulina.")
q("m9s-05", T, "m", "302", "Perché nelle cellule renali l'aldosterone non viene «coperto» dal cortisolo, molto più abbondante?", [
  "Un enzima inattiva il cortisolo trasformandolo in cortisone",
  "Il cortisolo non attraversa la membrana delle cellule renali",
  "Il recettore dei mineralcorticoidi non lega mai il cortisolo",
  "La transcortina trattiene tutto il cortisolo nel sangue",
  "Il cortisolo viene coniugato con glucuronato nel rene",
  ], 0,
  "È la 11β-idrossisteroide deidrogenasi di tipo 2 (il nome non è nella sbobina).")
q("m9s-06", T, "m", "302", "Qual è la sequenza del sistema renina-angiotensina-aldosterone?", [
  "Renina: angiotensinogeno → angiotensina I; ACE: angiotensina I → angiotensina II → aldosterone",
  "ACE: angiotensinogeno → angiotensina I; renina: angiotensina I → angiotensina II → aldosterone",
  "Renina: angiotensina II → angiotensina I; ACE: angiotensina I → aldosterone",
  "Aldosterone → renina → angiotensinogeno → angiotensina II",
  "ACE2: angiotensinogeno → angiotensina II; renina: angiotensina II → aldosterone",
  ], 0,
  "Parte quando cala la pressione; l'angiotensina I è un decapeptide.")
q("m9s-07", T, "m", "301–302", "Quali idrossilazioni distinguono cortisolo, aldosterone e testosterone?", [
  "Cortisolo 11, 17, 21; aldosterone 11, 21; testosterone 17",
  "Cortisolo 11, 21; aldosterone 11, 17, 21; testosterone solo 11",
  "Cortisolo solo 17; aldosterone 11, 17; testosterone 11, 21",
  "Cortisolo 17, 21; aldosterone solo 11; testosterone 17, 21",
  "Tutti e tre sono idrossilati in 11, 17 e 21",
  ], 0,
  "Un deficit di uno di questi P450 sposta la sintesi verso altri ormoni, con effetti patologici.")
q("m9s-08", T, "a", "303", "Perché nel morbo di Addison autoimmune la pelle si pigmenta?", [
  "Senza cortisolo l'ipofisi produce molto ACTH",
  "Senza aldosterone il potassio alto stimola i melanociti",
  "Senza cortisolo la tirosinasi non è più inibita",
  "Gli autoanticorpi stimolano direttamente i melanociti",
  "Senza ormoni surrenalici aumenta la vitamina D cutanea",
  ], 0,
  "Si associano iposodiemia, iperkaliemia, ipotensione e ipoglicemia grave.")
q("m9s-09", T, "a", "303", "Quale quadro è tipico della sindrome di Cushing?", [
  "Iperglicemia, perdita muscolare e infezioni",
  "Ipoglicemia, aumento della massa muscolare, iperpigmentazione",
  "Iposodiemia, iperkaliemia, ipotensione grave",
  "Ipocalcemia, tetania, aumento del paratormone",
  "Poliuria con urine diluite e glicemia normale",
  ], 0,
  "Sono gli stessi effetti di una terapia cortisonica prolungata.")
q("m9s-10", T, "a", "304", "Che cosa succede in un neonato geneticamente maschio senza 5α-reduttasi?", [
  "I genitali esterni maschili non si sviluppano",
  "Si sviluppano genitali femminili interni, perché manca il testosterone",
  "I genitali sono normali, ma alla pubertà manca l'aromatasi",
  "Lo sviluppo è normale, perché il testosterone basta in ogni fase",
  "Si ha iperplasia surrenalica per eccesso di ACTH",
  ], 0,
  "Il DHT agisce nello sviluppo embrionale, il testosterone alla pubertà. L'enzima usa NADPH.")
q("m9s-11", T, "l", "304", "Quale enzima forma l'estradiolo dal testosterone?", [
  "Aromatasi", "5α-reduttasi", "Desmolasi", "17α-idrossilasi", "21-idrossilasi"], 0,
  "Crea l'anello A aromatico: è l'unico caso in cui sappiamo formare un anello aromatico.")
q("m9s-12", T, "l", "300", "Con quale proteina è legato nel citosol il recettore degli steroidi, secondo la sbobina?", [
  "Una chaperon", "La calmodulina", "La β-arrestina", "Una proteina G", "La clatrina"], 0,
  "Legato l'ormone, il recettore dimerizza e si lega a sequenze palindromiche del DNA con le dita di zinco.",
  note="La sbobina cita Hsp70; nei testi di riferimento la chaperon tipica dei recettori steroidei è Hsp90 (con Hsp70 come cochaperon).")
q("m9s-13", T, "h", "303", "Quale affermazione sull'angiotensina e sui suoi enzimi è corretta?", [
  "L'ACE2 inattiva l'angiotensina II ed è il recettore di SARS-CoV-2",
  "L'ACE attiva la bradichinina, che causa vasocostrizione",
  "L'ACE2 converte l'angiotensina I in angiotensina II nei polmoni",
  "La renina è una carbossipeptidasi che agisce sull'angiotensina II",
  "Gli ACE-inibitori bloccano la sintesi dell'angiotensinogeno nel fegato",
  ], 0,
  "L'ACE degrada anche la bradichinina, un vasodilatatore.",
  note="Sbobina di Biochimica II, p. 303: l'angiotensina III è definita un prodotto inattivo. Nei testi di riferimento l'angiotensina III conserva attività biologica (stimola l'aldosterone).")
q("m9s-14", T, "h", "305", "Un deficit di un citocromo P450 della steroidogenesi surrenalica (per esempio la 21-idrossilasi) causa tipicamente:", [
  "Poco cortisolo, ACTH alto, troppi androgeni",
  "Molto cortisolo, ACTH basso e atrofia della corticale",
  "Poco cortisolo, ACTH basso e assenza di androgeni",
  "Molto aldosterone, renina alta e ipotensione",
  "Nessun effetto, perché le vie sono intercambiabili",
  ], 0,
  "Le vie sono intercambiabili e gli intermedi hanno attività biologica: un blocco ne fa accumulare alcuni.",
  note="Sbobina di Biochimica II, p. 305: la conseguenza è chiamata genericamente «insufficienza surrenalica». Il quadro tipico è l'iperplasia surrenalica congenita; il dettaglio della 21-idrossilasi non è nella sbobina.")

# ── Mediatori locali ed eicosanoidi (p. 306–310) ───────────────────────────
T = "m9-locali"
q("m9l-01", T, "f", "306", "Da quale amminoacido si forma l'ossido nitrico?", [
  "Arginina", "Citrullina", "Ornitina", "Glutammina", "Lisina"], 0,
  "NO sintasi: arginina + O₂ + NADPH → citrullina + NO.")
q("m9l-02", T, "f", "306", "Quale ormone gastrointestinale stimola la fame?", [
  "Grelina", "GLP-1", "Leptina", "GLP-2", "Colecistochinina"], 0,
  "GLP-1 e GLP-2 sono prodotti dall'intestino e danno sazietà.")
q("m9l-03", T, "f", "308", "Da quale acido grasso deriva l'acido arachidonico?", [
  "Acido linoleico (ω-6, 18 C)", "Acido linolenico (ω-3, 18 C)", "Acido oleico (ω-9, 18 C)", "Acido palmitico (16 C)", "Acido stearico (18 C)"], 0,
  "L'acido arachidonico ha 20 atomi di carbonio; l'acido linoleico è essenziale.")
q("m9l-04", T, "m", "306", "Perché l'NO agisce solo localmente?", [
  "È un radicale libero con emivita molto breve",
  "È un peptide degradato subito dalle peptidasi",
  "È idrofilico e non attraversa le membrane",
  "Viene legato dall'albumina appena prodotto",
  "Viene secreto solo nelle sinapsi nervose",
  ], 0,
  "Rilassa la muscolatura liscia: abbassa la pressione e permette l'erezione.")
q("m9l-05", T, "m", "307", "Quale enzima libera l'acido arachidonico dai fosfolipidi di membrana?", [
  "Fosfolipasi A2, che taglia in posizione 2",
  "Fosfolipasi C, che libera inositolo trisfosfato",
  "Lipasi ormone-sensibile, che taglia i diacilgliceroli",
  "Lipoproteina lipasi, che taglia i trigliceridi",
  "Fosfolipasi D, che libera la testa polare",
  ], 0,
  "Dall'arachidonato si formano prostaglandine, trombossani e leucotrieni.")
q("m9l-06", T, "m", "307", "Perché i FANS che inibiscono la COX-1 possono danneggiare lo stomaco?", [
  "La COX-1 gastrica fa prostaglandine che stimolano il muco",
  "La COX-1 gastrica inibisce la pompa protonica e riduce l'acidità",
  "La COX-1 gastrica produce leucotrieni che proteggono la mucosa",
  "L'inibizione della COX-1 aumenta la produzione di gastrina",
  "L'inibizione della COX-1 attiva il pepsinogeno nella mucosa",
  ], 0,
  "La COX-2 è invece specifica dell'infiammazione.")
q("m9l-07", T, "a", "308", "Che cosa significa che un acido grasso è ω-3?", [
  "Il primo doppio legame è al C3 dall'estremità metilica",
  "Il primo doppio legame è al terzo carbonio contando dal carbossile",
  "Ha tre doppi legami in tutta la catena",
  "Ha 3 atomi di carbonio in meno dell'acido grasso di origine",
  "Il terzo carbonio porta un gruppo ossidrile",
  ], 0,
  "L'acido linolenico (ω-3) dà EPA e DHA, importanti per il SNC.",
  note="La sbobina dice «a partire da C-terminale»: si intende l'estremità metilica (carbonio ω), non quella carbossilica.")
q("m9l-08", T, "a", "308–309", "Quale rapporto tra ω-6 e ω-3 indica la sbobina come ideale?", [
  "Circa 4:1", "Circa 1:4", "Circa 20:1", "Circa 1:1 esatto", "Circa 50:1"], 0,
  "Nella dieta occidentale prevalgono di molto gli ω-6; l'olio d'oliva ha circa 11:1, quello di lino è ricco di ω-3.")
q("m9l-09", T, "a", "309", "Quali grassi alimentari peggiorano di più il profilo LDL/HDL secondo la sbobina?", [
  "Gli acidi grassi trans",
  "Gli acidi grassi monoinsaturi",
  "Gli acidi grassi ω-3",
  "Gli acidi grassi a catena media",
  "Gli acidi grassi polinsaturi ω-6",
  ], 0,
  "Si formano anche con fritture prolungate. I monoinsaturi (olio d'oliva) riducono le LDL.")
q("m9l-10", T, "l", "307", "Quale isoforma della cicloossigenasi è specifica dell'infiammazione?", [
  "COX-2", "COX-1", "COX-3", "Lipossigenasi 5", "Trombossano sintasi"], 0,
  "L'aspirina inibisce la COX-1 (in modo irreversibile).")
q("m9l-11", T, "h", "307", "Quale affermazione sulle NO sintasi è corretta secondo i testi di riferimento?", [
  "Quella dei macrofagi non dipende dal calcio; quella endoteliale sì",
  "L'isoforma dei macrofagi dipende dal calcio; quella endoteliale ne è indipendente",
  "Tutte le isoforme sono indipendenti dal calcio e costitutive",
  "L'isoforma dei macrofagi usa NADH invece di NADPH",
  "L'NO dei macrofagi si forma dalla citrullina",
  ], 0,
  "L'NO dei macrofagi, con il superossido della NADPH ossidasi, uccide i batteri.",
  note="Sbobina di Biochimica II, p. 307: l'isoforma dei macrofagi è indicata come calcio-dipendente e quella epiteliale come calcio-indipendente. È il contrario: iNOS (macrofagi) è calcio-indipendente, eNOS e nNOS dipendono dal calcio-calmodulina.")
q("m9l-12", T, "h", "310", "Secondo la sbobina, che effetto hanno gli ω-3 sul rischio coronarico?", [
  "Lo riducono, ma non agiscono su LDL e HDL",
  "Lo aumentano, perché riducono le HDL",
  "Lo riducono abbassando direttamente le LDL",
  "Non hanno alcun effetto sul rischio coronarico",
  "Lo aumentano, perché favoriscono l'infiammazione",
  ], 0,
  "Gli ω-6 invece aumentano l'infiammazione e hanno un effetto negativo sulle HDL.")
