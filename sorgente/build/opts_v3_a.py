"""Revisione 3 delle opzioni (novembre 2026): la risposta giusta non deve essere riconoscibile perché è la più lunga
o la più articolata. FIX: id -> i 4 distrattori riscritti con lunghezza e struttura simili alla risposta giusta
(che resta invariata e diventa la prima opzione; l'app le mescola)."""
FIX = {
    "m1c-04": [
        "L'intermedio è sempre più ossidato del terminale e per questo non può più essere ridotto",
        "Il terminale entra nel ciclo di Krebs, mentre l'intermedio non vi può accedere",
        "L'intermedio viene eliminato con le urine, mentre il terminale resta nella cellula",
        "Il terminale si accumula nel tessuto adiposo come riserva energetica a lungo termine"],
    "m1t-03": [
        "pH 7,4, 37 °C, concentrazioni cellulari",
        "pH 0, 25 °C, reagenti e prodotti 1 M",
        "pH 7, 37 °C, reagenti e prodotti 1 mM",
        "pH 7,4, 25 °C, reagenti e prodotti 0,1 M"],
    "m1a-01": [
        "−61 kJ/mol (−14,6 kcal/mol)",
        "+30,5 kJ/mol (+7,3 kcal/mol)",
        "−7,3 kJ/mol (−1,7 kcal/mol)",
        "−45,6 kJ/mol (−10,9 kcal/mol)"],
    "m1a-03": ["Glucosio 6-fosfato", "Glicerolo 3-fosfato", "Fruttosio 6-fosfato", "Glucosio 1-fosfato"],
    "m1a-08": [
        "Iperfosfatemia, perché l'eccesso di ATP prodotto libera fosfato inorganico nel sangue",
        "Ipoglicemia grave, perché l'insulina blocca subito la glicogenolisi nel fegato",
        "Acidosi lattica immediata, perché il muscolo fermenta tutto il glucosio che riceve",
        "Ipercalcemia, perché il fosfato in eccesso mobilizza il calcio dalle ossa verso il sangue"],
    "m1a-10": [
        "È regolata dall'insulina, che la attiva dopo il pasto tramite fosforilazione",
        "È inibita dall'ATP alto, quindi lavora solo quando la carica energetica scarseggia",
        "È un enzima allosterico attivato dal GDP che si accumula durante la traduzione",
        "La sua sintesi viene indotta solo quando i ribosomi in attività richiedono GTP"],
    "m1o-10": ["FAD", "FMNH₂", "NADH", "FADH⁺"],
    "m1e-05": [
        "Effettori allosterici che entrano nella cellula",
        "Variazioni del pH intracellulare nel citosol",
        "Variazioni locali della temperatura del tessuto",
        "Variazioni della forza ionica del citoplasma"],
    "m1e-06": [
        "Da effettore allosterico negativo",
        "Da inibitore competitivo reversibile",
        "Da inibitore incompetitivo puro",
        "Da inibitore non competitivo misto"],
    "m1e-07": [
        "I loro enzimi sono troppo lenti per rispondere ai segnali ormonali e non hanno siti allosterici disponibili",
        "Non usano coenzimi né cofattori, quindi non possono essere modulate da effettori allosterici",
        "Avvengono solo nella matrice mitocondriale, dove i segnali ormonali e gli effettori non arrivano",
        "Hanno tutte ΔG°' fortemente positivo e quindi non procedono senza l'accoppiamento con l'ATP"],
    "m1e-09": [
        "Allosterico (con cooperatività positiva tra le subunità)",
        "Saturato (con tutti i siti attivi occupati dal substrato)",
        "Cooperativo (con cinetica sigmoide e coefficiente di Hill > 1)",
        "Ad attività minima (limitato dal rilascio del prodotto)"],
    "m2i-03": ["7", "14", "24", "10"],
    "m2i-08": [
        "Insulino-resistenza con produzione normale di insulina",
        "Eccesso di glucagone prodotto dalle cellule α del pancreas",
        "Difetto dei GLUT2 epatici con secrezione insulinica normale",
        "Eccesso di cortisolo da iperplasia della corticale del surrene"],
    "m2i-10": [
        "Il numero di molecole di glucosio trasportate al secondo da un trasportatore",
        "La costante di equilibrio tra glucosio extracellulare e intracellulare",
        "La concentrazione intracellulare di glucosio a cui il trasporto si ferma del tutto",
        "Il numero di trasportatori presenti per micrometro quadrato di membrana"],
    "m2f-01": [
        "Esochinasi I (ubiquitaria)",
        "Fosfoglucomutasi (epatica)",
        "Glucosio 6-fosfatasi (microsomiale)",
        "Esochinasi II (muscolare)"],
    "m2f-02": [
        "Si lega alle proteine del citosol e non riesce più a diffondere",
        "Viene subito polimerizzato in glicogeno in tutte le cellule del corpo",
        "È più grande del glucosio e non riesce a passare attraverso i GLUT",
        "Viene ossidato subito a CO₂ nel mitocondrio prima di poter uscire"],
    "m2f-04": [
        "È inibita dal suo prodotto, il glucosio 6-fosfato, come l'esochinasi muscolare",
        "È fosforilata dalla PKA e inattivata nel citosol quando arriva il glucagone",
        "Non è regolata da altri fattori: dipende solo dalla concentrazione di glucosio",
        "È attivata allostericamente dall'AMP quando la carica energetica scarseggia"],
    "m2f-05": [
        "Per aumentare la KM per il glucosio quando la glicemia sale molto",
        "Per legare il Mg²⁺, che può entrare solo quando il sito attivo è chiuso",
        "Per far uscire più in fretta il glucosio 6-fosfato appena formato",
        "Per legare un secondo glucosio nel sito allosterico della subunità"],
    "m2f-09": ["10 mM", "1,0 mM", "0,5 mM", "0,01 mM"],
    "m2g-05": [
        "È accoppiata all'idrolisi di ATP, che rende negativo il ΔG complessivo",
        "È irreversibile, quindi procede verso destra in qualsiasi condizione",
        "È attivata dall'AMP, che sposta l'equilibrio verso la formazione dei triosi",
        "Il FBP è un composto ad alta energia che si scinde spontaneamente"],
    "m2g-07": [
        "Consuma due molecole di ATP e accoppia la loro idrolisi alla formazione del piruvato",
        "Libera CO₂, che esce subito dalla cellula e sposta l'equilibrio verso il piruvato",
        "Il piruvato viene subito ridotto a lattato dalla LDH, che lo sottrae all'equilibrio",
        "Il PEP è stabilizzato dalla risonanza del fosfato, che rende la sua idrolisi molto lenta"],
    "m2g-08": [
        "Alcalinizzante, perché consuma 2 H⁺",
        "Neutro, perché non libera né consuma H⁺",
        "Acidificante, perché produce 2 CO₂",
        "Alcalinizzante, perché produce 2 OH⁻"],
    "m2g-10": [
        "Al fruttosio 1,6-bisfosfato",
        "Al fosfoenolpiruvato (PEP)",
        "All'1,3-bisfosfoglicerato",
        "Non si ferma: arriva a lattato"],
    "m2g-12": [
        "Sposta direttamente il fosfato dal C3 al C2, senza intermedi e senza residui fosforilati",
        "Usa ATP per fosforilare il C2, poi una fosfatasi separata rimuove il fosfato in C3",
        "Idrolizza il fosfato in C3 e lo riattacca al C2 sfruttando l'energia del NADH",
        "Una serina fosforilata cede il fosfato al C1, formando 1,3-bisfosfoglicerato come prodotto"],
    "m2g-13": [
        "Fosfoglucomutasi (glucosio 6-fosfato mutasi)",
        "Fosfomannosio isomerasi (mannosio isomerasi)",
        "Glucosio 6-fosfato deidrogenasi (G6PDH)",
        "Fosfofruttochinasi 1 (fosfoesoso chinasi)"],
    "m2g-16": [
        "Fosfoanidridico tra il C1 e il fosfato β dell'ATP",
        "Fosfoestere sul C6 del fruttosio 1-P",
        "Glicosidico tra il C1 e il C2 del fruttosio",
        "Fosfoanidridico sul C1 del fruttosio 6-P"],
    "m2r-04": [
        "Riduzione del piruvato a lattato, poi decarbossilazione del lattato a etanolo",
        "Ossidazione del piruvato ad acetil-CoA, poi riduzione dell'acetil-CoA a etanolo",
        "Carbossilazione del piruvato a ossalacetato, poi sua riduzione a etanolo con NADH",
        "Riduzione del piruvato ad acetaldeide con NADH, poi decarbossilazione a etanolo"],
    "m2r-05": [
        "Il lattato è un acido debole che a pH 7 resta quasi tutto in forma protonata",
        "La reazione libera ioni OH⁻ che neutralizzano i protoni prodotti dalla glicolisi",
        "Il lattato viene subito ossidato a CO₂ nel mitocondrio della stessa cellula muscolare",
        "L'anidrasi carbonica tampona tutti i protoni prodotti dalla reazione della LDH"],
    "m2r-06": [
        "L'etanolo inibisce la secrezione di insulina e stimola quella di glucagone dal pancreas",
        "L'acetaldeide blocca la glicolisi epatica inattivando la fosfofruttochinasi 1",
        "L'etanolo consuma tutto il NADH del fegato, bloccando la catena respiratoria mitocondriale",
        "L'etanolo viene trasformato direttamente in lattato dalla LDH, che consuma il glucosio"],
    "m2r-09": ["M4 (muscolare)", "H2M2 (polmonare)", "H3M (ibrido)", "M3H (ibrido)"],
    "m2n-02": [
        "Al NAD⁺ della matrice tramite la malato deidrogenasi",
        "Direttamente all'O₂ del complesso IV, saltando la catena",
        "Al citocromo c nello spazio intermembrana mitocondriale",
        "All'FMN del complesso I sul lato della matrice"],
    "m2reg-01": ["Fosfoglicerato chinasi", "Trioso fosfato isomerasi", "Fosfoglicerato mutasi", "Fosfoglucosio isomerasi"],
    "m2reg-02": [
        "ATP e citrato ad alta concentrazione",
        "Acetil-CoA e NADH mitocondriale",
        "Glucosio 6-fosfato e insulina",
        "Fosfoenolpiruvato e alanina"],
    "m2reg-03": [
        "È il più abbondante dei tre nucleotidi adenilici nel citosol, quindi le sue variazioni assolute sono le più grandi",
        "Inibisce direttamente l'ATP sintasi, quindi segnala subito quando la sintesi di ATP rallenta",
        "Viene prodotto dall'adenilato ciclasi in risposta a glucagone e adrenalina durante il digiuno",
        "Si forma solo quando l'ATP cellulare è esaurito del tutto, quindi indica uno stato di emergenza"],
    "m2reg-05": [
        "La attiva, perché il fegato a digiuno ha bisogno di produrre più ATP dal glucosio",
        "Non cambia la sua attività catalitica, ma ne accelera la degradazione nel proteasoma",
        "La sposta nel mitocondrio, dove lavora insieme alla piruvato carbossilasi",
        "La rende sensibile all'insulina, che poi la attiva allostericamente dopo il pasto"],
    "m2reg-06": [
        "In R c'è una cisteina che lega il F6P; in T una serina che lega l'ATP al suo posto",
        "In T il sito attivo è occupato dall'ATP, mentre in R dall'AMP che sposta l'ATP dal sito",
        "Non cambia nulla nel sito attivo: tra le due forme cambia soltanto la Vmax dell'enzima",
        "In R c'è Glu161 che lega il Mg²⁺ dell'ATP; in T arriva Arg162 che lega il citrato"],
    "m2reg-10": [
        "Nucleotide difosfato chinasi",
        "AMP deaminasi (adenilato deaminasi)",
        "Adenilato ciclasi (di membrana)",
        "Creatina chinasi (fosfocreatina chinasi)"],
}
FIX.update({
    "m2p-01": [
        "L'aumento della glicolisi quando la cellula passa da anaerobiosi ad aerobiosi",
        "La fermentazione alcolica dei lieviti quando l'ossigeno viene a mancare del tutto",
        "L'inibizione della respirazione mitocondriale da parte di un eccesso di glucosio",
        "La glicolisi aerobia delle cellule tumorali anche in presenza di molto ossigeno"],
    "m2p-02": ["Esochinasi I", "Piruvato chinasi", "Piruvato deidrogenasi", "Fosfoglicerato chinasi"],
    "m2p-03": ["1,3-bisfosfoglicerato", "Fosfoenolpiruvato", "Fruttosio 1,6-bisfosfato", "3-fosfoglicerato"],
    "m2p-06": [
        "Manca la fruttochinasi: il fruttosio non viene fosforilato e passa nelle urine",
        "Manca il GLUT5 intestinale: il fruttosio fermenta nel colon e dà diarrea e dolore",
        "Il fruttosio 1-P inibisce la glucochinasi e blocca del tutto l'ingresso del glucosio",
        "Manca la fruttosio 1,6-bisfosfatasi: si blocca la sintesi di glicogeno nel fegato"],
    "m2p-09": [
        "Galattochinasi (galattosio chinasi)",
        "UDP-galattosio 4-epimerasi (forma epatica)",
        "Lattasi intestinale (β-galattosidasi)",
        "Aldolasi B (fruttosio 1-P aldolasi)"],
    "m2d-02": [
        "Tre: NAD⁺, FAD e coenzima A",
        "Quattro: TPP, biotina, NAD⁺, FAD",
        "Cinque: TPP, biotina, CoA, FMN, NADP⁺",
        "Quattro: TPP, lipoato, NADP⁺, FMN"],
    "m2d-05": ["CO₂ e NADH", "ATP e AMP", "Piruvato e CoA", "Citrato e ADP", ][:3] + ["Succinil-CoA e NAD⁺"],
    "m2d-06": [
        "Usa meno coenzimi, perché più enzimi condividono lo stesso NAD⁺ legato al complesso",
        "Non ha bisogno di regolazione, perché lavora sempre alla sua velocità massima possibile",
        "Funziona anche senza NAD⁺, perché gli elettroni restano legati al lipoato del complesso",
        "Consuma meno ATP per ogni molecola di substrato trasformata rispetto a enzimi separati"],
    "m3k-04": ["Malato deidrogenasi", "Fumarasi (fumarato idratasi)", "Isocitrato deidrogenasi", "Aconitasi (aconitato idratasi)"],
    "m3k-06": [
        "Aconitasi, fumarasi e malato deidrogenasi, tutte mitocondriali",
        "Succinil-CoA sintetasi, succinato deidrogenasi, fumarasi",
        "Citrato sintasi, aconitasi, succinato deidrogenasi, malato deidrogenasi",
        "Isocitrato deidrogenasi, succinil-CoA sintetasi, malato deidrogenasi"],
    "m3k-08": [
        "Citrato → isocitrato (aconitasi mitocondriale)",
        "Malato → ossalacetato (malato deidrogenasi)",
        "Acetil-CoA → citrato (citrato sintasi)",
        "Glutammato → α-chetoglutarato (transaminasi)"],
    "m3k-13": [
        "FAD (riboflavina, B2): l'alimentazione era povera di latte e derivati, unica fonte della vitamina nella dieta",
        "TPP (tiamina, B1): si mangiava soprattutto riso brillato, privato della cuticola ricca di tiamina",
        "CoA (acido pantotenico, B5): la carne era rara e i cereali coltivati non contengono pantotenato",
        "NADP (niacina, B3): il mais conteneva troppo triptofano, che ne blocca l'assorbimento intestinale"],
    "m3k-17": [
        "Diidrolipoil transacetilasi",
        "Succinil-CoA sintetasi (tiochinasi)",
        "Diidrolipoil deidrogenasi",
        "Diidrolipoil transferasi"],
    "m3c-01": ["NAD⁺", "Coenzima Q", "Citocromo c", "H₂O"],
    "m3c-04": ["3 e 2", "1,5 e 2,5", "2 e 1", "4 e 2"],
    "m3c-08": [
        "A produrre ATP direttamente nel complesso III, senza passare dall'ATP sintasi",
        "A ridurre l'ossigeno ad acqua usando direttamente gli elettroni del coenzima Q",
        "A trasportare il NADH citosolico dentro la matrice mitocondriale attraverso la membrana",
        "A trasferire due elettroni insieme dal citocromo c al complesso IV in un solo passaggio"],
    "m3c-12": [
        "FAD (flavin adenin dinucleotide)",
        "Biotina (vitamina B7)",
        "Lipoato (acido lipoico)",
        "TPP (tiamina pirofosfato)"],
    "m3c-14": [
        "Eme b, eme c1 e un centro Fe-S",
        "Solo eme a3 e un centro CuA",
        "Centri Fe-S, FMN ed eme b",
        "Eme b, CuA e un centro Fe-S"],
    "m3c-15": [
        "Un'istidina distale",
        "Una molecola di ossigeno",
        "Lo zolfo di una cisteina",
        "Un'altra molecola di acqua"],
    "m3c-16": [
        "Nella membrana plasmatica",
        "Nella matrice mitocondriale, libero",
        "Nello spazio intermembrana",
        "Nella membrana mitocondriale esterna"],
    "m3s-09": [
        "Viene fosforilato dall'ATP prodotto e defosforilato quando la subunità β lo rilascia",
        "Lega una molecola di ATP a ogni giro dell'anello e la cede direttamente alla subunità γ",
        "Ossida il NADH della matrice e usa l'energia liberata per far ruotare l'anello c",
        "Si protona nel semicanale verso la matrice e si deprotona verso lo spazio intermembrana"],
    "m3r-01": ["Catalasi perossisomiale", "Glutatione perossidasi", "NADPH ossidasi", "Mieloperossidasi"],
    "m3r-06": [
        "GSH (glutatione ridotto)",
        "GS-SeH (selenoglutatione)",
        "Glutatione perossido (GS-OOH)",
        "GSOH (glutatione sulfenico)"],
    "m4d-01": [
        "Cervello e rene",
        "Tessuto adiposo bruno e rene",
        "Eritrociti e muscolo cardiaco",
        "Intestino tenue e pancreas"],
    "m4d-04": [
        "Libera più molecole di glucosio per ogni legame rotto rispetto all'idrolisi",
        "È più veloce perché non ha bisogno del piridossal fosfato come cofattore",
        "Non richiede enzimi, perché il fosfato attacca il legame glicosidico spontaneamente",
        "Il glucosio esce libero e può passare subito nel sangue attraverso i GLUT"],
    "m4d-08": [
        "Nel citosol, libera; soltanto nel fegato",
        "Nel citosol, legata al glicogeno; fegato e muscolo",
        "Nel lume dei lisosomi; in tutti i tessuti",
        "Sulla membrana plasmatica; fegato e cervello"],
    "m4d-09": ["Tiamina pirofosfato", "Biotina (vitamina H)", "Flavin mononucleotide", "Acido lipoico"],
    "m4s-03": [
        "La reazione consuma GTP, che ha un ΔG di idrolisi più negativo dell'ATP",
        "Avviene nel reticolo endoplasmatico, da cui l'UDP-glucosio non può uscire",
        "L'UTP in eccesso inibisce la reazione inversa legandosi al sito dell'enzima",
        "L'UDP-glucosio viene subito fosforilato dalla glicogeno sintasi nel citosol"],
    "m4s-08": [
        "UDP-glucosio sintasi",
        "Glucosio 1-P uridilchinasi",
        "Glicogeno sintasi (forma a)",
        "UTP-glucosio fosforilasi"],
    "m4s-09": [
        "Amilo-(1,6)-glucosidasi",
        "Oligo-(1,4→1,4)-glucantransferasi",
        "α-amilasi (1,4-glucanoidrolasi)",
        "Glicogeno ramificasi (1,4→1,4)"],
    "m4r-04": ["Ca²⁺", "AMP", "cAMP", "Glucagone"],
    "m4r-08": [
        "Fosforila la sintasi e la fosforilasi: spegne la sintesi e accende la degradazione del glicogeno",
        "Degrada il glicogeno nei lisosomi insieme all'α-glucosidasi acida, quando il glicogeno è in eccesso",
        "Sintetizza cAMP a partire dall'ATP quando arriva il glucagone, attivando la PKA sul glicogeno",
        "Defosforila soltanto la fosforilasi, senza alcun effetto sulla sintasi e sulla fosforilasi chinasi"],
    "m4e-02": [
        "Usa solo glicogeno muscolare, che basta per tutta la durata della corsa",
        "Usa soprattutto creatina fosfato, che si rigenera continuamente durante lo sforzo",
        "Produce molto più lattato, perché lo sforzo dura più a lungo e il glicogeno si esaurisce",
        "Usa soprattutto proteine muscolari come fonte principale di energia per la contrazione"],
    "m4g-01": [
        "Infezioni virali del fegato che causano accumulo di glicogeno",
        "Forme di diabete con eccesso di glicogeno epatico e muscolare",
        "Malattie endocrine da eccesso di glucagone in circolo",
        "Malattie autoimmuni dirette contro la glicogeno sintasi"],
    "m4g-03": [
        "Glucosio 6-fosfatasi epatica",
        "Enzima ramificante (amilo-transglicosilasi)",
        "Fosfofruttochinasi muscolare",
        "Glicogeno fosforilasi epatica"],
    "m4g-04": [
        "Contiene fruttosio, che entra nella glicolisi senza passare dal glucosio 6-fosfato",
        "Blocca la glicolisi epatica e lascia così più glucosio 6-fosfato disponibile per il sangue",
        "Fornisce una glucosio 6-fosfatasi vegetale che l'intestino assorbe e porta al fegato",
        "Viene trasformato direttamente in glicogeno nell'intestino, che poi lo rilascia nel sangue"],
    "m3m-08": [
        "Lo spermatozoo non ha mitocondri: l'energia per il flagello viene solo dalla glicolisi",
        "I mitocondri paterni vengono espulsi insieme al secondo corpo polare dopo la fecondazione",
        "Il DNA mitocondriale paterno è identico a quello materno, quindi non si distingue",
        "I mitocondri restano nella coda dello spermatozoo, che non entra mai nell'ovocita"],
})
FIX.update({
    "m3m-09": ["Gli enzimi del ciclo di Krebs", "Le porine della membrana esterna", "Gli istoni mitocondriali", "Il citocromo c e l'UCP1"],
    "m3m-10": [
        "L'ATP serve a fosforilare la proinsulina, che solo così viene tagliata nei granuli",
        "L'ATP apre i GLUT2, che fanno entrare più glucosio e stimolano così la trascrizione",
        "L'ATP attiva i canali Ca²⁺ del reticolo, che rilasciano l'insulina già legata alle membrane",
        "L'ATP apre i canali K⁺, la membrana si iperpolarizza ed esce Ca²⁺ che spinge fuori l'insulina"],
    "m3m-11": [
        "L'insulino-resistenza distrugge le cellule β per autoimmunità, con anticorpi contro le isole e calo della secrezione",
        "L'insulino-resistenza riduce i radicali, che inibiscono UCP2 nelle cellule β: più ATP e secrezione eccessiva di insulina",
        "I radicali aumentano la secrezione di insulina, che a lungo andare desensibilizza i recettori del muscolo e del fegato",
        "L'UCP2 indotta nelle cellule β aumenta la sintesi di ATP, che chiude i canali K⁺ in modo permanente e le esaurisce"],
    "m3m-12": [
        "Diminuisce il numero di mitocondri fino a zero, quindi l'ossigeno non viene più ridotto ad acqua",
        "Si attiva il mtDNA paterno rimasto silente, che codifica complessi respiratori meno efficienti",
        "Cala l'ossigeno nel sangue per la ridotta funzione polmonare, e l'ipossia genera radicali",
        "Diminuisce la produzione di UCP2 e di catalasi, perché il genoma nucleare smette di trascriverle"],
    "m3m-13": [
        "L'accumulo di mitocondri paterni non degradati",
        "La perdita progressiva dell'ATP sintasi di membrana",
        "Un eccesso di UCP1 nel tessuto adiposo bruno",
        "Un difetto della fusione dei perossisomi"],
    "m3m-14": [
        "Solo anemia e disturbi della coagulazione, perché colpiscono soprattutto gli eritrociti",
        "Solo cecità e sordità, perché i mitocondri difettosi sono presenti solo negli organi di senso",
        "Solo infezioni ricorrenti, perché i mitocondri servono soprattutto ai linfociti e ai macrofagi",
        "Nessun sintomo fino all'età adulta, perché il mtDNA mutato si attiva solo dopo la pubertà"],
    "m4d-12": [
        "Eteropolisaccaride di glucosio e galattosio",
        "Omopolisaccaride lineare di fruttosio",
        "Eteropolisaccaride ramificato di glucosio",
        "Omopolisaccaride lineare di glucosio"],
    "m4d-14": [
        "Glicogeno sintasi, enzima ramificante, glicogenina",
        "α-amilasi, maltasi, lattasi (dell'orletto a spazzola)",
        "Esochinasi, glucochinasi, fosfoglucomutasi",
        "Glicogeno fosforilasi, enzima ramificante, glicogenina"],
    "m4d-15": [
        "In entrambi diventa glucosio libero che va nel sangue tramite i GLUT2",
        "Muscolo: diventa glucosio e va nel sangue. Fegato: viene usato nella glicolisi",
        "In entrambi diventa UDP-glucosio e viene subito riconvertito in glicogeno",
        "Muscolo: entra nella via dei pentoso fosfati. Fegato: va solo in glicolisi"],
    "m4d-16": [
        "Non hanno GLUT nella membrana plasmatica, quindi il glucosio libero non può uscire",
        "Il glucosio libero è tossico per queste cellule e viene subito ossidato a CO₂",
        "La glicogeno fosforilasi non funziona fuori dal fegato e non forma glucosio 1-P",
        "La glucochinasi, a Km alta, rifosforilerebbe subito tutto il glucosio libero"],
    "m4d-17": [
        "L'enzima lavora nel citosol senza trasportatori, poi il glucosio passa nel RE con i GLUT4",
        "T1 porta dentro il glucosio, l'enzima lo fosforila nel lume e T2 fa uscire il G6P nel citosol",
        "Il G6P entra nel mitocondrio, dove viene idrolizzato e il glucosio esce con i GLUT2",
        "L'enzima è sulla faccia citosolica del RE e libera il glucosio senza bisogno di trasportatori"],
    "m4d-18": [
        "Monomero; il piridossal fosfato è legato a una serina fosforilata",
        "Tetramero αβγδ; il piridossal fosfato è libero nel sito attivo",
        "Omodimero; il FAD è legato covalentemente a un residuo di cisteina",
        "Omotetramero; la tiamina pirofosfato è legata a un residuo di istidina"],
    "m4d-19": [
        "I GLUT2 consumano ATP: servono molte molecole di glucosio per giustificare la spesa",
        "Il glucosio esce per esocitosi in vescicole, che si formano solo con glucosio abbondante",
        "Serve a saturare prima l'esochinasi epatica, che altrimenti lo rifosforila subito",
        "I GLUT2 hanno alta affinità e trattengono il glucosio finché non è in forte eccesso"],
    "m4s-10": [
        "Glicogeno fosforilasi, transferasi, α-1,6-glucosidasi",
        "Esochinasi, fosfoglucomutasi, glucosio 6-fosfatasi",
        "UDP-glucosio pirofosforilasi, PP1, fosforilasi chinasi",
        "Glicogeno sintasi, enzima deramificante, glucochinasi"],
    "m4s-13": [
        "La glicogenina fornisce l'UTP necessario ad attivare il glucosio 1-fosfato in UDP-glucosio",
        "La glicogenina forma i legami α-1,6 delle ramificazioni che la sintasi non sa fare",
        "La glicogenina fosforila la sintasi e la porta nella forma a, più attiva nel citosol",
        "Non sa formare legami α-1,4: è la glicogenina ad allungare tutte le catene esterne"],
    "m4s-14": [
        "Rende il glicogeno meno solubile in acqua, così precipita in granuli stabili nel citosol",
        "I rami contengono UTP legato, che fornisce subito l'energia per aggiungere nuovi glucosi",
        "Ogni ramo contiene una molecola di glicogenina, che fa da innesco per la sintesi e la degradazione",
        "Le ramificazioni proteggono i legami α-1,4 dalla fosforilasi, rallentando la degradazione"],
    "m4s-15": [
        "Solo durante il digiuno prolungato, quando il fegato produce glucosio con la gluconeogenesi",
        "Solo durante lo sforzo intenso, perché il muscolo ricostruisce il glicogeno mentre lo consuma",
        "Mai nel muscolo, che lo riceve già pronto dal fegato; nel fegato solo di notte, durante il sonno",
        "Solo quando la glicemia scende, perché l'ipoglicemia attiva la glicogeno sintasi tramite glucagone"],
    "m4s-16": [
        "Nella via dei pentoso fosfati",
        "Nel ciclo di Krebs (succinil-CoA)",
        "Nella β-ossidazione mitocondriale",
        "Nel metabolismo del fruttosio"],
    "m4r-11": [
        "Fosforilasi a (defosforilata, più attiva) e b (fosforilata, meno attiva)",
        "Fosforilasi R e T, entrambe fosforilate e ugualmente attive nel muscolo",
        "Fosforilasi I (indipendente) e D (dipendente dal glucosio 6-fosfato)",
        "Fosforilasi a (fosforilata, meno attiva) e b (defosforilata, più attiva)"],
    "m4r-12": [
        "La inibisce (effettore allosterico negativo)",
        "La fosforila (tramite la GSK3 attivata)",
        "Nessuno: agisce solo sulla fosforilasi",
        "La inattiva legandosi al sito catalitico"],
    "m4r-15": [
        "Attivata da glucagone e adrenalina; inibita da insulina, glucosio 6-P e glucosio",
        "Attivata da AMP e Ca²⁺; inibita da ATP e glucosio 6-P, come la fosforilasi",
        "Attivata da Ca²⁺ e cAMP; inibita da glucosio e insulina nel fegato e nel muscolo",
        "Attivata da insulina e adrenalina; inibita da glucagone e glucosio 6-fosfato"],
    "m4r-16": [
        "La fosforilasi ha siti multipli (più serine fosforilate), la sintasi uno solo",
        "Nessuna delle due viene fosforilata: sono regolate solo allostericamente",
        "Hanno gli stessi siti, fosforilati sempre insieme dalla stessa chinasi",
        "La sintasi è fosforilata su tirosine, la fosforilasi solo su treonine"],
    "m4r-17": [
        "Consuma tutto l'UDP-glucosio del citosol, che non resta disponibile per la sintasi",
        "Fosforila direttamente la sintasi e la porta nella forma b, meno attiva",
        "Degrada la glicogenina al centro del granulo, eliminando il primer per la sintesi",
        "Lega e attiva la PKA sulla GL: finché è in R la sintasi resta fosforilata dalla PKA"],
    "m4r-18": [
        "P1 e P2 dalla GSK3: inattivano la sintasi e staccano la PP1 dal glicogeno",
        "Solo P1, dall'adrenalina tramite PKA: la PP1 si lega più saldamente al glicogeno",
        "P2 dall'insulina: attiva la fosforilasi. P1 (PKA): la PP1 viene degradata",
        "P1 (adrenalina/PKA): attiva la PP1. P2 (chinasi insulino-sensibile): la PP1 si stacca"],
    "m4r-19": [
        "Lo stesso enzima, codificato da un solo gene, con la stessa regolazione",
        "Enzimi con reazioni diverse: fosforolisi nel muscolo, idrolisi nel fegato",
        "Le forme a e b dello stesso gene, prodotte per splicing alternativo",
        "Isoenzimi: stesso gene, ma regolati entrambi allo stesso modo dall'AMP"],
    "m4o-07": ["51, cellule β del pancreas", "14, cellule δ del pancreas", "9, ipofisi posteriore", "29, cellule β del pancreas"],
    "m4o-08": ["La corticale del surrene", "Il pancreas endocrino", "L'ipofisi anteriore", "La tiroide (cellule C)"],
    "m4o-09": [
        "Recettore tirosin-chinasico dimerico che si autofosforila",
        "Recettore intracellulare che agisce come fattore di trascrizione",
        "Canale ionico regolato dal ligando sulla membrana plasmatica",
        "Recettore a 7 eliche transmembrana con attività guanilato ciclasi"],
    "m4o-11": [
        "Solo il cAMP, che si lega direttamente alla subunità catalitica e la attiva del tutto",
        "Solo l'AMP, che segnala la contrazione e la attiva allostericamente in modo completo",
        "Solo il Ca²⁺ della contrazione, mentre la fosforilazione da PKA la inibisce parzialmente",
        "Solo l'insulina, che la fa defosforilare dalla PP1 e la porta nella forma più attiva"],
    "m4o-12": [
        "Vasodilatazione cutanea e splancnica, che disperde il calore prodotto dai muscoli",
        "Abbassa la glicemia, perché fa entrare tutto il glucosio nel muscolo tramite GLUT4",
        "Blocca la glicolisi muscolare, perché il muscolo deve usare solo acidi grassi",
        "Bradicardia e broncocostrizione, che riducono il consumo di ossigeno in attesa dello sforzo"],
    "m4o-13": [
        "Attiva la PKA, che fosforila e spegne fosforilasi chinasi e glicogeno fosforilasi",
        "Aumenta il cAMP, che lega la fosforilasi e la blocca nello stato T meno attivo",
        "Fosforila la fosforilasi tramite la PKB, portandola nella forma b inattiva",
        "Attiva la GSK3, che fosforila e spegne direttamente la glicogeno fosforilasi"],
    "m4o-14": [
        "Un ciclo futile: il glucosio prodotto dal glicogeno viene subito riconvertito in glicogeno",
        "Un feedback negativo: il glucosio prodotto spegne la secrezione di glucagone dal pancreas",
        "Una via senza enzimi: il glucagone stacca direttamente il glucosio dal glicogeno epatico",
        "Una conversione 1:1: ogni molecola di ormone libera una molecola di glucosio nel sangue"],
    "m4o-15": [
        "La aumenta: il glucosio formato serve a produrre l'ATP per la glicogenolisi",
        "Non cambia: glicolisi e glicogenolisi sono regolate in modo indipendente",
        "La trasferisce nel mitocondrio, dove il glucosio viene ossidato più in fretta",
        "La aumenta solo nel fegato, mentre la riduce nel muscolo per risparmiare glucosio"],
    "m5f-05": [
        "Solo fegato, dove aumenta la sintesi di PEPCK e di glucosio 6-fosfatasi nel nucleo",
        "Pancreas (inibisce l'insulina) e cervello (riduce il consumo di glucosio dei neuroni)",
        "Rene (aumenta il riassorbimento di glucosio) e intestino (aumenta l'assorbimento)",
        "Muscolo (stimola la glicogenolisi) e fegato (inibisce la glicolisi tramite la PFK2)"],
    "m5f-06": [
        "Perché finisce il glicogeno epatico, che è il precursore della gluconeogenesi",
        "Perché il cortisolo scende quasi a zero dopo i primi giorni di digiuno prolungato",
        "Perché il lattato prodotto dal muscolo si esaurisce e manca il substrato principale",
        "Perché il fegato perde la glucosio 6-fosfatasi dopo alcuni giorni di digiuno"],
    "m5r-03": [
        "Il malato è più energetico dell'ossalacetato e conserva il potere riducente",
        "Per consumare NADH nel citosol, dove serve a ridurre il piruvato a lattato",
        "L'ossalacetato è instabile e si decarbossila spontaneamente nella matrice",
        "Il malato serve per produrre ATP nel citosol tramite l'enzima malico"],
    "m5r-07": [
        "Non può fare glicolisi, quindi il fegato consuma tutto il glucosio presente nel sangue",
        "Non produce insulina, quindi il glucosio non entra nel fegato e viene perso con le urine",
        "Non assorbe glucosio dall'intestino per un difetto associato dei trasportatori SGLT1",
        "Il fegato trasforma tutto il glucosio 6-fosfato in acido urico e lattato da eliminare"],
    "m5r-08": [
        "Perché consuma il NADH che serve alla gliceraldeide 3-fosfato deidrogenasi citosolica",
        "Perché produce lattato in eccesso, che acidificherebbe l'epatocita durante il digiuno",
        "Perché inibisce la PEPCK quando le due sono attive insieme nel citosol dell'epatocita",
        "Perché consuma il GTP prodotto dal ciclo di Krebs, che serve alla PEPCK mitocondriale"],
    "m5r-11": [
        "Fosfofruttochinasi 1 (PFK1)",
        "Fruttosio 2,6-bisfosfatasi",
        "Aldolasi A (fruttosio bisfosfato)",
        "Fosfoglucosio isomerasi"],
    "m5g-04": [
        "Perché sono due isomeri diversi, uno prodotto nel fegato e l'altro nel muscolo scheletrico",
        "Perché il glicerolo 1-fosfato si forma dalla lipolisi e il 3-fosfato dalla glicolisi",
        "È un errore della sbobina: il glicerolo 1-fosfato non esiste nelle cellule umane",
        "Perché uno ha il fosfato sul carbonio centrale (C2) e l'altro su quello terminale"],
    "m5reg-01": [
        "Per fosforilazione da parte della PKA",
        "Allostericamente dall'AMP e dall'ADP",
        "Per compartimentazione nel nucleo",
        "Allostericamente dall'acetil-CoA"],
    "m5reg-03": [
        "IRE (insulina), SRE (steroli), HRE (ipossia, tramite HIF-1α)",
        "SRE (steroli), CRE (cAMP/glucagone), ERE (estrogeni)",
        "HRE (ipossia), IRE (insulina), TRE (ormoni tiroidei)",
        "ARE (androgeni), GRE (glucocorticoidi), IRE (insulina)"],
    "m5reg-07": [
        "L'AMP è un prodotto della gluconeogenesi e ne frena la velocità per feedback negativo",
        "L'AMP attiva la PEPCK, quindi serve a coordinare i due enzimi della gluconeogenesi",
        "Non ha un senso fisiologico: è un effetto osservato solo in vitro con enzima purificato",
        "AMP alto segnala abbondanza di energia: la cellula può permettersi di fare glucosio"],
})
FIX.update({
    "m5a-02": [
        "Iperglicemia, insulina, acidi grassi",
        "Acidi grassi, corpi chetonici, somatostatina",
        "Iperglicemia, GLP-1, somatostatina",
        "Ipoglicemia, insulina, corpi chetonici"],
    "m5a-03": [
        "La gluconeogenesi si blocca del tutto finché il ritmo circadiano non si riadatta",
        "La PEPCK raddoppia la sua espressione per compensare lo stress del viaggio",
        "Non cambia nulla: la PEPCK è costitutiva e non segue un ritmo circadiano",
        "Il cortisolo smette di essere secreto e la PEPCK scompare dagli epatociti"],
    "m5a-05": [
        "Erano obesi e sedentari, con accumulo di glicogeno nel muscolo e nel fegato",
        "Avevano ipoglicemia grave, perché il muscolo consumava tutto il glucosio del sangue",
        "Non mostravano differenze di resistenza, ma avevano più massa muscolare dei normali",
        "Correvano meno, perché il muscolo produceva troppo lattato e consumava più glicogeno"],
    "m6r-01": [
        "NADH e glucosio 6-fosfato",
        "ATP e ribulosio 5-fosfato",
        "NADPH e desossiribosio",
        "FADH₂ e xilulosio 5-fosfato"],
    "m6r-03": [
        "Transchetolasi (con TPP)",
        "Esochinasi I (ubiquitaria)",
        "6-fosfogluconato deidrogenasi",
        "Lattonasi (6-fosfogluconolattonasi)"],
    "m6r-05": [
        "Un frammento di 3 atomi di carbonio",
        "Un gruppo fosfato dal C1 al C6",
        "Un'unità di CO₂ legata alla biotina",
        "Un frammento di 4 atomi di carbonio"],
    "m6r-06": ["Piridossal fosfato", "Biotina (vitamina H)", "NADP⁺ legato", "Acido lipoico"],
    "m6r-07": [
        "Ribulosio 5-fosfato epimerasi",
        "Transaldolasi (con base di Schiff)",
        "Fosfopentosio mutasi",
        "Ribosio fosfato pirofosfochinasi"],
    "m6g-03": [
        "Muscolo scheletrico, cuore, diaframma e cervello, dove il consumo di energia è massimo",
        "Cervello e midollo spinale, che usano quasi solo glucosio come fonte di energia",
        "Osso e cartilagine, dove serve NADPH per la sintesi della matrice extracellulare",
        "Rene e intestino tenue, dove la via fornisce l'energia per il trasporto del glucosio"],
    "m6g-04": [
        "Solo la concentrazione di glucosio nel sangue",
        "Solo l'insulina, che attiva la G6PD dopo il pasto",
        "La disponibilità di ossigeno e di FAD nel citosol",
        "Il rapporto NAD⁺/NADH nella matrice mitocondriale"],
    "m6n-02": [
        "Un'allergia IgE-mediata alle proteine delle fave",
        "Un deficit di vitamina B12 da dieta a base di legumi",
        "Una crisi emolitica da deficit di piruvato chinasi da fave",
        "Un'anemia da carenza di ferro tipica del Mediterraneo"],
    "m6n-08": [
        "Inibisce la G6PD epatica, così gli epatociti restano senza NADPH e senza difesa antiossidante",
        "Blocca il complesso IV dei mitocondri epatici come fa il cianuro, fermando la sintesi di ATP",
        "Consuma tutto il glicogeno epatico e causa una necrosi degli epatociti da grave ipoglicemia",
        "Viene coniugato al glucuronato in eccesso e il coniugato precipita nei canalicoli biliari"],
    "m6n-14": [
        "Antidepressivi triciclici",
        "Inibitori della ricaptazione della serotonina",
        "Antipsicotici di prima generazione",
        "Analgesici oppioidi"],
    "b1c-01": ["Paracrina (per diffusione)", "Endocrina (tramite il sangue)", "Autocrina (sulla stessa cellula)", "Sinaptica (tramite neurotrasmettitori)"],
    "b1c-03": [
        "Proteine intere e piccoli peptidi",
        "Solo acqua e ioni monovalenti",
        "Ribosomi e mRNA già tradotti",
        "Proteine, acidi nucleici e lipidi"],
    "b1c-04": [
        "Delta viene internalizzato nella cellula bersaglio e trasloca nel nucleo, dove lega direttamente il DNA con CREB",
        "Il legame con Delta attiva l'adenilato ciclasi associata a Notch: il cAMP attiva la PKA, che fosforila CSL nel nucleo",
        "Il legame con Delta apre il canale per il Ca²⁺ formato da Notch: il Ca²⁺ attiva la calcineurina, che entra nel nucleo",
        "Il legame con Delta provoca la dimerizzazione e l'autofosforilazione di Notch, che recluta STAT e lo porta nel nucleo"],
    "b1c-05": [
        "L'ormone agisce su cellule vicine e deve legarsi prima che venga degradato",
        "L'ormone deve dissociarsi rapidamente per permettere segnali brevi e ripetuti",
        "L'ormone è sempre idrofobico e viaggia legato a proteine di trasporto plasmatiche",
        "L'ormone arriva a concentrazioni molto alte (10⁻⁶–10⁻³ M) e satura i recettori"],
    "b1c-06": [
        "Sono degradate dalle collagenasi della matrice extracellulare appena assemblate",
        "Non sono glicosilate e quindi vengono riconosciute subito dal proteasoma",
        "Si formano nel citosol e non vengono mai inserite stabilmente nella membrana",
        "Il loro poro lascia entrare proteasi dalla cellula vicina, che le tagliano"],
    "b1c-07": ["CREB", "STAT3", "NF-κB", "fos/jun"],
    "b1c-08": [
        "Nella giunzione neuromuscolare e nelle sinapsi chimiche del sistema nervoso",
        "Nel controllo della glicemia da parte di insulina e glucagone nel sangue",
        "Nella fototrasduzione della retina, dove la luce attiva la rodopsina",
        "Nelle sinapsi elettriche del cuore, tramite le gap junction tra i cardiomiociti"],
    "bh1c-01": [
        "Concentrazione bassa e affinità del recettore altissima, così il ligando resta legato a lungo dopo ogni impulso",
        "Trasporto nel sangue legato a proteine plasmatiche, così il ligando arriva lentamente e in modo costante",
        "Recettore nucleare con effetto genico, così ogni impulso modifica in modo duraturo la trascrizione",
        "Affinità del recettore altissima e degradazione lenta, così il complesso resiste alla diluizione del ligando"],
    "b1r-02": [
        "Cresce lentamente e linearmente con il ligando, senza mai raggiungere un plateau",
        "Diminuisce aumentando il ligando, perché i recettori vengono internalizzati",
        "Non dipende dalla concentrazione di ligando, perché i siti sono sempre occupati",
        "Ha un andamento sigmoide che non satura, perché i siti continuano ad aumentare"],
    "b1r-03": ["Bmax", "Kd", "−Bmax", "1/Bmax"],
    "b1r-04": [
        "Misura la velocità massima degli enzimi bersaglio e la loro costante catalitica",
        "Misura il punto isoelettrico dei recettori e la loro carica a pH fisiologico",
        "Determina la sequenza amminoacidica del recettore e i suoi domini funzionali",
        "Stima l'emivita del farmaco nel plasma e la sua velocità di eliminazione renale"],
    "bh1r-01": [
        "B ha affinità maggiore perché la sua Kd è più alta: lega più farmaco per ogni recettore occupato",
        "Hanno la stessa affinità se hanno lo stesso Bmax: la Kd indica solo la velocità di dissociazione",
        "A occupa per forza più recettori a saturazione: con Kd bassa il Bmax del farmaco A è maggiore",
        "La Kd non dice nulla sull'affinità: per confrontarle serve conoscere la concentrazione di recettore"],
    "b1i-01": [
        "Sulla membrana plasmatica",
        "Nella matrice extracellulare",
        "Nel sangue (proteine di trasporto)",
        "Nel reticolo endoplasmatico"],
    "b1i-03": [
        "L'ormone stesso, che entra nella cellula e agisce direttamente sugli enzimi bersaglio",
        "Il recettore attivato, che si stacca dalla membrana e migra nel nucleo per agire",
        "La proteina di trasporto che porta l'ormone nel sangue fino alla cellula bersaglio",
        "Un secondo ormone rilasciato dalla cellula bersaglio che agisce sulle cellule vicine"],
    "b1i-05": [
        "Degradano i secondi messaggeri e spengono il segnale appena il ligando si stacca",
        "Trasportano gli ormoni idrofobici nel sangue fino alle cellule bersaglio",
        "Formano il poro dei recettori canale e ne regolano l'apertura e la chiusura",
        "Fosforilano direttamente i fattori di trascrizione e li portano nel nucleo"],
    "b1i-06": ["SH2", "SH3", "PTB", "DD"],
    "bh1i-01": [
        "È idrofobico ma troppo grande per attraversare la membrana: entra per endocitosi e viene degradato",
        "Viene sempre degradato nel sangue dalle proteasi plasmatiche prima di raggiungere il nucleo",
        "I peptidi non possono legare proteine nucleari, quindi agiscono solo su enzimi del citosol",
        "Agisce solo su cellule vicine (paracrino), che non possiedono recettori nucleari per i peptidi"],
    "b2c-01": [
        "Nucleari, citosolici, di membrana plasmatica e mitocondriali, secondo la sede",
        "Recettori canale, accoppiati a proteine G, nucleari, per gli ormoni steroidei",
        "Tirosin-chinasici, serin-chinasici, fosfatasi e proteasi di membrana",
        "Recettori canale, con attività catalitica, per le integrine e per le caderine"],
    "b2c-02": [
        "Un recettore a 7 eliche accoppiato a proteina G",
        "Un recettore tirosin-chinasico dimerico",
        "Un recettore nucleare che lega il DNA",
        "Un canale per anioni (Cl⁻) controllato da ligando"],
    "b2c-03": [
        "Acetilcolina e glutammato: aprono canali per Na⁺ e iperpolarizzano",
        "Serotonina e ATP: aprono canali per Ca²⁺ e iperpolarizzano la membrana",
        "Adrenalina e glicina: chiudono canali per K⁺ e depolarizzano",
        "GABA e glutammato: aprono canali per cationi (Na⁺) e depolarizzano"],
    "b2c-04": [
        "Endocitosi del recettore nicotinico e sua degradazione nei lisosomi della fibra muscolare",
        "Attività GTPasica intrinseca del recettore, che idrolizza il GTP e chiude il canale",
        "Fosforilazione del recettore da parte della PKA, che lo stacca dalla proteina G",
        "Ricaptazione dell'acetilcolina intera nel terminale e sua idrolisi dalle MAO mitocondriali"],
    "b2c-05": [
        "I veri sono agonisti che desensibilizzano il recettore; i depolarizzanti (succinilcolina) sono antagonisti dell'acetilcolina",
        "Entrambi inibiscono l'acetilcolinesterasi: i veri in modo reversibile, i depolarizzanti (succinilcolina) in modo irreversibile",
        "I veri bloccano i canali del Na⁺ della fibra muscolare; i depolarizzanti (succinilcolina) bloccano i canali del Ca²⁺",
        "I veri agiscono sui recettori muscarinici; i depolarizzanti (succinilcolina) aprono i canali K⁺ e iperpolarizzano il muscolo"],
    "b2c-06": [
        "Lega direttamente il curaro nel plasma e lo inattiva prima che raggiunga la placca motrice",
        "Attiva i recettori muscarinici, che sostituiscono i nicotinici bloccati nella contrazione",
        "Blocca i canali del Na⁺ voltaggio-dipendenti, prolungando la depolarizzazione della fibra",
        "Stimola la sintesi di acetilcolina nel terminale, che compete con il curaro per l'enzima"],
    "b2c-07": ["M1, M3 e M5 (numero dispari)", "Solo M1 (neuronale)", "Tutti i cinque sottotipi", "M3 e M5 (ghiandolari)"],
    "b2c-09": [
        "Glicina, per transamminazione",
        "Tirosina, per idrossilazione",
        "Triptofano, per decarbossilazione",
        "Acetil-CoA, per condensazione"],
    "bh2c-01": [
        "L'atropina riattiva l'acetilcolinesterasi bloccata, staccando il gas nervino dal sito attivo dell'enzima",
        "L'atropina aumenta la sintesi di acetilcolina, compensando la perdita di segnale dovuta al gas nervino",
        "L'atropina degrada il gas nervino nel plasma prima che raggiunga le sinapsi, impedendo nuovi danni",
        "L'acetilcolina scende a zero perché il gas nervino la distrugge: l'atropina ne simula l'azione sul recettore"],
    "bh2c-02": [
        "Recettore canale: apre direttamente un poro per il Cl⁻ che iperpolarizza la membrana",
        "Recettore catalitico: attiva una tirosin-chinasi che fosforila e chiude i canali Na⁺",
        "Eterodimero GPCR: la subunità αs attiva l'adenilato ciclasi e apre i canali Ca²⁺",
        "Recettore nucleare: lega il DNA e reprime la trascrizione dei geni eccitatori"],
})
FIX.update({
    "b2r-01": [
        "Il ligando li apre come un canale ionico e il Ca²⁺ entrato attiva il dominio chinasico",
        "Il ligando fa scambiare GDP con GTP sulla subunità α associata alla coda intracellulare",
        "Il ligando li fa entrare nel nucleo, dove fosforilano direttamente i fattori di trascrizione",
        "Il ligando ne induce la dimerizzazione e la fosforilazione incrociata sulle serine da parte della PKA"],
    "b2r-03": [
        "RTK → Raf → Ras → MEK → MAP chinasi → STAT",
        "RTK → SOS → Raf → Ras → MAP chinasi → MEK → fos/jun",
        "RTK → GRB2 → PKA → Ras → MEK → CREB",
        "RTK → Ras → SOS → MEK → Raf → MAP chinasi → fos/jun"],
    "b2r-04": [
        "GEF idrolizza il GTP (spegne); GAP scambia GDP con GTP (attiva)",
        "Entrambi la attivano: GEF in membrana, GAP nel citosol con il GTP",
        "Entrambi la fosforilano: GEF su serine (attiva), GAP su tirosine (spegne)",
        "GEF lega Ras al recettore (attiva); GAP la stacca dalla membrana (spegne)"],
    "b2r-05": [
        "Ras resta sempre inattiva e la via proliferativa non si accende neanche con il fattore di crescita",
        "Il recettore non dimerizza più e la via si ferma a monte di Ras, senza autofosforilazione",
        "Si blocca solo MEK, mentre Raf e la MAP chinasi restano attivabili normalmente dal recettore",
        "Ras resta legata al GDP e SOS non riesce più a caricare il GTP, spegnendo la cascata"],
    "b2r-06": [
        "Con la cristallografia di MEK legato a Raf e a Ras, che ha mostrato l'ordine di contatto",
        "Bloccando MEK con un inibitore, Ras non si attiva più: quindi MEK sta a monte di Ras",
        "Misurando il cAMP prodotto da MEK dopo l'attivazione di Ras con il fattore di crescita",
        "In un mutante Raf inattivo, una Ras oncogenica ripristina comunque l'attivazione di MEK"],
    "b2r-08": [
        "È un canale ionico che si apre quando lega l'insulina",
        "Non ha attività chinasica e usa la JAK associata",
        "È un recettore nucleare che lega l'insulina nel citosol",
        "È un monomero che dimerizza solo dopo il legame"],
    "bh2r-01": [
        "Con molti recettori in membrana il recettore diventa un canale ionico sempre aperto",
        "Con tanti recettori Ras perde il GTP più in fretta e resta attiva più a lungo nel tempo",
        "Con molti recettori manca SOS, quindi Ras resta carica di GTP senza essere regolata",
        "Con molti recettori questi migrano nel nucleo e attivano direttamente la trascrizione"],
    "bh2r-02": [
        "Ras non si attiva mai, perché senza GAP non può caricare il GTP",
        "Il recettore non si autofosforila e la via MAPK resta spenta",
        "Aumenta il cAMP, perché Ras attiva l'adenilato ciclasi al posto di Raf",
        "La MAP chinasi non entra nel nucleo e i geni bersaglio restano spenti"],
    "b2t-02": [
        "È un canale ionico che depolarizza la cellula tumorale",
        "Degrada gli altri HER e libera i loro fattori di crescita",
        "Lega direttamente il DNA come un fattore di trascrizione",
        "Forma omodimeri solo con EGF e li rende sempre attivi"],
    "b2t-04": ["HER2 (ErbB2)", "HER4 (ErbB4)", "TGF-β (tipo II)", "HER3 (ErbB3)"],
    "bh2t-01": [
        "Inibitori dell'acetilcolinesterasi e curari, che bloccano la trasmissione del segnale",
        "Analoghi del cAMP e inibitori delle fosfodiesterasi, che spengono la via di Ras e Raf",
        "Agonisti di Ras e inibitori di GAP, che esauriscono la cellula tumorale per iperstimolo",
        "Steroidi e ormoni tiroidei, che riducono la trascrizione dei recettori nel nucleo"],
    "b2s-01": ["Insulina ed EGF", "Acetilcolina e GABA", "EPO e interleuchine", "PDGF e NGF"],
    "b2s-03": [
        "Vengono subito degradate nel proteasoma e la loro affinità per il DNA cala",
        "Escono dal nucleo e si legano al recettore come monomeri inattivi in membrana",
        "Diventano canali ionici e fanno entrare Ca²⁺ che attiva la trascrizione",
        "Formano omodimeri che fosforilano JAK e attivano STAT nel citosol"],
    "b2s-04": ["Tirosina", "Istidina e aspartato", "Lisina e arginina", "Tirosina e istidina"],
    "b2k-02": [
        "Il recettore per le citochine è un canale ionico: lo apre la chinasi JAK associata alla membrana",
        "L'RTK non si fosforila mai: è la JAK associata a fosforilare le proteine bersaglio",
        "Sono identici: entrambi hanno attività tirosin-chinasica intrinseca nel dominio intracellulare",
        "Il recettore per le citochine ha attività serin-chinasica intrinseca e non ha bisogno di JAK"],
    "b2k-03": ["Insulina", "Glucagone", "Aldosterone", "Trombopoietina"][:3] + ["Tiroxina (T4)"],
    "b2k-04": [
        "Fosforila JAK e la stacca dal recettore per spegnere il segnale",
        "Apre canali ionici della membrana e fa entrare il Ca²⁺",
        "Viene secreta e agisce come citochina sulle cellule vicine",
        "Resta nel citosol e attiva Ras tramite il complesso GRB2-SOS"],
    "bh2k-01": [
        "Il recettore si autofosforila comunque e STAT viene attivata normalmente in membrana",
        "STAT entra nel nucleo anche senza fosforilazione e attiva i geni in modo ridotto",
        "Aumenta la produzione di globuli rossi perché il segnale non viene più spento",
        "Si attiva la via di Ras al suo posto, che compensa del tutto la mancanza di JAK"],
    "b3g-03": [
        "Il loop extracellulare E1, il più corto",
        "L'N-terminale extracellulare glicosilato",
        "Il C-terminale, sede della palmitoilazione",
        "Il loop citoplasmatico C1, il più corto"],
    "b3g-04": [
        "Si lega più forte a βγ e il trimero si stacca dalla membrana per raggiungere l'effettore",
        "Si separa da βγ ed entra nel nucleo, dove attiva direttamente la trascrizione genica",
        "Viene subito ubiquitinata e degradata nel proteasoma per spegnere il segnale",
        "Resta legata a βγ e al recettore e attiva l'effettore solo dopo aver idrolizzato il GTP"],
    "b3g-05": [
        "Ogni GPCR ha una sola proteina G dedicata, codificata dallo stesso gene del recettore",
        "La proteina G si autoassembla a caso, quindi ogni cellula ne produce combinazioni diverse",
        "Le combinazioni nascono dallo splicing alternativo del recettore, non da geni diversi",
        "Pochi geni per α, β e γ, ma molte modificazioni post-traduzionali che le rendono diverse"],
    "bh3g-01": [
        "La Gαs non lega più il GTP, quindi il recettore del GHRH resta sempre attivo",
        "Il recettore del GHRH è assente e l'ipofisi secerne GH senza alcun controllo",
        "L'ipofisi non riceve più il feedback del fegato, che smette di produrre IGF-1",
        "La Gαs mutata attiva la fosfolipasi C al posto dell'adenilato ciclasi, alzando il Ca²⁺"],
    "b3c-03": [
        "Viene fosforilata dal recettore attivato, che la stacca dalla membrana e la porta nel citosol",
        "Lega il GTP sulla subunità catalitica, che si separa dalle regolatrici come una proteina G",
        "Il cAMP si lega alle subunità catalitiche (2 per subunità), che rilasciano le regolatrici",
        "Entra nel nucleo, dove il cAMP la separa dal DNA e libera le subunità catalitiche"],
    "b3c-04": [
        "Gs: prostaglandine, adenosina. Gi: adrenalina, glucagone, ACTH",
        "Tutti usano Gs, che può attivare o inibire l'adenilato ciclasi",
        "Gs: insulina, IGF-1. Gi: adrenalina, glucagone, noradrenalina",
        "Gs: acetilcolina (muscarinici dispari). Gi: glucagone, ACTH"],
    "b3c-05": [
        "Apre i canali del Ca²⁺ della membrana plasmatica e attiva la calmodulina",
        "Degrada il cAMP residuo nel citosol, spegnendo la PKA che lo ha fosforilato",
        "Inattiva il recettore β-adrenergico fosforilandone la coda C-terminale",
        "Lega le sequenze CRE nel citosol e blocca la traduzione degli mRNA bersaglio"],
    "b3c-06": [
        "Inibisce l'adenilato ciclasi degli enterociti, che non producono più cAMP: si perdono acqua e sali",
        "ADP-ribosila la Gαi, che resta sempre attiva: il cAMP scende e l'intestino non riassorbe più l'acqua",
        "Degrada il cAMP attivando la fosfodiesterasi, che apre i canali del Cl⁻ e fa perdere acqua e sali",
        "Fosforila un'arginina della Gαs, che non lega più il GTP: il cAMP crolla e l'acqua resta nel lume"],
    "b3c-07": [
        "Attiva la Gαs in modo permanente, quindi l'adenilato ciclasi resta stimolata e il cAMP sale",
        "Blocca la fosfodiesterasi del cAMP, che non viene più degradato e resta alto nella cellula",
        "ADP-ribosila la Gαi rendendola sempre attiva: l'adenilato ciclasi resta inibita e il cAMP scende",
        "ADP-ribosila la Gαs, che non idrolizza più il GTP: l'adenilato ciclasi è attiva e il cAMP sale"],
    "b3c-10": [
        "Che il cAMP è assente e le subunità sono legate",
        "Che la PKA è stata degradata nel proteasoma",
        "Che la proteina G è inattiva e lega il GDP",
        "Che il cAMP è salito e le subunità si sono unite"],
    "bh3c-01": [
        "Attivano direttamente la PKA, che fosforila e desensibilizza il recettore β-adrenergico",
        "Aumentano il cAMP attivando l'adenilato ciclasi, che compensa il calo dovuto alla Gαi",
        "Bloccano il recettore muscarinico, impedendo all'acetilcolina di agire troppo a lungo",
        "Fosforilano il recettore β-adrenergico tramite la βARK e lo staccano dall'adrenalina"],
    "bh3c-02": [
        "Gαi ADP-ribosilata → adenilato ciclasi inibita → cAMP basso → riassorbimento bloccato → perdita di acqua e sali",
        "Gαs ADP-ribosilata → fosfodiesterasi attivata → cAMP basso → canali chiusi → acqua trattenuta nel lume",
        "Recettore muscarinico bloccato → Gq inattiva → IP₃ basso → Ca²⁺ basso → secrezione di acqua e sali",
        "Gαs fosforilata → PKA inibita → chiusura dei canali Cl⁻ → riassorbimento ridotto → diarrea acquosa"],
    "bh3c-03": [
        "Amplifica il segnale: la fosfodiesterasi produce altro cAMP a partire dall'AMP già presente",
        "Serve a produrre cGMP dal cAMP, così la cellula attiva anche la PKG insieme alla PKA",
        "Attiva la proteina G: il prodotto della fosfodiesterasi riporta la Gα nella forma legata al GTP",
        "Non ha significato fisiologico: è un bersaglio casuale della PKA, osservato solo in vitro"],
    "b3s-01": [
        "La fosforilazione della Gα",
        "La degradazione della Gβγ",
        "L'endocitosi della Gα con il recettore",
        "L'attività GTPasica della Gβγ"],
    "b3s-02": ["AKAP", "GRB2", "SOS (GEF)", "Calmodulina"],
    "b3s-03": [
        "La PKA, richiamata dal cAMP prodotto dalla Gαs",
        "La PKC, richiamata dal DAG di membrana",
        "La βARK, richiamata dalla Gαs legata al GTP",
        "La MAP chinasi, richiamata da Ras attivata"],
    "b3s-04": [
        "Viene sempre degradato nel lisosoma, senza possibilità di riciclo in membrana",
        "Resta nell'endosoma per sempre, legato all'arrestina e al ligando",
        "Viene secreto nello spazio extracellulare insieme all'ormone legato",
        "Viene fosforilato di nuovo dalla PKA e torna in membrana già attivo"],
    "bh3s-01": [
        "L'adrenalina viene degradata dalle MAO del cuore e la sua concentrazione effettiva crolla",
        "La Gs perde la sua ancora prenilica e si stacca dalla membrana, lontano dall'adenilato ciclasi",
        "Il cAMP non attiva più la PKA, perché le subunità regolatrici vengono degradate nel tempo",
        "L'adenilato ciclasi viene sintetizzata di meno, perché la PKA ne reprime il gene tramite CREB"],
    "b3m-03": [
        "Sulla membrana plasmatica: è un GPCR a 7 eliche",
        "Nel nucleo: come gli steroidi, l'NO regola la trascrizione",
        "Nel reticolo endoplasmatico: libera Ca²⁺ come l'IP₃",
        "Nel citosol: l'NO non può attraversare la membrana"],
    "b3m-04": [
        "Un GPCR accoppiato a Gs che attiva l'adenilato ciclasi",
        "La guanilato ciclasi solubile del citosol, con un eme",
        "Un recettore canale per il Na⁺ dei tubuli renali",
        "Un recettore di membrana con attività tirosin-chinasica"],
    "b3m-05": [
        "↑cAMP → PKA → fosforila la chinasi delle catene leggere della miosina → contrazione del vaso",
        "↑cGMP → PKG → apre i canali del Ca²⁺ voltaggio-dipendenti → contrazione e poi rilassamento",
        "↑IP₃ → rilascio di Ca²⁺ dal reticolo → attivazione della NO sintasi endoteliale → rilassamento",
        "↑DAG → PKC → inibisce la fosfatasi delle catene leggere della miosina → rilassamento del vaso"],
    "b3m-06": [
        "Attiva la guanilato ciclasi solubile, che produce più cGMP nella muscolatura liscia dei vasi",
        "Libera NO nell'endotelio, che diffonde nel muscolo liscio e fa salire il cAMP",
        "Blocca la PKG, impedendo la contrazione della muscolatura liscia del tessuto erettile",
        "Inibisce la fosfodiesterasi 3, mantenendo alto più a lungo il cAMP nella muscolatura dei vasi"],
    "b3m-07": [
        "L'NO non attraversa più la membrana, che si è irrigidita dopo il primo stimolo",
        "La guanilato ciclasi solubile è stata degradata dal proteasoma dopo il primo picco",
        "Il GTP della cellula è esaurito e non può essere convertito in cGMP",
        "La PKA ha fosforilato la guanilato ciclasi e l'ha staccata dal suo gruppo eme"],
})
FIX.update({
    "bh3m-01": [
        "NO → GPCR di membrana → Gs → adenilato ciclasi → cAMP → PKA → fosforilazione della miosina → contrazione",
        "NO → recettore di membrana → PLCβ → IP₃ → rilascio di Ca²⁺ dal RE → calmodulina → contrazione",
        "NO → guanilato ciclasi di membrana → cGMP → PKC → ↑Ca²⁺ e fosforilazione delle catene leggere → contrazione",
        "NO → fosfodiesterasi 5 → più cGMP → PKA → ↓Ca²⁺ e fosforilazione delle catene pesanti → rilassamento"],
    "b4c-01": ["≈ 10⁻³–10⁻⁴ M", "≈ 10⁻¹–10⁻² M", "≈ 10⁻¹⁰–10⁻¹¹ M", "≈ 10⁻⁵–10⁻⁶ M"],
    "b4c-02": [
        "Per diffusione semplice secondo gradiente",
        "Con i recettori per l'IP₃ della membrana plasmatica",
        "Con i recettori per la rianodina e con i GLUT",
        "Con la Na⁺/K⁺-ATPasi e con il simporto Na⁺/Ca²⁺"],
    "b4c-03": [
        "Solo la contrazione muscolare scheletrica e cardiaca, perché il Ca²⁺ agisce esclusivamente sulla troponina C",
        "Solo la trascrizione genica, perché il Ca²⁺ entra nel nucleo e si lega direttamente alle sequenze promotrici",
        "Solo la sintesi di ATP nel mitocondrio, perché il Ca²⁺ attiva le deidrogenasi del ciclo di Krebs e nient'altro",
        "Solo la secrezione di ormoni e neurotrasmettitori, perché il Ca²⁺ agisce solo sull'esocitosi delle vescicole"],
    "b4c-04": [
        "Un GPCR a 7 eliche della membrana plasmatica, accoppiato a Gq, che apre i canali del Ca²⁺ voltaggio-dipendenti",
        "Un recettore tirosin-chinasico del RE che, legando l'IP₃, dimerizza e fosforila i canali del Ca²⁺ vicini",
        "Un canale del RE a 5 subunità come il nicotinico, ognuna con 4 eliche, con residui basici nel poro",
        "Un canale della membrana plasmatica a 4 subunità, ognuna con 2 eliche, selettivo per il Na⁺ e non per il Ca²⁺"],
    "b4c-05": [
        "La rianodina endogena prodotta dal muscolo",
        "L'IP₃ prodotto dalla fosfolipasi C di membrana",
        "Il cAMP, tramite la PKA legata al canale",
        "Il Mg²⁺ citosolico (rilascio indotto da Mg²⁺)"],
    "b4c-06": [
        "Bassa: lo chiude (paralisi). Alta (µM): blocca il canale semiaperto (contrazione massiva)",
        "Lo apre sempre, a qualsiasi concentrazione, provocando una contrazione tetanica prolungata",
        "Non agisce sul canale: blocca invece la Ca²⁺-ATPasi del reticolo, a basse e ad alte dosi",
        "Bassa: lo apre del tutto (rilassamento). Alta (µM): lo apre parzialmente (contrazione lieve)"],
    "b4c-07": [
        "Cervello, fegato, rene",
        "Miocardio, muscolo scheletrico, fegato",
        "Tutti e tre nel muscolo liscio",
        "Muscolo scheletrico, cervello, miocardio"],
    "bh4c-01": [
        "L'IP₃ apre anche la Ca²⁺-ATPasi della membrana, che pompa altro Ca²⁺ dentro la cellula dall'esterno",
        "Il Ca²⁺ blocca l'antiporto Na⁺/Ca²⁺ in modo permanente, così tutto quello rilasciato resta nel citosol",
        "La calmodulina rilascia il Ca²⁺ che aveva legato a riposo, raddoppiando subito la concentrazione libera",
        "Il mitocondrio smette di accumulare Ca²⁺ e rilascia anche quello della matrice, amplificando il segnale"],
    "b4m-02": [
        "Un foglietto β a barile che lega il Ca²⁺ al centro",
        "Un dito di zinco che lega il Ca²⁺ al posto dello Zn²⁺",
        "Due foglietti β uniti da un'elica che lega il Mg²⁺",
        "Un'α-elica avvolta su sé stessa con due cisteine"],
    "b4m-03": [
        "Viene degradata nel proteasoma, liberando le proteine bersaglio che teneva inibite nel citosol",
        "Entra nel reticolo endoplasmatico e chiude i recettori per l'IP₃, spegnendo il rilascio di Ca²⁺",
        "Si lega direttamente al DNA nel nucleo e attiva la trascrizione dei geni con sequenze CRE",
        "Si apre e perde affinità per le proteine bersaglio, che restano inattive finché il Ca²⁺ non scende"],
    "b4m-04": [
        "Il Ca²⁺ attiva la glicogeno sintasi, che libera glucosio 1-P dalle estremità del glicogeno",
        "Il Ca²⁺ inibisce la fosforilasi chinasi, così la PKA può attivare da sola la fosforilasi",
        "Il Ca²⁺ attiva la PP1, che defosforila la glicogeno fosforilasi portandola nella forma a",
        "Ca²⁺-calmodulina attiva la PKA, che fosforila e attiva direttamente la glicogeno fosforilasi"],
    "b4m-05": [
        "Il Ca²⁺ si lega direttamente al DNA e cambia la conformazione dei promotori dei geni bersaglio",
        "Il Ca²⁺ attiva STAT tramite JAK, che dimerizza ed entra nel nucleo con il Ca²⁺ legato",
        "Il Ca²⁺ inibisce la RNA polimerasi II, riducendo la trascrizione di tutti i geni della cellula",
        "Ca²⁺-calmodulina attiva la PKA, che fosforila fattori di trascrizione come STAT e Smad"],
    "b4m-06": [
        "Entrambe attive quando sono fosforilate",
        "Entrambe inattive quando sono fosforilate",
        "Sintasi fosforilata attiva, fosforilasi fosforilata inattiva",
        "Sintasi fosforilata attiva, fosforilasi fosforilata attiva"],
    "bh4m-01": [
        "Attiva la glicogeno sintasi e inibisce la fosforilasi chinasi: il muscolo riforma le riserve durante lo sforzo",
        "Non ha effetti diretti sul glicogeno: il Ca²⁺ agisce solo sulla troponina e sulla contrazione dei filamenti",
        "Attiva la PP1, che defosforila sia la sintasi sia la fosforilasi: degradazione e sintesi procedono insieme",
        "Blocca la glicolisi per risparmiare ATP e attiva la sintasi: il glucosio 6-P viene accumulato come glicogeno"],
    "b4p-04": [
        "cAMP e Ca²⁺ (più fosfatidilcolina)",
        "IP₃ e Ca²⁺ (più fosfatidiletanolammina)",
        "cGMP e calmodulina (più colesterolo)",
        "PIP₃ e Mg²⁺ (più sfingomielina)"],
    "b4p-05": [
        "La sintesi di glicogeno epatico indotta dall'insulina dopo il pasto",
        "La produzione di cGMP da NO nella muscolatura liscia dei vasi",
        "La degradazione del cAMP da parte della fosfodiesterasi nel fegato",
        "La traslocazione dei GLUT4 nel muscolo indotta dall'insulina tramite PKB"],
    "b4p-06": [
        "IP₃, che apre i canali del Ca²⁺ del RE",
        "DAG, che attiva la PKC in membrana",
        "PIP₂ (fosfato in posizione 4), che attiva la PKA",
        "PIP₃ (fosfato in posizione 5), che attiva la PKC"],
    "b4p-07": [
        "Tra il C1 del glicerolo e l'acido grasso",
        "Tra il fosfato e la testa polare (inositolo)",
        "Tra il C2 del glicerolo e l'acido grasso",
        "Tra il C3 dell'inositolo e il suo fosfato"],
    "b4p-08": ["fos, jun e Myc", "Smad2 e Smad4", "STAT3 e STAT5", "CREB, CBP, p300"],
    "bh4p-01": [
        "Gq-GTP → adenilato ciclasi → cAMP → PKA → fosforilazione dei canali del Ca²⁺ → Ca²⁺ e cAMP attivano la PKC",
        "Gq-GTP → PI3K → PIP₂ → PIP₃ (rilascio di Ca²⁺ dal RE) + DAG → Ca²⁺ e PIP₃ attivano la PKB",
        "Gq-GTP → PLCγ → PIP₃ → IP₄ (rilascio di Ca²⁺ dal mitocondrio) + DAG → Ca²⁺ e DAG attivano la PKA",
        "Gq-GTP → PLCβ → PIP₂ → DAG (rilascio di Ca²⁺ dal RE) + IP₃ → Ca²⁺ e IP₃ attivano la PKC in membrana"],
    "bh4p-02": [
        "Quella Ras-MAPK: niente PIP₃, niente SOS, quindi meno espressione genica e meno proliferazione cellulare",
        "Quella del cAMP: niente PIP₃, niente fosfodiesterasi, quindi la PKA resta attiva e prevale la glicogenolisi",
        "Quella JAK-STAT: niente PIP₃, niente STAT fosforilate, quindi meno trascrizione dei geni della lipogenesi",
        "Nessuna: il PIP₂ basta ad attivare la PKB, quindi traslocazione dei GLUT4 e sintesi di glicogeno restano"],
    "b4a-02": ["ACTH e TSH", "Insulina e glucagone", "LH e FSH", "GH e prolattina"],
    "b4a-03": [
        "Tre ormoni tiroidei diversi (T3, T4, rT3) che inibiscono rispettivamente ipotalamo, ipofisi e tiroide",
        "Tre tempi di risposta degli steroidi: secondi (membrana), minuti (citosol) e ore (nucleo)",
        "L'ormone periferico inibisce l'ipotalamo; l'ormone ipofisario inibisce la ghiandola periferica; l'ipotalamo inibisce l'ipofisi",
        "L'ormone ipofisario inibisce l'ipofisi; l'ormone ipotalamico inibisce la ghiandola periferica; l'ormone periferico la stimola"],
    "b4a-04": [
        "Basso, perché la tiroide non lo stimola",
        "Normale, perché il TSH non dipende da T3 e T4",
        "Assente, perché la tiroidite distrugge l'ipofisi",
        "Basso, perché manca il feedback positivo"],
    "b4a-05": [
        "Dipeptide di glicina e tirosina iodata, con il carbossile libero",
        "Proteina di 51 aa con due catene unite da ponti disolfuro",
        "Derivato del colesterolo con un anello aromatico, come gli estrogeni",
        "Tripeptide: glutammato, istidina, prolina con carbossile libero"],
    "b4a-06": [
        "Si misura direttamente la radioattività dell'ormone endogeno, che è naturalmente marcato con iodio",
        "Si conta il numero di recettori marcati con un ligando radioattivo e si ricava l'ormone circolante",
        "Si misura l'assorbanza del campione a 280 nm e si confronta con una curva di ormone purificato",
        "L'ormone marcato del campione compete con quello non marcato per il recettore; la radioattività legata è proporzionale all'ormone"],
    "b4a-07": [
        "La radioattività di un anticorpo secondario marcato con iodio, misurata con un contatore γ",
        "La fluorescenza naturale dell'ormone, eccitata con luce ultravioletta e misurata dallo strumento",
        "Il precipitato di proteine che si forma quando l'ormone lega l'anticorpo primario nel pozzetto",
        "Un anticorpo primario coniugato a un fluoroforo, che emette luce quando lega il recettore dell'ormone"],
    "b4a-08": [
        "Con un anticorpo anti-acetilcolina marcato con un enzima, che dà un prodotto colorato proporzionale al legame",
        "Misurando il pH del campione: l'acetilcolinesterasi libera acido acetico e il calo del pH dà la concentrazione",
        "Colina acetiltransferasi → acetil-CoA; citrato sintasi → citrato; aconitasi → prodotto colorato misurato",
        "Acetilcolinesterasi → acetato; acetato chinasi → acetil fosfato; fosfatasi usa il fosfato per un prodotto colorato"],
    "bh4a-01": [
        "Deficit di TRH ipotalamico che, senza stimolo sull'ipofisi, riduce il TSH e lascia la tiroide senza freno",
        "Tiroidite con distruzione della ghiandola, che libera ormoni e poi blocca la produzione ipofisaria di TSH",
        "Recettori ipofisari del TRH iperattivi, che aumentano gli ormoni tiroidei consumando tutto il TSH prodotto",
        "Mancanza di iodio nella dieta, che riduce il TSH e costringe la tiroide a produrre più T3 e T4 per compenso"],
    "b5i-01": [
        "Cellule α delle isole di Langerhans",
        "Cellule δ delle isole di Langerhans",
        "Cellule acinose del pancreas esocrino",
        "Cellule duttali del pancreas esocrino"],
    "b5i-02": ["29 (catena unica)", "86 (31 + 55)", "110 (24 + 86)", "51 (catena unica)"],
    "b5i-03": [
        "Proinsulina → (taglio del peptide segnale nel Golgi) preproinsulina → (taglio del peptide C) insulina",
        "Viene sintetizzata già matura sui ribosomi liberi e poi accumulata nei granuli di secrezione",
        "Preproinsulina → (taglio del peptide C nel RE) proinsulina → (taglio del peptide segnale) insulina",
        "Insulina → (glicosilazione nel Golgi) proinsulina → (aggiunta del peptide C nei granuli) forma attiva"],
    "b5i-04": [
        "Adrenalina, noradrenalina, simpatico, somatostatina, glucagone e digiuno prolungato",
        "Solo il glucosio, che entra con i GLUT2 e chiude i canali K⁺ ATP-dipendenti",
        "Glucagone, cortisolo, ormone della crescita e ipoglicemia, come risposta allo stress",
        "Glucosio, amminoacidi, adrenalina, simpatico, somatostatina e apertura dei canali K⁺"],
    "b5i-05": [
        "SOS (fattore di scambio di Ras)",
        "PKA (protein chinasi cAMP-dipendente)",
        "STAT5 (trasduttore del segnale)",
        "GRB2 (proteina adattatrice con SH2)"],
    "b5i-06": [
        "Sono identici: entrambi compaiono in pochi minuti alle stesse concentrazioni, ma i tardivi durano di più nel tempo",
        "Immediati (ore, 10⁻⁸ M): espressione genica. Tardivi (minuti, 10⁻⁹–10⁻¹⁰ M): GLUT4 ed enzimi del glicogeno",
        "Immediati (minuti, 10⁻⁸ M): richiedono più insulina. Tardivi (giorni): passano per il cAMP e la PKA nel nucleo",
        "Immediati (secondi, 10⁻⁶ M): apertura dei canali K⁺. Tardivi (minuti, 10⁻⁹ M): GLUT4 ed enzimi del glicogeno"],
    "b5i-07": [
        "Fosforila e attiva direttamente la glicogeno sintasi, che passa nella forma a più attiva",
        "Attiva la glicogeno fosforilasi, che in presenza di glucosio lavora al contrario e sintetizza",
        "Aumenta il cAMP, che attiva la PKA e quindi la glicogeno sintasi fosforilata",
        "Attiva la GSK3, che defosforila la glicogeno sintasi e la mantiene nella forma attiva"],
    "b5i-08": [
        "Blocca il recettore del glucagone legandosi al suo posto",
        "Fosforila la PKA e la stacca dalle subunità regolatrici",
        "Aumenta l'adenilato ciclasi, che consuma l'ATP disponibile",
        "Inibisce la fosfodiesterasi, così il cAMP viene sequestrato"],
    "b5i-09": [
        "Lega il glucosio 6-fosfato come attivatore allosterico e fosforila tutte le serine della sintasi contemporaneamente",
        "Riconosce una sequenza ricca di prolina sul substrato tramite un dominio SH3, come le chinasi della via di Ras",
        "Lega l'UDP-glucosio legato alla sintasi e fosforila solo le molecole di enzima che stanno già allungando il glicogeno",
        "Lega una fosfotirosina di innesco introdotta dal recettore dell'insulina e poi fosforila le tirosine successive"],
    "b5i-10": ["IRS1", "AKAP", "Calmodulina", "Glicogenina"],
    "b5i-11": [
        "Il peptide C abbassa la glicemia da solo e serve per dosare correttamente l'insulina da somministrare",
        "Il peptide C è la forma attiva dell'insulina: misura quanta insulina farmaco agisce davvero sui tessuti",
        "Il peptide C misura la resistenza all'insulina, perché sale solo quando i recettori sono internalizzati",
        "L'insulina farmaco contiene peptide C: il dosaggio misura quanta insulina esogena è in circolo"],
    "bh5i-01": [
        "La PKA fosforila entrambi gli enzimi: la sintasi fosforilata è attiva e la fosforilasi fosforilata è inattiva",
        "Il Ca²⁺ attiva la fosforilasi chinasi, che fosforila la sintasi (attivandola) e la fosforilasi (inattivandola)",
        "La GSK3 attivata dalla PKB fosforila la sintasi (attivandola), mentre la PP1 defosforila la fosforilasi",
        "Il cAMP sale e attiva la PP1, che fosforila sia la sintasi (attivandola) sia la fosforilasi (inattivandola)"],
})
FIX.update({
    "bh5i-02": [
        "Deficit di secrezione delle cellule β, per esempio per distruzione autoimmune delle isole",
        "Eccesso di somatostatina, che blocca il recettore dell'insulina sui tessuti periferici",
        "Insulina esogena in eccesso, somministrata per errore in dose troppo alta",
        "Mutazione del peptide C, che non viene tagliato e resta legato all'insulina circolante"],
    "bh5i-03": [
        "IRS1 → PI3K → PIP₃ → PKB → GSK3 → MAP chinasi → fattori di trascrizione",
        "Recettore → Gs → adenilato ciclasi → cAMP → PKA → CREB → geni bersaglio",
        "Recettore → JAK → STAT fosforilata → dimero di STAT → geni bersaglio",
        "IRS1 → PLCγ → IP₃ → Ca²⁺ → calmodulina → CaM chinasi → fattori di trascrizione"],
    "bh5i-04": [
        "Attivano direttamente il recettore dell'insulina sulla cellula β, che si autoregola aumentando la secrezione",
        "Inibiscono la secrezione di glucagone dalle cellule α, che normalmente frena le cellule β vicine",
        "Aprono i canali K⁺-ATP della cellula β, iperpolarizzando la membrana e facendo uscire Ca²⁺",
        "Aumentano i GLUT2 della cellula β, così entra più glucosio e si produce più ATP"],
    "d1c-03": [
        "Vengono ceduti direttamente all'O₂ nel citosol, che si riduce ad acqua senza bisogno di coenzimi",
        "Restano sul carbonio come carica negativa, finché il carbonio non viene eliminato come CO₂",
        "Vengono usati per sintetizzare ATP nella glicolisi, legandosi direttamente all'ADP nel citosol",
        "Passano a NADP⁺ o FMN, poi alla catena respiratoria e infine alla CO₂, che diventa bicarbonato"],
    "d1c-04": [
        "La conformazione cambia solo rompendo legami; la configurazione cambia per rotazione attorno ai legami singoli",
        "Sono sinonimi: entrambe indicano la disposizione spaziale degli atomi e cambiano solo rompendo legami",
        "La configurazione riguarda solo i doppi legami; la conformazione riguarda solo i centri chirali della molecola",
        "Entrambe cambiano per rotazione attorno ai legami singoli; la configurazione solo a temperature elevate"],
    "d1c-06": [
        "Enantiomeri (immagini speculari)",
        "Isomeri di struttura (di posizione)",
        "Conformeri (rotameri)",
        "Diastereoisomeri ottici (epimeri)"],
    "d1c-07": [
        "Quella con più gruppi alcolici liberi in posizione 4",
        "Quella legata covalentemente alle proteine di membrana",
        "Quella che contiene il legame glicosidico α1→6",
        "Quella con il carbonio anomerico impegnato nel legame"],
    "d1a-03": [
        "Un aggregato di molecole anfipatiche con le code apolari rivolte verso l'acqua",
        "Un legame a idrogeno condiviso tra tre atomi di ossigeno vicini",
        "Una micella con il core polare e la superficie apolare esposta",
        "La sfera di idratazione disordinata attorno a uno ione carico"],
    "d1a-04": [
        "Perché si formano molti legami covalenti tra i fosfolipidi vicini, che liberano energia",
        "Perché le teste polari si respingono e spingono le code apolari a unirsi al centro",
        "Perché l'acqua si lega alle code apolari e le ordina, diminuendo l'entalpia del sistema",
        "Perché l'aggregazione delle teste polari libera i controioni, diminuendo l'entropia dell'acqua"],
    "d1h-02": [
        "La diminuzione di entropia del complesso, che diventa più ordinato e quindi più stabile",
        "La formazione di legami covalenti transitori tra il sito attivo e il substrato legato",
        "L'aumento di entalpia dovuto alla rottura dei legami a H tra l'acqua e le due superfici",
        "La riduzione del numero di molecole d'acqua libere, che diventano più ordinate"],
    "d1m-01": [
        "Come amido nel fegato e nel rene",
        "Come trigliceridi nel muscolo scheletrico",
        "Come cellulosa nel tessuto adiposo",
        "Come glicogeno nel tessuto adiposo"],
    "d1m-02": [
        "Fonte principale di energia per tutti i tessuti",
        "Riserva energetica a lungo termine, accumulata nel muscolo",
        "Componente principale delle membrane, insieme ai fosfolipidi",
        "Precursori del glucosio; nella sintesi proteica sono secondari"],
    "d2s-03": [
        "Sì, per definizione: la lettera L indica proprio la rotazione a sinistra della luce",
        "Sì, tutti tranne la glicina, che non ha centri chirali e non ruota la luce polarizzata",
        "No, sono tutti destrogiri: la serie L corrisponde sempre alla rotazione verso destra",
        "Sì, perché hanno tutti la stessa configurazione della L-gliceraldeide, che è levogira"],
    "d2s-05": ["Leucina e valina", "Serina e cisteina", "Prolina e istidina", "Isoleucina e leucina"],
    "d2s-06": [
        "Diastereoisomeri con la stessa attività sedativa",
        "Farmaco attivo solo come miscela racemica dei due isomeri",
        "Isomeri geometrici del legame peptidico con effetti diversi",
        "Enantiomeri con effetti diversi: R teratogeno, S sedativo"],
    "d2h-01": [
        "È L-alanina pura, che non è otticamente attiva perché ha la configurazione L",
        "L'alanina non ha centri chirali, come la glicina, e non ruota mai la luce",
        "È D-alanina pura, che a differenza della L non ruota la luce polarizzata",
        "Il polarimetro misura solo i D-amminoacidi e non rileva la L-alanina"],
    "d2c-03": [
        "Lo zolfo è sempre ossidato a solfossido, che non forma legami a idrogeno con l'acqua",
        "Forma ponti disolfuro con altre metionine, che nascondono lo zolfo all'interno della proteina",
        "Ha un anello aromatico che contiene lo zolfo e rende apolare tutta la catena laterale",
        "Lo zolfo è all'estremità della catena (tiolo libero), ma ha un pKa troppo alto per ionizzarsi"],
    "d2c-05": [
        "La forma ridotta della cisteina, con due gruppi −SH liberi",
        "Un precursore della metionina, che dona il gruppo metilico",
        "Un derivato della serina in cui l'−OH è sostituito da −SH",
        "Il dimero di due metionine unite da un legame tioetere"],
    "d2a-01": [
        "Molecola neutra senza cariche",
        "Anione con carica netta −1",
        "Catione con carica netta +1",
        "Ione dipolare con carica netta −1"],
    "d2a-02": [
        "Il pH a cui la carica netta della molecola è zero",
        "Il pH a cui il gruppo è tutto protonato",
        "Il pH fisiologico a cui lavora il gruppo nella cellula",
        "Il pH a cui il gruppo è dissociato al 100%"],
    "d2a-03": [
        "La glicina è più piccola dell'acido acetico e il suo carbossile è più esposto all'acqua",
        "La glicina ha due carbossili che si dissociano insieme, raddoppiando l'acidità",
        "Il gruppo amminico vicino cede il suo protone al carbossile e lo rende più acido",
        "Il gruppo amminico vicino dona elettroni al carbossile e stabilizza la forma protonata"],
    "d2a-04": [
        "Media tra il pK dell'α-amminico e quello del carbossile laterale",
        "Media di tutti e tre i pK dei gruppi ionizzabili della molecola",
        "È uguale al pK dell'α-carbossile, il gruppo più acido della molecola",
        "Media tra il pK dell'α-carbossile e quello del gruppo α-amminico"],
    "d2a-06": [
        "Ha un pKa vicino a 12: a pH fisiologico è sempre protonata e stabilizza le cariche negative",
        "È l'unico amminoacido aromatico, quindi lega i substrati con interazioni di impilamento",
        "Forma ponti disolfuro con le cisteine vicine, che tengono fermo il sito catalitico",
        "Ha un pKa vicino a 4: a pH fisiologico è sempre deprotonata e attacca i substrati"],
    "d2h-03": [
        "Quando inizia a dissociarsi il carbossile, perché i primi OH⁻ aggiunti non trovano protoni da neutralizzare",
        "Quando il gruppo amminico è dissociato al 50%, cioè al pH uguale al suo pKa di circa 9,6",
        "Quando la glicina raggiunge carica netta −1 e tutti i suoi gruppi sono già deprotonati",
        "Mai: la curva della glicina sale in modo regolare perché i due gruppi tamponano insieme"],
    "d2n-01": [
        "Quelli più abbondanti nelle proteine dell'organismo",
        "Quelli necessari solo nei bambini durante la crescita",
        "Quelli con catena laterale carica a pH fisiologico",
        "Quelli che l'organismo sintetizza solo nel fegato"],
    "d2n-02": ["Serina", "Treonina", "Glicina", "Tirosina"],
    "d2n-03": [
        "Per decarbossilazione, con perdita del carbossile come CO₂",
        "Per idrossilazione, con l'aggiunta di un −OH al carbonio β",
        "Per carbossilazione con biotina, come nella piruvato carbossilasi",
        "Per riduzione con NADH, prendendo l'azoto dall'ammoniaca libera"],
    "d2n-04": [
        "Forma ponti disolfuro che stabilizzano la protrombina nel plasma",
        "Stabilizza la tripla elica della protrombina come l'idrossiprolina",
        "Assorbe a 280 nm e permette di dosare la protrombina nel plasma",
        "Con due cariche positive lega bene i fosfolipidi delle piastrine"],
    "d2p-01": [
        "Per idrolisi tra α-carbossile di un amminoacido e α-ammino del successivo, con consumo di H₂O",
        "Per condensazione tra le catene laterali di due amminoacidi vicini, con uscita di H₂O",
        "Per condensazione tra i gruppi α-amminici di due amminoacidi, con uscita di NH₃",
        "Per condensazione tra α-carbossile di un amminoacido e catena laterale del successivo"],
    "d2p-02": [
        "Perché è un legame ionico tra il carbossile e il gruppo amminico",
        "Per l'ingombro delle catene laterali che bloccano la rotazione",
        "Perché è stabilizzato da un legame a idrogeno con il residuo vicino",
        "Per risonanza ha un parziale carattere di triplo legame"],
    "d2p-03": [
        "Il cis non può dare risonanza, quindi il legame sarebbe libero di ruotare e instabile",
        "Il trans forma più legami a idrogeno con l'acqua e con le catene laterali vicine",
        "È il ribosoma a imporre il trans, che poi non può più cambiare dopo il ripiegamento",
        "In trans i carboni α sono dallo stesso lato e le catene laterali si stabilizzano a vicenda"],
    "d2p-04": [
        "N-terminale della glicina, C-terminale del glutammato",
        "Entrambe sulla cisteina, che chiude un anello disolfuro",
        "Non ha estremità libere, perché è un tripeptide ciclico",
        "N-terminale della cisteina, C-terminale della glicina"],
    "d2p-05": [
        "Tutti e quattro i carbossili e i quattro gruppi amminici",
        "Solo i tre legami peptidici, che sono parzialmente carichi",
        "I gruppi amminici di ogni residuo, che restano protonati",
        "Solo l'N-terminale (~2,2) e il C-terminale (~9,6)"],
    "d2p-06": ["Coenzima libero", "Dominio non proteico", "Apoproteina", "Oloenzima"],
    "d3p-01": [
        "Catena A di 30 aa e catena B di 21 aa",
        "Una sola catena di 51 aa ripiegata su sé stessa",
        "Tre catene di 17 aa unite da ponti disolfuro",
        "Catena A di 21 aa e catena B di 31 aa"],
    "d3p-03": [
        "Tre intercatena (A6–B7, A11–B19, A20–B30)",
        "Uno intercatena (A7–B7) e due intracatena (A6–A11, B19–B20)",
        "Due intracatena (A6–A11, B7–B19) e nessuno intercatena",
        "Due intercatena (A6–B7, A11–B19) e uno intracatena (A7–A20)"],
    "d3p-04": [
        "Fuori dalla cellula c'è più cisteina libera disponibile",
        "Servono enzimi che esistono solo nello spazio extracellulare",
        "Nel citosol manca l'ossigeno che serve a formare il ponte",
        "L'ambiente extracellulare è più riducente del citosol"],
    "d3p-06": ["I ponti disolfuro", "I legami ionici (ponti salini)", "I legami peptidici", "Le forze di van der Waals"],
    "d3h-01": [
        "Cambia il codice genetico della cellula: tutte le proteine successive vengono tradotte con un amminoacido sbagliato",
        "Accorcia sempre la proteina, perché la sostituzione introduce un codone di stop e la catena resta tronca",
        "Impedisce la trascrizione del gene, perché l'mRNA mutato viene degradato prima di arrivare al ribosoma",
        "Rende la proteina insolubile in ogni caso, perché qualunque sostituzione espone residui idrofobici all'acqua"],
    "d3s-01": ["3,0", "4,2", "2,0", "5,4"],
    "d3s-02": [
        "Legami a idrogeno tra le catene laterali",
        "Ponti disolfuro tra cisteine vicine nella sequenza",
        "Interazioni ioniche tra residui carichi",
        "Legami a idrogeno tra le catene laterali e l'acqua"],
})
FIX.update({
    "d3s-04": [
        "Che tutte le combinazioni di φ e ψ sono possibili e compaiono con frequenza simile nelle proteine",
        "Che gli angoli φ e ψ dipendono solo dalla sequenza e non dalla struttura secondaria della catena",
        "Che il legame peptidico ruota liberamente e gli angoli φ e ψ cambiano in continuazione",
        "Che gli angoli φ e ψ osservati occupano quasi tutto il grafico: solo ¼ della superficie è vuoto"],
    "d3s-05": [
        "Ponte disolfuro tra le cisteine dei residui i e i+3, sempre presenti",
        "Legame ionico tra le catene laterali dei residui i+1 e i+2",
        "Legame a H tra le catene laterali dei residui i+1 e i+2",
        "Legame a H tra l'N–H del residuo i e il C=O del residuo i+4"],
    "d3s-06": [
        "φ ≈ −120°, ψ ≈ +130°",
        "φ ≈ +60°, ψ ≈ +45/+50°",
        "φ ≈ −60°, ψ ≈ +140°",
        "φ ≈ +120°, ψ ≈ −130°"],
    "d3h-02": [
        "Un'α-elica lunga e stabile, con molti legami a H",
        "Un foglietto β parallelo ideale e molto regolare",
        "Il nucleo idrofobico compatto della proteina",
        "Una superelica coiled coil come nella cheratina"],
    "d3c-01": [
        "Ala-Gly-Ser (X spesso Pro, Y spesso Lys)",
        "Pro-Pro-Gly-Cys (con ponti disolfuro)",
        "Lys-X-Y (X spesso Gly, Y spesso 5-Hyl)",
        "Gly-X-Y (X spesso Cys, Y spesso Trp)"],
    "d3c-03": [
        "Tre α-eliche destrorse avvolte tra loro in una superelica sinistrorsa",
        "Due catene β antiparallele avvolte tra loro, stabilizzate da ponti disolfuro",
        "Tre catene destrorse avvolte tra loro in una superelica anch'essa destrorsa",
        "Tre catene sinistrorse avvolte tra loro in una superelica sinistrorsa"],
    "d3c-04": [
        "È il residuo che forma i legami crociati covalenti tra le molecole vicine",
        "È il residuo che viene idrossilato dalla prolil-idrossilasi nel RE",
        "È il residuo su cui si legano glucosio e galattosio nel Golgi",
        "È l'unico residuo abbastanza grande da riempire il centro della tripla elica"],
    "d3c-05": [
        "Viene ridotto a glutammato con il gruppo amminico della prolina",
        "Si lega covalentemente alla prolina idrossilata come gruppo prostetico",
        "Non partecipa alla reazione: è solo un effettore allosterico",
        "Viene carbossilato e ridotto a citrato consumando CO₂"],
    "d3c-06": [
        "Senza vitamina K i fattori della coagulazione non vengono carbossilati e il sangue non coagula",
        "Senza vitamina C si accumulano troppi legami crociati e il collagene diventa fragile",
        "Senza vitamina C il collagene non viene secreto e resta accumulato nei fibroblasti",
        "Senza vitamina C il collagene non viene glicosilato e la tripla elica si srotola"],
    "d3c-07": [
        "Servono alla glicosilazione delle idrossilisine, che avviene fuori dalla cellula",
        "La peptidasi che li taglia si trova solo nel Golgi e nelle vescicole di secrezione",
        "Proteggono il collagene dalla collagenasi finché non è inserito nelle fibrille",
        "Altrimenti la tripla elica non si formerebbe e le catene resterebbero separate"],
    "d3c-09": ["Idrossiprolina", "Prolina", "Glicina", "Asparagina"],
    "d3c-10": [
        "Struttura a tripla elica come quella del collagene",
        "Foglietti β ricchi di glicina e alanina impilati",
        "Alta glicosilazione delle lisine sulla superficie",
        "Alto contenuto di prolina con legami crociati di allisina"],
    "d3h-03": [
        "Scorbuto da carenza di vitamina C: fragilità ossea il primo, lassità dei legamenti il secondo",
        "Latirismo da β-amminopropionitrile: fratture il primo, iperestensibilità della pelle il secondo",
        "Deficit di elastina: fragilità ossea il primo, sindrome di Marfan con lassità il secondo",
        "Carenza di vitamina D in entrambi: rachitismo il primo, ipotonia muscolare il secondo"],
    "d3h-04": [
        "La perdita progressiva delle glicine della tripla elica",
        "La riduzione dell'idrossiprolina per minore attività della prolil-idrossilasi",
        "La sostituzione progressiva del collagene con fibre di elastina",
        "L'aumento della glicosilazione delle idrossilisine del collagene"],
    "d3h-05": [
        "L'enzima idrossila un'altra prolina vicina e il ferro resta Fe²⁺: l'ascorbato serve solo come antiossidante",
        "Il ferro passa a Fe⁴⁺ e l'enzima si degrada: l'ascorbato serve a sostituire l'enzima perso",
        "L'ascorbato sostituisce l'α-chetoglutarato, che senza prolina non può essere decarbossilato",
        "Non succede nulla: senza prolina l'enzima resta fermo e la vitamina C serve ad altre reazioni"],
    "d3t-02": [
        "Sono sinonimi: entrambi indicano un'unità globulare compatta di una catena polipeptidica",
        "Motivo: unità globulare compatta e funzionale; dominio: combinazione di pochi elementi di struttura secondaria",
        "Il dominio è formato da una sola α-elica; il motivo è un insieme di domini con la stessa funzione",
        "Motivo: sequenza di pochi amminoacidi conservata; dominio: struttura quaternaria di più subunità"],
    "d3f-01": ["Mioglobina", "Lisozima", "Insulina", "Citocromo c"],
    "d3f-03": [
        "La ribonucleasi si ripiega solo con l'aiuto dei chaperoni: senza di loro la sequenza non basta a dare la struttura",
        "I ponti disolfuro si formano a caso: la ribonucleasi recupera solo l'1% dell'attività, come atteso statisticamente",
        "La ribonucleasi resta inattiva: una volta denaturata, una proteina non può più riacquistare la sua struttura",
        "La ribonucleasi riacquista l'attività solo se si aggiunge ATP, che fornisce l'energia per il ripiegamento"],
    "d3f-04": [
        "Le proteine non si ripiegano mai da sole: serve sempre l'intervento delle chaperonine",
        "Il folding non è spontaneo, perché la catena ripiegata ha meno entropia di quella distesa",
        "Il folding avviene solo nel ribosoma, mentre la catena viene ancora sintetizzata",
        "Esplorando a caso tutte le conformazioni il folding avverrebbe in pochi nanosecondi, troppo in fretta"],
    "d3f-05": [
        "DnaK (Hsp70) e DnaJ (Hsp40)",
        "Hsp90 (2 subunità) e Hsp70 (1 subunità)",
        "PDI (2 subunità) e GrpE (2 subunità)",
        "GroES (14 subunità) e GroEL (7 subunità)"],
    "d3f-06": [
        "Si formano molti ponti disolfuro, ciascuno dei quali libera molta energia e compensa l'ordine",
        "I residui polari liberano energia legandosi tra loro all'interno della proteina ripiegata",
        "Il folding consuma ATP, che fornisce l'energia libera necessaria a ordinare la catena",
        "Il collasso idrofobico ordina l'acqua attorno alle catene apolari, diminuendone l'entalpia"],
    "d3f-08": [
        "DnaJ scambia ADP con ATP (DnaK si chiude sulla proteina); GrpE stimola l'idrolisi dell'ATP (DnaK la rilascia)",
        "Sono le due subunità di GroEL: DnaJ forma l'anello inferiore della camera, GrpE quello superiore",
        "Degradano le proteine misfoldate: DnaJ le marca con l'ubiquitina, GrpE le porta al proteasoma",
        "DnaJ lega la proteina e la porta a GroEL; GrpE fa da coperchio alla camera al posto di GroES"],
    "d3f-10": [
        "Le ossida ad acido cisteico (−SO₃⁻)",
        "Riduce i ponti disolfuro tra cisteine",
        "Le trasforma in serine per idrolisi",
        "Forma nuovi ponti disolfuro tra cisteine"],
    "d3f-11": [
        "Nel citosol, sui ribosomi liberi",
        "Nella matrice dei mitocondri",
        "Nel nucleo, sulle proteine istoniche",
        "Nei lisosomi, prima della degradazione"],
    "d3h-07": [
        "Aggiungere altra urea e più β-mercaptoetanolo, che rompe definitivamente tutti i ponti disolfuro e libera la catena",
        "Aggiungere chaperoni GroEL e GroES con ATP, che ripiegano la proteina anche con i ponti disolfuro sbagliati",
        "Riscaldare a 90 °C senza riducente, così i ponti disolfuro sbagliati si sciolgono e quelli giusti si riformano",
        "Togliere l'urea e aggiungere iodoacetato, che blocca le cisteine libere e stabilizza i ponti disolfuro già formati"],
    "d3h-08": [
        "Le proteine aggregate sono troppo piccole per essere riconosciute: gli oligomeri sfuggono a chaperoni e proteasoma",
        "Il proteasoma degrada solo le fibrille mature: gli oligomeri iniziali restano e continuano a crescere senza controllo",
        "Le fibrille sono fatte di α-eliche molto stabili, che nessun sistema cellulare riesce a srotolare e degradare",
        "Le proteine coinvolte non hanno una sequenza nota: non è possibile capire quale conformazione prendano"],
    "d3h-09": [
        "Secrezione all'esterno della cellula, dove viene ripiegata dalle proteasi extracellulari",
        "Ritorno al ribosoma per essere riletta e sintetizzata di nuovo con la sequenza corretta",
        "Trasferimento nel reticolo endoplasmatico, dove resta in modo permanente legata alla PDI",
        "Accumulo nei mitocondri, dove viene ripiegata dalle chaperonine mitocondriali Hsp60"],
    "d3q-01": [
        "Il ripiegamento tridimensionale di una singola catena polipeptidica nello spazio",
        "La sequenza degli amminoacidi di tutte le catene di un complesso proteico",
        "L'insieme di α-eliche e foglietti β che formano i domini di una sola catena",
        "L'associazione di più domini della stessa catena polipeptidica in un'unità compatta"],
    "d3q-03": [
        "Solo una maggiore solubilità in acqua rispetto ai monomeri isolati",
        "Maggiore velocità di traduzione di un gene lungo, con meno errori",
        "Resistenza alle proteasi e alla denaturazione, ma nient'altro",
        "Meno geni da trascrivere, ma minore stabilità e nessuna cooperatività"],
    "d3q-04": [
        "La capacità di legare più substrati diversi contemporaneamente sullo stesso sito attivo",
        "La formazione di ponti disolfuro tra subunità diverse, che le rendono un'unica catena",
        "La polimerizzazione delle subunità in fibre lunghe, come accade per la tubulina",
        "Il legame del substrato a una subunità, che blocca sempre le altre subunità del complesso"],
    "d3q-05": [
        "I ponti disolfuro tra le subunità impediscono qualsiasi tipo di simmetria",
        "Le subunità di una proteina multimerica sono sempre diverse tra loro",
        "La simmetria ciclica è vietata per tutte le proteine fatte di L-amminoacidi",
        "L'immagine speculare richiederebbe legami peptidici in conformazione cis"],
    "d3q-06": [
        "Le tubuline sono unite da ponti disolfuro che si rompono e si riformano molto rapidamente",
        "La tubulina è una proteina fibrosa a tripla elica, che si avvolge e si srotola in continuazione",
        "Ogni protomero è un monomero di tubulina α o β, legato covalentemente a quello successivo",
        "I protomeri di tubulina (dimeri αβ) sono uniti da legami covalenti che si idrolizzano facilmente"],
    "d3q-08": [
        "14, è un tetradecamero a simmetria diedrica",
        "4, è un tetramero a simmetria diedrica",
        "2, è un dimero isologo a simmetria ciclica",
        "7, è un eptamero a simmetria diedrica"],
    "dh3q-01": ["Ciclica C4, tipica dei tetrameri", "Speculare (riflessione)", "Elicoidale, come i polimeri", "Nessuna simmetria regolare"],
    "dh3q-02": [
        "Omo-tetramero a simmetria ciclica, con subunità identiche unite da ponti disolfuro intramolecolari",
        "Proteina monomerica con quattro domini, uniti da ponti disolfuro all'interno della stessa catena",
        "Dimero isologo di due catene uguali, con ponti disolfuro che legano i domini di ciascuna catena",
        "Polimero di protomeri come la tubulina, con legami non covalenti che ne permettono la dissociazione"],
    "d3x-01": [
        "L'insieme dei geni di una cellula, uguale in tutti i tessuti dell'organismo",
        "L'insieme delle proteine di tutti i tessuti, sempre uguale nel corso della vita",
        "La sequenza completa degli amminoacidi di una proteina e le sue modificazioni",
        "L'insieme degli mRNA trascritti da una cellula in un dato momento"],
    "d3x-02": [
        "Solo la sequenza amminoacidica, determinata prima della purificazione",
        "Solo il colore e l'assorbanza nel visibile delle diverse proteine",
        "Il numero di ponti disolfuro e la temperatura di denaturazione",
        "Il punto di fusione, la viscosità e l'indice di rifrazione della proteina"],
    "d3x-03": [
        "Purezza e resa crescono insieme a ogni passaggio",
        "La resa è sempre il 100% se si lavora a 4 °C",
        "Non c'è relazione: dipendono da fattori diversi",
        "Più alta è la purezza richiesta, più alta è la resa"],
    "d3x-04": [
        "I ribosomi e i polisomi, che vanno sul fondo della provetta",
        "Le proteine solubili del citosol, che precipitano sul fondo",
        "I microsomi (frammenti di RE), che formano il pellet",
        "I mitocondri e i lisosomi, mentre i nuclei restano sospesi"],
    "d3x-05": [
        "Le impurità assorbono i raggi X e coprono il segnale della proteina",
        "La proteina va prima denaturata e le impurità lo impediscono",
        "Serve una grande resa, che si ottiene solo con proteine pure",
        "Le impurità cambiano la sequenza della proteina nel cristallo"],
    "d3x-06": [
        "Fino a ~3000 rpm, a temperatura ambiente, senza vuoto né refrigerazione",
        "Usa un campo elettrico al posto della forza centrifuga per separare le molecole",
        "Funziona solo con proteine già precipitate con solfato d'ammonio",
        "Fino a ~8.000 rpm e 6.000 g, aperta all'aria, usata per cellule e batteri"],
    "d3x-07": [
        "Microsomi → mitocondri → nuclei e cellule intere → citosol (sopranatante finale)",
        "Citosol → nuclei e cellule intere → mitocondri → microsomi (sopranatante finale)",
        "Tutte le frazioni sedimentano insieme a 500 g: si separano poi per densità",
        "Mitocondri → nuclei e cellule intere → microsomi → citosol (sopranatante finale)"],
    "dh3x-01": [
        "Cristallizzare subito l'omogenato, poi identificare l'enzima nella struttura ottenuta ai raggi X",
        "Ultracentrifugare l'omogenato a 600.000 g e usare il sopranatante, dove restano gli enzimi della matrice",
        "Precipitare tutte le proteine con urea 8 M, poi separarle per carica e dimensione con le cromatografie",
        "Ridurre i ponti disolfuro con β-mercaptoetanolo, poi purificare per affinità dall'omogenato totale"],
    "h1e-02": [
        "Lavorano entrambi a circa metà della propria Vmax",
        "Il secondo è più veloce, perché ha la KM più alta",
        "Entrambi lavorano vicino alla propria Vmax",
        "Il primo è a ½ Vmax, il secondo a circa il 50% della Vmax"],
    "h2f-02": [
        "Il G6P la attiva allostericamente come effettore positivo",
        "L'insulina la defosforila tramite la proteina fosfatasi 1",
        "Il fruttosio 6-fosfato la porta dal nucleo al citosol",
        "L'ATP ne riduce la KM come effettore omotropico positivo"],
    "h2f-03": [
        "Perché la glucochinasi non produce G6P ma fruttosio 6-fosfato, che non inibisce l'enzima",
        "Nel fegato il G6P esce subito dalla cellula con i GLUT2 e non si accumula",
        "La glucochinasi è già inibita dal glucosio, quindi un secondo inibitore non serve",
        "L'esochinasi lavora solo nel mitocondrio, dove il G6P non arriva mai a concentrazioni alte"],
    "h2g-02": [
        "La glicolisi si blocca alla GAP deidrogenasi e si accumula la GAP",
        "Si produce più ATP del normale, perché l'arseniato è più energetico",
        "Non si forma NADH, ma si forma comunque l'ATP della fosfoglicerato chinasi",
        "Si blocca la piruvato chinasi e si accumula il fosfoenolpiruvato"],
    "h2m-02": [
        "Il cuore produce più lattato del muscolo scheletrico",
        "L'isoenzima H₄ è inattivo e il cuore non usa il lattato",
        "L'isoenzima M₄ non riconosce il piruvato come substrato",
        "Il cuore converte il piruvato in etanolo invece che in lattato"],
})
FIX.update({
    "h2m-03": [
        "La piruvato deidrogenasi epatica, poi la glicolisi",
        "La LDH cardiaca (soprattutto H₄), poi la glicogenolisi",
        "La piruvato carbossilasi, poi il ciclo di Krebs",
        "La lattato ossidasi, poi la via dei pentoso fosfati"],
    "h2n-03": [
        "Il NADH stesso, tramite un trasportatore specifico della membrana interna",
        "Il NAD⁺, scambiato con il NADH da un antiporto della membrana interna",
        "Il FADH₂ prodotto nel citosol dalla glicerolo 3-P deidrogenasi",
        "Il piruvato, che porta con sé gli elettroni del NADH nella matrice"],
    "h2n-04": [
        "L'ossalacetato è tossico nella matrice e va subito eliminato nel citosol",
        "L'aspartato serve a sintetizzare l'urea nella matrice e nel citosol",
        "È l'aspartato, e non il malato, a trasportare gli elettroni nel citosol",
        "L'ossalacetato si decarbossila a piruvato prima di poter uscire dalla matrice"],
    "h2n-06": [
        "La glicerolo 3-P deidrogenasi citosolica, libera nel citosol vicino alla membrana esterna",
        "La malato deidrogenasi mitocondriale, nella matrice accanto al complesso I",
        "La succinato deidrogenasi, sulla faccia della membrana interna rivolta verso la matrice",
        "La GAP deidrogenasi, nel citosol accanto alla membrana mitocondriale esterna"],
    "h2r-03": [
        "Inibisce solo quando è legato al magnesio, mentre come substrato è libero",
        "È un inibitore competitivo del fruttosio 6-fosfato e ne occupa il sito di legame catalitico",
        "Inibisce solo l'isoforma epatica dell'enzima, mentre è substrato di quella muscolare",
        "Il sito allosterico ha alta affinità e lega l'ATP prima del sito catalitico"],
    "h2p-08": ["Glucosio 6-fosfato", "Fruttosio 1-fosfato", "UDP-galattosio", "Galattosio 6-fosfato"],
    "h2d-07": [
        "Deficit di lattato deidrogenasi (subunità M)",
        "Deficit di glucosio 6-fosfatasi epatica (von Gierke)",
        "Deficit di GLUT4 nel muscolo e nel tessuto adiposo",
        "Deficit di glicogeno fosforilasi muscolare (McArdle)"],
    "h2d-08": [
        "La PDH si attiva e aumenta la produzione di CO₂",
        "Aumenta la β-ossidazione degli acidi grassi nel mitocondrio",
        "La glicolisi viene inibita e cala il consumo di glucosio",
        "Aumenta la fosforilazione ossidativa e il consumo di O₂"],
    "h3s-01": [
        "Un gradiente di ATP e uno di ADP tra i due lati",
        "Un gradiente di Na⁺ e uno di K⁺ attraverso la membrana",
        "Solo un gradiente di pH tra i due lati della membrana",
        "Un gradiente di O₂ e uno di CO₂ tra matrice e citosol"],
    "h3m-03": [
        "Enzimi del ciclo di Krebs e della piruvato deidrogenasi",
        "Enzimi della β-ossidazione degli acidi grassi",
        "Proteine della membrana esterna (porine, TOM)",
        "DNA polimerasi e fattori di trascrizione mitocondriali"],
    "h3m-08": [
        "Pelle, capelli e mucose",
        "Eritrociti e piastrine",
        "Tessuto adiposo bianco e osso",
        "Tutti i tessuti allo stesso modo"],
    "h4s-03": [
        "Solo 1 UTP, perché il glucosio 1-fosfato si forma dal glucosio libero senza consumo di ATP",
        "1 ATP (esochinasi/glucochinasi) e 1 GTP (che dà GDP + Pi nella glicogeno sintasi)",
        "2 ATP (esochinasi e fosfoglucomutasi) e nessun UTP, perché l'UDP-glucosio non è richiesto",
        "Nessuno: la glicogeno sintasi usa l'energia del legame glicosidico già presente nel glicogeno"],
    "h4o-02": [
        "Perché il glucagone si moltiplica nel sangue dopo il primo legame",
        "Perché ogni recettore lega molte molecole di ormone insieme",
        "Perché il cAMP è un enzima che degrada direttamente il glicogeno",
        "Perché il glicogeno degradato attiva di nuovo il proprio recettore"],
    "h4o-08": [
        "Esce subito dal fegato tramite i GLUT2 e torna nel sangue periferico",
        "Diventa tutto glicogeno epatico, perché la glicolisi è inibita dall'insulina",
        "Viene ossidato a lattato e ceduto al sangue per il ciclo di Cori",
        "Viene convertito in corpi chetonici e ceduto al cervello e al muscolo"],
    "h4a-08": [
        "Gli acidi grassi non possono produrre ATP nel muscolo scheletrico",
        "Il lattato si azzera e la glicolisi muscolare si ferma del tutto",
        "Manca l'insulina e il glucosio del sangue non entra più nel muscolo",
        "Si blocca la catena respiratoria per accumulo di acetil-CoA"],
    "h4g-01": [
        "Glicogenosi II (Pompe)",
        "Glicogenosi III (Cori-Forbes)",
        "Glicogenosi V (McArdle)",
        "Glicogenosi VI (Hers)"],
    "h4g-02": [
        "Nella III manca la glicogeno sintasi e il glicogeno non si forma",
        "Nella I manca anche l'insulina, che non viene più secreta",
        "Nella III il glicogeno si accumula nei lisosomi e non nel citosol",
        "Nella I è colpito solo il muscolo, nella III anche il fegato"],
    "h4g-03": [
        "Contiene glucosio 6-fosfatasi vegetale attiva",
        "È ricco di fruttosio, che non richiede l'enzima mancante",
        "Stimola la gluconeogenesi epatica tramite il glucagone",
        "Inibisce la glicolisi epatica e lascia più glucosio libero"],
    "h4g-05": [
        "Manca la glicogeno fosforilasi muscolare",
        "Manca l'enzima ramificante del citosol",
        "Manca la glucosio 6-fosfatasi del reticolo",
        "Manca la glicogenina al centro del granulo"],
    "h4g-08": [
        "Manca la xantina ossidasi epatica e l'acido urico non viene trasformato in urea",
        "Aumenta il glicogeno renale, che viene degradato direttamente ad acido urico",
        "L'acido urico deriva dal glicogeno accumulato, ossidato dai perossisomi",
        "Aumenta l'insulina, che riduce l'escrezione renale di acido urico"],
    "h5r-01": [
        "Aldolasi, enolasi e fosfoglicerato chinasi, che hanno ΔG°' positivo",
        "Esochinasi, aldolasi e piruvato chinasi, sostituite da fosfatasi specifiche",
        "GAP deidrogenasi, PFK1 e PDH, sostituite da enzimi mitocondriali",
        "Solo la piruvato chinasi, perché le altre tappe sono reversibili"],
    "h5n-02": [
        "Defosforila la PEPCK con la PP1 e la rende inattiva nel citosol",
        "Inibisce allostericamente la PEPCK tramite il fruttosio 2,6-bisfosfato",
        "Aumenta il cAMP, che tramite CREB reprime il gene della PEPCK",
        "Attiva il GRE del promotore della PEPCK insieme al cortisolo"],
    "h5n-08": [
        "Stimolano iperglicemia e insulina; inibiscono ipoglicemia, amminoacidi e catecolamine",
        "Stimolano acidi grassi e corpi chetonici; inibiscono gli amminoacidi e l'ipoglicemia",
        "Stimolano somatostatina e insulina; inibiscono adrenalina, noradrenalina e amminoacidi",
        "Il glucagone viene secreto in modo costante, indipendentemente dalla glicemia"],
    "h5a-04": [
        "Ipoglicemia grave e incapacità di correre per esaurimento del glucosio",
        "Obesità e diabete per eccesso di gluconeogenesi nel muscolo",
        "Incapacità di correre a lungo per accumulo di lattato nel muscolo",
        "Accumulo di glicogeno muscolare e ridotta sensibilità all'insulina"],
    "h5a-05": [
        "La gluconeogenesi si blocca definitivamente dopo il viaggio",
        "La glicemia aumenta di notte per un eccesso di insulina",
        "Il glicogeno epatico non viene più usato durante la notte",
        "Non cambia nulla, perché la melatonina regola subito anche la PEPCK"],
    "h5a-07": [
        "Il GLUT1 trasporta il glucagone fuori dalla cellula α quando la glicemia cala",
        "Le cellule α hanno GLUT2 e si comportano come le β, ma con segnale invertito",
        "L'insulina attiva le cellule α durante l'ipoglicemia tramite il recettore tirosin-chinasico",
        "Le cellule α sono insensibili al glucosio e rispondono solo alle catecolamine"],
    "h5a-08": [
        "Inibisce la sintesi di glicogeno muscolare, che viene degradato",
        "Blocca la β-ossidazione nel muscolo, che consuma allora le proteine",
        "Aumenta l'insulina e la lipogenesi, sottraendo amminoacidi al muscolo",
        "Inibisce la PEPCK epatica e costringe il muscolo a produrre glucosio"],
    "h6g-03": [
        "Solo muscolo scheletrico e cuore, per l'alto consumo di ATP",
        "Solo cervello e retina, che dipendono dal glucosio e dal NADPH",
        "Solo i tessuti che fanno gluconeogenesi, cioè fegato e rene",
        "Solo gli eritrociti, perché non hanno mitocondri e altre vie per il NADPH"],
    "h6g-04": [
        "Non ha glucosio 6-fosfato disponibile nel citosol",
        "Non ha bisogno di ribosio, perché non sintetizza nucleotidi",
        "È inibita dal glucagone tramite fosforilazione della G6PD",
        "Non contiene NADP⁺, ma solo NAD⁺ legato agli enzimi glicolitici"],
    "h6g-05": [
        "La fase non ossidativa consuma ATP a ogni trasferimento, e questo la rende reversibile",
        "La fase ossidativa avviene nel mitocondrio, dove i prodotti non possono tornare indietro",
        "La fase non ossidativa usa NADPH come riducente, che la rende reversibile",
        "In realtà sono tutte irreversibili, perché la via è regolata solo dalla G6PD"],
    "h6g-06": [
        "No, perché il ribosio deriva solo dalla fase ossidativa",
        "Sì, ma solo nel mitocondrio, dove c'è una seconda G6PD",
        "Sì, tramite la gluconeogenesi, che produce ribosio 5-P dal piruvato",
        "No, perché la transchetolasi richiede NADPH come coenzima"],
    "h6g-08": [
        "Il ribosio 5-P inibisce la G6PD e blocca la via finché non viene consumato",
        "Il ribosio 5-P viene ossidato a CO₂ dalla transaldolasi, producendo NADPH",
        "Il ribosio 5-P esce dalla cellula con i GLUT e viene usato dal fegato",
        "Il ribosio 5-P viene trasformato in NADPH dalla 6-fosfogluconato deidrogenasi"],
    "h6n-02": [
        "Solo gli eritrociti hanno la G6PD; il gene è sul cromosoma Y, presente solo nei maschi",
        "Il gene è sul cromosoma Y; negli eritrociti l'enzima è più instabile che negli altri tessuti",
        "Le donne non hanno eritrociti con G6PD, ma usano solo l'enzima malico per il NADPH",
        "È autosomico dominante ma più grave nei maschi per motivi ormonali legati al testosterone"],
    "h6n-03": [
        "Usa NADH come donatore di elettroni e produce ATP durante l'idrossilazione",
        "Trasferisce il fosfato dall'ATP al farmaco per renderlo più solubile in acqua",
        "Usa il glutatione come donatore di ossigeno e lo trasferisce al farmaco",
        "Usa O₂ e due elettroni del NADPH: entrambi gli atomi di O vanno al substrato"],
    "x1c-02": [
        "Vengono ossidati nel ciclo di Krebs e forniscono elettroni alla catena respiratoria",
        "Formano direttamente ATP legandosi all'ADP nella matrice mitocondriale",
        "Sono metaboliti terminali che regolano l'eliminazione dell'urea nel rene",
        "Sostituiscono il glucosio come combustibile quando la glicemia si abbassa"],
    "x1t-01": [
        "La reazione è irreversibile e rappresenta il punto di regolazione principale di tutta la via",
        "L'enzima che la catalizza manca nella cellula, quindi la reazione non procede in nessun verso",
        "Il ΔG°' tabulato è sbagliato, perché misurato in condizioni lontane da quelle biologiche",
        "La reazione procede solo se accoppiata all'idrolisi di ATP, che sposta il ΔG verso lo zero"],
    "x1t-04": [
        "ΔG = ΔG°' − RT ln([prodotti]/[reagenti])",
        "ΔG = ΔG°' + RT ln([reagenti]/[prodotti])",
        "ΔG = ΔG°' × RT ln([prodotti]/[reagenti])",
        "ΔG = −RT ln([prodotti]/[reagenti])"],
    "x1e-02": [
        "Sono ugualmente rapide, perché entrambe agiscono direttamente sul sito attivo",
        "L'allosterica è lenta, perché richiede la trascrizione di nuovi geni nel nucleo",
        "La quantità di enzima non è regolabile: dipende solo dal genoma della cellula",
        "Il controllo della quantità agisce in secondi; l'allosterica in giorni"],
    "x2f-01": [
        "La glucochinasi non lega il glucosio 6-fosfato perché ha un sito attivo troppo piccolo",
        "Il glucosio 6-fosfato non si forma nel fegato, perché viene subito defosforilato nel RE",
        "La glucochinasi è mitocondriale e il glucosio 6-fosfato resta confinato nel citosol",
        "Il glucosio 6-fosfato attiva la glucochinasi invece di inibirla, per accumulare glicogeno"],
    "x2n-03": ["3-PG (o 3PG)", "DHAP (o DAP)", "Glc3P (glucosio 3-P)", "GAP (o GA3P)"],
    "x3r-03": [
        "Il selenio lega l'ossigeno molecolare e lo trasforma direttamente in acqua nel citosol",
        "La selenocisteina è più stabile della cisteina e non si ossida mai, neanche con i perossidi",
        "Il selenio trasporta elettroni dalla catena respiratoria al glutatione ossidato",
        "La selenocisteina lega il NADPH e lo trasferisce direttamente al perossido da ridurre"],
    "x3r-04": [
        "K e B12 (cobalamina)",
        "B1, B2 e la niacina (provitamina B3)",
        "D, K e il colecalciferolo (provitamina D)",
        "K, B12 e acido folico (provitamine)"],
    "x3m-02": [
        "Il padre trasmette mitocondri sani ad alcuni figli e non ad altri, compensando il difetto",
        "Ogni figlio ha mutazioni nucleari diverse che modificano il fenotipo mitocondriale",
        "Il mtDNA si ricombina con quello paterno in modo diverso in ogni figlio",
        "La madre trasmette il mtDNA mutato solo ai figli maschi, mentre le femmine sono portatrici"],
    "x4o-01": [
        "Il glucagone circola a concentrazioni molto alte e satura tutti i recettori epatici disponibili",
        "Il glucagone entra nella cellula e attiva direttamente tutte le fosforilasi del glicogeno",
        "Il glucagone agisce sul DNA e aumenta rapidamente la sintesi della glicogeno fosforilasi",
        "Ogni recettore attivato produce una sola molecola di cAMP, che basta per tutta la cellula"],
    "x5f-03": [
        "Lega un recettore di membrana accoppiato a Gs, attiva l'adenilato ciclasi e la PKA fosforila gli enzimi",
        "È un peptide: fosforila direttamente la PFK2 nel citosol e abbassa il fruttosio 2,6-bisfosfato",
        "Inibisce l'insulina nel sangue legandola e impedendole di raggiungere il recettore epatico",
        "Lega un recettore tirosin-chinasico, attiva la PKB e aumenta la trascrizione degli enzimi"],
    "x5g-01": [
        "Esochinasi e aldolasi, come per gli altri zuccheri",
        "Trioso fosfato isomerasi e PEPCK citosolica",
        "Glicerolo fosfatasi e aldolasi B epatica",
        "Glicerolo chinasi e trioso fosfato isomerasi"],
    "x5g-03": [
        "Diventa acetil-CoA e poi citrato nel ciclo di Krebs",
        "Diventa glicerolo e poi diidrossiacetone fosfato",
        "Diventa piruvato tramite la lattato deidrogenasi",
        "Diventa malonil-CoA e poi ossalacetato"],
    "x5a-01": [
        "I corpi chetonici si trasformano in glucosio nel fegato e nel rene tramite la PEPCK",
        "Inibiscono direttamente la proteolisi muscolare legando il proteasoma",
        "Attivano la sintesi proteica nel muscolo durante il digiuno prolungato",
        "Il muscolo li usa al posto delle proteine come fonte di azoto per l'urea"],
    "x5a-03": [
        "Più lattato, più tessuto adiposo, meno mitocondri e insulino-resistenza marcata",
        "Meno mitocondri, ma muscoli più grandi, più glicogeno e più forza massima",
        "Diabete di tipo 2 con iperglicemia a digiuno e ridotta sensibilità all'insulina",
        "Meno acidi grassi usati e accumulo di trigliceridi nelle fibre muscolari"],
    "x6g-02": [
        "Solo la fase non ossidativa, partendo dai triosi della glicolisi e senza produrre NADPH",
        "Solo la glicolisi, che fornisce ribosio dall'aldolasi e NADPH dalla GAP deidrogenasi",
        "Il riciclo completo del glucosio 6-P a CO₂, con 12 NADPH e nessun ribosio residuo",
        "Solo la G6PD, che produce ribosio senza la 6-fosfogluconato deidrogenasi"],
    "x6g-03": [
        "La lattato deidrogenasi",
        "La GAP deidrogenasi",
        "La piruvato carbossilasi",
        "La malato deidrogenasi"],
})
FIX["d2n-05"] = [
    "Dalla transaminazione del piruvato",
    "Dall'idrossilazione dell'alanina",
    "Dalla decarbossilazione del glutammato",
    "Dalla degradazione ossidativa della glicina"]
