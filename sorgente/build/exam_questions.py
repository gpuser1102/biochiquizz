"""Domande d'esame proposte a lezione, deduplicate e risolte sulle sbobine -> data/exam.json.
ans = indice 0-3 della risposta giusta; opzioni nell'ordine originale.
times = in quanti gruppi di foto compare; pending = risposta da confermare (esclusa dal feed)."""
import json, os

Q = []
def q(id, topic, page, text, opts, ans, why, note=None, times=1, pending=False, src="Biochimica II"):
    Q.append(dict(id=id, topic=topic, page=page, src=src, q=text, opts=opts, ans=ans, why=why, note=note, times=times, pending=pending))

# ---------------- Termodinamica e ATP ----------------
q("eq", "m1-termodinamica", "10–12", "La definizione migliore per una reazione vicina all'equilibrio è:",
  ["avviene sempre con una variazione di energia libera", "ha una variazione di energia libera vicina a zero",
   "di solito è un punto di controllo di una via metabolica", "avviene molto lentamente"], 1,
  "Vicino all'equilibrio ΔG ≈ 0: la reazione è reversibile e il verso dipende solo dalle concentrazioni. I punti di controllo sono invece le reazioni con ΔG molto negativo.", times=2)
q("dg-dg0", "m1-termodinamica", "11–12", "Il ΔG differisce dal ΔG°' quando si ha:",
  ["una variazione della concentrazione di enzima", "una variazione della concentrazione degli ioni divalenti",
   "una variazione del Keq", "una diversa concentrazione dei reagenti e prodotti"], 3,
  "ΔG = ΔG°' + RT ln([prodotti]/[reagenti]): cambia con le concentrazioni. L'enzima cambia solo la velocità e la Keq è una costante.", times=2)
q("atp-ph", "m1-atp", "15", "L'energia libera standard della scissione dell'ATP in ADP e fosfato è −30 kJ/mole. Al pH fisiologico questo valore:",
  ["diviene più negativo", "diviene più positivo", "resta invariato", "dipende dalla concentrazione del magnesio"], 0,
  "Più alto è il pH, più l'idrolisi è favorita: a pH 7,4 il ΔG scende sotto −30 kJ/mol. Il magnesio stabilizza l'ATP, ma la domanda chiede l'effetto del pH.", times=2)
q("atp-legami", "m1-atp", "14, 25", "Quale di questi legami non è presente nell'ATP?",
  ["N-glicosidico", "Emiacetalico", "Fosfodiestere", "Fosfoestere"], 2,
  "Nell'ATP ci sono il legame N-glicosidico (adenina–ribosio), il fosfoestere (ribosio–fosfato α) e due fosfoanidridici. Il fosfodiestere lega i nucleotidi negli acidi nucleici.",
  note="Sbobina di Biochimica II, p. 25: dice che il legame emiacetalico si trova «nel ribosio e nell'ATP». Nell'ATP il C1' del ribosio è legato all'adenina, quindi è un N-glicoside e non più un emiacetale. All'esame la risposta attesa resta fosfodiestere.", times=2)
q("slp-def", "m1-atp", "19, 44", "Che cos'è la fosforilazione dell'ATP a livello del substrato?",
  ["Il trasferimento del fosfato in gamma dell'ATP ad una molecola con formazione di un legame estere",
   "La formazione dell'ATP dall'ADP e Pi mediante riossidazione del NADH", "L'idrolisi dell'ATP",
   "La formazione dell'ATP dall'ADP e Pi mediante energia rilasciata dalla scissione di un composto con un ΔG°' minore di −30 kJ/mole"], 3,
  "Un composto con potenziale di trasferimento più alto dell'ATP (1,3-BPG, PEP) cede il fosfato all'ADP. La B è la fosforilazione ossidativa, la A una normale reazione chinasica.", times=2)
q("ndpk", "m1-atp", "17–18", "Quale di queste affermazioni è falsa riguardo alla nucleotide difosfato chinasi?",
  ["Trasferisce il fosfato in gamma da un trinucleotide ad un dinucleotide", "Ha un'energia libera standard vicina allo zero",
   "La sua azione favorisce i processi catabolici", "La reazione dipende dal consumo degli NTP"], 2,
  "Forma GTP, UTP e CTP per le biosintesi (proteine, zuccheri, lipidi): favorisce l'anabolismo. Ha ΔG°' ≈ 0 e va avanti perché gli NTP vengono consumati. «Trinucleotide/dinucleotide» sta per nucleoside trifosfato/difosfato.", times=2)
q("carica", "m1-atp", "16–17", "In una cellula le concentrazioni di ATP ed ADP sono equivalenti e quella dell'AMP è trascurabile. In queste condizioni:",
  ["Prevarrà il catabolismo", "Prevarrà l'anabolismo", "I due processi sono equivalenti", "Il ΔG°' di idrolisi aumenta"], 0,
  "Carica energetica = ([ATP] + ½[ADP]) / ([ATP] + [ADP] + [AMP]) = 1,5/2 = 0,75. Sotto il valore normale di 0,9 aumentano le vie che generano ATP.", times=2)
q("no-atp", "m2-ingresso", "32–33", "Quale di questi processi non richiede ATP?",
  ["Fosforilazione del glucosio", "Trasporto del glucosio dal sangue alle cellule", "Pompa sodio potassio", "Pompa del calcio"], 1,
  "I GLUT fanno diffusione facilitata secondo gradiente. Esochinasi, Na⁺/K⁺-ATPasi e Ca²⁺-ATPasi consumano ATP.",
  note="Sbobina di Biochimica II, p. 32: l'SGLT1 (scritto «SGLUT1») è descritto prima come «trasportatore attivo che utilizza ATP» e poi come simporto senza ATP. È un trasporto attivo secondario: l'ATP lo consuma la pompa Na⁺/K⁺, non l'SGLT1.", times=2)
q("legami-energia", "m1-atp", "19–20", "Ordina per energia libera, dalla più positiva alla più negativa, la scissione di: fosfoguanidinico della creatina fosfato (A), fosfoestere (B), tioestere (C), fosfoanidridico (D).",
  ["A-B-C-D", "B-D-C-A", "C-D-B-A", "B-C-A-D"], 1,
  "ΔG°' di idrolisi: fosfoestere (es. glucosio 6-P) ≈ −14 kJ/mol, fosfoanidridico dell'ATP ≈ −30, tioestere dell'acetil-CoA −31,4, fosfocreatina ≈ −43.")

# ---------------- Ossidoriduzioni e legami ----------------
q("pk-base", "m1-coenzimi", "24", "La base B ha un pK pari a 9,0. A pH 9,0 in soluzione si avrà:",
  ["Uguale concentrazione di B e B⁻", "Uguale concentrazione di B e B⁺", "Prevalenza della forma B", "Prevalenza della forma B⁺"], 1,
  "A pH = pK le due forme sono in uguale concentrazione. La base B accetta un protone e diventa BH⁺ (B⁺).", times=2)
q("etanolo-nad", "m1-coenzimi", "53", "L'etanolo, in presenza degli enzimi necessari, reagisce con due molecole di NAD⁺. Il prodotto finale è:",
  ["Etano", "Acetaldeide", "Acetato", "Anidride carbonica"], 2,
  "Etanolo → acetaldeide (alcol deidrogenasi, 1 NAD⁺) → acetato (aldeide deidrogenasi, 1 NAD⁺).", times=2)
q("chetoacido", "m1-coenzimi", "23–24, 49", "La riduzione di un alfa-chetoacido produce:",
  ["un composto con un alcol primario e un gruppo aldeidico", "un composto con alcol secondario e un gruppo carbossilico",
   "un composto con un chetone ed un gruppo carbossilico", "un composto con due gruppi carbossilici"], 1,
  "Il chetone in α si riduce ad alcol secondario e il carbossile resta: piruvato → lattato.", times=2)
q("elettroni-glc", "m1-coenzimi", "22", "Quanti elettroni vengono persi per la completa ossidazione della molecola di glucosio ad anidride carbonica ed acqua?",
  ["8", "12", "24", "32"], 2,
  "Ogni carbonio del glucosio passa in media da 0 a +4: 6 × 4 = 24 elettroni, cioè le 12 coppie raccolte da 10 NADH e 2 FADH₂.")
q("ox-carbossile", "m1-coenzimi", "22", "Quale di queste affermazioni è vera riguardo l'ossidazione di un gruppo carbossilico?",
  ["Non è possibile", "Riguarda solo la forma deprotonata", "Viene rilasciato come CO₂", "È una reazione reversibile"], 2,
  "Il carbonio carbossilico è il più ossidato di una molecola organica: l'ultimo passaggio possibile è la sua eliminazione come CO₂, come nelle decarbossilazioni del ciclo di Krebs.")
q("elettroni-acoa", "m1-coenzimi", "22", "L'acetil-CoA (CH₃COSCoA) viene ossidato nel ciclo di Krebs a 2 molecole di CO₂. Quanti elettroni vengono persi nell'ossidazione?",
  ["2", "4", "6", "8"], 3,
  "I due carboni dell'acetile passano in totale da 0 a +8: 8 elettroni, raccolti da 3 NADH e 1 FADH₂ (4 coppie).")
q("c-secondario", "m1-coenzimi", "23", "Per ossidare un carbonio secondario saturo a chetone quali passaggi sono necessari?",
  ["Ossidazione NAD dipendente con aggiunta di una molecola d'acqua", "Idratazione seguita da un'ossidazione",
   "Ossidazione, idratazione ed un ulteriore ossidazione", "Non è possibile la trasformazione"], 2,
  "Ossidazione FAD-dipendente a doppio legame (succinato → fumarato), idratazione ad alcol secondario (→ malato), ossidazione NAD-dipendente a chetone (→ ossalacetato).")
q("no-acqua", "m1-coenzimi", "25", "Quale tra questi legami non richiede la perdita di una molecola d'acqua per la sua formazione?",
  ["Estere", "Fosfoanidridico", "Emiacetalico", "Glicosidico"], 2,
  "L'emiacetale si forma per addizione dell'OH al carbonile (C5–OH sul C1 del glucosio). Estere, fosfoanidride e glicoside sono condensazioni.")

# ---------------- Enzimologia ----------------
q("glc-fru", "m1-enzimologia", "23, 40", "La trasformazione da glucosio a fruttosio è catalizzata da:",
  ["Idrolasi", "Ossidoreduttasi", "Chinasi", "Isomerasi"], 3,
  "Glucosio (aldoso) e fruttosio (chetoso) sono isomeri: la conversione non cambia lo stato di ossidazione (es. fosfoesoso isomerasi, G6P → F6P).", times=2)
q("idrolasi", "m1-enzimologia", "31", "Quali di questi enzimi appartiene alla classe delle idrolasi?",
  ["Proteasi", "Amilasi", "Lipasi", "Tutte e tre"], 3, "Proteasi, amilasi e lipasi scindono legami usando l'acqua: sono tutte idrolasi.")
q("es-saturante", "m1-enzimologia", "27", "Se in una reazione enzimatica tutto l'enzima è nella forma ES vuol dire che:",
  ["Il substrato è uguale alla KM", "La concentrazione dell'enzima è uguale a quella del substrato", "Si è raggiunta metà della Vmax", "Il substrato è saturante"], 3,
  "Con tutto l'enzima legato come ES si lavora a Vmax: il substrato è saturante.")
q("primaria", "m1-enzimologia", "25", "In quale livello di struttura di una proteina non intervengono legami deboli?",
  ["Primaria", "Secondaria", "Terziaria", "Quaternaria"], 0,
  "La primaria è la sequenza unita da legami peptidici covalenti. Secondaria, terziaria e quaternaria dipendono da legami deboli (idrogeno, ionici, idrofobici).",
  src="Biochimica I")
q("piu-enzima", "m1-enzimologia", "27", "In una reazione enzimatica un ulteriore aumento dell'enzima provoca:",
  ["Aumento della KM", "Aumento della Vmax", "Diminuzione della KM", "Aumento della kcat"], 1,
  "Vmax = k₂[E]: cresce con l'enzima. KM e kcat sono costanti.")
q("km-unita", "m1-enzimologia", "27", "Le dimensioni della KM sono:", ["s⁻¹", "M", "s M⁻¹", "M⁻¹"], 1,
  "La KM è la concentrazione di substrato a cui v = ½ Vmax: si misura in M.")
q("k05-neg", "m1-enzimologia", "28", "La K0,5 (KM apparente) di un enzima allosterico, in presenza di un effettore allosterico negativo:",
  ["Non subisce variazioni", "Diminuisce", "Aumenta", "Dipende dalla concentrazione del substrato"], 2,
  "L'effettore negativo sposta l'equilibrio verso T: la sigmoide va a destra e la K0,5 aumenta.", times=2)
q("t-r", "m1-enzimologia", "28", "In un enzima allosterico la transizione dalla forma T alla forma R è inibita da:",
  ["Effettore omotropico negativo", "Effettore eterotropico negativo", "Effettore eterotropico positivo", "Gli effettori allosterici non hanno influenza"], 1,
  "La inibisce un effettore negativo diverso dal substrato (eterotropico). L'effettore omotropico è il substrato stesso e di solito è positivo.")
q("s-km", "m1-enzimologia", "27", "Quando la concentrazione di substrato è uguale alla KM:",
  ["La velocità è uguale alla velocità massima", "Tutto l'enzima è legato al substrato", "La velocità è metà della velocità massima", "Diminuisce la formazione del prodotto"], 2,
  "È la definizione di KM: la concentrazione di substrato a cui v = ½ Vmax.")
q("serina", "m1-enzimologia", "29", "Quale tra questi residui aminoacidici si può trovare nel sito di fosforilazione di una proteina substrato di una protein chinasi?",
  ["Fenilalanina", "Serina", "Aspartato", "Lisina"], 1, "Le protein chinasi fosforilano l'OH di serina e treonina (e tirosina).")
q("lento", "m1-enzimologia", "30", "Tra i meccanismi di regolazione, quale tra questi rientra in un meccanismo lento?",
  ["Controllo allosterico", "Espressione dell'enzima", "Fosforilazione dell'enzima", "Nessuno dei tre"], 1,
  "Allosteria e fosforilazione sono rapide. Cambiare la quantità di enzima (sintesi o degradazione) richiede ore.")
q("acqua-sub", "m1-enzimologia", "146", "Quali tra questi enzimi ha l'acqua come substrato?",
  ["Isomerasi", "Chinasi", "Ossidoreduttasi (deidrogenasi)", "Fosfatasi"], 3,
  "La fosfatasi idrolizza l'estere fosforico (es. glucosio 6-fosfatasi). Le chinasi usano ATP, le deidrogenasi NAD/FAD.")
q("mutasi", "m1-enzimologia", "45", "Enzimi che trasferiscono gruppi sostituenti in posizioni diverse della stessa molecola si chiamano:",
  ["Isomerasi", "Fosforilasi", "Chinasi", "Mutasi"], 3, "Le mutasi spostano un gruppo nella stessa molecola: 3-fosfoglicerato → 2-fosfoglicerato.")

# ---------------- Ingresso del glucosio ----------------
q("glut-fegato", "m2-ingresso", "32–33", "Quali sono i trasportatori di glucosio nell'epatocita?", ["GLUT1", "GLUT2", "GLUT3", "GLUT4"], 1,
  "GLUT2: fegato, pancreas e membrana basolaterale dell'enterocita. Kt 17 mM, alta capacità: lavora dopo i pasti.")
q("amilasi", "m2-ingresso", "31", "È maggiore il glucosio rilasciato per unità di tempo dall'alfa-amilasi dall'amilosio o dall'amilopectina?",
  ["È equivalente", "Amilosio", "Amilopectina", "Per rispondere c'è bisogno dei valori di KM per i due substrati"], 2,
  "Da confermare.", pending=True)
q("glut4", "m2-ingresso", "33, 35", "In quali tra queste cellule l'insulina permette il trasferimento sulla superficie dei trasportatori GLUT4?",
  ["Neuroni", "Globuli rossi", "Epatociti", "Adipociti"], 3, "GLUT4: muscolo scheletrico, cuore e tessuto adiposo.")
q("glut-entero", "m2-ingresso", "32", "Quale trasportatore del glucosio si trova sulla membrana basolaterale degli enterociti?", ["GLUT1", "GLUT2", "GLUT3", "GLUT4"], 1,
  "Dal lume il glucosio entra con l'SGLT1, verso il sangue esce con il GLUT2 basolaterale.")
q("glut-bidir", "m2-ingresso", "33", "I trasportatori GLUT sono:",
  ["unidirezionali", "bidirezionali", "possono assumere una sola conformazione", "sono tutti sotto controllo ormonale"], 1,
  "Diffusione facilitata: il verso dipende solo dal gradiente (il fegato a digiuno libera glucosio con il GLUT2). Hanno due conformazioni, T1 e T2, e solo il GLUT4 è sotto controllo ormonale.")
q("glut-tumore", "m2-ingresso", "64 e seguenti (pagine non numerate, effetto Warburg)", "In una cellula tumorale aumenta l'espressione di GLUT. Si tratterà di:", ["GLUT1", "GLUT2", "GLUT3", "GLUT4"], 0,
  "Nelle cellule tumorali il fattore HIF è attivo anche con l'ossigeno e fa trascrivere enzimi glicolitici, LDH e trasportatori: soprattutto il GLUT1, ad alta affinità, che lavora già a glicemia basale (effetto Warburg).",
  note="La sbobina cita sia GLUT1 sia GLUT3 tra i geni attivati da HIF: la risposta attesa è GLUT1. Se a lezione è stato detto diversamente, fallo presente segnalandolo.")
q("gr-postprandiale", "m2-ingresso", "33–34", "Ai valori di glicemia post-prandiale, la velocità di ingresso del glucosio nel globulo rosso:",
  ["Aumenta", "Diminuisce", "Resta invariata", "Resta invariata ma aumenta la concentrazione"], 0,
  "Da confermare.", pending=True)
q("gr-insulina", "m2-ingresso", "33", "Quale di queste cellule non ha il recettore per l'insulina?",
  ["Epatocita", "Miocita", "Adipocita", "Globulo rosso"], 3,
  "Il globulo rosso prende il glucosio con il GLUT1, indipendente dall'insulina. Esistono pochi recettori anche sugli eritrociti, ma la risposta attesa è questa.")
q("insulina-sec", "m2-ingresso", "34", "Quali di questi eventi non è coinvolto nella secrezione dell'insulina?",
  ["Fosforilazione del glucosio per opera della glucochinasi", "Fosforilazione ossidativa", "Ingresso di ioni potassio", "Ingresso del calcio"], 2,
  "L'ATP chiude i canali del K⁺: il potassio smette di uscire, la membrana si depolarizza, entra Ca²⁺ e partono le vescicole di insulina.")
q("glut1-neonati", "m2-ingresso", "33", "Quali di questi eventi è più probabile che avvengano in neonati che presentano mutazioni del gene che codifica per GLUT1? (E come intervenire?)",
  ["Ipoglicemia", "Problemi neurologici", "Insufficienza renale", "Insufficienza cardiaca"], 1,
  "Il GLUT1 porta il glucosio oltre la barriera ematoencefalica: il deficit dà convulsioni e ritardo dello sviluppo con glicemia normale. Si interviene con la dieta chetogenica, perché i corpi chetonici entrano nel cervello con altri trasportatori.",
  note="Il nome della sindrome (deficit di GLUT1) e la dieta chetogenica non sono nelle sbobine.")
q("glut-placenta", "m2-ingresso", None, "Quale trasportatore del glucosio vi aspettate di trovare nelle cellule della placenta?", ["GLUT1", "GLUT2", "GLUT3", "GLUT4"], 0,
  "Nella placenta il trasportatore principale è il GLUT1: come nella barriera ematoencefalica, deve far passare glucosio già a glicemia basale.",
  note="Non è nelle sbobine (Lehninger).")
q("peptide-c", "m2-ingresso", "36", "Un paziente con iperglicemia presenta nel sangue valori normali del peptide C originato dal taglio della proinsulina. Questo dato indica che:",
  ["L'insulina non viene prodotta dalle cellule del pancreas", "L'insulina non trasporta i GLUT4 sulle membrane delle cellule muscolari",
   "Il trasporto del glucosio nel fegato è rallentato", "La glucochinasi del pancreas è c… (fine illeggibile nella foto)"], 1,
  "Peptide C normale = l'insulina viene prodotta. L'iperglicemia dipende dall'insulino-resistenza: i GLUT4 non vengono esposti sulla membrana.")

# ---------------- Fosforilazione del glucosio ----------------
q("glc-atp", "m2-fosforilazione", "37, 40", "Nella reazione: Glucosio + ATP → Glucosio 6P + ADP",
  ["Il fosfato in alfa dell'ATP è trasferito al glucosio", "La scissione dell'ATP spinge la reazione verso destra", "Si forma un legame anidridico", "Il ΔG°' è ampiamente positivo"], 1,
  "Viene trasferito il fosfato γ e si forma un fosfoestere. La reazione è accoppiata all'idrolisi dell'ATP, che rende il ΔG negativo.", times=2)
q("glucochinasi", "m2-fosforilazione", "37", "Quale delle seguenti affermazioni è vera per la glucochinasi?",
  ["È un enzima ubiquitario", "Trasforma il glucosio in glucosio 1-P", "Ha una KM superiore a quella dell'esochinasi", "Forma un legame fosfoanidridico tra il glucosio ed il fosfato"], 2,
  "La glucochinasi (esochinasi IV) è solo in fegato e pancreas, ha una KM circa 100 volte più alta dell'esochinasi e forma glucosio 6-P con un fosfoestere.")
q("g6p-falsa", "m2-fosforilazione", "38, 65", "Quale tra queste affermazioni non è vera per il glucosio 6P?",
  ["È il precursore del ribosio", "Può essere immagazzinato sotto forma di glicogeno", "Passa liberamente nel mitocondrio", "Nell'epatocita può essere convertito in glucosio"], 2,
  "La membrana mitocondriale interna è impermeabile: il G6P resta nel citosol. Dà ribosio (pentoso fosfati), glicogeno e, nel fegato, glucosio libero (glucosio 6-fosfatasi).")

# ---------------- Glicolisi ----------------
q("bilancio-g6p", "m2-glicolisi", "47", "Il bilancio della glicolisi a partire dal glucosio-6P dà:",
  ["La riduzione di una molecola di NAD⁺", "La produzione di anidride carbonica", "Un aumento del pH", "La formazione di 3 molecole di ATP"], 3,
  "Partendo dal G6P non si spende l'ATP dell'esochinasi: 4 prodotti − 1 (PFK1) = 3 ATP. Si riducono 2 NAD⁺, non si forma CO₂ e il pH scende.")
q("glut5", "m2-glicolisi", "64 e seguenti (pagine non numerate)", "Le cellule testicolari posseggono trasportatori GLUT5. Quanti ATP si formano nella glicolisi?", ["1", "2", "3", "4"], 1,
  "Il GLUT5 trasporta fruttosio. Nel muscolo il fruttosio diventa fruttosio 6-P con l'esochinasi; nel fegato fruttosio 1-P con la fruttochinasi, poi DHAP e gliceraldeide. In entrambi i casi il bilancio è di 2 ATP netti per esoso (4 prodotti, 2 spesi).",
  note="Sbobina di Biochimica II, pagine non numerate dopo p. 64: la triosio chinasi fosforila la gliceraldeide a «gliceraldeide 2-fosfato». Il prodotto è la gliceraldeide 3-fosfato, come mostra anche la figura accanto.")
q("gapdh-legame", "m2-glicolisi", "43", "Durante la catalisi della gliceraldeide 3P deidrogenasi quale legame non si forma?",
  ["Fosfoanidridico", "Tioemiacetale", "Fosfoestere", "Tioestere"], 2,
  "Si formano il tioemiacetale (Cys–aldeide), il tioestere dopo l'ossidazione e il fosfoanidridico misto dell'1,3-BPG. Il fosfoestere in C3 c'era già nella GA3P.",
  note="Sbobina di Biochimica II, p. 43: il meccanismo dice che va al NAD⁺ «l'H⁺ sotto forma di idruro» e che «la riduzione» trasforma l'aldeide. Va al NAD⁺ un idruro (H⁻), l'aldeide si ossida e si forma il tioestere con la cisteina.")
q("gapdh-cys", "m2-glicolisi", "43", "Quale residuo aminoacidico è coinvolto nella catalisi della gliceraldeide 3-fosfato deidrogenasi?",
  ["Serina", "Cisteina", "Lisina", "Metionina"], 1, "Il gruppo SH della cisteina attacca l'aldeide; per questo lo iodoacetato, che lo alchila, blocca la glicolisi.")
q("gapdh-nadh", "m2-glicolisi", "43", "Nella reazione GA3P + Pi + NAD⁺ ⇌ 1,3-BPG + NADH + H⁺, un aumento del NADH produce:",
  ["Una diminuzione del NAD⁺", "Un aumento della GA3P", "Una diminuzione del pH", "Nessun cambiamento"], 1,
  "Più NADH sposta l'equilibrio a sinistra (Le Chatelier): si riforma GA3P e aumenta il NAD⁺.")
q("slp-reazione", "m2-glicolisi", "44", "Quale delle seguenti reazioni è una fosforilazione a livello del substrato?",
  ["Conversione della gliceraldeide in 1,3 bisfosfoglicerato", "Conversione del 1,3 bisfosfoglicerato in 3-fosfoglicerato", "Formazione del 2-fosfoglicerato", "Formazione del fosfoenolpiruvato"], 1,
  "La fosfoglicerato chinasi: l'1,3-BPG cede il fosfato all'ADP. L'altra della glicolisi è la piruvato chinasi.")
q("dg-negativo", "m2-glicolisi", "47", "Quale delle seguenti reazioni della glicolisi procede con un ΔG negativo?",
  ["Conversione del glucosio 6P in fruttosio 6P", "Reazione della gliceraldeide 3 fosfato deidrogenasi", "Reazione dell'enolasi", "Reazione della piruvato chinasi"], 3,
  "Le tre reazioni con ΔG fortemente negativo sono esochinasi/glucochinasi, PFK1 e piruvato chinasi. Le altre sono vicine all'equilibrio.", times=2)
q("bpg-falsa", "m2-glicolisi", "43–44", "Quale di queste affermazioni è falsa per l'1,3 bisfosfoglicerato?",
  ["Contiene un legame fosfoanidridico", "Contiene un legame fosfoesterico", "È meno ossidato del 3-fosfoglicerato", "Ha un potenziale di trasferimento maggiore dell'ATP"], 2,
  "1,3-BPG e 3-fosfoglicerato hanno lo stesso stato di ossidazione (C1 a livello di acido): la fosfoglicerato chinasi sposta solo il fosfato.")
q("non-glicolisi", "m2-glicolisi", "39", "Quali tra questi composti non partecipa alla glicolisi?",
  ["Esteri fosforici", "Esosi", "Acidi dicarbossilici", "Fosfoanidridi"], 2,
  "Nella glicolisi ci sono esosi, esteri fosforici e fosfoanidridi (ATP, 1,3-BPG). Gli acidi dicarbossilici (malato, ossalacetato, succinato) sono del ciclo di Krebs.")
q("doppio-legame", "m2-glicolisi", "45", "Quale dei seguenti composti della glicolisi ha un doppio legame?",
  ["2-fosfoglicerato", "Fosfoenolpiruvato", "Fruttosio 1,6-bisfosfato", "Piruvato"], 1,
  "Il PEP ha un doppio legame C=C (forma enolica). Carbossili e chetoni hanno C=O, ma la domanda intende il doppio legame tra carboni.")
q("ga3p-fbp", "m2-glicolisi", "41", "Una soluzione contiene gliceraldeide 3-P. Quali enzimi bisogna aggiungere per formare fruttosio 1,6 bisfosfato?",
  ["Gliceraldeide 3-P deidrogenasi + aldolasi", "Gliceraldeide 3-P deidrogenasi + aldolasi + triosofosfato isomerasi",
   "Triosofosfato isomerasi + diidrossiacetone 3-P deidrogenasi", "Aldolasi + triosofosfato isomerasi"], 3,
  "La trioso fosfato isomerasi forma DHAP da una parte della GA3P, poi l'aldolasi (reversibile) condensa DHAP + GA3P in FBP.")
q("fbp-f6p", "m2-glicolisi", "41, 146", "Una soluzione contiene gliceraldeide 3-P, aldolasi e triosofosfato isomerasi, quindi si forma fruttosio 1,6-bisfosfato. Quale ulteriore enzima della via glicolitica, aggiunto, permetterà la formazione del fruttosio 6-P?",
  ["Nessuno", "Bastano quelli presenti", "Fosfofruttochinasi 1", "Fosfoesoso isomerasi"], 0,
  "Per FBP → F6P serve la fruttosio 1,6-bisfosfatasi, che è della gluconeogenesi. La PFK1 è irreversibile e la fosfoesoso isomerasi agisce su F6P/G6P.",
  note="Nel foglio la domanda dice «alla soluzione precedente»: qui è collegata a quella sulla gliceraldeide 3-P. Se a lezione la soluzione era un'altra, fallo presente segnalandolo.")

# ---------------- Fermentazioni ----------------
q("ferm-irrev", "m2-fermentazioni", "53", "La fermentazione etanolica non è un processo reversibile. Perché?",
  ["Perché avviene in due tappe", "Non ci sono nei microrganismi gli enzimi per le reazioni inverse", "La prima tappa della fermentazione alcolica è una decarbossilazione", "L'acetaldeide si ossida velocemente in acetato"], 2,
  "Piruvato → acetaldeide + CO₂: la decarbossilazione è irreversibile. La riduzione ad etanolo (alcol deidrogenasi) invece è reversibile.")
q("etanolo-vera", "m2-fermentazioni", "53", "Quale di queste affermazioni è vera per l'etanolo?",
  ["La conversione in acetato richiede 1 NADH", "La conversione in acetato richiede l'aldeide deidrogenasi", "In eccesso di etanolo, diminuisce la formazione di lattato", "È consigliabile assumere etanolo prima di una attività sportiva"], 1,
  "Etanolo → acetaldeide (alcol deidrogenasi) → acetato (aldeide deidrogenasi): si producono 2 NADH. L'NADH in eccesso spinge il piruvato a lattato, quindi il lattato aumenta.")
q("etanolo-falsa", "m2-fermentazioni", "53, 169", "Quale affermazione è falsa per l'etanolo?",
  ["Passa la barriera ematoencefalica", "La sua conversione in acetato avviene nel fegato", "La produzione di acido acetico è un processo fermentativo", "L'alcol deidrogenasi è un enzima costitutivo"], 2,
  "Nel fegato l'etanolo viene ossidato con NAD⁺: è un'ossidazione, non una fermentazione (che serve a riossidare NADH). L'alcol deidrogenasi è costitutiva; inducibile è il citocromo P450.")
q("ldh-fattore", "m2-fermentazioni", "49–52", "Quale dei seguenti fattori non è influente per la conversione del piruvato in lattato?",
  ["pH cellulare", "Consumo dell'ATP per la contrazione muscolare", "Velocità dell'ingresso del glucosio nella cellula", "Rapporto citoplasmatico NAD⁺/NADH"], 2,
  "Da confermare.", pending=True)
q("ldh-falsa", "m2-fermentazioni", "50", "Quale affermazione è falsa per la lattico deidrogenasi?",
  ["È un enzima a chiralità selettiva", "È sempre un omotetramero", "È un enzima dipendente dal pH", "È presente nei globuli rossi"], 1,
  "È un tetramero di subunità H e M: solo H4 e M4 sono omotetrameri, M3H, M2H2 e MH3 sono eterotetrameri.",
  note="Sbobina di Biochimica II, p. 49: c'è scritto che la LDH forma solo l'isomero «R». L'L-lattato è (S)-lattato.")
q("ldh1", "m2-fermentazioni", "50, 52", "La presenza nel sangue dell'isoenzima LDH1 può essere indice di:",
  ["Strappi muscolari", "Fragilità dei globuli rossi", "Infarto del miocardio", "Cirrosi epatica"], 2,
  "LDH1 = H4, isoenzima cardiaco: marker tardivo di infarto (circa 48 ore). Sale anche nell'emolisi, ma la risposta attesa è l'infarto.")
q("ldh-struttura", "m2-fermentazioni", "50", "Gli isoenzimi della lattato deidrogenasi differiscono per la KM. Quale livello della struttura proteica è responsabile della variazione?",
  ["Primaria", "Secondaria", "Terziaria", "Quaternaria"], 3, "Da confermare.", pending=True)
q("cori", "m2-fermentazioni", "51, 148", "Quale di queste condizioni deve essere soddisfatta dal fegato per il ciclo di Cori?",
  ["Deve essere attiva la via glicolitica", "Ci deve essere un alto rapporto NAD⁺/NADH", "Deve essere attiva la trasduzione del segnale dell'insulina", "Deve essere attiva la glucochinasi"], 1,
  "Il fegato ossida il lattato a piruvato con la LDH: serve molto NAD⁺. Glicolisi e glucochinasi devono essere ferme, perché si fa gluconeogenesi.")
q("anion-gap", "m2-fermentazioni", "52", "L'anion gap (AG) in biochimica clinica è dato da AG = [Na⁺] − ([Cl⁻] + [HCO₃⁻]). In presenza di lattato il valore dell'AG:",
  ["Rimane invariato", "Aumenta", "Diminuisce", "Si annulla"], 1,
  "Il lattato è un anione non misurato: il bicarbonato cala per tamponare l'H⁺, quindi l'AG aumenta (acidosi lattica ad anion gap aumentato).",
  note="L'anion gap non è nelle sbobine.")

# ---------------- Sistemi navetta ----------------
q("dhap-rid", "m2-navette", "54", "Quale composto si forma dalla riduzione NADH dipendente del diidrossiacetone fosfato?",
  ["Non può essere ridotto", "Gliceraldeide 3-P", "Un alfachetoacido", "Glicerolo fosfato"], 3,
  "Il chetone del DHAP si riduce ad alcol secondario: glicerolo 3-fosfato. È il primo passo della navetta del glicerolo fosfato.",
  note="Sbobina di Biochimica II, p. 54: chiama il glicerolo 3-fosfato «3-fosfoglicerolo (3-PG)». Non confonderlo con il 3-fosfoglicerato, che altrove è abbreviato 3-PG.", times=2)
q("navetta-fad", "m2-navette", "54", "Nel sistema navetta del glicerolo fosfato:",
  ["Il FADH₂ è ossidato dal diidrossiacetone fosfato", "Il NADH cede gli elettroni direttamente al FAD", "Il glicerolo fosfato è ossidato dal FAD", "Il FADH₂ cede gli elettroni direttamente all'ossigeno"], 2,
  "La glicerolo 3-fosfato deidrogenasi mitocondriale, FAD-dipendente, ossida il glicerolo fosfato a DHAP; il FADH₂ passa gli elettroni alla catena respiratoria (coenzima Q).")
q("navetta-atp", "m2-navette", "47, 54", "Se la riossidazione del NADH produce 2,5 ATP e quella del FADH₂ 1,5 ATP, quante ATP si formano in totale da glucosio a piruvato se il sistema navetta è quello del glicerolo fosfato?",
  ["3", "4", "5", "7"], 2, "2 ATP netti + 2 NADH citosolici che, con la navetta del glicerolo fosfato, diventano FADH₂: 2 + 2 × 1,5 = 5.")

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "exam.json")
json.dump(Q, open(out, "w"), ensure_ascii=False, indent=1)
print(len(Q), "domande,", sum(not x["pending"] for x in Q), "nel feed,", sum(x["pending"] for x in Q), "da confermare")
