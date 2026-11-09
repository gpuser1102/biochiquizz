"""Revisione 3, secondo giro: correzioni dei distrattori rimasti più corti della risposta giusta.
OVERRIDE sostituisce la voce corrispondente di FIX (o la crea)."""
OVERRIDE = {
    "m2d-05": ["CO₂ e NAD⁺ ridotto", "ATP e AMP ciclico", "Piruvato e CoA-SH", "Succinil-CoA e NAD⁺"],
    "m3c-01": ["NAD⁺", "Coenzima Q", "Citocromo c", "H₂O"],
    "m3c-04": ["3 e 2", "1,5 e 2,5", "2,5 e 2,5", "4 e 2,5"],
    "m3s-09": [
        "Viene fosforilato dall'ATP prodotto e defosforilato quando la subunità β rilascia l'ATP nella matrice",
        "Lega una molecola di ATP a ogni giro dell'anello e la cede direttamente alla subunità γ del rotore",
        "Ossida il NADH della matrice e usa l'energia liberata per far ruotare l'anello c",
        "Si protona nel semicanale verso la matrice e si deprotona in quello verso lo spazio intermembrana"],
    "m3m-09": ["Le porine", "Gli istoni", "Il citocromo c", "Le DNA polimerasi"],
    "m4s-13": [
        "La glicogenina fornisce l'UTP necessario ad attivare il glucosio 1-fosfato in UDP-glucosio nel citosol",
        "La glicogenina forma i legami α-1,6 delle ramificazioni, che la sintasi da sola non è in grado di fare",
        "La glicogenina fosforila la sintasi e la porta nella forma a, più attiva nel citosol",
        "Non sa formare legami α-1,4: è la glicogenina ad allungare tutte le catene esterne"],
    "m4r-19": [
        "Lo stesso enzima, codificato da un solo gene, con la stessa localizzazione e la stessa regolazione",
        "Enzimi con reazioni diverse: fosforolisi nel muscolo, idrolisi nel fegato",
        "Le forme a e b dello stesso gene, prodotte per splicing alternativo nei due tessuti",
        "Isoenzimi: stesso gene, ma regolati entrambi allo stesso modo dall'AMP"],
    "m5f-05": [
        "Solo fegato, dove aumenta la sintesi di PEPCK e di glucosio 6-fosfatasi agendo sui geni nel nucleo",
        "Pancreas (inibisce l'insulina) e cervello (riduce il consumo di glucosio da parte dei neuroni)",
        "Rene (aumenta il riassorbimento di glucosio) e intestino (aumenta l'assorbimento)",
        "Muscolo (stimola la glicogenolisi) e fegato (inibisce la glicolisi tramite la PFK2)"],
    "m5reg-01": [
        "Per fosforilazione da parte della PKA epatica",
        "Allostericamente dall'AMP e dall'ADP",
        "Per sequestro nel nucleo, come la glucochinasi",
        "Allostericamente dall'acetil-CoA"],
    "m5reg-03": [
        "IRE (insulina), SRE (steroli), HRE (ipossia, tramite HIF-1α)",
        "SRE (steroli), CRE (cAMP/glucagone), ERE (estrogeni e progestinici)",
        "HRE (ipossia), IRE (insulina), TRE (ormoni tiroidei)",
        "ARE (androgeni), GRE (glucocorticoidi), IRE (insulina e IGF-1)"],
    "m6g-04": [
        "Solo la concentrazione di glucosio nel sangue e nel citosol",
        "Solo l'insulina, che attiva la G6PD dopo il pasto",
        "La disponibilità di ossigeno e di FAD nel citosol della cellula",
        "Il rapporto NAD⁺/NADH nella matrice mitocondriale"],
    "m6n-08": [
        "Inibisce la G6PD epatica, così gli epatociti restano senza NADPH e senza alcuna difesa antiossidante",
        "Blocca il complesso IV dei mitocondri epatici come fa il cianuro, fermando del tutto la sintesi di ATP",
        "Consuma tutto il glicogeno epatico e causa una necrosi degli epatociti da grave ipoglicemia",
        "Viene coniugato al glucuronato in eccesso e il coniugato precipita nei canalicoli biliari"],
    "b1c-03": [
        "Proteine intere e piccoli peptidi segnale",
        "Solo acqua e ioni monovalenti (Na⁺, K⁺)",
        "Ribosomi e mRNA già tradotti",
        "Proteine, acidi nucleici e lipidi"],
    "b1c-07": ["CREB", "STAT3", "NF-κB", "AP-1"],
    "bh1c-01": [
        "Concentrazione bassa e affinità del recettore altissima, così il ligando resta legato a lungo dopo ogni singolo impulso",
        "Trasporto nel sangue legato a proteine plasmatiche, così il ligando arriva lentamente e in modo costante ai recettori",
        "Recettore nucleare con effetto genico, così ogni impulso modifica in modo duraturo la trascrizione",
        "Affinità del recettore altissima e degradazione lenta, così il complesso resiste alla diluizione del ligando"],
    "b1i-03": [
        "L'ormone stesso, che entra nella cellula e agisce direttamente sugli enzimi bersaglio del citosol",
        "Il recettore attivato, che si stacca dalla membrana e migra nel nucleo per agire sulla trascrizione",
        "La proteina di trasporto che porta l'ormone nel sangue fino alla cellula bersaglio",
        "Un secondo ormone rilasciato dalla cellula bersaglio che agisce sulle cellule vicine"],
    "bh1i-01": [
        "È idrofobico ma troppo grande per attraversare la membrana: entra per endocitosi e viene degradato nei lisosomi",
        "Viene sempre degradato nel sangue dalle proteasi plasmatiche, molto prima di poter raggiungere il nucleo",
        "I peptidi non possono legare proteine nucleari, quindi agiscono solo su enzimi del citosol",
        "Agisce solo su cellule vicine (paracrino), che non possiedono recettori nucleari per i peptidi"],
    "b2c-01": [
        "Nucleari, citosolici, di membrana plasmatica e mitocondriali, classificati in base alla sede",
        "Recettori canale, accoppiati a proteine G, nucleari, per gli ormoni steroidei e tiroidei",
        "Tirosin-chinasici, serin-chinasici, fosfatasi e proteasi di membrana",
        "Recettori canale, con attività catalitica, per le integrine e per le caderine"],
    "b2c-04": [
        "Endocitosi del recettore nicotinico e sua successiva degradazione nei lisosomi della fibra muscolare",
        "Attività GTPasica intrinseca del recettore, che idrolizza il GTP e chiude il canale",
        "Fosforilazione del recettore da parte della PKA, che lo stacca dalla proteina G",
        "Ricaptazione dell'acetilcolina intera nel terminale e sua idrolisi da parte delle MAO mitocondriali"],
    "bh2c-02": [
        "Recettore canale: apre direttamente un poro per il Cl⁻ che iperpolarizza la membrana del neurone",
        "Recettore catalitico: attiva una tirosin-chinasi che fosforila e chiude i canali Na⁺ voltaggio-dipendenti",
        "Eterodimero GPCR: la subunità αs attiva l'adenilato ciclasi e apre i canali Ca²⁺",
        "Recettore nucleare: lega il DNA e reprime la trascrizione dei geni eccitatori"],
    "b2k-03": ["Insulina", "Glucagone", "Aldosterone", "Tireotropina (TSH)"],
    "b3g-05": [
        "Ogni GPCR ha una sola proteina G dedicata, codificata dallo stesso gene del recettore",
        "La proteina G si autoassembla a caso, quindi ogni cellula ne produce combinazioni sempre diverse e imprevedibili",
        "Le combinazioni nascono dallo splicing alternativo del recettore, non da geni diversi",
        "Pochi geni per α, β e γ, ma moltissime modificazioni post-traduzionali che le rendono tutte diverse"],
    "b3c-03": [
        "Viene fosforilata dal recettore attivato, che la stacca dalla membrana e la porta libera nel citosol",
        "Lega il GTP sulla subunità catalitica, che si separa dalle subunità regolatrici come una proteina G",
        "Il cAMP si lega alle subunità catalitiche (2 per subunità), che rilasciano le regolatrici",
        "Entra nel nucleo, dove il cAMP la separa dal DNA e libera le subunità catalitiche"],
    "b3c-05": [
        "Apre i canali del Ca²⁺ della membrana plasmatica e attiva la calmodulina nel citosol",
        "Degrada il cAMP residuo nel citosol, spegnendo così la PKA che lo ha fosforilato",
        "Inattiva il recettore β-adrenergico fosforilandone la coda C-terminale",
        "Lega le sequenze CRE nel citosol e blocca la traduzione degli mRNA bersaglio"],
    "b3c-06": [
        "Inibisce l'adenilato ciclasi degli enterociti, che non producono più cAMP: si perdono acqua e sali",
        "ADP-ribosila la Gαi, che resta sempre attiva: il cAMP scende e l'intestino non riassorbe più acqua e sali",
        "Degrada il cAMP attivando la fosfodiesterasi intestinale, che apre i canali del Cl⁻ e fa perdere acqua e sali",
        "Fosforila un'arginina della Gαs, che non lega più il GTP: il cAMP crolla e l'acqua resta nel lume"],
    "b3c-10": [
        "Che il cAMP è assente e le subunità sono legate tra loro",
        "Che la PKA è stata degradata nel proteasoma",
        "Che la proteina G è inattiva e lega il GDP",
        "Che il cAMP è salito e le subunità si sono riunite insieme"],
    "bh3c-01": [
        "Attivano direttamente la PKA, che fosforila e desensibilizza il recettore β-adrenergico del cardiomiocita",
        "Aumentano il cAMP attivando l'adenilato ciclasi, che compensa il calo dovuto alla Gαi attivata",
        "Bloccano il recettore muscarinico, impedendo all'acetilcolina di agire troppo a lungo",
        "Fosforilano il recettore β-adrenergico tramite la βARK e lo staccano dall'adrenalina"],
    "bh3c-02": [
        "Gαi ADP-ribosilata → adenilato ciclasi inibita → cAMP basso → riassorbimento bloccato nell'enterocita → perdita di acqua e sali",
        "Gαs ADP-ribosilata → fosfodiesterasi attivata → cAMP basso → canali chiusi nell'enterocita → acqua trattenuta nel lume",
        "Recettore muscarinico bloccato → Gq inattiva → IP₃ basso → Ca²⁺ basso → secrezione di acqua e sali",
        "Gαs fosforilata → PKA inibita → chiusura dei canali Cl⁻ → riassorbimento ridotto → diarrea acquosa"],
    "bh3c-03": [
        "Amplifica il segnale: la fosfodiesterasi produce altro cAMP a partire dall'AMP già presente nel citosol",
        "Serve a produrre cGMP dal cAMP, così la cellula attiva anche la PKG insieme alla PKA",
        "Attiva la proteina G: il prodotto della fosfodiesterasi riporta la subunità Gα nella forma legata al GTP",
        "Non ha significato fisiologico: è un bersaglio casuale della PKA, osservato solo in vitro"],
    "b3s-02": ["AKAP-79", "GRB2", "SOS (GEF)", "Calmodulina"],
    "b3m-05": [
        "↑cAMP → PKA → fosforila la chinasi delle catene leggere della miosina → contrazione del vaso sanguigno",
        "↑cGMP → PKG → apre i canali del Ca²⁺ voltaggio-dipendenti → contrazione e poi rilassamento",
        "↑IP₃ → rilascio di Ca²⁺ dal reticolo → attivazione della NO sintasi endoteliale → rilassamento del vaso",
        "↑DAG → PKC → inibisce la fosfatasi delle catene leggere della miosina → rilassamento del vaso"],
    "b4c-03": [
        "Solo la contrazione muscolare scheletrica e cardiaca, perché il Ca²⁺ agisce esclusivamente sulla troponina C",
        "Solo la trascrizione genica, perché il Ca²⁺ entra nel nucleo e si lega direttamente alle sequenze promotrici dei geni",
        "Solo la sintesi di ATP nel mitocondrio, perché il Ca²⁺ attiva le deidrogenasi del ciclo di Krebs e nient'altro",
        "Solo la secrezione di ormoni e di neurotrasmettitori, perché il Ca²⁺ agisce soltanto sull'esocitosi delle vescicole"],
    "b4c-05": [
        "La rianodina endogena prodotta dal muscolo stesso",
        "L'IP₃ prodotto dalla fosfolipasi C della membrana",
        "Il cAMP, tramite la PKA legata al canale",
        "Il Mg²⁺ citosolico (rilascio indotto da Mg²⁺)"],
    "bh4c-01": [
        "L'IP₃ apre anche la Ca²⁺-ATPasi della membrana, che pompa altro Ca²⁺ dentro la cellula dall'esterno",
        "Il Ca²⁺ blocca l'antiporto Na⁺/Ca²⁺ in modo permanente, così tutto quello rilasciato resta nel citosol a lungo",
        "La calmodulina rilascia tutto il Ca²⁺ che aveva legato a riposo, raddoppiando subito la concentrazione libera",
        "Il mitocondrio smette di accumulare Ca²⁺ e rilascia anche quello della matrice, amplificando il segnale"],
    "bh4m-01": [
        "Attiva la glicogeno sintasi e inibisce la fosforilasi chinasi: il muscolo riforma le sue riserve durante lo sforzo",
        "Non ha effetti diretti sul glicogeno: il Ca²⁺ agisce solo sulla troponina C e sulla contrazione dei filamenti di actina",
        "Attiva la PP1, che defosforila sia la sintasi sia la fosforilasi: degradazione e sintesi procedono insieme",
        "Blocca la glicolisi per risparmiare ATP e attiva la sintasi: il glucosio 6-P viene accumulato come glicogeno"],
    "b4p-04": [
        "cAMP e Ca²⁺ (più fosfatidilcolina di membrana)",
        "IP₃ e Ca²⁺ (più fosfatidiletanolammina)",
        "cGMP e calmodulina (più colesterolo di membrana)",
        "PIP₃ e Mg²⁺ (più sfingomielina)"],
    "b4p-07": [
        "Tra il carbonio 1 del glicerolo e l'acido grasso",
        "Tra il fosfato e la testa polare (inositolo)",
        "Tra il carbonio 2 del glicerolo e l'acido grasso",
        "Tra il carbonio 3 dell'inositolo e il suo fosfato"],
    "b4p-08": ["fos, jun e Myc", "Smad2, Smad4", "STAT3 e STAT5", "CREB, CBP, p300"],
    "b4a-02": ["ACTH e TSH", "Insulina e glucagone", "LH e FSH", "GH e prolattina"][:1] + ["Insulina e glucagone", "Ormone luteinizzante e FSH", "GH e prolattina"],
    "b4a-03": [
        "Tre ormoni tiroidei diversi (T3, T4 e rT3) che inibiscono rispettivamente l'ipotalamo, l'ipofisi e la tiroide stessa",
        "Tre tempi di risposta degli steroidi: secondi (effetti di membrana), minuti (citosol) e ore (effetti sul nucleo)",
        "L'ormone periferico inibisce l'ipotalamo; l'ormone ipofisario inibisce la ghiandola periferica; l'ipotalamo inibisce l'ipofisi",
        "L'ormone ipofisario inibisce l'ipofisi; l'ormone ipotalamico inibisce la ghiandola periferica; l'ormone periferico la stimola"],
    "b5i-04": [
        "Adrenalina, noradrenalina, simpatico, somatostatina, glucagone, digiuno prolungato e ipoglicemia",
        "Solo il glucosio, che entra con i GLUT2 e chiude i canali K⁺ ATP-dipendenti della cellula β",
        "Glucagone, cortisolo, ormone della crescita e ipoglicemia, come risposta allo stress",
        "Glucosio, amminoacidi, adrenalina, simpatico, somatostatina e apertura dei canali K⁺ ATP-dipendenti"],
    "b5i-05": [
        "SOS (fattore di scambio del nucleotide di Ras)",
        "PKA (protein chinasi cAMP-dipendente)",
        "STAT5 (trasduttore del segnale e attivatore)",
        "GRB2 (proteina adattatrice con SH2)"],
    "b5i-06": [
        "Sono identici: entrambi compaiono in pochi minuti alle stesse concentrazioni di insulina, ma i tardivi durano di più nel tempo",
        "Immediati (ore, 10⁻⁸ M): espressione genica (meno gluconeogenesi). Tardivi (minuti, 10⁻⁹–10⁻¹⁰ M): GLUT4 ed enzimi del glicogeno",
        "Immediati (minuti, 10⁻⁸ M): richiedono più insulina. Tardivi (giorni): passano per il cAMP e la PKA nel nucleo",
        "Immediati (secondi, 10⁻⁶ M): apertura dei canali K⁺. Tardivi (minuti, 10⁻⁹ M): GLUT4 ed enzimi del glicogeno muscolare"],
    "b5i-10": ["IRS1", "AKAP", "Calmodulina", "GL"],
    "bh5i-01": [
        "La PKA fosforila entrambi gli enzimi: la sintasi fosforilata è attiva e la fosforilasi fosforilata è inattiva",
        "Il Ca²⁺ attiva la fosforilasi chinasi (portata da GM), che fosforila la sintasi (attivandola) e la fosforilasi (inattivandola)",
        "La GSK3 attivata dalla PKB fosforila la sintasi (attivandola), mentre la PP1 defosforila la fosforilasi",
        "Il cAMP sale e attiva la PP1 (portata da GM), che fosforila sia la sintasi (attivandola) sia la fosforilasi (inattivandola)"],
    "bh5i-02": [
        "Deficit di secrezione delle cellule β, per esempio per distruzione autoimmune delle isole di Langerhans",
        "Eccesso di somatostatina, che blocca il recettore dell'insulina sui tessuti periferici",
        "Insulina esogena in eccesso, somministrata per errore in una dose troppo alta",
        "Mutazione del peptide C, che non viene tagliato e resta legato all'insulina circolante nel plasma"],
    "d2n-02": ["Lisina", "Treonina", "Glicina", "Asparagina"],
    "d3p-04": [
        "Fuori dalla cellula c'è più cisteina libera",
        "Servono enzimi presenti solo fuori dalla cellula",
        "Nel citosol manca l'ossigeno che serve al ponte",
        "L'ambiente extracellulare è più riducente"],
    "d3h-01": [
        "Cambia il codice genetico della cellula: tutte le proteine successive vengono tradotte con un amminoacido sbagliato",
        "Accorcia sempre la proteina, perché la sostituzione introduce un codone di stop e la catena resta tronca a metà",
        "Impedisce la trascrizione del gene, perché l'mRNA mutato viene degradato prima di arrivare al ribosoma",
        "Rende la proteina insolubile in ogni caso, perché qualunque sostituzione espone residui idrofobici all'acqua circostante"],
    "d3c-09": ["Idrossiprolina", "Prolina", "Serina", "Asparagina"],
    "d3f-01": ["Mioglobina", "Lisozima C", "Insulina", "Citocromo c"],
    "d3f-06": [
        "Si formano molti ponti disolfuro, ciascuno dei quali libera molta energia e compensa l'ordine della catena",
        "I residui polari liberano energia legandosi tra loro all'interno della proteina ripiegata",
        "Il folding consuma ATP, che fornisce l'energia libera necessaria a ordinare la catena",
        "Il collasso idrofobico ordina l'acqua attorno alle catene apolari, diminuendone l'entalpia e l'entropia"],
    "d3h-07": [
        "Aggiungere altra urea e più β-mercaptoetanolo, che rompe definitivamente tutti i ponti disolfuro e libera la catena",
        "Aggiungere chaperoni GroEL e GroES con ATP, che ripiegano la proteina anche se i ponti disolfuro restano quelli sbagliati",
        "Riscaldare a 90 °C senza riducente, così i ponti disolfuro sbagliati si sciolgono e quelli giusti si riformano da soli",
        "Togliere l'urea e aggiungere iodoacetato, che blocca le cisteine libere e stabilizza i ponti disolfuro già formati"],
    "d3h-08": [
        "Le proteine aggregate sono troppo piccole per essere riconosciute: gli oligomeri sfuggono sia ai chaperoni sia al proteasoma",
        "Il proteasoma degrada solo le fibrille mature: gli oligomeri iniziali restano nella cellula e continuano a crescere senza controllo",
        "Le fibrille sono fatte di α-eliche molto stabili, che nessun sistema cellulare riesce a srotolare e degradare",
        "Le proteine coinvolte non hanno una sequenza nota: non è possibile capire quale conformazione prendano"],
    "d3q-04": [
        "La capacità di legare più substrati diversi contemporaneamente sullo stesso sito attivo della proteina",
        "La formazione di ponti disolfuro tra subunità diverse, che le rendono un'unica catena",
        "La polimerizzazione delle subunità in fibre lunghe, come accade per la tubulina",
        "Il legame del substrato a una subunità, che blocca sempre le altre subunità dell'intero complesso"],
    "dh3q-01": ["Ciclica C4, tipica dei tetrameri", "Speculare (per riflessione)", "Elicoidale, come i polimeri", "Diedrica D4, come GroEL"],
    "d3x-04": [
        "I ribosomi e i polisomi, che vanno sul fondo della provetta",
        "Le proteine solubili del citosol, che precipitano sul fondo",
        "I microsomi (frammenti di RE), che formano il pellet compatto",
        "I mitocondri e i lisosomi, mentre i nuclei restano sospesi in alto"],
    "dh3x-01": [
        "Cristallizzare subito l'omogenato, poi identificare l'enzima nella struttura ottenuta con la diffrazione ai raggi X",
        "Ultracentrifugare l'omogenato a 600.000 g e usare il sopranatante, dove restano gli enzimi della matrice mitocondriale",
        "Precipitare tutte le proteine con urea 8 M, poi separarle per carica e dimensione con le cromatografie",
        "Ridurre i ponti disolfuro con β-mercaptoetanolo, poi purificare per affinità dall'omogenato totale"],
    "h1e-02": [
        "Lavorano entrambi a circa metà della propria Vmax",
        "Il secondo è più veloce, perché ha la KM più alta",
        "Entrambi lavorano vicino alla propria Vmax massima",
        "Il primo è a ½ Vmax, il secondo a circa il 50% della Vmax"],
    "h2f-02": [
        "Il G6P la attiva allostericamente come effettore positivo",
        "L'insulina la defosforila tramite la proteina fosfatasi 1 (PP1)",
        "Il fruttosio 6-fosfato la porta dal nucleo al citosol",
        "L'ATP ne riduce la KM come effettore omotropico positivo"],
    "h5a-05": [
        "La gluconeogenesi si blocca definitivamente dopo il viaggio",
        "La glicemia aumenta di notte per un eccesso di insulina circolante",
        "Il glicogeno epatico non viene più usato durante la notte",
        "Non cambia nulla, perché la melatonina regola subito anche la PEPCK"],
    "x5a-01": [
        "I corpi chetonici si trasformano in glucosio nel fegato e nel rene tramite la PEPCK citosolica",
        "Inibiscono direttamente la proteolisi muscolare legando il proteasoma",
        "Attivano la sintesi proteica nel muscolo durante il digiuno prolungato",
        "Il muscolo li usa al posto delle proteine come fonte di azoto per sintetizzare l'urea"],
    "x5a-03": [
        "Più lattato, più tessuto adiposo, meno mitocondri e un'insulino-resistenza marcata",
        "Meno mitocondri, ma muscoli più grandi, più glicogeno e più forza massima",
        "Diabete di tipo 2 con iperglicemia a digiuno e ridotta sensibilità periferica all'insulina",
        "Meno acidi grassi usati e accumulo di trigliceridi nelle fibre muscolari"],
    "x6g-03": ["La lattato deidrogenasi", "La GAP deidrogenasi", "La piruvato chinasi", "La malato deidrogenasi"],
}
