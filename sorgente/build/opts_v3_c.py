"""Revisione 3, terzo giro: domande in cui la giusta era nettamente più lunga di 3 distrattori su 4
(restava riconoscibile come «una delle due lunghe»). PATCH: id -> {distrattore vecchio: distrattore riscritto}."""
PATCH = {
    "m1c-01": {
        "Il trasporto dei nutrienti dal sangue all'interno delle cellule": "Il trasporto dei nutrienti dal sangue all'interno delle cellule, che consuma ATP",
        "L'insieme delle reazioni che consumano ATP per produrre calore corporeo": "L'insieme delle reazioni che consumano ATP per produrre il calore corporeo"},
    "m1c-02": {
        "Glucosio e acidi grassi": "Glucosio, acidi grassi e glicerolo",
        "Lattato, urea e acetone": "Lattato, urea e acetone (nel digiuno)"},
    "m1c-06": {
        "Nel ciclo di Krebs, perché ossida completamente l'acetil-CoA a due CO₂": "Nel ciclo di Krebs, perché ossida completamente l'acetil-CoA a due molecole di CO₂",
        "In tutte e tre in quantità simile, circa un terzo dell'ATP per ciascuna": "In tutte e tre in quantità simile, circa un terzo dell'ATP totale per ciascuna via"},
    "m1c-07": {"Colesterolo": "Colesterolo (nel fegato)", "Acidi grassi": "Acidi grassi (a catena lunga)"},
    "m1c-08": {"NAD⁺": "NADH⁺", "FAD⁺": "FADPH"},
    "m1t-01": {"Quanta attivazione serve": "Quanta energia di attivazione serve", "Quale enzima la catalizza": "Quale enzima la catalizza e come"},
    "m1t-05": {
        "Consumano sempre ATP, e il ΔG negativo deriva solo da quell'idrolisi": "Consumano sempre ATP, e il ΔG negativo deriva soltanto dall'idrolisi dell'ATP",
        "Sono all'equilibrio, quindi piccole variazioni di substrato le regolano": "Sono all'equilibrio, quindi piccole variazioni di substrato bastano a regolarle"},
    "m1t-06": {
        "A 37 °C il ΔG°' cambia segno, perché è definito a 25 °C": "A 37 °C il ΔG°' cambia segno, perché il valore tabulato è definito a 25 °C e pH 7",
        "Non è possibile: con ΔG°' positivo la reazione procede sempre verso sinistra": "Non è possibile: con ΔG°' positivo la reazione procede sempre verso sinistra nella cellula"},
    "m1t-07": {"Che è espresso in kcal": "Che è espresso in kcal/mol", "Che è la seconda misura": "Che è la seconda misura fatta"},
    "m1a-04": {
        "L'adenina cambia conformazione e cede energia al gruppo fosfato": "L'adenina cambia conformazione e cede la sua energia al gruppo fosfato terminale",
        "Il magnesio legato all'ATP viene liberato e rilascia energia di legame": "Il magnesio legato all'ATP viene liberato e rilascia la sua energia di legame (Mg–O)"},
    "m1a-14": {"Circa 30 mg/dl": "Circa 30–45 mg/dl", "Circa 0,3 mg/dl": "Circa 0,3–0,5 mg/dl"},
    "m1o-07": {
        "Reagente + ATP → prodotto fosforilato + ADP": "Reagente ridotto + ATP → prodotto fosforilato + ADP + Pi",
        "Ossidante + riducente → acqua + energia libera + calore": "Ossidante + riducente → acqua + energia libera + calore dissipato"},
    "m1o-08": {
        "Una riduzione, perché il C1 perde il gruppo aldeidico": "Una riduzione, perché il C1 perde il gruppo aldeidico e acquista idrogeni",
        "Una fosforilazione, perché il fosfato passa dal C3 al C1": "Una fosforilazione, perché il fosfato passa dal C3 al C1 della molecola"},
    "m1e-03": {"Denaturato": "Denaturato (aperto)", "Fosforilato": "Fosforilato (teso)"},
    "m1e-08": {"Costante di Hill": "Costante di Hill (nH)", "Costante di Michaelis": "Costante di Michaelis (KM)"},
    "m2i-05": {
        "Usa SGLT1, che concentra il glucosio contro gradiente": "Usa SGLT1 (neuroni) e SGLT2 (barriera), che concentrano il glucosio",
        "È insulino-dipendente e riceve glucosio grazie al GLUT4": "È insulino-dipendente e riceve glucosio grazie al GLUT4 dei neuroni"},
    "m2f-06": {
        "Per inibire la glicolisi epatica durante il pasto": "Per inibire la glicolisi epatica durante il pasto e risparmiare glucosio per il sangue",
        "Perché il fegato non ha GLUT e deve trattenere il glucosio": "Perché il fegato non ha GLUT e deve trattenere il glucosio appena entrato nella cellula"},
    "m2g-06": {
        "Viene ridotto il FAD e si forma un doppio legame C=C": "Viene ridotto il FAD legato all'enzima e si forma un doppio legame C=C",
        "Il C1 viene eliminato come CO₂ con riduzione del NAD⁺": "Il C1 viene eliminato come CO₂, con riduzione contemporanea del NAD⁺"},
    "m2g-15": {"3-fosfoglicerato": "3-fosfoglicerato (3PG)", "Fosfoenolpiruvato": "Fosfoenolpiruvato (PEP)"},
    "m2r-02": {"Neuroni": "Neuroni corticali", "Epatociti": "Epatociti periportali"},
    "m2r-03": {
        "3, una per cuore, muscolo e fegato": "3, uno per ciascun tessuto: cuore, muscolo e fegato",
        "4, una per ciascuna subunità del tetramero": "4, uno per ciascuna delle subunità del tetramero"},
    "m2n-03": {
        "Produce GTP nella matrice oltre al NADH": "Produce anche GTP nella matrice, oltre a trasferire gli elettroni del NADH",
        "Gli elettroni arrivano al FAD ed entrano dal complesso II": "Gli elettroni arrivano al FAD mitocondriale ed entrano dal complesso II"},
    "m2reg-04": {
        "Un enzima a valle produce un attivatore per l'enzima che sta a monte": "Un enzima a valle produce un attivatore per l'enzima che sta a monte, accelerando l'ingresso",
        "L'enzima viene fosforilato dalla PKA quando arriva il glucagone nel fegato": "L'enzima viene fosforilato dalla PKA quando arriva il glucagone nel fegato, e si attiva"},
    "m2reg-08": {
        "Il fruttosio 6-fosfato degrada l'enzima se resta nel citosol": "Il fruttosio 6-fosfato degrada l'enzima se questo resta libero nel citosol",
        "Per lasciare il glucosio alla sintesi di glicogeno nel nucleo": "Per lasciare il glucosio alla sintesi di glicogeno che avviene nel nucleo"},
    "m2reg-11": {"ADP e NADH": "ADP e NADH citosolico", "AMP e F1,6BP": "AMP e fruttosio 1,6-BP"},
    "m2p-04": {
        "A sinistra, perché il pH intracellulare diventa più basico": "A sinistra, perché il pH intracellulare diventa più basico e l'Hb lega meglio l'O₂",
        "Non si sposta, perché l'eritrocita compensa con l'esochinasi": "Non si sposta, perché l'eritrocita compensa aumentando l'attività dell'esochinasi"},
    "m2p-07": {
        "Viene trasformato in glicerolo dalla fruttosio reduttasi del fegato": "Viene trasformato in glicerolo dalla fruttosio reduttasi del fegato e poi esterificato",
        "Non viene fosforilato nel fegato e si accumula come tale negli epatociti": "Non viene fosforilato nel fegato e si accumula come tale negli epatociti, che si rigonfiano"},
    "m2p-08": {
        "Galattosio → UDP-galattosio → glicogeno → glucosio 1-P": "Galattosio → UDP-galattosio → (glicogeno sintasi) glicogeno → glucosio 1-P",
        "Galattosio → galattosio 6-P → (isomerasi) fruttosio 6-P → glicolisi": "Galattosio → galattosio 6-P → (fosfoesoso isomerasi) fruttosio 6-P → glicolisi"},
    "m2d-01": {"Lattato e NAD⁺": "Lattato, CO₂ e NAD⁺", "Acetaldeide e CO₂": "Acetaldeide, CO₂ e NADH"},
    "m2d-08": {
        "L'insulina fosforila la PDH e ne aumenta l'attività": "L'insulina fa fosforilare la PDH dalla chinasi e ne aumenta l'attività",
        "Il lattato prodotto dalla contrazione attiva la PDH chinasi": "Il lattato prodotto dalla contrazione attiva la PDH chinasi e la fosfatasi"},
    "m2d-09": {"Iperammoniemia e vomito": "Iperammoniemia e vomito ricorrente", "Anemia emolitica e ittero": "Anemia emolitica e ittero neonatale"},
    "m2d-13": {"Un legame tioestere con il CoA": "Un legame tioestere con il CoA dell'E2 (acetil-lipoile)", "Un legame estere con una serina": "Un legame estere con una serina (lipoil-O-Ser)"},
    "m3k-05": {
        "Così l'enzima consuma meno ATP per ogni molecola di citrato prodotta": "Così l'enzima consuma meno ATP per ogni molecola di citrato prodotta nella matrice mitocondriale",
        "L'ossalacetato è il prodotto della reazione e deve uscire prima che entri l'acetil-CoA": "L'ossalacetato è il prodotto della reazione e deve uscire dal sito prima che entri l'acetil-CoA"},
    "m3k-09": {
        "Sì, ma solo se il ciclo lavora alla massima velocità": "Sì, ma solo se il ciclo lavora alla massima velocità e l'ossalacetato è abbondante",
        "Una sì e una no: una viene dall'acetile, l'altra dall'ossalacetato": "Una sì e una no: una viene dall'acetile appena entrato, l'altra dall'ossalacetato"},
    "m3k-10": {
        "La TPP serve alla glicogeno fosforilasi del cuore e alla glicolisi dei neuroni": "La TPP serve alla glicogeno fosforilasi del cuore e all'aldolasi della glicolisi nei neuroni",
        "Manca il NAD, che serve alla catena respiratoria dei tessuti a più alto consumo": "Manca il NAD, che serve alla catena respiratoria dei tessuti a più alto consumo di ossigeno"},
    "m3k-11": {
        "Bloccano il complesso IV legando il ferro dell'eme a3": "Bloccano il complesso IV legando il ferro dell'eme a3 come il cianuro",
        "Legano la TPP della PDH, impedendo la decarbossilazione": "Legano la TPP della PDH, impedendo la decarbossilazione del piruvato"},
    "m3c-02": {"Nella membrana plasmatica": "Nella membrana plasmatica esterna", "Nella matrice mitocondriale": "Nella matrice, libera in soluzione"},
    "m3c-06": {
        "Dal citocromo c e dal complesso IV, che glieli restituiscono": "Dal citocromo c e dal complesso IV, che glieli restituiscono dopo aver ridotto l'O₂",
        "Dal complesso III e dal complesso IV, in ordine di potenziale": "Dal complesso III e dal complesso IV, in ordine crescente di potenziale redox"},
    "m3c-07": {
        "Ridotto solo il complesso III, con tutti gli altri trasportatori ossidati": "Ridotto solo il complesso III bloccato, con tutti gli altri trasportatori della catena ossidati",
        "Tutti ridotti, perché gli elettroni non possono più uscire verso l'ossigeno": "Tutti ridotti, perché gli elettroni non possono più uscire verso l'ossigeno del complesso IV"},
    "m3c-13": {"Ferredossina": "Ferredossina mitocondriale", "Citocromo c1": "Citocromo c1 (eme c)"},
    "m3s-04": {
        "Le tre β sono sempre nella stessa conformazione e lavorano tutte insieme": "Le tre β sono sempre nella stessa conformazione e lavorano tutte insieme a ogni giro di γ",
        "Le α fanno la catalisi, mentre le β servono solo a legare il fosfato inorganico": "Le α fanno la catalisi, mentre le β servono solo a legare il fosfato inorganico e l'ADP"},
    "m3s-05": {
        "Trasporta il NADH citosolico dentro la matrice": "Trasporta il NADH citosolico dentro la matrice, scambiandolo con il NAD⁺",
        "Scambia ADP della matrice con ATP del citosol, consumando ATP": "Scambia ADP della matrice con ATP del citosol, consumando ATP per ogni scambio"},
    "m3s-06": {
        "Blocca l'ATP sintasi legando la subunità c del canale F₀": "Blocca l'ATP sintasi legando la subunità c del canale F₀, come l'oligomicina",
        "Inibisce l'ATP/ADP traslocasi, bloccando l'uscita dell'ATP": "Inibisce l'ATP/ADP traslocasi, bloccando l'uscita dell'ATP verso il citosol"},
    "m3s-07": {
        "Aumenta, perché i protoni rientrano liberamente nella matrice": "Aumenta, perché i protoni rientrano liberamente nella matrice attraverso l'F₀",
        "Si azzera solo la glicolisi, mentre la catena respiratoria continua": "Si azzera solo la glicolisi, mentre la catena respiratoria continua al massimo"},
    "m3s-08": {
        "Pompa protoni fuori dalla matrice per aumentare il gradiente": "Pompa protoni fuori dalla matrice per aumentare il gradiente elettrochimico",
        "Blocca il complesso IV per far accumulare calore nel mitocondrio": "Blocca il complesso IV per far accumulare il calore nel mitocondrio"},
    "m3r-02": {
        "Ossida il NADPH a NADP⁺ senza substrato": "Ossida il NADPH a NADP⁺ senza bisogno di substrato",
        "Produce superossido per uccidere i batteri": "Produce superossido nei fagociti per uccidere i batteri"},
    "m3r-03": {
        "Mai: la catena respiratoria trasferisce sempre tutti gli elettroni fino all'acqua": "Mai: la catena respiratoria trasferisce sempre tutti gli elettroni fino all'acqua, senza perdite",
        "Quando il complesso IV lavora troppo veloce e libera ossigeno parzialmente ridotto": "Quando il complesso IV lavora troppo veloce e libera ossigeno parzialmente ridotto nella matrice"},
    "m3r-04": {
        "Forma il glutatione insieme a cisteina e glicina": "Forma il glutatione insieme a cisteina, glutammato e glicina",
        "Ripara direttamente il DNA danneggiato dai radicali": "Ripara direttamente il DNA danneggiato dai radicali liberi"},
    "m3m-05": {
        "Aumenta l'ATP e quindi apre i canali K⁺ della cellula β": "Aumenta l'ATP e quindi apre i canali K⁺ della cellula β, che si iperpolarizza",
        "Inibisce la glucochinasi della cellula β legandola nel nucleo": "Inibisce la glucochinasi della cellula β legandola e sequestrandola nel nucleo"},
    "m3m-06": {
        "I mitocondri smettono di dividersi e la cellula ne resta priva": "I mitocondri smettono di dividersi con l'età e la cellula ne resta progressivamente priva",
        "L'ATP sintasi viene degradata dal proteasoma e non è più risintetizzata": "L'ATP sintasi viene degradata dal proteasoma e non è più risintetizzata dal genoma nucleare"},
    "m4d-02": {"Amilasi": "α-amilasi salivare", "Esochinasi": "Glucosio 6-fosfatasi"},
    "m4d-04": {
        "È più veloce perché non ha bisogno del piridossal fosfato come cofattore": "È più veloce perché non ha bisogno del piridossal fosfato come cofattore dell'enzima",
        "Il glucosio esce libero e può passare subito nel sangue attraverso i GLUT": "Il glucosio esce libero e può passare subito nel sangue attraverso i GLUT2"},
    "m4d-07": {
        "Sintetizza la glicogenina e la lega alla prima catena di glucosio": "Sintetizza la glicogenina e la lega alla prima catena di glucosio del granulo",
        "Stacca glucosio 1-fosfato dai rami con fosforolisi dei legami α-1,6": "Stacca glucosio 1-fosfato dai rami con la fosforolisi dei legami α-1,6 dei punti di ramo"},
    "m4d-08": {"Nel citosol, libera; soltanto nel fegato": "Nel citosol, libera; soltanto nel fegato adulto", "Nel lume dei lisosomi; in tutti i tessuti": "Nel lume dei lisosomi; in tutti i tessuti del corpo"},
    "m4s-04": {
        "Trasporta il glucosio dentro l'epatocita insieme al GLUT2": "Trasporta il glucosio dentro l'epatocita insieme al GLUT2 e lo fosforila subito",
        "Lega la glicogeno fosforilasi e la tiene attiva sulla particella": "Lega la glicogeno fosforilasi e la tiene attiva sulla particella di glicogeno"},
    "m4s-05": {
        "Idrolizza i legami α-1,6 dei rami e lascia catene lineari": "Idrolizza i legami α-1,6 dei rami e lascia catene lineari più facili da allungare",
        "Aggiunge un singolo glucosio con legame α-1,6 usando l'UDP-glucosio": "Aggiunge un singolo glucosio con legame α-1,6 usando direttamente l'UDP-glucosio"},
    "m4r-06": {
        "Il glucosio 6-fosfato, come per la sintasi": "Il glucosio 6-fosfato e l'insulina, come per la glicogeno sintasi",
        "Solo il glucosio, che si lega alla subunità α": "Solo il glucosio, che si lega alla subunità α e la porta in forma R"},
    "m4r-07": {
        "Viene trasformato in UDP-glucosio dalla sintasi stessa": "Viene trasformato in UDP-glucosio dalla sintasi stessa e poi aggiunto alla catena",
        "Attiva la PKA, che a sua volta fosforila la sintasi nella forma attiva": "Attiva la PKA, che a sua volta fosforila la sintasi e la porta nella forma attiva a"},
    "m4o-04": {"Inibendo la PKA e attivando la PP1": "Inibendo la PKA e attivando la PP1 sul glicogeno", "Via cGMP, attivando la glicogeno sintasi": "Via cGMP e PKG, attivando la glicogeno sintasi"},
    "m4o-05": {
        "Aumenta il Ca²⁺, che attiva la sintasi tramite calmodulina": "Aumenta il Ca²⁺, che attiva la sintasi tramite la calmodulina e la CaM chinasi",
        "La defosforila tramite PP1 e accende la sintesi di glicogeno": "La defosforila tramite la PP1 e accende la sintesi di glicogeno anche a digiuno"},
    "m4e-03": {
        "Gli acidi grassi non entrano nel muscolo senza insulina": "Gli acidi grassi non entrano nel muscolo senza insulina e il muscolo resta a secco",
        "I grassi bloccano i GLUT4 e impediscono l'ingresso del glucosio": "I grassi bloccano i GLUT4 e impediscono l'ingresso del glucosio nel muscolo"},
    "m4g-05": {
        "Il glucagone alto stimola insieme la sintesi di purine e di trigliceridi": "Il glucagone alto stimola insieme, tramite la PKA, la sintesi di purine e quella di trigliceridi",
        "Il rene non filtra né l'acido urico né i trigliceridi per un danno glomerulare": "Il rene non filtra né l'acido urico né i trigliceridi per un danno glomerulare da glicogeno"},
}
PATCH.update({
    "m4g-06": {
        "Diventa glucosio nel muscolo stesso": "Diventa glucosio nel muscolo stesso con la gluconeogenesi",
        "Si accumula nel fegato invece che nel sangue": "Si accumula nel fegato invece che nel sangue periferico"},
    "m4g-07": {
        "Accumulo di mioglobina nel fegato": "Accumulo di mioglobina nel fegato dopo danno muscolare",
        "Carenza ereditaria di mioglobina nel muscolo": "Carenza ereditaria di mioglobina nel muscolo scheletrico"},
    "m4g-08": {
        "Malattia di Hers, fosforilasi epatica": "Malattia di Hers, glicogeno fosforilasi epatica",
        "Malattia di Tarui, fosfofruttochinasi": "Malattia di Tarui, fosfofruttochinasi muscolare"},
    "m5r-05": {
        "La riduzione del GTP a GDP con liberazione di energia": "La riduzione del GTP a GDP, con liberazione di energia libera nel sito attivo",
        "L'ossidazione del NADH citosolico accoppiata alla reazione": "L'ossidazione del NADH citosolico accoppiata direttamente alla reazione"},
    "m5r-06": {
        "Serve più biotina, perché il lattato va carbossilato due volte": "Serve più biotina, perché il lattato va carbossilato due volte prima di diventare PEP",
        "Il lattato salta la piruvato carbossilasi ed entra come malato": "Il lattato salta la piruvato carbossilasi ed entra nel mitocondrio direttamente come malato"},
    "m5g-02": {
        "Non serve NAD⁺ per ossidare il glicerolo 3-fosfato": "Non serve NAD⁺ per ossidare il glicerolo 3-fosfato a triosio fosfato",
        "Entra come piruvato, saltando la fruttosio 1,6-bisfosfatasi": "Entra come piruvato, saltando la fruttosio 1,6-bisfosfatasi e la G6Pasi"},
    "m5g-03": {
        "Lo trasforma tutto in lattato prima di rilasciarlo": "Lo trasforma tutto in lattato prima di rilasciarlo nel sangue",
        "Manca la glicerolo 3-fosfato deidrogenasi citosolica": "Gli manca la glicerolo 3-fosfato deidrogenasi, non la chinasi"},
    "m5reg-05": {
        "Attiva la PP1, che defosforila la PEPCK e la rende inattiva": "Attiva la PP1, che defosforila la PEPCK e la rende inattiva senza ridurne la quantità",
        "Attiva la PKA, che fosforila la PEPCK e ne blocca il sito attivo": "Attiva la PKA, che fosforila la PEPCK e ne blocca il sito attivo legando il GTP"},
    "m5reg-08": {
        "Lavora in coppia con la PFK1, a cui passa direttamente il prodotto": "Lavora in coppia con la PFK1, a cui passa direttamente il prodotto per canalizzazione",
        "Usa due ATP per ogni molecola di fruttosio 2,6-bisfosfato prodotta": "Usa due molecole di ATP per ogni molecola di fruttosio 2,6-bisfosfato prodotta"},
    "m5a-01": {
        "L'etanolo viene ossidato consumando glucosio come fonte di elettroni": "L'etanolo viene ossidato consumando glucosio come fonte di elettroni per l'alcol deidrogenasi",
        "L'etanolo blocca l'assorbimento intestinale del glucosio inibendo gli SGLT1": "L'etanolo blocca l'assorbimento intestinale del glucosio inibendo gli SGLT1 degli enterociti"},
    "m6r-08": {
        "La ribosio 5-P isomerasi li trasforma in glucosio libero": "La ribosio 5-P isomerasi li trasforma in glucosio libero, che esce dalla cellula",
        "Si accumulano nel citosol come riserva per le sintesi successive": "Si accumulano nel citosol come riserva di pentosi per le sintesi successive"},
    "m6r-09": {
        "Trasforma il glicogeno in ribosio tramite la fosforilasi": "Trasforma il glicogeno in ribosio tramite la fosforilasi e la ribosio 5-P isomerasi",
        "Usa solo la G6PD, bloccando la 6-fosfogluconato deidrogenasi": "Usa solo la G6PD, bloccando la 6-fosfogluconato deidrogenasi a valle del lattone"},
    "m6g-01": {
        "Transchetolasi": "Transchetolasi (con TPP)",
        "Ribosio 5-P isomerasi": "Ribosio 5-fosfato isomerasi A"},
    "m6n-01": {
        "Serve a sintetizzare l'emoglobina": "Serve a sintetizzare l'eme e la globina dell'emoglobina",
        "Trasporta l'ossigeno insieme all'emoglobina": "Trasporta l'ossigeno insieme all'emoglobina nei capillari"},
    "m6n-02": {
        "Un'allergia IgE-mediata alle proteine delle fave": "Un'allergia IgE-mediata alle proteine delle fave e dei piselli"},
    "m6n-03": {
        "Urea, nel ciclo dell'ornitina": "Urea nel ciclo dell'ornitina, e purine nel fegato",
        "Glucosio, durante la gluconeogenesi": "Glucosio durante la gluconeogenesi, e glicogeno"},
    "m6n-04": {
        "A sintetizzare anticorpi contro i batteri": "A sintetizzare gli anticorpi che opsonizzano i batteri da fagocitare",
        "Alla catalasi, che produce acqua ossigenata": "Alla catalasi, che produce acqua ossigenata per uccidere i batteri"},
    "m6n-07": {
        "Granuli di ferro accumulati nei siderociti": "Granuli di ferro non emico accumulati nei siderociti del midollo",
        "Inclusioni batteriche nei globuli rossi infetti": "Inclusioni batteriche nei globuli rossi infetti da Bartonella"},
    "m6n-10": {
        "Acido acetilsalicilico": "Acido acetilsalicilico coniugato",
        "Paracetamolo glucuronide": "Paracetamolo solfato (via PAPS)"},
    "m6n-13": {
        "Ormoni che inducono gli enzimi epatici": "Ormoni che inducono gli enzimi epatici della fase I e II",
        "Enzimi della famiglia del citocromo P450": "Enzimi della famiglia del citocromo P450 microsomiale"},
    "b1i-01": {"Sulla membrana plasmatica": "Sulla membrana plasmatica (GPCR)", "Nel reticolo endoplasmatico": "Nel reticolo endoplasmatico liscio"},
    "b2c-10": {"Colinesterasi": "Butirrilcolinesterasi", "Acetilcolinesterasi": "Acetilcolinesterasi (AChE)"},
    "b3c-01": {"Fosfolipasi C": "Fosfolipasi C (β)", "Fosfodiesterasi": "Fosfodiesterasi 4"},
    "b3s-04": {
        "Resta nell'endosoma per sempre, legato all'arrestina e al ligando": "Resta nell'endosoma per sempre, legato alla β-arrestina e al ligando"},
    "b4a-06": {
        "Si misura l'assorbanza del campione a 280 nm e si confronta con una curva di ormone purificato": "Si misura l'assorbanza del campione a 280 nm, dovuta ai residui aromatici, e la si confronta con una curva di ormone purificato",
        "Si misura direttamente la radioattività dell'ormone endogeno, che è naturalmente marcato con iodio": "Si misura direttamente la radioattività dell'ormone endogeno, che è naturalmente marcato con iodio radioattivo, senza anticorpi"},
    "b5i-06": {
        "Immediati (minuti, 10⁻⁸ M): richiedono più insulina. Tardivi (giorni): passano per il cAMP e la PKA nel nucleo": "Immediati (minuti, 10⁻⁸ M): richiedono più insulina e agiscono sui GLUT2. Tardivi (giorni, 10⁻⁶ M): passano per il cAMP e la PKA nel nucleo",
        "Immediati (secondi, 10⁻⁶ M): apertura dei canali K⁺. Tardivi (minuti, 10⁻⁹ M): GLUT4 ed enzimi del glicogeno muscolare": "Immediati (secondi, 10⁻⁶ M): apertura dei canali K⁺. Tardivi (minuti, 10⁻⁹ M): GLUT4, enzimi del glicogeno muscolare e trascrizione"},
    "d2h-03": {
        "Quando la glicina raggiunge carica netta −1 e tutti i suoi gruppi sono già deprotonati": "Quando la glicina raggiunge carica netta −1 e tutti i suoi gruppi ionizzabili sono già deprotonati",
        "Mai: la curva della glicina sale in modo regolare perché i due gruppi tamponano insieme": "Mai: la curva della glicina sale in modo regolare, perché i due gruppi tamponano insieme fino a pH 12"},
    "d2p-01": {
        "Per condensazione tra i gruppi α-amminici di due amminoacidi, con uscita di NH₃": "Per condensazione tra i gruppi α-amminici di due amminoacidi successivi, con uscita di NH₃",
        "Per condensazione tra le catene laterali di due amminoacidi vicini, con uscita di H₂O": "Per condensazione tra le catene laterali di due amminoacidi vicini nella catena, con uscita di H₂O"},
    "d3t-02": {
        "Sono sinonimi: entrambi indicano un'unità globulare compatta di una catena polipeptidica": "Sono sinonimi: entrambi indicano un'unità globulare compatta e funzionale di una catena polipeptidica",
        "Motivo: sequenza di pochi amminoacidi conservata; dominio: struttura quaternaria di più subunità": "Motivo: breve sequenza di pochi amminoacidi conservata; dominio: struttura quaternaria di più subunità"},
    "d3f-04": {
        "Il folding avviene solo nel ribosoma, mentre la catena viene ancora sintetizzata": "Il folding avviene solo nel ribosoma, mentre la catena viene ancora sintetizzata dal C-terminale",
        "Le proteine non si ripiegano mai da sole: serve sempre l'intervento delle chaperonine": "Le proteine non si ripiegano mai da sole: serve sempre l'intervento delle chaperonine con ATP"},
    "d3f-08": {
        "DnaJ lega la proteina e la porta a GroEL; GrpE fa da coperchio alla camera al posto di GroES": "DnaJ lega la proteina nascente e la porta a GroEL; GrpE fa da coperchio alla camera al posto di GroES",
        "Degradano le proteine misfoldate: DnaJ le marca con l'ubiquitina, GrpE le porta al proteasoma": "Degradano le proteine misfoldate: DnaJ le marca con l'ubiquitina, GrpE le porta al proteasoma 26S"},
    "dh3q-01": {"Diedrica D4, come GroEL": "Diedrica D4, come i tetrameri planari", "Speculare (per riflessione)": "Speculare, per riflessione su un piano"},
    "h1c-02": {
        "Perché non può più dare energia e serve soltanto come precursore biosintetico": "Perché non può più dare energia e serve soltanto come precursore per le biosintesi",
        "Perché viene eliminato con la respirazione insieme alla CO₂ del ciclo di Krebs": "Perché viene eliminato con la respirazione, insieme alla CO₂ prodotta dal ciclo di Krebs"},
    "h1t-03": {
        "Perché sono le uniche reazioni della via che producono o consumano ATP": "Perché sono le uniche reazioni della via che producono o consumano ATP e GTP",
        "Perché le reazioni all'equilibrio sono troppo lente per essere regolate": "Perché le reazioni all'equilibrio sono troppo lente per essere regolate da ormoni"},
    "h1a-01": {
        "Perché dall'ATP si forma un legame tioestere con il coenzima A": "Perché dall'ATP si forma un legame tioestere ad alta energia con il coenzima A",
        "Perché la reazione consuma un protone e alcalinizza l'ambiente": "Perché la reazione consuma un protone e alcalinizza l'ambiente del citosol"},
    "h1a-02": {
        "L'AMP prodotto inibisce allostericamente la reazione inversa": "L'AMP prodotto inibisce allostericamente la reazione inversa e la rende lenta",
        "Si forma un legame fosfoestere ad alta energia sul substrato attivato": "Si forma un legame fosfoestere ad alta energia sul substrato attivato, che lo stabilizza"},
    "h1a-03": {
        "0,75: carica alta, prevalgono le vie anaboliche": "0,75: carica alta, prevalgono le vie anaboliche e di sintesi",
        "0,9: equilibrio tra vie cataboliche e anaboliche": "0,9: carica normale, equilibrio tra catabolismo e anabolismo"},
    "h1a-04": {
        "La temperatura corporea, che lo rende più vicino allo zero": "La temperatura corporea di 37 °C, che lo rende più vicino allo zero",
        "L'AMP, che compete con l'ADP e ne riduce la concentrazione": "L'AMP, che compete con l'ADP e ne riduce la concentrazione libera"},
    "h1o-03": {
        "L'ossidazione di un'aldeide ad acido carbossilico": "L'ossidazione di un'aldeide ad acido carbossilico, tipica del FAD",
        "Un'idratazione del doppio legame con aggiunta di H₂O": "Un'idratazione del doppio legame con aggiunta di una molecola d'acqua"},
    "h1o-05": {
        "Un'idrolisi, perché richiede l'aggiunta di acqua": "Un'idrolisi, perché richiede l'aggiunta di una molecola di acqua",
        "Un'ossidazione: il chetone è più ossidato dell'aldeide": "Un'ossidazione: il chetone è più ossidato dell'aldeide e serve NAD⁺"},
    "h1e-01": {"Non cambiano né la Vmax né la KM": "Non cambiano né la Vmax né la KM dell'enzima", "Raddoppiano sia la Vmax sia la KM": "Raddoppiano sia la Vmax sia la KM insieme"},
    "h1e-02": {
        "Lavorano entrambi a circa metà della propria Vmax": "Lavorano entrambi a circa metà della propria Vmax massima",
        "Il secondo è più veloce, perché ha la KM più alta": "Il secondo è più veloce, perché ha la KM più alta del primo"},
})
PATCH.update({
    "h1e-04": {
        "È sempre un inibitore, perché stabilizza la forma T": "È sempre un inibitore, perché stabilizza la forma T a bassa affinità per il substrato",
        "È un ormone che fosforila l'enzima su serine e treonine": "È un ormone che fa fosforilare l'enzima su serine e treonine tramite la PKA"},
    "h1e-07": {
        "Che la reazione catalizzata è irreversibile": "Che la reazione catalizzata è irreversibile e molto esoergonica",
        "Che è un enzima allosterico con cinetica sigmoide": "Che è un enzima allosterico con cinetica sigmoide e cooperativa"},
    "h1e-08": {
        "La gluconeogenesi avviene interamente nel mitocondrio": "La gluconeogenesi avviene interamente nel mitocondrio e la glicolisi nel citosol",
        "Le due vie usano coenzimi diversi che non si scambiano": "Le due vie usano coenzimi diversi (NAD⁺ e NADP⁺) che non si scambiano mai"},
    "h2i-08": {
        "Aumenta il gradiente di Na⁺ sfruttato dal GLUT4": "Aumenta il gradiente di Na⁺ che il GLUT4 sfrutta per concentrare il glucosio",
        "Attiva la trascrizione del gene GLUT1 nel muscolo": "Attiva la trascrizione del gene GLUT1 nel muscolo, che diventa il trasportatore principale"},
    "h2f-01": {
        "Entrambe lavorano a circa metà della loro Vmax": "Entrambe lavorano a circa metà della loro Vmax, perché la glicemia è normale",
        "Entrambe lavorano vicino alla loro velocità massima": "Entrambe lavorano vicino alla loro velocità massima, perché il glucosio è in eccesso"},
    "h2f-05": {
        "Accumulo di glicogeno epatico con epatomegalia": "Accumulo di glicogeno epatico con epatomegalia e ipoglicemia",
        "Assenza totale di insulina, come nel diabete tipo 1": "Assenza totale di insulina fin dall'infanzia, come nel diabete tipo 1"},
    "h2f-07": {
        "Non ci sono differenze di specificità tra i due enzimi": "Non ci sono differenze di specificità: entrambi fosforilano tutti gli esosi alla stessa velocità",
        "Entrambe fosforilano solo il mannosio quando il glucosio è basso": "Entrambe fosforilano solo il mannosio quando il glucosio è basso, e il fegato perde il fruttosio"},
    "h2f-08": {"Diventare glicogeno": "Diventare glicogeno tramite glucosio 1-P", "Entrare nella glicolisi": "Entrare nella glicolisi come fruttosio 6-P"},
    "h2g-06": {
        "Il PEP contiene due legami fosfoanidridici in successione": "Il PEP contiene due legami fosfoanidridici in successione, come l'ATP",
        "Il PEP contiene un legame tioestere tra fosfato e piruvato": "Il PEP contiene un legame tioestere tra il fosfato e il piruvato"},
    "h2g-07": {"Dal GTP prodotto nel ciclo di Krebs": "Dal GTP prodotto dalla succinil-CoA sintetasi", "Dall'ATP, tramite una chinasi dedicata": "Dall'ATP, tramite una chinasi dedicata a lei"},
    "h2m-04": {"Non ha alcun effetto sul pH": "Non ha alcun effetto sul pH della cellula", "Libera due H⁺ per ogni piruvato": "Libera due H⁺ per ogni piruvato ridotto"},
    "h2m-05": {
        "Deficit di LDH, che impedisce lo smaltimento del lattato": "Deficit acquisito di LDH, che impedisce lo smaltimento del lattato nel fegato",
        "Aumento della gluconeogenesi muscolare, che rilascia lattato": "Aumento della gluconeogenesi muscolare, che rilascia lattato invece di glucosio"},
    "h2m-07": {
        "L'etanolo blocca i GLUT4 del muscolo": "L'etanolo blocca i GLUT4 del muscolo e il glucosio resta nel sangue",
        "L'etanolo viene trasformato in glicogeno e sottrae glucosio": "L'etanolo viene trasformato in glicogeno epatico e sottrae glucosio"},
    "h2n-01": {
        "Produce NADPH invece di NADH nella matrice": "Produce NADPH invece di NADH nella matrice, che non entra nella catena",
        "Trasferisce un solo elettrone per ogni NADH citosolico": "Trasferisce un solo elettrone per ogni NADH citosolico invece di due"},
    "h2n-05": {"In aerobiosi la glicolisi non produce NADH": "In aerobiosi la glicolisi non produce più NADH", "Viene tutto convertito in lattato dalla LDH": "Viene tutto riossidato dalla LDH, formando lattato"},
    "h2n-08": {
        "Nessuna navetta nel cuore, che usa solo il lattato": "Nessuna navetta nel cuore, che usa solo lattato; glicerolo fosfato negli altri",
        "Malato-aspartato in tutti i tessuti, senza differenze": "Malato-aspartato in tutti i tessuti, senza differenze tra muscolo e fegato"},
    "h2r-01": {
        "Le due forme differiscono solo per la Vmax": "Le due forme differiscono solo per la Vmax, non nel sito",
        "In T il sito attivo lega più ATP e meno F6P": "In T il sito attivo lega più ATP e meno F6P per affinità"},
    "h2r-02": {
        "Perché l'ATP non ha alcun effetto sulla PFK1": "Perché l'ATP non ha alcun effetto sulla PFK1, né come substrato né come inibitore",
        "Perché l'AMP è prodotto direttamente dalla PFK1": "Perché l'AMP è prodotto direttamente dalla PFK1 a ogni reazione catalizzata"},
    "h2r-06": {"Effetto omotropico del substrato": "Effetto omotropico: il substrato prepara gli altri siti", "Inibizione da prodotto della PFK1": "Inibizione da prodotto: rallenta la PFK1 a monte"},
    "h2r-07": {
        "Si inattiva solo la PK muscolare": "Si inattiva solo la PK muscolare, mentre quella epatica resta attiva",
        "Il PEP viene trasformato in glicogeno": "Il PEP viene trasformato direttamente in glicogeno nel fegato"},
    "h2r-08": {"La GAP deidrogenasi, perché è l'unica redox": "La GAP deidrogenasi, perché è l'unica reazione redox", "La piruvato chinasi, perché è l'ultima reazione": "La piruvato chinasi, perché è l'ultima reazione della via"},
    "h2p-01": {"Il NADH aumenta e attiva la glicolisi": "Il NADH aumenta e attiva allostericamente l'esochinasi", "L'AMP aumenta e blocca la piruvato chinasi": "L'AMP aumenta e blocca la piruvato chinasi del lievito"},
    "h2p-04": {
        "Manca il NADPH e il glutatione non viene ridotto": "Manca il NADPH e il glutatione non viene ridotto, come nel favismo",
        "Si blocca la sintesi dell'eme nell'eritrocita maturo": "Si blocca la sintesi dell'eme nell'eritrocita maturo, che perde l'Hb"},
    "h2p-07": {"Attiva la PFK1 più del glucosio": "Attiva la PFK1 più del glucosio, saturandola", "Entra solo in presenza di insulina": "Entra solo in presenza di insulina, che attiva la lipogenesi"},
    "h2d-01": {
        "La citrato sintasi: si accumula acetil-CoA": "La citrato sintasi, che usa la tiamina: si accumula acetil-CoA",
        "Solo la LDH: si accumula piruvato ma non lattato": "Solo la LDH, che usa la tiamina: si accumula piruvato ma non lattato"},
    "h2d-02": {
        "Nell'uomo manca la piruvato carbossilasi": "Nell'uomo manca la piruvato carbossilasi, che serve a fare ossalacetato",
        "Nell'uomo la gluconeogenesi non avviene nel fegato": "Nell'uomo la gluconeogenesi non avviene nel fegato ma solo nel rene"},
    "h2d-03": {
        "E1 trasferisce al CoA; E2 decarbossila; E3 riduce il FAD": "E1 trasferisce l'acetile al CoA; E2 decarbossila; E3 riduce il FAD",
        "E1 riduce il NAD⁺; E2 decarbossila; E3 trasferisce l'acetile": "E1 riduce il NAD⁺; E2 decarbossila il piruvato; E3 trasferisce l'acetile"},
    "h2d-04": {"Rende la reazione reversibile": "Rende la reazione reversibile a seconda dei bisogni", "Fosforila E1 per regolare il complesso": "Fosforila E1 per regolare l'attività del complesso"},
    "h2d-05": {"Si lega al TPP e lo attiva": "Si lega al TPP di E1 e lo attiva", "Riossida il NADH della matrice": "Riossida il NADH della matrice per E3"},
    "h2d-06": {"Alto Ca²⁺ nel muscolo durante la contrazione": "Alto Ca²⁺ nel muscolo durante la contrazione intensa", "Ipoglicemia con AMP alto in tutte le cellule": "Ipoglicemia con AMP alto in tutte le cellule del corpo"},
    "h3k-04": {
        "Usa il FAD, che ha un potenziale più positivo del NAD⁺": "Usa il FAD, che ha un potenziale più positivo del NAD⁺ e accetta meglio gli elettroni",
        "Rompe un legame tioestere ad alta energia del substrato": "Rompe un legame tioestere ad alta energia del substrato, come la succinil-CoA sintetasi"},
    "h3k-06": {
        "Il GTP fosforila il succinato per formare succinil-CoA": "Il GTP fosforila il succinato per formare succinil-CoA e poi il GDP",
        "Il FADH₂ della succinato deidrogenasi fosforila il GDP": "Il FADH₂ della succinato deidrogenasi fosforila il GDP legato all'enzima"},
    "h3c-01": {"12 elettroni, in 6 NADH": "12 elettroni, in 6 NADH e 0 FADH₂", "24 elettroni, in 12 NADH": "24 elettroni, in 12 NADH e 0 FADH₂"},
    "h3c-02": {
        "Il NADH ha un potenziale più positivo dell'O₂": "Il NADH ha un potenziale più positivo dell'O₂ e cede elettroni per questo",
        "Ogni complesso consuma ATP per spingere gli elettroni": "Ogni complesso consuma ATP per spingere gli elettroni verso il successivo"},
    "h3c-06": {
        "Contiene un eme che accetta un solo elettrone alla volta": "Contiene un eme che accetta un solo elettrone alla volta, come i citocromi",
        "È legato covalentemente al complesso III e ruota con esso": "È legato covalentemente al complesso III e ruota con esso nella membrana"},
    "h3c-07": {
        "A ridurre direttamente l'O₂ ad acqua nel complesso III": "A ridurre direttamente l'O₂ ad acqua nel complesso III, senza il complesso IV",
        "A portare il NADH citosolico all'interno della matrice": "A portare gli elettroni del NADH citosolico all'interno della matrice"},
    "h3s-04": {"Resta costante in entrambi i casi": "Resta costante in entrambi i casi, perché c'è succinato", "Aumenta con l'oligomicina e si ferma con il DNP": "Aumenta con l'oligomicina e si ferma del tutto con il DNP"},
    "h3s-05": {
        "Aumenta la sintesi di ATP e l'eccesso di ATP produce calore": "Aumenta la sintesi di ATP e l'eccesso di ATP idrolizzato produce molto calore",
        "Inibisce la glicolisi e costringe la cellula a bruciare solo grassi": "Inibisce la glicolisi e costringe la cellula a bruciare solo grassi, che scaldano"},
    "h3s-06": {"Aumenta la sintesi di ATP con l'ATP sintasi": "Aumenta la sintesi di ATP con l'ATP sintasi e la idrolizza", "Fermenta il glucosio a lattato producendo calore": "Fermenta il glucosio a lattato, producendo calore nel citosol"},
    "h3s-07": {"Dal GTP prodotto nel ciclo di Krebs": "Dal GTP prodotto dalla succinil-CoA sintetasi nel ciclo di Krebs", "Da nessuna fonte: lo scambio è elettricamente neutro": "Da nessuna fonte: lo scambio è elettricamente neutro e spontaneo"},
    "h3s-08": {"2 H⁺ per ATP: NADH 5 ATP, FADH₂ 3 ATP": "2 H⁺ per ATP sintetizzato: NADH 5 ATP, FADH₂ 3 ATP", "8 H⁺ per ATP: NADH 1,25 ATP, FADH₂ 0,75": "Circa 8 H⁺ per ATP: NADH 10 H⁺ (1,25), FADH₂ 6 H⁺ (0,75)"},
    "h3r-01": {"Citocromo c ossidasi, poi catalasi": "Citocromo c ossidasi (→ H₂O₂), poi catalasi", "SOD da sola, che produce direttamente acqua": "SOD da sola (→ H₂O), senza bisogno di altri enzimi"},
    "h3r-02": {
        "Senza G6PD si accumula lattato che lisa la membrana": "Senza G6PD si accumula lattato che acidifica e lisa la membrana dell'eritrocita",
        "Senza G6PD aumenta il 2,3-BPG e l'emoglobina precipita": "Senza G6PD aumenta il 2,3-BPG e l'emoglobina precipita nei corpi di Heinz"},
    "h3r-03": {"Il selenio è un metallo di transizione redox": "Il selenio è un metallo di transizione redox come il ferro", "Il selenio lega l'ossigeno come il ferro dell'eme": "Il selenio lega l'ossigeno molecolare come il ferro dell'eme"},
    "h3r-05": {"Solo quando il complesso IV è iperattivo": "Solo quando il complesso IV è iperattivo e consuma troppo O₂", "Quando nella matrice c'è molto ADP disponibile": "Quando nella matrice c'è molto ADP disponibile per l'ATP sintasi"},
    "h3r-06": {"Attiva la PDH e riduce la produzione di lattato": "Attiva la PDH e riduce la produzione di lattato nel citosol", "Aumenta la sintesi di ubichinone e di citocromo c": "Aumenta la sintesi di ubichinone e di citocromo c nella membrana"},
    "h3r-08": {"K e D": "K, D e B12", "B1, B2 e B6": "B1, B2, B6 e niacina"},
    "h3m-01": {"Solo il figlio maschio è a rischio": "Solo il figlio maschio, perché l'X è materno", "Entrambi hanno il 25% di probabilità": "Entrambi hanno il 25% di probabilità di ereditarla"},
    "h3m-04": {"I radicali bloccano il GLUT4 delle cellule β": "I radicali bloccano il GLUT4 delle cellule β e riducono l'ingresso del glucosio", "Lo stress ossidativo aumenta l'ATP e blocca l'esocitosi": "Lo stress ossidativo aumenta l'ATP e blocca l'esocitosi dei granuli di insulina"},
    "h3m-05": {"Non viene mai replicato, quindi accumula danni": "Non viene mai replicato dopo la nascita, quindi accumula danni nel tempo", "È a singolo filamento e non ha un filamento stampo": "È a singolo filamento e non ha un filamento stampo per la riparazione"},
    "h3m-06": {"Si aprono direttamente i canali del Ca²⁺": "Si aprono direttamente i canali del Ca²⁺ e la secrezione aumenta", "Non cambia nulla, perché la glicolisi compensa": "Non cambia nulla, perché la glicolisi compensa del tutto il deficit"},
    "h3m-07": {"La perdita progressiva del DNA nucleare": "La perdita progressiva del DNA nucleare a ogni divisione", "L'aumento della sintesi di ATP con l'età": "L'aumento eccessivo della sintesi di ATP con l'età"},
    "h3m-08": {"Eritrociti e piastrine": "Eritrociti, piastrine e linfociti", "Pelle, capelli e mucose": "Pelle, capelli e mucose orali"},
    "h4d-02": {
        "La glicogenina rimuove il ramo e lo trasferisce su una nuova catena": "La glicogenina rimuove il ramo intero e lo trasferisce su una nuova catena in crescita",
        "L'α-1,6-glucosidasi stacca tutti e 4 i residui come glucosio 1-fosfato": "L'α-1,6-glucosidasi stacca tutti e 4 i residui del ramo come glucosio 1-fosfato"},
    "h4d-06": {
        "L'UTP trasferisce il fosfato al C6 formando UDP-glucosio": "L'UTP trasferisce il fosfato al C6 formando UDP-glucosio come intermedio",
        "L'ATP fosforila il C6 e un'idrolasi stacca il fosfato dal C1": "L'ATP fosforila il C6 e poi un'idrolasi separata stacca il fosfato dal C1"},
    "h4s-02": {"Degrada il glicogeno all'interno dei lisosomi": "Degrada il glicogeno all'interno dei lisosomi insieme all'α-glucosidasi", "Trasporta il glucosio 6-fosfato dentro il reticolo": "Trasporta il glucosio 6-fosfato dentro il reticolo endoplasmatico"},
    "h4r-01": {"La forma a è inattiva e la b è attiva": "La forma a è inattiva in T e la b è attiva in R", "La forma a è sempre in T e la b sempre in R": "La forma a è sempre in T e la b è sempre in R"},
    "h4r-03": {"Il cAMP, che si lega al sito catalitico": "Il cAMP, che si lega al sito catalitico dopo il pasto", "L'adrenalina, che si lega al sito allosterico": "L'adrenalina, che si lega al sito allosterico dell'enzima"},
    "h4r-06": {"Perché la PP1 consuma il glucosio liberato": "Perché la PP1 consuma il glucosio 1-fosfato liberato dalla fosforilasi", "Perché la PP1 attiva la glicogeno fosforilasi": "Perché la PP1 attiva la glicogeno fosforilasi e ne raddoppia l'effetto"},
    "h4r-07": {"Richiede l'insulina per essere attivata": "Richiede l'insulina per essere attivata dalla PKB", "Usa il GTP invece dell'ATP come donatore": "Usa il GTP invece dell'ATP come donatore di fosfato"},
    "h4o-01": {"Gq → PLC → IP₃ → Ca²⁺ → glicogeno sintasi attiva": "Gq → PLC → IP₃ → Ca²⁺ → calmodulina → glicogeno sintasi attiva", "Gi → calo del cAMP → PP1 inattiva → fosforilasi a": "Gi → calo del cAMP → PKA inattiva → PP1 inattiva → fosforilasi a"},
    "h4o-03": {"Con l'AMP legato alla subunità α": "Con l'AMP legato alla subunità α e nessuna fosforilazione", "Solo con l'insulina tramite la PKB": "Solo con l'insulina, tramite la PKB e la PP1"},
    "h4o-04": {"Il cortisolo, che induce la fosforilasi muscolare": "Il cortisolo, che induce la sintesi della fosforilasi muscolare", "Il glucosio plasmatico, che si lega alla fosforilasi": "Il glucosio plasmatico, che si lega alla fosforilasi muscolare b"},
    "h4o-07": {"L'insulina non ha alcun effetto sul glicogeno del fegato": "L'insulina non ha alcun effetto sul glicogeno del fegato, solo sul muscolo", "Il glucosio agisce come un ormone sul recettore dell'insulina": "Il glucosio agisce come un ormone sul recettore dell'insulina degli epatociti"},
})
PATCH.update({
    "h4a-02": {"Sollevamento pesi ripetuto": "Sollevamento pesi ripetuto (anaerobico)", "Sforzo moderato e prolungato": "Sforzo moderato e prolungato (65% VO₂max)"},
    "h4a-03": {"Solo grassi, con una dieta chetogenica": "Solo grassi, con una dieta chetogenica per risparmiare glucosio", "Carboidrati solo dopo 48 ore di riposo": "Carboidrati solo dopo 48 ore di riposo, quando la sintasi è attiva"},
    "h4a-04": {
        "Il trasferimento diretto di glicogeno dal fegato al muscolo": "Il trasferimento diretto di glicogeno dal fegato al muscolo dopo lo sforzo",
        "La degradazione molto rapida del glicogeno durante lo sforzo intenso": "La degradazione molto rapida del glicogeno muscolare durante lo sforzo intenso"},
    "h4a-05": {"Le proteine bloccano la secrezione di insulina": "Le proteine bloccano la secrezione di insulina e quindi la sintasi", "Nessun amminoacido può essere convertito in glucosio": "Nessun amminoacido può essere convertito in glucosio nel fegato"},
    "h4a-06": {"L'adrenalina blocca la glicolisi dopo pochi secondi": "L'adrenalina blocca la glicolisi muscolare dopo pochi secondi di sforzo", "Il glicogeno non può essere degradato in anaerobiosi": "Il glicogeno non può essere degradato in anaerobiosi oltre il primo minuto"},
    "h4g-06": {"Assente in fegato e muscolo": "Assente sia nel fegato sia nel muscolo", "Normale ma in quantità enorme": "Normale nella struttura, ma in quantità enorme"},
    "h4g-07": {"Ia: lisosomiale; Ib: citosolica": "Ia: forma lisosomiale; Ib: forma citosolica dell'enzima", "Ia: autosomica; Ib: mitocondriale": "Ia: ereditarietà autosomica; Ib: ereditarietà mitocondriale"},
    "h5f-04": {"Solo negli eritrociti": "Solo negli eritrociti e nel cervello", "Cervello e midollo spinale": "Cervello (90%) e midollo spinale (10%)"},
    "h5f-06": {"Solo fegato": "Solo fegato, sugli enzimi", "Muscolo e cervello": "Muscolo, cervello e pancreas"},
    "h5r-03": {"Il malato è il vero substrato della PEPCK citosolica": "Il malato è il vero substrato della PEPCK citosolica, non l'ossalacetato", "Il malato è più energetico e spinge la reazione della PEPCK": "Il malato è più energetico e spinge la reazione della PEPCK verso il PEP"},
    "h5g-01": {"Come acetil-CoA, che attiva la piruvato carbossilasi": "Come acetil-CoA, che attiva la piruvato carbossilasi nel mitocondrio", "Come piruvato, dopo la transaminazione nel mitocondrio": "Come piruvato, dopo la transaminazione nel mitocondrio epatico"},
    "h5g-03": {"Il glicerolo entra nel Krebs come succinato": "Il glicerolo entra nel Krebs come succinato e dà ossalacetato", "Gli acidi grassi non vengono ossidati nel fegato": "Gli acidi grassi non vengono ossidati nel fegato ma solo nel muscolo"},
    "h5g-07": {"Lo elimina con le urine": "Lo elimina con le urine attraverso il rene", "Lo accumula come glicogeno": "Lo accumula come glicogeno cardiaco di riserva"},
    "h5n-01": {"È regolato solo dal glucosio, non da insulina e glucagone": "È regolato solo dal glucosio, non da insulina e glucagone, in entrambe le fasi", "A digiuno produce più F2,6BP per sostenere la gluconeogenesi": "A digiuno produce più F2,6BP, che sostiene la gluconeogenesi nel fegato"},
    "h5n-03": {"GRE e IRE": "GRE, IRE e SRE", "Solo l'IRE": "IRE, SRE e HRE"},
    "h5n-04": {"Perché la PK attiva la PEPCK": "Perché la PK attiva la PEPCK e la consuma", "Perché la PK consuma PEP solo nel muscolo": "Perché la PK consuma il PEP solo nel muscolo e non nel fegato"},
    "h5n-06": {"Inibisce la PEPCK mitocondriale": "Inibisce la PEPCK e attiva la PDH", "Attiva la piruvato chinasi epatica": "Attiva la piruvato chinasi epatica e la PDH"},
    "h5n-07": {"Sintasi ↑, PK epatica ↑, F2,6BP ↑": "Fosforilasi ↓, sintasi ↑, PK epatica ↑, F2,6BP ↑", "PEPCK ↓ e glicolisi ↑, per produrre ATP": "Fosforilasi ↑, sintasi ↑, PEPCK ↓, glicolisi ↑"},
    "h5a-01": {"L'etanolo attiva la glicogeno sintasi e sottrae glucosio": "L'etanolo attiva la glicogeno sintasi e sottrae glucosio al sangue durante la notte", "L'etanolo stimola la secrezione di insulina dalle cellule β": "L'etanolo stimola la secrezione di insulina dalle cellule β anche a digiuno"},
    "h5a-02": {"Perché aumenta l'insulina, che blocca la PEPCK": "Perché aumenta l'insulina, che blocca la PEPCK; il cervello usa lattato", "Perché il cervello smette di consumare energia": "Perché il cervello smette di consumare glucosio; il muscolo usa acidi grassi"},
    "h5a-03": {"Tutti gli epatociti fanno le stesse vie con la stessa intensità": "Tutti gli epatociti fanno le stesse vie con la stessa intensità, senza zonazione", "Solo i perivenosi fanno gluconeogenesi, perché hanno più ossigeno": "Solo i perivenosi fanno gluconeogenesi e urea, perché ricevono più ossigeno"},
    "h5a-06": {"Migliora per l'effetto antinfiammatorio sul pancreas": "Migliora, per l'effetto antinfiammatorio sulle isole del pancreas", "Ipoglicemia per aumento della secrezione di insulina": "Ipoglicemia, per aumento della secrezione di insulina dalle cellule β"},
    "h6r-04": {"La G6PD, dosabile con il NADPH": "La G6PD, dosabile con il NADPH negli eritrociti", "La 6-fosfogluconato deidrogenasi": "La 6-fosfogluconato deidrogenasi, dosabile nel fegato"},
    "h6r-05": {"Usa la gluconeogenesi per ottenere il ribosio": "Usa la gluconeogenesi per ottenere il ribosio dal piruvato", "Converte il NADPH in eccesso in ribosio 5-fosfato": "Converte il NADPH in eccesso in ribosio 5-fosfato con una reduttasi"},
    "h6r-07": {"Diventano glicogeno": "Diventano glicogeno nell'adipocita", "Si accumulano come ribosio 5-fosfato": "Si accumulano come ribosio 5-fosfato nel citosol"},
    "h6r-08": {"Il NADPH porta 4 elettroni invece di 2": "Il NADPH porta 4 elettroni invece di 2: serve alle biosintesi", "Il NADPH si trova solo nel mitocondrio": "Il NADPH si trova solo nel mitocondrio: i pool sono separati"},
    "h6n-01": {"Le fave causano una carenza acuta di ferro e folati": "Le fave causano una carenza acuta di ferro e folati, che blocca l'eritropoiesi", "Le fave bloccano la sintesi dell'emoglobina nei reticolociti": "Le fave bloccano la sintesi dell'emoglobina nei reticolociti, che si lisano"},
    "h6n-05": {"Serve a sintetizzare gli anticorpi": "Serve a sintetizzare gli anticorpi nel fagolisosoma", "Serve a ridurre il glutatione dei batteri": "Serve a ridurre il glutatione dei batteri fagocitati"},
    "h6n-06": {"Il P450 rende le sostanze più idrofobiche": "Rendendo le sostanze più idrofobiche, come il benzopirene", "Il P450 consuma tutto il NADPH della cellula": "Consumando tutto il NADPH della cellula epatica"},
    "x1c-01": {"A ossidare gli acidi grassi del tessuto adiposo": "A ossidare gli acidi grassi del tessuto adiposo, che vengono liberati", "A ridurre l'ossigeno nel citosol per produrre calore": "A ridurre l'ossigeno nel citosol per produrre calore dopo il pasto"},
    "x1c-03": {"Viene immagazzinata nel muscolo come glutammina": "Viene immagazzinata nel muscolo come glutammina di riserva", "Diventa nitrato e viene eliminata con il sudore": "Diventa nitrato nel fegato e viene eliminata con il sudore"},
    "x1c-04": {"Glicogeno, che viene trasformato in fosfolipidi": "Glicogeno e glucosio, che vengono trasformati in fosfolipidi", "Corpi chetonici, precursori diretti dei fosfolipidi": "Corpi chetonici e acetone, precursori diretti dei fosfolipidi"},
    "x1e-01": {"Aumenta sia KM sia Vmax": "Aumenta sia la KM sia la Vmax apparenti", "Diminuisce la Vmax, KM invariata": "Diminuisce la Vmax apparente, KM invariata"},
    "x2n-01": {"La membrana mitocondriale esterna è impermeabile al NADH": "La membrana mitocondriale esterna è impermeabile al NADH, quella interna no", "Entra liberamente, ma la sbobina usa le navette per semplificare": "Entra liberamente, ma la sbobina usa le navette per semplificare lo schema"},
    "x2n-04": {"Nel citosol, legata alla membrana mitocondriale esterna": "Nel citosol, legata alla membrana mitocondriale esterna, e riduce il NAD⁺", "Nella membrana esterna, dove cede elettroni al citocromo c": "Nella membrana esterna, dove cede elettroni al citocromo c tramite FMN"},
    "x3r-02": {"Attiva la piruvato deidrogenasi e il ciclo di Krebs": "Attiva la piruvato deidrogenasi, il ciclo di Krebs e la catena respiratoria", "Aumenta la PDH fosfatasi e la sintesi di ATP mitocondriale": "Aumenta la PDH fosfatasi e la sintesi di ATP mitocondriale con COX4-1"},
    "x3m-01": {
        "Insulina → GLUT4 → glucosio → ATP ↑ → chiusura canali Ca²⁺ → esocitosi": "Insulina → GLUT4 → glucosio → glicolisi → ATP ↑ → chiusura canali Ca²⁺ → iperpolarizzazione → esocitosi",
        "Glucosio (GLUT2) → glicolisi → ATP ↑ → apertura canali K⁺ → ingresso di Na⁺ → esocitosi": "Glucosio (GLUT2) → glicolisi e Krebs → ATP ↑ → apertura canali K⁺ → ingresso di Na⁺ → esocitosi"},
    "x3m-03": {"È avvolto negli istoni, che producono radicali": "È avvolto negli istoni, che producono radicali durante la replicazione", "Si replica solo una volta nella vita della cellula": "Si replica solo una volta nella vita della cellula e non si ripara"},
    "x4d-02": {"Il glucosio 1-P produce due molecole di 1,3-BPG in più": "Il glucosio 1-P produce due molecole di 1,3-BPG in più: 4 ATP netti invece di 2", "Il glucosio del glicogeno salta la fosfofruttochinasi e quindi un ATP": "Il glucosio del glicogeno salta la fosfofruttochinasi e quindi un ATP: 3 netti"},
    "x4s-01": {"È un caso dell'evoluzione, senza vantaggi per la cellula": "È un caso dell'evoluzione, senza vantaggi per la cellula: una sola via basterebbe", "Sintesi e degradazione avvengono in organelli diversi della cellula": "Sintesi e degradazione avvengono in organelli diversi della cellula (RE e lisosomi)"},
    "x4s-02": {"Sulla glicogenina": "Sulla glicogenina centrale", "Sull'estremità riducente": "Sulle estremità riducenti libere"},
    "x4s-03": {"CTP, dalla CTP sintetasi": "CTP, dalla CTP sintetasi citosolica", "ATP, dall'adenilato chinasi": "ATP, dall'adenilato chinasi (miochinasi)"},
    "x4o-02": {"Aumenta il cAMP, che attiva la sintasi tramite PKA": "Aumenta il cAMP, che attiva la sintasi tramite la PKA e la PP1", "Aumenta GLUT2 in membrana e attiva GSK3, che fosforila la sintasi": "Aumenta GLUT2 in membrana e, tramite PKB, attiva GSK3: la sintasi è fosforilata"},
    "x4e-01": {"È una malattia da accumulo di glicogeno nel muscolo degli atleti": "È una malattia da accumulo di glicogeno nel muscolo degli atleti, dovuta a un deficit enzimatico", "Il glicogeno resta sempre alto, qualunque sia la dieta o lo sforzo": "Il glicogeno resta sempre alto, qualunque sia la dieta o lo sforzo, per adattamento genetico"},
    "x4e-02": {"Nessuno, perché lo sforzo leggero usa solo fosfocreatina": "Nessuno, perché lo sforzo leggero usa solo fosfocreatina e ATP", "Solo quello epatico, mentre quello muscolare resta intatto": "Solo quello epatico, mentre quello muscolare resta del tutto intatto"},
    "x4e-03": {"Solo la sera, perché di notte la sintesi è più rapida": "Solo la sera, perché di notte la sintesi di glicogeno è più rapida", "Mai, perché bastano le proteine a ricostituire il glicogeno": "Mai, perché bastano le proteine a ricostituire il glicogeno muscolare"},
    "x4e-04": {"Lipogenesi aerobia e anaerobia": "Lipogenesi aerobia e anaerobia (sintesi)", "Glicogenosintesi aerobia e anaerobia": "Glicogenosintesi aerobia e anaerobia (muscolo)"},
    "x4g-01": {"Il glucagone attiva la glicolisi invece della glicogenolisi": "Il glucagone attiva la glicolisi epatica invece della glicogenolisi, e il G6P viene consumato", "Il glucagone non viene prodotto perché le cellule α sono distrutte": "Il glucagone non viene prodotto, perché le cellule α del pancreas sono distrutte dal glicogeno"},
    "x5f-01": {"Circa 500 g, metà dal fegato": "Circa 500 g, di cui metà dal fegato", "Circa 20 g, tutto dagli eritrociti": "Circa 20 g, quasi tutto dagli eritrociti"},
    "x5f-02": {"Si attiva la sintesi di glicogeno, che continua fino alla colazione": "Si attiva la sintesi di glicogeno, che continua fino alla colazione del mattino", "Entrambe si azzerano, perché di notte il consumo di glucosio è nullo": "Entrambe si azzerano, perché di notte il consumo di glucosio è praticamente nullo"},
    "x5g-01": {"Glicerolo fosfatasi e aldolasi B epatica": "Glicerolo fosfatasi e aldolasi B epatica (citosolica)", "Trioso fosfato isomerasi e PEPCK citosolica": "Trioso fosfato isomerasi e PEPCK citosolica del fegato"},
    "x5g-02": {"Dall'ossalacetato, tramite la PEPCK": "Dall'ossalacetato, tramite la PEPCK, saltando la piruvato carbossilasi", "Dal glucosio 6-P, saltando la fruttosio 1,6-bisfosfatasi": "Dal glucosio 6-P, saltando la fruttosio 1,6-bisfosfatasi e l'aldolasi"},
    "x5g-04": {"Il lattato non entra nel muscolo, quindi va per forza al fegato": "Il lattato non può entrare nel muscolo, quindi va per forza al fegato per essere ossidato", "Nel fegato NAD⁺/NADH è basso, e la LDH riduce il piruvato a lattato": "Nel fegato NAD⁺/NADH è basso, e la LDH riduce il piruvato a lattato prima della gluconeogenesi"},
    "x5a-04": {"Le cellule di Kupffer prendono il posto degli epatociti periportali": "Le cellule di Kupffer prendono il posto degli epatociti periportali e ne assumono le funzioni", "Il lobulo smette di fare gluconeogenesi finché il danno non si ripara": "Il lobulo smette di fare gluconeogenesi e urea finché il danno non si è riparato"},
    "x6g-01": {"Non cambia, perché la via dipende solo dal glucosio": "Non cambia, perché la via dipende solo dal glucosio e non dal NADPH", "Accelera solo la fase non ossidativa, per produrre ribosio": "Accelera solo la fase non ossidativa, per produrre ribosio e non NADPH"},
})
