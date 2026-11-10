"""Domande HARD (livello h), modulo 2: ingresso del glucosio, glicolisi, fermentazioni, navette, PDH (pp. 31–73)."""
from bank_common import q

T = "m2-ingresso"
q("h2i-01", T, "h", "31–32", "Perché l'assorbimento del glucosio da parte di SGLT1 è considerato un trasporto attivo secondario?", [
  'Sfrutta il gradiente di Na⁺ creato dalla Na⁺/K⁺-ATPasi, senza idrolizzare ATP',
  "Idrolizza una molecola di ATP per ogni glucosio che porta dentro l'enterocita",
  'Trasporta il glucosio secondo il suo gradiente, senza alcun costo energetico',
  "È attivato dall'insulina, che lo porta sulla membrana apicale dopo il pasto",
  'Trasporta il glucosio in simporto con il K⁺, che entra secondo gradiente',
  ], 0,
  "Il glucosio entra contro gradiente, il Na⁺ secondo gradiente; l'ATP lo consuma la pompa Na⁺/K⁺ basolaterale.",
  note="Sbobina di Biochimica II, p. 31: il trasportatore è chiamato «SGLUT1» e se ne dice prima che «utilizza ATP», poi che nel simporto «non c'è utilizzo di ATP». La sigla corretta è SGLT1, ed è un trasporto attivo secondario: l'ATP lo consuma la pompa Na⁺/K⁺, non SGLT1.")
q("h2i-02", T, "h", "33–34", "La glicemia passa da 5 mM (digiuno) a 15 mM (dopo un pasto). In quale tessuto aumenta di più, in proporzione, l'ingresso di glucosio, senza bisogno di insulina?", [
  'Fegato (GLUT2, Kt ≈ 17 mM), lontano dalla saturazione',
  'Cervello (GLUT3, Kt ≈ 0,1 mM), che è il tessuto più avido',
  'Eritrocita (GLUT1, Kt ≈ 3 mM), sempre esposto al plasma',
  "Muscolo a riposo (GLUT4), indipendente dall'insulina",
  'Tessuto adiposo (GLUT4), sensibile alla sola glicemia',
  ], 0,
  "Un trasportatore con Kt alta lavora lontano dalla saturazione: il flusso cresce quasi in proporzione alla glicemia. Con Kt bassa è già quasi saturo a digiuno; GLUT4 dipende dall'insulina.")
q("h2i-03", T, "h", "35–36", "Paziente iperglicemico con peptide C plasmatico normale-alto. L'ipotesi più probabile è:", [
  "Insulino-resistenza: l'insulina c'è ma non espone i GLUT4",
  'Distruzione autoimmune delle cellule β (diabete tipo 1)',
  'Eccesso di somatostatina che blocca la secrezione di insulina',
  'Deficit di GLUT2 epatico che impedisce la captazione postprandiale',
  'Insulinoma, che produce peptide C senza insulina attiva',
  ], 0,
  "Il peptide C è secreto in quantità equimolare all'insulina endogena: indica che le cellule β la producono. È il quadro del diabete tipo 2.")
q("h2i-04", T, "h", "34–35", "Nella cellula β, quale evento lega direttamente il metabolismo del glucosio alla secrezione di insulina?", [
  "L'aumento di ATP/ADP chiude i canali K⁺-ATP e depolarizza la cellula",
  'Il glucosio si lega a un recettore di membrana accoppiato a proteina G',
  "Il G6P apre i canali del Na⁺ e l'ingresso di Na⁺ causa l'esocitosi",
  "Il glucagone delle cellule α vicine stimola direttamente l'esocitosi",
  "L'AMP prodotto dalla glicolisi attiva la fusione delle vescicole",
  ], 0,
  'Depolarizzazione → apertura dei canali del Ca²⁺ → esocitosi. Il glucosio entra con GLUT2 e la glucochinasi fa da sensore.')
q("h2i-05", T, "h", "35", "Nella maturazione dell'insulina, quale sequenza è corretta?", [
  'Peptide segnale rimosso → ponti disolfuro → taglio del peptide C',
  'Taglio del peptide C → ponti disolfuro → rimozione del peptide segnale',
  'Ponti disolfuro → rimozione del peptide segnale → taglio della catena A',
  'Taglio del peptide C → rimozione del peptide segnale → ponti disolfuro',
  'Rimozione del peptide segnale → taglio del peptide C → ponti disolfuro',
  ], 0,
  'Preproinsulina → proinsulina → insulina (catene A e B). I ponti si formano prima del taglio, quando il peptide C tiene vicine le due catene.',
  note="Sbobina di Biochimica II, p. 35: c'è scritto «due ponti disolfuro intercatena e un ponte disolfuro intercatena». Sono due intercatena (tra A e B) e uno intracatena (dentro la catena A).")
q("h2i-06", T, "h", "36", "Il fruttosio della dieta raggiunge il fegato. Quale trasportatore NON lo trasporta efficacemente?", [
  'GLUT1',
  'GLUT2',
  'GLUT4',
  'Tutti lo trasportano allo stesso modo',
  'Nessuno: il fruttosio entra per diffusione',
  ], 0,
  "Secondo la sbobina il fruttosio entra con GLUT2 e GLUT4, non con GLUT1. Non è nelle sbobine, ma il trasportatore specifico del fruttosio nell'intestino è GLUT5.")
q("h2i-07", T, "h", "32", "Perché il cervello riceve glucosio anche quando la glicemia scende vicino a 3 mM?", [
  'GLUT1 della barriera e GLUT3 dei neuroni hanno Kt bassa',
  'Il cervello usa GLUT2, che lavora meglio a glicemie basse',
  "L'insulina aumenta i GLUT del cervello durante il digiuno",
  'Il cervello produce glucosio con la gluconeogenesi',
  'Il glucosio attraversa la barriera per semplice diffusione',
  ], 0,
  'GLUT3 ha Kt ≈ 0,1 mM: è saturato anche a glicemie basse, così il neurone è protetto dalle variazioni di glicemia.')
q("h2i-08", T, "h", "35", "Come agisce l'insulina sull'ingresso di glucosio nel muscolo?", [
  'Porta in membrana i GLUT4 contenuti in vescicole intracellulari',
  'Attiva la trascrizione del gene GLUT1 nel muscolo',
  "Aumenta l'affinità dei GLUT4 già presenti in membrana",
  'Fosforila il glucosio sulla faccia esterna della membrana, così il glucosio non può più uscire',
  'Aumenta il gradiente di Na⁺ sfruttato dal GLUT4',
  ], 0,
  "Cambia il numero di trasportatori in membrana, non la loro Kt. Quando l'insulina cala i GLUT4 vengono reinternalizzati per endocitosi.",
  note="Sbobina di Biochimica II, p. 34: c'è scritto che i GLUT4 hanno affinità molto alta per il glucosio e possono prenderlo «anche a livello basale», e che l'insulina ne favorisce «la presenza». Il punto chiave è che senza insulina i GLUT4 sono quasi tutti nelle vescicole, non in membrana.")

T = "m2-fosforilazione"
q("h2f-01", T, "h", "37", "Esochinasi (KM ≈ 0,1 mM) e glucochinasi (KM ≈ 10 mM) hanno Vmax simili. Con glicemia di 5 mM:", [
  'Esochinasi quasi saturata; glucochinasi a circa un terzo della Vmax',
  'Entrambe lavorano vicino alla loro velocità massima',
  'La glucochinasi è più veloce perché ha la KM più alta',
  "L'esochinasi è inibita dal glucosio, mentre la glucochinasi lavora alla velocità massima",
  'Entrambe lavorano a circa metà della loro Vmax',
  ], 0,
  "5/(10+5) ≈ 0,33. La glucochinasi accelera solo quando la glicemia sale dopo il pasto: il fegato capta glucosio quando ce n'è in eccesso.",
  note="Sbobina di Biochimica II, p. 37: compare «Il glucosio viene definito come organo generoso». È il fegato a essere definito organo generoso.")
q("h2f-02", T, "h", "55–56", "Dopo un pasto ricco di carboidrati la glucochinasi epatica viene attivata. Qual è il meccanismo?", [
  "Il glucosio la libera dalla GKRP e l'enzima torna nel citosol",
  'Il G6P la attiva allostericamente come effettore positivo',
  "L'insulina la defosforila tramite la proteina fosfatasi 1",
  'Il fruttosio 6-fosfato la porta dal nucleo al citosol',
  "L'ATP ne riduce la KM come effettore omotropico",
  ], 0,
  'La GKRP la tratteneva inattiva nel nucleo. Il fruttosio 6-fosfato favorisce invece il legame con la GKRP e il sequestro nel nucleo.',
  note="Sbobina di Biochimica II, p. 56: nel riepilogo delle differenze il glucosio è indicato come «effettore allosterico negativo» della glucochinasi, mentre una pagina prima è positivo. Per la glucochinasi il glucosio è un attivatore (stacca la GKRP); è un effettore negativo della sola GKRP.")
q("h2f-03", T, "h", "55", "Perché l'esochinasi è inibita dal G6P mentre la glucochinasi epatica no?", [
  'Il fegato deve fosforilare glucosio anche con G6P alto, per fare glicogeno',
  "Perché la glucochinasi non produce G6P ma fruttosio 6-fosfato, che non inibisce l'enzima",
  'Nel fegato il G6P esce subito con i GLUT2',
  'La glucochinasi è già inibita dal glucosio',
  "L'esochinasi lavora solo nel mitocondrio",
  ], 0,
  'Dopo i pasti il fegato immagazzina glucosio; gli altri tessuti fosforilano solo quanto consumano. Regolazioni diverse riflettono ruoli diversi.')
q("h2f-04", T, "h", "55", "Durante la catalisi l'esochinasi si chiude attorno a glucosio e ATP (adattamento indotto). Quale vantaggio dà?", [
  "Esclude l'acqua, evitando l'idrolisi improduttiva dell'ATP",
  "Aumenta il ΔG°' della reazione rendendola più favorita",
  'Permette di legare il G6P come attivatore allosterico',
  'Fa entrare nel sito attivo il magnesio libero',
  "Rende la reazione reversibile come quelle all'equilibrio",
  ], 0,
  "L'acqua competerebbe con il glucosio come accettore del fosfato γ.")
q("h2f-05", T, "h", "56", "Un soggetto con mutazione inattivante eterozigote della glucochinasi (MODY2). Che cosa ti aspetti?", [
  'Iperglicemia lieve a digiuno, per soglia di rilevazione più alta',
  'Ipoglicemia grave per eccesso di secrezione di insulina',
  "Nessuna alterazione della glicemia, perché l'esochinasi epatica compensa del tutto il difetto",
  'Accumulo di glicogeno epatico con epatomegalia',
  'Assenza totale di insulina, come nel diabete tipo 1',
  ], 0,
  'Non è nelle sbobine, ma segue dal ruolo della glucochinasi come sensore del glucosio in cellule β e fegato.')
q("h2f-06", T, "h", "37", "Perché la fosforilazione intrappola il glucosio nella cellula?", [
  'Il G6P è carico e non è riconosciuto dai GLUT',
  'Il G6P è troppo grande per passare dai GLUT',
  'Il G6P si lega alla membrana plasmatica',
  'Il G6P diventa subito glicogeno in tutte le cellule',
  'Il G6P è insolubile e precipita nel citosol',
  ], 0,
  'Può uscire solo dopo idrolisi da parte della glucosio 6-fosfatasi (fegato, rene). Per questo il muscolo non cede glucosio al sangue.')
q("h2f-07", T, "h", "56", "Quale differenza di specificità tra esochinasi e glucochinasi crea un problema al fegato?", [
  'La glucochinasi è specifica per il glucosio: servono enzimi per fruttosio e galattosio',
  "L'esochinasi è specifica per il glucosio: il muscolo non può usare il fruttosio della dieta",
  'La glucochinasi fosforila il fruttosio in C6 e il galattosio in C1',
  'Entrambe fosforilano solo il mannosio quando il glucosio è basso',
  'Non ci sono differenze di specificità tra i due enzimi',
  ], 0,
  "Fruttosio e galattosio arrivano al fegato con la vena porta e richiedono fruttochinasi e galattochinasi. L'esochinasi fosforila diversi esosi.")
q("h2f-08", T, "h", "37", "Quale NON è un destino del G6P in un epatocita?", [
  'Uscire dalla cellula come G6P tramite GLUT2',
  'Entrare nella glicolisi',
  'Diventare glicogeno',
  'Entrare nella via dei pentoso fosfati',
  'Essere idrolizzato a glucosio libero dalla glucosio 6-fosfatasi',
  ], 0,
  'Il G6P è un crocevia; esce solo dopo essere stato defosforilato dalla glucosio 6-fosfatasi.')

T = "m2-glicolisi"
q("h2g-01", T, "h", "43", "Lo iodoacetato alchila le cisteine. Quale tappa della glicolisi blocca e quale intermedio si accumula?", [
  'GAP deidrogenasi: si accumulano GAP e DHAP',
  'Enolasi: si accumula 2-fosfoglicerato',
  'Piruvato chinasi: si accumula fosfoenolpiruvato',
  'Aldolasi: si accumula fruttosio 1,6-bisfosfato',
  'Esochinasi: si accumula glucosio libero',
  ], 0,
  "Il tiolato della cisteina del sito attivo attacca l'aldeide formando un tioemiacetale; se è alchilato la reazione si ferma e la cellula non produce ATP glicolitico netto.")
q("h2g-02", T, "h", "43–44", "L'arseniato (AsO₄³⁻) sostituisce il Pi nella reazione della GAP deidrogenasi formando 1-arseno-3-fosfoglicerato, che si idrolizza spontaneamente. Conseguenza?", [
  "Si forma NADH ma non l'ATP della fosfoglicerato chinasi",
  'La glicolisi si blocca alla GAP deidrogenasi e si accumula la GAP',
  'Si produce più ATP del normale',
  'Non si forma NADH ma si forma ATP',
  'Si blocca la piruvato chinasi',
  ], 0,
  "Il guadagno netto di ATP diventa zero. Non è nelle sbobine, ma si ragiona sul meccanismo: l'energia del legame acil-fosfato va persa.")
q("h2g-03", T, "h", "39–45", "Quante reazioni della glicolisi sono ossidoriduzioni e quale ossida il glucosio?", [
  'Una sola: la GAP deidrogenasi',
  'Due: GAP deidrogenasi e piruvato chinasi',
  'Tre: esochinasi, PFK1 e piruvato chinasi',
  'Nessuna: la glicolisi non ossida il glucosio',
  "Una sola: l'enolasi",
  ], 0,
  "La GAP deidrogenasi ossida l'aldeide ad acil-fosfato riducendo il NAD⁺. L'enolasi è una deidratazione, isomerasi e mutasi sono riarrangiamenti.")
q("h2g-04", T, "h", "41–42", "L'aldolasi ha ΔG°' ≈ +24 kJ/mol. Perché nella cellula la reazione procede verso i triosi?", [
  'I triosi sono consumati e restano bassi: il ΔG reale va a circa 0',
  "L'aldolasi è regolata allostericamente dal fruttosio 2,6-bisfosfato",
  "La reazione è accoppiata all'idrolisi di una molecola di ATP",
  "L'enzima abbassa il ΔG°' fino a renderlo negativo",
  "La PFK1 e l'aldolasi formano un'unica reazione accoppiata",
  ], 0,
  "Inoltre da un reagente si formano due prodotti, quindi il termine di concentrazione abbassa molto il ΔG. Nell'eritrocita il ΔG reale è circa −0,2 kJ/mol.")
q("h2g-05", T, "h", "47", "Correggendo i ΔG°' con le concentrazioni reali dell'eritrocita, quale reazione che sembrava irreversibile risulta vicina all'equilibrio?", [
  'Fosfoglicerato chinasi',
  'Esochinasi',
  'Fosfofruttochinasi 1',
  'Piruvato chinasi',
  'Nessuna: le irreversibili restano quattro',
  ], 0,
  "Ha ΔG°' negativo ma ΔG reale ≈ 0: per questo funziona anche nella gluconeogenesi.")
q("h2g-06", T, "h", "45–46", "Perché l'idrolisi del PEP ha un ΔG°' (≈ −62 kJ/mol) più negativo di quella dell'ATP?", [
  "L'enolpiruvato prodotto tautomerizza subito alla forma chetonica, più stabile",
  'Il PEP contiene due legami fosfoanidridici in successione',
  'Il PEP contiene un legame tioestere tra fosfato e piruvato',
  'Il piruvato ha più cariche negative del PEP e si stabilizza',
  "La reazione è accoppiata all'idrolisi di una molecola di ATP che resta legata nel sito attivo",
  ], 0,
  "È l'esempio A ⇒ B ⇒ C della sbobina: la forma enolica viene continuamente sottratta.")
q("h2g-07", T, "h", "45", "Una fosfoglicerato mutasi priva del fosfato sull'istidina del sito attivo è inattiva. Come viene riattivata?", [
  'Dal 2,3-bisfosfoglicerato, che le cede un fosfato',
  "Dall'ATP, tramite una chinasi dedicata",
  'Dal GTP prodotto nel ciclo di Krebs',
  'Dal fosfato inorganico presente nel citosol',
  'Dal fosfoenolpiruvato tramite la piruvato chinasi',
  ], 0,
  "L'enzima fosforilato passa il fosfato al C2 e lo riprende dal C3, attraverso il 2,3-BPG intermedio.")
q("h2g-08", T, "h", "47", "Qual è il bilancio netto della glicolisi per una molecola di glucosio?", [
  'Glucosio → 2 piruvato + 2 NADH + 2 ATP netti',
  'Glucosio → 2 piruvato + 2 NADH + 4 ATP netti',
  'Glucosio → 2 lattato + 2 NADH + 2 ATP netti',
  'Glucosio → 2 piruvato + 2 NADPH + 2 ATP netti',
  'Glucosio → 2 piruvato + 2 FADH₂ + 2 ATP netti',
  ], 0,
  'Glucosio + 2 NAD⁺ + 2 ADP + 2 Pi → 2 piruvato + 2 NADH + 2 H⁺ + 2 ATP + 2 H₂O. 4 ATP prodotti, 2 investiti; i 2 H⁺ rendono la glicolisi acidificante.')

T = "m2-fermentazioni"
q("h2m-01", T, "h", "49", "Perché la cellula in anaerobiosi deve trasformare il piruvato in lattato pur non guadagnando ATP da questa reazione?", [
  'Per rigenerare il NAD⁺ necessario alla GAP deidrogenasi',
  'Per produrre ATP dalla riduzione del piruvato',
  'Per eliminare il piruvato, che è tossico per la cellula',
  'Per formare glucosio direttamente nel muscolo',
  'Per produrre CO₂ come nella fermentazione alcolica',
  ], 0,
  "Senza NAD⁺ la glicolisi si fermerebbe e con essa l'unica produzione di ATP. Nel citosol il rapporto NAD⁺/NADH è alto (circa 700).")
q("h2m-02", T, "h", "50", "L'isoenzima H₄ della LDH (cuore) ha una KM per il piruvato più alta dell'M₄ (muscolo scheletrico). Che cosa comporta?", [
  'Il cuore tende a ossidare il lattato, il muscolo a produrlo',
  'Il cuore produce più lattato del muscolo scheletrico',
  "L'isoenzima H₄ è inattivo e il cuore non usa il lattato",
  "L'isoenzima M₄ non riconosce il piruvato come substrato",
  'Il cuore converte il piruvato in etanolo',
  ], 0,
  "Il cuore usa il lattato come combustibile; il muscolo riduce rapidamente il piruvato durante lo sforzo. Non è nelle sbobine che l'H₄ è inibito da alte concentrazioni di piruvato.")
q("h2m-03", T, "h", "51", "Nel ciclo di Cori, quale enzima trasforma nel fegato il lattato in piruvato e quale processo lo riconverte in glucosio?", [
  'La LDH epatica (soprattutto M₄), poi la gluconeogenesi',
  'La piruvato deidrogenasi, poi la glicolisi',
  'La LDH cardiaca (H₄), poi la glicogenolisi',
  'La piruvato carbossilasi, poi il ciclo di Krebs',
  'La lattato ossidasi, poi la via dei pentoso fosfati',
  ], 0,
  'Il fegato spende 6 legami ad alta energia per ogni glucosio riformato: il ciclo di Cori costa energia al fegato.',
  note="Sbobina di Biochimica II, p. 50: c'è scritto che fegato e rene hanno isoenzimi «intermedi». Il fegato ha soprattutto LDH-5 (M₄), come dice la stessa sbobina a p. 51; il rene soprattutto LDH-1 e LDH-2. La reazione è all'equilibrio: nel fegato, dove il piruvato viene consumato dalla gluconeogenesi, anche M₄ ossida il lattato.")
q("h2m-04", T, "h", "51–52", "Secondo l'impostazione del corso, la reazione della LDH che cosa fa al pH della cellula muscolare?", [
  "Consuma un H⁺: contrasta l'acidificazione",
  'Libera un H⁺: forma acido lattico',
  'Non ha alcun effetto sul pH',
  'Libera due H⁺ per ogni piruvato',
  'Libera CO₂, che forma acido carbonico e acidifica la cellula',
  ], 0,
  "Piruvato + NADH + H⁺ → lattato + NAD⁺. L'acidificazione deriva soprattutto dall'idrolisi dell'ATP. Il lattato esce poi con un H⁺ tramite l'MCT: acidifica il sangue, non la cellula.")
q("h2m-05", T, "h", "52", "Un paziente in shock settico ha lattato plasmatico alto. Quale meccanismo è più coerente?", [
  'Ipossia tissutale: il NADH non viene riossidato e il piruvato diventa lattato',
  'Eccesso di attività della PDH, che trasforma il piruvato in lattato direttamente nel mitocondrio',
  'Aumento della gluconeogenesi muscolare, che rilascia lattato',
  'Deficit di LDH, che impedisce lo smaltimento del lattato',
  'Eccesso di ossigeno nei tessuti, che ossida il piruvato a lattato',
  ], 0,
  'Ipossia, sepsi, anemia, intossicazione da CO e neoplasie sono cause di iperlattatemia.')
q("h2m-06", T, "h", "53", "Perché la decarbossilazione del piruvato ad acetaldeide nel lievito è irreversibile?", [
  'Perché si libera CO₂, che si allontana',
  'Perché consuma una molecola di ATP',
  "Perché è un'ossidoriduzione con NAD⁺",
  'Perché avviene nel mitocondrio del lievito',
  "Perché l'acetaldeide è un metabolita terminale",
  ], 0,
  'La seconda tappa (acetaldeide → etanolo, alcol deidrogenasi) è invece reversibile e rigenera il NAD⁺.')
q("h2m-07", T, "h", "53", "Dopo un forte consumo di alcol, perché può comparire ipoglicemia a digiuno?", [
  "Il NADH alto dell'ossidazione dell'etanolo blocca lattato → piruvato",
  "L'etanolo inibisce la secrezione di insulina dalle cellule β",
  "L'acetaldeide attiva la glucochinasi e il fegato capta tutto il glucosio rimasto nel sangue",
  "L'etanolo viene trasformato in glicogeno e sottrae glucosio",
  "L'etanolo blocca i GLUT4 del muscolo",
  ], 0,
  'Il rapporto NADH/NAD⁺ alto sposta lattato ⇌ piruvato verso il lattato e sottrae substrato alla gluconeogenesi.')
q("h2m-08", T, "h", "50", "Un paziente ha LDH plasmatica alta con aumento dell'isoenzima LDH-1 (H₄) a 48 ore da un dolore toracico. Interpretazione?", [
  'Infarto del miocardio, con LDH-1 come marker tardivo',
  'Strappo muscolare scheletrico, con LDH-5 come marker',
  'Epatite acuta, con LDH-5 come marker precoce',
  'Infarto del miocardio in atto da meno di due ore',
  'Emolisi intravascolare, con LDH-5 come marker',
  ], 0,
  "Troponina e CK-MB sono i marker precoci. La LDH nel sangue indica morte cellulare; il pattern isoenzimatico indica l'organo.")

T = "m2-navette"
q("h2n-01", T, "h", "53–54", "Perché la navetta del glicerolo 3-fosfato rende meno ATP della navetta malato-aspartato?", [
  'Gli elettroni entrano al coenzima Q tramite FAD, saltando il complesso I',
  'Consuma ATP per trasportare il glicerolo 3-fosfato nella matrice, abbassando la resa netta',
  'Trasferisce un solo elettrone per ogni NADH citosolico',
  'Riduce il NAD⁺ della matrice, che poi entra nel complesso II',
  'Produce NADPH invece di NADH nella matrice',
  ], 0,
  'Circa 1,5 ATP invece di circa 2,5 per NADH citosolico.')
q("h2n-02", T, "h", "54", "Nella navetta del glicerolo fosfato, quale reazione avviene nel citosol?", [
  'DHAP + NADH → glicerolo 3-fosfato + NAD⁺',
  'Glicerolo 3-fosfato + FAD → DHAP + FADH₂',
  'Malato + NAD⁺ → ossalacetato + NADH',
  'GAP + NAD⁺ + Pi → 1,3-BPG + NADH',
  'Glicerolo + ATP → glicerolo 3-fosfato + ADP',
  ], 0,
  'La riossidazione a DHAP avviene sulla faccia esterna della membrana interna, con il FAD.',
  note="Sbobina di Biochimica II, p. 54: c'è scritto che nella reazione della GAP deidrogenasi aumenta la produzione di GAP (in realtà la GAP si consuma) e il glicerolo 3-fosfato è abbreviato «3-PG», che è la sigla del 3-fosfoglicerato.")
q("h2n-03", T, "h", "53", "La membrana mitocondriale interna è impermeabile al NADH. Che cosa attraversa davvero la membrana nelle navette?", [
  'Gli elettroni, portati da molecole come glicerolo 3-P o malato',
  'Il NADH stesso, tramite un trasportatore specifico della membrana interna',
  'Il NAD⁺, scambiato con il NADH',
  'Il FADH₂ prodotto nel citosol',
  'Il piruvato, che porta con sé il NADH',
  ], 0,
  'I pool di NAD citosolico e mitocondriale restano separati.')
q("h2n-04", T, "h", "54", "Nella navetta malato-aspartato, perché l'ossalacetato rientra nel citosol come aspartato?", [
  "Non c'è un trasportatore per l'ossalacetato: esce come aspartato",
  "L'ossalacetato è tossico nella matrice e va subito eliminato",
  "L'aspartato serve a sintetizzare urea nella matrice",
  "È l'aspartato a trasportare gli elettroni nel citosol",
  "L'ossalacetato si decarbossila prima di poter uscire",
  ], 0,
  'Viene transaminato ad aspartato, che esce; nel citosol torna ossalacetato. Il dettaglio della navetta malato-aspartato non è nelle sbobine (Lehninger).')
q("h2n-05", T, "h", "53–54", "In una cellula muscolare in esercizio aerobico, perché il NADH citosolico non si accumula?", [
  'Le navette ne trasferiscono gli elettroni al mitocondrio',
  'Viene tutto convertito in lattato dalla LDH',
  'Attraversa liberamente la membrana mitocondriale interna',
  'Viene consumato dalla piruvato deidrogenasi',
  'In aerobiosi la glicolisi non produce NADH',
  ], 0,
  "La catena respiratoria cede gli elettroni all'O₂ e rigenera il NAD⁺. È il terzo modo (oltre a LDH e fermentazione alcolica) per far proseguire la glicolisi.")
q("h2n-06", T, "h", "54", "Quale enzima della navetta del glicerolo fosfato contiene il FAD e dove si trova?", [
  'La glicerolo 3-P deidrogenasi mitocondriale, sulla faccia esterna della membrana interna',
  'La glicerolo 3-P deidrogenasi citosolica, libera nel citosol',
  'La malato deidrogenasi mitocondriale, nella matrice',
  'La succinato deidrogenasi, sulla faccia della membrana interna rivolta verso la matrice',
  'La GAP deidrogenasi, nel citosol accanto alla membrana',
  ], 0,
  "L'isoforma citosolica usa il NADH; quella mitocondriale ha il FAD e cede gli elettroni al coenzima Q.")
q("h2n-07", T, "h", "53–54", "Se la catena respiratoria è bloccata, le navette continuano a riossidare il NADH citosolico?", [
  'No: le navette si fermano e resta solo la LDH',
  'Sì: sono indipendenti dalla catena respiratoria',
  'Sì, ma solo la navetta del glicerolo fosfato',
  "Sì, perché usano l'ATP glicolitico",
  'No, perché la glicolisi si blocca prima',
  ], 0,
  'Senza catena attiva FADH₂ e NADH mitocondriali non vengono riossidati. Per questo i veleni della catena respiratoria aumentano il lattato.')
q("h2n-08", T, "h", "54", "Quale navetta prevale nel muscolo scheletrico e nel cervello, e quale nel fegato e nel cuore?", [
  'Glicerolo fosfato in muscolo e cervello; malato-aspartato in fegato e cuore',
  'Malato-aspartato in muscolo e cervello; glicerolo fosfato in fegato e cuore',
  'Malato-aspartato in tutti i tessuti, senza differenze',
  'Glicerolo fosfato in tutti i tessuti, senza differenze',
  'Nessuna navetta nel cuore, che usa solo il lattato',
  ], 0,
  'Non è nelle sbobine (Lehninger): la navetta del glicerolo fosfato è più rapida ma rende meno.')

T = "m2-regolazione"
q("h2r-01", T, "h", "57–58", "Nella PFK1, che cosa cambia tra forma R e forma T nel sito di legame del F6P?", [
  "In R l'Arg 162 attira il F6P; in T il Glu 161 lo respinge",
  "In R il Glu 161 attira il F6P; in T l'Arg 162 lo respinge",
  'In T il sito attivo viene fosforilato dalla PKA',
  'In T il sito attivo lega più ATP e meno F6P',
  'Le due forme differiscono solo per la Vmax',
  ], 0,
  "L'Arg è positiva, il Glu negativo; il F6P ha due cariche negative. Gli effettori allosterici spostano l'equilibrio R ⇌ T.")
q("h2r-02", T, "h", "58–59", "Perché l'AMP è un segnale più sensibile dell'ATP per la PFK1?", [
  "Per l'adenilato chinasi, l'AMP varia molto più in percentuale dell'ATP",
  "Perché nel citosol l'AMP è molto più abbondante dell'ATP, soprattutto nel muscolo a riposo",
  "Perché l'AMP si lega al sito catalitico al posto del F6P",
  "Perché l'AMP è prodotto direttamente dalla PFK1",
  "Perché l'ATP non ha alcun effetto sulla PFK1",
  ], 0,
  "2 ADP ⇌ ATP + AMP. Nell'esempio della sbobina l'AMP passa da 0,02 a 0,07 mM (×3,5) mentre l'ATP scende solo del 5%.")
q("h2r-03", T, "h", "57–58", "L'ATP è substrato della PFK1 ma anche suo inibitore. Come si conciliano le due cose?", [
  'Ha anche un sito allosterico a bassa affinità, occupato solo ad ATP alto',
  'Inibisce solo quando è legato al magnesio',
  'È un inibitore competitivo del fruttosio 6-fosfato e ne occupa il sito di legame catalitico',
  "Inibisce solo l'isoforma epatica dell'enzima",
  "In realtà l'ATP non inibisce la PFK1",
  ], 0,
  "Il sito catalitico ha alta affinità; quando l'ATP è alto occupa anche il sito allosterico e stabilizza la forma T. È un effettore omotropico.")
q("h2r-04", T, "h", "59–60", "Quale è il più potente attivatore della PFK1 epatica e chi ne controlla la concentrazione?", [
  'Il F2,6BP, regolato da insulina e glucagone',
  'Il F1,6BP, regolato dalla piruvato chinasi',
  "L'AMP, regolato dal glucagone",
  "Il citrato, regolato dall'insulina",
  'Il glucosio, regolato dalla glucochinasi',
  ], 0,
  "Il F2,6BP è attivo a concentrazioni micromolari. L'insulina ne aumenta la sintesi, il glucagone la riduce tramite la PFK2/FBPasi2.")
q("h2r-05", T, "h", "60", "Perché il citrato citosolico inibisce la PFK1?", [
  'Esce dal mitocondrio quando ATP e NADH sono alti',
  'È un prodotto diretto della glicolisi citosolica',
  'Compete con il F6P nel sito catalitico',
  'Attiva una fosfatasi che defosforila la PFK1',
  "Riduce l'AMP tramite l'adenilato chinasi",
  ], 0,
  'Il citrato si accumula quando il ciclo di Krebs è rallentato: segnala che non serve altro acetil-CoA dalla glicolisi.')
q("h2r-06", T, "h", "60–61", "Il fruttosio 1,6-bisfosfato attiva la piruvato chinasi. Come si chiama questo tipo di regolazione e a che cosa serve?", [
  'Feed-forward: la tappa finale si prepara al flusso',
  'Inibizione a feedback da parte del prodotto finale',
  'Regolazione covalente tramite fosforilazione',
  'Inibizione da prodotto della PFK1',
  'Effetto omotropico del substrato',
  ], 0,
  "Quando la PFK1 è attiva, il F1,6BP attiva la piruvato chinasi ed evita l'accumulo di intermedi a valle.")
q("h2r-07", T, "h", "61", "A digiuno il glucagone fa fosforilare dalla PKA la piruvato chinasi epatica. Qual è l'effetto e a che cosa serve?", [
  'La PK epatica si inattiva e il PEP resta per la gluconeogenesi',
  'La PK epatica si attiva e la glicolisi del fegato produce più ATP per la gluconeogenesi',
  'La glicolisi accelera per produrre glucosio',
  'Si inattiva solo la PK muscolare',
  'Il PEP viene trasformato in glicogeno',
  ], 0,
  'Si evita il ciclo futile PEP → piruvato → ossalacetato → PEP.',
  note="Sbobina di Biochimica II, p. 61: c'è scritto che la fosforilazione della PK «rallenta la glicolisi e quindi riduce la produzione di glucosio». Riduce il consumo di glucosio e favorisce la sua produzione (gluconeogenesi). Inoltre a p. 62 ADP e acetil-CoA sono indicati come attivatori della PK, mentre a p. 60 l'acetil-CoA è un inibitore: l'acetil-CoA inibisce (Lehninger).")
q("h2r-08", T, "h", "54–60", "Quale delle tre tappe regolate è considerata il principale punto di controllo della glicolisi e perché?", [
  'La PFK1: il F1,6BP è il primo intermedio solo glicolitico',
  "L'esochinasi, perché è la prima reazione della via e consuma il primo ATP",
  "La piruvato chinasi, perché è l'ultima reazione",
  "La GAP deidrogenasi, perché è l'unica redox",
  "L'aldolasi, perché scinde l'esoso in due triosi",
  ], 0,
  "È la tappa di commissione. Il G6P invece ha altri destini (glicogeno, pentoso fosfati): controllare l'esochinasi non basta.")

T = "m2-pasteur"
q("h2p-01", T, "h", "62–63", "Lieviti in anaerobiosi vengono esposti all'ossigeno e il consumo di glucosio crolla. Qual è il meccanismo indicato nel corso?", [
  'ATP e citrato citosolico aumentano e inibiscono la PFK1',
  "L'ossigeno inattiva direttamente l'esochinasi ossidandone le cisteine",
  "L'ossigeno ossida il glucosio prima che entri",
  'Il NADH aumenta e attiva la glicolisi',
  "L'AMP aumenta e blocca la piruvato chinasi",
  ], 0,
  'La fosforilazione ossidativa produce molto ATP: da un glucosio se ne ricava molto di più, quindi ne serve meno.',
  note="Sbobina di Biochimica II, p. 63: la PFK1 è definita «l'enzima che catalizza la prima reazione della glicolisi». È la terza reazione; è la prima tappa specifica (di commissione).")
q("h2p-02", T, "h", "62", "Le cellule tumorali consumano molto glucosio e producono lattato anche in presenza di ossigeno. Come si chiama il fenomeno?", [
  'Effetto Warburg',
  'Effetto Pasteur',
  'Effetto Bohr',
  'Effetto Haldane',
  'Ciclo di Cori',
  ], 0,
  "Le cellule tumorali non mostrano l'effetto Pasteur. Vi contribuisce l'HIF, che aumenta la PDH chinasi e inibisce la PDH.")
q("h2p-03", T, "h", "63", "In un paziente con deficit di piruvato chinasi eritrocitaria, che cosa succede alla curva di dissociazione dell'O₂ e perché?", [
  'A destra: si accumula 2,3-BPG',
  'A sinistra: cala il 2,3-BPG',
  'Non cambia',
  'A destra: aumenta il lattato',
  "A sinistra: aumenta l'ATP",
  ], 0,
  "Il PEP si accumula, le reazioni a monte (all'equilibrio) aumentano l'1,3-BPG e quindi il 2,3-BPG, che riduce l'affinità dell'Hb per l'O₂.")
q("h2p-04", T, "h", "63–64", "Perché il deficit di piruvato chinasi causa anemia emolitica?", [
  'Con poco ATP la pompa Na⁺/K⁺ cede e la cellula perde la forma',
  "Si accumula lattato che acidifica la cellula e lisa la membrana dell'eritrocita",
  'Manca il NADPH e il glutatione non viene ridotto',
  "Aumenta l'affinità dell'Hb per l'O₂ e la cellula muore",
  "Si blocca la sintesi dell'eme nell'eritrocita maturo",
  ], 0,
  "L'eritrocita dipende solo dalla glicolisi: si rigonfia, perde la forma biconcava e viene eliminato dalla milza. È il deficit enzimatico glicolitico più frequente.")
q("h2p-05", T, "h", "63", "Quale enzima dell'eritrocita forma il 2,3-BPG e da quale intermedio?", [
  "Bisfosfoglicerato mutasi, dall'1,3-BPG",
  'Fosfoglicerato chinasi, dal 3-fosfoglicerato',
  'Enolasi, dal fosfoenolpiruvato',
  'GAP deidrogenasi, dalla gliceraldeide 3-P',
  'Fosfoglicerato mutasi, dal 2-fosfoglicerato',
  ], 0,
  "Il fosfato passa dal C1 al C2 (shunt di Rapoport-Luebering): l'eritrocita rinuncia a 1 ATP per ogni 1,3-BPG deviato.")
q("h2p-06", T, "h", "63", "Nel deficit di esochinasi eritrocitaria, che cosa ti aspetti?", [
  "Meno 2,3-BPG e Hb più affine all'O₂",
  "Più 2,3-BPG e Hb meno affine all'O₂",
  'Accumulo di PEP e anemia emolitica',
  "Aumento dell'ATP eritrocitario",
  "Nessun effetto sull'emoglobina",
  ], 0,
  'Se la glicolisi non parte si forma poco 1,3-BPG: curva a sinistra e minore cessione di O₂ ai tessuti.')
q("h2p-07", T, "h", "64", "Il fruttosio entra nella glicolisi epatica a valle della PFK1 (via fruttosio 1-fosfato). Perché un eccesso di fruttosio favorisce la lipogenesi?", [
  'Salta la PFK1: i triosi si formano senza controllo',
  'Inibisce la piruvato deidrogenasi epatica e devia il piruvato verso i lipidi',
  'Attiva la PFK1 più del glucosio',
  'Non produce piruvato ma solo glicerolo',
  'Entra solo in presenza di insulina',
  ], 0,
  'I triosi forniscono acetil-CoA e glicerolo 3-fosfato per i trigliceridi. La sbobina riporta queste pagine solo come immagini; il metabolismo del fruttosio è nel Lehninger.')
q("h2p-08", T, "h", "64", "Nella galattosemia classica (deficit di galattosio 1-fosfato uridiltransferasi), quale sostanza si accumula?", [
  'Galattosio 1-fosfato',
  'Glucosio 6-fosfato',
  'Fruttosio 1-fosfato',
  'UDP-glucosio',
  'Lattosio',
  ], 0,
  'Si accumula anche il galattitolo, che causa cataratta. La sbobina riporta queste pagine solo come immagini; il dettaglio è nel Lehninger.')

T = "m2-pdh"
q("h2d-01", T, "h", "66–69", "Un paziente con grave carenza di tiamina (beriberi, alcolismo). Quali enzimi sono compromessi e che cosa si accumula?", [
  'PDH e α-chetoglutarato deidrogenasi: si accumulano piruvato e lattato',
  'Solo la LDH: si accumula piruvato ma non lattato',
  'La citrato sintasi: si accumula acetil-CoA',
  'La piruvato carbossilasi, che usa la tiamina: si accumulano piruvato e alanina',
  'La succinato deidrogenasi: si accumula succinato',
  ], 0,
  "Il TPP è il coenzima di E1 di entrambi i complessi. Cala l'ATP aerobico, soprattutto nel sistema nervoso.")
q("h2d-02", T, "h", "69", "Perché nell'uomo gli acidi grassi non possono essere convertiti in glucosio netto?", [
  "La PDH è irreversibile e nel Krebs i 2 C dell'acetile escono come CO₂",
  'Gli acidi grassi nel fegato non producono acetil-CoA ma solo corpi chetonici',
  "Nell'uomo la gluconeogenesi non avviene nel fegato",
  "Nell'uomo manca la piruvato carbossilasi",
  "L'acetil-CoA inibisce la fruttosio 1,6-bisfosfatasi",
  ], 0,
  "L'acetil-CoA non può tornare a piruvato. Dagli zuccheri si fanno grassi, non il contrario (eccezione: il glicerolo dei trigliceridi).")
q("h2d-03", T, "h", "66–69", "Quale sequenza di eventi nella PDH è corretta?", [
  "E1 decarbossila; E2 trasferisce l'acetile al CoA; E3 riossida il lipoato",
  'E1 trasferisce al CoA; E2 decarbossila; E3 riduce il FAD',
  "E3 decarbossila; E2 ossida il lipoato con il FAD; E1 trasferisce l'acetile al CoA",
  "E1 riduce il NAD⁺; E2 decarbossila; E3 trasferisce l'acetile",
  "E2 decarbossila; E1 trasferisce l'acetile; E3 ossida il FADH₂",
  ], 0,
  'E1 (TPP): decarbossilazione; E2 (lipoammide): transacetilazione; E3 (FAD): ossidoriduzione, con riduzione finale del NAD⁺.',
  note="Sbobina di Biochimica II, pp. 68 e 70: la sbobina indica «Acido lipoico = E2» e «coenzima A (CoA-SH) (E3)» e descrive E2 come trimero ed E3 come «dimero αβ». Il CoA accetta l'acetile su E2 (transacetilasi), non su E3; E2 forma il nucleo del complesso (24 o più subunità organizzate in trimeri) ed E3 è un omodimero.")
q("h2d-04", T, "h", "69", "Qual è il vantaggio del braccio flessibile lipoil-lisina di E2?", [
  "Trasporta l'intermedio tra E1, E2 ed E3 senza che diffonda",
  'Lega il piruvato dal citosol e lo porta direttamente al sito attivo di E1',
  'Fosforila E1 per regolare il complesso',
  'Cede gli elettroni direttamente al NAD⁺',
  'Rende la reazione reversibile',
  ], 0,
  'È un channeling: reazione più veloce e intermedi reattivi protetti. Il lipoato è legato con legame ammidico a una lisina.')
q("h2d-05", T, "h", "71–72", "Nel muscolo che inizia a contrarsi, il Ca²⁺ attiva la PDH. Come?", [
  'Attiva la PDH fosfatasi, che defosforila E1',
  'Attiva la PDH chinasi, che fosforila E1',
  "Inibisce l'ingresso di piruvato nel mitocondrio",
  'Si lega al TPP e lo attiva',
  'Riossida il NADH della matrice',
  ], 0,
  'Il segnale della contrazione anticipa il fabbisogno di ATP.')
q("h2d-06", T, "h", "72", "In quale condizione la PDH chinasi è massimamente attiva (PDH inattiva)?", [
  'ATP/ADP, NADH/NAD⁺ e acetil-CoA/CoA alti, come a digiuno',
  'Alti livelli di piruvato e di ADP nella matrice',
  'Alto Ca²⁺ nel muscolo durante la contrazione',
  'Alta insulina dopo un pasto ricco di carboidrati, con molto piruvato disponibile',
  'Ipoglicemia con AMP alto in tutte le cellule',
  ], 0,
  "Durante l'ossidazione di acidi grassi la PDH viene spenta: si risparmiano piruvato e glucosio per la gluconeogenesi.",
  note="Sbobina di Biochimica II, p. 72: c'è scritto che l'AMP inibisce la PDH chinasi e il GTP la attiva. Nei testi il principale inibitore della chinasi è l'ADP (con piruvato), gli attivatori sono ATP, NADH e acetil-CoA. Non sono sicuro che il prof abbia detto «AMP» a lezione: all'esame meglio ragionare in termini di carica energetica.")
q("h2d-07", T, "h", "73", "Un bambino con acidosi lattica congenita, atassia e ritardo psicomotorio. Quale deficit enzimatico è più probabile?", [
  'Deficit della piruvato deidrogenasi (subunità E1)',
  'Deficit di lattato deidrogenasi',
  'Deficit di glucosio 6-fosfatasi',
  'Deficit di GLUT4',
  'Deficit di glicogeno fosforilasi muscolare (McArdle)',
  ], 0,
  'Il piruvato non viene ossidato e viene ridotto a lattato; il cervello, dipendente dal glucosio, è il più colpito. Non è nelle sbobine che si tratta con dieta chetogenica.')
q("h2d-08", T, "h", "73", "In un tumore ipossico, l'HIF aumenta la PDH chinasi. Quale conseguenza è corretta?", [
  'La PDH si inattiva e il piruvato diventa lattato',
  'La PDH si attiva e aumenta la produzione di CO₂',
  'Aumenta la β-ossidazione mitocondriale',
  'La glicolisi viene inibita',
  'Aumenta la fosforilazione ossidativa',
  ], 0,
  "La PDH chinasi fosforila e inattiva la PDH. È uno dei meccanismi dell'effetto Warburg.")
