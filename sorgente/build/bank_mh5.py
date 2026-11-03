"""Domande HARD (livello h), modulo 5: gluconeogenesi (pp. 139–158)."""
from bank_common import q

T = "m5-fonti"
q("h5f-01", T, "h", "141", "Dalle 22 a mezzogiorno del giorno dopo, senza colazione, come cambiano le fonti di glucosio ematico?", [
  'Il glicogeno epatico cala e la gluconeogenesi diventa la fonte principale',
  'Il glicogeno muscolare sostiene la glicemia per tutta la notte e la mattina',
  'La gluconeogenesi si ferma di notte e riparte solo al risveglio',
  'La glicemia è sostenuta solo dal glucosio assorbito con la cena',
  'Il glicogeno epatico aumenta di notte grazie al cortisolo e poi si consuma al mattino',
  ], 0,
  'Dopo ogni pasto la gluconeogenesi si azzera e riparte la sintesi di glicogeno.')
q("h5f-02", T, "h", "140", "Perché la gluconeogenesi è indispensabile anche se abbiamo riserve di glicogeno?", [
  'Il glicogeno epatico finisce in meno di un giorno; serve anche a riciclare il lattato',
  'Il glicogeno muscolare non contiene glucosio ma solo glucosio 6-fosfato',
  'Il cervello usa solo glucosio di origine gluconeogenica, non quello del glicogeno',
  'Il glicogeno epatico si forma solo di notte e non è disponibile di giorno',
  'La gluconeogenesi produce ATP netto, indispensabile al fegato durante il digiuno',
  ], 0,
  'Il cervello consuma circa 120 g di glucosio al giorno e il glicogeno epatico è circa 100 g; il glicogeno muscolare non può dare glucosio al sangue. Sulle cifre la sbobina parla di 160 g/die di glucosio, per il 70% al cervello.')
q("h5f-03", T, "h", "140–141", "Quali sono i principali precursori della gluconeogenesi e da dove vengono?", [
  'Lattato, amminoacidi (soprattutto alanina) e glicerolo',
  'Acidi grassi a catena pari, acetil-CoA e corpi chetonici',
  'Solo il lattato prodotto da muscolo ed eritrociti',
  'Glicogeno muscolare, urea e acetoacetato',
  'Colesterolo, glicerolo e acidi grassi a catena pari',
  ], 0,
  "Il lattato viene da eritrociti e muscolo, l'alanina dalle proteine muscolari, il glicerolo dai trigliceridi del tessuto adiposo. Gli acidi grassi a catena pari non danno glucosio netto.")
q("h5f-04", T, "h", "140", "Dove avviene la gluconeogenesi?", [
  'Fegato (circa 90%) e rene (circa 10%)',
  'Muscolo scheletrico e cuore',
  'Cervello e midollo spinale',
  'Solo negli eritrociti',
  'Tessuto adiposo e intestino, in parti uguali',
  ], 0,
  'Serve la glucosio 6-fosfatasi, presente in fegato e rene; il contributo renale aumenta nel digiuno prolungato.')
q("h5f-05", T, "h", "142", "Perché il cortisolo è legato al ritmo della gluconeogenesi?", [
  'Ha un picco al mattino e induce la trascrizione di enzimi come la PEPCK',
  'Si lega a un recettore di membrana e attiva la PKA come il glucagone',
  'Inibisce la glicogenolisi di notte e la riattiva al mattino',
  'Viene secreto solo dopo i pasti, quando la glicemia è alta',
  'Aumenta la secrezione notturna di insulina e quindi la sintesi di glicogeno',
  ], 0,
  'Ha un minimo verso mezzanotte. Come ormone steroideo agisce tramite un recettore nucleare sulla trascrizione: effetti lenti.',
  note="Sbobina di Biochimica II, p. 142: il cortisolo è definito «ormone anabolizzante» perché fa sintetizzare proteine. Nel metabolismo il cortisolo è catabolico per le proteine muscolari (le degrada per dare amminoacidi alla gluconeogenesi, come dice la stessa sbobina a p. 149); induce la sintesi di specifici enzimi epatici.")
q("h5f-06", T, "h", "149", "Su quali tessuti agisce il cortisolo per favorire la gluconeogenesi?", [
  'Fegato, muscolo e tessuto adiposo',
  'Solo fegato',
  'Pancreas e cervello',
  'Muscolo e cervello',
  'Rene e intestino soltanto, dove avviene la gluconeogenesi',
  ], 0,
  'Fegato: enzimi gluconeogenici; muscolo: proteolisi e rilascio di alanina; tessuto adiposo: glicerolo dai trigliceridi. Per questo una terapia cortisonica prolungata riduce la massa muscolare e può dare iperglicemia.')
q("h5f-07", T, "h", "139", "Un neonato prematuro va spesso in ipoglicemia grave dopo il parto. Perché?", [
  "Il glicogeno si accumula nell'ultimo trimestre: le riserve sono scarse",
  'Ha troppo glucagone, che consuma il glicogeno ancora prima del parto',
  'Non produce insulina e quindi non può usare il glucosio del sangue',
  'Il suo glicogeno ha una struttura anomala che la fosforilasi non riconosce',
  'Assorbe troppo glucosio dal latte e va in ipoglicemia reattiva',
  ], 0,
  "Quando cessa l'apporto dalla placenta, il prematuro non ha riserve sufficienti. Lo stesso succede con malnutrizione materna.")
q("h5f-08", T, "h", "139", "Il figlio di una madre con diabete mal controllato può avere ipoglicemia dopo la nascita. Perché?", [
  'Ha iperinsulinemia, che blocca glicogenolisi e gluconeogenesi',
  'Ha poco glicogeno, perché la madre diabetica non gli cede glucosio',
  'Ha un deficit congenito di glucosio 6-fosfatasi epatica',
  'Non produce glucagone, perché le cellule α sono soppresse',
  "Ha ricevuto attraverso la placenta l'insulina della madre",
  ], 0,
  "Esposto a molto glucosio in utero, ha iperplasia delle cellule β. L'insulina materna non attraversa la placenta; il glucosio sì.")

T = "m5-reazioni"
q("h5r-01", T, "h", "143", "Quali tre tappe della glicolisi devono essere aggirate dalla gluconeogenesi e con quali enzimi?", [
  'PK → piruvato carbossilasi + PEPCK; PFK1 → FBPasi1; esochinasi → G6Pasi',
  "Aldolasi, enolasi e fosfoglicerato chinasi, che hanno ΔG°' positivo",
  'Esochinasi, aldolasi e piruvato chinasi, sostituite da fosfatasi',
  'GAP deidrogenasi, PFK1 e PDH, sostituite da enzimi mitocondriali',
  'Solo la piruvato chinasi, perché le altre tappe sono reversibili',
  ], 0,
  "Le altre sette reazioni sono all'equilibrio e vengono usate in senso inverso.")
q("h5r-02", T, "h", "144–145", "Perché per trasformare il piruvato in PEP servono due enzimi e due nucleotidi?", [
  'Il PEP è molto energetico: serve carbossilare e poi decarbossilare',
  'Il piruvato deve prima entrare nel nucleo per essere attivato',
  'La piruvato chinasi è reversibile ma troppo lenta nel fegato',
  'Serve NADPH per ridurre il piruvato prima di fosforilarlo',
  'Il PEP si forma nel citosol ma deve essere attivato nel mitocondrio da due chinasi',
  ], 0,
  "Piruvato → ossalacetato (piruvato carbossilasi, ATP, biotina); poi la decarbossilazione dell'ossalacetato spinge la sintesi del PEP (PEPCK, GTP). La CO₂ entra e poi esce: è lo stesso carbonio a rendere la reazione possibile.",
  note="Sbobina di Biochimica II, p. 145: tra i prodotti della PEP carbossichinasi compare l'«ADP». Con il GTP si forma GDP. Inoltre a p. 144 si legge che l'acetil-CoA attiva la «piruvato decarbossilazione»: è la piruvato carbossilazione.")
q("h5r-03", T, "h", "145", "Perché l'ossalacetato prodotto nel mitocondrio (da alanina) esce come malato?", [
  "Non c'è un trasportatore per l'ossalacetato; il malato porta anche NADH",
  'Il malato è più energetico e spinge la reazione della PEPCK',
  'Il malato è il vero substrato della PEPCK citosolica',
  "L'ossalacetato è tossico nel citosol e va mascherato come malato",
  "Il malato attiva la glucosio 6-fosfatasi del reticolo e accelera l'uscita del glucosio",
  ], 0,
  'Viene ridotto a malato (MDH mitocondriale), esce e viene riossidato nel citosol, producendo il NADH che serve alla GAP deidrogenasi.')
q("h5r-04", T, "h", "150", "Se il precursore è il lattato, perché l'ossalacetato non ha bisogno di uscire come malato?", [
  'Il NADH viene già dal lattato; il PEP si forma nel mitocondrio ed esce',
  'Il lattato entra direttamente nella glicolisi come fosfoenolpiruvato',
  'Il lattato non passa per il piruvato ma diventa subito ossalacetato',
  'Il lattato attiva la piruvato chinasi e salta il primo bypass',
  'Il lattato produce NADPH, che sostituisce il NADH nella GAP deidrogenasi citosolica',
  ], 0,
  "La conversione lattato → piruvato produce già il NADH citosolico; la PEPCK mitocondriale trasforma l'ossalacetato in PEP, che esce con un trasportatore. È uno dei motivi per cui esistono due isoforme di PEPCK.")
q("h5r-05", T, "h", "147", "Confronta il bilancio della gluconeogenesi con quello di un'ipotetica glicolisi inversa.", [
  "Gluconeogenesi: 4 ATP + 2 GTP, ΔG°' ≈ −38; inversa: 2 ATP, ΔG°' ≈ +84",
  'Hanno lo stesso costo, ma la gluconeogenesi è più veloce',
  'La gluconeogenesi produce 2 ATP netti, la glicolisi inversa ne consuma 2',
  "La glicolisi inversa sarebbe favorita, ma è inibita dall'insulina",
  "Gluconeogenesi: 2 ATP, ΔG°' ≈ +84; inversa: 6 ATP, ΔG°' ≈ −38",
  ], 0,
  'Entrambe usano 2 NADH. I 4 legami ad alta energia in più sono il prezzo per rendere la via irreversibile.')
q("h5r-06", T, "h", "146", "Che cosa ha in comune la fruttosio 1,6-bisfosfatasi con la glucosio 6-fosfatasi?", [
  'Idrolizzano un fosfoestere con acqua, senza riformare ATP',
  "Entrambe producono ATP trasferendo il fosfato all'ADP",
  'Entrambe si trovano nel lume del reticolo endoplasmatico',
  'Entrambe richiedono la biotina come coenzima',
  'Entrambe sono attivate allostericamente dal fruttosio 2,6-bisfosfato',
  ], 0,
  'Sono reazioni esoergoniche che aggirano due chinasi irreversibili. Solo la glucosio 6-fosfatasi è nel lume del reticolo.')
q("h5r-07", T, "h", "146", "Un paziente con glicogenosi di tipo I. Quale delle due vie per mantenere la glicemia funziona?", [
  'Nessuna delle due',
  'Solo la gluconeogenesi',
  'Solo la glicogenolisi',
  'Entrambe, ma più lentamente',
  'Solo la gluconeogenesi renale, che non ha bisogno della glucosio 6-fosfatasi',
  ], 0,
  'Glicogenolisi e gluconeogenesi producono entrambe G6P, che senza glucosio 6-fosfatasi non diventa glucosio. Un deficit della sola fosforilasi epatica sarebbe meno grave.',
  note="Sbobina di Biochimica II, p. 146: c'è scritto «malattia di tipo 1 di diabete mellito»; si intende la glicogenosi di tipo I (von Gierke).")
q("h5r-08", T, "h", "143–147", "Quante molecole di piruvato servono per un glucosio e quante tappe sono in comune con la glicolisi?", [
  '2 piruvati; 7 reazioni comuni e 3 tappe specifiche',
  '1 piruvato; tutte e 10 le reazioni sono comuni',
  '2 piruvati; nessuna reazione in comune con la glicolisi',
  '3 piruvati; 5 reazioni comuni e 5 specifiche',
  '2 piruvati; 3 reazioni comuni e 7 tappe specifiche con enzimi propri',
  ], 0,
  'Le 3 tappe specifiche usano 4 enzimi: il primo bypass ne usa due (piruvato carbossilasi e PEPCK).')

T = "m5-glicerolo"
q("h5g-01", T, "h", "147", "Da quale punto entra il glicerolo nella gluconeogenesi e perché è una via più semplice?", [
  'Come DHAP, a livello dei triosi: salta il bypass piruvato → PEP',
  'Come piruvato, dopo la transaminazione nel mitocondrio',
  'Come acetil-CoA, che attiva la piruvato carbossilasi',
  'Come ossalacetato, dopo la carbossilazione del glicerolo',
  'Come glucosio 6-fosfato, dopo la condensazione di due molecole di glicerolo',
  ], 0,
  'Glicerolo → glicerolo 3-fosfato (glicerolo chinasi, nel fegato) → DHAP (glicerolo 3-fosfato deidrogenasi).',
  note="Sbobina di Biochimica II, p. 141: il glicerolo viene fosforilato a «glicerolo 1-P». Il prodotto della glicerolo chinasi è il glicerolo 3-fosfato (come la sbobina scrive a p. 147).")
q("h5g-02", T, "h", "149", "Perché l'adipocita non può riutilizzare il glicerolo liberato dalla lipolisi?", [
  'Ha poca glicerolo chinasi',
  "Il glicerolo è tossico per l'adipocita",
  "L'adipocita non ha GLUT4",
  'Il glicerolo viene trasformato in acidi grassi',
  "L'adipocita lo ossida completamente a CO₂ nei mitocondri",
  ], 0,
  "Il glicerolo esce nel sangue e viene fosforilato nel fegato. Non è nelle sbobine: l'adipocita ricava il glicerolo 3-P dalla glicolisi o dalla gliceroneogenesi.")
q("h5g-03", T, "h", "147", "Perché il glicerolo dei trigliceridi può dare glucosio mentre gli acidi grassi a catena pari no?", [
  'Il glicerolo dà DHAP; gli acidi grassi danno solo acetil-CoA',
  'Il glicerolo contiene più carbonio degli acidi grassi',
  'Gli acidi grassi non vengono ossidati nel fegato',
  'Il glicerolo entra nel Krebs come succinato',
  'Gli acidi grassi inibiscono la PEPCK e bloccano la gluconeogenesi nel fegato',
  ], 0,
  "Il DHAP è un intermedio a 3 C della gluconeogenesi; l'acetil-CoA non può diventare piruvato. Il glicerolo è però una piccola parte della massa dei trigliceridi.")
q("h5g-04", T, "h", "147", "Quale altro substrato «lipidico» può fornire glucosio netto?", [
  'Il propionil-CoA, che diventa succinil-CoA',
  "L'acetoacetato, che diventa ossalacetato",
  'Il colesterolo, che diventa piruvato',
  'Il palmitato, che diventa malato',
  "L'acetil-CoA, che si condensa con un altro acetil-CoA e diventa succinato",
  ], 0,
  'Il propionil-CoA viene da acidi grassi a catena dispari e da alcuni amminoacidi; il passaggio metilmalonil-CoA → succinil-CoA richiede vitamina B12.')
q("h5g-05", T, "h", "149", "A digiuno notturno, da dove deriva il glicerolo usato dal fegato?", [
  'Dalla lipolisi dei trigliceridi del tessuto adiposo',
  'Dalla degradazione del glicogeno epatico',
  'Dai fosfolipidi delle membrane degli epatociti',
  'Dal lattato prodotto dal muscolo durante la notte',
  'Dai trigliceridi della cena, ancora presenti nei chilomicroni circolanti',
  ], 0,
  'La lipolisi è favorita da cortisolo, glucagone e adrenalina; il cortisolo sfavorisce anche la riesterificazione dei trigliceridi.')
q("h5g-06", T, "h", "148", "Perché il lattato si forma nel muscolo ma viene usato per la gluconeogenesi nel fegato?", [
  'Il rapporto NAD⁺/NADH è basso nel muscolo e alto nel fegato',
  'Il muscolo non ha la lattato deidrogenasi',
  'Il fegato non ha la piruvato chinasi',
  'Il lattato è prodotto solo dal fegato e poi ceduto al muscolo',
  'Nel muscolo il lattato viene ossidato a CO₂ e nel fegato viene ridotto a glucosio',
  ], 0,
  "Sotto sforzo la LDH muscolare riduce il piruvato; nel fegato ossida il lattato a piruvato. La stessa reazione all'equilibrio va in direzioni opposte secondo le concentrazioni.")
q("h5g-07", T, "h", "148", "Che cosa fa il cuore con il lattato prodotto dal muscolo scheletrico?", [
  'Lo ossida a piruvato con la LDH-1 e lo usa nel Krebs',
  'Lo trasforma in glucosio con la gluconeogenesi',
  'Lo accumula come glicogeno',
  'Lo elimina con le urine',
  'Lo trasforma in corpi chetonici, che poi cede al cervello durante il digiuno',
  ], 0,
  'Il lattato è anche un combustibile, non solo uno scarto.')
q("h5g-08", T, "h", "141", "Qual è il percorso dell'alanina muscolare fino al glucosio?", [
  'Al fegato, dove la transaminazione dà piruvato per la gluconeogenesi',
  'Viene ossidata nel muscolo a CO₂ e il carbonio non arriva al fegato',
  'Diventa direttamente glicerolo nel tessuto adiposo',
  'Entra nel fegato come acetil-CoA e attiva la piruvato carbossilasi',
  'Diventa lattato nel muscolo, che poi viene ossidato dal cuore',
  ], 0,
  "Il gruppo amminico va all'urea. È il ciclo glucosio-alanina (dettaglio con il metabolismo degli amminoacidi).")

T = "m5-regolazione"
q("h5n-01", T, "h", "153–154", "Come agisce l'enzima bifunzionale PFK2/FBPasi2 dopo un pasto e a digiuno?", [
  'Pasto: defosforilato, sale il F2,6BP; digiuno: fosforilato, cala il F2,6BP',
  'Pasto: fosforilato, degrada il F2,6BP; digiuno: defosforilato, lo produce',
  'A digiuno produce più F2,6BP per sostenere la gluconeogenesi',
  'È regolato solo dal glucosio, non da insulina e glucagone',
  'Produce fruttosio 1,6-bisfosfato, che attiva la PFK1 dopo il pasto',
  ], 0,
  'Dopo il pasto (insulina) lavora il dominio chinasico e prevale la glicolisi; a digiuno (glucagone, PKA) lavora il dominio fosfatasico e prevale la gluconeogenesi. Il F2,6BP attiva la PFK1 e inibisce la FBPasi1.',
  note="Sbobina di Biochimica II, p. 154: c'è scritto che con l'insulina si attiva il dominio fosfatasico (N-terminale) e con il glucagone quello chinasico (C-terminale). È il contrario, come dice la stessa sbobina una pagina prima (p. 153): l'insulina attiva la chinasi (più F2,6BP), il glucagone la fosfatasi. Inoltre nel fegato il dominio chinasico è N-terminale e quello fosfatasico C-terminale.")
q("h5n-02", T, "h", "151–152", "Come fa l'insulina a ridurre la quantità di PEPCK nel fegato?", [
  'Tramite la PKB fa degradare FOXO1, che attiva il gene della PEPCK',
  'Defosforila la PEPCK con la PP1 e la rende inattiva',
  'Inibisce allostericamente la PEPCK tramite il F2,6BP',
  'Aumenta il cAMP, che reprime il gene della PEPCK',
  'Attiva il GRE del promotore della PEPCK insieme al cortisolo',
  ], 0,
  'La PKB fosforila FOXO1, che viene degradato (ubiquitina-proteasoma). La PEPCK è regolata soprattutto a livello di trascrizione.',
  note="Sbobina di Biochimica II, p. 151: il fattore è chiamato «FOX1»; il nome corretto è FOXO1.")
q("h5n-03", T, "h", "151", "Quali elementi di risposta del promotore della PEPCK aumentano la sua trascrizione?", [
  'GRE, TRE e CRE',
  "Solo l'IRE",
  'GRE e IRE',
  'Solo il CRE',
  'Nessuno: la PEPCK non è regolata a livello genico ma solo allostericamente',
  ], 0,
  "GRE: glucocorticoidi; TRE: ormoni tiroidei; CRE: cAMP (glucagone). L'IRE (insulina) la riduce.")
q("h5n-04", T, "h", "152", "Perché nel fegato la piruvato chinasi deve essere inibita durante la gluconeogenesi?", [
  'Per evitare il ciclo futile PEP → piruvato → PEP',
  'Perché la piruvato chinasi produce glucosio',
  'Perché la PK consuma PEP solo nel muscolo',
  'Perché la PK attiva la PEPCK',
  'Non serve inibirla, perché nel fegato la PK non è espressa',
  ], 0,
  'Il ciclo futile consumerebbe ATP e GTP. Il glucagone fosforila e inattiva la PK epatica (forma L); le altre cellule non fanno gluconeogenesi e la loro PK non risponde al glucagone.')
q("h5n-05", T, "h", "155", "Quali effettori regolano allostericamente la fruttosio 1,6-bisfosfatasi?", [
  'È inibita da F2,6BP e AMP',
  'È attivata da F2,6BP e AMP',
  "È inibita dal citrato e dall'acetil-CoA",
  "È attivata dall'insulina tramite la PKB",
  'È inibita dal glucagone tramite la PKA, che la fosforila',
  ], 0,
  'Quando servono glicolisi o energia, la gluconeogenesi si ferma: regolazione reciproca rispetto alla PFK1.')
q("h5n-06", T, "h", "144–155", "Perché l'acetil-CoA prodotto dalla β-ossidazione notturna favorisce la gluconeogenesi epatica?", [
  'Attiva la piruvato carbossilasi e inibisce la PDH',
  'Viene convertito direttamente in glucosio',
  'Attiva la piruvato chinasi epatica',
  'Inibisce la PEPCK mitocondriale',
  'Aumenta il F2,6BP e attiva la PFK1 nel fegato durante la notte',
  ], 0,
  "Il piruvato viene indirizzato verso ossalacetato e glucosio invece che verso acetil-CoA. Gli acidi grassi danno al fegato l'energia per la gluconeogenesi, non il carbonio.",
  note="Sbobina di Biochimica II, p. 155: il primo enzima regolato è chiamato «piruvato carbossichinasi»; è la piruvato carbossilasi.")
q("h5n-07", T, "h", "156–157", "Il glucagone aumenta la glicemia agendo contemporaneamente su più enzimi epatici. Quale combinazione è corretta?", [
  'Fosforilasi ↑, sintasi ↓, F2,6BP ↓, PK epatica ↓, PEPCK ↑',
  'Sintasi ↑, PK epatica ↑, F2,6BP ↑',
  'F2,6BP ↑ e PFK1 ↑, con glicolisi epatica attiva',
  'PEPCK ↓ e glicolisi ↑, per produrre ATP',
  'Agisce solo sulla glicogeno fosforilasi e non tocca la gluconeogenesi',
  ], 0,
  'Tutti gli effetti partono da cAMP e PKA: fosforilazione di fosforilasi chinasi, glicogeno sintasi, PFK2/FBPasi2 e piruvato chinasi, più la trascrizione della PEPCK tramite CREB.')
q("h5n-08", T, "h", "156", "Quali fattori stimolano e quali inibiscono la secrezione di glucagone?", [
  'Stimolano ipoglicemia, amminoacidi e catecolamine; inibiscono iperglicemia e insulina',
  'Stimolano iperglicemia e insulina; inibiscono ipoglicemia e amminoacidi',
  'Stimolano acidi grassi e corpi chetonici; inibiscono gli amminoacidi',
  "Stimola la somatostatina; inibisce l'adrenalina",
  'Il glucagone viene secreto in modo costante, indipendentemente dalla glicemia',
  ], 0,
  'Gli amminoacidi stimolano sia insulina sia glucagone: così un pasto proteico non causa ipoglicemia.')

T = "m5-approfondimenti"
q("h5a-01", T, "h", "158", "Una persona a digiuno beve molto alcol la sera e va in ipoglicemia. Quale meccanismo?", [
  "Il NADH prodotto dall'etanolo blocca lattato → piruvato e malato → ossalacetato",
  "L'etanolo stimola la secrezione di insulina dalle cellule β",
  "L'etanolo attiva la glicogeno sintasi e sottrae glucosio",
  "L'acetaldeide inibisce la glucosio 6-fosfatasi del reticolo",
  "L'etanolo viene trasformato in glicogeno e il fegato smette di liberare glucosio nel sangue",
  ], 0,
  "L'ossidazione dell'etanolo (alcol e aldeide deidrogenasi) aumenta il NADH citosolico e la gluconeogenesi si ferma. A digiuno il glicogeno è già esaurito.",
  note="Sbobina di Biochimica II, p. 158: c'è scritto che l'acetaldeide «viene ulteriormente ossidata ad ossalacetato». Viene ossidata ad acetato.")
q("h5a-02", T, "h", "157", "Nel digiuno prolungato (oltre alcuni giorni) la gluconeogenesi diminuisce. Perché e come si compensa?", [
  'Per risparmiare le proteine muscolari; il cervello usa i corpi chetonici',
  'Perché finisce il glicerolo e la gluconeogenesi non ha substrati',
  "Perché aumenta l'insulina, che blocca la PEPCK",
  'Perché il cervello smette di consumare energia',
  'Perché il glicogeno epatico si ricostituisce e sostituisce la gluconeogenesi',
  ], 0,
  "Le proteine muscolari sono la principale fonte di substrati; il fegato produce corpi chetonici che il cervello impara a usare. Nell'anoressia grave questo risparmio non riesce.")
q("h5a-03", T, "h", "158–159", "Quale distribuzione metabolica nel lobulo epatico è corretta secondo il corso?", [
  'Periportali: β-ossidazione, gluconeogenesi, urea; perivenosi: glicolisi, lipogenesi',
  'Tutti gli epatociti fanno le stesse vie con la stessa intensità',
  'Periportali: glicolisi e lipogenesi; perivenosi: gluconeogenesi e urea',
  'Solo i perivenosi fanno gluconeogenesi, perché hanno più ossigeno',
  'Perivenosi: urea e β-ossidazione; periportali: sintesi di glutammina e lipoproteine',
  ], 0,
  'I periportali ricevono più O₂; i perivenosi sintetizzano anche glutammina. È un gradiente plastico: in caso di danno le zone possono cambiare funzione.')
q("h5a-04", T, "h", "153", "Nel topo transgenico con PEPCK sovraespressa nel muscolo, quale fenotipo è stato osservato?", [
  'Corsa molto più lunga, più acidi grassi, meno lattato, ma aggressività',
  'Ipoglicemia grave e incapacità di correre',
  'Obesità e diabete per eccesso di gluconeogenesi',
  'Incapacità di correre per accumulo di lattato',
  "Accumulo di glicogeno muscolare e ridotta sensibilità all'insulina",
  ], 0,
  "Avevano anche più mitocondri e più sensibilità all'insulina. Un singolo enzima può cambiare l'intero metabolismo.")
q("h5a-05", T, "h", "156", "Nei primi giorni di jet lag, che cosa succede alla regolazione notturna della glicemia?", [
  "La PEPCK resta sull'orario di partenza: glicemia notturna meno regolata",
  'La gluconeogenesi si blocca definitivamente dopo il viaggio',
  'La glicemia aumenta di notte per eccesso di insulina',
  'Il glicogeno non viene più usato durante la notte',
  'Non cambia nulla, perché la melatonina regola subito anche la PEPCK',
  ], 0,
  'La sintesi circadiana di PEPCK è guidata dal cortisolo. Il consiglio della sbobina è spostare la cena più tardi nei primi giorni.')
q("h5a-06", T, "h", "149", "Un paziente diabetico inizia una terapia con cortisone ad alte dosi. Che cosa ti aspetti sulla glicemia e perché?", [
  "Peggiora: più gluconeogenesi e meno sensibilità all'insulina",
  "Migliora per l'effetto antinfiammatorio sul pancreas",
  'Ipoglicemia per aumento della secrezione di insulina',
  "Nessun effetto sulla glicemia, solo sull'infiammazione",
  'Cala per aumento della glicogenolisi muscolare, che consuma glucosio',
  ], 0,
  'Il cortisone è un farmaco «da maneggiare con cura» nei diabetici.')
q("h5a-07", T, "h", "156", "Perché le cellule α del pancreas, con GLUT1, aumentano la secrezione di glucagone quando la glicemia cala?", [
  'Un flusso costante di glucosio inibisce il glucagone; se cala, la cellula α si attiva',
  'Il GLUT1 trasporta il glucagone fuori dalla cellula α',
  'Le cellule α hanno GLUT2 e si comportano come le β',
  "L'insulina attiva le cellule α durante l'ipoglicemia",
  'Le cellule α sono insensibili al glucosio e rispondono solo alle catecolamine',
  ], 0,
  "È l'ipotesi del corso. Si è visto anche che, se le cellule β sono danneggiate, alcune cellule α possono trasformarsi in β.")
q("h5a-08", T, "h", "157", "Perché una terapia cortisonica prolungata (es. in un paziente oncologico) porta a perdita di massa muscolare?", [
  'Mantiene una gluconeogenesi continua dalle proteine muscolari',
  'Inibisce la sintesi di glicogeno muscolare',
  'Blocca la β-ossidazione nel muscolo',
  "Aumenta l'insulina e la lipogenesi",
  'Inibisce la PEPCK epatica e costringe il muscolo a produrre glucosio',
  ], 0,
  'È lo stesso meccanismo del digiuno prolungato senza risparmio proteico.')
