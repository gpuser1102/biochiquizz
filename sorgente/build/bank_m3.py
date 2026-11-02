"""Blocco 3 – Ciclo di Krebs e fosforilazione ossidativa (sbobina di Biochimica II, p. 74–114)."""
from bank_common import q

T = "m3-krebs"
q("m3k-01", T, "f", "74", "Dove avviene il ciclo di Krebs?", ["Nella matrice mitocondriale", "Nel citosol", "Nello spazio intermembrana", "Nel reticolo endoplasmatico"], 0,
  "Tutti gli enzimi sono nella matrice tranne la succinato deidrogenasi, che è nella membrana interna.")
q("m3k-02", T, "f", "76", "Quale enzima unisce acetil-CoA e ossalacetato?", ["Citrato sintasi", "Aconitasi", "Isocitrato deidrogenasi", "Piruvato carbossilasi"], 0,
  "È una condensazione di Claisen che forma citrato e libera CoA.")
q("m3k-03", T, "f", "74", "Che cosa produce un giro del ciclo di Krebs per acetil-CoA?", ["3 NADH, 1 FADH₂, 1 GTP, 2 CO₂", "2 NADH, 2 FADH₂, 1 ATP, 2 CO₂", "4 NADH, 1 GTP, 1 CO₂", "3 NADH, 1 FADH₂, 2 ATP"], 0,
  "NADH da isocitrato DH, α-chetoglutarato DH e malato DH; FADH₂ dalla succinato DH; GTP dalla succinil-CoA sintetasi.")
q("m3k-04", T, "f", "83", "Quale enzima del ciclo di Krebs è anche il complesso II della catena respiratoria?", ["Succinato deidrogenasi", "Malato deidrogenasi", "Fumarasi", "Isocitrato deidrogenasi"], 0,
  "È l'unico enzima del ciclo integrato nella membrana mitocondriale interna.")
q("m3k-05", T, "m", "79", "Perché la citrato sintasi lega prima l'ossalacetato e poi l'acetil-CoA (meccanismo sequenziale ordinato)?", [
  "Perché l'ossalacetato è presente in quantità minime: l'enzima si assicura che ci sia prima di usare l'acetil-CoA",
  "Perché l'acetil-CoA è più grande", "Perché l'ossalacetato è il prodotto", "Perché così consuma meno ATP"], 0,
  "L'adattamento indotto evita anche l'idrolisi improduttiva del tioestere dell'acetil-CoA.")
q("m3k-06", T, "m", "84", "Quali sono le tre reazioni del ciclo con ΔG fortemente negativo, quindi regolate?", [
  "Citrato sintasi, isocitrato deidrogenasi, α-chetoglutarato deidrogenasi", "Aconitasi, fumarasi, malato deidrogenasi", "Succinil-CoA sintetasi, succinato DH, fumarasi", "Tutte le otto reazioni"], 0,
  "Le altre sono vicine all'equilibrio.")
q("m3k-07", T, "m", "84–85", "Come viene regolato il ciclo di Krebs?", [
  "NADH e ATP lo rallentano, ADP e Ca²⁺ lo accelerano", "Solo dall'insulina", "È attivato dal NADH", "Non è regolato"], 0,
  "È il controllo «da parte dell'accettore»: se c'è ADP la cellula ha bisogno di ATP.")
q("m3k-08", T, "m", "87", "Qual è la reazione anaplerotica più importante?", ["Piruvato → ossalacetato (piruvato carbossilasi)", "Citrato → isocitrato", "Malato → ossalacetato", "Acetil-CoA → citrato"], 0,
  "Riempie il ciclo di intermedi; è attivata dall'acetil-CoA.")
q("m3k-09", T, "a", "84", "Le due CO₂ che escono in un giro del ciclo provengono dai carboni dell'acetil-CoA appena entrato?", [
  "No: vengono dall'ossalacetato; i carboni dell'acetile escono nei giri successivi", "Sì, entrambe", "Una sì e una no", "No, vengono dal CoA"], 0,
  "Per eliminare completamente i carboni di un acetile servono due giri.",
  note="Sbobina di Biochimica II, p. 77: dopo la seconda decarbossilazione c'è scritto che «abbiamo così ossidato l'acetato». A p. 84 la stessa sbobina chiarisce che le CO₂ escono dai carboni dell'ossalacetato.")
q("m3k-10", T, "a", "86", "Perché il beri-beri colpisce soprattutto sistema nervoso e cuore?", [
  "La TPP serve a PDH (cervello, che usa glucosio) e ad α-chetoglutarato DH (cuore, che dipende dal ciclo di Krebs)",
  "Perché la tiamina serve alla sintesi di acetilcolina", "Perché la tiamina è un antiossidante", "Perché manca il NAD"], 0,
  "Senza TPP si bloccano le due decarbossilazioni ossidative.")
q("m3k-11", T, "a", "86", "Come agiscono arsenico e mercurio sul metabolismo energetico?", [
  "Legano i gruppi SH del lipoato, bloccando PDH e α-chetoglutarato DH", "Inibiscono l'ATP sintasi", "Bloccano il complesso IV", "Ossidano il NADH"], 0,
  "I composti con ditioli possono liberare l'enzima legando l'arsenico.")
q("m3k-12", T, "a", "89", "Perché per ossidare completamente gli acidi grassi serve anche il glucosio?", [
  "Perché l'acetil-CoA ha bisogno di ossalacetato, che si forma dal piruvato",
  "Perché gli acidi grassi si ossidano solo nel citosol", "Perché la β-ossidazione consuma glucosio", "Perché servono i GLUT"], 0,
  "Si dice che i grassi «bruciano al fuoco dei carboidrati».")
q("m3k-13", T, "a", "85", "Pellagra: quale coenzima manca e perché in Veneto era endemica?", [
  "NAD (niacina, B3): l'alimentazione si basava sul mais, in cui la niacina non è disponibile senza trattamento alcalino",
  "FAD (riboflavina): carenza di latte", "TPP (tiamina): riso brillato", "CoA (B5): carenza di carne"], 0,
  "In America Latina la nixtamalizzazione (calce viva) rendeva disponibile la niacina. Sintomi: dermatite, diarrea, demenza.")
q("m3k-14", T, "l", "78, 82", "Come si chiama correttamente l'enzima che forma GTP dal succinil-CoA?", ["Succinil-CoA sintetasi", "Succinil-CoA sintasi", "Succinato chinasi", "Succinato deidrogenasi"], 0,
  "Si chiama sintetasi perché la reazione coinvolge un nucleotide trifosfato.",
  note="Sbobina di Biochimica II, p. 78: l'enzima è chiamato «succinil-CoA sintasi (perché utilizziamo GDP)», contro la definizione data poco prima. A p. 82 è chiamato correttamente sintetasi.")
q("m3k-15", T, "l", "80", "Qual è l'intermedio della reazione dell'aconitasi?", ["cis-Aconitato", "trans-Aconitato", "Citril-CoA", "Ossalsuccinato"], 0,
  "Deidratazione e reidratazione: citrato → cis-aconitato → isocitrato.")
q("m3k-16", T, "l", "80", "Che tipo di centro ha l'aconitasi nel sito attivo?", ["Un centro 4Fe-4S", "Un eme", "Un atomo di zinco", "Un centro rame"], 0,
  "Se perde un ferro diventa inattiva; l'isoforma citosolica è la IRP1, che regola ferritina e recettore della transferrina.")
q("m3k-17", T, "l", "82", "Come si chiama l'E2 del complesso dell'α-chetoglutarato deidrogenasi?", ["Diidrolipoil transsuccinilasi", "Diidrolipoil transacetilasi", "Succinil-CoA sintetasi", "Diidrolipoil deidrogenasi"], 0,
  "Trasferisce un gruppo succinile invece che acetile; l'E3 è uguale a quello della PDH.")
q("m3k-18", T, "l", "83", "Quale stereoisomero del malato forma la fumarasi?", ["L-malato", "D-malato", "Meso-malato", "Racemo"], 0,
  "L'idratazione del fumarato è stereospecifica.")

T = "m3-catena"
q("m3c-01", T, "f", "90", "Qual è l'accettore finale degli elettroni nella catena respiratoria?", ["O₂", "NAD⁺", "Coenzima Q", "Citocromo c"], 0,
  "L'ossigeno viene ridotto ad acqua nel complesso IV.")
q("m3c-02", T, "f", "91", "Dove si trova la catena respiratoria?", ["Nella membrana mitocondriale interna", "Nella membrana esterna", "Nella matrice", "Nel citosol"], 0,
  "Le creste aumentano la superficie disponibile.")
q("m3c-03", T, "f", "95", "Quale complesso non pompa protoni?", ["Complesso II", "Complesso I", "Complesso III", "Complesso IV"], 0,
  "Il ΔE tra succinato e coenzima Q è troppo piccolo.")
q("m3c-04", T, "m", "90", "Quanti ATP si ottengono circa dalla riossidazione di un NADH e di un FADH₂?", ["2,5 e 1,5", "3 e 2", "1,5 e 2,5", "2 e 1"], 0,
  "Il FADH₂ entra al coenzima Q, saltando il complesso I.")
q("m3c-05", T, "m", "92", "Come sono disposti i trasportatori della catena?", [
  "In ordine di potenziale di riduzione crescente, dal NADH (−0,32 V) all'O₂ (+0,81 V)", "In ordine di massa", "In ordine casuale", "In ordine di potenziale decrescente"], 0,
  "Gli elettroni scendono «in discesa» verso l'accettore più affine.")
q("m3c-06", T, "m", "95", "Da quali fonti il coenzima Q riceve elettroni?", [
  "Complesso I, complesso II, glicerolo 3-P deidrogenasi della navetta, β-ossidazione", "Solo dal complesso I", "Dal citocromo c", "Dal complesso IV"], 0,
  "Convoglia gli elettroni di tutti gli enzimi flavinici.")
q("m3c-07", T, "a", "104", "Se blocchi il complesso III con antimicina A, in che stato saranno i trasportatori?", [
  "Ridotti quelli a monte (NADH, complesso I, Q), ossidati quelli a valle (citocromo c, complesso IV)",
  "Tutti ossidati", "Tutti ridotti", "Ossidati a monte, ridotti a valle"], 0,
  "È il metodo con cui è stata ricostruita la sequenza dei trasportatori.")
q("m3c-08", T, "a", "96–97", "A che cosa serve il ciclo del Q nel complesso III?", [
  "A passare da un trasportatore a 2 elettroni (QH₂) a uno a 1 elettrone (citocromo c), un elettrone per volta",
  "A produrre ATP", "A ridurre l'ossigeno", "A trasportare NADH"], 0,
  "Un elettrone va al citocromo c1 → c, l'altro torna attraverso i citocromi b a un Q.")
q("m3c-09", T, "a", "99", "Quanta energia libera si libera nel trasferimento di 2 elettroni dal NADH all'O₂?", ["Circa −218 kJ/mol", "Circa −30 kJ/mol", "Circa −61 kJ/mol", "Circa −1000 kJ/mol"], 0,
  "ΔG°' = −nFΔE°' con ΔE°' = 0,81 − (−0,32) = 1,13 V.")
q("m3c-10", T, "a", "104", "Il cianuro blocca il complesso IV. Cosa succede ai trasportatori?", ["Restano tutti ridotti", "Restano tutti ossidati", "Si riduce solo il citocromo c", "Il coenzima Q si ossida"], 0,
  "Gli elettroni non possono uscire verso l'ossigeno. Lo stesso fanno CO e sodio azide.")
q("m3c-11", T, "l", "92", "Come si chiama il complesso I secondo la nomenclatura usata nella sbobina?", ["NADH-Q reduttasi", "NADH ossidasi", "Ubichinone deidrogenasi", "Citocromo b reduttasi"], 0,
  "Si scrive prima chi si ossida, poi chi si riduce, poi «reduttasi». Il complesso IV sarebbe correttamente citocromo c-ossigeno reduttasi.")
q("m3c-12", T, "l", "93", "Quale gruppo prostetico flavinico contiene il complesso I?", ["FMN (flavin mononucleotide)", "FAD", "Biotina", "Lipoato"], 0,
  "L'FMN prende due elettroni dal NADH e li cede uno alla volta ai centri Fe-S.")
q("m3c-13", T, "l", "96", "Come si chiama la proteina Fe-S del complesso III, con due cisteine e due istidine?", ["Proteina di Rieske", "Adrenodossina", "Ferredossina", "Citocromo c1"], 0,
  "A differenza delle Fe-S classiche, due ligandi del ferro sono istidine.")
q("m3c-14", T, "l", "98", "Quali sono i centri metallici del complesso IV?", ["Eme a, eme a3, CuA e CuB", "Eme b e c1", "Solo eme a3", "Fe-S e FMN"], 0,
  "L'ossigeno viene ridotto nel centro binucleare eme a3–CuB.")
q("m3c-15", T, "l", "97", "Che cosa coordina il ferro del citocromo c nella sesta posizione?", ["Lo zolfo di una metionina", "Un'istidina distale", "L'ossigeno", "Una cisteina"], 0,
  "Ferro coordinato da 4 N della porfirina, un'istidina e una metionina: tutte le posizioni sono occupate e non lega O₂.")
q("m3c-16", T, "l", "94", "Il coenzima Q si trova:", ["Nella membrana mitocondriale interna", "Nella membrana plasmatica", "Nella matrice", "Nello spazio intermembrana"], 0,
  "Ha una coda di 10 unità isopreniche che lo tiene nel doppio strato.",
  note="Sbobina di Biochimica II, p. 94: c'è scritto che il coenzima Q è presente «nella membrana plasmatica». Si trova nella membrana mitocondriale interna.")

T = "m3-atpsintasi"
q("m3s-01", T, "f", "100", "Come si chiama la teoria che spiega la sintesi di ATP nel mitocondrio?", ["Teoria chemiosmotica di Mitchell", "Teoria dell'adattamento indotto", "Teoria chiave-serratura", "Teoria del cambio di legame di Michaelis"], 0,
  "Il gradiente protonico creato dalla catena alimenta l'ATP sintasi.")
q("m3s-02", T, "f", "100", "Da quali parti è formata l'ATP sintasi?", ["F₀ nella membrana e F₁ verso la matrice", "F₁ nella membrana e F₀ nella matrice", "Solo F₁", "Complessi I e IV"], 0,
  "F₀ è il canale e rotore per i protoni, F₁ catalizza la sintesi di ATP.")
q("m3s-03", T, "m", "100", "Da quali due componenti è formata la forza motrice protonica?", ["Gradiente elettrico (potenziale di membrana) e gradiente chimico (ΔpH)", "Gradiente di Na⁺ e K⁺", "ATP e ADP", "Temperatura e pressione"], 0,
  "I protoni pompati fuori rendono il lato P positivo e più acido.")
q("m3s-04", T, "m", "102", "Come funziona il meccanismo di «cambio di legame» delle subunità β?", [
  "Le tre β passano a turno per le conformazioni L (lega ADP + Pi), T (forma ATP) e O (rilascia ATP)",
  "Ogni β sintetizza ATP indipendentemente", "Le β ruotano con l'anello c", "Le α fanno la catalisi"], 0,
  "La rotazione di γ cambia la conformazione delle β; il passaggio che costa più energia è il rilascio dell'ATP.")
q("m3s-05", T, "m", "103–104", "Che cosa fa l'ATP/ADP traslocasi?", [
  "Scambia ATP della matrice con ADP del citosol, sfruttando il potenziale di membrana", "Sintetizza ATP", "Trasporta fosfato", "Trasporta NADH"], 0,
  "ATP⁴⁻ esce e ADP³⁻ entra: si sposta una carica negativa netta verso l'esterno.")
q("m3s-06", T, "a", "105", "Che effetto ha il 2,4-dinitrofenolo?", [
  "Riporta protoni nella matrice scavalcando l'ATP sintasi: gli elettroni fluiscono ma l'energia diventa calore",
  "Blocca il complesso IV", "Blocca l'ATP sintasi", "Aumenta la sintesi di ATP"], 0,
  "È un disaccoppiante; usato in passato come dimagrante, con molti decessi.")
q("m3s-07", T, "a", "105", "Con l'oligomicina, che succede al consumo di ossigeno?", [
  "Diminuisce: il gradiente non si scarica e il trasporto di elettroni rallenta", "Aumenta", "Non cambia", "Si azzera la glicolisi"], 0,
  "Trasporto di elettroni e sintesi di ATP sono accoppiati.")
q("m3s-08", T, "a", "106", "A che cosa serve la termogenina (UCP1) nel tessuto adiposo bruno?", [
  "Lascia rientrare i protoni nella matrice producendo calore invece di ATP", "Sintetizza ATP", "Trasporta acidi grassi", "Pompa protoni fuori"], 0,
  "È un disaccoppiante fisiologico, importante per la termoregolazione del neonato.")
q("m3s-09", T, "a", "101–102", "Nell'anello c dell'F₀, perché l'aspartato si protona e si deprotona?", [
  "Si protona nel semicanale verso lo spazio intermembrana (pH acido) e cede il protone nel semicanale verso la matrice (pH basico): così l'anello ruota",
  "Perché viene fosforilato", "Perché lega ATP", "Perché ossida il NADH"], 0,
  "Ogni protone che entra fa avanzare il rotore di una subunità c.")
q("m3s-10", T, "l", "102", "Che cosa significano le sigle O, L e T delle subunità β?", ["Open, Loose, Tight", "Open, Light, Tight", "Oxidized, Loaded, Taut", "Open, Locked, Tense"], 0,
  "L = loose: lega ADP e Pi in modo lasso.",
  note="Sbobina di Biochimica II, p. 102: la L è sciolta come «light». La sigla sta per loose.")
q("m3s-11", T, "l", "101–102", "Nell'ATP sintasi, quale parte ruota e quale fa da statore?", [
  "Ruotano l'anello c con γ ed ε; la subunità a, b₂ e δ sono lo statore", "Ruota la subunità a", "Ruotano le α e β", "Non ruota nulla"], 0,
  "Le α3β3 stanno ferme, tenute dal braccio periferico.",
  note="Sbobina di Biochimica II, p. 101: c'è scritto che «la proteina a è un rotore che gira». Ruota l'anello delle subunità c; la a fa parte dello statore.")
q("m3s-12", T, "l", "100", "La prima ipotesi sul meccanismo dell'ATP sintasi prevedeva intermedi ad alta energia (accoppiamento chimico). Chi è il premio Nobel della teoria chemiosmotica?", ["Peter Mitchell", "Hans Krebs", "Daniel Koshland", "Carl Cori"], 0,
  "Mitchell la propose nel 1961 e ricevette il Nobel nel 1978.",
  note="Sbobina di Biochimica II, p. 100: l'ipotesi dell'accoppiamento chimico è attribuita a Koshland e quella di Mitchell agli anni '70–'80. L'ipotesi chimica è di Slater (1953); Mitchell propose la teoria chemiosmotica nel 1961. Le date non sono nella sbobina, vengono dai testi di riferimento.")

T = "m3-radicali"
q("m3r-01", T, "f", "108", "Quale enzima trasforma l'anione superossido in perossido di idrogeno?", ["Superossido dismutasi", "Catalasi", "Glutatione perossidasi", "NADPH ossidasi"], 0,
  "La catalasi poi scinde H₂O₂ in acqua e ossigeno.")
q("m3r-02", T, "m", "109", "Che cosa fa la glutatione perossidasi?", [
  "Riduce i perossidi ossidando due glutatione (GSH → GSSG)", "Riduce il glutatione ossidato", "Produce superossido", "Ossida il NADPH"], 0,
  "Il GSSG viene poi ridotto dalla glutatione reduttasi con il NADPH.")
q("m3r-03", T, "m", "110", "Quando la catena respiratoria produce più radicali?", [
  "Quando l'ossigeno è scarso: gli elettroni si fermano sui trasportatori (es. ubichinone) e possono ridurre l'O₂ a superossido",
  "Quando c'è molto ossigeno", "Quando c'è molto ADP", "Mai, la catena è perfetta"], 0,
  "HIF sostituisce la subunità COX4-1 con COX4-2, più affine all'ossigeno.")
q("m3r-04", T, "a", "109", "Perché il selenio è importante nella difesa antiossidante?", [
  "È nel sito attivo della glutatione perossidasi come selenocisteina", "È un cofattore della catalasi", "Ripara il DNA", "Forma il glutatione"], 0,
  "Va però assunto in piccole quantità: in eccesso è tossico.")
q("m3r-05", T, "a", "109", "Quali metalli contengono le isoforme della superossido dismutasi?", ["Cu-Zn nel citosol, Mn nel mitocondrio", "Fe nel citosol, Cu nel mitocondrio", "Solo Zn", "Se e Fe"], 0,
  "Mutazioni della SOD1 (Cu-Zn) sono associate a forme di SLA.")
q("m3r-06", T, "l", "109", "Come si chiama il glutatione ossidato?", ["GSSG (disolfuro di glutatione)", "GSH", "GS-SeH", "Glutatione perossido"], 0,
  "Due GSH legati da un ponte disolfuro tra le cisteine.")

T = "m3-malattie"
q("m3m-01", T, "f", "111", "Da chi si eredita il DNA mitocondriale?", ["Solo dalla madre", "Solo dal padre", "Da entrambi", "Dipende dal sesso del figlio"], 0,
  "I mitocondri dello spermatozoo non vengono trasmessi allo zigote.")
q("m3m-02", T, "m", "111", "Quante proteine codifica il DNA mitocondriale umano?", ["13", "37", "1000", "Nessuna"], 0,
  "Tutte subunità della catena respiratoria e dell'ATP sintasi, più rRNA e tRNA.")
q("m3m-03", T, "m", "112", "Che cosa si intende per eteroplasmia?", [
  "Coesistenza in una cellula di mitocondri mutati e sani in proporzione variabile", "Tutti i mitocondri mutati", "Mitocondri di origine paterna", "DNA nucleare mutato"], 0,
  "L'omoplasmia è quando tutti i mitocondri sono uguali (tutti mutati o tutti sani).")
q("m3m-04", T, "a", "112", "Una donna ha una malattia da mutazione del mtDNA. Chi tra i suoi figli può ereditarla?", [
  "Sia i figli maschi sia le femmine", "Solo le figlie, con il 50% di probabilità", "Solo i maschi", "Nessuno"], 0,
  "Tutti i figli ricevono i mitocondri materni; la gravità dipende dalla quota di mitocondri mutati. Solo le figlie la trasmettono alla generazione successiva.",
  note="Sbobina di Biochimica II, p. 112: c'è scritto che «le figlie hanno il 50% di probabilità di ereditare la malattia, mentre i figli non sono a rischio». Il mtDNA va a tutti i figli, maschi e femmine; sono i maschi a non trasmetterlo.")
q("m3m-05", T, "a", "112", "Come può l'aumento di UCP2 nelle cellule β contribuire al diabete di tipo 2?", [
  "Scarica il gradiente protonico, riduce l'ATP e quindi la secrezione di insulina", "Aumenta la secrezione di glucagone", "Blocca i GLUT4", "Inibisce la glucochinasi"], 0,
  "L'aumento dei radicali (superossido) induce UCP2: meno ATP, canali K⁺ meno chiusi, meno insulina.")
q("m3m-06", T, "l", "113", "Qual è l'ipotesi mitocondriale dell'invecchiamento descritta nella sbobina?", [
  "I radicali danneggiano il mtDNA (con riparazione limitata), riducendo l'efficienza della catena respiratoria", "I telomeri mitocondriali si accorciano", "I mitocondri paterni si accumulano", "L'ATP sintasi si degrada"], 0,
  "È una delle ipotesi; un'altra chiama in causa difetti della divisione mitocondriale.")
