"""Giro 2026-11-24, blocco 1 – Biochimica I, biologia molecolare: clonaggio genico (p. 260–269)
e PCR (p. 270–280). Argomenti finora scoperti."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Clonaggio genico (p. 260–269) ───────────────────────────────────────────
T = "d13-clonaggio"

q("u1124-001", T, "f", "261", "Qual è la sequenza corretta delle tappe del clonaggio?", [
  "Digestione, ligazione, trasformazione, piastramento, selezione",
  "Ligazione, digestione, piastramento, trasformazione, selezione",
  "Trasformazione, digestione, ligazione, selezione, piastramento",
  "Digestione, trasformazione, ligazione, selezione, piastramento",
  "Selezione, digestione, ligazione, trasformazione, piastramento",
  ], 0,
  "Prima si taglia DNA e vettore, poi si uniscono, poi il ricombinante entra nell'ospite, che viene fatto crescere su piastra e infine selezionato.")

q("u1124-002", T, "f", "261", "Che cosa riconoscono sul DNA gli enzimi di restrizione?", [
  "Sequenze palindromiche",
  "Sequenze poli-adeniliche",
  "Le origini di replicazione",
  "I promotori dei geni",
  "Le estremità dei telomeri",
  ], 0,
  "Sono enzimi di origine batterica che tagliano in maniera sequenza-specifica riconoscendo sequenze palindromiche.")

q("u1124-003", T, "f", "261", "Che cosa sono le «sticky ends» generate da molti enzimi di restrizione?", [
  "Estremità a singolo filamento, complementari fra loro",
  "Estremità a doppio filamento, prive di qualsiasi sporgenza",
  "Estremità metilate, protette dalla digestione",
  "Estremità circolari, già richiuse su se stesse",
  "Estremità fosforilate in 3', pronte per la ligasi",
  ], 0,
  "Il taglio sfalsato sulla sequenza palindromica lascia code a singolo filamento «appiccicose», che tendono a riappaiarsi perché complementari. Gli enzimi che tagliano dritto danno invece estremità piatte.")

q("u1124-004", T, "f", "261", "Fino a quante kbp di DNA estraneo può veicolare un plasmide come vettore di clonaggio?", [
  "Circa 10 kbp",
  "Circa 45 kbp",
  "Circa 100 kbp",
  "Circa 150 kbp",
  "Circa 300 kbp",
  ], 0,
  "Plasmidi fino a 10 kbp, fago λ fino a 21 kbp, cosmidi 32–45 kbp, BAC 100–300 kbp, YAC fino a 150 kbp.")

q("u1124-005", T, "f", "262", "In che forma si presentano normalmente i plasmidi all'interno della cellula batterica?", [
  "Superavvolta",
  "Rilassata",
  "Lineare",
  "Denaturata",
  "A singolo filamento",
  ], 0,
  "Si presentano superavvolti; si rilassano o si linearizzano solo in seguito a rotture durante le manipolazioni sperimentali.")

q("u1124-006", T, "f", "264", "Nel test di complementazione con X-gal, come appaiono le colonie che contengono il plasmide ricombinante?", [
  "Bianche",
  "Blu",
  "Blu solo al centro",
  "Rosse",
  "Non crescono affatto",
  ], 0,
  "L'inserto interrompe il gene lacZ: senza subunità α non si forma betagalattosidasi attiva, X-gal non viene idrolizzato e la colonia resta bianca. Le colonie blu hanno ricevuto un plasmide non ricombinante.")

q("u1124-007", T, "m", "261", "Perché, per esprimere una proteina umana in un batterio, si clona il cDNA e non il DNA cromosomico?", [
  "Perché il cDNA contiene solo le sequenze codificanti, che il batterio sa tradurre",
  "Perché il cDNA è più stabile del DNA genomico nelle condizioni di coltura",
  "Perché il cDNA è a singolo filamento e si inserisce meglio nel vettore",
  "Perché il DNA cromosomico non può essere tagliato dagli enzimi di restrizione",
  "Perché solo il cDNA possiede un'origine di replicazione riconosciuta dal batterio",
  ], 0,
  "Il cDNA è sintetizzato in vitro sull'mRNA maturo, quindi è privo di introni; il batterio non ha lo spliceosoma. Il DNA cromosomico si clona quando interessano regioni regolative o introni.")

q("u1124-008", T, "m", "261", "Perché conviene digerire vettore e inserto con due enzimi di restrizione diversi anziché con uno solo?", [
  "Perché le due estremità non sono complementari e il vettore non si richiude su se stesso",
  "Perché due enzimi diversi aumentano la processività della DNA ligasi nella reazione",
  "Perché due tagli distinti producono sempre estremità piatte, più facili da unire",
  "Perché in questo modo il vettore perde l'origine di replicazione e non si duplica",
  "Perché solo con due enzimi diversi si ottengono sticky ends, con uno solo estremità piatte",
  ], 0,
  "Con due estremità non complementari il DNA non può richiudersi su se stesso, ma solo unirsi a una molecola tagliata con gli stessi due enzimi; questo orienta anche l'inserto.")

q("u1124-009", T, "m", "262", "Che differenza c'è fra plasmidi a controllo stringente e a controllo rilassato?", [
  "I primi si replicano con il cromosoma e restano in poche copie, i secondi in molte copie",
  "I primi si replicano in molte copie per cellula, i secondi una sola volta per ciclo",
  "I primi hanno due origini di replicazione, i secondi una sola origine di replicazione",
  "I primi sono superavvolti in modo permanente, i secondi restano sempre rilassati",
  "I primi si trasmettono soltanto per coniugazione, i secondi solo per trasformazione chimica",
  ], 0,
  "I plasmidi grandi si replicano in modo coordinato con il cromosoma batterico (controllo stringente, poche copie); i piccoli, come i pUC, si replicano in modo indipendente fino a 500–700 copie.")

q("u1124-010", T, "m", "262", "Quali sono i tre elementi comuni a tutti i vettori di clonaggio?", [
  "Origine di replicazione, marcatore di selezione e siti unici di restrizione",
  "Origine di replicazione, promotore inducibile e sequenza di legame al ribosoma",
  "Promotore, terminatore della trascrizione e marcatore di resistenza agli antibiotici",
  "Sito cos, centromero artificiale e marcatore di resistenza agli antibiotici",
  "Sequenze telomeriche, geni par e siti unici di taglio per gli enzimi di restrizione",
  ], 0,
  "La sequenza ori permette la replicazione nell'ospite, il marcatore (di solito una resistenza) permette di selezionare chi ha il plasmide, i siti unici di taglio permettono di inserire il DNA.")

q("u1124-011", T, "m", "262", "Nel linguaggio della sbobina, che cosa distingue trasformazione e trasfezione?", [
  "La trasformazione introduce DNA nudo nei batteri, la trasfezione è mediata da fagi o virus",
  "La trasformazione introduce DNA nei lieviti, la trasfezione introduce DNA nei batteri",
  "La trasformazione richiede l'elettroporazione, la trasfezione il trattamento con CaCl₂",
  "La trasformazione riguarda i plasmidi, la trasfezione riguarda i cromosomi artificiali",
  "La trasformazione avviene solo in natura, la trasfezione solo in condizioni di laboratorio",
  ], 0,
  "Nelle cellule animali, però, «trasformazione» indica il passaggio allo stato tumorale, e l'introduzione di DNA eterologo si chiama trasfezione.")

q("u1124-012", T, "m", "263", "Come agisce il trattamento con CaCl₂ usato per rendere competenti i batteri?", [
  "Crea pori temporanei nella membrana, sfruttati con uno shock termico caldo-ghiaccio",
  "Degrada la parete cellulare con enzimi litici, lasciando protoplasti privi di parete",
  "Applica un impulso elettrico ad alto voltaggio che altera la permeabilità di membrana",
  "Induce la formazione dei pili necessari al passaggio del materiale genetico",
  "Neutralizza le cariche del DNA, che così attraversa la membrana per diffusione",
  ], 0,
  "I sali di calcio creano pori temporanei; il batterio viene portato intorno ai 40 °C e subito dopo in ghiaccio, così il DNA resta intrappolato. L'impulso elettrico è invece l'elettroporazione.")

q("u1124-013", T, "m", "266", "Come si ottiene il cDNA da clonare?", [
  "Retrotrascrivendo l'mRNA con la trascrittasi inversa, usando un innesco di poli-T",
  "Digerendo il DNA genomico con enzimi di restrizione che risparmiano gli esoni",
  "Amplificando il DNA cromosomico con primer complementari ai soli esoni del gene",
  "Trascrivendo in vitro il gene clonato con l'RNA polimerasi del fago T7",
  "Rimuovendo gli introni dal DNA genomico con una ligasi specifica per le giunzioni esoniche",
  ], 0,
  "La trascrittasi inversa è un enzima retrovirale; l'innesco oligo-dT si appaia alla coda poli-A. L'RNA viene poi degradato e si ottiene un DNA a doppio filamento con le sole porzioni codificanti.")

q("u1124-014", T, "a", "262", "Tre campioni dello stesso plasmide — superavvolto, rilassato e linearizzato — vengono corsi su gel di agarosio. Quale affermazione è corretta?", [
  "Solo il lineare migra secondo la propria dimensione reale rispetto a uno standard",
  "Solo il superavvolto migra secondo la propria dimensione reale rispetto a uno standard",
  "Le tre forme migrano insieme, perché hanno tutte lo stesso numero di paia di basi",
  "Il rilassato corre più veloce di tutti, perché incontra poco attrito nella maglia di gel",
  "Il superavvolto resta nel pozzetto, perché è troppo compatto per entrare nel gel",
  ], 0,
  "Il superavvolto corre molto veloce perché compatto, il rilassato si comporta come un DNA più grande; solo la forma lineare è confrontabile con uno standard di lunghezze note.")

q("u1124-015", T, "a", "263", "Perché in laboratorio si usano plasmidi incapaci di costruire pili?", [
  "Perché la coniugazione trasferirebbe il materiale genetico in modo non controllabile",
  "Perché i pili impediscono al plasmide di raggiungere un numero elevato di copie",
  "Perché i pili rendono il batterio sensibile agli antibiotici usati nella fase di selezione",
  "Perché senza pili il plasmide perde il fattore di fertilità e diventa più piccolo",
  "Perché i pili ostacolano l'ingresso del DNA nudo durante la trasformazione",
  ], 0,
  "Il fattore di fertilità consente il passaggio spontaneo del plasmide da una cellula donatrice a una ricevente: un processo naturale, ma non controllabile in laboratorio.")

q("u1124-016", T, "a", "263", "Un plasmide porta la resistenza all'ampicillina e alla tetraciclina; il DNA da clonare viene inserito dentro il gene per la resistenza all'ampicillina. Come si comporta il batterio ricombinante?", [
  "Cresce su tetraciclina ma non su ampicillina",
  "Cresce su ampicillina ma non su tetraciclina",
  "Cresce su entrambi gli antibiotici senza alcun problema",
  "Non cresce né su ampicillina né su tetraciclina",
  "Cresce solo se i due antibiotici sono presenti insieme",
  ], 0,
  "L'inserto interrompe il gene per la resistenza all'ampicillina: quella resistenza è persa, mentre resta quella alla tetraciclina. È l'inattivazione inserzionale.",
  note="Errore nella sbobina (Biochimica I, p. 263): per il batterio ricombinante scrive che «muore se piastrato su un terreno che contiene tetraciclina ma sopravvive su un terreno che contiene ampicillina». È il contrario, e contraddice la logica dell'inattivazione inserzionale descritta due righe sopra.")

q("u1124-017", T, "a", "264", "Perché ogni colonia di una genoteca contiene un solo tipo di plasmide ricombinante?", [
  "Perché una cellula non può mantenere due plasmidi con la stessa origine di replicazione",
  "Perché durante la trasformazione entra sempre una sola molecola di DNA per cellula",
  "Perché gli enzimi di restrizione tagliano in modo da generare un solo inserto per vettore",
  "Perché i plasmidi in eccesso vengono degradati dalle nucleasi della cellula ospite",
  "Perché solo un plasmide per cellula riesce a esprimere il marcatore di resistenza",
  ], 0,
  "Se due plasmidi con la stessa ori entrassero nella stessa cellula, uno dei due andrebbe perso con la replicazione.")

q("u1124-018", T, "a", "267", "Una proteina ricombinante espressa in E. coli precipita nei corpi inclusi. Perché questo non è necessariamente uno svantaggio?", [
  "Perché la frazione insolubile si separa dalle proteine di E. coli, che restano solubili",
  "Perché nei corpi inclusi la proteina è già nella sua conformazione nativa e attiva",
  "Perché la precipitazione protegge la proteina dalle proteasi batteriche citoplasmatiche",
  "Perché i corpi inclusi contengono solo proteina pura, senza lipidi o altre sostanze",
  "Perché la proteina insolubile viene secreta spontaneamente nel terreno di coltura",
  ], 0,
  "Centrifugando si raccolgono i corpi inclusi, scartando le proteine solubili di E. coli; poi, dializzando lentamente l'agente caotropico, la proteina può rifoldarsi in vitro.")

q("u1124-019", T, "a", "267", "Quale limite dell'espressione in batteri NON è aggirabile?", [
  "L'assenza degli enzimi per le modificazioni post-traduzionali",
  "La formazione di corpi inclusi con proteina mal ripiegata",
  "La tossicità della proteina ricombinante per la cellula ospite",
  "La bassa velocità di crescita delle colture batteriche",
  "L'impossibilità di inserire più di 8 kb di DNA nel vettore",
  ], 0,
  "Corpi inclusi e tossicità si aggirano (rifolding in vitro, promotore inducibile); la mancanza delle modificazioni post-traduzionali no, e in quel caso il batterio non è utilizzabile.",
  note="La sbobina (Biochimica I, p. 267) elenca fra le modificazioni post-traduzionali mancanti «alchilazioni, acetilazioni, fosforilazioni», ma dimentica la glicosilazione, che è il motivo più frequente per cui una proteina umana non si può produrre in E. coli.")

q("u1124-020", T, "a", "268", "Nell'ingegnerizzazione del plasmide Ti di Agrobacterium tumefaciens, che cosa va mantenuto?", [
  "Le sequenze di confine del T-DNA, che favoriscono l'integrazione nel genoma vegetale",
  "I geni che codificano per gli ormoni vegetali, necessari alla crescita della pianta",
  "I geni per la sintesi delle opine, che il batterio usa come fonte di nutrimento",
  "La porzione centrale del T-DNA, indispensabile per la formazione del callo",
  "I geni vir, che devono restare sullo stesso plasmide per mediare l'excisione del T-DNA",
  ], 0,
  "Si elimina il T-DNA che produce la galla ma si conservano le ripetizioni di confine di 25 bp; i geni vir vengono forniti da un altro plasmide.")

q("u1124-021", T, "l", "260", "Quale legame salda la DNA ligasi usata nel clonaggio?", [
  "Un legame fosfodiestere fra il 3'-OH di un nucleotide e il 5'-fosfato del successivo",
  "Un legame fosfodiestere fra il 5'-OH di un nucleotide e il 3'-fosfato del successivo",
  "Un legame N-glicosidico fra il carbonio 1' del desossiribosio e l'azoto della base",
  "Un legame idrogeno fra le basi complementari delle due estremità coesive",
  "Un legame estereo fra il gruppo 2'-OH del ribosio e il fosfato in posizione α",
  ], 0,
  "È la stessa ligasi che salda i frammenti di Okazaki nella duplicazione.",
  note="Errore nella sbobina (Biochimica I, p. 260): descrive la ligasi come formatrice di «un legame fosfodiestere tra un 5'OH e un 3'P». I gruppi sono invertiti: la ligasi unisce il 3'-OH di un nucleotide al 5'-fosfato di quello adiacente.")

q("u1124-022", T, "l", "264", "Perché l'inserto clonabile nel fago λ è limitato a 8–21 kb?", [
  "Perché il capside accoglie 38–51 kb e 30 kb del genoma fagico sono indispensabili",
  "Perché il sito cos tollera solo inserti compresi entro le 21 kb complessive",
  "Perché oltre le 21 kb il DNA fagico non riesce più a circolarizzarsi nel batterio",
  "Perché la replicazione a cerchio rotante si blocca con genomi superiori a 51 kb",
  "Perché la ligasi batterica non salda estremità coesive distanti più di 21 kb",
  ], 0,
  "Il genoma di λ è lungo circa 45 kb; la testa del capside ha una certa flessibilità e ne accoglie fra 38 e 51 kb, quindi può variare solo la porzione non indispensabile.")

q("u1124-023", T, "l", "265", "Quale elemento è tipico dei BAC e li distingue dai plasmidi comuni?", [
  "I geni par, che garantiscono la ripartizione nelle due cellule figlie",
  "Il sito cos, che permette il packaging in vitro nella testa del fago",
  "Le sequenze telomeriche, che proteggono le estremità durante la replicazione",
  "Il centromero, che consente la segregazione durante la mitosi dell'ospite",
  "Il promotore T7, che assicura un'elevata efficienza di trascrizione",
  ], 0,
  "BAC e plasmidi condividono ori, marcatori di resistenza e siti di restrizione; i geni par sono il tratto distintivo, insieme al controllo stringente che mantiene una copia per cellula. Telomeri e centromero sono dei YAC, il sito cos dei cosmidi.")

q("u1124-024", T, "h", "262", "Un ricercatore taglia vettore e inserto con un solo enzima di restrizione, liga e trasforma: ottiene moltissime colonie resistenti all'antibiotico, ma quasi nessuna contiene l'inserto. Qual è la spiegazione più probabile?", [
  "Le estremità del vettore sono complementari fra loro e si sono richiuse su se stesse",
  "L'enzima di restrizione ha prodotto estremità piatte, che la ligasi non riesce a unire",
  "Il vettore ha perso l'origine di replicazione durante la digestione con l'enzima",
  "L'inserto è stato degradato dalle nucleasi batteriche subito dopo la trasformazione",
  "Il marcatore di resistenza è stato interrotto dall'inserimento del DNA da clonare",
  ], 0,
  "Con un solo enzima le due estremità del vettore linearizzato sono complementari: la richiusura su se stesso compete con l'inserimento. Si evita digerendo con due enzimi diversi.")

q("u1124-025", T, "h", "264", "In un esperimento di clonaggio in pUC con X-gal, dopo la trasformazione tutte le colonie risultano blu. Che cosa è successo con maggiore probabilità?", [
  "Il vettore si è richiuso senza incorporare il DNA da clonare, e lacZ è rimasto integro",
  "L'inserto è entrato in tutte le colonie e ha interrotto il gene lacZ del vettore",
  "Le cellule hanno perso il plasmide, e la betagalattosidasi prodotta è quella cromosomica",
  "L'X-gal è stato degradato dagli antibiotici presenti nel terreno di coltura",
  "La subunità α è stata prodotta in eccesso, mascherando l'interruzione del gene",
  ], 0,
  "Colonia blu significa lacZα integro, cioè plasmide non ricombinante: nessun inserto si è inserito nel polilinker.")

q("u1124-026", T, "h", "261", "Si deve costruire una genoteca da frammenti di circa 200 kb. Quale vettore è adatto?", [
  "Un BAC, che veicola fra 100 e 300 kbp",
  "Un YAC, che veicola fino a 150 kbp",
  "Un cosmide, che veicola fra 32 e 45 kbp",
  "Il fago λ, che veicola fino a 21 kbp",
  "Un plasmide pUC, che veicola fino a 10 kbp",
  ], 0,
  "200 kb supera la capienza di YAC, cosmidi, fago λ e plasmidi: resta il cromosoma artificiale batterico.")

q("u1124-027", T, "h", "267", "Si vuole produrre in E. coli una proteina umana che risulta tossica per il batterio. Quale accorgimento adotta il sistema di espressione descritto nella sbobina?", [
  "Un promotore inducibile tenuto spento dal repressore fino a coltura cresciuta",
  "Un promotore costitutivo forte, che massimizza la resa fin dall'inizio della coltura",
  "Un vettore privo di origine di replicazione, che limita il numero di copie per cellula",
  "Una coda di istidine all'N-terminale, che neutralizza la tossicità della proteina",
  "Un ceppo privo di ribosomi funzionanti, che rallenta la traduzione del messaggero",
  ], 0,
  "Nel sistema T7 il repressore lac blocca la polimerasi finché non si aggiunge lattosio o un suo analogo: a quel punto le cellule sono già cresciute a sufficienza.")

q("u1124-028", T, "h", "269", "Perché per esprimere un gene in cellule di mammifero si ricorre a vettori retrovirali e non a plasmidi?", [
  "Perché i plasmidi non sono disponibili per i mammiferi e i retrovirus integrano il gene",
  "Perché i plasmidi non possono superare le 8 kb di inserto, limite assente nei retrovirus",
  "Perché i retrovirus evitano del tutto il rischio di mutagenesi inserzionale nell'ospite",
  "Perché i retrovirus si integrano anche nelle cellule che non entrano mai in mitosi",
  "Perché solo i retrovirus possiedono le sequenze LTR necessarie alla trascrizione",
  ], 0,
  "Per il mammifero non esistono sistemi plasmidici: i vettori virali assicurano infezione efficiente e espressione stabile. Restano però gli svantaggi: integrazione solo dopo la dissoluzione della membrana nucleare, casualità dell'inserzione e limite di 8 kb fra le LTR.")


# ── PCR (p. 270–280) ────────────────────────────────────────────────────────
P = "d13-pcr"

q("u1124-029", P, "f", "270", "Chi ha messo a punto la PCR?", [
  "K. Mullis, negli anni '80",
  "K. Mullis, negli anni '60",
  "F. Sanger, negli anni '70",
  "P. Berg, negli anni '70",
  "H. Boyer, negli anni '90",
  ], 0,
  "La tecnica ha rivoluzionato la genetica molecolare rendendo possibile amplificare in vitro una data sequenza di DNA.")

q("u1124-030", P, "f", "271", "Quali sono le tre temperature di un ciclo di PCR, nell'ordine?", [
  "95 °C, 50–65 °C, 68–72 °C",
  "72 °C, 95 °C, 50–65 °C",
  "50–65 °C, 95 °C, 68–72 °C",
  "37 °C, 72 °C, 95 °C",
  "95 °C, 68–72 °C, 50–65 °C",
  ], 0,
  "Denaturazione a 95 °C per 10–40 s, annealing dei primer a 50–65 °C per 30–120 s, polimerizzazione a 68–72 °C.")

q("u1124-031", P, "f", "272", "Perché nella PCR si usa una DNA polimerasi estratta da microrganismi termofili?", [
  "Perché mantiene struttura e attività alle temperature di denaturazione",
  "Perché lavora senza bisogno di un primer che fornisca l'innesco",
  "Perché ha un'elevata attività di correzione di bozze, che riduce gli errori",
  "Perché sintetizza il DNA in entrambe le direzioni, 5'→3' e 3'→5'",
  "Perché riconosce direttamente le sequenze palindromiche del DNA stampo",
  ], 0,
  "Le temperature di denaturazione, intorno ai 90–95 °C, denaturerebbero un enzima comune; le polimerasi termofile hanno inoltre un optimum superiore ai 37 °C.")

q("u1124-032", P, "f", "274", "Che cosa amplifica la RT-PCR?", [
  "Un RNA, convertito prima in cDNA dalla trascrittasi inversa",
  "Un DNA genomico, usando primer complementari agli introni",
  "Un DNA plasmidico, usando il vettore stesso come stampo",
  "Una proteina, dopo retrotraduzione nella sequenza codificante",
  "Un RNA, direttamente, senza bisogno di retrotrascrizione",
  ], 0,
  "Si estrae l'RNA, lo si retrotrascrive in cDNA con un oligo-dT e poi lo si amplifica con primer specifici. Serve a valutare il livello di espressione di un gene.")

q("u1124-033", P, "f", "279", "Quale tipo di PCR consente di misurare la quantità di DNA di partenza?", [
  "La real time PCR",
  "La nested PCR",
  "La multiplex PCR",
  "La PCR su DNA genomico",
  "La PCR con estremità coesive",
  ], 0,
  "Il valore Ct, il ciclo soglia oltre il quale la fluorescenza supera il valore di soglia, è correlato alla quantità iniziale di stampo; una curva standard permette di risalire alla concentrazione.")

q("u1124-034", P, "m", "270", "Quali due caratteristiche della replicazione del DNA sfrutta la PCR?", [
  "La sintesi in direzione 5'→3' e la necessità di un primer",
  "La sintesi in direzione 3'→5' e la necessità di un'elicasi",
  "L'attività esonucleasica di correzione e la presenza di una pinza scorrevole",
  "La semiconservatività della replicazione e l'azione della topoisomerasi",
  "La sintesi discontinua del filamento lento e l'azione della DNA ligasi",
  ], 0,
  "Il 3'-OH del primer esegue l'attacco nucleofilo sul fosfato in α del desossinucleotide trifosfato; il pirofosfato liberato viene poi idrolizzato, rendendo la reazione irreversibile.")

q("u1124-035", P, "m", "271", "Come sono disposti i due primer rispetto alla regione da amplificare?", [
  "Con il 3'-OH rivolto verso l'interno della regione da amplificare",
  "Con il 3'-OH rivolto verso l'esterno della regione da amplificare",
  "Entrambi sullo stesso filamento, a monte della regione da amplificare",
  "Appaiati fra loro, in modo da formare una forcina che innesca la sintesi",
  "Con il 5'-fosfato rivolto verso l'interno della regione da amplificare",
  ], 0,
  "Sono complementari alle due estremità 3' della sequenza: ciascuno offre un 3'-OH libero su un filamento, e la sintesi procede verso l'interno.")

q("u1124-036", P, "m", "272", "Da quale ciclo in poi la PCR produce frammenti di dimensione definita dai due primer?", [
  "Dal terzo",
  "Dal primo",
  "Dal secondo",
  "Dal decimo",
  "Dal trentesimo",
  ], 0,
  "Nei primi cicli i filamenti vengono replicati finché la polimerasi non si stacca casualmente; dal terzo ciclo compare la popolazione di lunghezza definita, che cresce esponenzialmente.")

q("u1124-037", P, "m", "272", "Come si può usare la PCR per aggiungere siti di restrizione a un gene da clonare?", [
  "Modificando i primer, che portano code riconosciute dagli enzimi di restrizione",
  "Aggiungendo gli enzimi di restrizione direttamente nella miscela di reazione",
  "Usando una polimerasi termofila priva dell'attività di correzione di bozze",
  "Aumentando la temperatura di annealing, che favorisce i tagli sequenza-specifici",
  "Sostituendo i desossinucleotidi con analoghi riconosciuti dalle endonucleasi",
  ], 0,
  "Si lascia intatta la parte del primer che riconosce il gene e si aggiungono due regioni riconosciute da enzimi di restrizione: la PCR amplifica e insieme introduce i siti.")

q("u1124-038", P, "m", "275", "Su che cosa si basa la nested PCR?", [
  "Su due coppie di primer successive, la seconda più interna della prima",
  "Su due coppie di primer usate insieme nella stessa reazione di amplificazione",
  "Su una coppia di primer e un controllo interno a concentrazione nota",
  "Su primer che amplificano contemporaneamente più segmenti dello stesso gene",
  "Su una sonda fluorescente che segnala in tempo reale l'avanzare della reazione",
  ], 0,
  "Il primo amplificato può contenere aspecifici; i primer interni, usando quel prodotto come stampo, generano solo l'amplificato specifico. Aumentano specificità e sensibilità.")

q("u1124-039", P, "m", "276", "Che cosa indica il valore Ct nella real time PCR?", [
  "Il ciclo in cui la fluorescenza del campione supera il valore soglia",
  "Il ciclo in cui la reazione raggiunge il plateau e si arresta",
  "Il numero totale di cicli necessari per saturare la fluorescenza",
  "La temperatura di annealing ottimale calcolata per quella coppia di primer",
  "Il rapporto fra DNA bersaglio e controllo interno al termine della reazione",
  ], 0,
  "Più DNA stampo c'è all'inizio, più breve è la fase di latenza e più basso è il Ct: con molto DNA il ciclo soglia può essere il 10°, con poco il 35°.")

q("u1124-040", P, "a", "271", "Quale affermazione sulla PCR classica è corretta?", [
  "Amplifica un DNA stampo; la retrotrascrizione serve solo se si parte da RNA",
  "Amplifica sempre a partire dall'RNA cellulare, previa retrotrascrizione",
  "Amplifica l'RNA direttamente, grazie a una polimerasi RNA-dipendente",
  "Amplifica solo DNA a singolo filamento, estratto in condizioni denaturanti",
  "Amplifica il DNA senza bisogno di innesco, grazie alla polimerasi termofila",
  ], 0,
  "Lo stampo della PCR è un DNA; quando il punto di partenza è l'RNA si fa prima una retrotrascrizione, e la tecnica si chiama RT-PCR.",
  note="Errore nella sbobina (Biochimica I, p. 271): «La PCR consiste fondamentalmente nell'amplificazione a partire dall'RNA di una cellula che dev'essere retrascritto da una trascrittasi inversa». Questa è la descrizione della RT-PCR, non della PCR in generale, che amplifica un DNA stampo.")

q("u1124-041", P, "a", "273", "Nella mutagenesi sito-specifica con PCR, perché il DNA di partenza viene eliminato con DpnI?", [
  "Perché è metilato, mentre l'amplificato prodotto in vitro non lo è",
  "Perché è lineare, mentre l'amplificato prodotto in vitro è circolare",
  "Perché è a singolo filamento, mentre l'amplificato è a doppio filamento",
  "Perché è privo della mutazione e ha quindi una temperatura di fusione più alta",
  "Perché è legato ai primer mutanti e viene riconosciuto dall'enzima come estraneo",
  ], 0,
  "Il plasmide templato proviene da cellule che lo hanno metilato; la PCR non metila, quindi l'enzima degrada selettivamente lo stampo originale e resta solo il DNA mutato.",
  note="Refuso nella sbobina (Biochimica I, p. 273): l'enzima è indicato come «DPM1». Il nome corretto è DpnI.")

q("u1124-042", P, "a", "273", "Come si ottiene, con la PCR, una delezione invece di una sostituzione puntiforme?", [
  "Usando due primer non perfettamente complementari, ma shiftati fra loro",
  "Usando un primer più lungo della sequenza del gene da amplificare",
  "Usando una polimerasi priva dell'attività di correzione di bozze",
  "Aumentando la concentrazione di Mg²⁺ nella miscela oppure sostituendolo con Mn²⁺",
  "Riducendo il numero di cicli, così che l'amplificato resti incompleto",
  ], 0,
  "Primer shiftati saltano un tratto e danno una delezione; un primer più lungo della sequenza dà un'inserzione. Polimerasi senza proofreading e Mn²⁺ servono invece alla mutagenesi random.")

q("u1124-043", P, "a", "273", "A che cosa serve la mutagenesi random eseguita con la PCR?", [
  "A far evolvere in vitro un enzima verso nuove attività o specificità di substrato",
  "A correggere in modo mirato una mutazione patogena in un gene già clonato",
  "A introdurre siti di restrizione in posizioni note alle estremità dell'amplificato",
  "A eliminare selettivamente il DNA templato metilato dalla miscela di reazione",
  "A quantificare il DNA di partenza confrontandolo con uno standard interno",
  ], 0,
  "La polimerasi introduce errori in posizioni non note; su molte varianti ce n'è una remota probabilità che una sia favorevole. Si favorisce con rapporti alterati dei nucleotidi, più Mg²⁺ o Mn²⁺.")

q("u1124-044", P, "a", "277", "Come funziona una sonda TaqMan nella real time PCR?", [
  "L'esonucleasi 5'→3' della polimerasi la degrada e separa reporter e quencher",
  "Si intercala fra le basi del DNA a doppio filamento ed emette fluorescenza",
  "Si appaia ai primer e ne blocca l'estensione finché non c'è l'amplificato",
  "Lega il DNA neosintetizzato e spegne la fluorescenza in modo proporzionale",
  "Viene estesa dalla polimerasi e incorpora nucleotidi marcati con un fluoroforo",
  ], 0,
  "Sul probe a singolo filamento stanno un reporter e un quencher abbastanza vicini da spegnere la fluorescenza; il probe ha il 3'-OH bloccato e, quando viene degradato, il reporter si libera e dà segnale proporzionale all'amplificato. SYBR Green I e bromuro di etidio sono invece probe non specifici.",
  note="Imprecisione nella sbobina (Biochimica I, p. 277): «la polimerasi utilizza un'attività 5'-3' esonucleasica per degradare il primer a livello del probe». Ciò che viene degradato è il probe, non il primer.")

q("u1124-045", P, "a", "278", "Perché, per sapere se in un sieropositivo l'infezione da HIV è in atto, non basta la PCR sul DNA?", [
  "Perché il genoma virale integrato c'è comunque: l'infezione attiva si vede sull'RNA",
  "Perché il DNA provirale viene degradato nei linfociti T dei soggetti sieropositivi",
  "Perché la PCR su DNA non raggiunge la sensibilità necessaria per il genoma virale",
  "Perché il virus HIV ha un genoma a RNA e non integra mai nel genoma della cellula",
  "Perché i primer complementari al genoma di HIV riconoscono anche il DNA della cellula ospite",
  ], 0,
  "Il provirus integrato dà amplificato in entrambi i casi; se la malattia è in atto il genoma virale viene trascritto, quindi serve una RT-PCR sull'RNA. Nella sola sieropositività l'analisi dei cDNA non dà amplificato.")

q("u1124-046", P, "l", "274", "Quali sono le due trascrittasi inverse più usate in laboratorio?", [
  "AMV e MoMLV",
  "AMV e RNasi H",
  "Taq e Pfu polimerasi",
  "T7 e T4 polimerasi",
  "DpnI e EcoRI",
  ], 0,
  "AMV viene dall'Avian Myeloblastosis Virus, MoMLV dal Moloney Murine Leukemia Virus. L'RNasi H è l'enzima che degrada l'RNA nell'ibrido DNA-RNA.")

q("u1124-047", P, "l", "280", "Quale sequenza si amplifica per stabilire il sesso di un individuo?", [
  "DYZ1, un frammento di 250 bp presente sul cromosoma Y",
  "DYZ1, un frammento di 250 bp presente sul cromosoma X",
  "Una sequenza Short Tandem Repeat di meno di 100 bp sul cromosoma Y",
  "Il locus dell'RNasi P, usato anche come controllo positivo dell'estrazione",
  "La regione N1 del cromosoma Y, affiancata dalla regione N2 di controllo",
  ], 0,
  "Si può rendere il sistema più selettivo con una nested PCR. Le Short Tandem Repeats servono invece al DNA fingerprinting in medicina forense.")

q("u1124-048", P, "h", "276", "Due campioni vengono analizzati in real time PCR: il campione A ha Ct = 12, il campione B ha Ct = 32. Che cosa si deduce?", [
  "A conteneva molto più DNA stampo di B all'inizio della reazione",
  "B conteneva molto più DNA stampo di A all'inizio della reazione",
  "A ha avuto una fase di latenza più lunga, dovuta a primer limitanti",
  "I due campioni contenevano la stessa quantità di DNA, ma sonde diverse",
  "B ha raggiunto prima il plateau, segno di un'amplificazione più efficiente",
  ], 0,
  "Più stampo c'è all'inizio, più breve è la fase di latenza e più precocemente la fluorescenza supera la soglia.")

q("u1124-049", P, "h", "278", "Un tampone per SARS-CoV-2 risulta positivo per la regione N1, negativo per N2 e positivo per l'RP. Come va refertato?", [
  "Non conclusivo: il test va ripetuto",
  "Positivo: l'amplificato di una regione virale basta per la diagnosi",
  "Negativo: con una sola regione virale amplificata il risultato è negativo",
  "Non valido: la positività di RP indica un errore nell'estrazione degli RNA",
  "Positivo debole: la carica virale è bassa ma il risultato è comunque certo",
  ], 0,
  "Servono entrambe le regioni virali per la positività. Con entrambe negative e RP positivo il tampone è negativo; se mancano anche gli amplificati di RP il test è non valido perché l'estrazione può essere fallita.")

q("u1124-050", P, "h", "275", "In una PCR diagnostica compaiono, oltre alla banda attesa, alcune bande aspecifiche. Quale strategia risolve il problema?", [
  "Una nested PCR, con una seconda coppia di primer più interna",
  "Una PCR competitiva, con un controllo interno a concentrazione nota",
  "Una multiplex PCR, con più coppie di primer nella stessa reazione",
  "Una RT-PCR, retrotrascrivendo l'RNA totale prima dell'amplificazione",
  "Un aumento del numero di cicli, fino a 50, per arricchire il prodotto specifico",
  ], 0,
  "Gli aspecifici nascono quando i primer riconoscono, con efficienza minore, porzioni diverse dal gene. Solo l'amplificato specifico contiene anche le sequenze interne, quindi solo quello viene riamplificato.")

q("u1124-051", P, "h", "279", "In un paziente con sospetto linfoma follicolare si eseguono due primer che appaiano uno sul cromosoma 14 e uno sul cromosoma 18. Si ottiene un amplificato. Che cosa significa?", [
  "È avvenuta la traslocazione, e i due primer si trovano ora sulla stessa molecola",
  "I due cromosomi sono presenti in copia soprannumeraria nelle cellule analizzate",
  "Il gene BCL-2 è rimasto in una regione eterocromatica e non viene trascritto",
  "I primer hanno riconosciuto sequenze aspecifiche su cromosomi non omologhi",
  "La cellula ha subito una delezione che ha avvicinato i due loci sullo stesso braccio",
  ], 0,
  "Normalmente due primer su cromosomi diversi non danno amplificato. Con la traslocazione BCL-2 passa dal locus eterocromatico alla regione dei geni per le immunoglobuline sul 14, altamente trascritta, e la cellula prolifera.")

q("u1124-052", P, "h", "280", "Perché il cell-free fetal DNA si presta bene all'analisi con PCR?", [
  "Perché è piccolo e frammentato, quindi facilmente amplificabile",
  "Perché è presente nel sangue materno in concentrazione molto elevata",
  "Perché è privo di introni, essendo prodotto a partire dall'mRNA fetale",
  "Perché resta stabile a lungo e può essere analizzato a distanza di giorni",
  "Perché è a singolo filamento e non richiede la fase di denaturazione iniziale",
  ], 0,
  "È DNA fetale rilasciato dal trofoblasto, circolante per un tempo limitato nel sangue materno: si isola con un semplice prelievo venoso e va analizzato subito dopo. Il successivo sequenziamento shotgun permette di cercare patologie a carico di geni specifici.")
