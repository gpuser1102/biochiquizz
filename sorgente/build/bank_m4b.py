"""Biochimica II – rinforzo dei livelli f/m/a/l: malattie mitocondriali (p. 111–114) e glicogeno (p. 115–132)."""
from bank_common import q

# ---------------------------------------------------------------- Malattie mitocondriali
T = "m3-malattie"
q("m3m-07", T, "f", "112", "Come si chiama la condizione in cui tutti i mitocondri di una cellula sono mutati?", ["Omoplasmia", "Eteroplasmia", "Aneuploidia", "Mosaicismo nucleare"], 0,
  "Con una proporzione variabile di mitocondri mutati e sani si parla di eteroplasmia.")
q("m3m-08", T, "f", "111", "Perché lo zigote non contiene mitocondri paterni?", [
  "Lo spermatozoo ne ha pochi e vengono degradati subito dopo la fecondazione", "Lo spermatozoo non ha mitocondri", "Vengono espulsi con il corpo polare", "Il DNA mitocondriale paterno è identico a quello materno"], 0,
  "Per questo l'eredità del mtDNA è esclusivamente materna.")
q("m3m-09", T, "m", "111", "Oltre alle 13 proteine, che cosa codifica il DNA mitocondriale?", ["rRNA e tRNA", "Tutti gli enzimi del ciclo di Krebs", "Le proteine del poro mitocondriale", "Gli istoni mitocondriali"], 0,
  "Le malattie mitocondriali possono dipendere anche da geni nucleari che regolano la funzione dei mitocondri.")
q("m3m-10", T, "m", "112", "Nella cellula β, perché serve tanto ATP per secernere insulina?", [
  "L'ATP chiude i canali K⁺, la membrana si depolarizza ed entra Ca²⁺ che fa uscire l'insulina", "L'ATP serve a sintetizzare il glucosio", "L'ATP apre i GLUT2", "L'ATP fosforila direttamente l'insulina"], 0,
  "Glucosio → GLUT2 → glicolisi e Krebs → ATP → chiusura dei canali K⁺ → Ca²⁺ → esocitosi.")
q("m3m-11", T, "a", "113", "Secondo la sbobina, come insulino-resistenza e disfunzione β si collegano nel diabete di tipo 2?", [
  "L'insulino-resistenza aumenta i radicali, che inducono UCP2 nelle cellule β: meno ATP e meno secrezione di insulina", "L'insulino-resistenza distrugge le cellule β per autoimmunità", "L'UCP2 aumenta la sintesi di ATP", "I radicali aumentano la secrezione di insulina"], 0,
  "La somma di disfunzione β e insulino-resistenza produce il diabete di tipo 2.")
q("m3m-12", T, "a", "114", "Perché nell'anziano si pensa che aumentino i radicali liberi?", [
  "Aumenta l'infiammazione generale (parametri infiammatori più alti), che produce radicali", "Perché diminuisce il numero di mitocondri a zero", "Perché il mtDNA paterno si attiva", "Perché cala l'ossigeno nel sangue"], 0,
  "Per questo con l'età si consiglia di aumentare gli antiossidanti.")
q("m3m-13", T, "l", "113", "Qual è l'ipotesi alternativa a quella del danno al mtDNA per spiegare l'invecchiamento?", [
  "Un difetto della divisione dei mitocondri", "L'accumulo di mitocondri paterni", "La perdita dell'ATP sintasi", "Un eccesso di UCP1"], 0,
  "Tutte le ipotesi concordano sul ruolo centrale del mitocondrio.")
q("m3m-14", T, "l", "111", "Quali sintomi possono dare le malattie mitocondriali?", [
  "Disturbi neurologici, disabilità fisiche, problemi di crescita, disturbi metabolici e di fertilità", "Solo anemia", "Solo cecità", "Solo infezioni ricorrenti"], 0,
  "Possono colpire qualsiasi organo; non c'è una cura, si gestiscono i sintomi.")

# ---------------------------------------------------------------- Degradazione
T = "m4-degradazione"
q("m4d-12", T, "f", "115", "Che tipo di polisaccaride è il glicogeno?", ["Omopolisaccaride ramificato di glucosio", "Eteropolisaccaride di glucosio e galattosio", "Polimero lineare di fruttosio", "Disaccaride"], 0,
  "Legami α-1,4 nelle catene e α-1,6 nelle ramificazioni; al centro c'è la glicogenina.")
q("m4d-13", T, "f", "116", "Da quale estremità la glicogeno fosforilasi stacca il glucosio?", ["Estremità non riducenti", "Estremità riducente", "Dal centro della molecola", "Dalla glicogenina"], 0,
  "Ogni ramificazione termina con un'estremità non riducente: tanti punti d'attacco.")
q("m4d-14", T, "m", "115", "Quali sono i tre enzimi della degradazione del glicogeno?", [
  "Glicogeno fosforilasi, transferasi, α-1,6-glucosidasi", "Glicogeno sintasi, ramificante, glicogenina", "Amilasi, maltasi, lattasi", "Esochinasi, glucochinasi, fosfoglucomutasi"], 0,
  "Transferasi e α-1,6-glucosidasi sono le due attività dell'enzima deramificante.")
q("m4d-15", T, "m", "117", "Che cosa succede al glucosio 6-P nel muscolo e nel fegato dopo la glicogenolisi?", [
  "Muscolo: solo glicolisi. Fegato: diventa glucosio libero che va nel sangue", "In entrambi va nel sangue", "Muscolo: va nel sangue. Fegato: glicolisi", "In entrambi diventa UDP-glucosio"], 0,
  "Il glicogeno muscolare ha funzione energetica, quello epatico mantiene la glicemia.")
q("m4d-16", T, "a", "117", "Perché le cellule extraepatiche, anche con una glucosio 6-fosfatasi, non riuscirebbero a esportare glucosio?", [
  "L'esochinasi, a Km molto bassa, rifosforilerebbe subito il glucosio libero", "Perché non hanno GLUT", "Perché il glucosio libero è tossico", "Perché la fosforilasi non funziona fuori dal fegato"], 0,
  "Nel fegato la glucochinasi fosforila il glucosio solo quando la sua concentrazione è alta.")
q("m4d-17", T, "a", "117", "Come lavora il sistema della glucosio 6-fosfatasi nel reticolo endoplasmatico?", [
  "T1 porta dentro il G6P, l'enzima lo idrolizza nel lume, T2 fa uscire il fosfato e T3 il glucosio", "L'enzima lavora nel citosol senza trasportatori", "Il glucosio esce dal RE con i GLUT4", "Il G6P viene idrolizzato nel mitocondrio"], 0,
  "Il glucosio esce poi dall'epatocita con i GLUT2.")
q("m4d-18", T, "l", "118", "Com'è fatta la glicogeno fosforilasi e come è legato il suo coenzima?", [
  "Omodimero; il piridossal fosfato è legato a un residuo di lisina", "Monomero; PLP legato a una serina", "Tetramero αβγδ; PLP libero", "Omodimero; FAD legato a una cisteina"], 0,
  "Qui il PLP usa il suo gruppo fosfato come catalizzatore acido-base, non il gruppo aldeidico.")
q("m4d-19", T, "l", "117", "Perché la glicogenolisi deve produrre molto glucosio per farlo uscire dal fegato?", [
  "I GLUT2 hanno bassa affinità: funzionano solo con glucosio intracellulare abbondante", "Perché i GLUT2 consumano ATP", "Perché il glucosio esce per esocitosi", "Perché serve a saturare l'esochinasi"], 0,
  "È uno dei motivi delle tante ramificazioni.")

# ---------------------------------------------------------------- Sintesi
T = "m4-sintesi"
q("m4s-10", T, "f", "123", "Quali sono i tre enzimi della sintesi del glicogeno?", [
  "Glicogeno sintasi, enzima ramificante, glicogenina", "Fosforilasi, transferasi, glucosidasi", "Esochinasi, fosfoglucomutasi, glucosio 6-fosfatasi", "PP1, PKA, GSK3"], 0,
  "La glicogeno sintasi è l'enzima principale e quello regolato.")
q("m4s-11", T, "f", "124", "Quale nucleotide fornisce l'energia per aggiungere glucosio al glicogeno?", ["UTP", "ATP", "GTP", "CTP"], 0,
  "UTP + glucosio 1-P → UDP-glucosio + PPi.")
q("m4s-12", T, "m", "124", "Che legame forma la glicogeno sintasi?", ["α-1,4", "α-1,6", "β-1,4", "β-1,6"], 0,
  "I legami α-1,6 delle ramificazioni li forma l'enzima ramificante.")
q("m4s-13", T, "m", "124", "Perché la glicogeno sintasi ha bisogno della glicogenina?", [
  "Non può iniziare una catena da zero: serve un primer, che la glicogenina costruisce su sé stessa", "Perché la glicogenina fornisce l'UTP", "Perché la glicogenina forma le ramificazioni", "Perché la glicogenina la fosforila"], 0,
  "La glicogenina aggiunge circa 7 glucosi alla propria tirosina e poi resta al centro, senza attività catalitica.")
q("m4s-14", T, "a", "124", "Perché una struttura ramificata è vantaggiosa per la sintesi e la degradazione?", [
  "Le tante estremità permettono di aggiungere o staccare molti glucosi contemporaneamente", "Perché rende il glicogeno più solubile in acqua del glucosio libero", "Perché i rami contengono UTP", "Perché la glicogenina sta su ogni ramo"], 0,
  "Inoltre accumulare glucosio libero creerebbe una pressione osmotica enorme.")
q("m4s-15", T, "a", "123", "In quali situazioni il glicogeno deve essere riformato?", [
  "Dopo l'attività fisica (muscolo) e dopo la notte o tra i pasti (fegato), quando arriva glucosio", "Solo durante il digiuno", "Solo durante lo sforzo", "Mai nel muscolo"], 0,
  "La sintesi è stimolata dall'insulina dopo i pasti.")
q("m4s-16", T, "l", "124", "Dove si era già incontrato l'UDP-glucosio nel corso?", ["Nel metabolismo del galattosio", "Nella via dei pentoso fosfati", "Nel ciclo di Krebs", "Nella β-ossidazione"], 0,
  "Lì serve all'UDP-galattosio 4-epimerasi e alla uridiltransferasi.")

# ---------------------------------------------------------------- Regolazione
T = "m4-regolazione"
q("m4r-11", T, "f", "119", "Come si chiamano le due forme della glicogeno fosforilasi?", [
  "Fosforilasi a (fosforilata, più attiva) e b (defosforilata, meno attiva)", "Fosforilasi a (defosforilata) e b (fosforilata)", "Fosforilasi R e T, entrambe fosforilate", "Fosforilasi I e D"], 0,
  "Ogni forma esiste negli stati R (attivo) e T (meno attivo).")
q("m4r-12", T, "f", "125", "Che effetto ha il glucosio 6-fosfato sulla glicogeno sintasi?", ["La attiva (effettore allosterico positivo)", "La inibisce", "La fosforila", "Nessuno"], 0,
  "Sposta la sintasi b dallo stato T allo stato R.")
q("m4r-13", T, "m", "120", "Quali molecole inibiscono la fosforilasi b muscolare riportandola nello stato T?", ["ATP e glucosio 6-P", "AMP e Ca²⁺", "cAMP e glucagone", "Glucosio 1-P e UTP"], 0,
  "Con tanto ATP la glicolisi è inutile; con tanto G6P è inutile degradare il glicogeno.")
q("m4r-14", T, "m", "125", "Quale forma della glicogeno sintasi è attiva?", ["Forma a, defosforilata", "Forma b, fosforilata", "Forma a, fosforilata", "Entrambe allo stesso modo"], 0,
  "È l'opposto della fosforilasi: la stessa fosforilazione spegne la sintesi e accende la degradazione.")
q("m4r-15", T, "a", "126", "Da che cosa è attivata e da che cosa è inibita la PP1?", [
  "Attivata da insulina, glucosio 6-P e glucosio; inibita da glucagone e adrenalina", "Attivata da glucagone; inibita da insulina", "Attivata da AMP; inibita da ATP", "Attivata da Ca²⁺; inibita da glucosio"], 0,
  "La PP1 defosforila fosforilasi a, fosforilasi chinasi e glicogeno sintasi.")
q("m4r-16", T, "a", "127", "Che differenza c'è tra glicogeno sintasi e fosforilasi nei siti di fosforilazione?", [
  "La sintasi ha siti multipli (più serine fosforilate), la fosforilasi uno solo", "La fosforilasi ha più siti", "Nessuna delle due viene fosforilata", "Hanno gli stessi siti"], 0,
  "La GSK3 fosforila in sequenza più serine dopo l'innesco della caseina chinasi 2.")
q("m4r-17", T, "a", "130", "Nel fegato, perché la fosforilasi a nello stato R blocca la sintesi del glicogeno?", [
  "Lega e inibisce la PP1 sulla GL: finché è in R la PP1 non può attivare la sintasi", "Perché consuma tutto l'UDP-glucosio", "Perché fosforila la sintasi", "Perché degrada la glicogenina"], 0,
  "Il glucosio la porta in T, la PP1 si libera e defosforila prima la fosforilasi e poi la sintasi.")
q("m4r-18", T, "l", "129", "Quali siti di GM vengono fosforilati e con quale effetto?", [
  "P1 (chinasi insulino-sensibile): attiva la PP1. P2 (adrenalina/PKA): la PP1 si stacca", "P1 e P2 dalla GSK3: inattivano la sintasi", "Solo P1, dall'adrenalina", "P2 dall'insulina: attiva la fosforilasi"], 0,
  "L'adrenalina fosforila anche un inibitore che si lega alla PP1 e la blocca del tutto.")
q("m4r-19", T, "l", "119", "Fosforilasi muscolare ed epatica sono:", [
  "Isoenzimi: stessa reazione, geni diversi, diversa localizzazione e regolazione", "Lo stesso enzima con la stessa regolazione", "Enzimi con reazioni diverse", "Forme a e b dello stesso gene"], 0,
  "L'AMP attiva solo la muscolare, il glucosio inibisce solo l'epatica.")

# ---------------------------------------------------------------- Controllo ormonale
T = "m4-ormoni"
q("m4o-07", T, "f", "120", "Quanti amminoacidi ha il glucagone e chi lo produce?", ["29, cellule α del pancreas", "51, cellule β", "14, cellule δ", "9, ipofisi posteriore"], 0,
  "È prodotto in ipoglicemia, lontano dai pasti.")
q("m4o-08", T, "f", "121", "Chi produce l'adrenalina?", ["La midollare del surrene", "La corticale del surrene", "Il pancreas", "L'ipofisi"], 0,
  "È l'ormone dell'attacco e della fuga; è un ormone di natura amminoacidica.")
q("m4o-09", T, "m", "120", "Che tipo di recettore ha il glucagone?", ["Recettore a 7 eliche transmembrana accoppiato a proteine G", "Recettore tirosin-chinasico", "Recettore intracellulare", "Canale ionico"], 0,
  "Gα-GTP attiva l'adenilato ciclasi → cAMP → PKA.")
q("m4o-10", T, "m", "121", "Di quali subunità è formata la fosforilasi chinasi?", ["(αβγδ)₄", "α₂β₂", "Un solo monomero", "(αβγ)₂"], 0,
  "La δ è simile alla calmodulina e lega il Ca²⁺ con mani EF.")
q("m4o-11", T, "a", "121", "Che cosa serve per la completa attivazione della fosforilasi chinasi muscolare?", [
  "Sia la fosforilazione da PKA sia il Ca²⁺: ciascuno da solo la attiva solo parzialmente", "Solo il cAMP", "Solo l'AMP", "Solo l'insulina"], 0,
  "Il Ca²⁺ rilasciato con la contrazione basta per gli sforzi leggeri, senza adrenalina.")
q("m4o-12", T, "a", "121–122", "Oltre al metabolismo, che cosa fa l'adrenalina per preparare all'azione?", [
  "Vasocostrizione cutanea e splancnica, che ridistribuisce il sangue verso i muscoli", "Vasodilatazione cutanea", "Abbassa la glicemia", "Blocca la glicolisi muscolare"], 0,
  "Aumenta energia, ossigeno e zucchero disponibili; nel fegato attiva la glicogenolisi.")
q("m4o-13", T, "a", "132", "Come l'insulina riduce la degradazione del glicogeno?", [
  "Attiva la PP1, che defosforila e spegne fosforilasi chinasi e glicogeno fosforilasi", "Attiva la PKA", "Aumenta il cAMP", "Fosforila la fosforilasi"], 0,
  "In parallelo la PKB inibisce la GSK3 e la sintasi resta attiva.",
  note="Sbobina di Biochimica II, p. 132: la «proteina chinasi insulino sensibile» che attiva la PP1 è chiamata PI3K. La PI3K è una chinasi lipidica (produce PIP₃) a monte della PKB; la chinasi che fosforila GM nel sito 1 è un'altra proteina. Non è nelle sbobine, ma è la versione del Lehninger.")
q("m4o-14", T, "l", "123", "Che cosa illustra lo schema della cascata glucagone → glucosio nel sangue?", [
  "L'amplificazione: poche molecole di ormone producono 10.000 e più molecole di glucosio", "Un ciclo futile", "Un feedback negativo", "Una via senza enzimi"], 0,
  "Ogni enzima attivato ne attiva molti al passaggio successivo.")
q("m4o-15", T, "l", "132", "Quando c'è glucagone, oltre a degradare il glicogeno, che cosa fa il fegato con la glicolisi?", [
  "La diminuisce: il glucosio formato deve uscire e non essere usato dall'epatocita", "La aumenta", "Non cambia", "La trasferisce nel mitocondrio"], 0,
  "Il fegato in ipoglicemia lavora per il resto dell'organismo.")
