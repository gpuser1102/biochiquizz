"""Domande HARD (livello h), modulo 3: ciclo di Krebs e fosforilazione ossidativa (pp. 74–114)."""
from bank_common import q

T = "m3-krebs"
q("h3k-01", T, "h", "79–80", "La citrato sintasi lega prima l'ossalacetato e poi l'acetil-CoA (meccanismo sequenziale ordinato). Perché è vantaggioso?", [
  "Si evita l'idrolisi improduttiva dell'acetil-CoA quando manca l'ossalacetato",
  "L'acetil-CoA è un inibitore dell'enzima e deve legarsi solo per ultimo",
  "L'ossalacetato è molto più abbondante dell'acetil-CoA nella matrice mitocondriale",
  'Così la reazione diventa reversibile e segue le concentrazioni dei substrati',
  "L'enzima deve prima legare l'ATP, che si trova nello stesso sito dell'ossalacetato",
  ], 0,
  "L'ossalacetato è scarso e instabile; il tioestere dell'acetil-CoA è ciò che spinge la reazione. Anche la chiusura del sito attivo (adattamento indotto) tiene fuori l'acqua finché non si forma il citril-CoA.")
q("h3k-02", T, "h", "84", "Un acetil-CoA marcato su entrambi i carboni entra nel ciclo. Al primo giro, quanta marcatura si ritrova nella CO₂ liberata?", [
  "Nessuna: al primo giro escono carboni dell'ossalacetato",
  'Tutta: entrambi i carboni marcati escono come CO₂',
  "Metà: un carbonio marcato esce all'isocitrato deidrogenasi",
  'Metà: un carbonio marcato esce alla succinato deidrogenasi',
  "Tutta: i due carboni escono all'α-chetoglutarato deidrogenasi",
  ], 0,
  "I carboni dell'acetile escono solo nei giri successivi. Il ciclo ossida l'equivalente di un acetile per giro, ma non gli stessi atomi.")
q("h3k-03", T, "h", "80–81", "Un paziente ha una grave carenza di ferro. Oltre all'anemia, quale enzima del ciclo di Krebs rischia di funzionare meno?", [
  "L'aconitasi, che ha un centro ferro-zolfo",
  'La citrato sintasi, che contiene un gruppo eme',
  'La fumarasi, che usa il rame come cofattore',
  'La malato deidrogenasi, che contiene zinco',
  "L'isocitrato deidrogenasi, che usa il ferro come coenzima",
  ], 0,
  "Se l'aconitasi (4Fe-4S) perde un ferro si inattiva e si accumula citrato. Senza ferro, l'aconitasi citosolica regola l'mRNA di recettore della transferrina e ferritina: è un sensore del ferro («moonlighting protein»).")
q("h3k-04", T, "h", "81", "Perché la reazione dell'isocitrato deidrogenasi è molto esoergonica mentre altre deidrogenazioni non lo sono?", [
  'È anche una decarbossilazione: la CO₂ liberata rende il ΔG molto negativo',
  'Consuma una molecola di ATP che spinge la deidrogenazione',
  'Usa il FAD, che ha un potenziale più positivo del NAD⁺',
  'Rompe un legame tioestere ad alta energia del substrato',
  "Avviene nel citosol, dove il rapporto NAD⁺/NADH è molto alto e favorisce l'ossidazione",
  ], 0,
  'È una decarbossilazione ossidativa, irreversibile: è uno dei principali punti di regolazione del ciclo.')
q("h3k-05", T, "h", "82", "Che cosa hanno in comune e in che cosa differiscono il complesso della PDH e quello dell'α-chetoglutarato deidrogenasi?", [
  'Stessi coenzimi ed E3 identico; diversi E1 ed E2; niente regolazione covalente',
  'Sono identici in tutte le subunità e differiscono solo per il substrato',
  "L'α-chetoglutarato deidrogenasi non usa la tiamina pirofosfato",
  "Entrambi sono regolati dalla stessa chinasi e dalla stessa fosfatasi, come risposta all'insulina",
  "La PDH produce GTP, mentre l'α-chetoglutarato deidrogenasi produce NADH",
  ], 0,
  "Coenzimi: TPP, lipoato, CoA, FAD, NAD⁺. L'α-KGDH non è regolata per fosforilazione ma è inibita dai suoi prodotti (succinil-CoA, NADH).")
q("h3k-06", T, "h", "82", "Nella reazione della succinil-CoA sintetasi, quale sequenza di intermedi porta al GTP?", [
  "Succinil-fosfato, poi istidina fosforilata dell'enzima, poi GDP",
  'Succinato e CO₂, poi il fosfato inorganico passa direttamente al GDP',
  'Il CoA cede il fosfato al GDP senza intermedi enzimatici',
  'Il GTP fosforila il succinato per formare succinil-CoA',
  'Il FADH₂ della succinato deidrogenasi fosforila il GDP',
  ], 0,
  "Succinil-CoA + Pi → succinil-fosfato (+ CoA) → fosfato su un'istidina → GTP. È l'unica fosforilazione a livello del substrato del ciclo.",
  note="Sbobina di Biochimica II, p. 78: l'enzima è chiamato «succinil-CoA sintasi». Il nome corretto è succinil-CoA sintetasi (lo usa la stessa sbobina a p. 82): per la convenzione della sbobina, «sintetasi» indica gli enzimi che usano un nucleoside trifosfato, come qui nella reazione inversa.")
q("h3k-07", T, "h", "84–85", "Durante l'esercizio, il ciclo di Krebs muscolare accelera. Quali segnali sono responsabili?", [
  'ADP e Ca²⁺ alti e NADH/NAD⁺ basso',
  'ATP e NADH alti nella matrice',
  'Accumulo di succinil-CoA',
  'Accumulo di citrato nella matrice',
  'Insulina che defosforila la citrato sintasi',
  ], 0,
  "Attivano isocitrato deidrogenasi e α-chetoglutarato deidrogenasi. È la «regolazione da parte dell'accettore»: l'ADP segnala bisogno di ATP.")
q("h3k-08", T, "h", "87–89", "Un soggetto mangia molti grassi ma pochissimi carboidrati. Perché l'ossidazione degli acidi grassi può essere limitata?", [
  "L'ossalacetato viene soprattutto dal piruvato, quindi dal glucosio",
  'Gli acidi grassi inibiscono la citrato sintasi e bloccano il ciclo',
  'Senza glucosio il mitocondrio non può rigenerare il NAD⁺ ossidato',
  'La β-ossidazione funziona solo in presenza di insulina',
  "L'acetil-CoA in eccesso viene trasformato in glucosio dal fegato",
  ], 0,
  "L'acetil-CoA entra nel ciclo solo condensandosi con l'ossalacetato. La piruvato carbossilasi (biotina) è la principale reazione anaplerotica ed è attivata dall'acetil-CoA.")

T = "m3-catena"
q("h3c-01", T, "h", "90–91", "Ossidando completamente una molecola di glucosio, quanti elettroni vengono ceduti e quanti coenzimi ridotti si formano?", [
  '24 elettroni, in 10 NADH e 2 FADH₂',
  '12 elettroni, in 6 NADH',
  '24 elettroni, in 12 NADH',
  '36 elettroni, in 18 coenzimi',
  '24 elettroni, in 8 NADH e 4 FADH₂',
  ], 0,
  'Ogni coenzima accetta 2 elettroni: 12 coenzimi ridotti.')
q("h3c-02", T, "h", "92–93", "Perché nella catena respiratoria il flusso di elettroni va dal NADH all'O₂ e non al contrario?", [
  "I trasportatori hanno potenziali di riduzione crescenti fino all'O₂",
  "L'O₂ è più ridotto del NADH e attira i suoi protoni lungo la membrana interna",
  "L'ATP sintasi tira gli elettroni verso il complesso IV",
  'Ogni complesso consuma ATP per spingere gli elettroni',
  "Il NADH ha un potenziale più positivo dell'O₂",
  ], 0,
  "Da −0,32 V (NAD⁺/NADH) a +0,82 V (O₂/H₂O): ogni passaggio ha ΔE positivo e quindi ΔG negativo (ΔG°' = −nFΔE°').")
q("h3c-03", T, "h", "99", "Calcola il ΔG°' dell'ossidazione del NADH da parte dell'O₂ (E°' NAD⁺/NADH = −0,32 V; O₂/H₂O = +0,82 V; n = 2; F ≈ 96,5 kJ/V·mol).", [
  'Circa −220 kJ/mol',
  'Circa −96 kJ/mol',
  'Circa +220 kJ/mol',
  'Circa −30 kJ/mol',
  'Circa −490 kJ/mol',
  ], 0,
  "ΔE°' = 0,82 − (−0,32) = 1,14 V; ΔG°' = −2 × 96,5 × 1,14 ≈ −220 kJ/mol.",
  note="Sbobina di Biochimica II, p. 99: la formula è scritta «nF[(0,81 − (0,32)]», senza il segno meno del NAD e senza il meno davanti. Corretto: ΔG°' = −nF[0,81 − (−0,32)].")
q("h3c-04", T, "h", "104", "In mitocondri isolati si aggiunge antimicina A (inibitore del complesso III). In che stato saranno coenzima Q e citocromo c?", [
  'Q ridotto, citocromo c ossidato',
  'Entrambi ridotti',
  'Entrambi ossidati',
  'Q ossidato, citocromo c ridotto',
  'Invariati, perché il complesso II bypassa il III',
  ], 0,
  'I trasportatori a monte del blocco restano ridotti, quelli a valle ossidati.')
q("h3c-05", T, "h", "94–95", "Il succinato rende circa 1,5 ATP e il NADH circa 2,5. Perché?", [
  'Entrano dal complesso II, che non pompa protoni, e saltano il complesso I',
  "Il succinato cede gli elettroni direttamente all'O₂ senza passare dalla catena",
  'Il FADH₂ porta un solo elettrone invece dei due del NADH',
  "Il complesso II consuma una parte dell'ATP per trasferire gli elettroni",
  'Il FADH₂ cede gli elettroni direttamente al complesso III',
  ], 0,
  'Gli elettroni arrivano direttamente al coenzima Q. Il ΔE tra fumarato/succinato e Q è troppo piccolo per pompare protoni.')
q("h3c-06", T, "h", "95", "Quale caratteristica rende il coenzima Q adatto a raccogliere elettroni da più fonti (complesso I, II, glicerolo 3-P deidrogenasi, β-ossidazione)?", [
  'È piccolo e liposolubile, mobile nella membrana, e accetta 1 o 2 elettroni',
  'È una proteina solubile dello spazio intermembrana che lega un eme di tipo c',
  'Contiene un eme che accetta un solo elettrone alla volta',
  'È legato covalentemente al complesso III e ruota con esso',
  'Accetta elettroni solo dal NADH tramite il FMN del complesso I',
  ], 0,
  'La coda isoprenica lo tiene nella membrana interna. Il citocromo c invece è una proteina solubile dello spazio intermembrana.')
q("h3c-07", T, "h", "96–97", "A che cosa serve il ciclo Q nel complesso III?", [
  'A passare un elettrone alla volta al citocromo c pompando più protoni',
  "A ridurre direttamente l'O₂ ad acqua nel complesso III",
  'A trasferire gli elettroni dal NADH al FMN del complesso I',
  "A sintetizzare ATP accoppiando il trasporto di elettroni alla rotazione dell'anello c",
  "A portare il NADH citosolico all'interno della matrice",
  ], 0,
  "Il QH₂ cede 2 elettroni ma il citocromo c ne accetta uno: uno va a c₁ e c, l'altro tramite bL e bH riduce un altro Q. Il risultato netto è l'ossidazione di QH₂.")
q("h3c-08", T, "h", "98–99", "Nel complesso IV, quale affermazione sui protoni è corretta per ogni O₂ ridotto?", [
  '8 H⁺ prelevati dalla matrice: 4 formano H₂O, 4 sono pompati',
  '8 H⁺ pompati tutti nello spazio intermembrana',
  'Nessun protone pompato: il complesso IV forma solo acqua',
  "2 H⁺ pompati e 2 usati per formare una molecola d'acqua",
  "4 H⁺ prelevati dallo spazio intermembrana per formare l'acqua",
  ], 0,
  'Entrambi i processi contribuiscono al gradiente: anche i protoni «chimici» sono sottratti alla matrice.',
  note="Sbobina di Biochimica II, p. 99: c'è scritto «8 protoni in totale vengono pompati». Gli 8 H⁺ sono prelevati dalla matrice, ma ne vengono pompati solo 4; gli altri 4 si combinano con l'O₂.")

T = "m3-atpsintasi"
q("h3s-01", T, "h", "100", "Quali due componenti formano la forza motrice protonica?", [
  'Un gradiente elettrico e un gradiente di pH',
  'Un gradiente di ATP e uno di ADP',
  'Un gradiente di Na⁺ e uno di K⁺',
  'Solo un gradiente di pH tra i due lati',
  'Un gradiente di O₂ tra matrice e citosol',
  ], 0,
  "Lato P positivo e più acido, matrice negativa e più basica. È il nucleo dell'ipotesi chemiosmotica di Mitchell.",
  note="Sbobina di Biochimica II, p. 100: l'ipotesi alternativa degli intermedi ad alta energia è attribuita a Koshland. Nei testi è l'ipotesi chimica (Slater); l'ipotesi chemiosmotica di Mitchell è del 1961 (Nobel 1978).")
q("h3s-02", T, "h", "101–102", "Nella F₀, che cosa ruota e che cosa resta fermo?", [
  "Ruotano l'anello c, γ ed ε; restano fermi a, b₂, δ e α₃β₃",
  "Ruota la subunità a; restano fermi l'anello c, lo statore e l'esamero α₃β₃",
  "Ruota l'esamero α₃β₃; l'anello c resta fermo",
  "Ruota tutta l'ATP sintasi insieme alla membrana",
  "Non ruota nulla: c'è solo un cambio di conformazione",
  ], 0,
  "I protoni entrano dal semicanale di a, protonano l'Asp di una subunità c e l'anello ruota; lo statore (b₂, δ) blocca α₃β₃.",
  note="Sbobina di Biochimica II, p. 101: c'è scritto che «la proteina a è un rotore che gira». La subunità a è ferma (fa parte dello statore); a ruotare è l'anello delle subunità c, come la stessa sbobina descrive a p. 102.")
q("h3s-03", T, "h", "102–103", "Secondo il meccanismo di Boyer (cambio di legame), quale passaggio richiede la maggior parte dell'energia del gradiente?", [
  "Il rilascio dell'ATP dalla subunità β in conformazione T",
  'La formazione del legame fosfoanidridico nel sito T',
  'Il legame di ADP e Pi alla subunità in conformazione L',
  "La rotazione della subunità a attorno all'anello c",
  "L'ingresso del fosfato nella matrice con il simporto",
  ], 0,
  "Nel sito T l'ATP si forma con ΔG ≈ 0; è il distacco (T → O) a costare energia.",
  note="Sbobina di Biochimica II, p. 102: la conformazione L è chiamata «light». Nei testi è «loose» (allentata).")
q("h3s-04", T, "h", "105", "In mitocondri isolati con succinato si aggiunge oligomicina e poi 2,4-dinitrofenolo. Che cosa succede al consumo di O₂?", [
  "Si ferma con l'oligomicina e riparte con il DNP, senza ATP",
  "Aumenta con l'oligomicina e si ferma con il DNP",
  'Resta costante in entrambi i casi',
  "Si ferma con l'oligomicina e resta fermo anche dopo l'aggiunta del DNP",
  'Aumenta in entrambi i casi, con produzione di ATP',
  ], 0,
  "Con l'oligomicina il gradiente non viene scaricato e il trasporto di elettroni rallenta; il DNP scarica il gradiente. È la prova dell'accoppiamento.")
q("h3s-05", T, "h", "105–106", "Perché il 2,4-dinitrofenolo, usato in passato come dimagrante, provoca ipertermia potenzialmente letale?", [
  "Riporta i protoni nella matrice scavalcando l'ATP sintasi: l'energia diventa calore",
  "Blocca il complesso IV e l'energia degli elettroni rimasti nella catena si libera come calore",
  'Inibisce la glicolisi e costringe la cellula a bruciare solo grassi',
  "Aumenta la sintesi di ATP e l'eccesso di ATP produce calore",
  'Attiva la termogenina in tutti i tessuti, non solo nel grasso bruno',
  ], 0,
  'È un acido debole liposolubile (disaccoppiante): la cellula ossida più nutrienti per compensare. Il dosaggio era difficile da controllare.',
  note="Sbobina di Biochimica II, p. 105: c'è scritto che il DNP «passa la membrana plasmatica» rilasciando il H⁺; si intende la membrana mitocondriale interna.")
q("h3s-06", T, "h", "106–107", "Nel neonato, come produce calore il tessuto adiposo bruno?", [
  'La termogenina fa rientrare i protoni senza produrre ATP',
  'Idrolizza ATP con le pompe ioniche della membrana',
  'Fermenta il glucosio a lattato producendo calore',
  'Blocca il complesso IV e accumula elettroni che producono calore',
  "Aumenta la sintesi di ATP con l'ATP sintasi",
  ], 0,
  "La termogenina (UCP1) è nella membrana interna: la catena lavora senza sintesi di ATP e l'energia si libera come calore. È un disaccoppiamento fisiologico.",
  note="Sbobina di Biochimica II, p. 106: il tessuto adiposo bruno serve per riscaldare «il feto». Il riscaldamento serve al neonato, dopo la nascita (il feto è riscaldato dalla madre). La termogenina è UCP1, non «UP1».")
q("h3s-07", T, "h", "104", "Lo scambio ATP⁴⁻ (fuori) / ADP³⁻ (dentro) della ATP/ADP traslocasi è elettrogenico. Da dove prende l'energia?", [
  "Dal potenziale di membrana, che favorisce l'uscita dell'ATP⁴⁻",
  "Dall'idrolisi di una molecola di ATP per ogni scambio",
  'Dal gradiente di Na⁺ mantenuto dalla pompa Na⁺/K⁺ della membrana plasmatica',
  'Da nessuna fonte: lo scambio è elettricamente neutro',
  'Dal GTP prodotto nel ciclo di Krebs',
  ], 0,
  'Esce una carica negativa in più verso il lato P, positivo; il Pi entra con un H⁺. Parte della forza motrice protonica serve quindi al trasporto.')
q("h3s-08", T, "h", "101–104", "Qual è il costo in protoni per ogni ATP che arriva nel citosol, e come si ricavano i valori 2,5 e 1,5?", [
  'Circa 4 H⁺ per ATP: NADH 10 H⁺ (2,5), FADH₂ 6 H⁺ (1,5)',
  '3 H⁺ per ATP, senza costo di trasporto: NADH 3,3 e FADH₂ 2 ATP',
  '8 H⁺ per ATP: NADH 1,25 ATP, FADH₂ 0,75',
  '2 H⁺ per ATP: NADH 5 ATP, FADH₂ 3 ATP',
  "Nessun protone: l'ATP si forma dal NADH",
  ], 0,
  '3 H⁺ per la sintesi + 1 per il trasporto. Non è nelle sbobine nel dettaglio: con 8 subunità c servono 8 H⁺ per 3 ATP.')

T = "m3-radicali"
q("h3r-01", T, "h", "108–109", "Quale sequenza di enzimi elimina il superossido fino ad acqua?", [
  'SOD (→ H₂O₂ + O₂), poi catalasi o glutatione perossidasi',
  'Catalasi (→ H₂O₂ + O₂), poi superossido dismutasi (→ H₂O)',
  'Glutatione reduttasi, poi superossido dismutasi',
  'Citocromo c ossidasi, poi catalasi',
  'SOD da sola, che produce direttamente acqua',
  ], 0,
  'La SOD produce H₂O₂, che va eliminato da catalasi o glutatione perossidasi.')
q("h3r-02", T, "h", "109", "Un soggetto con deficit di glucosio 6-fosfato deidrogenasi assume un farmaco ossidante. Perché i suoi eritrociti vanno in emolisi?", [
  'Senza NADPH il glutatione non si rigenera e i perossidi ossidano la cellula',
  "Senza G6PD l'eritrocita non produce ATP e la pompa Na⁺/K⁺ si ferma del tutto",
  'Senza G6PD la superossido dismutasi non viene sintetizzata',
  'Senza G6PD si accumula lattato che lisa la membrana',
  "Senza G6PD aumenta il 2,3-BPG e l'emoglobina precipita",
  ], 0,
  "La glutatione reduttasi usa NADPH; senza GSH la glutatione perossidasi non elimina i perossidi. L'eritrocita ha solo la via dei pentoso fosfati come fonte di NADPH.")
q("h3r-03", T, "h", "109", "Perché la glutatione perossidasi contiene selenocisteina e non cisteina?", [
  'Il selenolato è più reattivo verso i perossidi del tiolato',
  "Il selenio lega l'ossigeno come il ferro dell'eme",
  'Il selenio è un donatore di NADPH per la reazione',
  'La selenocisteina forma ponti diselenuro più stabili dei ponti disolfuro',
  'Il selenio è un metallo di transizione redox',
  ], 0,
  'Il selenolo è più acido (Se⁻ a pH fisiologico); viene riportato a Se⁻ da due molecole di GSH. Il selenio va assunto con la dieta, ma in eccesso è tossico.')
q("h3r-04", T, "h", "109", "Quale associazione tra superossido dismutasi e metallo è corretta?", [
  'Citosolica Cu/Zn; mitocondriale Mn',
  'Citosolica Fe; mitocondriale Se',
  'Citosolica Mn; mitocondriale Cu/Zn',
  'Tutte le SOD contengono un eme',
  'Citosolica Zn; mitocondriale Mg',
  ], 0,
  'Mutazioni della SOD1 (Cu/Zn) sono associate ad alcune forme di SLA.')
q("h3r-05", T, "h", "110", "In quale condizione la catena respiratoria produce più superossido?", [
  "Con poco O₂ o catena molto ridotta: un elettrone passa all'O₂",
  'Con O₂ abbondante e catena completamente ossidata',
  "Quando l'ATP sintasi lavora alla massima velocità e scarica il gradiente",
  "Quando nella matrice c'è molto ADP disponibile",
  'Solo quando il complesso IV è iperattivo',
  ], 0,
  "Gli elettroni restano su trasportatori come il semichinone e vengono ceduti a un O₂ uno alla volta: la riduzione monoelettronica dell'O₂ dà superossido.")
q("h3r-06", T, "h", "110–111", "Come riduce l'HIF la produzione di radicali nella cellula ipossica?", [
  'Sposta verso glicolisi e lattato e sostituisce COX4-1 con COX4-2',
  'Aumenta la β-ossidazione e il flusso di elettroni nella catena',
  'Attiva la PDH e riduce la produzione di lattato',
  'Inibisce la glicolisi per ridurre il consumo di glucosio',
  'Aumenta la sintesi di ubichinone e di citocromo c',
  ], 0,
  "Più enzimi glicolitici, LDH e PDH chinasi; COX4-2 è più affine all'O₂. Meno flusso di elettroni nel mitocondrio, meno superossido.")
q("h3r-07", T, "h", "110", "Secondo lo studio del 2017 citato a lezione, che effetto hanno gli antiossidanti sui tumori già formati?", [
  'Potrebbero favorire le metastasi',
  'Fanno sempre regredire il tumore',
  'Non hanno alcun effetto misurabile',
  'Aumentano lo stress ossidativo nel tumore',
  'Bloccano le metastasi ma non il tumore primario',
  ], 0,
  'Aiuterebbero le cellule tumorali a sopportare lo stress ossidativo che normalmente le limita. Il prof sottolinea che il risultato è discusso e non confermato.')
q("h3r-08", T, "h", "108", "Quali vitamine sono considerate antiossidanti classiche?", [
  'C, E e A/β-carotene',
  'B1, B2 e B6',
  'K e D',
  'B12 e folato',
  'C, E e K (la K protegge le membrane)',
  ], 0,
  'La vitamina E protegge le membrane, la C agisce in ambiente acquoso.',
  note="Sbobina di Biochimica II, p. 108: tra le antiossidanti è inclusa anche la vitamina K. La K serve alla carbossilazione dei fattori della coagulazione, non è un antiossidante classico.")

T = "m3-malattie"
q("h3m-01", T, "h", "112", "Una donna con una malattia del DNA mitocondriale (omoplasmia) ha un figlio maschio e una figlia. Che cosa ti aspetti?", [
  'Entrambi la ereditano; solo la figlia la trasmette',
  'Solo la figlia è a rischio, con probabilità del 50%',
  'Solo il figlio maschio è a rischio',
  'Nessuno dei due, perché il mtDNA si ricombina',
  'Entrambi hanno il 25% di probabilità',
  ], 0,
  "Lo zigote riceve i mitocondri solo dall'ovocita.",
  note="Sbobina di Biochimica II, p. 112: c'è scritto che «le figlie hanno il 50% di probabilità, mentre i figli non sono a rischio». È sbagliato: tutti i figli di una madre omoplasmica ereditano il mtDNA mutato, maschi e femmine; i maschi però non lo trasmettono.")
q("h3m-02", T, "h", "112", "Perché due fratelli con la stessa mutazione del mtDNA possono avere quadri clinici molto diversi?", [
  "Per l'eteroplasmia: la quota di mitocondri mutati varia",
  'Perché uno dei due ha ereditato il mtDNA del padre',
  'Perché la mutazione mitocondriale è recessiva',
  'Perché il loro mtDNA ha istoni diversi',
  'Perché le malattie mitocondriali colpiscono solo i maschi',
  ], 0,
  'La proporzione di mtDNA mutato varia tra individui e tessuti, e i sintomi compaiono sopra una soglia. Omoplasmia: tutti i mitocondri mutati.')
q("h3m-03", T, "h", "111", "Il mtDNA codifica 13 proteine. A quale funzione appartengono?", [
  'Subunità dei complessi della fosforilazione ossidativa',
  'Enzimi del ciclo di Krebs e della piruvato deidrogenasi',
  'Enzimi della β-ossidazione',
  'Proteine della membrana esterna',
  'DNA polimerasi mitocondriali',
  ], 0,
  'Es. le subunità maggiori del complesso IV. Il resto delle proteine mitocondriali è codificato dal DNA nucleare; il mtDNA codifica anche rRNA e tRNA.')
q("h3m-04", T, "h", "112–113", "Secondo l'ipotesi presentata a lezione, come può lo stress ossidativo ridurre la secrezione di insulina nel diabete tipo 2?", [
  'Il superossido induce UCP2: meno ATP e meno secrezione di insulina',
  "Il superossido degrada direttamente l'insulina nel sangue",
  "Lo stress ossidativo aumenta l'ATP e blocca l'esocitosi",
  "UCP2 aumenta la sintesi di ATP, che inibisce i canali del Ca²⁺ e l'esocitosi",
  'I radicali bloccano il GLUT4 delle cellule β',
  ], 0,
  'Con meno ATP i canali K⁺ restano aperti e la cellula β non risponde al glucosio. Insulino-resistenza + disfunzione β = diabete tipo 2.')
q("h3m-05", T, "h", "113", "Perché il mtDNA è considerato più vulnerabile del DNA nucleare ai radicali liberi?", [
  'È vicino alla catena respiratoria, senza istoni e con riparazione meno efficiente',
  'È un DNA lineare a singolo filamento, quindi più esposto alle esonucleasi della matrice',
  'Si trova nel citosol, dove la concentrazione di radicali è più alta',
  'È a singolo filamento e non ha un filamento stampo',
  'Non viene mai replicato, quindi accumula danni',
  ], 0,
  "La catena respiratoria è la sede principale della produzione di superossido. Su questo si basa una delle ipotesi mitocondriali dell'invecchiamento.",
  note="Sbobina di Biochimica II, p. 113: c'è scritto che il DNA mitocondriale «non può ripararsi». I mitocondri hanno sistemi di riparazione (es. riparazione per escissione di basi), solo meno completi di quelli nucleari.")
q("h3m-06", T, "h", "112", "In una cellula β con una mutazione mitocondriale che riduce la produzione di ATP, che cosa succede ai canali del potassio e alla secrezione di insulina?", [
  "I canali K-ATP restano aperti e l'insulina non viene secreta",
  'I canali K-ATP si chiudono e la secrezione di insulina aumenta',
  'Si aprono direttamente i canali del Ca²⁺',
  "La cellula β secerne glucagone al posto dell'insulina",
  'Non cambia nulla, perché la glicolisi compensa',
  ], 0,
  'Con poco ATP la membrana non si depolarizza e il Ca²⁺ non entra. Esiste un diabete mitocondriale a trasmissione materna (es. m.3243A>G).')
q("h3m-07", T, "h", "113–114", "Quale ipotesi sull'invecchiamento viene presentata come più razionale a lezione?", [
  "Il danno progressivo al mtDNA riduce l'efficienza della catena",
  "L'accorciamento progressivo dei telomeri presenti sul DNA mitocondriale",
  'La perdita progressiva del DNA nucleare',
  "L'aumento della sintesi di ATP con l'età",
  "La riduzione dei radicali liberi con l'età",
  ], 0,
  'Il danno (o un difetto della divisione mitocondriale) è favorito da radicali e infiammazione. Tutte le ipotesi concordano sul ruolo centrale del mitocondrio.')
q("h3m-08", T, "h", "111", "Quali tessuti sono più colpiti nelle malattie mitocondriali e perché?", [
  'Sistema nervoso, muscolo e cuore',
  'Pelle, capelli e mucose a rapido ricambio',
  'Eritrociti',
  'Tessuto adiposo bianco',
  'Tutti allo stesso modo',
  ], 0,
  "Dipendono molto dalla fosforilazione ossidativa. L'eritrocita maturo non ha mitocondri.")
