"""Biologia molecolare – lezioni 1–3 (comunicazione cellulare, recettori di membrana, GPCR e via del cAMP).
La sbobina non ha numeri di pagina: il riferimento è la lezione."""
from bank_common import q as _q

S = "Biologia molecolare"
L1, L2, L3 = "lezione 1", "lezione 2", "lezione 3"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ---------------------------------------------------------------- 1. Comunicazione cellulare
T = "bm1-comunicazione"
q("b1c-01", T, "f", L1, "Come si chiama la comunicazione in cui il segnale resta sulla superficie della cellula che lo produce?", ["Juxtacrina (per contatto)", "Paracrina", "Endocrina", "Autocrina"], 0,
  "Serve il contatto fisico tra le cellule: ligando–recettore o gap junction.")
q("b1c-02", T, "f", L1, "Da quante connessine è formato un connessone?", ["6", "4", "12", "2"], 0,
  "Due connessoni affiancati, uno per cellula, formano una gap junction.")
q("b1c-03", T, "m", L1, "Che cosa può passare attraverso una gap junction?", ["Ioni, amminoacidi, zuccheri, nucleotidi", "Proteine intere", "Solo acqua", "Interi organelli"], 0,
  "Il poro esclude le proteine; le gap junction formano sinapsi elettriche (cuore, retina).")
q("b1c-04", T, "m", L1, "Nella segnalazione Notch, come arriva il segnale nel nucleo?", [
  "Il legame con Delta provoca il taglio proteolitico di Notch: la porzione intracellulare entra nel nucleo e attiva CSL", "Delta entra nella cellula bersaglio", "Notch attiva l'adenilato ciclasi", "Notch apre un canale per il Ca²⁺"], 0,
  "Notch regola lo sviluppo (asse destro-sinistro, cuore) e il mantenimento delle staminali.")
q("b1c-05", T, "a", L1, "Perché il recettore di un ormone endocrino deve avere affinità altissima?", [
  "L'ormone si diluisce nel sangue e arriva a concentrazioni di 10⁻¹²–10⁻⁹ M", "Perché agisce su cellule vicine", "Perché deve dissociarsi rapidamente", "Perché è sempre idrofobico"], 0,
  "Paracrina: 10⁻⁹–10⁻⁶ M; sinaptica: 10⁻⁶–10⁻³ M, con affinità bassa e dissociazione rapida.")
q("b1c-06", T, "a", L1, "Perché le connessine hanno un'emivita 10–20 volte più breve delle altre proteine di membrana?", [
  "La cellula sfrutta la loro instabilità per regolarne quantità e funzione", "Perché sono degradate dalle collagenasi", "Perché non sono glicosilate", "Perché si formano nel citosol"], 0,
  "Sovra o sottoespressione delle connessine è associata ad alcuni tumori e alla guarigione delle ferite.")
q("b1c-07", T, "l", L1, "Quale fattore di trascrizione attiva il frammento intracellulare di Notch?", ["CSL", "CREB", "STAT", "fos/jun"], 0,
  "CSL è presente nelle cellule che rispondono alla via di Notch.")
q("b1c-08", T, "l", L1, "Dove è tipica la comunicazione autocrina?", ["Negli organismi in sviluppo e nella risposta immunitaria e infiammatoria", "Nella giunzione neuromuscolare", "Nel controllo della glicemia", "Nella vista"], 0,
  "La stessa cellula produce il segnale e ne risente.")
q("bh1c-01", T, "h", L1, "Un neurotrasmettitore deve dare segnali brevissimi e ripetibili. Quale combinazione lo permette?", [
  "Concentrazione locale alta e affinità del recettore bassa, così il complesso si dissocia appena il ligando si diluisce", "Concentrazione bassa e affinità altissima", "Trasporto nel sangue legato a proteine", "Recettore nucleare con effetto genico", "Affinità altissima e degradazione lenta"], 0,
  "Nelle sinapsi la diluizione e la degradazione del neurotrasmettitore spostano subito l'equilibrio verso la forma dissociata.")

T = "bm1-recettore-ligando"
q("b1r-01", T, "f", L1, "Che relazione c'è tra Ka e Kd?", ["Kd = 1/Ka", "Kd = Ka", "Kd = Ka²", "Non sono collegate"], 0,
  "Kd bassa significa alta affinità.")
q("b1r-02", T, "m", L1, "Come si riconosce il legame specifico in una curva di saturazione recettore-ligando?", [
  "Cresce rapidamente e raggiunge un plateau (Bmax) quando i siti sono saturi", "Cresce lentamente e linearmente", "Diminuisce aumentando il ligando", "Non dipende dalla concentrazione di ligando"], 0,
  "Il legame aspecifico cresce lentamente e non satura.")
q("b1r-03", T, "a", L1, "Nel grafico di Scatchard (legato/libero contro legato), che cosa dà la pendenza?", ["−1/Kd", "Bmax", "Kd", "−Bmax"], 0,
  "L'intercetta con l'asse dei legati dà Bmax, il numero massimo di siti.")
q("b1r-04", T, "l", L1, "Perché l'analisi di Scatchard è utile in farmacologia?", [
  "Stima affinità e numero di recettori, utili per dosare agonisti e antagonisti", "Misura la velocità degli enzimi", "Misura il pI dei recettori", "Determina la sequenza del recettore"], 0,
  "Molti farmaci agiscono come agonisti o antagonisti del ligando naturale.")
q("bh1r-01", T, "h", L1, "Due farmaci si legano allo stesso recettore: A ha Kd = 1 nM, B ha Kd = 100 nM. Quale affermazione è corretta?", [
  "A ha affinità 100 volte maggiore: bastano concentrazioni più basse per occupare metà dei recettori", "B ha affinità maggiore perché la sua Kd è più alta", "Hanno la stessa affinità se hanno lo stesso Bmax", "A occupa per forza più recettori a saturazione", "Kd non dice nulla sull'affinità"], 0,
  "La Kd è la concentrazione di ligando che occupa il 50% dei siti; Bmax (numero di siti) non dipende dal farmaco.")

T = "bm1-intra-superficie"
q("b1i-01", T, "f", L1, "Dove si trova il recettore di un ormone idrofobico?", ["Nella cellula (citosol o nucleo)", "Sulla membrana plasmatica", "Nella matrice extracellulare", "Nel sangue"], 0,
  "L'ormone attraversa la membrana; nel sangue viaggia legato a proteine di trasporto.")
q("b1i-02", T, "f", L1, "Quale dominio riconosce le fosfotirosine?", ["SH2", "SH3", "PH", "Zinc finger"], 0,
  "Anche il dominio PTB lega fosfotirosine; SH3 lega sequenze ricche di prolina; PH lega fosfoinositidi.")
q("b1i-03", T, "m", L1, "Che cos'è un secondo messaggero?", [
  "Una piccola molecola intracellulare che amplifica il segnale del complesso recettore-ligando", "L'ormone stesso dentro la cellula", "Il recettore attivato", "La proteina di trasporto dell'ormone"], 0,
  "Esempi: Ca²⁺, cAMP, cGMP, DAG, fosfoinositidi.")
q("b1i-04", T, "m", L1, "Da quale precursore derivano catecolamine e ormoni tiroidei?", ["Tirosina", "Colesterolo", "Triptofano", "Glutammato"], 0,
  "Gli ormoni steroidei derivano dal colesterolo.")
q("b1i-05", T, "a", L1, "A cosa servono le proteine adattatrici (scaffold)?", [
  "Avvicinano i partner della cascata rendendo la segnalazione rapida ed efficiente", "Degradano i secondi messaggeri", "Trasportano gli ormoni nel sangue", "Formano il poro dei recettori canale"], 0,
  "Usano domini SH2, PTB, PH e SH3 per tenere insieme recettore, chinasi e bersagli.")
q("b1i-06", T, "l", L1, "Quale dominio posiziona una proteina sulla membrana legando il fosfatidilinositolo?", ["PH", "SH2", "SH3", "PTB"], 0,
  "Il dominio PH lega i fosfoinositidi di membrana.")
q("bh1i-01", T, "h", L1, "Perché un ormone peptidico non agisce direttamente sui geni come uno steroide?", [
  "È idrofilico, non attraversa la membrana: lega un recettore di superficie che genera secondi messaggeri", "Perché è troppo piccolo", "Perché viene sempre degradato nel sangue", "Perché i peptidi non possono legare proteine", "Perché agisce solo su cellule vicine"], 0,
  "Gli effetti sui geni possono comunque arrivare, ma indirettamente (es. CREB fosforilato dalla PKA).")

# ---------------------------------------------------------------- 2. Recettori di membrana
T = "bm2-canali"
q("b2c-01", T, "f", L2, "Quali sono le quattro famiglie di recettori di membrana?", [
  "Recettori canale, accoppiati a proteine G, con attività catalitica, per le citochine", "Nucleari, citosolici, di membrana, mitocondriali", "Solo canali ionici e GPCR", "Tirosin-chinasici, serin-chinasici, fosfatasi, proteasi"], 0,
  "Sono i quattro tipi trattati a lezione.")
q("b2c-02", T, "f", L2, "Il recettore nicotinico dell'acetilcolina è:", ["Un canale per cationi controllato da ligando", "Un recettore a 7 eliche accoppiato a proteina G", "Un recettore tirosin-chinasico", "Un recettore nucleare"], 0,
  "Il muscarinico invece è un GPCR.")
q("b2c-03", T, "m", L2, "Quali neurotrasmettitori sono inibitori e perché?", [
  "GABA e glicina: aprono canali per anioni (Cl⁻) e iperpolarizzano", "Acetilcolina e glutammato: aprono canali per Na⁺", "Serotonina e ATP: aprono canali per Ca²⁺", "Adrenalina: chiude i canali K⁺"], 0,
  "Gli eccitatori aprono canali per cationi e depolarizzano.")
q("b2c-04", T, "m", L2, "Come si spegne il segnale dell'acetilcolina?", [
  "Diffusione e idrolisi da parte dell'acetilcolinesterasi; la colina viene ricaptata e riutilizzata", "Endocitosi del recettore", "Attività GTPasica del recettore", "Fosforilazione da PKA"], 0,
  "Con affinità bassa, la diluizione sposta l'equilibrio verso la forma dissociata.")
q("b2c-05", T, "a", L2, "Differenza tra curari veri e depolarizzanti:", [
  "I veri sono antagonisti dell'acetilcolina; i depolarizzanti (succinilcolina) sono agonisti che desensibilizzano il recettore", "I veri sono agonisti, i depolarizzanti antagonisti", "Entrambi inibiscono l'acetilcolinesterasi", "I depolarizzanti bloccano i canali del Ca²⁺"], 0,
  "La succinilcolina dà prima fascicolazioni e poi paralisi flaccida.")
q("b2c-06", T, "a", L2, "Perché la neostigmina antagonizza l'effetto di un curaro vero?", [
  "Inibisce l'acetilcolinesterasi: più acetilcolina compete con il curaro per il recettore", "Lega direttamente il curaro", "Attiva i recettori muscarinici", "Blocca i canali del Na⁺"], 0,
  "Gli inibitori delle colinesterasi si usano anche in Alzheimer e myasthenia gravis.")
q("b2c-07", T, "a", L2, "Quali recettori muscarinici agiscono inibendo l'adenilato ciclasi?", ["M2 e M4 (numero pari)", "M1, M3, M5 (numero dispari)", "Solo M1", "Tutti"], 0,
  "I dispari agiscono attraverso la via dei fosfoinositidi.")
q("b2c-08", T, "l", L2, "Quale elica di ogni subunità del recettore nicotinico riveste il poro?", ["L'elica 2", "L'elica 1", "L'elica 4", "L'elica 7"], 0,
  "Porta residui acidi che rendono il canale selettivo per i cationi; nel GABA-A porta residui basici (anioni).")
q("b2c-09", T, "l", L2, "Da quale molecola deriva il GABA?", ["Glutammato, per decarbossilazione", "Glicina", "Acetil-CoA", "Tirosina"], 0,
  "Enzima: glutammato decarbossilasi.")
q("b2c-10", T, "l", L2, "Quale enzima sintetizza l'acetilcolina?", ["Colina acetiltransferasi", "Acetilcolinesterasi", "Colinesterasi", "Glutammato decarbossilasi"], 0,
  "Acetil-CoA + colina → acetilcolina.",
  note="Sbobina di Biologia molecolare, lezione 2: chiama «colinesterasi» l'enzima di sintesi; la colinesterasi la degrada, la sintesi è della colina acetiltransferasi.")
q("bh2c-01", T, "h", L2, "Un paziente esposto a un gas nervino (inibitore irreversibile dell'acetilcolinesterasi) ha paralisi. Quale ragionamento spiega l'uso di un antagonista come l'atropina?", [
  "L'acetilcolina si accumula e iperstimola i recettori: un antagonista ne blocca l'azione e riequilibra il sistema", "L'atropina riattiva l'acetilcolinesterasi", "L'atropina aumenta la sintesi di acetilcolina", "L'atropina degrada il gas nervino", "L'atropina apre i canali del Cl⁻"], 0,
  "Bloccare l'enzima che spegne il segnale lascia l'acetilcolina alta; l'antagonista toglie l'eccesso di stimolazione (l'atropina agisce sui muscarinici).")
q("bh2c-02", T, "h", L2, "Il GABA-B riduce l'eccitabilità del neurone. Con quale meccanismo?", [
  "Eterodimero GPCR: le subunità βγ della proteina G chiudono i canali Ca²⁺ e aprono quelli K⁺", "Apre direttamente un canale per il Cl⁻", "Attiva una tirosin-chinasi", "Inibisce l'acetilcolinesterasi", "Lega il DNA e reprime geni eccitatori"], 0,
  "L'uscita di K⁺ iperpolarizza la membrana. Il GABA-A è invece il recettore canale per il Cl⁻.")

T = "bm2-rtk"
q("b2r-01", T, "f", L2, "Come si attivano i recettori tirosin-chinasici?", [
  "Il ligando ne induce la dimerizzazione e l'autofosforilazione incrociata sulle tirosine", "Il ligando li apre come un canale", "Scambiano GDP con GTP", "Entrano nel nucleo"], 0,
  "Le fosfotirosine reclutano proteine con domini SH2.")
q("b2r-02", T, "f", L2, "Ras è attiva quando lega:", ["GTP", "GDP", "ATP", "cAMP"], 0,
  "È una piccola proteina G monomerica ancorata alla membrana per prenilazione.")
q("b2r-03", T, "m", L2, "Qual è l'ordine della via di Ras?", ["RTK → SOS → Ras → Raf → MEK → MAP chinasi → fos/jun", "RTK → Raf → Ras → MEK → STAT", "Ras → RTK → MEK → Raf", "RTK → PKA → Ras → CREB"], 0,
  "La MAP chinasi fosforilata entra nel nucleo e attiva fattori di trascrizione.")
q("b2r-04", T, "m", L2, "Che ruolo hanno GEF e GAP su Ras?", [
  "GEF scambia GDP con GTP (attiva); GAP stimola l'idrolisi del GTP (spegne)", "GEF idrolizza il GTP, GAP lo carica", "Entrambi la attivano", "Entrambi la fosforilano"], 0,
  "Si legano alla stessa regione di Ras: agisce l'una o l'altra.")
q("b2r-05", T, "a", L2, "Una mutazione impedisce a Ras di idrolizzare il GTP. Che cosa succede?", [
  "Ras resta sempre attiva e la via proliferativa è accesa anche senza fattore di crescita", "Ras resta inattiva", "Il recettore non dimerizza più", "Si blocca solo MEK"], 0,
  "È il meccanismo di molte mutazioni oncogeniche di Ras.")
q("b2r-06", T, "a", L2, "Come si è capito che MEK sta a valle di Ras e Raf?", [
  "In un mutante Ras bloccato su GDP (N17), un Raf oncogenico ripristina l'attivazione di MEK", "Con la cristallografia di MEK", "Bloccando MEK, Ras non si attiva", "Misurando il cAMP"], 0,
  "Se un attivatore a valle bypassa il blocco a monte, sta più in basso nella cascata.")
q("b2r-07", T, "l", L2, "Su quali residui viene fosforilata la MAP chinasi?", ["Thr183 e Tyr185", "Ser e Thr qualsiasi", "Tyr del dominio SH2", "His e Asp"], 0,
  "Si trovano nella regione «labbro» e ne cambiano la conformazione.")
q("b2r-08", T, "l", L2, "Che cosa ha di particolare il recettore dell'insulina?", ["È già un tetramero (2α + 2β) anche senza ligando", "È un canale ionico", "Non ha attività chinasica", "È un recettore nucleare"], 0,
  "Le subunità α legano l'insulina, le β hanno attività tirosin-chinasica.")
q("bh2r-01", T, "h", L2, "In una cellula tumorale il recettore EGF è sovraespresso, ma il fattore di crescita è normale. Perché la via proliferativa è comunque iperattiva?", [
  "Con molti recettori in membrana la dimerizzazione avviene anche senza ligando", "Perché il recettore diventa un canale", "Perché Ras perde il GTP", "Perché manca SOS", "Perché il recettore è nel nucleo"], 0,
  "Ipersintesi del recettore, recettore attivo da monomero o fattore di crescita sovraespresso: tutte accendono la via in modo anomalo.")
q("bh2r-02", T, "h", L2, "Una cellula ha una GAP non funzionante. Quale effetto ti aspetti?", [
  "Ras resta più a lungo nella forma GTP e la via MAPK è iperattiva", "Ras non si attiva mai", "Il recettore non si autofosforila", "Aumenta il cAMP", "La MAP chinasi non entra nel nucleo"], 0,
  "La GAP spegne Ras accelerandone l'attività GTPasica; perderla equivale a mantenere Ras accesa.")

T = "bm2-terapia"
q("b2t-01", T, "f", L2, "Contro quale recettore è diretto il trastuzumab?", ["HER2", "HER1 (EGFR)", "HER3", "Recettore dell'insulina"], 0,
  "È un anticorpo monoclonale umanizzato ricombinante; il cetuximab è contro HER1.")
q("b2t-02", T, "m", L2, "Perché HER2 è importante nei tumori pur non legando fattori di crescita?", [
  "Forma eterodimeri con gli altri HER e li attiva", "Perché è un canale ionico", "Perché degrada gli altri HER", "Perché lega direttamente il DNA"], 0,
  "La sua sovraespressione favorisce la proliferazione.")
q("b2t-03", T, "a", L2, "Quale tumore è associato a HER3 nella sbobina?", ["Carcinoma mammario", "Glioblastoma", "Tumore dell'ovaio", "Tumore della vescica"], 0,
  "HER1: vescica, seno, rene, prostata, glioblastoma; HER4: ovaio.")
q("b2t-04", T, "l", L2, "Contro quale recettore è diretto il cetuximab?", ["HER1 (EGFR)", "HER2", "HER4", "TGF-β"], 0,
  "Entrambi sono anticorpi monoclonali.")
q("bh2t-01", T, "h", L2, "Quali due strategie terapeutiche contro i recettori tirosin-chinasici descrive la sbobina?", [
  "Molecole anti-recettore che bloccano la segnalazione e anticorpi monoclonali selettivi", "Inibitori dell'acetilcolinesterasi e curari", "Analoghi del cAMP e inibitori delle fosfodiesterasi", "Agonisti di Ras e inibitori di GAP", "Steroidi e ormoni tiroidei"], 0,
  "L'immunoterapia colpisce i recettori attivati in modo anomalo nella trasformazione.")

T = "bm2-sertre"
q("b2s-01", T, "f", L2, "Quali ligandi legano i recettori serin/treonin-chinasici?", ["TGF-β e BMP", "Insulina ed EGF", "Acetilcolina e GABA", "Eritropoietina e interleuchine"], 0,
  "Le loro mutazioni contribuiscono ad alcune forme di cancro.")
q("b2s-02", T, "m", L2, "Quali proteine trasmettono il segnale del TGF-β al nucleo?", ["Le Smad", "Le STAT", "MAP chinasi", "CREB"], 0,
  "Fosforilate, formano eterodimeri, aumentano l'affinità per il DNA e attivano geni.")
q("b2s-03", T, "a", L2, "Che cosa cambia nelle Smad quando vengono fosforilate dal recettore?", [
  "Formano eterodimeri e la loro affinità per il DNA aumenta molto", "Vengono degradate", "Escono dal nucleo", "Diventano canali ionici"], 0,
  "Normalmente la loro affinità per il DNA è bassa.")
q("b2s-04", T, "l", L2, "Su quali residui si autofosforilano i recettori del TGF-β?", ["Serina e treonina", "Tirosina", "Istidina", "Lisina"], 0,
  "Hanno un solo dominio transmembrana, N-terminale extracellulare che lega il ligando e C-terminale catalitico.")

T = "bm2-citochine"
q("b2k-01", T, "f", L2, "Quale via di segnalazione usano i recettori per le citochine?", ["JAK-STAT", "Ras-MAPK", "cAMP-PKA", "IP₃-Ca²⁺"], 0,
  "È coinvolta in processi immunitari, divisione e morte cellulare.")
q("b2k-02", T, "m", L2, "Che differenza c'è tra un recettore per le citochine e un RTK?", [
  "Il recettore per le citochine non ha attività enzimatica: lo fosforila la chinasi JAK associata", "Il recettore per le citochine è un canale", "L'RTK non si fosforila", "Sono identici"], 0,
  "Negli RTK il recettore si autofosforila.")
q("b2k-03", T, "a", L2, "Quale ormone che controlla la proliferazione dei globuli rossi usa la via JAK-STAT?", ["Eritropoietina", "Insulina", "Glucagone", "Aldosterone"], 0,
  "Ha un ruolo fondamentale nell'emopoiesi.")
q("b2k-04", T, "l", L2, "Che cosa fa STAT dopo essere stata fosforilata?", ["Dimerizza, entra nel nucleo e attiva la trascrizione", "Fosforila JAK", "Apre canali ionici", "Viene secreta"], 0,
  "Le combinazioni di diversi JAK e STAT rendono la segnalazione selettiva.")
q("bh2k-01", T, "h", L2, "Una mutazione elimina l'attività chinasica di JAK. Quale effetto ha sulla segnalazione dell'eritropoietina?", [
  "Il recettore non viene fosforilato, STAT non si lega e non c'è attivazione genica", "Il recettore si autofosforila comunque", "STAT entra nel nucleo senza fosforilazione", "Aumenta la produzione di globuli rossi", "Si attiva la via di Ras al suo posto"], 0,
  "Il recettore per le citochine dipende interamente da JAK, perché non ha un dominio catalitico.")

# ---------------------------------------------------------------- 3. Recettori accoppiati a proteine G
T = "bm3-gpcr"
q("b3g-01", T, "f", L3, "Quante eliche transmembrana ha un GPCR?", ["7", "12", "4", "1"], 0,
  "N-terminale extracellulare, C-terminale citosolico.")
q("b3g-02", T, "f", L3, "Quale subunità della proteina G trimerica lega GDP/GTP?", ["α", "β", "γ", "Tutte e tre"], 0,
  "β e γ l'accompagnano; α e γ hanno ancore preniliche.")
q("b3g-03", T, "m", L3, "Quale loop del GPCR interagisce con la proteina G?", ["Il loop citoplasmatico C3, il più lungo", "Il loop extracellulare E1", "L'N-terminale", "L'elica 7"], 0,
  "Il cambio conformazionale indotto dal ligando lo modifica.")
q("b3g-04", T, "m", L3, "Che cosa succede quando la Gα scambia GDP con GTP?", [
  "Perde affinità per βγ e si separa, restando in membrana, per attivare l'effettore", "Si lega più forte a βγ", "Entra nel nucleo", "Viene degradata"], 0,
  "Gli effettori principali sono adenilato ciclasi e fosfolipasi C.")
q("b3g-05", T, "a", L3, "Perché le combinazioni di subunità della proteina G sono così numerose?", [
  ">20 geni per α, 5 per β e 6 per γ: oltre mille combinazioni, che permettono una regolazione fine", "Perché ogni GPCR ha una sola proteina G", "Perché la proteina G si autoassembla a caso", "Per lo splicing del recettore"], 0,
  "Le classi di Gα si distinguono per l'effettore con cui interagiscono.")
q("b3g-06", T, "l", L3, "Come si chiama l'oncogene che codifica una Gαs mutata senza attività GTPasica?", ["gsp", "ras", "raf", "erbB"], 0,
  "Trovato in quasi metà dei tumori ipofisari con alta produzione di GH.")
q("bh3g-01", T, "h", L3, "Nei tumori ipofisari con Gαs mutata (gsp) la secrezione di GH è altissima. Perché?", [
  "La Gαs non idrolizza il GTP, resta attiva e stimola continuamente l'adenilato ciclasi", "La Gαs non lega il GTP", "Il recettore del GHRH è assente", "L'ipofisi non riceve feedback", "La Gαs attiva la fosfolipasi C"], 0,
  "Senza attività GTPasica il segnale non si spegne: proliferazione e secrezione incontrollate.")

T = "bm3-camp"
q("b3c-01", T, "f", L3, "Quale enzima produce il cAMP?", ["Adenilato ciclasi", "Fosfodiesterasi", "Guanilato ciclasi", "Fosfolipasi C"], 0,
  "ATP → cAMP + PPi; la fosfodiesterasi lo degrada ad AMP.")
q("b3c-02", T, "f", L3, "Quale chinasi è attivata dal cAMP?", ["PKA", "PKC", "PKG", "MAP chinasi"], 0,
  "PKA = protein chinasi A, attivata dall'AMP ciclico.")
q("b3c-03", T, "m", L3, "Come si attiva la PKA?", [
  "Il cAMP si lega alle subunità regolatrici (2 per subunità), che rilasciano le subunità catalitiche", "Viene fosforilata dal recettore", "Lega il GTP", "Entra nel nucleo"], 0,
  "Servono 4 cAMP per liberare le 2 subunità catalitiche; il legame è cooperativo.")
q("b3c-04", T, "m", L3, "Quali ormoni usano Gs e quali Gi?", [
  "Gs: adrenalina, glucagone, ACTH. Gi: prostaglandine, adenosina", "Gs: prostaglandine; Gi: glucagone", "Tutti usano Gs", "Gs: insulina; Gi: adrenalina"], 0,
  "Gs aumenta l'attività dell'adenilato ciclasi, Gi la riduce.")
q("b3c-05", T, "a", L3, "Che cosa fa CREB dopo essere stato fosforilato dalla PKA?", [
  "Entra nel nucleo, lega le sequenze CRE e attiva la trascrizione di geni specifici", "Apre i canali del Ca²⁺", "Degrada il cAMP", "Inattiva il recettore"], 0,
  "La PKA può quindi modulare enzimi già presenti e anche la sintesi di nuove proteine.")
q("b3c-06", T, "a", L3, "Come agisce la tossina del colera?", [
  "ADP-ribosila un'arginina della Gαs, che non idrolizza più il GTP: cAMP sempre alto e perdita di acqua e sali", "Inibisce l'adenilato ciclasi", "Blocca la Gi", "Degrada il cAMP"], 0,
  "Le subunità B legano un ganglioside dell'epitelio intestinale; la A1 ha l'attività enzimatica.")
q("b3c-07", T, "a", L3, "Come agisce la tossina della pertosse?", [
  "ADP-ribosila la Gαi, che non viene più attivata: l'adenilato ciclasi non è inibita e il cAMP sale", "Attiva la Gαs", "Blocca la fosfodiesterasi", "Rende la Gi sempre attiva e abbassa il cAMP"], 0,
  "La Gi modificata non può più essere attivata dal recettore.",
  note="Sbobina di Biologia molecolare, lezione 3: dice che la Gi «rimane costantemente attiva» e il cAMP diminuisce; è il contrario.")
q("b3c-08", T, "l", L3, "Quale proteina ancora la PKA vicino ad adenilato ciclasi e recettore?", ["AKAP", "β-arrestina", "βARK", "Calmodulina"], 0,
  "AKAP5 recluta anche una fosfatasi per spegnere il segnale.")
q("b3c-09", T, "l", L3, "Che effetto ha la fosforilazione della glicogeno sintasi da parte della PKA?", ["La inattiva", "La attiva", "Nessun effetto", "La porta nel nucleo"], 0,
  "La PKA attiva invece la fosforilasi chinasi, che attiva la degradazione del glicogeno.",
  note="Sbobina di Biologia molecolare, lezione 3: mette la glicogeno sintasi tra le proteine «attivate» dalla PKA; la fosforilazione la inattiva.")
q("b3c-10", T, "l", L3, "Con la FRET sulla PKA (sonde su subunità regolatrice e catalitica), cosa indica la perdita del segnale FRET?", [
  "Che il cAMP è salito e le subunità si sono separate", "Che il cAMP è assente", "Che la PKA è stata degradata", "Che la proteina G è inattiva"], 0,
  "La FRET avviene solo se le due sonde sono vicinissime.")
q("bh3c-01", T, "h", L3, "Nel cuore, adrenalina e acetilcolina arrivano insieme. Come contribuiscono le subunità βγ liberate dal recettore dell'acetilcolina a bilanciare l'effetto?", [
  "Formano trimeri «spuri» con la Gαs attivata dall'adrenalina, sottraendola all'adenilato ciclasi", "Attivano direttamente la PKA", "Aumentano il cAMP", "Bloccano il recettore muscarinico", "Fosforilano il recettore β-adrenergico"], 0,
  "L'acetilcolina apre anche i canali K⁺ (iperpolarizzazione), rafforzando l'effetto inibitorio.")
q("bh3c-02", T, "h", L3, "Un paziente ha diarrea acquosa profusa dopo un viaggio. Quale catena di eventi molecolari è la più coerente con il colera?", [
  "Gαs ADP-ribosilata → adenilato ciclasi sempre attiva → cAMP alto → canali aperti nell'enterocita → perdita di acqua e sali", "Gαi attivata → cAMP basso → riassorbimento bloccato", "PKA inibita → chiusura dei canali", "Fosfodiesterasi attivata → cAMP basso → secrezione", "Recettore muscarinico bloccato → diarrea"], 0,
  "La tossina blocca l'attività GTPasica della Gαs: il segnale non si spegne più.")
q("bh3c-03", T, "h", L3, "Tra i bersagli della PKA c'è una fosfodiesterasi del cAMP. Che significato ha?", [
  "È un meccanismo di spegnimento: il segnale attiva l'enzima che degrada il proprio secondo messaggero", "Amplifica il segnale producendo altro cAMP", "Serve a produrre cGMP", "Attiva la proteina G", "Non ha alcun significato fisiologico"], 0,
  "Insieme all'attività GTPasica di Gα, alla β-arrestina e alle fosfatasi reclutate da AKAP.")

T = "bm3-spegnimento"
q("b3s-01", T, "f", L3, "Qual è il meccanismo di spegnimento intrinseco della proteina G?", ["L'attività GTPasica della Gα", "La fosforilazione della Gα", "La degradazione della Gβγ", "L'endocitosi della Gα"], 0,
  "Idrolizzato il GTP, la Gα si riassocia a βγ nel trimero inattivo.")
q("b3s-02", T, "m", L3, "Quale proteina si lega al recettore β-adrenergico fosforilato e ne blocca l'interazione con la proteina G?", ["β-arrestina", "AKAP", "GRB2", "SOS"], 0,
  "Si lega alla stessa superficie usata dalla proteina G.")
q("b3s-03", T, "a", L3, "Quale chinasi fosforila la coda C-terminale del recettore β-adrenergico e chi la richiama?", [
  "La βARK, richiamata dalle subunità βγ liberate", "La PKA, richiamata dal cAMP", "La PKC, richiamata dal DAG", "La MAP chinasi"], 0,
  "Anche la PKA può fosforilare il recettore.")
q("b3s-04", T, "l", L3, "Che cosa succede al recettore desensibilizzato dopo l'endocitosi?", [
  "Viene defosforilato e riportato in membrana, oppure degradato nel lisosoma", "Viene sempre degradato", "Resta nell'endosoma per sempre", "Viene secreto"], 0,
  "Nell'endosoma l'arrestina si dissocia.")
q("bh3s-01", T, "h", L3, "Durante una stimolazione adrenergica prolungata la risposta cardiaca diminuisce, anche se l'adrenalina è ancora legata. Perché?", [
  "Il recettore fosforilato da βARK lega la β-arrestina, non attiva più la Gs e viene internalizzato", "L'adrenalina viene degradata", "La Gs perde la sua ancora prenilica", "Il cAMP non attiva più la PKA", "L'adenilato ciclasi viene sintetizzata di meno"], 0,
  "È la desensibilizzazione o adattamento del recettore.")
