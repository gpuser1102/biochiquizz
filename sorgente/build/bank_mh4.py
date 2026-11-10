"""Domande HARD (livello h), modulo 4: glicogeno (pp. 115–139)."""
from bank_common import q

T = "m4-degradazione"
q("h4d-01", T, "h", "116", "Perché la glicogeno fosforilasi usa il Pi invece dell'acqua (fosforolisi invece di idrolisi)?", [
  "Si forma G1P già fosforilato: si risparmia l'ATP dell'esochinasi",
  "L'acqua non può entrare nel sito attivo per motivi sterici",
  'Si forma glucosio libero, che esce più facilmente dalla cellula',
  'La fosforolisi produce direttamente una molecola di ATP',
  "Il Pi stabilizza la forma R dell'enzima e lo rende più veloce",
  ], 0,
  'Il G1P carico resta nella cellula. Nel muscolo la glicolisi da glicogeno rende 3 ATP netti per unità di glucosio invece di 2.')
q("h4d-02", T, "h", "115–116", "La glicogeno fosforilasi si ferma a 4 residui da una ramificazione. Quale sequenza completa la degradazione del ramo?", [
  "La transferasi sposta 3 residui; l'α-1,6-glucosidasi libera l'ultimo come glucosio",
  'La fosforilasi taglia anche il legame α-1,6 e libera glucosio 1-fosfato dal punto di ramificazione',
  "L'α-1,6-glucosidasi stacca tutti e 4 i residui come glucosio 1-fosfato",
  'La transferasi idrolizza il legame α-1,6 e la glucosidasi sposta i residui',
  'La glicogenina rimuove il ramo e lo trasferisce su una nuova catena',
  ], 0,
  'Transferasi e glucosidasi sono due attività dello stesso enzima deramificante. Dal punto di ramificazione esce glucosio libero (circa il 10% dei residui), non G1P.',
  note="Sbobina di Biochimica II, pp. 115–116: prima c'è scritto che la fosforilasi si ferma a 4 residui dalla ramificazione, poi che la transferasi interviene «a 3 residui dal glucosio con legame α-1,6». I residui rimasti sono 4: 3 vengono trasferiti, 1 resta legato in α-1,6.")
q("h4d-03", T, "h", "117", "Perché il muscolo non può cedere glucosio al sangue dopo aver degradato il proprio glicogeno?", [
  'Non ha la glucosio 6-fosfatasi',
  'Non ha la glicogeno fosforilasi',
  'Il suo glicogeno non ha ramificazioni',
  'Non ha trasportatori GLUT in membrana',
  'Non converte il G1P in G6P',
  ], 0,
  'Il G6P resta nella cellula e va solo in glicolisi: il glicogeno muscolare ha funzione energetica locale, quello epatico mantiene la glicemia.')
q("h4d-04", T, "h", "117", "Dove avviene la reazione della glucosio 6-fosfatasi e quale conseguenza ha un difetto del trasportatore del G6P?", [
  'Nel lume del reticolo; un difetto del trasportatore del G6P dà la glicogenosi Ib',
  'Nel citosol; un difetto del trasportatore del G6P non ha conseguenze',
  'Nel mitocondrio; un difetto del trasportatore del G6P dà la glicogenosi di tipo II (Pompe)',
  'Nel lisosoma; un difetto del trasportatore dà la malattia di Pompe',
  'Sulla membrana plasmatica; un difetto del trasportatore aumenta la glicemia',
  ], 0,
  'Servono tre trasportatori: G6P (dentro), Pi e glucosio (fuori). Il difetto del trasportatore T1 dà lo stesso quadro del deficit enzimatico.')
q("h4d-05", T, "h", "118–119", "Quale ruolo ha il piridossal fosfato (vitamina B6) nella glicogeno fosforilasi?", [
  'Il suo fosfato fa da catalizzatore acido-base per il Pi',
  "Lega il glucosio con una base di Schiff sull'aldeide",
  'Trasporta elettroni come il FAD nelle deidrogenasi',
  'Fornisce il fosfato che finisce nel glucosio 1-fosfato',
  "Lega l'AMP allosterico nella forma b dell'enzima",
  ], 0,
  "Aiuta il Pi a cedere il protone al legame glicosidico; non usa il gruppo aldeidico come nelle transaminasi. È legato a una lisina dell'enzima.")
q("h4d-06", T, "h", "116", "La fosfoglucomutasi converte G1P in G6P. Qual è il suo meccanismo?", [
  'Una serina fosforilata passa il fosfato al C6 (glucosio 1,6-bisfosfato)',
  "L'ATP fosforila il C6 e un'idrolasi stacca il fosfato dal C1",
  'Il fosfato migra spontaneamente dal C1 al C6 senza intermedi',
  "Un'istidina fosforilata cede il fosfato al C1 del glucosio 6-P e lo riprende dal C6",
  "L'UTP trasferisce il fosfato al C6 formando UDP-glucosio",
  ], 0,
  "Poi l'enzima riprende il fosfato dal C1. Meccanismo analogo alla fosfoglicerato mutasi (che usa un'istidina).")
q("h4d-07", T, "h", "117", "Perché la struttura molto ramificata del glicogeno è utile al fegato?", [
  'Moltiplica le estremità non riducenti su cui agisce la fosforilasi',
  'Rende il glicogeno insolubile e quindi osmoticamente inerte',
  "Aumenta la pressione osmotica e richiama acqua nell'epatocita",
  "Permette alla fosforilasi di partire anche dall'estremità riducente",
  'Rallenta la degradazione e protegge le riserve tra i pasti',
  ], 0,
  'Si libera rapidamente molto glucosio, e solo con alte concentrazioni i GLUT2 (bassa affinità) lo portano fuori. Un polimero ramificato si allunga e si accorcia più in fretta di uno lineare.')
q("h4d-08", T, "h", "115", "Perché il glucosio viene immagazzinato come glicogeno e non come glucosio libero?", [
  'Il glucosio libero aumenterebbe enormemente la pressione osmotica',
  'Il glucosio libero è tossico per il fegato e per il muscolo',
  'Il glicogeno contiene più energia per grammo dei trigliceridi',
  'Il glicogeno è insolubile e non lega acqua',
  'Il glucosio libero uscirebbe comunque dalla cellula con i GLUT',
  ], 0,
  'Un polimero è osmoticamente quasi inerte. I grassi restano la riserva più concentrata di energia.')

T = "m4-sintesi"
q("h4s-01", T, "h", "124", "Qual è il donatore di glucosio per la glicogeno sintasi e come si forma?", [
  'UDP-glucosio, da glucosio 1-fosfato + UTP',
  'Glucosio 6-fosfato, legato direttamente',
  'Glucosio 1-fosfato, attivato con ATP',
  'GDP-glucosio, da glucosio 1-fosfato + GTP',
  'CDP-glucosio, da glucosio 6-fosfato + CTP',
  ], 0,
  "La UDP-glucosio pirofosforilasi forma UDP-glucosio + PPi; l'idrolisi del PPi rende la reazione irreversibile. L'UTP è il nucleotide delle biosintesi dei carboidrati.")
q("h4s-02", T, "h", "124", "Che cosa fa la glicogenina?", [
  'Si autoglucosila su una tirosina e forma il primer per la sintasi',
  'Crea le ramificazioni α-1,6 nelle catene in crescita prodotte dalla sintasi',
  "Degrada il glicogeno all'interno dei lisosomi",
  'Attiva la glicogeno fosforilasi trasformandola in forma a',
  'Trasporta il glucosio 6-fosfato dentro il reticolo',
  ], 0,
  'Lega il primo glucosio da UDP-glucosio e allunga da sola un breve primer (circa 7 residui), poi resta al centro della molecola. La glicogeno sintasi non sa iniziare una catena da zero.')
q("h4s-03", T, "h", "124", "Quali nucleosidi trifosfato si consumano per inserire nel glicogeno un glucosio che entra nella cellula come glucosio libero?", [
  '1 ATP (esochinasi/glucochinasi) e 1 UTP (che dà UDP + PPi; il PPi viene poi idrolizzato)',
  'Solo 1 UTP, perché il glucosio 1-fosfato si forma senza consumo di ATP',
  '1 ATP e 1 GTP',
  '2 ATP e nessun UTP',
  'Nessuno: la glicogeno sintasi non richiede energia',
  ], 0,
  "Il glucosio 1-fosfato viene dal G6P (fosfoglucomutasi, all'equilibrio). L'UDP si ricarica a UTP con ATP (nucleoside difosfato chinasi).")
q("h4s-04", T, "h", "124", "Quale enzima crea le ramificazioni del glicogeno?", [
  "L'enzima ramificante (amilo-1,4→1,6-transglicosilasi)",
  'La glicogeno sintasi, quando cambia conformazione',
  'La glicogenina, nelle fasi iniziali della sintesi',
  "L'α-1,6-glucosidasi, che lavora anche in senso inverso",
  'La fosfoglucomutasi, che sposta il legame dal C1 al C6',
  ], 0,
  'Sposta un segmento di catena su un legame α-1,6; la sintasi allunga poi entrambe le catene.')
q("h4s-05", T, "h", "125", "Il G6P attiva la glicogeno sintasi b (fosforilata). A che cosa serve?", [
  "Avvia la sintesi di glicogeno anche prima che agisca l'insulina",
  'Inattiva la glicogeno sintasi a quando il G6P è in eccesso',
  'Attiva la glicogeno fosforilasi per bilanciare il flusso',
  'Blocca la glicolisi epatica per deviare tutto il G6P verso la sintesi del glicogeno',
  'Fa uscire il glucosio dal fegato tramite i GLUT2',
  ], 0,
  'È un effettore allosterico eterotropico positivo della forma b (fosforilata), uguale in fegato e muscolo.')
q("h4s-06", T, "h", "135", "Perché una dieta ricca di grassi e povera di carboidrati non ricostituisce il glicogeno muscolare dopo uno sforzo?", [
  "L'acetil-CoA dei grassi non può tornare a piruvato",
  'Gli acidi grassi inibiscono direttamente la glicogeno sintasi',
  'Il glicogeno si forma solo a partire dalle proteine',
  'Gli acidi grassi inibiscono la glicogenina',
  "Senza carboidrati l'insulina non viene mai secreta",
  ], 0,
  "La PDH è irreversibile: non c'è sintesi netta di glucosio dai grassi. Servono carboidrati, meglio subito dopo lo sforzo.",
  note="Sbobina di Biochimica II, p. 135: c'è scritto che dall'acetil-CoA non si riottiene il piruvato perché «la reazione della piruvato carbossilasi è irreversibile». L'irreversibile in questione è la piruvato deidrogenasi (piruvato → acetil-CoA).")
q("h4s-07", T, "h", "124–125", "Quale coppia di enzimi va regolata in modo reciproco per evitare un ciclo futile nel metabolismo del glicogeno?", [
  'Glicogeno sintasi e glicogeno fosforilasi',
  'Glicogeno sintasi e glicogenina',
  'Fosfoglucomutasi e glucosio 6-fosfatasi',
  'Enzima ramificante e enzima deramificante',
  'Esochinasi e UDP-glucosio pirofosforilasi',
  ], 0,
  "Quando una è attiva l'altra deve essere inattiva: le fosforilazioni ormonali hanno effetti opposti sui due enzimi.")
q("h4s-08", T, "h", "124", "In quale direzione la glicogeno sintasi allunga la catena e quale legame forma?", [
  "All'estremità non riducente, con legame α-1,4",
  "All'estremità riducente, con legame α-1,6",
  "All'estremità non riducente, con legame β-1,4",
  "All'estremità riducente, con legame α-1,4",
  'In entrambe le direzioni, con legame α-1,4',
  ], 0,
  'Le estremità non riducenti sono anche quelle su cui lavora la fosforilasi.')

T = "m4-regolazione"
q("h4r-01", T, "h", "119", "Qual è la relazione tra le forme a/b e gli stati R/T della glicogeno fosforilasi?", [
  'La forma a è soprattutto in R; la b soprattutto in T',
  'La forma a è sempre in T e la b sempre in R',
  'La forma b è quella fosforilata, ed è la più attiva nello stato R',
  'Le forme a e b non hanno stati conformazionali',
  'La forma a è inattiva e la b è attiva',
  ], 0,
  'La fosforilasi a è fosforilata, la b defosforilata ma può passare in R con effettori allosterici: regolazione covalente e allosterica si sommano.')
q("h4r-02", T, "h", "119–120", "Un muscolo si contrae senza adrenalina in circolo. Quale segnale attiva la fosforilasi b?", [
  "L'AMP, che sposta la fosforilasi b in R",
  'Il glucagone, tramite il cAMP',
  'Il glucosio, che si lega al sito allosterico',
  "L'insulina, tramite la PKB",
  'Il citrato, che esce dal mitocondrio',
  ], 0,
  "L'AMP aumenta quando cala l'ATP; ATP e G6P riportano la fosforilasi b in T. Nel fegato l'AMP non attiva la fosforilasi.")
q("h4r-03", T, "h", "120", "Nel fegato, quale effettore allosterico inattiva la fosforilasi a e perché ha senso?", [
  'Il glucosio, che ferma la glicogenolisi dopo il pasto',
  "L'AMP, che nel fegato segnala un eccesso di energia dopo il pasto",
  'Il Ca²⁺, rilasciato dal reticolo dopo il pasto',
  'Il cAMP, che si lega al sito catalitico',
  "L'adrenalina, che si lega al sito allosterico",
  ], 0,
  "Il fegato smette subito di degradare glicogeno, prima ancora che arrivi l'insulina: è un sensore della glicemia.")
q("h4r-04", T, "h", "130", "Nel fegato, come fa il glucosio ad attivare anche la sintesi del glicogeno?", [
  'La fosforilasi a in T libera la PP1, che attiva la glicogeno sintasi',
  'Il glucosio attiva direttamente la glicogeno sintasi chinasi 3, che attiva la sintasi',
  'Il glucosio fosforila la glicogeno sintasi rendendola attiva',
  'Il glucosio blocca la PP1 e così la sintasi resta fosforilata',
  'Il glucosio attiva la PKA, che defosforila la glicogeno sintasi',
  ], 0,
  'La fosforilasi a in R lega e inibisce la PP1; il glucosio la porta in T, la PP1 si libera, la defosforila (→ b) e poi defosforila la glicogeno sintasi.')
q("h4r-05", T, "h", "126", "Come agisce l'insulina sulla glicogeno sintasi?", [
  'Attiva la PKB, che inattiva la GSK3: la sintasi resta defosforilata',
  'Attiva la GSK3, che fosforila la glicogeno sintasi e la porta nella forma attiva',
  'Attiva la PKA, che fosforila direttamente la glicogeno sintasi',
  'Inibisce la PP1, così la sintasi resta fosforilata e attiva',
  'Aumenta il cAMP, che si lega alla glicogeno sintasi',
  ], 0,
  'La PKB fosforila e inattiva la GSK3; la PP1 rimuove i fosfati residui. La glicogeno sintasi è attiva quando è defosforilata.',
  note="Sbobina di Biochimica II, p. 126: c'è scritto che la GSK3 fosforila la glicogeno sintasi «attivandola» e, poco dopo, che così «la glicogeno fosforilasi rimanga nella forma defosforilata, attiva». La fosforilazione da parte della GSK3 inattiva la glicogeno sintasi, ed è la sintasi (non la fosforilasi) che l'insulina mantiene defosforilata e attiva.")
q("h4r-06", T, "h", "127–128", "Perché durante la glicogenolisi indotta da ormoni la PP1 deve essere inibita?", [
  'Per evitare un ciclo futile di fosforilazioni e defosforilazioni',
  'Perché la PP1 degrada direttamente il glicogeno',
  'Perché la PP1 attiva la glicogeno fosforilasi',
  "Perché la PP1 sintetizza cAMP e prolungherebbe troppo il segnale dell'adrenalina",
  'Perché la PP1 consuma il glucosio liberato',
  ], 0,
  "Altrimenti defosforilerebbe subito fosforilasi a e fosforilasi chinasi, sprecando ATP. Nel muscolo l'adrenalina stacca la PP1 da GM e fosforila un suo inibitore.")
q("h4r-07", T, "h", "126–127", "Perché la GSK3 può fosforilare la glicogeno sintasi solo dopo un'altra chinasi?", [
  'Riconosce un fosfato già messo dalla caseina chinasi 2',
  'È attivata solo dal cAMP prodotto dal glucagone',
  'Lavora solo sulla forma a della glicogeno fosforilasi',
  "Richiede l'insulina per essere attivata",
  "Usa il GTP invece dell'ATP come donatore",
  ], 0,
  'È un priming: la glicogeno sintasi ha più siti di fosforilazione. A riposo il sito di riconoscimento della GSK3 è occupato da uno pseudosubstrato.')
q("h4r-08", T, "h", "128–130", "Quale ruolo hanno le proteine GM (muscolo) e GL (fegato)?", [
  'Ancorano al glicogeno la PP1 e gli enzimi del suo metabolismo',
  'Sono le isoforme muscolare ed epatica della glicogeno sintasi',
  'Sono i recettori di membrana di glucagone e adrenalina',
  'Sono i trasportatori del G6P nel reticolo endoplasmatico',
  'Sono inibitori della glicogenina nei due tessuti',
  ], 0,
  "Formano un'unità operativa; la loro fosforilazione decide se la PP1 è legata e attiva. L'insulina fosforila GM sul sito 1 (PP1 attiva), l'adrenalina sul sito 2 (PP1 si stacca).")

T = "m4-ormoni"
q("h4o-01", T, "h", "120–121", "Quale sequenza descrive l'azione del glucagone sul glicogeno epatico?", [
  'Gs → adenilato ciclasi → cAMP → PKA → fosforilasi chinasi → fosforilasi a',
  'Recettore tirosin-chinasico → PKB → GSK3 → fosforilasi chinasi → fosforilasi a',
  'Gi → calo del cAMP → PP1 inattiva → fosforilasi a',
  'Recettore nucleare → trascrizione del gene della fosforilasi',
  'Gq → PLC → IP₃ → Ca²⁺ → glicogeno sintasi attiva',
  ], 0,
  'Il recettore ha 7 eliche transmembrana. La PKA fosforila anche la glicogeno sintasi, inattivandola.',
  note="Sbobina di Biochimica II, p. 131: c'è scritto che il glucagone aumenta i livelli di «AMP» nel fegato; è il cAMP (AMP ciclico).")
q("h4o-02", T, "h", "123", "Perché la cascata del cAMP è considerata un sistema di amplificazione?", [
  'Perché ogni tappa è enzimatica e moltiplica il segnale',
  'Perché il glucagone si moltiplica nel sangue',
  'Perché ogni recettore lega molte molecole di ormone',
  'Perché il cAMP è un enzima che degrada il glicogeno',
  'Perché il glicogeno attiva il proprio recettore',
  ], 0,
  'Pochi ormoni attivano molte adenilato ciclasi, ogni PKA molte fosforilasi chinasi, e così via: da poche molecole di ormone si ottengono 10.000 e più molecole di glucosio.')
q("h4o-03", T, "h", "121", "Come viene completamente attivata la fosforilasi chinasi muscolare?", [
  'Con fosforilazione (PKA) e Ca²⁺ sulla subunità δ',
  'Solo con il cAMP legato direttamente alla subunità γ',
  "Solo con l'insulina tramite la PKB",
  'Con il glucosio legato al sito allosterico',
  "Con l'AMP legato alla subunità α",
  ], 0,
  "La subunità δ è una calmodulina; ciascun segnale da solo dà un'attivazione parziale. Il Ca²⁺ della contrazione collega il lavoro muscolare alla glicogenolisi.")
q("h4o-04", T, "h", "122", "Durante una camminata, senza adrenalina in circolo, che cosa attiva la glicogenolisi muscolare?", [
  'Il Ca²⁺ del reticolo sarcoplasmatico, che attiva la fosforilasi chinasi',
  'Il glucagone, che si lega ai recettori della fibra muscolare e attiva la PKA',
  "L'insulina, che aumenta durante l'attività fisica leggera",
  'Il cortisolo, che induce la fosforilasi muscolare',
  'Il glucosio plasmatico, che si lega alla fosforilasi',
  ], 0,
  "Il Ca²⁺ è liberato con lo stimolo nervoso; anche l'AMP attiva la fosforilasi b. Il muscolo non ha recettori per il glucagone.")
q("h4o-05", T, "h", "121–122", "L'adrenalina ha effetti diversi su fegato e muscolo. Quale affermazione è corretta?", [
  'Fegato: glicemia ↑; muscolo: glucosio per la glicolisi locale',
  'Muscolo: glucosio ceduto al sangue; fegato: nessun effetto',
  'Fegato: glicogenolisi bloccata; muscolo: glicogenolisi attivata',
  'Agisce solo sul tessuto adiposo e non sul glicogeno',
  'Attiva la glicogeno sintasi in entrambi i tessuti',
  ], 0,
  "In entrambi stimola la glicogenolisi (ormone dell'attacco o fuga), ma il glucosio ha destini diversi.")
q("h4o-06", T, "h", "131–132", "Un paziente con insulinoma (eccesso di insulina) a digiuno. Che cosa succede al glicogeno epatico e alla glicemia?", [
  'Il fegato non rilascia glucosio: ipoglicemia',
  'La fosforilasi si attiva e la glicemia sale',
  'Il glicogeno si esaurisce e la glicemia aumenta',
  'Nessun effetto, perché prevale il glucagone',
  'Il glicogeno muscolare passa nel sangue',
  ], 0,
  "PKB e PP1 restano attive: la glicogeno sintasi lavora e la fosforilasi è spenta. L'insulina è l'unico ormone ipoglicemizzante.")
q("h4o-07", T, "h", "131", "Perché il glucosio da solo blocca la glicogenolisi epatica prima che arrivi l'insulina?", [
  'La secrezione di insulina richiede tempo, il glucosio portale agisce subito',
  'Il glucosio inibisce il recettore del glucagone sugli epatociti',
  'Il glucosio attiva la PKA degli epatociti, che inattiva direttamente la fosforilasi a',
  "Il glucosio agisce come un ormone sul recettore dell'insulina",
  "L'insulina non ha alcun effetto sul glicogeno del fegato",
  ], 0,
  'Nella cellula β servono glicolisi, Krebs, fosforilazione ossidativa ed esocitosi. Il glucosio della vena porta agisce subito sulla fosforilasi a: il glicogeno epatico viene preservato appena si mangia.',
  note="Sbobina di Biochimica II, p. 131: c'è scritto che l'insulina è «propriamente anabolica, quindi di distruzione del glicogeno». Va letto «di costruzione».")
q("h4o-08", T, "h", "132", "Dopo un pasto, che cosa fa la maggior parte del glucosio che entra nell'epatocita, secondo il corso?", [
  "La maggior parte entra nella glicolisi, stimolata dall'insulina",
  'Esce subito dal fegato tramite i GLUT2',
  "Diventa tutto glicogeno epatico, perché la glicolisi è inibita dall'insulina",
  'Viene ossidato a lattato e ceduto al sangue',
  'Viene convertito in corpi chetonici',
  ], 0,
  'In parte inibisce la fosforilasi e attiva la PP1 (sintesi di glicogeno). Dalla glicolisi epatica deriva anche acetil-CoA per la lipogenesi.')

T = "m4-attivita"
q("h4a-01", T, "h", "133", "In uno scatto di 10 secondi, in quale ordine intervengono le fonti di ATP?", [
  'ATP → fosfocreatina → glicolisi anaerobia',
  'β-ossidazione → fosfocreatina → glicolisi',
  'Metabolismo aerobio → fosfocreatina → ATP',
  'Gluconeogenesi → glicogeno → fosfocreatina',
  'Glicolisi dal glucosio plasmatico soltanto',
  ], 0,
  'La glicolisi anaerobia usa il glicogeno; il metabolismo aerobio cresce dopo. Negli sforzi lunghi prevale il metabolismo aerobio, sempre più di acidi grassi.',
  note="Sbobina di Biochimica II, p. 133: le curve del grafico sono chiamate «anabolismo aerobio» e «anabolismo anaerobio»; si intende metabolismo (catabolismo) aerobio e anaerobio.")
q("h4a-02", T, "h", "134", "In quale tipo di sforzo il glicogeno muscolare NON viene praticamente consumato?", [
  'Sforzo leggero (circa 25% del VO₂max)',
  'Sforzo intenso di breve durata (circa 85% del VO₂max)',
  'Sforzo moderato e prolungato',
  'Scatto alla massima intensità',
  'Sollevamento pesi ripetuto',
  ], 0,
  'È sostenuto soprattutto da acidi grassi e glucosio plasmatico. Lo sforzo intenso esaurisce il glicogeno in poco tempo.')
q("h4a-03", T, "h", "135", "Qual è la strategia migliore per ricostituire il glicogeno dopo una gara?", [
  'Carboidrati subito dopo e a intervalli regolari nelle 24 ore',
  'Digiuno per 24 ore per stimolare la gluconeogenesi',
  'Solo proteine, che il muscolo trasforma direttamente in glicogeno',
  'Solo grassi, con una dieta chetogenica',
  'Carboidrati solo dopo 48 ore di riposo',
  ], 0,
  'Subito dopo lo sforzo la sintesi di glicogeno è particolarmente attiva.')
q("h4a-04", T, "h", "135", "Che cos'è la supercompensazione del glicogeno?", [
  "Il glicogeno, dopo l'esaurimento, sale oltre i valori iniziali con molti carboidrati",
  'La sintesi di glicogeno muscolare a partire dagli acidi grassi della dieta dopo uno sforzo',
  'La degradazione molto rapida del glicogeno durante lo sforzo intenso',
  'Il trasferimento diretto di glicogeno dal fegato al muscolo',
  "L'aumento della glicemia durante lo sforzo per effetto dell'adrenalina",
  ], 0,
  'Con una dieta ricca di carboidrati succede in circa due giorni; a digiuno o con dieta povera di carboidrati il glicogeno non si ricostituisce.')
q("h4a-05", T, "h", "135", "Perché le proteine sono una fonte poco efficiente per ricostituire il glicogeno?", [
  "Pochi amminoacidi sono glucogenici e servono soprattutto per l'energia",
  'Le proteine non contengono atomi di carbonio utilizzabili',
  'Nessun amminoacido può essere convertito in glucosio',
  'Le proteine inibiscono direttamente la glicogeno sintasi e bloccano la glicogenina',
  'Le proteine bloccano la secrezione di insulina',
  ], 0,
  'Dopo lo sforzo gli amminoacidi coprono soprattutto il deficit energetico: il contributo al glicogeno è minimo. Secondo il prof servono carboidrati complessi.')
q("h4a-06", T, "h", "133", "Nel corso di uno sforzo intenso, perché aumenta la quota di metabolismo aerobio?", [
  "Fosfocreatina finita e glicolisi poco efficiente; cresce l'apporto di O₂",
  'La glicolisi si arresta per mancanza di ADP nel citosol e resta solo la via aerobia',
  'Il lattato attiva direttamente la catena respiratoria',
  "L'adrenalina blocca la glicolisi dopo pochi secondi",
  'Il glicogeno non può essere degradato in anaerobiosi',
  ], 0,
  'Le riserve di fosfocreatina finiscono in pochi secondi; man mano si adeguano apporto di O₂ e attività mitocondriale.')
q("h4a-07", T, "h", "133–134", "Durante uno sforzo, quale fonte di glucosio entra nel muscolo oltre al glicogeno?", [
  'Il glucosio plasmatico, che entra con i GLUT4',
  'Il glucosio prodotto dal muscolo con la gluconeogenesi',
  'Il glucosio derivato dagli acidi grassi',
  'Nessuna: il muscolo usa solo il proprio glicogeno',
  'Il glucosio ceduto dal cuore al muscolo',
  ], 0,
  "Viene dal glicogeno epatico e dalla gluconeogenesi. Non è nelle sbobine che anche la contrazione, indipendentemente dall'insulina, porta i GLUT4 in membrana.")
q("h4a-08", T, "h", "134", "Perché un maratoneta che esaurisce il glicogeno muscolare deve rallentare («muro»)?", [
  'Gli acidi grassi da soli sostengono solo intensità moderate',
  'Gli acidi grassi non possono produrre ATP nel muscolo scheletrico',
  'Il lattato si azzera e la glicolisi si ferma',
  "Manca l'insulina e il glucosio non entra",
  'Si blocca la catena respiratoria',
  ], 0,
  "L'ossidazione degli acidi grassi è più lenta e richiede più O₂ per ATP prodotto rispetto al glucosio. Non è nelle sbobine nel dettaglio, ma segue dal grafico sulle fonti energetiche.")

T = "m4-glicogenosi"
q("h4g-01", T, "h", "136–138", "Un bambino ha ipoglicemia a digiuno grave, epatomegalia, lattato alto, iperlipidemia e iperuricemia. Glicogeno epatico abbondante e di struttura normale. Diagnosi?", [
  'Glicogenosi I (von Gierke)',
  'Glicogenosi II (Pompe)',
  'Glicogenosi III (Cori)',
  'Glicogenosi V (McArdle)',
  'Glicogenosi 0',
  ], 0,
  'Deficit di glucosio 6-fosfatasi: il G6P da glicogenolisi e gluconeogenesi non diventa glucosio e viene deviato verso glicolisi e lattato.')
q("h4g-02", T, "h", "137–138", "Perché nella glicogenosi di tipo I l'ipoglicemia è più grave che nella glicogenosi di tipo III?", [
  'Nella I sono bloccate sia glicogenolisi sia gluconeogenesi',
  'Nella III manca la glicogeno sintasi e il glicogeno non si forma',
  "Nella I manca anche l'insulina",
  'Nella III il glicogeno è nei lisosomi',
  'Nella I è colpito solo il muscolo',
  ], 0,
  'La glucosio 6-fosfatasi è la via finale comune. Nella III la gluconeogenesi funziona e il glicogeno è parzialmente degradabile.')
q("h4g-03", T, "h", "137", "Perché nella glicogenosi di tipo I si somministra amido di mais crudo?", [
  'È digerito lentamente e rilascia glucosio per ore',
  'Contiene glucosio 6-fosfatasi attiva',
  "È ricco di fruttosio, che non richiede l'enzima",
  'Stimola la gluconeogenesi epatica',
  'Inibisce la glicolisi epatica',
  ], 0,
  "Il rilascio graduale copre le ore senza pasti e previene l'ipoglicemia notturna. La sbobina sottolinea la ricchezza di amilopectina.",
  note="Sbobina di Biochimica II, p. 137: c'è scritto che l'amido di mais crudo libera «grosse quantità di glucosio» con «ingresso massiccio». Il motivo per cui si usa crudo è il contrario: la digestione lenta dà un rilascio graduale per diverse ore e previene l'ipoglicemia notturna.")
q("h4g-04", T, "h", "138", "Un giovane ha crampi e mioglobinuria durante esercizi intensi, glicemia normale e nessun aumento di lattato durante lo sforzo. Diagnosi?", [
  'Glicogenosi V (McArdle)',
  'Glicogenosi I (von Gierke)',
  'Glicogenosi II (Pompe)',
  'Deficit di carnitina',
  'Deficit di LDH-H',
  ], 0,
  'Deficit di fosforilasi muscolare: senza glicogenolisi il muscolo non produce lattato; il fegato (fosforilasi normale) mantiene la glicemia.',
  note="Sbobina di Biochimica II, p. 138: la mioglobinuria è definita «presenza di mioglobina nel sangue»; è la presenza di mioglobina nelle urine.")
q("h4g-05", T, "h", "138", "Perché nella malattia di Pompe (tipo II) il glicogeno si accumula pur essendo normali gli enzimi citosolici?", [
  "Manca l'α-1,4-glucosidasi acida dei lisosomi",
  'Manca la glicogeno fosforilasi muscolare',
  "Manca l'enzima ramificante del citosol",
  'Manca la glucosio 6-fosfatasi',
  'Manca la glicogenina',
  ], 0,
  'Il glicogeno che arriva nei lisosomi (autofagia) non viene degradato e si accumula, soprattutto in cuore e muscolo. È anche una malattia da accumulo lisosomiale.')
q("h4g-06", T, "h", "138", "Nella glicogenosi di tipo III (Cori), quale struttura avrà il glicogeno?", [
  'Anomala, con ramificazioni corte residue',
  'Normale ma in quantità enorme',
  'Lineare, perché mancano le ramificazioni',
  'Con legami β-1,4 al posto degli α',
  'Assente in fegato e muscolo',
  ], 0,
  "La fosforilasi si ferma vicino ai punti di ramificazione (destrina limite). Nel deficit dell'enzima ramificante (tipo IV, non nelle sbobine) le catene sono invece lunghe e poco ramificate.")
q("h4g-07", T, "h", "137", "Che cosa distingue la glicogenosi Ia dalla Ib?", [
  "Ia: deficit dell'enzima; Ib: del trasportatore del G6P",
  "Ia: forma muscolare dell'enzima; Ib: forma epatica dell'enzima",
  'Ia: deficit della fosforilasi; Ib: della sintasi',
  'Ia: autosomica; Ib: mitocondriale',
  'Ia: lisosomiale; Ib: citosolica',
  ], 0,
  'Il risultato metabolico è lo stesso. Non è nelle sbobine che la Ib dà anche neutropenia.')
q("h4g-08", T, "h", "138", "Perché nella glicogenosi di tipo I compare iperuricemia?", [
  'Più purine dai pentosi, più degradazione dei nucleotidi, meno escrezione',
  "Manca la xantina ossidasi epatica e l'acido urico non viene trasformato in urea",
  'Aumenta il glicogeno renale, che produce acido urico',
  "L'acido urico deriva dal glicogeno accumulato",
  "Aumenta l'insulina, che riduce l'escrezione",
  ], 0,
  "Il G6P accumulato alimenta la via dei pentoso fosfati (più ribosio 5-P e sintesi di purine); il calo di Pi e ATP aumenta la degradazione dei nucleotidi; il lattato compete con l'urato per l'escrezione renale. Nella sbobina c'è solo che l'acido urico aumenta quando le cellule soffrono.")
