"""Blocco 2 – Ingresso del glucosio e glicolisi (sbobina di Biochimica II, p. 31–73)."""
from bank_common import q

T = "m2-ingresso"
q("m2i-01", T, "f", "31", "Quale enzima digerisce l'amido nella bocca e nell'intestino?", ["α-amilasi", "β-amilasi", "Lattasi", "Glicogeno fosforilasi"], 0,
  "L'α-amilasi salivare e pancreatica scinde i legami α1-4; l'uomo non ha enzimi per i legami β della cellulosa.")
q("m2i-02", T, "f", "33", "Quale trasportatore è richiamato sulla membrana dall'insulina?", ["GLUT1", "GLUT2", "GLUT3", "GLUT4"], 3,
  "Muscolo scheletrico, cuore e tessuto adiposo: i GLUT4 stanno in vescicole e l'insulina ne fa fondere le vescicole con la membrana.")
q("m2i-03", T, "f", "33", "Quanti segmenti transmembrana hanno i trasportatori GLUT?", ["7", "12", "4", "24"], 1,
  "Struttura comune a 12 eliche transmembrana, con due conformazioni (T1 verso l'esterno, T2 verso l'interno).")
q("m2i-04", T, "m", "32", "Come entra il glucosio dal lume intestinale nell'enterocita?", [
  "Per diffusione facilitata con GLUT2", "In simporto con Na⁺ tramite SGLT1, sfruttando il gradiente mantenuto dalla pompa Na⁺/K⁺", "Per endocitosi", "Con un'ATPasi specifica per il glucosio"], 1,
  "È un trasporto attivo secondario: l'SGLT1 non consuma ATP, lo consuma la Na⁺/K⁺-ATPasi.",
  note="Sbobina di Biochimica II, p. 32: chiama il trasportatore «SGLUT1» e lo descrive prima come «trasportatore attivo che utilizza ATP». Il nome corretto è SGLT1 ed è attivo secondario.")
q("m2i-05", T, "m", "34", "Perché il cervello riceve glucosio anche a glicemia bassa?", [
  "Perché usa GLUT2, ad alta capacità", "Perché GLUT1 (barriera ematoencefalica) e GLUT3 (neuroni) hanno Kt molto basse", "Perché è insulino-dipendente", "Perché usa SGLT1"], 1,
  "GLUT3 ha Kt ≈ 0,1 mM: lavora vicino alla saturazione anche con poco glucosio.")
q("m2i-06", T, "m", "34", "Che cosa innesca la secrezione di insulina nella cellula β?", [
  "L'aumento di ATP, che chiude i canali K⁺, depolarizza e fa entrare Ca²⁺", "L'apertura dei canali K⁺", "Il legame del glucosio a un recettore di membrana", "L'aumento di AMP ciclico da glucagone"], 0,
  "Glucosio → GLUT2 → glucochinasi → glicolisi e fosforilazione ossidativa → ATP ↑ → canali K⁺ chiusi → Ca²⁺ in entrata → esocitosi.")
q("m2i-07", T, "a", "33–34", "Dopo un pasto la glicemia passa da 4,5 a 9 mM. Quale trasportatore aumenta di più il suo flusso?", ["GLUT1 (Kt 3 mM)", "GLUT2 (Kt 17 mM)", "GLUT3 (Kt 0,1 mM)", "Aumentano tutti in proporzione uguale"], 1,
  "Con Kt alta il GLUT2 è lontano dalla saturazione e il flusso cresce quasi in proporzione alla glicemia: per questo fegato e pancreas «sentono» il pasto.")
q("m2i-08", T, "a", "36", "Paziente con iperglicemia e peptide C assente. Che cosa indica?", [
  "Insulino-resistenza con produzione normale di insulina", "Mancata produzione di insulina (deficit delle cellule β)", "Eccesso di glucagone", "Difetto dei GLUT2 epatici"], 1,
  "Il peptide C si libera dal taglio della proinsulina: se manca, l'insulina non viene prodotta. Se è normale con iperglicemia, il problema è la resistenza (GLUT4).")
q("m2i-09", T, "l", "31", "Quale enzima dell'orletto a spazzola scinde i frammenti di amido con legami α1-6 (destrine limite)?", ["Isomaltasi", "Saccarasi", "Lattasi", "Maltasi acida"], 0,
  "L'isomaltasi (α-destrinasi) completa la digestione dell'amilopectina; saccarasi e lattasi agiscono su saccarosio e lattosio.")
q("m2i-10", T, "l", "33", "Che cosa indica la Kt di un GLUT?", ["La concentrazione di glucosio a cui il trasporto è a metà della velocità massima", "Il numero di glucosi trasportati al secondo", "La costante di equilibrio del trasporto", "La concentrazione intracellulare di glucosio"], 0,
  "È l'equivalente della KM per un trasportatore: più è bassa, più il trasportatore è affine.")

T = "m2-fosforilazione"
q("m2f-01", T, "f", "37", "Quale enzima fosforila il glucosio negli epatociti?", ["Esochinasi I", "Glucochinasi (esochinasi IV)", "Fosfoglucomutasi", "Glucosio 6-fosfatasi"], 1,
  "Fegato e cellule β del pancreas usano la glucochinasi, a bassa affinità.")
q("m2f-02", T, "f", "38", "Perché il glucosio fosforilato resta intrappolato nella cellula?", ["Perché il G6P è carico negativamente e non ha trasportatori", "Perché si lega alle proteine", "Perché viene subito polimerizzato", "Perché è più grande"], 0,
  "Le cariche negative del fosfato impediscono l'uscita attraverso i GLUT.")
q("m2f-03", T, "m", "55", "Come viene regolata l'esochinasi ubiquitaria?", ["È inibita dal suo prodotto, il glucosio 6-fosfato", "È attivata dall'insulina", "È inibita dall'ATP", "È sequestrata nel nucleo"], 0,
  "Il G6P si lega a un sito allosterico e la inibisce.")
q("m2f-04", T, "m", "55–56", "Come viene regolata la glucochinasi epatica?", [
  "Per compartimentazione: legata a una proteina regolatrice nel nucleo è inattiva, nel citosol è attiva",
  "Per inibizione da glucosio 6-fosfato", "Per fosforilazione da PKA", "Non è regolata"], 0,
  "Molto glucosio libera la glucochinasi dalla proteina regolatrice; il fruttosio 6-P la riporta nel nucleo.")
q("m2f-05", T, "m", "40", "Perché l'esochinasi chiude il sito attivo quando legano glucosio e ATP (adattamento indotto)?", [
  "Per escludere l'acqua ed evitare l'idrolisi improduttiva dell'ATP", "Per aumentare la KM", "Per legare il Mg²⁺", "Per far uscire il G6P"], 0,
  "Il fosfato γ deve andare sul C6 del glucosio, non all'acqua.")
q("m2f-06", T, "a", "37–38", "Perché il fegato usa un enzima con KM alta per il glucosio?", [
  "Per fosforilare il glucosio solo quando la glicemia è alta, lasciandolo prima agli altri organi",
  "Perché così consuma meno ATP", "Perché la glucochinasi è più veloce dell'esochinasi a ogni concentrazione", "Per inibire la glicolisi"], 0,
  "A digiuno la glucochinasi lavora poco e il glucosio resta disponibile per cervello ed eritrociti; dopo il pasto il fegato immagazzina l'eccesso.")
q("m2f-07", T, "a", "38", "Il glucosio 6-fosfato è un crocevia. Quale via non parte da lui?", ["Glicolisi", "Via dei pentoso fosfati", "Sintesi del glicogeno", "β-ossidazione"], 3,
  "Il G6P va in glicolisi, pentoso fosfati, glicogeno o (nel fegato) torna glucosio.")
q("m2f-08", T, "l", "37", "Come si chiama anche la glucochinasi?", ["Esochinasi IV", "Esochinasi II", "Fruttochinasi", "Fosfoesoso chinasi"], 0,
  "È l'isoenzima IV della famiglia delle esochinasi.")
q("m2f-09", T, "l", "37", "Quanto vale circa la KM dell'esochinasi per il glucosio secondo la sbobina?", ["0,1 mM", "10 mM", "1 mM", "17 mM"], 0,
  "Esochinasi ≈ 0,1 mM, glucochinasi ≈ 10 mM: circa 100 volte di differenza.")

T = "m2-glicolisi"
q("m2g-01", T, "f", "38", "Dove avviene la glicolisi?", ["Nel citosol", "Nella matrice mitocondriale", "Nel reticolo endoplasmatico", "Nel nucleo"], 0,
  "È una via citosolica e non richiede ossigeno.")
q("m2g-02", T, "f", "47", "Bilancio netto della glicolisi per una molecola di glucosio:", ["2 piruvato, 2 ATP, 2 NADH", "2 piruvato, 4 ATP, 2 NADH", "2 lattato, 2 ATP", "2 acetil-CoA, 2 ATP, 2 NADH"], 0,
  "4 ATP prodotti − 2 spesi = 2 netti; 2 NADH dalla gliceraldeide 3-P deidrogenasi.")
q("m2g-03", T, "f", "39", "Quale enzima scinde il fruttosio 1,6-bisfosfato in due triosi?", ["Aldolasi", "Trioso fosfato isomerasi", "Enolasi", "Fosfofruttochinasi 1"], 0,
  "Si formano diidrossiacetone fosfato e gliceraldeide 3-fosfato.")
q("m2g-04", T, "f", "44", "Quante reazioni di fosforilazione a livello del substrato ci sono nella glicolisi?", ["Una", "Due", "Tre", "Quattro"], 1,
  "Fosfoglicerato chinasi e piruvato chinasi.")
q("m2g-05", T, "m", "41", "Perché la reazione dell'aldolasi procede verso destra pur avendo ΔG°' positivo?", [
  "Perché i triosi vengono consumati subito e il ΔG reale diventa vicino a zero", "Perché è accoppiata all'idrolisi di ATP", "Perché è irreversibile", "Perché è attivata dall'AMP"], 0,
  "Per legge di azione di massa: nelle concentrazioni cellulari il ΔG è circa −0,2 kJ/mol.")
q("m2g-06", T, "m", "43", "Che cosa succede nella reazione della gliceraldeide 3-fosfato deidrogenasi?", [
  "L'aldeide viene ossidata e il fosfato inorganico forma un legame anidridico misto ad alta energia",
  "Viene consumato ATP", "Si forma CO₂", "Viene ridotto il FAD"], 0,
  "È l'unica ossidoriduzione della glicolisi: si forma 1,3-BPG e NADH.")
q("m2g-07", T, "m", "45", "Perché la piruvato chinasi è così esoergonica?", [
  "Perché la forma enolica del piruvato tautomerizza subito nella forma chetonica, molto più stabile", "Perché consuma due ATP", "Perché libera CO₂", "Perché il PEP è un tioestere"], 0,
  "L'idrolisi del PEP (−62 kJ/mol) basta a formare ATP (+30) con ΔG°' complessivo di circa −32 kJ/mol.")
q("m2g-08", T, "m", "47", "La glicolisi è un processo:", ["Acidificante, perché produce 2 H⁺", "Alcalinizzante", "Neutro", "Che consuma protoni"], 0,
  "Glucosio + 2 NAD⁺ + 2 ADP + 2 Pi → 2 piruvato + 2 NADH + 2 H⁺ + 2 ATP + 2 H₂O.")
q("m2g-09", T, "a", "43", "Lo iodoacetato blocca la glicolisi. Su quale enzima agisce e come?", [
  "Gliceraldeide 3-P deidrogenasi, alchilando la cisteina del sito attivo", "Piruvato chinasi, competendo con il PEP", "Aldolasi, legando il FBP", "Esochinasi, sostituendo l'ATP"], 0,
  "Il gruppo SH della cisteina catalitica viene legato covalentemente e l'enzima perde l'attività.")
q("m2g-10", T, "a", "47", "Se in una soluzione con tutti gli enzimi glicolitici manca il NAD⁺, dove si ferma la via?", [
  "Alla gliceraldeide 3-fosfato", "Al fruttosio 1,6-bisfosfato", "Al fosfoenolpiruvato", "Non si ferma"], 0,
  "La gliceraldeide 3-P deidrogenasi richiede NAD⁺: per questo il NADH va sempre riossidato (fermentazione o navette).")
q("m2g-11", T, "a", "47", "Delle reazioni della glicolisi, quale ha ΔG°' negativo ma ΔG reale vicino a zero nella cellula?", [
  "Fosfoglicerato chinasi", "Piruvato chinasi", "Fosfofruttochinasi 1", "Esochinasi"], 0,
  "Con le concentrazioni reali la fosfoglicerato chinasi è all'equilibrio, per questo non è un punto di regolazione.")
q("m2g-12", T, "a", "45", "Come funziona la fosfoglicerato mutasi?", [
  "Un'istidina fosforilata cede il fosfato al C2 (intermedio 2,3-BPG), poi riprende quello in C3",
  "Sposta direttamente il fosfato dal C3 al C2 senza intermedi", "Usa ATP per fosforilare il C2", "Idrolizza il fosfato in C3"], 0,
  "L'enzima va attivato con il 2,3-bisfosfoglicerato, che lo fosforila.")
q("m2g-13", T, "l", "40", "Nella glicolisi, come si chiama l'enzima che converte il glucosio 6-fosfato in fruttosio 6-fosfato?", [
  "Fosfoesoso isomerasi (fosfoglucosio isomerasi)", "Fosfoglucomutasi", "Trioso fosfato isomerasi", "Fosfofruttochinasi 2"], 0,
  "Aldoso → chetoso. Non va confusa con la fosfoglucomutasi (G1P ⇌ G6P).")
q("m2g-14", T, "l", "39", "Nell'aldolasi, quali carboni del fruttosio 1,6-bisfosfato diventano il diidrossiacetone fosfato?", ["C1–C3", "C4–C6", "C2–C4", "C1, C2, C6"], 0,
  "La scissione è tra C3 e C4: C1–C3 → DHAP, C4–C6 → gliceraldeide 3-P.")
q("m2g-15", T, "l", "40", "Il prodotto della gliceraldeide 3-P deidrogenasi si chiama:", ["1,3-bisfosfoglicerato", "2,3-bisfosfoglicerato", "3-fosfoglicerato", "Glicerolo 3-fosfato"], 0,
  "Il fosfato aggiunto è in C1 (anidride mista), quello in C3 era già presente.")
q("m2g-16", T, "l", "41", "Nella glicolisi la reazione della PFK1 forma quale legame?", ["Fosfoestere sul C1 del fruttosio 6-P", "Fosfoanidridico", "Glicosidico", "Tioestere"], 0,
  "Il fosfato γ dell'ATP esterifica l'OH del C1.")

T = "m2-fermentazioni"
q("m2r-01", T, "f", "49", "Qual è lo scopo della fermentazione lattica?", ["Rigenerare NAD⁺ per la glicolisi", "Produrre ATP aggiuntivo", "Eliminare il piruvato in eccesso", "Produrre glucosio"], 0,
  "Senza NAD⁺ la gliceraldeide 3-P deidrogenasi si ferma; la LDH riossida il NADH riducendo il piruvato.")
q("m2r-02", T, "f", "49", "Quali cellule fanno sempre fermentazione lattica?", ["Eritrociti", "Epatociti", "Cardiomiociti", "Neuroni"], 0,
  "Non hanno mitocondri.")
q("m2r-03", T, "m", "50", "Quanti isoenzimi della LDH esistono e perché?", ["5, dalle combinazioni di subunità H e M nel tetramero", "2, H e M", "4, uno per subunità", "3, cuore, muscolo e fegato"], 0,
  "H4, H3M, H2M2, HM3, M4.")
q("m2r-04", T, "m", "53", "Nella fermentazione alcolica, quali sono le due tappe?", [
  "Decarbossilazione del piruvato ad acetaldeide, poi riduzione ad etanolo con NADH", "Riduzione del piruvato a lattato, poi decarbossilazione", "Ossidazione dell'acetaldeide ad acetato", "Carbossilazione del piruvato"], 0,
  "La prima è irreversibile (si perde CO₂), la seconda reversibile (alcol deidrogenasi).")
q("m2r-05", T, "a", "52", "Secondo la sbobina, perché la riduzione del piruvato a lattato non acidifica la cellula?", [
  "Perché la LDH consuma un H⁺ (NADH + H⁺) e il lattato esce con un H⁺ dal trasportatore dei monocarbossilati",
  "Perché il lattato è un acido debole", "Perché la reazione libera OH⁻", "Perché il lattato viene subito ossidato"], 0,
  "L'acidificazione muscolare viene soprattutto dall'idrolisi dell'ATP; il lattato esce con un protone verso il sangue.",
  note="Il ruolo del lattato nell'acidosi è dibattuto: alcuni testi (Lehninger) attribuiscono l'acidificazione all'acido lattico. All'esame segui l'impostazione della sbobina.")
q("m2r-06", T, "a", "53", "Perché l'assunzione di molto etanolo può dare ipoglicemia e acidosi lattica?", [
  "Perché l'ossidazione dell'etanolo produce NADH: piruvato → lattato e la gluconeogenesi da lattato si blocca",
  "Perché l'etanolo inibisce l'insulina", "Perché l'acetaldeide blocca la glicolisi", "Perché l'etanolo consuma NADH"], 0,
  "Con rapporto NADH/NAD⁺ alto il fegato non può ossidare il lattato a piruvato.")
q("m2r-07", T, "l", "49", "Quale stereoisomero del lattato si forma nell'uomo?", ["L-lattato (S)", "D-lattato (R)", "Una miscela racemica", "Meso-lattato"], 0,
  "La LDH umana è stereospecifica e forma L-lattato.",
  note="Sbobina di Biochimica II, p. 49: c'è scritto che si forma l'isomero «R». L'L-lattato è (S).")
q("m2r-08", T, "l", "53", "Quale metallo contiene l'alcol deidrogenasi?", ["Zinco", "Ferro", "Magnesio", "Rame"], 0,
  "È uno dei motivi per cui lo zinco è necessario nella dieta.")
q("m2r-09", T, "l", "52", "L'isoenzima LDH1 corrisponde a:", ["H4 (cardiaco)", "M4 (muscolare)", "H2M2", "M3H"], 0,
  "LDH1 = H4, LDH5 = M4.")

T = "m2-navette"
q("m2n-01", T, "f", "53", "Perché servono i sistemi navetta?", [
  "Perché la membrana mitocondriale interna è impermeabile al NADH", "Perché il NADH è instabile nel citosol", "Per trasportare ATP", "Per portare il piruvato nel mitocondrio"], 0,
  "Si trasferiscono gli elettroni del NADH citosolico, non la molecola.")
q("m2n-02", T, "m", "54", "Nella navetta del glicerolo fosfato, a chi cede gli elettroni il glicerolo 3-fosfato?", ["Al FAD della glicerolo 3-P deidrogenasi mitocondriale", "Al NAD⁺ mitocondriale", "Direttamente all'O₂", "Al citocromo c"], 0,
  "Poi passano al coenzima Q: si formano circa 1,5 ATP per NADH citosolico.")
q("m2n-03", T, "a", "54", "Perché con la navetta malato-aspartato si ricava più ATP che con quella del glicerolo fosfato?", [
  "Perché gli elettroni arrivano al NAD⁺ mitocondriale ed entrano dal complesso I",
  "Perché trasporta due NADH", "Perché non consuma ATP", "Perché produce GTP"], 0,
  "NADH mitocondriale ≈ 2,5 ATP contro FADH₂ ≈ 1,5.",
  note="La sbobina descrive in dettaglio solo la navetta del glicerolo fosfato.")
q("m2n-04", T, "l", "54", "Nella navetta del glicerolo fosfato, l'enzima citosolico usa NADH; quello mitocondriale usa FAD. Come si chiamano?", [
  "Glicerolo 3-fosfato deidrogenasi citosolica e mitocondriale", "Glicerolo chinasi e glicerolo fosfatasi", "Malato deidrogenasi citosolica e mitocondriale", "Trioso fosfato isomerasi e aldolasi"], 0,
  "Sono due isoenzimi della glicerolo 3-fosfato deidrogenasi.",
  note="Sbobina di Biochimica II, p. 54: il glicerolo 3-fosfato è chiamato «3-fosfoglicerolo (3-PG)». Non va confuso con il 3-fosfoglicerato.")

T = "m2-regolazione"
q("m2reg-01", T, "f", "57", "Qual è il principale punto di regolazione della glicolisi?", ["Fosfofruttochinasi 1", "Aldolasi", "Enolasi", "Fosfoglicerato chinasi"], 0,
  "È il primo passaggio di non ritorno specifico della glicolisi.")
q("m2reg-02", T, "f", "58", "Quali sono gli effettori allosterici positivi della PFK1?", ["AMP e fruttosio 2,6-bisfosfato", "ATP e citrato", "Acetil-CoA e NADH", "Glucosio 6-P e insulina"], 0,
  "Negativi: ATP e citrato.")
q("m2reg-03", T, "m", "59", "Perché l'AMP è un segnale così sensibile della carica energetica?", [
  "Perché l'adenilato chinasi (2 ADP ⇌ ATP + AMP) amplifica: una piccola diminuzione di ATP fa aumentare di molto l'AMP in percentuale",
  "Perché è il più abbondante dei tre nucleotidi", "Perché inibisce direttamente l'ATP sintasi", "Perché viene prodotto dal glucagone"], 0,
  "Con ATP 1 mM e AMP 0,02 mM, consumare 0,1 mM di ATP fa salire l'AMP a circa 0,07 mM (+300%).")
q("m2reg-04", T, "m", "60", "Che cosa significa che il fruttosio 1,6-bisfosfato attiva la piruvato chinasi «a feed-forward»?", [
  "Che il prodotto di un enzima a monte attiva un enzima a valle, preparando la via al flusso in arrivo",
  "Che il prodotto finale inibisce il primo enzima", "Che l'enzima è attivato dal suo substrato", "Che l'enzima è fosforilato"], 0,
  "Se la PFK1 è attiva, la piruvato chinasi viene accelerata per smaltire gli intermedi.")
q("m2reg-05", T, "m", "61", "Che effetto ha la fosforilazione della piruvato chinasi epatica indotta dal glucagone?", [
  "La inattiva, così il PEP prodotto dalla gluconeogenesi non torna a piruvato",
  "La attiva, per produrre più ATP", "Non cambia la sua attività", "La sposta nel mitocondrio"], 0,
  "Evita il ciclo futile PEP → piruvato → OAA → PEP durante la gluconeogenesi.",
  note="Sbobina di Biochimica II, p. 61: c'è scritto che la fosforilazione «rallenta la glicolisi e quindi riduce la produzione di glucosio». Al contrario, favorisce la produzione di glucosio (gluconeogenesi) perché evita il ciclo futile.")
q("m2reg-06", T, "a", "58", "Nella PFK1, che cosa cambia tra forma R e forma T nel sito attivo?", [
  "In R c'è Arg162 positiva che attira il F6P; in T compare Glu161 negativo che lo respinge",
  "In R c'è una cisteina, in T una serina", "In T il sito attivo è occupato dall'ATP", "Non cambia nulla, cambia solo la Vmax"], 0,
  "Il cambio di residuo spiega la diversa affinità per il fruttosio 6-fosfato.")
q("m2reg-07", T, "a", "60", "Nel fegato, quale effettore della PFK1 è il più potente e perché?", [
  "Il fruttosio 2,6-bisfosfato, perché agisce a concentrazioni micromolari", "L'ATP, perché è il più abbondante", "Il citrato, perché è il più stabile", "L'AMP, perché è un substrato"], 0,
  "Poi viene l'AMP; ATP e citrato agiscono a concentrazioni più alte.")
q("m2reg-08", T, "a", "56", "Perché la glucochinasi viene riportata nel nucleo quando si accumula fruttosio 6-fosfato?", [
  "Perché se la glicolisi è ferma a valle è inutile continuare a fosforilare glucosio",
  "Perché il fruttosio 6-P è tossico", "Per favorire la gluconeogenesi da fruttosio", "Perché il F6P degrada l'enzima"], 0,
  "Il F6P attiva la proteina regolatrice, che sequestra la glucochinasi.")
q("m2reg-09", T, "l", "58", "Quale residuo della PFK1 compare nel sito attivo nella forma R?", ["Arginina 162", "Glutammato 161", "Lisina 162", "Istidina 161"], 0,
  "Arg162 (positiva) in R, Glu161 (negativo) in T.")
q("m2reg-10", T, "l", "59", "L'enzima che interconverte ATP, ADP e AMP si chiama:", ["Adenilato chinasi (miochinasi)", "Nucleotide difosfato chinasi", "AMP deaminasi", "Adenilato ciclasi"], 0,
  "2 ADP ⇌ ATP + AMP. Da non confondere con l'adenilato ciclasi, che forma cAMP.")
q("m2reg-11", T, "l", "60", "Quali sono gli effettori allosterici negativi della piruvato chinasi secondo la sbobina?", ["ATP e acetil-CoA", "AMP e F1,6BP", "Citrato e AMP", "ADP e NADH"], 0,
  "Positivi: AMP e fruttosio 1,6-bisfosfato.",
  note="Sbobina di Biochimica II, p. 60 e 62: a p. 60 l'acetil-CoA è un effettore negativo, a p. 62 c'è scritto che «l'ADP e l'acetil-CoA la attivano». La versione corretta è quella di p. 60: l'acetil-CoA inibisce.")

T = "m2-pasteur"
q("m2p-01", T, "f", "62", "Che cos'è l'effetto Pasteur?", [
  "La diminuzione del consumo di glucosio quando una cellula passa da anaerobiosi ad aerobiosi", "L'aumento della glicolisi in presenza di ossigeno", "La fermentazione alcolica nei lieviti", "L'inibizione della respirazione da parte del glucosio"], 0,
  "In aerobiosi la fosforilazione ossidativa produce molto ATP e la glicolisi rallenta.")
q("m2p-02", T, "m", "63", "Su quale enzima agisce soprattutto il citrato nell'effetto Pasteur?", ["Fosfofruttochinasi 1", "Esochinasi", "Piruvato chinasi", "Piruvato deidrogenasi"], 0,
  "Il citrato esce dal mitocondrio quando l'ATP è abbondante e inibisce la PFK1.",
  note="Sbobina di Biochimica II, p. 63: la PFK1 è definita «l'enzima che catalizza la prima reazione della glicolisi». È la terza reazione; è però il primo passaggio specifico e irreversibile della via.")
q("m2p-03", T, "m", "63", "Negli eritrociti, quale metabolita della glicolisi abbassa l'affinità dell'emoglobina per l'O₂?", ["2,3-bisfosfoglicerato", "1,3-bisfosfoglicerato", "Fosfoenolpiruvato", "Lattato"], 0,
  "Deriva dall'1,3-BPG tramite la bisfosfoglicerato mutasi (shunt di Rapoport-Luebering).")
q("m2p-04", T, "a", "63–64", "In un deficit di piruvato chinasi negli eritrociti, la curva di dissociazione dell'emoglobina si sposta:", [
  "A destra, perché si accumulano intermedi a monte e aumenta il 2,3-BPG", "A sinistra, perché manca il 2,3-BPG", "Non si sposta", "A destra, perché aumenta il lattato"], 0,
  "L'Hb cede più O₂, ma la cellula ha poco ATP: la pompa Na⁺/K⁺ funziona male, l'eritrocita si gonfia e viene eliminato (anemia emolitica).")
q("m2p-05", T, "a", "63", "In un deficit di esochinasi negli eritrociti, la curva di dissociazione dell'emoglobina si sposta:", [
  "La curva si sposta a sinistra: poco 2,3-BPG, Hb più affine all'O₂", "La curva si sposta a destra", "Non cambia nulla", "L'eritrocita produce più lattato"], 0,
  "Se la glicolisi non parte si forma poco 1,3-BPG e quindi poco 2,3-BPG.")
q("m2p-06", T, "a", "64 e seguenti (pagine non numerate)", "Nell'intolleranza ereditaria al fruttosio, perché il fegato va in sofferenza?", [
  "Manca l'aldolasi B: il fruttosio 1-P si accumula e sequestra fosfato, l'ATP crolla",
  "Manca la fruttochinasi: il fruttosio passa nelle urine", "Manca il GLUT5", "Il fruttosio inibisce la glucochinasi"], 0,
  "La fruttosuria essenziale (deficit di fruttochinasi) è invece benigna.")
q("m2p-07", T, "a", "64 e seguenti (pagine non numerate)", "Perché un eccesso di fruttosio favorisce la steatosi epatica?", [
  "Perché nel fegato entra nella glicolisi a valle della PFK1, saltando il principale punto di controllo",
  "Perché inibisce la β-ossidazione", "Perché non viene fosforilato", "Perché stimola il glucagone"], 0,
  "Il flusso non regolato verso piruvato e acetil-CoA alimenta la sintesi di acidi grassi.",
  note="Sbobina di Biochimica II, pagine non numerate dopo p. 64: nel paragrafo sugli sciroppi c'è scritto «glucosio» dove si intende fruttosio («sciroppo di glucosio (miscela formata prevalentemente da fruttosio)», «consumo eccessivo di glucosio... tossico»). Il riferimento corretto è allo sciroppo ad alto contenuto di fruttosio.")
q("m2p-08", T, "m", "64 e seguenti (pagine non numerate)", "Come entra il galattosio nella glicolisi?", [
  "Galattosio → galattosio 1-P → (scambio con UDP-glucosio) glucosio 1-P → glucosio 6-P",
  "Galattosio → fruttosio 6-P", "Galattosio → gliceraldeide 3-P", "Galattosio → glucosio libero per epimerizzazione diretta"], 0,
  "Galattochinasi, galattosio 1-P uridiltrasferasi, UDP-galattosio 4-epimerasi, fosfoglucomutasi.")
q("m2p-09", T, "l", "64 e seguenti (pagine non numerate)", "Quale enzima manca nella forma più frequente di galattosemia?", ["Galattosio 1-fosfato uridiltrasferasi", "Galattochinasi", "UDP-galattosio 4-epimerasi", "Lattasi"], 0,
  "Il galattosio si accumula; nel cristallino viene ridotto a galattitolo e causa cataratta.")
q("m2p-10", T, "l", "64 e seguenti (pagine non numerate)", "Nel fegato la triosio chinasi fosforila la gliceraldeide a:", ["Gliceraldeide 3-fosfato", "Gliceraldeide 2-fosfato", "Diidrossiacetone fosfato", "Glicerolo 3-fosfato"], 0,
  "Poi la GA3P prosegue nella glicolisi.",
  note="Sbobina di Biochimica II, pagine non numerate dopo p. 64: c'è scritto «gliceraldeide 2-fosfato». Il prodotto è la gliceraldeide 3-fosfato.")
q("m2p-11", T, "l", "63", "Come si chiama l'enzima eritrocitario che forma il 2,3-BPG?", ["Bisfosfoglicerato mutasi", "Fosfoglicerato chinasi", "Fosfoglicerato mutasi", "2,3-BPG sintasi mitocondriale"], 0,
  "Sposta il fosfato dal C1 al C2 dell'1,3-BPG.",
  note="Sbobina di Biochimica II, p. 63: c'è scritto «tramite una mutazione». Si intende tramite una mutasi.")
q("m2p-12", T, "l", "64 e seguenti (pagine non numerate)", "Il fruttosio 1-fosfato viene scisso da quale isoenzima dell'aldolasi?", ["Aldolasi B", "Aldolasi A", "Aldolasi C", "Fruttosio 1,6-bisfosfatasi"], 0,
  "L'aldolasi B (fegato) scinde F1P in DHAP e gliceraldeide.")

T = "m2-pdh"
q("m2d-01", T, "f", "65", "Che cosa produce la piruvato deidrogenasi?", ["Acetil-CoA, CO₂ e NADH", "Ossalacetato", "Lattato e NAD⁺", "Acetaldeide e CO₂"], 0,
  "Piruvato + CoA + NAD⁺ → acetil-CoA + CO₂ + NADH.")
q("m2d-02", T, "f", "66", "Quanti e quali coenzimi usa il complesso della piruvato deidrogenasi?", [
  "Cinque: TPP, lipoato, CoA, FAD, NAD⁺", "Tre: NAD⁺, FAD, CoA", "Due: NAD⁺ e biotina", "Quattro: TPP, biotina, NAD⁺, FAD"], 0,
  "Derivano da tiamina (B1), acido lipoico, pantotenato (B5), riboflavina (B2) e niacina (B3).")
q("m2d-03", T, "f", "65", "Dove si trova il complesso della piruvato deidrogenasi?", ["Nella matrice mitocondriale", "Nel citosol", "Nella membrana plasmatica", "Nel reticolo endoplasmatico"], 0,
  "Il piruvato entra nel mitocondrio con un trasportatore specifico, insieme a un protone.")
q("m2d-04", T, "m", "71", "Come viene regolata covalentemente la PDH?", [
  "La PDH chinasi la fosforila e la inattiva; la PDH fosfatasi la defosforila e la attiva",
  "La fosforilazione la attiva", "È regolata solo allostericamente", "La PKA la attiva in risposta al glucagone"], 0,
  "La fosforilazione avviene sull'E1 e blocca tutto il complesso.")
q("m2d-05", T, "m", "70", "Quali prodotti inibiscono la PDH (inibizione da prodotto)?", ["Acetil-CoA e NADH", "CO₂ e NADH", "ATP e AMP", "Piruvato e CoA"], 0,
  "L'acetil-CoA inibisce E2, il NADH inibisce E3.")
q("m2d-06", T, "m", "66–67", "Quali sono i vantaggi di un complesso multienzimatico?", [
  "Il prodotto passa subito all'enzima successivo, gli intermedi reattivi non si disperdono, e basta regolare un enzima per controllare tutto",
  "Usa meno coenzimi", "Non ha bisogno di regolazione", "Funziona anche senza NAD⁺"], 0,
  "Si supera il limite della diffusione e si regola tutto bloccando E1.")
q("m2d-07", T, "a", "69", "Perché nell'uomo i grassi non possono diventare zuccheri?", [
  "Perché la reazione della PDH è irreversibile: l'acetil-CoA non può tornare piruvato",
  "Perché gli acidi grassi non producono acetil-CoA", "Perché manca la glucochinasi", "Perché l'acetil-CoA inibisce la gluconeogenesi"], 0,
  "Gli zuccheri possono diventare grassi (via acetil-CoA), non il contrario. Fa eccezione il glicerolo dei trigliceridi.")
q("m2d-08", T, "a", "72", "Nel muscolo che si contrae, perché aumenta l'attività della PDH?", [
  "Il Ca²⁺ attiva la PDH fosfatasi, e l'ADP/piruvato inibiscono la chinasi",
  "L'ATP attiva la PDH", "Il NADH attiva la fosfatasi", "L'insulina fosforila la PDH"], 0,
  "Il calcio favorisce il legame della fosfatasi al complesso.")
q("m2d-09", T, "a", "73", "Un neonato con deficit di E1 della PDH presenterà soprattutto:", [
  "Acidosi lattica e problemi neurologici", "Ipoglicemia isolata", "Iperammoniemia", "Anemia emolitica"], 0,
  "Il piruvato non viene ossidato: il NADH si riossida solo con la fermentazione lattica; il cervello, che dipende dal glucosio, è il più colpito.")
q("m2d-10", T, "a", "73", "In ipossia, come agisce HIF sulla PDH?", [
  "Aumenta l'espressione della PDH chinasi: la PDH viene fosforilata e inibita", "Attiva la PDH fosfatasi", "Aumenta la sintesi di E1", "Non ha effetti sulla PDH"], 0,
  "Il piruvato viene dirottato verso il lattato: è uno dei meccanismi dell'effetto Warburg.")
q("m2d-11", T, "l", "66", "Come si chiama l'enzima E2 della PDH?", ["Diidrolipoil transacetilasi", "Diidrolipoil deidrogenasi", "Piruvato decarbossilasi", "Lipoamide sintasi"], 0,
  "E1 piruvato deidrogenasi (decarbossilazione), E2 transacetilasi (trasferimento al CoA), E3 diidrolipoil deidrogenasi (riossida il lipoato con FAD → NAD⁺).",
  note="Sbobina di Biochimica II, p. 68: lo scambio dell'acetile tra lipoato e CoA è attribuito all'«E3». Il trasferimento al CoA lo fa l'E2 (transacetilasi); l'E3 riossida il lipoato.")
q("m2d-12", T, "l", "68", "Come si chiama l'intermedio legato alla TPP dopo la decarbossilazione del piruvato?", ["Idrossietil-TPP", "Acetil-TPP", "Carbossietil-TPP", "Lattil-TPP"], 0,
  "Poi viene ossidato e trasferito all'acido lipoico come acetile (acetil-diidrolipoamide).")
q("m2d-13", T, "l", "67", "Il lipoato è legato covalentemente all'E2 tramite:", ["Un legame ammidico con una lisina (lipoamide)", "Un ponte disolfuro con una cisteina", "Un estere con una serina", "Un legame glicosidico"], 0,
  "Il lungo braccio lisina-lipoato oscilla tra E1 ed E3.")
q("m2d-14", T, "l", "67", "Il carbonio reattivo della tiamina pirofosfato si trova:", ["Nell'anello tiazolico, tra N e S", "Nell'anello pirimidinico", "Nel pirofosfato", "Nella catena laterale"], 0,
  "Il C2 del tiazolo si deprotona (carbanione/ilide) e attacca il carbonile del piruvato.",
  note="Sbobina di Biochimica II, p. 67: c'è scritto «derivata dall'enzima B1». Si intende la vitamina B1 (tiamina).")
