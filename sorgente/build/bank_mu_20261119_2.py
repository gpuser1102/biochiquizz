"""Giro 2026-11-19, blocco 2 – Biochimica I: carboidrati (p. 182–197): monosaccaridi, legame glicosidico
e disaccaridi, polisaccaridi e peptidoglicano, glicoproteine."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Monosaccaridi (p. 182–187) ─────────────────────────────────────────────
T = "d9-mono"
q("u1119-056", T, "f", "182", "Quale formula empirica vale per la maggior parte dei carboidrati?", [
  "(CH₂O)n",
  "(CHO)n",
  "(CH₂)nO",
  "(CH₃O)n",
  "Cn(H₂O)2n",
  ], 0,
  "Da qui «idrati di carbonio». Non vale per tutti: alcuni contengono anche N, P o S.")
q("u1119-057", T, "f", "182", "Quali sono i monosaccaridi più piccoli?", [
  "I triosi, come gliceraldeide e diidrossiacetone",
  "I tetrosi, come l'eritrosio e il chetoso eritrulosio",
  "I pentosi, come ribosio e ribulosio",
  "I diosi, come la glicolaldeide e l'acetone",
  "Gli esosi, come glucosio e fruttosio",
  ], 0,
  "Dalla D-gliceraldeide derivano gli aldosi, dal diidrossiacetone i chetosi.")
q("u1119-058", T, "m", "182", "Come si stabilisce se un monosaccaride appartiene alla serie D?", [
  "Dall'OH del carbonio chirale più lontano dal carbonile, a destra nella proiezione di Fischer",
  "Dall'OH del carbonio anomerico, che nella proiezione di Fischer si trova a destra",
  "Dal segno della rotazione della luce polarizzata, che è positivo per tutti gli zuccheri D",
  "Dall'OH del C2, che nella proiezione di Fischer degli zuccheri D si trova sempre a destra",
  "Dal carbonile, che negli zuccheri D si trova in basso nella proiezione di Fischer",
  ], 0,
  "È il penultimo carbonio. La serie D/L non dice nulla sul verso della rotazione (destrogiro o levogiro). Quasi tutti i monosaccaridi naturali sono D.")
q("u1119-059", T, "m", "183", "Che cosa sono due epimeri?", [
  "Stereoisomeri che differiscono per la configurazione di un solo carbonio, non quello che definisce la serie D/L",
  "Enantiomeri che differiscono per la configurazione di tutti i carboni chirali e sono immagini speculari",
  "Stereoisomeri che differiscono solo per la configurazione del penultimo carbonio, quello che definisce la serie D/L",
  "Isomeri di struttura che differiscono per la posizione del gruppo carbonilico, come aldosi e chetosi",
  "Forme cicliche dello stesso zucchero che differiscono per la posizione dell'OH sul carbonio anomerico",
  ], 0,
  "Esempio: glucosio e galattosio, che differiscono solo al C4. Le forme che differiscono al carbonio anomerico sono gli anomeri.")
q("u1119-060", T, "f", "188", "Di quale carbonio il galattosio è epimero rispetto al glucosio?", [
  "C4",
  "C2",
  "C3",
  "C5",
  "C1",
  ], 0,
  "Cambia solo la posizione dell'OH sul C4.")
q("u1119-061", T, "l", "183", "Qual è il primo chetoso che ha un centro chirale?", [
  "Eritrulosio",
  "Diidrossiacetone",
  "Ribulosio",
  "Xilulosio",
  "Gliceraldeide",
  ], 0,
  "Il diidrossiacetone (3 C) non ha centri chirali; l'eritrulosio (4 C) ne ha uno. La gliceraldeide è un aldoso.")
q("u1119-062", T, "m", "184", "Nella ciclizzazione del glucosio a glucopiranosio, quali gruppi reagiscono e che cosa si forma?", [
  "Il C1 aldeidico e l'OH del C5: si forma un emiacetale",
  "Il C1 aldeidico e l'OH del C4: si forma un emiacetale",
  "Il C1 aldeidico e l'OH del C6: si forma un acetale",
  "Il C2 chetonico e l'OH del C5: si forma un emichetale",
  "Il C1 aldeidico e l'OH del C5: si forma un acetale",
  ], 0,
  "L'OH del penultimo carbonio attacca il carbonio aldeidico, che da sp² diventa sp³ e un nuovo stereocentro (anomeri α e β).")
q("u1119-063", T, "a", "184", "Nella formula di Haworth del D-glucopiranosio, come riconosci l'anomero α?", [
  "L'OH del C1 è dal lato opposto rispetto al C6 (in basso)",
  "L'OH del C1 è dallo stesso lato del gruppo CH₂OH del C6 (in alto)",
  "L'OH del C1 giace sul piano dell'anello",
  "Il C6 è sotto il piano dell'anello",
  "L'OH del C2 è dallo stesso lato del C6",
  ], 0,
  "Nel β l'OH anomerico sta dallo stesso lato del C6. Gli OH a destra nella proiezione di Fischer vanno in basso nella formula di Haworth.")
q("u1119-064", T, "f", "184", "Quale anomero del D-glucosio prevale in soluzione acquosa?", [
  "Il β, circa due terzi",
  "L'α, circa due terzi",
  "Sono al 50% ciascuno",
  "La forma lineare aperta",
  "La forma furanosica",
  ], 0,
  "Eppure è l'anomero α quello che più comunemente forma i polimeri (amido, glicogeno).")
q("u1119-065", T, "h", "184", "Sciogli in acqua α-D-glucosio puro: la rotazione specifica parte da circa +112° e scende fino a +52,7°. Perché?", [
  "L'anello si apre e si richiude di continuo finché α e β raggiungono l'equilibrio (mutarotazione)",
  "Il glucosio si ossida lentamente ad acido gluconico, che ruota la luce polarizzata molto meno",
  "Il glucosio si isomerizza a fruttosio fino all'equilibrio, perché il fruttosio è levogiro",
  "L'anello piranosico si trasforma via via in quello furanosico, che ha un potere rotatorio minore",
  "Le molecole si associano tra loro con legami glicosidici e formano disaccaridi meno attivi",
  ], 0,
  "All'equilibrio circa 1/3 α (+112,2°) e 2/3 β (+18,7°) danno +52,7°.",
  note="Sbobina di Biochimica I, p. 184: dà all'α-D-glucopiranosio una rotazione di +122°. Il valore corretto è +112,2° (le proporzioni corrette sono circa 36% α e 64% β; la sbobina arrotonda a 30/70).")
q("u1119-066", T, "m", "184", "Come ciclizza il fruttosio nel β-D-fruttofuranosio?", [
  "Il carbonio chetonico C2 reagisce con l'OH del C5: si forma un emichetale",
  "Il carbonio chetonico C1 reagisce con l'OH del C4: si forma un emichetale",
  "Il carbonio aldeidico C1 reagisce con l'OH del C5: si forma un emiacetale",
  "Il carbonio chetonico C2 reagisce con l'OH del C5: si forma un chetale",
  "Il carbonio chetonico C3 reagisce con l'OH del C6: si forma un emichetale",
  ], 0,
  "Il nuovo stereocentro è il C2, su cui si formano gli anomeri α e β.",
  note="Sbobina di Biochimica I, p. 184: scrive che nei chetosi il gruppo chetonico «sta in posizione 1». Nel fruttosio il carbonile è sul C2, come la sbobina stessa dice subito dopo.")
q("u1119-067", T, "a", "185", "Che differenza c'è tra il passaggio sedia → barca e il passaggio α → β di un glucopiranosio?", [
  "Sedia/barca è un cambio di conformazione senza rottura di legami; α/β cambia la configurazione e richiede l'apertura dell'anello",
  "Sedia/barca cambia la configurazione e richiede l'apertura dell'anello; α/β è un cambio di conformazione senza rottura di legami",
  "Sono entrambi cambi di conformazione per rotazione attorno ai legami singoli, senza rompere nessun legame covalente dell'anello",
  "Sono entrambi cambi di configurazione che richiedono di rompere un legame covalente e di riformarlo dal lato opposto",
  "Sedia/barca richiede un enzima specifico (una mutarotasi), mentre α/β avviene spontaneamente senza rottura di legami",
  ], 0,
  "La sedia è la conformazione più comune; la barca si trova soprattutto nei polisaccaridi con sostituenti ingombranti.")
q("u1119-068", T, "m", "185", "Che cosa si ottiene ossidando in condizioni blande il C1 del glucosio?", [
  "L'acido gluconico, un acido aldonico",
  "L'acido glucuronico, un acido aldonico",
  "L'acido gluconico, un acido uronico",
  "L'acido glucarico, un acido aldarico",
  "Il sorbitolo, un polialcol",
  ], 0,
  "Ossidando il C6 si ha un acido uronico (glucuronico); ossidando C1 e C6 un acido aldarico (glucarico). Il sorbitolo si ottiene invece per riduzione.")
q("u1119-069", T, "l", "186", "Che cosa si ottiene ossidando sia il C1 sia il C6 del glucosio con ossidanti forti?", [
  "Acido glucarico",
  "Acido glucuronico",
  "Acido gluconico",
  "Glucono-δ-lattone",
  "Acido glicolico",
  ], 0,
  "Gli acidi aldarici hanno due gruppi carbossilici.")
q("u1119-070", T, "l", "185", "Come si chiama il lattone che si forma quando l'acido gluconico ciclizza perdendo acqua?", [
  "δ-gluconolattone",
  "γ-gluconolattone",
  "β-gluconolattone",
  "ε-gluconolattone",
  "α-gluconolattone",
  ], 0,
  "δ perché il legame coinvolge l'ossigeno del carbonio δ, cioè il C5. È il prodotto della glucosio ossidasi.")
q("u1119-071", T, "a", "186", "Come funziona il dosaggio enzimatico del glucosio in sangue e urine descritto nella sbobina?", [
  "La glucosio ossidasi ossida il C1 producendo H₂O₂, che una perossidasi usa per colorare un substrato incolore",
  "La glucosio ossidasi riduce il C1 consumando H₂O₂, e una perossidasi decolora un indicatore già colorato",
  "Il Cu²⁺ ossida il glucosio e si riduce a Cu⁺, che una perossidasi accoppiata trasforma in un composto colorato",
  "La perossidasi ossida direttamente il glucosio a gluconato e libera un colorante legato al glucosio",
  "La glucosio ossidasi produce NADH, che riduce un sale di rame e fa comparire un precipitato rosso",
  ], 0,
  "L'intensità del colore è proporzionale al glucosio presente. Ha sostituito la reazione di Fehling, semiquantitativa.")
q("u1119-072", T, "f", "186", "Su quale principio si basa la reazione di Fehling per rilevare il glucosio?", [
  "Il glucosio si ossida e riduce il Cu²⁺ a Cu⁺",
  "Il glucosio si riduce e ossida il Cu⁺ a Cu²⁺",
  "Il glucosio lega il Cu²⁺ e forma un complesso blu",
  "Il Cu²⁺ idrolizza il glucosio in due triosi",
  "Il glucosio precipita con il Cu²⁺ come sale",
  ], 0,
  "È la proprietà riducente del carbonio aldeidico (anomerico libero).")
q("u1119-073", T, "f", "187", "Che cos'è la N-acetilglucosammina?", [
  "Un glucosio con un gruppo amminico al posto di un OH, acetilato sull'azoto",
  "Un glucosio con un gruppo acetile al posto del gruppo aldeidico",
  "Un glucosio legato con un legame glicosidico a una molecola di acetilcolina",
  "Una glucosammina con un gruppo fosfato aggiunto sull'azoto amminico",
  "Un amminoacido acetilato legato al carbonio anomerico del glucosio",
  ], 0,
  "Glucosio → glucosammina (OH sostituito da un'ammina) → N-acetilglucosammina (NAG).")

# ── Legame glicosidico e disaccaridi (p. 187–189) ──────────────────────────
T = "d9-glicosidico"
q("u1119-074", T, "f", "187", "Che tipo di gruppo funzionale è il legame glicosidico?", [
  "Un acetale, formato dal gruppo emiacetalico con un altro alcol",
  "Un emiacetale, formato da un gruppo aldeidico con un altro alcol",
  "Un estere, formato da un acido con un gruppo alcolico",
  "Un'anidride, formata da due gruppi carbossilici",
  "Un'ammide, formata da un'ammina con un carbossile",
  ], 0,
  "Si forma con perdita di una molecola d'acqua; il carbonio anomerico coinvolto non è più ossidabile.")
q("u1119-075", T, "m", "187", "Nel nome di un disaccaride, che cosa indica il suffisso «-il» (es. α-D-glucopiranosil-)?", [
  "Il residuo il cui carbonio anomerico è impegnato nel legame, all'estremità non riducente",
  "Il residuo che conserva il carbonio anomerico libero e ossidabile, all'estremità riducente",
  "Il residuo legato con un legame β invece che α, a qualunque estremità",
  "Il residuo che porta la ramificazione α(1→6) nel punto di diramazione",
  "Il residuo in forma furanosica, che si trova all'estremità non riducente",
  ], 0,
  "Come negli amminoacidi, l'ultimo residuo della sequenza (qui quello riducente) è indicato con il nome intero.")
q("u1119-076", T, "a", "188", "Perché il maltosio è uno zucchero riducente e il saccarosio no?", [
  "Nel maltosio il C1 del secondo glucosio è libero; nel saccarosio sono impegnati entrambi i carboni anomerici",
  "Nel maltosio il legame è α, nel saccarosio è β, e i legami β impediscono l'ossidazione del carbonio",
  "Il saccarosio contiene fruttosio, e i chetosi non possono mai ridurre il rame della reazione di Fehling",
  "Nel maltosio il legame è α(1→6), che lascia libero il C1; nel saccarosio è α(1→4), che lo impegna",
  "Il maltosio si apre in due glucosi liberi in acqua, mentre il saccarosio resta intatto in soluzione",
  ], 0,
  "Saccarosio: C1 del glucosio e C2 del fruttosio sono legati tra loro, nessun emiacetale resta libero.")
q("u1119-077", T, "m", "188", "Quale legame unisce galattosio e glucosio nel lattosio?", [
  "β(1→4)",
  "α(1→4)",
  "β(1→6)",
  "α(1→6)",
  "α(1→2)β",
  ], 0,
  "Il C1 del galattosio in β è legato al C4 del glucosio; il C1 del glucosio resta libero, quindi il lattosio è riducente.")
q("u1119-078", T, "l", "188", "Quali carboni sono impegnati nel legame glicosidico del saccarosio?", [
  "Il C1 del glucosio e il C2 del fruttosio",
  "Il C1 del glucosio e il C1 del fruttosio",
  "Il C1 del glucosio e il C4 del fruttosio",
  "Il C2 del glucosio e il C1 del fruttosio",
  "Il C1 del glucosio e il C6 del fruttosio",
  ], 0,
  "Sono i due carboni anomerici: per questo il saccarosio non è riducente.")
q("u1119-079", T, "h", "188", "Un disaccaride formato da due glucosi non riduce il reattivo di Fehling. Come sono legati i due glucosi?", [
  "Con un legame tra i due C1 anomerici (α1↔α1)",
  "Con un legame α(1→4), come nel maltosio",
  "Con un legame β(1→4), come nel cellobiosio",
  "Con un legame α(1→6), come nell'isomaltosio",
  "Con un legame β(1→6), come nel gentiobiosio",
  ], 0,
  "Per non essere riducente nessun carbonio anomerico deve restare libero, come nel saccarosio. È il trealosio, che non è nelle sbobine: il principio è quello di p. 188.")
q("u1119-080", T, "f", "189", "In un punto di ramificazione del glicogeno, come continua la nuova catena?", [
  "Un solo legame α(1→6) al punto di ramificazione, poi legami α(1→4)",
  "Solo legami α(1→6), uno per ogni glucosio della nuova catena",
  "Un legame β(1→6) al punto di ramificazione, poi legami β(1→4)",
  "Un legame α(1→4) al punto di ramificazione, poi solo legami α(1→6)",
  "Un legame α(1→6) ogni due residui lungo tutta la nuova catena",
  ], 0,
  "Il legame 1,6 è possibile grazie all'OH del C6, che reagisce con il carbonio anomerico di un altro glucosio.")

# ── Polisaccaridi e peptidoglicano (p. 189–197) ────────────────────────────
T = "d9-poli"
q("u1119-081", T, "f", "189", "Che differenza c'è tra omopolisaccaridi ed eteropolisaccaridi?", [
  "Gli omopolisaccaridi ripetono lo stesso zucchero, gli eteropolisaccaridi zuccheri diversi",
  "Gli omopolisaccaridi sono lineari, gli eteropolisaccaridi sono sempre ramificati",
  "Gli omopolisaccaridi sono di riserva, gli eteropolisaccaridi solo di origine batterica",
  "Gli omopolisaccaridi hanno legami α, gli eteropolisaccaridi solo legami β",
  "Gli omopolisaccaridi sono vegetali, gli eteropolisaccaridi solo animali",
  ], 0,
  "Entrambi possono essere lineari o ramificati. Negli eteropolisaccaridi spesso si ripete un'unità disaccaridica.")
q("u1119-082", T, "m", "190", "Che differenza c'è tra amilosio e amilopectina?", [
  "L'amilosio è lineare con legami α(1→4) e forma un'elica; l'amilopectina è ramificata con legami α(1→6)",
  "L'amilosio è ramificato con legami α(1→6); l'amilopectina è lineare con legami α(1→4) e forma un'elica",
  "L'amilosio ha legami β(1→4) come la cellulosa; l'amilopectina ha legami α(1→4) e α(1→6) come il glicogeno",
  "Sono entrambi ramificati, ma l'amilosio ha un'estremità riducente in più per ogni punto di ramificazione",
  "L'amilosio è la riserva delle piante, l'amilopectina è la riserva degli animali al posto del glicogeno",
  ], 0,
  "Sono le due forme dell'amido, la riserva di glucosio delle piante (e di alcuni batteri e cianobatteri).")
q("u1119-083", T, "a", "190", "In che cosa differiscono soprattutto l'amilopectina e il glicogeno?", [
  "Nella frequenza delle ramificazioni: ogni 24–30 residui nell'amilopectina, ogni 8–12 nel glicogeno",
  "Nel tipo di legame: l'amilopectina ha legami β(1→4), il glicogeno legami α(1→4) e α(1→6)",
  "Nel numero di estremità riducenti: molte nell'amilopectina, una sola per molecola di glicogeno",
  "Nella frequenza delle ramificazioni: ogni 8–12 residui nell'amilopectina, ogni 24–30 nel glicogeno",
  "Nel monomero: l'amilopectina è un polimero di fruttosio, il glicogeno un polimero di glucosio",
  ], 0,
  "Entrambi hanno una sola estremità riducente e molte non riducenti, su cui agiscono gli enzimi che aggiungono o staccano glucosio.")
q("u1119-084", T, "f", "191", "Perché l'uomo non può usare la cellulosa come fonte di glucosio?", [
  "Non ha la cellulasi, l'enzima che scinde i legami β(1→4)",
  "Non ha l'amilasi, l'enzima che scinde i legami α(1→4)",
  "Non ha l'isomaltasi, che scinde i legami α(1→6) della cellulosa",
  "La cellulosa contiene galattosio, che l'intestino non assorbe",
  "La cellulosa è troppo ramificata per essere attaccata dagli enzimi",
  ], 0,
  "Batteri, funghi e alcuni insetti hanno la cellulasi; noi no.")
q("u1119-085", T, "a", "191", "Perché la cellulosa forma fibre insolubili mentre l'amilosio si avvolge in un'elica?", [
  "Con i legami β(1→4) ogni sedia è ruotata di 180°: catene diritte che si associano con legami H",
  "Con i legami α(1→4) ogni sedia è ruotata di 180°: catene diritte che si associano con legami H",
  "La cellulosa è molto ramificata e le ramificazioni si intrecciano formando fibre insolubili",
  "La cellulosa ha gruppi carbossilici che si legano al calcio e formano fibre insolubili",
  "La cellulosa è formata da fruttosio, che non può formare le eliche tipiche del glucosio",
  ], 0,
  "I tanti legami H tra catene adiacenti danno insolubilità e resistenza meccanica, utili per la funzione strutturale.")
q("u1119-086", T, "f", "191", "Da quali unità sono formati i glicosamminoglicani?", [
  "Da unità disaccaridiche ripetute di un acido uronico e di N-acetilglucosammina o N-acetilgalattosammina",
  "Da unità disaccaridiche ripetute di glucosio e galattosio, unite da legami β(1→4) come nel lattosio",
  "Da catene di N-acetilglucosammina e acido sialico legate a una ceramide nella membrana",
  "Da unità ripetute di NAG e NAM unite da brevi peptidi con D-amminoacidi, come nei batteri",
  "Da catene ramificate di mannosio legate a un'asparagina della proteina tramite il dolicolo",
  ], 0,
  "Sono anche detti mucopolisaccaridi.")
q("u1119-087", T, "m", "191", "Perché i glicosamminoglicani sono catene anioniche?", [
  "A pH neutro i loro gruppi acidi (carbossili degli acidi uronici) sono deprotonati",
  "A pH neutro i loro gruppi amminici liberi perdono il protone e diventano negativi",
  "Legano molti ioni cloruro, che si fissano agli ossidrili degli zuccheri",
  "Contengono molti residui di aspartato e glutammato nella catena polisaccaridica",
  "Contengono fosfati sul carbonio anomerico di ogni unità che si ripete",
  ], 0,
  "Per questo i loro nomi finiscono in «-ato». I gruppi solfato, che aggiungono altre cariche negative, non sono nelle sbobine.")
q("u1119-088", T, "m", "192", "Che differenza c'è tra un proteoglicano e una glicoproteina?", [
  "Nel proteoglicano prevale la parte glucidica (fino al 95%), nella glicoproteina quella proteica",
  "Nel proteoglicano prevale la parte proteica, nella glicoproteina quella glucidica (fino al 95%)",
  "Il proteoglicano ha solo O-glicosilazioni, la glicoproteina solo N-glicosilazioni sull'asparagina",
  "Il proteoglicano si trova nelle membrane, la glicoproteina solo nel plasma come proteina circolante",
  "Il proteoglicano contiene eteropolisaccaridi lipidici, la glicoproteina solo oligosaccaridi di glucosio",
  ], 0,
  "Nei proteoglicani i glicosamminoglicani costituiscono circa il 95% della massa.")
q("u1119-089", T, "l", "192", "Negli aggregati di proteoglicani, quale molecola fa da asse centrale e quale è la proteina nucleo?", [
  "Acido ialuronico come asse, aggrecano come proteina nucleo",
  "Aggrecano come asse, acido ialuronico come proteina nucleo",
  "Condroitin solfato come asse, collagene come proteina nucleo",
  "Eparina come asse, fibronectina come proteina nucleo",
  "Cellulosa come asse, elastina come proteina nucleo",
  ], 0,
  "Sulla proteina nucleo si attaccano le catene di glicosamminoglicani.")
q("u1119-090", T, "f", "192", "Quale di queste NON è una funzione dei proteoglicani?", [
  "Riserva di glucosio per i tessuti",
  "Lubrificazione",
  "Componente strutturale del connettivo",
  "Adesione delle cellule alla matrice",
  "Legame di fattori di crescita",
  ], 0,
  "La riserva di glucosio è il glicogeno (amido nelle piante).")
q("u1119-091", T, "m", "195", "Che cosa ha di particolare il tetrapeptide del peptidoglicano?", [
  "Contiene D-amminoacidi: D-glutammato e D-alanina",
  "Contiene solo L-amminoacidi, come le proteine umane",
  "Contiene idrossiprolina e idrossilisina, come il collagene",
  "Contiene cisteine che formano ponti disolfuro tra catene",
  "È legato al NAG con un legame N-glicosidico sull'asparagina",
  ], 0,
  "Sequenza L-Ala, D-Glu, L-Lys, D-Ala. Il ribosoma non può usare D-amminoacidi: li inseriscono enzimi specifici.")
q("u1119-092", T, "a", "196", "Come differisce il legame crociato del peptidoglicano tra Gram-positivi e Gram-negativi?", [
  "Gram+: ponte di pentaglicina tra D-Ala e L-Lys; Gram−: la Lys (o il DAP) lega direttamente la D-Ala vicina",
  "Gram+: la Lys lega direttamente la D-Ala vicina; Gram−: ponte di pentaglicina tra D-Ala e L-Lys",
  "Gram+: ponte disolfuro tra cisteine; Gram−: legame isopeptidico tra lisina e glutammina adiacenti",
  "Gram+: ponte di pentaglicina tra due NAM; Gram−: legame glicosidico β(1→4) tra NAG di catene vicine",
  "Gram+ e Gram− hanno lo stesso ponte di pentaglicina, ma nei Gram− il peptidoglicano è molto più spesso",
  ], 0,
  "Nei Gram− il peptidoglicano è sottile e sta nello spazio periplasmatico, tra membrana interna ed esterna.")
q("u1119-093", T, "l", "196", "Che cos'è il DAP che può sostituire la lisina nel peptidoglicano dei Gram-negativi?", [
  "L'acido diamminopimelico: come la lisina, con un carbonio in più che porta un'ammina e un carbossile",
  "Il diamminopropano: una lisina accorciata di due carboni che ha perso anche il gruppo carbossilico",
  "Il diidrossiacetone fosfato: un trioso che lega la D-alanina con un legame estere",
  "La diamminopurina: una base azotata che fa da ponte tra due catene di NAM",
  "L'acido diaminopropionico: una D-alanina con un secondo gruppo amminico sul carbonio β",
  ], 0,
  "Ha due gruppi amminici e due carbossilici.")
q("u1119-094", T, "h", "196", "I batteri convertono la L-alanina in D-alanina con una racemasi, possibile bersaglio di antibiotici. Quale coenzima ti aspetti in questo enzima?", [
  "Piridossal fosfato (vitamina B6)",
  "Tiamina pirofosfato (vitamina B1)",
  "Biotina (vitamina B7)",
  "FAD (vitamina B2)",
  "Tetraidrofolato (vitamina B9)",
  ], 0,
  "Il PLP forma una base di Schiff con l'amminoacido e permette di togliere e rimettere il protone sul carbonio α, invertendone la configurazione. Noi non abbiamo D-amminoacidi nelle proteine, quindi l'enzima è un bersaglio selettivo.")
q("u1119-095", T, "a", "197", "Perché la penicillina blocca la formazione della parete batterica?", [
  "Somiglia al dipeptide D-Ala-D-Ala e inattiva in modo irreversibile la transpeptidasi dei legami crociati",
  "Somiglia al NAM e inibisce in modo reversibile l'enzima che lega gli zuccheri della catena glicanica",
  "Inibisce la racemasi batterica, che non produce più la D-alanina necessaria al tetrapeptide della parete",
  "Idrolizza i legami glicosidici tra NAG e NAM come il lisozima, sciogliendo la parete già formata",
  "Lega il ponte di pentaglicina e impedisce che si stacchi dalla lisina del tetrapeptide vicino",
  ], 0,
  "La transpeptidasi stacca la D-Ala terminale (all'inizio le D-Ala sono due) e lega la glicina del ponte: è il passaggio bloccato.")

# ── Glicoproteine (p. 192–195) ─────────────────────────────────────────────
T = "d9-glicoproteine"
q("u1119-096", T, "f", "192", "Su quali residui avvengono la N-glicosilazione e la O-glicosilazione?", [
  "N: asparagina; O: serina o treonina",
  "N: glutammina; O: serina o tirosina",
  "N: lisina; O: serina o treonina",
  "N: asparagina; O: tirosina o cisteina",
  "N: arginina; O: treonina o idrossiprolina",
  ], 0,
  "N-glicosidico sull'azoto ammidico dell'Asn; O-glicosidico sull'ossidrile di Ser o Thr.")
q("u1119-097", T, "m", "192", "Dove si trovano gli enzimi delle N- e delle O-glicosilazioni?", [
  "N-glicosilazioni nel RE e nel Golgi; O-glicosilazioni solo nel Golgi",
  "N-glicosilazioni solo nel Golgi; O-glicosilazioni nel RE e nel Golgi",
  "Entrambe solo nel citosol, durante la traduzione sui ribosomi liberi",
  "N-glicosilazioni nei lisosomi; O-glicosilazioni nel reticolo liscio",
  "Entrambe solo nel RE rugoso, prima dell'arrivo della proteina al Golgi",
  ], 0,
  "Sono modifiche post-traduzionali; il Golgi poi smista le proteine in base all'informazione dei carboidrati.")
q("u1119-098", T, "a", "194", "Come viene aggiunto l'oligosaccaride nella N-glicosilazione?", [
  "Si costruisce sul dolicolo fosfato, che passa dal lato citosolico al lume del RE, poi è trasferito in blocco a un'Asn",
  "Si aggiunge uno zucchero alla volta direttamente sull'asparagina, nel citosol, mentre la proteina viene tradotta dal ribosoma",
  "Si costruisce su un fosfolipide del Golgi e viene trasferito in blocco a una serina della proteina",
  "Si costruisce sull'UDP-glucosio nel lume del RE e viene trasferito a una lisina della proteina",
  "Si costruisce sul dolicolo fosfato nel lume del lisosoma e viene trasferito a una treonina",
  ], 0,
  "Al dolicolo fosfato si aggiungono NAG e mannosio sul lato citosolico; con il flip-flop si affaccia nel lume, dove si aggiungono altri mannosi ed eventualmente glucosi.")
q("u1119-099", T, "l", "194", "Quanti residui ha l'oligosaccaride che il dolicolo trasferisce in blocco sull'asparagina?", [
  "14",
  "9",
  "12",
  "7",
  "20",
  ], 0,
  "Glc₃Man₉GlcNAc₂ (la composizione non è nelle sbobine, Lehninger).")
q("u1119-100", T, "m", "193", "Quale segnale indirizza le idrolasi acide verso i lisosomi?", [
  "Residui di mannosio 6-fosfato",
  "Residui di acido sialico terminali",
  "Residui di glucosio 6-fosfato",
  "Una sequenza KDEL al C-terminale",
  "Una catena di ubiquitine sulla lisina 48",
  ], 0,
  "Il Golgi fosforila il mannosio in due tappe: fosfotransferasi, poi fosfodiesterasi che stacca la N-acetilglucosammina.")
q("u1119-101", T, "l", "193", "Quale molecola fornisce la N-acetilglucosammina fosfato nella prima tappa della marcatura del mannosio?", [
  "UDP-N-acetilglucosammina",
  "CMP-acido sialico",
  "GDP-mannosio",
  "Dolicolo fosfato",
  "UDP-N-acetilgalattosammina",
  ], 0,
  "La fosfotransferasi rilascia UMP e lega la GlcNAc-fosfato al mannosio; poi la fosfodiesterasi stacca la GlcNAc e lascia il mannosio 6-fosfato.")
q("u1119-102", T, "h", "193", "Nella mucolipidosi di tipo II (I-cell disease) i lisosomi sono pieni di materiale non degradato e le idrolasi acide si trovano nel sangue. Qual è il difetto?", [
  "Manca la fosfotransferasi della prima tappa: senza mannosio 6-fosfato le idrolasi vengono secrete",
  "Manca il recettore del mannosio 6-fosfato sulla membrana plasmatica, che di solito le recupera",
  "Manca il dolicolo fosfato: le idrolasi non sono glicosilate e il Golgi non le riconosce più",
  "La pompa protonica dei lisosomi è difettosa e le idrolasi escono dai lisosomi verso il sangue",
  "Le idrolasi hanno troppo acido sialico e il fegato non le cattura più dal circolo sanguigno",
  ], 0,
  "Si accumulano glicosamminoglicani e glicolipidi non degradati, perché gli enzimi non arrivano a destinazione.")
q("u1119-103", T, "a", "194", "Come controlla l'acido sialico la vita media delle glicoproteine plasmatiche?", [
  "Finché è presente, il recettore epatico non lega la proteina; quando viene rimosso, la proteina viene catturata ed eliminata",
  "Finché è presente, il recettore epatico lega e protegge la proteina; quando viene rimosso, la proteina resta libera nel plasma",
  "Viene aggiunto progressivamente in circolo: più acido sialico porta la proteina, prima viene degradata nel lisosoma",
  "Lega gli ioni calcio del plasma: quando li perde, la proteina precipita e viene filtrata dal rene",
  "Marca le proteine con un segnale di ubiquitinazione che il proteasoma del plasma riconosce dopo la sua rimozione",
  ], 0,
  "Gli enzimi sulla parete dei vasi rimuovono l'acido sialico, che sta all'estremità delle ramificazioni; l'asialoglicoproteina espone gli zuccheri sottostanti riconosciuti dai recettori del fegato.")
q("u1119-104", T, "f", "195", "In quale di queste interazioni gli oligosaccaridi di superficie NON sono indicati come mediatori?", [
  "Legame dell'ossigeno all'emoglobina",
  "Adesione dei batteri all'epitelio",
  "Riconoscimento della cellula ospite da parte dei virus",
  "Migrazione dei linfociti nei tessuti",
  "Riconoscimento delle proteine circolanti da parte del fegato",
  ], 0,
  "Batterio-epitelio, virus-ospite, linfocita-tessuto; e, con l'acido sialico, la rimozione delle glicoproteine plasmatiche.")
