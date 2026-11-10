"""Domande HARD (livello h), modulo 1: ripasso di propedeutica e Biochimica I (pp. 5–30).
Ragionate, in stile esame, 5 opzioni. Sono le sole domande della Hard mode."""
from bank_common import q

T = "m1-catabolismo"
q("h1c-01", T, "h", "6–9", "Un nutriente viene completamente ossidato a CO₂ e H₂O. Quale affermazione sui suoi atomi di carbonio e sugli elettroni ceduti è corretta?", [
  "Gli elettroni passano a NAD⁺/FAD e poi all'O₂; la CO₂ nasce dalle decarbossilazioni",
  "Il carbonio reagisce con l'O₂ nella catena respiratoria e forma direttamente CO₂",
  "Gli elettroni vanno all'O₂ già nella glicolisi, che per questo richiede ossigeno",
  "L'H₂O si forma nel ciclo di Krebs, mentre la CO₂ si forma nel complesso IV",
  'NADH e FADH₂ sono i metaboliti terminali e vengono eliminati con le urine',
  ], 0,
  "L'O₂ è solo l'accettore finale degli elettroni (forma H₂O); la CO₂ nasce dalle decarbossilazioni ossidative (PDH, isocitrato e α-chetoglutarato deidrogenasi).")
q("h1c-02", T, "h", "8–9", "Perché l'acetil-CoA è definito metabolita intermedio e non terminale?", [
  'Perché può essere ossidato nel Krebs oppure usato per biosintesi, secondo lo stato energetico',
  'Perché deriva solo dai carboidrati e non può essere prodotto da altri nutrienti',
  'Perché non può più dare energia e serve soltanto come precursore biosintetico',
  'Perché viene eliminato con la respirazione insieme alla CO₂ del ciclo di Krebs',
  "Perché nell'uomo può essere riconvertito in glucosio quando la glicemia si abbassa a digiuno",
  ], 0,
  "Un metabolita terminale (CO₂, H₂O, urea) non rientra nel metabolismo. L'acetil-CoA è precursore di acidi grassi e colesterolo; nell'uomo non può dare glucosio netto.")
q("h1c-03", T, "h", "6–7", "Una cellula si sta preparando a dividersi. Quale combinazione descrive correttamente il suo fabbisogno metabolico?", [
  'Catabolismo per ATP e NADPH, più precursori per sintetizzare DNA e fosfolipidi',
  'Solo anabolismo, perché durante la mitosi il catabolismo si arresta del tutto',
  'Solo catabolismo, perché la divisione consuma le molecole complesse esistenti',
  'Solo ATP, perché le biosintesi di DNA e membrane non richiedono potere riducente',
  'Potere riducente sotto forma di NAD⁺ ossidato, ceduto dalle vie anaboliche',
  ], 0,
  'Servono basi azotate, acidi grassi, glicerolo e teste polari. Le biosintesi sono riduttive e consumano ATP: catabolismo e anabolismo sono accoppiati.',
  note="Sbobina di Biochimica II, pp. 6–7: il potere riducente per le biosintesi è indicato come «soprattutto NADH». Per le biosintesi riduttive il coenzima è il NADPH (Lehninger).")
q("h1c-04", T, "h", "8", "Perché la glicolisi è considerata un processo ossidativo, pur non consumando ossigeno?", [
  'Perché il glucosio cede elettroni al NAD⁺ nella reazione della GAP deidrogenasi',
  "Perché libera CO₂ nella reazione dell'aldolasi, come le decarbossilazioni ossidative",
  "Perché consuma ATP nella fase preparatoria, cedendo energia all'ambiente",
  'Perché avviene in parte nel mitocondrio, dove si trovano gli enzimi ossidativi',
  'Perché riduce il piruvato a lattato, ossidando in parallelo il NADH a NAD⁺',
  ], 0,
  "Ossidazione significa perdita di elettroni, non reazione con l'O₂. L'ossigeno interviene solo sul destino del NADH e del piruvato.")
q("h1c-05", T, "h", "8", "Da quale processo la cellula ricava la maggior parte dell'ATP ottenuto dall'ossidazione completa del glucosio?", [
  'Dalla fosforilazione ossidativa, che riossida NADH e FADH₂',
  'Dalla glicolisi, grazie alle due fosforilazioni a livello del substrato',
  'Dal ciclo di Krebs, grazie al GTP prodotto dalla succinil-CoA sintetasi',
  "Dalla piruvato deidrogenasi, che forma il legame tioestere dell'acetil-CoA",
  'In parti uguali da glicolisi, ciclo di Krebs e fosforilazione ossidativa',
  ], 0,
  'Glicolisi e Krebs danno poco ATP diretto (2 + 2): il loro prodotto principale sono i coenzimi ridotti, riossidati nella catena respiratoria (circa 28 ATP).')
q("h1c-06", T, "h", "6–8", "Come viene eliminato l'azoto degli amminoacidi e perché non come NH₃ libera?", [
  'Viene organicata e trasformata nel fegato in urea, poi eliminata con le urine',
  'Viene espirata come NH₃ insieme alla CO₂ prodotta dalle decarbossilazioni',
  'Viene ossidata a nitrato dalla catena respiratoria e poi filtrata dal rene',
  'Viene immagazzinata come glutammato nel tessuto adiposo fino al pasto successivo',
  "Viene eliminata come acido urico, il principale prodotto azotato nell'uomo",
  ], 0,
  "L'NH₃ è tossica: viene unita al bicarbonato e trasformata in urea, non tossica. L'acido urico deriva dalle purine, non è la via principale dell'azoto amminoacidico.")
q("h1c-07", T, "h", "7–8", "Le vie cataboliche di carboidrati, lipidi e proteine sono dette convergenti perché:", [
  'Portano a pochi intermedi comuni (piruvato, acetil-CoA) che entrano nel Krebs',
  'Avvengono tutte nel citosol, dove si trovano gli enzimi della glicolisi e della β-ossidazione',
  'Sono catalizzate dagli stessi enzimi, indipendentemente dal nutriente',
  'Producono tutte urea come prodotto finale, che viene eliminata dal rene',
  "Richiedono tutte l'insulina per far entrare il nutriente nella cellula",
  ], 0,
  'Le vie anaboliche invece divergono da pochi precursori verso molte molecole complesse.')
q("h1c-08", T, "h", "6", "Perché vitamine e sali minerali sono indispensabili anche se non forniscono energia?", [
  'Perché da molte vitamine derivano i coenzimi delle reazioni del catabolismo',
  'Perché vengono ossidati nel ciclo di Krebs fino a CO₂, liberando energia',
  "Perché sono la principale riserva di fosfato per la sintesi dell'ATP",
  "Perché sono metaboliti terminali che regolano l'eliminazione delle scorie",
  "Perché forniscono lo scheletro carbonioso dell'acetil-CoA nei tessuti",
  ], 0,
  'Niacina → NAD, riboflavina → FAD, pantotenato → CoA. Sono micronutrienti: servono in piccole quantità e vengono riciclati.')

T = "m1-termodinamica"
q("h1t-01", T, "h", "11–12", "Una reazione A ⇌ B ha ΔG°' = +7 kJ/mol. Nella cellula B viene consumato rapidamente dalla reazione successiva. Che cosa succede?", [
  'Il rapporto [B]/[A] resta basso e il ΔG reale diventa negativo: procede verso B',
  "Non può avvenire, perché un ΔG°' positivo indica che la reazione è impossibile",
  "Procede solo se l'enzima abbassa il ΔG°' della reazione rendendolo negativo",
  'Procede verso A, perché sottraendo il prodotto la reazione torna indietro',
  "Il ΔG°' diventa negativo, perché il consumo di B cambia le condizioni standard",
  ], 0,
  "Il termine RT ln([B]/[A]) è negativo quando B è sottratto. È il caso di aldolasi e trioso fosfato isomerasi: decide il ΔG reale, non il ΔG°'.")
q("h1t-02", T, "h", "11", "Se la Keq di una reazione è 0,01, quale affermazione è corretta?", [
  "ΔG°' è positivo: in condizioni standard prevalgono i reagenti",
  "ΔG°' è negativo e la reazione procede spontaneamente verso i prodotti",
  "ΔG°' è zero, perché la Keq è molto vicina allo zero",
  'La Keq è negativa, quindi la reazione procede verso sinistra',
  'La reazione non può mai avvenire nella cellula, a nessuna concentrazione',
  ], 0,
  "ΔG°' = −RT ln Keq: ln 0,01 < 0, quindi ΔG°' > 0. Con le concentrazioni cellulari la reazione può comunque procedere.",
  note="Sbobina di Biochimica II, p. 11: si parla di Keq «negativa» o «uguale a 0». La Keq è un rapporto di concentrazioni: è sempre positiva; per ΔG°' = 0 vale 1, e per reazioni sfavorite è compresa tra 0 e 1.")
q("h1t-03", T, "h", "12–13", "Perché gli enzimi regolati di una via metabolica catalizzano reazioni con ΔG molto negativo?", [
  'Perché sono tappe irreversibili: controllandole si decide flusso e verso della via',
  'Perché solo le reazioni con ΔG negativo hanno bisogno di un enzima per avvenire',
  "Perché l'enzima regolato è quello che rende negativo il ΔG della reazione",
  "Perché le reazioni all'equilibrio sono troppo lente per essere regolate",
  'Perché sono le uniche reazioni della via che producono o consumano ATP',
  ], 0,
  'Le reazioni con ΔG ≈ 0 seguono le concentrazioni e vanno nei due sensi. Gli enzimi non cambiano il ΔG: cambiano la velocità.')
q("h1t-04", T, "h", "10", "Una reazione ha ΔG molto negativo nella cellula ma procede lentissima senza enzima. Come si spiega?", [
  'La termodinamica dice se può avvenire, non la velocità: serve un enzima',
  'Il ΔG è stato calcolato male: una reazione favorita è sempre veloce',
  "La reazione è all'equilibrio, quindi la sua velocità netta è zero",
  'Un ΔG molto negativo indica sempre una reazione intrinsecamente lenta',
  "Manca l'ATP, che è necessario per tutte le reazioni con ΔG negativo",
  ], 0,
  "Termodinamica = possibilità; cinetica = velocità. L'enzima abbassa l'energia di attivazione.")
q("h1t-05", T, "h", "12", "In una sequenza A ⇌ B ⇌ C di reazioni all'equilibrio, si aggiunge molto C. Che cosa succede?", [
  'Le reazioni si spostano a sinistra: C forma B e B forma A',
  "Aumenta la formazione di C, perché la via è già all'equilibrio",
  "Non succede nulla, perché reazioni all'equilibrio non rispondono",
  'Si blocca solo la seconda reazione, mentre la prima resta invariata',
  'Aumenta A, mentre B resta costante perché è un intermedio',
  ], 0,
  'Principio di Le Chatelier applicato a reazioni in serie (azione di massa).')
q("h1t-06", T, "h", "11–12", "Perché il ΔG°' (pH 7, 25 °C, 1 M) va corretto per descrivere una reazione nella cellula?", [
  'Perché nella cellula le concentrazioni sono millimolari e diverse tra loro',
  'Perché nel citosol il pH è circa 4, molto diverso da quello delle condizioni standard',
  "Perché la temperatura corporea annulla il contributo del ΔG°'",
  "Perché gli enzimi della cellula modificano il valore del ΔG°'",
  "Non va corretto: il ΔG°' coincide con quello che si ha nella cellula",
  ], 0,
  "ΔG = ΔG°' + RT ln([prodotti]/[reagenti]). Pesano soprattutto le concentrazioni; pH e temperatura incidono meno.",
  note="Sbobina di Biochimica II, p. 10: le condizioni standard sono riportate come «T = 273 °K (+25 °C)». 273 K corrisponde a 0 °C; 25 °C sono 298 K.")
q("h1t-07", T, "h", "18", "La fosforilazione del glucosio con Pi ha ΔG°' = +13,8 kJ/mol; l'idrolisi dell'ATP −30,5 kJ/mol. Quanto vale il ΔG°' della reazione esochinasica e perché?", [
  "Circa −16,7 kJ/mol: i ΔG°' di reazioni accoppiate si sommano",
  'Circa +44 kJ/mol: le energie si sommano in valore assoluto',
  "Circa −44 kJ/mol: l'ATP cede tutta la sua energia al glucosio",
  "Circa +13,8 kJ/mol: l'ATP non partecipa al bilancio energetico",
  "Circa 0 kJ/mol: l'enzima porta le due reazioni all'equilibrio",
  ], 0,
  '+13,8 + (−30,5) ≈ −16,7 kJ/mol. Accoppiamento energetico: una reazione endoergonica è spinta da una esoergonica con un intermedio comune.')
q("h1t-08", T, "h", "11", "Qual è la relazione corretta tra ΔG°' e Keq e cosa implica per Keq = 1?", [
  "ΔG°' = −RT ln Keq; con Keq = 1, ΔG°' = 0",
  "ΔG°' = RT ln Keq; con Keq = 1, ΔG°' = RT",
  "ΔG°' = −RT · Keq; con Keq = 1, ΔG°' = −RT",
  "ΔG°' = −nFΔE°' · Keq; con Keq = 1 è massimo",
  "ΔG°' = ΔH − TΔS; con Keq = 1, ΔG°' = ΔH",
  ], 0,
  'ln 1 = 0.',
  note="Sbobina di Biochimica II, p. 10: la formula è scritta «ΔG0 = −RT · keq», senza logaritmo. La relazione corretta è ΔG°' = −RT ln Keq (come poi dice la stessa sbobina a p. 11).")

T = "m1-atp"
q("h1a-01", T, "h", "13–14", "Perché l'idrolisi del legame fosfoanidridico dell'ATP è molto esoergonica?", [
  'Per minor repulsione tra cariche e maggiore risonanza e solvatazione dei prodotti',
  'Perché si rompe il legame fosfoestere tra ribosio e fosfato α, ricco di energia',
  "Perché dall'ATP si forma un legame tioestere con il coenzima A",
  "Perché la reazione consuma un protone e alcalinizza l'ambiente",
  "Perché nella reazione l'adenina viene ossidata e cede elettroni",
  ], 0,
  "ADP e Pi sono più stabilizzati (risonanza, solvatazione) dell'ATP, dove gli ossigeni carichi si respingono. Il fosfoestere tra ribosio e fosfato α è invece a bassa energia.",
  note="Sbobina di Biochimica II, p. 13: c'è scritto che il ΔG dell'idrolisi ATP → ADP + Pi è «ampiamente positivo». È negativo (ΔG°' ≈ −30,5 kJ/mol; nella cellula circa −50 kJ/mol). Sempre a p. 13 l'adenosina è indicata come base azotata: la base è l'adenina; adenosina = adenina + ribosio.")
q("h1a-02", T, "h", "14", "Una reazione di attivazione scinde l'ATP in AMP + PPi e il PPi viene idrolizzato dalla pirofosfatasi. Perché è importante?", [
  'Si rompono due legami fosfoanidridici: la reazione diventa praticamente irreversibile',
  "Si risparmia ATP rispetto alla scissione in ADP + Pi, perché l'AMP viene subito riciclato a ATP",
  "Il PPi è un coenzima che resta legato all'enzima e partecipa alla catalisi",
  'Si forma un legame fosfoestere ad alta energia sul substrato attivato',
  "L'AMP prodotto inibisce allostericamente la reazione inversa",
  ], 0,
  "ΔG°' complessivo ≈ −60 kJ/mol. Il consumo del PPi da parte della pirofosfatasi sottrae prodotto e spinge la reazione.")
q("h1a-03", T, "h", "16", "Calcola la carica energetica di una cellula con ATP 4 mM, ADP 2 mM, AMP 2 mM. Che cosa si attiva?", [
  '0,625: carica bassa, si attivano le vie che producono ATP',
  '0,9: equilibrio tra vie cataboliche e anaboliche',
  '0,5: carica bassa, si attivano le vie anaboliche',
  '0,75: carica alta, prevalgono le vie anaboliche',
  '0,75: carica abbastanza alta, prevalgono le vie anaboliche su quelle cataboliche',
  ], 0,
  'CE = (ATP + ½ADP)/(ATP + ADP + AMP) = (4 + 1)/8 = 0,625. Il valore normale è circa 0,9.')
q("h1a-04", T, "h", "15–16", "Quale fattore modifica di più il ΔG di idrolisi dell'ATP nella cellula rispetto al ΔG°'?", [
  'Le concentrazioni reali di ATP, ADP e Pi, che lo rendono più negativo',
  'La temperatura corporea, che lo rende più vicino allo zero',
  'Il pH citosolico, che lo rende positivo nella maggior parte delle cellule',
  'Il magnesio, che neutralizza le cariche e lo rende quasi nullo',
  "L'AMP, che compete con l'ADP e ne riduce la concentrazione",
  ], 0,
  'Nella cellula il ΔG di idrolisi è circa −50 kJ/mol. PH e Mg²⁺ contano, ma meno delle concentrazioni.',
  note="Sbobina di Biochimica II, p. 16: c'è scritto che con le concentrazioni cellulari il ΔG «diminuisce drasticamente» e che «il ΔG0' passa da −30 a −49». A cambiare è il ΔG reale, non il ΔG°' (che per definizione è standard), e diventa più negativo, cioè la reazione è ancora più favorita.")
q("h1a-05", T, "h", "15", "Qual è la forma dell'ATP che fa da substrato nelle reazioni ATP-dipendenti e perché?", [
  'Il complesso Mg²⁺-ATP, in cui il magnesio scherma le cariche dei fosfati',
  "L'ATP libero, perché il magnesio legato ne bloccherebbe il trasferimento",
  'Il complesso Ca²⁺-ATP, che è la forma prevalente nel citosol',
  "L'ATP completamente protonato, privo di cariche negative",
  'Il complesso Zn²⁺-ATP, perché lo zinco è il cofattore delle chinasi',
  ], 0,
  'Il Mg²⁺ scherma le cariche e orienta il substrato nel sito attivo: per questo le chinasi richiedono magnesio.')
q("h1a-06", T, "h", "17–18", "La nucleoside difosfato chinasi ha ΔG°' ≈ 0. Durante una sintesi proteica intensa che cosa succede?", [
  "La reazione si sposta a destra e rigenera GTP a spese dell'ATP",
  'La reazione si blocca, perché non ha un ΔG sufficientemente negativo',
  "Il GTP viene rigenerato direttamente dall'ATP sintasi mitocondriale",
  'La reazione si sposta a sinistra e produce ATP a spese del GTP',
  "Il GDP accumulato inibisce la sintesi proteica finché l'ATP non cala",
  ], 0,
  "ATP + GDP ⇌ ADP + GTP: il GTP consumato sposta la reazione verso destra. Una reazione all'equilibrio segue le concentrazioni (Le Chatelier).")
q("h1a-07", T, "h", "19–20", "Quale di questi composti NON può fosforilare l'ADP ad ATP in condizioni standard?", [
  'Glucosio 6-fosfato',
  'Fosfoenolpiruvato',
  '1,3-bisfosfoglicerato',
  'Fosfocreatina',
  'Nessuno: tutti e quattro possono farlo',
  ], 0,
  "Il G6P ha un legame fosfoestere a bassa energia (≈ −14 kJ/mol), meno negativo dell'ATP. Gli altri tre hanno ΔG°' di idrolisi più negativo dell'ATP.")
q("h1a-08", T, "h", "20", "All'inizio di uno scatto di 100 m, qual è la prima fonte che mantiene costante l'ATP muscolare?", [
  'La fosfocreatina, tramite la creatina chinasi',
  'La β-ossidazione degli acidi grassi muscolari',
  'Il glicogeno epatico, tramite la glicemia',
  'La fosforilazione ossidativa mitocondriale',
  'La gluconeogenesi epatica dal lattato',
  ], 0,
  "La reazione della creatina chinasi è all'equilibrio: a riposo con molto ATP si forma fosfocreatina, sotto sforzo si riforma ATP.")

T = "m1-coenzimi"
q("h1o-01", T, "h", "21–23", "Nella reazione malato + NAD⁺ → ossalacetato + NADH + H⁺, chi è il donatore ridotto e chi l'accettore ossidato?", [
  'Donatore ridotto: malato; accettore ossidato: NAD⁺',
  'Donatore ridotto: NAD⁺; accettore ossidato: malato',
  'Donatore ridotto: ossalacetato; accettore ossidato: NADH',
  'Donatore ridotto: NADH; accettore ossidato: ossalacetato',
  "Non è una redox, ma un'isomerizzazione del malato",
  ], 0,
  "L'alcol secondario del malato si ossida a chetone cedendo un idruro al NAD⁺.")
q("h1o-02", T, "h", "21–23", "Qual è la differenza nel modo in cui NAD⁺ e FAD accettano gli elettroni?", [
  'Il NAD⁺ accetta un idruro; il FAD accetta due atomi di idrogeno',
  'Il NAD⁺ accetta due atomi di idrogeno; il FAD accetta un idruro',
  'Entrambi accettano un solo elettrone alla volta, come i citocromi',
  'Il NAD⁺ accetta ossigeno, il FAD accetta idrogeno',
  'Il FAD accetta quattro elettroni, il NAD⁺ due',
  ], 0,
  "Idruro = 2 e⁻ + 1 H⁺; l'altro H⁺ va in soluzione, per questo si scrive NADH + H⁺. Il FAD diventa FADH₂.")
q("h1o-03", T, "h", "23", "La reazione succinato → fumarato è catalizzata da un enzima a FAD e non a NAD. Che tipo di ossidazione è?", [
  'Una deidrogenazione C–C: due carboni saturi formano un doppio legame',
  "L'ossidazione di un alcol secondario a chetone, che è la reazione tipica dei coenzimi flavinici",
  "L'ossidazione di un'aldeide ad acido carbossilico",
  "Un'idratazione del doppio legame con aggiunta di H₂O",
  'Una decarbossilazione ossidativa con liberazione di CO₂',
  ], 0,
  'Si perdono 2 elettroni come 2 atomi di H. Le deidrogenazioni C–C usano il FAD; quelle di alcoli e aldeidi in genere il NAD⁺.')
q("h1o-04", T, "h", "23", "Fumarato → malato è catalizzata dalla fumarasi. Qual è la natura della reazione?", [
  "È un'idratazione: non è un'ossidoriduzione netta",
  "È un'ossidazione che richiede NAD⁺ come accettore",
  'È una riduzione che richiede FADH₂ come donatore',
  'È una decarbossilazione che libera CO₂',
  "È un'isomerizzazione con spostamento di un fosfato",
  ], 0,
  "Si aggiunge H₂O al doppio legame. Prepara l'alcol secondario che poi sarà ossidato dalla malato deidrogenasi.")
q("h1o-05", T, "h", "22–23", "Il passaggio da un'aldeide a un chetone con la stessa formula (es. GAP → DHAP) è:", [
  "Un'isomerizzazione: lo stato di ossidazione complessivo non cambia",
  "Un'ossidazione: il chetone è più ossidato dell'aldeide",
  'Una riduzione: il carbonio chetonico è più ridotto di quello aldeidico, quindi serve NADH',
  'Una decarbossilazione, perché cambia il numero di carboni',
  "Un'idrolisi, perché richiede l'aggiunta di acqua",
  ], 0,
  'Come G6P → F6P e GAP ⇌ DHAP: nessun coenzima redox.')
q("h1o-06", T, "h", "22", "Quale sequenza ordina i composti a un carbonio dal più ridotto al più ossidato?", [
  'Metano → metanolo → formaldeide → acido formico → CO₂',
  'CO₂ → acido formico → formaldeide → metanolo → metano',
  'Metanolo → metano → formaldeide → CO₂ → acido formico',
  'Formaldeide → metanolo → metano → acido formico → CO₂',
  'Metano → formaldeide → metanolo → CO₂ → acido formico',
  ], 0,
  'Da −4 (metano) a +4 (CO₂): 8 elettroni in totale.',
  note="Sbobina di Biochimica II, p. 22: c'è scritto che l'azoto è «meno elettronegativo del carbonio». È il contrario: l'azoto è più elettronegativo del carbonio.")
q("h1o-07", T, "h", "24", "Nella cellula si parla di «piruvato» e non di «acido piruvico» perché:", [
  'Il carbossile ha pKa ≈ 3,5: a pH 7,4 è quasi tutto deprotonato',
  "L'acido piruvico è instabile e si decarbossila subito a acetaldeide",
  "Il piruvato è la forma ridotta dell'acido piruvico, prodotta dalla LDH",
  'Il piruvato nella cellula è sempre legato al coenzima A',
  'Il carbossile ha pKa ≈ 9: a pH 7,4 è quasi tutto protonato',
  ], 0,
  'Quando pH > pKa prevale la forma deprotonata (base coniugata, suffisso «-ato»).')
q("h1o-08", T, "h", "21", "Quale accoppiamento vitamina-coenzima è corretto?", [
  'Niacina → NAD; riboflavina → FAD; pantotenato → CoA',
  'Riboflavina → NAD; niacina → FAD; tiamina → CoA',
  'Tiamina → NAD; biotina → FAD; folato → CoA',
  'Niacina → FAD; pantotenato → NAD; riboflavina → TPP',
  'Cobalamina → NAD; niacina → CoA; riboflavina → biotina',
  ], 0,
  'La tiamina dà il TPP, usato dalla piruvato deidrogenasi.')

T = "m1-enzimologia"
q("h1e-01", T, "h", "26–27", "Raddoppiando la concentrazione di un enzima michaeliano (substrato in eccesso), che cosa cambia?", [
  'Raddoppia la Vmax, la KM resta invariata',
  'Si dimezza la KM, la Vmax resta invariata',
  'Raddoppiano sia la Vmax sia la KM',
  'Non cambiano né la Vmax né la KM',
  "Aumenta l'affinità per il substrato",
  ], 0,
  "Vmax = kcat·[E]. La KM è una costante dell'enzima; la Vmax dipende dalla quantità di enzima.")
q("h1e-02", T, "h", "27", "Un enzima ha KM = 0,1 mM e un isoenzima KM = 10 mM per lo stesso substrato. Con [S] = 0,1 mM e Vmax uguali:", [
  "Il primo lavora a ½ Vmax, il secondo a circa l'1% della Vmax",
  'Lavorano entrambi a circa metà della propria Vmax',
  'Il secondo è più veloce perché ha la KM più alta',
  'Entrambi lavorano vicino alla Vmax',
  'Il primo è a ½ Vmax, il secondo a circa il 50% della Vmax',
  ], 0,
  'V = Vmax[S]/(KM + [S]): 0,1/0,2 = 0,5; 0,1/10,1 ≈ 0,01. È il caso esochinasi/glucochinasi.')
q("h1e-03", T, "h", "28", "Un effettore allosterico negativo che stabilizza la forma T come modifica la curva di un enzima allosterico?", [
  'Sposta la sigmoide a destra: aumenta la K0,5',
  'Sposta la sigmoide a sinistra: diminuisce la K0,5',
  "La trasforma in un'iperbole e raddoppia la Vmax",
  'Riduce la Vmax lasciando invariata la K0,5',
  'Non cambia la curva perché agisce sul sito catalitico',
  ], 0,
  'La K0,5 è la KM apparente: serve più substrato per la stessa velocità. Effettore positivo → forma R, curva a sinistra; negativo → forma T, curva a destra.')
q("h1e-04", T, "h", "28", "Quale affermazione descrive correttamente un effettore omotropico?", [
  "È il substrato stesso che, legandosi, modifica l'affinità degli altri siti",
  "È un effettore diverso dal substrato che si lega al sito allosterico e sposta l'equilibrio R/T",
  'È sempre un inibitore, perché stabilizza la forma T',
  'Si lega solo al sito catalitico, competendo con il substrato',
  "È un ormone che fosforila l'enzima su serine e treonine",
  ], 0,
  "Esempio: l'ATP per la PFK1 (cooperatività). Eterotropico = diverso dal substrato (es. AMP, citrato, F2,6BP sulla PFK1).")
q("h1e-05", T, "h", "29–30", "Il glucagone modifica l'attività di un enzima epatico nel giro di minuti. Quale meccanismo è più probabile?", [
  'Fosforilazione su Ser/Thr da una protein chinasi',
  "Induzione della trascrizione del gene dell'enzima",
  "Degradazione dell'enzima nel proteasoma",
  'Legame di un effettore allosterico prodotto dalla via',
  "Spostamento dell'enzima nel nucleo da parte di una proteina regolatrice",
  ], 0,
  'Gli ormoni agiscono per lo più con modificazioni covalenti (minuti), revertite dalle fosfatasi; la sintesi di nuovo enzima richiede ore.')
q("h1e-06", T, "h", "27", "Quale definizione è corretta per la KM?", [
  'La [S] a cui V0 = ½ Vmax; vale (k₋₁ + k₂)/k₁',
  "La velocità massima raggiungibile dall'enzima",
  'La costante di formazione del complesso ES (k₁)',
  "Un valore che aumenta all'aumentare dell'enzima",
  'Il rapporto tra kcat e la concentrazione di enzima',
  ], 0,
  'Solo se k₂ ≪ k₋₁ la KM approssima la costante di dissociazione di ES.')
q("h1e-07", T, "h", "42–43", "Un enzima ha kcat/KM ≈ 10⁸–10⁹ M⁻¹ s⁻¹ (es. trioso fosfato isomerasi). Che cosa significa?", [
  'Che la velocità è limitata solo dalla diffusione del substrato',
  'Che è un enzima molto lento, limitato dalla tappa catalitica',
  'Che ha una bassissima affinità per il proprio substrato',
  'Che è un enzima allosterico con cinetica sigmoide',
  'Che la reazione catalizzata è irreversibile',
  ], 0,
  'Ha raggiunto la perfezione catalitica. kcat/KM è la costante di specificità.')
q("h1e-08", T, "h", "30", "Glicolisi e gluconeogenesi avvengono nello stesso compartimento con molti enzimi in comune. Come si evita un ciclo futile?", [
  'Le tappe irreversibili hanno enzimi diversi, regolati in modo reciproco',
  'Le due vie avvengono in organi diversi e quindi nella stessa cellula non si sovrappongono mai',
  'Gli enzimi in comune alle due vie sono tutti irreversibili',
  'La gluconeogenesi avviene interamente nel mitocondrio',
  'Le due vie usano coenzimi diversi che non si scambiano',
  ], 0,
  "Se si attiva l'enzima catabolico si inibisce quello anabolico: è lo schema E3/E6 della sbobina.")
