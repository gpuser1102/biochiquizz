"""Biologia molecolare – via del cGMP (lezione 3), calcio e fosfolipidi (lezione 4), insulina (lezione 5)."""
from bank_common import q as _q

S = "Biologia molecolare"
L3, L4, L5 = "lezione 3", "lezione 4", "lezione 5"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ---------------------------------------------------------------- cGMP
T = "bm3-cgmp"
q("b3m-01", T, "f", L3, "Quale enzima produce il cGMP?", ["Guanilato ciclasi", "Adenilato ciclasi", "Fosfolipasi C", "Fosfodiesterasi 5"], 0,
  "GTP → cGMP + PPi; la fosfodiesterasi lo degrada a GMP.")
q("b3m-02", T, "f", L3, "Quale chinasi è attivata dal cGMP?", ["PKG", "PKA", "PKC", "PKB"], 0,
  "La PKG è un omodimero, in due isoforme (PKG-1 e PKG-2).")
q("b3m-03", T, "m", L3, "Dove si trova il recettore dell'NO e perché?", [
  "Nel citosol: l'NO è un gas che attraversa la membrana", "Sulla membrana plasmatica, con 7 eliche", "Nel nucleo, come gli steroidi", "Nel reticolo endoplasmatico"], 0,
  "È una guanilato ciclasi solubile con un gruppo eme: l'NO si lega al ferro e la attiva.")
q("b3m-04", T, "m", L3, "Qual è il recettore del peptide natriuretico atriale?", [
  "Un recettore di membrana con attività guanilato ciclasica", "Un GPCR accoppiato a Gs", "La guanilato ciclasi solubile del citosol", "Un recettore canale"], 0,
  "Le due vie del cGMP: recettore di membrana catalitico (ANP) e recettore citosolico per l'NO.",
  note="Sbobina di Biologia molecolare, lezione 3: tra le due vie parla di «peptidi che portano alla formazione di NO (es. peptide natriuretico atriale)». L'ANP agisce invece sul proprio recettore di membrana con attività guanilato ciclasica, senza passare per l'NO.")
q("b3m-05", T, "a", L3, "Come fa l'NO a provocare vasodilatazione?", [
  "↑cGMP → PKG → abbassa il Ca²⁺ e attiva la fosfatasi delle catene leggere della miosina → rilassamento", "↑cAMP → PKA → contrazione", "Apre i canali del Ca²⁺", "Attiva la PKC"], 0,
  "La PKG apre anche canali K⁺ (iperpolarizzazione) e inibisce i canali del Ca²⁺ voltaggio-dipendenti.")
q("b3m-06", T, "a", L3, "Come agisce il sildenafil (Viagra)?", [
  "Inibisce la fosfodiesterasi 5, mantenendo alto più a lungo il cGMP nella muscolatura dei vasi", "Attiva la guanilato ciclasi", "Libera NO", "Blocca la PKG"], 0,
  "La vasodilatazione aumenta l'afflusso di sangue nel tessuto erettile.")
q("b3m-07", T, "l", L3, "Perché una seconda stimolazione con NO a breve distanza produce molto meno cGMP?", [
  "La PKG ha attivato una fosfodiesterasi del cGMP che resta attiva", "Perché l'NO non attraversa più la membrana", "Perché la guanilato ciclasi è stata degradata", "Perché il GTP è esaurito"], 0,
  "Lo spegnimento è intrinseco alla via: picco rapido di cGMP e poi calo.")
q("b3m-08", T, "l", L3, "Quale gruppo prostetico lega l'NO nella guanilato ciclasi solubile?", ["Eme", "FAD", "Biotina", "Centro Fe-S"], 0,
  "L'NO si coordina al ferro in sesta posizione.")
q("bh3m-01", T, "h", L3, "Una cellula muscolare liscia vascolare riceve NO. Quale sequenza è corretta?", [
  "NO → guanilato ciclasi citosolica → cGMP → PKG → ↓Ca²⁺ e defosforilazione delle catene leggere → rilassamento", "NO → GPCR → Gs → cAMP → PKA → contrazione", "NO → recettore di membrana → PLC → IP₃ → contrazione", "NO → PKC → fosforilazione della miosina → contrazione", "NO → fosfodiesterasi 5 → più cGMP"], 0,
  "La PDE5 degrada il cGMP: inibirla prolunga l'effetto.",
  note="Sbobina di Biologia molecolare, lezione 3: nel riepilogo scrive «Il GMP ciclico attiva la proteina G» e «la proteina G fosforila i suoi bersagli»; si intende la PKG (protein chinasi G).")

# ---------------------------------------------------------------- Calcio
T = "bm4-calcio"
q("b4c-01", T, "f", L4, "Qual è la concentrazione di Ca²⁺ nel citosol a riposo?", ["≈ 10⁻⁷–10⁻⁸ M", "≈ 10⁻³ M", "≈ 1 M", "≈ 10⁻¹ M"], 0,
  "Fuori dalla cellula e negli organuli (RE, mitocondrio) è circa 10⁻³ M.")
q("b4c-02", T, "f", L4, "Come viene portato fuori dalla cellula il Ca²⁺?", [
  "Con la Ca²⁺-ATPasi e con l'antiporto Na⁺/Ca²⁺", "Per diffusione semplice", "Con i recettori per l'IP₃", "Con i recettori per la rianodina"], 0,
  "Altre Ca²⁺-ATPasi lo pompano nel reticolo sarcoplasmatico e nei mitocondri.")
q("b4c-03", T, "m", L4, "Quali processi controlla il Ca²⁺ come secondo messaggero?", [
  "Contrazione muscolare, secrezione di ormoni e neurotrasmettitori, divisione cellulare, metabolismo, espressione genica", "Solo la contrazione muscolare", "Solo la trascrizione", "Solo la sintesi di ATP"], 0,
  "Il segnale è la variazione della sua concentrazione citosolica.")
q("b4c-04", T, "m", L4, "Com'è fatto il recettore per l'IP₃?", [
  "Un canale del RE formato da 4 subunità, ognuna con 6 eliche, con residui acidi nel poro (selettività per il Ca²⁺)", "Un GPCR a 7 eliche", "Un recettore tirosin-chinasico", "Un canale a 5 subunità come il nicotinico"], 0,
  "Legando l'IP₃ si apre e lascia uscire il Ca²⁺ dal RE.")
q("b4c-05", T, "a", L4, "Che cosa apre fisiologicamente il recettore per la rianodina?", [
  "Il Ca²⁺ stesso (rilascio di Ca²⁺ indotto da Ca²⁺)", "La rianodina endogena", "L'IP₃", "Il cAMP"], 0,
  "La rianodina è un alcaloide vegetale insetticida, non una molecola endogena.")
q("b4c-06", T, "a", L4, "Che effetto ha la rianodina a basse e ad alte concentrazioni?", [
  "Bassa: blocca il canale semiaperto (contrazione massiva). Alta (µM): lo chiude (paralisi)", "Bassa: lo chiude; alta: lo apre", "Lo apre sempre", "Non agisce sul canale"], 0,
  "Effetto opposto in base alla dose.")
q("b4c-07", T, "l", L4, "Dove sono espressi RyR1, RyR2 e RyR3?", ["Muscolo scheletrico, miocardio, cervello", "Cervello, fegato, rene", "Miocardio, muscolo scheletrico, fegato", "Tutti e tre nel muscolo liscio"], 0,
  "Tutti consentono la fuoriuscita del Ca²⁺ dal reticolo.")
q("bh4c-01", T, "h", L4, "Perché un piccolo rilascio di Ca²⁺ dall'IP₃ può diventare un grande aumento di Ca²⁺ citosolico?", [
  "Il Ca²⁺ rilasciato apre i recettori per la rianodina e i canali voltaggio-dipendenti, amplificando il segnale", "Perché l'IP₃ apre la Ca²⁺-ATPasi", "Perché il Ca²⁺ blocca l'antiporto Na⁺/Ca²⁺ in modo permanente", "Perché la calmodulina rilascia il Ca²⁺ legato", "Perché il mitocondrio non accumula più Ca²⁺"], 0,
  "Anche la calmodulina-Ca²⁺ può riaprire i recettori per la rianodina.")

T = "bm4-calmodulina"
q("b4m-01", T, "f", L4, "Quanti ioni Ca²⁺ lega la calmodulina?", ["4", "2", "1", "7"], 0,
  "Due domini a mano EF, ciascuno con due siti, separati da una lunga α-elica.")
q("b4m-02", T, "f", L4, "Com'è fatto un dominio a mano EF?", [
  "Due α-eliche unite da un loop che coordina il Ca²⁺", "Un foglietto β a barile", "Un dito di zinco", "Un dominio SH2"], 0,
  "Il Ca²⁺ forma 7 legami di coordinazione con residui acidi (bipiramide pentagonale).")
q("b4m-03", T, "m", L4, "Che cosa succede alla calmodulina quando lega il Ca²⁺?", [
  "Cambia conformazione, si richiude e lega e attiva proteine bersaglio come la CaM chinasi", "Viene degradata", "Entra nel RE", "Si lega al DNA"], 0,
  "Modula anche fosfodiesterasi, adenilato ciclasi, Ca²⁺-ATPasi e chinasi delle catene leggere della miosina.")
q("b4m-04", T, "a", L4, "Come il Ca²⁺ favorisce la degradazione del glicogeno nel muscolo?", [
  "Ca²⁺-calmodulina attiva la fosforilasi chinasi, che fosforila e attiva la glicogeno fosforilasi", "Il Ca²⁺ attiva la glicogeno sintasi", "Il Ca²⁺ inibisce la fosforilasi chinasi", "Il Ca²⁺ attiva la PP1"], 0,
  "Contemporaneamente viene bloccata la sintesi del glicogeno.")
q("b4m-05", T, "a", L4, "Come può il Ca²⁺ cambiare l'espressione genica?", [
  "Ca²⁺-calmodulina attiva la CaM chinasi, che fosforila fattori di trascrizione come CREB", "Il Ca²⁺ si lega direttamente al DNA", "Il Ca²⁺ attiva STAT", "Il Ca²⁺ inibisce la RNA polimerasi"], 0,
  "CREB è fosforilato anche dalla PKA.")
q("b4m-06", T, "l", L4, "Quale stato della glicogeno sintasi e della glicogeno fosforilasi corrisponde alla fosforilazione?", [
  "Sintasi fosforilata inattiva, fosforilasi fosforilata attiva", "Entrambe attive", "Entrambe inattive", "Sintasi attiva, fosforilasi inattiva"], 0,
  "Così una stessa cascata di fosforilazioni favorisce la degradazione e blocca la sintesi.")
q("bh4m-01", T, "h", L4, "Durante la contrazione il Ca²⁺ sale nel muscolo. Quale effetto coordinato ha sul glicogeno?", [
  "Attiva la fosforilasi chinasi (degradazione) e una chinasi che inattiva la glicogeno sintasi: più glucosio per la glicolisi", "Attiva la sintesi e blocca la degradazione", "Non ha effetti sul glicogeno", "Attiva la PP1 che defosforila entrambi gli enzimi", "Blocca la glicolisi per risparmiare ATP"], 0,
  "Il muscolo che si contrae ha bisogno di ATP dalla glicolisi.")

T = "bm4-fosfoinositidi"
q("b4p-01", T, "f", L4, "Che cosa libera la fosfolipasi C dal PIP₂?", ["IP₃ e DAG", "Acido arachidonico", "Acido fosfatidico", "PIP₃"], 0,
  "Il DAG resta in membrana; l'IP₃ diffonde fino al reticolo endoplasmatico.")
q("b4p-02", T, "f", L4, "Quale fosfolipasi libera di solito l'acido arachidonico?", ["Fosfolipasi A2", "Fosfolipasi A1", "Fosfolipasi C", "Fosfolipasi D"], 0,
  "Taglia l'estere in posizione 2 del glicerolo; la D libera l'acido fosfatidico.")
q("b4p-03", T, "m", L4, "Quale isoforma di PLC è attivata dai GPCR e quale dagli RTK?", ["PLCβ da Gq, PLCγ da RTK", "PLCγ da Gq, PLCβ da RTK", "PLCδ da entrambi", "Solo PLCβ da entrambi"], 0,
  "La PLCβ può essere attivata anche dalle βγ delle proteine Gi.")
q("b4p-04", T, "m", L4, "Che cosa serve per attivare la PKC?", ["DAG e Ca²⁺ (più fosfatidilserina di membrana)", "Solo cAMP", "Solo IP₃", "cGMP"], 0,
  "Il Ca²⁺ porta la PKC in membrana sulla fosfatidilserina, il DAG scopre il sito catalitico.")
q("b4p-05", T, "a", L4, "Quale di questi processi è attivato dall'aumento di Ca²⁺ via IP₃?", [
  "La secrezione di enzimi digestivi pancreatici indotta dall'acetilcolina", "La sintesi di glicogeno epatico", "La produzione di cGMP da NO", "La degradazione del cAMP"], 0,
  "Anche secrezione di amilasi salivare e di insulina, contrazione della muscolatura liscia, glicogenolisi epatica.")
q("b4p-06", T, "a", L4, "Che cosa produce la PI3-chinasi e che cosa attiva?", [
  "PIP₃ (fosfato in posizione 3), che attiva la PKB", "IP₃, che apre il RE", "DAG, che attiva la PKC", "cAMP, che attiva la PKA"], 0,
  "Il PIP₃ non è substrato della PLC; la PKB favorisce sopravvivenza, captazione di glucosio e sintesi di glicogeno.")
q("b4p-07", T, "l", L4, "Dove taglia la fosfolipasi C?", ["Tra il carbonio 3 del glicerolo e il gruppo fosfato", "Tra il C1 e l'acido grasso", "Tra il fosfato e la testa polare", "Tra il C2 e l'acido grasso"], 0,
  "Così si stacca la testa polare (IP₃) con il suo fosfato.")
q("b4p-08", T, "l", L4, "Quali proteine attivate dalla PKB controllano la proliferazione secondo la sbobina?", ["c-Myc, Bcl-2, Bad", "fos e jun", "Smad", "STAT"], 0,
  "fos e jun sono a valle della MAP chinasi.")
q("bh4p-01", T, "h", L4, "Un ormone lega un GPCR accoppiato a Gq. Quale sequenza è corretta?", [
  "Gq-GTP → PLCβ → PIP₂ → IP₃ (rilascio di Ca²⁺ dal RE) + DAG → Ca²⁺ e DAG attivano la PKC", "Gq → adenilato ciclasi → cAMP → PKA", "Gq → PI3K → PIP₃ → PKC", "Gq → PLCγ → PIP₃ → PKB", "Gq → guanilato ciclasi → PKG"], 0,
  "Lo stesso esito (PLC → IP₃ + DAG) si ottiene da un RTK attraverso la PLCγ.")
q("bh4p-02", T, "h", L4, "In una cellula manca la PI3-chinasi. Quale via dell'insulina resta più compromessa?", [
  "Quella Ras-indipendente: niente PIP₃, niente PKB, quindi meno traslocazione di GLUT4 e meno sintesi di glicogeno", "Quella Ras-MAPK", "La via del cAMP", "La via JAK-STAT", "Nessuna, il PIP₂ basta"], 0,
  "Gli effetti immediati dell'insulina passano per IRS1 → PI3K → PIP₃ → PKB.")

T = "bm4-asse"
q("b4a-01", T, "f", L4, "Dove agiscono gli ormoni di rilascio prodotti dall'ipotalamo?", ["Sull'ipofisi anteriore", "Direttamente sui tessuti bersaglio", "Sul pancreas", "Sulla midollare del surrene"], 0,
  "L'ipofisi anteriore produce poi ACTH, TSH, LH, FSH, GH.")
q("b4a-02", T, "f", L4, "Quali ormoni rilascia l'ipofisi posteriore?", ["Ossitocina e vasopressina", "ACTH e TSH", "Insulina e glucagone", "LH e FSH"], 0,
  "L'ossitocina agisce su utero e ghiandola mammaria, la vasopressina sul riassorbimento renale di acqua.",
  note="Sbobina di Biologia molecolare, lezione 4: dice che la vasopressina controlla il riassorbimento di acqua «a livello delle arteriole renali»; agisce sui tubuli distali e sui dotti collettori (acquaporine).")
q("b4a-03", T, "m", L4, "Che cosa sono i feedback ultrabreve, breve e lungo?", [
  "L'ormone ipotalamico inibisce l'ipotalamo; l'ormone ipofisario inibisce l'ipotalamo; l'ormone periferico inibisce ipofisi e ipotalamo", "Tre ormoni diversi della tiroide", "Tre tempi di risposta degli steroidi", "Tre tipi di recettore"], 0,
  "Esempio: T3 e T4 inibiscono TSH e TRH.")
q("b4a-04", T, "m", L4, "In una tiroidite con T3 e T4 bassi, come sarà il TSH?", ["Alto, perché manca il feedback negativo", "Basso", "Normale", "Assente"], 0,
  "È uno dei criteri diagnostici.")
q("b4a-05", T, "a", L4, "Com'è fatto il TRH?", [
  "Tripeptide: piroglutammato, istidina, prolina ammidata al C-terminale", "Dipeptide di glicina e tirosina", "Proteina di 51 aa", "Derivato del colesterolo"], 0,
  "La sua identificazione valse il Nobel a Guillemin e Schally: gli ormoni di rilascio sono prodotti in quantità di nanogrammi.")
q("b4a-06", T, "a", L4, "Come funziona un dosaggio radioimmunologico di un ormone?", [
  "L'ormone non marcato del campione compete con quello radioattivo per l'anticorpo; con una curva standard si ricava la concentrazione", "Si misura la radioattività dell'ormone endogeno", "Si conta il numero di recettori", "Si misura l'assorbanza a 280 nm"], 0,
  "Più ormone non marcato c'è, meno ormone marcato resta legato all'anticorpo.")
q("b4a-07", T, "l", L4, "Nel test ELISA, che cosa rivela la presenza dell'ormone?", [
  "Un anticorpo secondario coniugato a un enzima che trasforma un substrato in un prodotto colorato", "La radioattività", "La fluorescenza dell'ormone", "Il precipitato di proteine"], 0,
  "L'intensità del colore è proporzionale alla quantità di ormone.")
q("b4a-08", T, "l", L4, "Come si dosa l'acetilcolina con enzimi accoppiati?", [
  "Acetilcolinesterasi → colina; colina ossidasi → betaina + H₂O₂; perossidasi usa H₂O₂ per un prodotto colorato", "Con un anticorpo marcato", "Misurando il pH", "Con la colina acetiltransferasi"], 0,
  "Il colore è proporzionale all'H₂O₂ e quindi all'acetilcolina.")
q("bh4a-01", T, "h", L4, "Un paziente ha TSH molto basso e T3/T4 alti. Quale interpretazione è coerente con l'asse?", [
  "Eccesso di ormoni tiroidei di origine tiroidea che, con il feedback negativo, sopprime TSH e TRH", "Deficit di TRH ipotalamico", "Tiroidite con distruzione della ghiandola", "Recettori ipofisari del TRH iperattivi", "Mancanza di iodio"], 0,
  "Se il problema fosse ipofisario (TSH alto) avremmo TSH e ormoni tiroidei entrambi alti.")

# ---------------------------------------------------------------- Insulina
T = "bm5-insulina"
q("b5i-01", T, "f", L5, "Quali cellule producono l'insulina?", ["Cellule β delle isole di Langerhans", "Cellule α", "Cellule δ", "Cellule acinose"], 0,
  "Le α producono glucagone, le δ somatostatina.")
q("b5i-02", T, "f", L5, "Da quanti amminoacidi è formata l'insulina matura?", ["51 (21 + 30)", "29", "86", "110"], 0,
  "PM ≈ 5808. Il glucagone ha 29 aa.")
q("b5i-03", T, "m", L5, "Come matura l'insulina?", [
  "Preproinsulina → (taglio del peptide segnale nel RE) proinsulina → (taglio del peptide C) insulina", "Viene sintetizzata già matura", "Proinsulina → preproinsulina → insulina", "Per glicosilazione nel Golgi"], 0,
  "Il taglio avviene vicino ad amminoacidi basici.")
q("b5i-04", T, "m", L5, "Quali fattori stimolano la secrezione di insulina?", [
  "Glucosio, amminoacidi (arginina), acidi grassi, ormoni gastrointestinali, parasimpatico, sulfoniluree", "Adrenalina e simpatico", "Solo il glucosio", "Glucagone e cortisolo soltanto"], 0,
  "Simpatico e adrenalina (stress) la inibiscono.")
q("b5i-05", T, "m", L5, "Qual è la proteina bersaglio fosforilata dal recettore dell'insulina, comune alle due vie?", ["IRS1 (substrato 1 del recettore dell'insulina)", "SOS", "PKA", "STAT"], 0,
  "Da IRS1 partono la via Ras-dipendente e quella Ras-indipendente.")
q("b5i-06", T, "a", L5, "Che differenza c'è tra effetti immediati e tardivi dell'insulina?", [
  "Immediati (minuti, 10⁻⁹–10⁻¹⁰ M): GLUT4 ed enzimi del glicogeno. Tardivi (ore, 10⁻⁸ M): espressione genica (meno gluconeogenesi, più sintesi di trigliceridi)", "Sono identici", "Gli immediati richiedono più insulina", "I tardivi passano per il cAMP"], 0,
  "I tardivi usano la via Ras-MAPK, gli immediati la via PI3K-PKB.")
q("b5i-07", T, "a", L5, "Come la PKB favorisce la sintesi di glicogeno?", [
  "Fosforila e inattiva la GSK3, così la glicogeno sintasi resta defosforilata e attiva", "Fosforila e attiva la glicogeno sintasi", "Attiva la glicogeno fosforilasi", "Aumenta il cAMP"], 0,
  "In più attiva la PP1 e la traslocazione dei GLUT4.")
q("b5i-08", T, "a", L5, "Come l'insulina contrasta l'azione del glucagone sulla PKA?", [
  "Attiva una fosfodiesterasi che abbassa il cAMP", "Blocca il recettore del glucagone", "Fosforila la PKA", "Aumenta l'adenilato ciclasi"], 0,
  "Con meno cAMP la PKA è meno attiva.")
q("b5i-09", T, "l", L5, "Come riconosce la GSK3 il suo substrato?", [
  "Lega una fosfoserina di innesco (priming) introdotta dalla caseina chinasi II e poi fosforila le serine successive", "Lega il glucosio", "Riconosce una sequenza ricca di prolina", "Lega l'UDP-glucosio"], 0,
  "La PKB fosforila un sito di pseudosubstrato all'N-terminale della GSK3, che si ripiega su sé stessa e si inattiva.")
q("b5i-10", T, "l", L5, "Quale proteina nel muscolo, fosforilata dall'insulina, porta la PP1 sul granulo di glicogeno?", ["GM", "IRS1", "AKAP", "Calmodulina"], 0,
  "La PKA (adrenalina) fosforila la GM in un altro sito e la PP1 si stacca; un inibitore fosforilato dalla PKA la blocca.")
q("b5i-11", T, "l", L5, "Perché il dosaggio del peptide C è utile in un diabetico trattato con insulina?", [
  "L'insulina farmaco non ha peptide C: il peptide C misura solo l'insulina endogena", "Perché il peptide C abbassa la glicemia", "Perché il peptide C è l'insulina attiva", "Perché misura la resistenza all'insulina"], 0,
  "È prodotto in quantità equimolare all'insulina endogena.")
q("bh5i-01", T, "h", L5, "Dopo un pasto, nel muscolo, la glicogeno sintasi è attiva e la fosforilasi inattiva. Quale combinazione di eventi dovuti all'insulina lo spiega?", [
  "PKB inattiva la GSK3 e la PP1 (portata da GM) defosforila sia la sintasi (attivandola) sia la fosforilasi (inattivandola)", "La PKA fosforila entrambi gli enzimi", "Il Ca²⁺ attiva la fosforilasi chinasi", "La GSK3 fosforila e attiva la glicogeno sintasi", "Il cAMP sale e attiva la PP1"], 0,
  "Sintasi attiva da defosforilata, fosforilasi attiva da fosforilata: la PP1 sposta entrambe verso la sintesi.",
  note="Sbobina di Biologia molecolare, lezione 5: in un passaggio scrive «la glicogeno sintasi è defosforilata (inattiva)»: defosforilata è attiva, come dice la sbobina stessa poco prima.")
q("bh5i-02", T, "h", L5, "Un paziente ha glicemia alta, insulina alta e peptide C alto. Quale meccanismo è più probabile?", [
  "Resistenza all'insulina, per esempio per ridotta espressione o internalizzazione del recettore", "Deficit di secrezione delle cellule β", "Eccesso di somatostatina", "Insulina esogena in eccesso", "Mutazione del peptide C"], 0,
  "Nel diabete di tipo 2 l'insulina c'è ma i tessuti non rispondono; nel tipo 1 manca la secrezione.")
q("bh5i-03", T, "h", L5, "Quale via mediata dall'insulina porta alla trascrizione di geni per glicolisi, glicogeno e acidi grassi?", [
  "IRS1 → Grb2 → SOS → Ras → Raf → MEK → MAP chinasi → fattori di trascrizione", "IRS1 → PI3K → PIP₃ → PKB → GLUT4", "Recettore → Gs → cAMP → CREB", "Recettore → JAK → STAT", "Recettore → PLCβ → IP₃ → Ca²⁺"], 0,
  "È la via Ras-dipendente, responsabile degli effetti anabolici a lungo termine.")
q("bh5i-04", T, "h", L5, "Perché le sulfoniluree aumentano la secrezione di insulina?", [
  "Chiudono i canali K⁺-ATP della cellula β, depolarizzando la membrana e facendo entrare Ca²⁺", "Attivano direttamente il recettore dell'insulina", "Inibiscono il glucagone", "Aumentano i GLUT4", "Bloccano la GSK3"], 0,
  "La sbobina cita le sulfoniluree tra i farmaci che stimolano la secrezione.",
  note="Il meccanismo sui canali K⁺-ATP non è spiegato nella sbobina, ma è lo stesso passaggio che usa il glucosio (ATP → chiusura dei canali K⁺ → depolarizzazione → Ca²⁺).")
