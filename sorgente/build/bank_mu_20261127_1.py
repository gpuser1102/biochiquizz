"""Giro 2026-11-27, blocco 1 – Biologia molecolare: argomenti scarni (recettori, proteine G,
ormoni pancreatici e della volemia, organi di senso, nucleotidi, folato, purine, pirimidine,
eme, bilirubina, ferro), con gli appunti 2023/24 caricati nel Project il 26/11."""
from bank_common import q as _q

S = "Biologia molecolare"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


def A(p):
    return f"appunti 2023/24, p. {p}"


# ── Interazione recettore-ligando ──────────────────────────────────────────
C = "bm1-recettore-ligando"

q("u1127-001", C, "a", A(10), "Nel grafico di Scatchard ([RL]/[L] in funzione di [RL]), dove si legge Bmax?", [
  "All'intercetta con l'asse del legato [RL], dove il rapporto [RL]/[L] vale zero",
  "All'intercetta con l'asse [RL]/[L], dove il legato [RL] vale esattamente zero",
  "Nella pendenza della retta, che corrisponde direttamente al valore di Bmax",
  "Nel punto in cui la retta incrocia la bisettrice del primo quadrante del grafico",
  "Nel punto di flesso della curva, che nel grafico di Scatchard è sigmoide",
  ], 0,
  "[RL]/[L] = (Bmax − [RL])/Kd: quando [RL]/[L] = 0, [RL] = Bmax. L'intercetta sull'asse y vale Bmax/Kd e la pendenza −1/Kd. Gli appunti scrivono solo «intercetta = Bmax» senza dire su quale asse.")

q("u1127-002", C, "f", A(9), "Che cosa rappresenta Bmax nell'equazione Bmax = [R] + [RL]?", [
  "Il numero totale di siti di legame, liberi più occupati dal ligando",
  "La concentrazione totale di ligando, libero più legato al recettore",
  "La concentrazione di ligando che occupa la metà dei siti di legame",
  "Il rapporto tra costante di associazione e costante di dissociazione",
  "La velocità massima con cui si forma il complesso recettore-ligando",
  ], 0,
  "Bmax è il numero massimo di siti saturabili: recettore libero [R] più recettore legato [RL]. La concentrazione che occupa metà dei siti è la Kd.")

# ── Recettori canale ───────────────────────────────────────────────────────
C = "bm2-canali"

q("u1127-003", C, "l", A(16), "Dove si legano le due molecole di acetilcolina sul recettore nicotinico?", [
  "Alle interfacce tra le subunità α/δ e α/γ, nel dominio extracellulare",
  "Alle interfacce tra le subunità β/δ e β/γ, nel dominio extracellulare",
  "Al centro del poro, sull'elica 2 di ciascuna delle cinque subunità",
  "Sulle due subunità β, nel dominio citosolico vicino all'elica 4",
  "In un'unica tasca della subunità δ, accanto al ponte disolfuro",
  ], 0,
  "Il recettore è un pentamero α₂βγδ; i due siti per l'acetilcolina stanno tra α e δ e tra α e γ, in una regione N-terminale extracellulare con un ponte disolfuro. Il legame di entrambe apre il poro.")

q("u1127-004", C, "m", A(17), "Che fine fa il GABA ricaptato dagli astrociti?", [
  "Diventa glutammato e glutammina, che torna al neurone e rigenera il GABA",
  "Viene ossidato direttamente a CO₂ per fornire energia all'astrocita",
  "Viene coniugato con acido glucuronico ed eliminato con le urine",
  "Viene idrolizzato da un'esterasi a glicina e acido butirrico",
  "Resta immagazzinato nell'astrocita come riserva stabile di neurotrasmettitore",
  ], 0,
  "Il GABA si forma dal glutammato per decarbossilazione; ricaptato dagli astrociti torna glutammato e poi glutammina, che rientra nel neurone ed è riconvertita in glutammato e GABA.")

q("u1127-005", C, "m", A(16), "Con quale via agiscono i recettori muscarinici M1, M3 e M5?", [
  "Attivano la via dei fosfoinositidi, con fosfolipasi C, IP₃ e DAG",
  "Inibiscono l'adenilato ciclasi e fanno scendere il cAMP nella cellula",
  "Sono canali cationici che si aprono direttamente legando l'acetilcolina",
  "Attivano la guanilato ciclasi solubile e fanno salire il cGMP",
  "Attivano direttamente JAK, che fosforila e attiva le proteine STAT",
  ], 0,
  "I muscarinici sono GPCR: quelli dispari (M1, M3, M5) attivano la via dei fosfoinositidi, quelli pari (M2, M4) inibiscono l'adenilato ciclasi. Il canale cationico è il recettore nicotinico.")

# ── Recettori tirosin-chinasici e terapia ──────────────────────────────────
C = "bm2-rtk"

q("u1127-006", C, "m", A(18), "Che affinità hanno per il ligando i recettori ad attività catalitica e in che tempi agiscono?", [
  "Altissima (picomolare): legano fattori di crescita e agiscono in minuti od ore",
  "Bassa (millimolare): legano neurotrasmettitori e agiscono in millisecondi",
  "Micromolare: legano ormoni steroidei e agiscono sul DNA in pochi secondi",
  "Nanomolare: legano solo l'insulina e agiscono soltanto in modo autocrino",
  "Variabile: legano lipidi e nucleotidi e agiscono tramite proteine G trimeriche",
  ], 0,
  "I recettori catalitici legano fattori di crescita e di differenziamento con affinità dell'ordine del picomolare e regolano funzioni su tempi lunghi. La bassa affinità è tipica dei recettori canale per i neurotrasmettitori.")

C = "bm2-terapia"

q("u1127-007", C, "l", A(20), "In quali tumori è implicato HER1 secondo gli appunti?", [
  "Vescica, seno, rene, prostata e glioblastomi",
  "Solo nel carcinoma mammario con amplificazione genica",
  "Ovaio, utero e cervice, ma non i tumori del sistema nervoso",
  "Leucemie e linfomi, perché HER1 è espresso solo nel sangue",
  "Colon, stomaco ed esofago, ma non vescica o prostata",
  ], 0,
  "Gli appunti associano HER1 (EGFR) a vescica, seno, rene, prostata e glioblastomi; HER3 al carcinoma mammario, HER4 all'ovaio. HER2 non lega fattori di crescita ma forma eterodimeri.")

C = "bm2-citochine"

q("u1127-008", C, "f", A(21), "Che cosa sono le citochine secondo gli appunti?", [
  "Polipeptidi del sistema immunitario, come interleuchine e interferoni",
  "Ormoni steroidei prodotti dalla corticale del surrene durante lo stress",
  "Amine derivate dalla tirosina che agiscono sul sistema nervoso centrale",
  "Lipidi derivati dall'acido arachidonico con azione solo paracrina",
  "Nucleotidi ciclici che fanno da secondi messaggeri nei linfociti",
  ], 0,
  "Le citochine (interleuchine, interferoni) sono polipeptidi prodotti dal sistema immunitario che regolano crescita e differenziamento, agendo in modo autocrino e paracrino.")

q("u1127-009", C, "a", A(21), "Perché i recettori per le citochine possono avere affinità diverse per i loro ligandi?", [
  "Le citochine agiscono a distanze diverse, in modo autocrino o paracrino",
  "Le citochine sono lipidi e attraversano la membrana a velocità diverse",
  "I recettori hanno un'attività chinasica propria che varia da cellula a cellula",
  "Le citochine circolano legate a proteine di trasporto di affinità variabile",
  "I recettori sono canali ionici e l'affinità dipende dal potenziale di membrana",
  ], 0,
  "Come per tutti i recettori, l'affinità si adatta alla concentrazione a cui arriva il ligando: segnali autocrini e paracrini percorrono distanze diverse. I recettori per le citochine non hanno attività enzimatica propria: usano JAK.")

# ── GPCR, tossine e spegnimento ────────────────────────────────────────────
C = "bm3-gpcr"

q("u1127-010", C, "h", A(23), "Gli appunti dicono che sia la Gα sia la Gγ restano in membrana grazie a un'ancora prenilica. Che cosa è più corretto?", [
  "La Gγ è prenilata; la Gα è ancorata da acidi grassi, cioè palmitoile o miristoile",
  "Entrambe sono prenilate, come scritto; la Gβ resta in membrana legata alla Gγ",
  "La Gα è prenilata; la Gγ è una proteina integrale con una sola elica transmembrana",
  "Nessuna delle due è lipidata: il trimero resta in membrana solo legando il recettore",
  "La Gβ è prenilata e trattiene in membrana sia la Gα sia la Gγ a cui è legata",
  ], 0,
  "La Gγ porta un gruppo prenilico (farnesile o geranilgeranile); la Gα è acilata (palmitoile, alcune anche miristoile). In entrambi i casi l'ancora è lipidica e il sistema resta sul versante citosolico della membrana. Il tipo di lipide non è nelle sbobine (Lehninger, Stryer).",
  note="Appunti di Biologia molecolare 2023/24, p. 23 (e sbobina, lezione 3): attribuiscono un'ancora prenilica anche alla Gα. È prenilata solo la Gγ; la Gα è ancorata da palmitoile o miristoile.")

q("u1127-011", C, "l", A(26), "Com'è fatta la tossina del colera?", [
  "5 subunità B che legano un ganglioside e una subunità A (A1 + A2) catalitica",
  "2 subunità A che legano il ganglioside e 5 subunità B dotate di attività catalitica",
  "Una sola catena con un dominio che lega il recettore e uno che ADP-ribosila",
  "5 subunità A identiche, ognuna con attività ADP-ribosiltransferasica",
  "Un dimero A-B in cui B entra nella cellula e A resta legata al ganglioside",
  ], 0,
  "Le 5 subunità B riconoscono un ganglioside (GM1) sulla membrana delle cellule intestinali; la subunità A entra, si separa e A1 (il core catalitico) ADP-ribosila la Gαs. Il nome GM1 non è nelle sbobine.")

q("u1127-012", C, "a", A(26), "La tossina del colera ADP-ribosila la stessa arginina della Gαs che è mutata nell'oncogene gsp. Che cosa hanno in comune i due casi?", [
  "In entrambi la Gαs non idrolizza il GTP e resta attiva sull'adenilato ciclasi",
  "In entrambi la Gαs non scambia più il GDP con il GTP e resta sempre spenta",
  "In entrambi il recettore non lega più il ligando e il cAMP crolla nella cellula",
  "In entrambi la Gαi viene bloccata e l'adenilato ciclasi resta sempre inibita",
  "In entrambi le subunità βγ non si staccano e l'effettore non viene raggiunto",
  ], 0,
  "Nell'oncogene gsp la perdita dell'attività GTPasica è dovuta a una mutazione, nel colera a una modificazione covalente dello stesso residuo: in tutti e due i casi la Gαs resta legata al GTP e l'adenilato ciclasi produce cAMP senza sosta.")

C = "bm3-spegnimento"

q("u1127-013", C, "a", A(27), "La PKA, una volta attivata, contribuisce anche a spegnere il segnale. In che modo, secondo gli appunti?", [
  "Viene portata sul sito insieme a una fosfatasi, che toglie i fosfati ai bersagli",
  "Si autofosforila e diventa insensibile al cAMP per alcune ore",
  "Degrada le proprie subunità regolatrici e resta poi inattiva per sempre",
  "Fosforila l'adenilato ciclasi e la trasforma in una fosfodiesterasi del cAMP",
  "Lega la β-arrestina e la trasporta sul recettore β-adrenergico",
  ], 0,
  "Sul sito di attivazione della PKA viene portata anche una fosfatasi che defosforila i bersagli. Inoltre la PKA fosforila una fosfodiesterasi del cAMP. Gli altri meccanismi di spegnimento sono l'attività GTPasica della Gα e la desensibilizzazione del recettore.")

q("u1127-014", C, "h", A(25), "In una cellula la βARK non funziona. Che cosa succede durante una stimolazione adrenergica prolungata?", [
  "Il recettore non viene fosforilato in C-terminale, la β-arrestina non si lega e la desensibilizzazione è ridotta",
  "La Gαs non idrolizza più il GTP e l'adenilato ciclasi resta attiva anche dopo che l'adrenalina si è staccata",
  "Il recettore viene endocitato più in fretta, perché la β-arrestina si lega subito anche senza fosforilazione",
  "Il cAMP non si forma affatto, perché la βARK è indispensabile per attivare l'adenilato ciclasi a valle della Gαs",
  "Le subunità βγ non si separano dalla Gα e il segnale dell'adrenalina non parte nemmeno all'inizio",
  ], 0,
  "Le βγ liberate richiamano la βARK, che fosforila la coda C-terminale del recettore; la β-arrestina lega quei fosfati e occupa la superficie su cui si lega la proteina G. Senza βARK manca questo passaggio e il recettore continua a segnalare.")

# ── Glucagone e controllo reciproco del glicogeno ──────────────────────────
C = "bm5-glucagone"

q("u1127-015", C, "f", A(41), "In quale condizione viene secreto il glucagone e dove agisce soprattutto?", [
  "Nell'ipoglicemia; agisce soprattutto sul fegato",
  "Nell'iperglicemia; agisce soprattutto sul muscolo",
  "Dopo un pasto; agisce soprattutto sul tessuto adiposo",
  "Nello stress acuto; agisce soprattutto sul cuore",
  "Nell'ipoglicemia; agisce soprattutto sul muscolo scheletrico",
  ], 0,
  "Le cellule α secernono glucagone quando la glicemia scende; il bersaglio principale è il fegato, che degrada glicogeno, fa gluconeogenesi e rilascia glucosio. Il muscolo non ha recettori per il glucagone (non è nelle sbobine).")

q("u1127-016", C, "m", A(43), "Su quali enzimi epatici agisce il glucagone per favorire la gluconeogenesi rispetto alla glicolisi?", [
  "Aumenta la PEP carbossichinasi e riduce la piruvato chinasi",
  "Aumenta la piruvato chinasi e riduce la PEP carbossichinasi",
  "Aumenta la glucochinasi e riduce la glucosio 6-fosfatasi",
  "Aumenta la PFK-1 e riduce la fruttosio 1,6-bisfosfatasi",
  "Aumenta la piruvato deidrogenasi e riduce la piruvato carbossilasi",
  ], 0,
  "Il glucagone inattiva per fosforilazione la piruvato chinasi L, aumenta la PEP carbossichinasi e abbassa il fruttosio 2,6-bisfosfato, così la PFK-1 rallenta e la FBPasi-1 lavora.")

q("u1127-017", C, "a", A(41), "Come contrastano glucagone e adrenalina la PP1 che l'insulina porta sul glicogeno?", [
  "La PKA fosforila GM in un secondo sito, che la stacca, e attiva l'inibitore della PP1",
  "La PKA defosforila GM, che si stacca dal glicogeno e porta via con sé la PP1",
  "La PKA marca la PP1 con ubiquitina e la manda a degradare nel proteasoma",
  "La PKB fosforila la PP1 su una serina N-terminale che fa da pseudosubstrato",
  "La PKA fosforila la glicogeno sintasi, che a sua volta lega e inibisce stabilmente la PP1",
  ], 0,
  "Con insulina GM, fosforilata, porta la PP1 su sintasi e fosforilasi. La PKA fosforila GM in una seconda posizione (perde affinità e rilascia gli enzimi) e attiva l'inibitore della PP1, che la lega e la blocca.")

# ── Volemia ────────────────────────────────────────────────────────────────
C = "bm6-vasopressina"

q("u1127-018", C, "m", A(49), "Quali stimoli fanno liberare la vasopressina?", [
  "Calo della pressione (barocettori) e aumento dell'osmolarità (osmocettori)",
  "Aumento della pressione (barocettori) e calo dell'osmolarità (osmocettori)",
  "Stiramento dell'atrio e aumento della concentrazione dei sali nel sangue",
  "Ipoglicemia e aumento del cortisolo nel sangue durante il digiuno",
  "Calo della pressione e calo dell'osmolarità del plasma, insieme",
  ], 0,
  "La vasopressina viene rilasciata quando i barocettori segnalano una pressione bassa e gli osmocettori una concentrazione salina alta: trattiene acqua. Lo stiramento atriale fa invece liberare l'ANP.")

q("u1127-019", C, "l", A(49), "In quali nuclei dell'ipotalamo si forma la maggior parte della vasopressina?", [
  "Sopraottico e paraventricolare",
  "Arcuato e ventromediale",
  "Soprachiasmatico e preottico",
  "Dorsomediale e laterale",
  "Paraventricolare e soprachiasmatico",
  ], 0,
  "La vasopressina è sintetizzata nei nuclei sopraottico e paraventricolare e scende per via assonale alla neuroipofisi, da cui viene immessa in circolo.")

C = "bm6-adrenalina"

q("u1127-020", C, "m", A(48), "Quale recettore dell'istamina è bloccato dagli antistaminici per le allergie respiratorie e con quale proteina G lavora?", [
  "H1, con una Gq che attiva la fosfolipasi C",
  "H2, con una Gs che fa salire il cAMP",
  "H1, con una Gi che fa scendere il cAMP",
  "H3, con una Gq che attiva la fosfolipasi C",
  "H4, con una Gs che fa salire il cAMP",
  ], 0,
  "H1 (bronchi, intestino, sistema cardiovascolare) usa Gq e PLC ed è il bersaglio di loratadina, cetirizina e fexofenadina. H2 regola la secrezione gastrica con Gs; H4 usa proteine G inibitorie.")

C = "bm6-idrofobici"

q("u1127-021", C, "l", A(51), "Quale abbinamento tra proteina di trasporto e ormoni è corretto?", [
  "SHBG – ormoni sessuali",
  "Transcortina – estrogeni",
  "ABP – glucocorticoidi",
  "CBG – ormoni tiroidei",
  "SHBG – aldosterone",
  ], 0,
  "Gli steroidi viaggiano legati a transcortina (CBG, corticosteroidi), SHBG (ormoni sessuali), ABP o TeBG (androgeni) e albumina.")

# ── Vitamina D, olfatto ────────────────────────────────────────────────────
C = "bm7-vitd"

q("u1127-022", C, "f", A(54), "Come si chiama la vitamina D3 che si forma nella pelle per azione della luce?", [
  "Colecalciferolo",
  "Ergocalciferolo",
  "Calcitriolo",
  "Calcidiolo",
  "7-deidrocolesterolo",
  ], 0,
  "La luce taglia l'anello B del 7-deidrocolesterolo tra C9 e C10 e si forma il colecalciferolo; poi fegato (25-OH, calcidiolo) e rene (1-OH, calcitriolo) lo attivano. L'ergocalciferolo è la vitamina D2, di origine vegetale.")

q("u1127-023", C, "m", A(54), "Quali processi media la vitamina D3 secondo gli appunti?", [
  "Assorbimento del Ca²⁺ in intestino e rene, rimodellamento dell'osso, risposta immunitaria",
  "Escrezione del Ca²⁺ con le urine, blocco degli osteoclasti, coagulazione del sangue",
  "Assorbimento intestinale del ferro, sintesi dell'emoglobina, maturazione degli eritrociti",
  "Riassorbimento renale del Na⁺, secrezione di renina, controllo della pressione",
  "Rilascio di insulina, captazione del glucosio nel muscolo, sintesi del glicogeno",
  ], 0,
  "Il calcitriolo, tramite il VDR, aumenta l'assorbimento di Ca²⁺ intestinale e renale, regola mineralizzazione e riassorbimento osseo (osteoclasti) e ha effetti sulla risposta immunitaria.")

C = "bm7-olfatto"

q("u1127-024", C, "m", A(58), "Che cosa rende «odorosa» una molecola, secondo gli appunti?", [
  "Il fatto di legare in modo selettivo uno dei recettori olfattivi, grazie alla sua struttura",
  "La sola volatilità: qualunque molecola volatile attiva allo stesso modo tutti i recettori olfattivi",
  "La presenza di un gruppo tiolico, che apre direttamente i canali del Cl⁻ delle ciglia",
  "La carica positiva: solo i cationi aprono i canali cAMP-dipendenti del neurone",
  "La capacità di attraversare la membrana e legare un recettore nucleare del neurone",
  ], 0,
  "Conta la struttura: una molecola è odorosa se dà un legame selettivo con uno dei circa mille recettori. Due enantiomeri come R- e S-carvone attivano recettori diversi e hanno odori diversi.")

q("u1127-025", C, "h", A(59), "Alcune molecole odorose attivano proteine G inibitorie. Quale effetto è coerente con quanto descritto negli appunti?", [
  "Bloccano la guanilato ciclasi o attivano fosfodiesterasi: meno nucleotide ciclico e meno depolarizzazione",
  "Aumentano il cAMP e aprono più canali del Cl⁻: la depolarizzazione del neurone diventa più forte",
  "Fanno chiudere i canali del K⁺ dalla PKA basolaterale: la percezione dell'odore viene amplificata",
  "Liberano Ca²⁺ dal reticolo tramite l'IP₃ e aprono canali del Na⁺: il neurone si depolarizza molto di più",
  "Non hanno effetti, perché nei neuroni olfattivi non sono espresse proteine G di tipo inibitorio",
  ], 0,
  "La via principale (Gα olfattiva → adenilato ciclasi → cAMP → canali cationici → uscita di Cl⁻) depolarizza. Le proteine G inibitorie riducono il nucleotide ciclico (meno guanilato ciclasi, più fosfodiesterasi) e quindi la depolarizzazione.")

# ── Nucleotidi ─────────────────────────────────────────────────────────────
C = "bm7-nucleotidi"

q("u1127-026", C, "a", A(63), "Come cambia la distribuzione dei nucleotidi in una cellula in ipossia?", [
  "Prevalgono NMP e NDP, mentre la somma dei nucleotidi resta costante",
  "Prevalgono gli NTP, perché la cellula accumula ATP come riserva di energia",
  "Prevalgono i dNTP, perché la cellula si prepara alla divisione",
  "Cala la somma di AMP, ADP e ATP, che vengono tutti degradati",
  "Prevalgono i nucleotidi guanilici su quelli adenilici",
  ], 0,
  "La concentrazione totale (AMP + ADP + ATP) è costante; cambia il rapporto. Con uno stato energetico basso, come in ipossia, prevalgono mono- e difosfati; nelle cellule che funzionano bene prevalgono i trifosfati.")

q("u1127-027", C, "m", A(63), "Quando aumentano molto i deossiribonucleotidi trifosfato nella cellula?", [
  "Durante la duplicazione del DNA, perché sono i substrati della DNA polimerasi",
  "In ipossia, quando la cellula converte gli NTP in forme più stabili",
  "Durante la sintesi proteica, perché servono a caricare i tRNA sugli amminoacidi",
  "Nel digiuno, perché derivano dalla degradazione degli NTP",
  "Negli eritrociti maturi, che li usano come riserva di energia",
  ], 0,
  "Di norma i ribonucleotidi prevalgono sui dNTP; questi salgono molto durante la duplicazione cellulare, quando la DNA polimerasi li consuma.")

q("u1127-028", C, "m", A(63), "Quale legame unisce base e zucchero in un nucleoside e perché si chiama β?", [
  "N-glicosidico; è β perché l'anomero del ribosio è β e la base sta sopra il piano dell'anello",
  "N-glicosidico; è β perché coinvolge l'azoto in posizione β della base, cioè N3 o N7",
  "O-glicosidico; è β perché la base si lega con un ossigeno al C1' del ribosio nell'anomero β",
  "Fosfodiestere; è β perché il fosfato fa da ponte tra la base e il C5' dello zucchero",
  "N-glicosidico; è β perché coinvolge il C5' del ribosio e non il C1'",
  ], 0,
  "Il legame si forma per condensazione tra il C1' dello zucchero e un azoto della base (N1 nelle pirimidine, N9 nelle purine); è β perché l'anomero è β, con la base sopra il piano del ribosio.")

# ── Folato e THF ───────────────────────────────────────────────────────────
C = "bm8-folato"

q("u1127-029", C, "h", A(67), "Gli appunti dicono che il metilen-THF viene ossidato a metenil-THF da una «metenil-THF reduttasi» che usa NADP⁺. Che cosa è corretto?", [
  "È la metilen-THF deidrogenasi: ossida il metilene con NADP⁺ e forma NADPH",
  "È corretto così: una reduttasi può usare il NADP⁺ per ossidare il metilene",
  "È la metilen-THF reduttasi: riduce il metilene a metile usando il NADH",
  "È la cicloidrolasi: apre l'anello del metenile e forma N10-formil-THF",
  "È la timidilato sintasi: ossida il metilene e libera DHF con il FAD",
  ], 0,
  "Il passaggio metilene → metenile è un'ossidazione, catalizzata dalla metilen-THF deidrogenasi con NADP⁺. La metilen-THF reduttasi fa l'opposto (metilene → metile) con NADPH; la cicloidrolasi converte il metenile in N10-formile.",
  note="Appunti di Biologia molecolare 2023/24, p. 67: chiamano «metenil THF reduttasi» l'enzima che ossida il metilen-THF con NADP⁺. È la metilen-THF deidrogenasi.")

q("u1127-030", C, "m", A(67), "A quali usi è destinata ciascuna forma carica del THF?", [
  "N10-formile per le purine, metilene per il dTMP, metile per la metionina",
  "N10-formile per il dTMP, metilene per la metionina, metile per le purine",
  "Metilene per le purine, N10-formile per la metionina, metile per il dTMP",
  "Metile per le purine e il dTMP, N10-formile solo per la metionina",
  "N5-formimino per le purine, metilene per la serina, metile per il dTMP",
  ], 0,
  "L'N10-formil-THF dona C2 e C8 della purina; il metilen-THF dà il metile del dTMP (timidilato sintasi); il metil-THF serve solo alla metionina sintasi, insieme alla B12.")

q("u1127-031", C, "a", A(67), "Qual è il principale donatore di unità monocarboniose al THF e che cosa si forma?", [
  "La serina, che diventa glicina e forma N5,N10-metilen-THF",
  "La glicina, che diventa serina e forma l'N10-formil-THF",
  "L'istidina, che diventa glutammato e forma metil-THF",
  "Il formiato, che diventa CO₂ e forma N5,N10-metilen-THF",
  "La metionina, che diventa omocisteina e forma metil-THF",
  ], 0,
  "La serina idrossimetiltransferasi cede il CH₂ della serina al THF (metilen-THF) e la serina diventa glicina. Formiato (N10-formile), istidina (formimino) e glicina (sistema di taglio) sono fonti minori.")

# ── Purine: regolazione, degradazione, salvataggio ─────────────────────────
C = "bm8-regolazione"

q("u1127-032", C, "l", A(69), "Quali siti allosterici inibitori ha la glutammina PRPP amidotransferasi?", [
  "Uno per gli ossipurinici (IMP, XMP, GMP) e uno per gli amminopurinici (AMP), con inibizione sinergica",
  "Uno per l'ATP e uno per il GTP, che hanno effetti opposti e si annullano a vicenda",
  "Uno per il PRPP e uno per la glutammina, che inibiscono entrambi l'enzima quando sono in eccesso nella cellula",
  "Uno solo, che lega tutti i nucleotidi monofosfato senza alcun effetto sinergico tra di loro",
  "Uno per i nucleotidi pirimidinici e uno per quelli purinici, che agiscono separatamente",
  ], 0,
  "L'enzima ha due siti per i prodotti finali: quando sono occupati entrambi l'inibizione è sinergica e l'enzima passa al dimero inattivo. Il PRPP, al contrario, favorisce il monomero attivo.")

q("u1127-033", C, "l", A(68), "Che ruolo ha la cisteina N-terminale del dominio glutamminasico dell'amidotransferasi?", [
  "Forma un intermedio covalente con la glutammina, da cui l'NH₃ è liberata per idrolisi",
  "Lega il PRPP e ne attiva il pirofosfato prima della sostituzione con l'ammino",
  "Coordina il Mg²⁺ che stabilizza i nucleotidi legati ai siti allosterici",
  "Forma il ponte disolfuro che tiene insieme le due subunità del dimero quaternario inattivo",
  "Lega l'AMP nel sito degli amminopurinici e blocca il canale per l'ammoniaca",
  ], 0,
  "La glutammina forma un intermedio covalente con la Cys N-terminale e viene idrolizzata; l'ammoniaca percorre un canale interno fino al sito fosforibosiltransferasico, dove sostituisce il pirofosfato del PRPP.")

C = "bm9-degradazione"

q("u1127-034", C, "m", A(76), "Come viene degradato il GMP fino alla xantina?", [
  "GMP → guanosina → guanina → xantina, con la guanina deaminasi",
  "GMP → IMP → inosina → xantina, con la GMP reduttasi",
  "GMP → XMP → xantosina → xantina, con l'IMP deidrogenasi",
  "GMP → guanosina → xantosina → xantina, con l'adenosina deaminasi",
  "GMP → guanina → ipoxantina → xantina, con la xantina ossidasi",
  ], 0,
  "Una nucleotidasi forma guanosina, la purina nucleoside fosforilasi libera guanina e la guanina deaminasi toglie l'ammino dando xantina, che la xantina ossidasi trasforma in acido urico.")

q("u1127-035", C, "l", A(76), "Oltre a formare l'acido urico, che ruolo ha l'H₂O₂ prodotta dalla xantina ossidasi secondo gli appunti?", [
  "Fa da messaggero nell'attivazione di neutrofili, linfociti T e citochine",
  "Ossida un gruppo SH e trasforma stabilmente l'enzima in deidrogenasi",
  "Serve alla purina nucleoside fosforilasi per scindere i nucleosidi in base e zucchero",
  "Riossida il molibdeno dell'enzima senza bisogno dell'ossigeno",
  "Inibisce l'AMP deaminasi e rallenta il catabolismo delle purine",
  ], 0,
  "La xantina ossidasi (FAD, molibdo-pterina, due cluster 2Fe-2S) cede gli elettroni all'O₂ formando H₂O₂, che funziona anche da mediatore nelle difese dell'organismo.")

C = "bm9-salvataggio"

q("u1127-036", C, "l", A(75), "Quale mutazione dell'HGPRT inattiva l'enzima solo in parte e dà artrite gottosa anziché Lesch-Nyhan?", [
  "D134",
  "G69",
  "D193",
  "G69 insieme a D193",
  "Nessuna: ogni mutazione del sito dà Lesch-Nyhan",
  ], 0,
  "Nel sito catalitico ci sono tre residui conservati: G69 (mutata, inattivazione completa e Lesch-Nyhan), D134 (inattivazione parziale, gotta) e D193 (non lega più il Mg²⁺, inattivazione completa).")

q("u1127-037", C, "m", A(74), "Da quale molecola si forma la putrescina e con quale coenzima?", [
  "Dall'ornitina, con una decarbossilasi PLP-dipendente",
  "Dalla lisina, con una decarbossilasi TPP-dipendente",
  "Dall'arginina, con un'ossidasi FAD-dipendente",
  "Dalla metionina, con una transferasi SAM-dipendente",
  "Dall'ornitina, con una carbossilasi biotina-dipendente",
  ], 0,
  "L'ornitina decarbossilasi (PLP) forma la putrescina; la SAM decarbossilata cede gruppi propilamminici per spermidina e spermina, lasciando metiltioadenosina, da cui si recupera l'adenina.")

q("u1127-038", C, "a", A(74), "Dove avvengono di preferenza la sintesi de novo e il salvataggio delle purine?", [
  "De novo soprattutto nel fegato; salvataggio soprattutto nei tessuti extraepatici",
  "De novo soprattutto nei tessuti extraepatici; salvataggio soprattutto nel fegato",
  "Entrambe solo nel fegato, che esporta poi i nucleotidi agli altri tessuti",
  "De novo solo negli eritrociti; salvataggio in tutte le altre cellule",
  "Entrambe solo nelle cellule in divisione, mai nei tessuti differenziati",
  ], 0,
  "La sintesi de novo è soprattutto epatica; i tessuti extraepatici dipendono molto dal salvataggio, che costa meno energia. Gli eritrociti non hanno l'amidotransferasi e usano solo il salvataggio.")

# ── Pirimidine e farmaci ───────────────────────────────────────────────────
C = "bm10-sintesi"

q("u1127-039", C, "m", A(81), "Che cos'è la UMP sintasi?", [
  "Una proteina bifunzionale citosolica con orotato fosforibosiltransferasi e OMP decarbossilasi",
  "Una proteina trifunzionale citosolica che riunisce CPS II, aspartato transcarbamilasi e diidroorotasi",
  "Una flavoproteina della membrana mitocondriale interna che ossida il diidroorotato",
  "Una chinasi che fosforila due volte l'UMP formando l'UTP per la sintesi dell'RNA",
  "Un enzima che trasferisce l'ammino della glutammina sull'UTP per formare il CTP",
  ], 0,
  "Le ultime due tappe (orotato + PRPP → OMP; OMP → UMP) sono sulla UMP sintasi. Le prime tre stanno sulla proteina CAD; la diidroorotato deidrogenasi è l'unico enzima mitocondriale.")

q("u1127-040", C, "l", A(83), "Senza substrato né effettori il rapporto T/R dell'aspartato transcarbamilasi è circa 200. Che cosa succede con CTP 0,4 mM e con ATP 2 mM?", [
  "Con il CTP sale a circa 1200; con l'ATP scende a circa 70",
  "Con il CTP scende a circa 70; con l'ATP sale a circa 1200",
  "Con il CTP sale a circa 1200; con l'ATP sale a circa 400",
  "Con il CTP scende a circa 20; con l'ATP resta circa 200",
  "Con entrambi resta circa 200: cambia solo la Vmax dell'enzima",
  ], 0,
  "Il CTP stabilizza lo stato T e alza la soglia della curva sigmoide; l'ATP sposta l'equilibrio verso R. La piccola differenza di energia tra i due stati permette agli effettori di spostarlo facilmente.")

q("u1127-041", C, "a", A(82), "Oltre al controllo sulla CPS II, come agisce l'UMP sulla propria sintesi?", [
  "Inibisce l'OMP decarbossilasi, l'enzima che lo produce",
  "Attiva la CPS II, perché segnala che servono più pirimidine",
  "Inibisce la glutammina PRPP amidotransferasi delle purine",
  "Inibisce la diidroorotato deidrogenasi nel mitocondrio",
  "Attiva l'aspartato transcarbamilasi spostandola verso lo stato R",
  ], 0,
  "La CPS II è attivata da ATP e PRPP e inibita dall'UTP; l'UMP fa un feedback a breve termine sull'OMP decarbossilasi. Il CTP inibisce l'aspartato transcarbamilasi.")

C = "bm10-farmaci"

q("u1127-042", C, "h", A(88), "Le cellule di un tumore diventano resistenti insieme a più chemioterapici con bersagli diversi. Quale meccanismo è il più probabile?", [
  "Producono pompe di membrana che espellono attivamente i farmaci dalla cellula",
  "Amplificano il gene della DHF reduttasi, che il farmaco non riesce più a inibire",
  "Riducono la folil-poliglutammato sintetasi e non trattengono più il farmaco",
  "Mutano la timidilato sintasi, che non lega più il 5-fluorodeossiuridilato",
  "Perdono il trasportatore del folato, da cui entrano gli analoghi del folato",
  ], 0,
  "Le altre risposte spiegano la resistenza a un solo farmaco o a una sola classe (metotrexato, 5-fluorouracile). La resistenza multipla a farmaci non correlati si spiega con pompe che li buttano fuori dalla cellula.")

# ── Eme, bilirubina, ferro ─────────────────────────────────────────────────
C = "bm11-eme"

q("u1127-043", C, "f", A(89), "In quali cellule si sintetizza soprattutto l'eme?", [
  "Nei precursori eritroidi (circa 85%) e negli epatociti (circa 15%)",
  "Negli epatociti (circa 85%) e nei precursori eritroidi (circa 15%)",
  "Nei macrofagi della milza (circa 85%) e negli epatociti (circa 15%)",
  "Nei miociti (circa 85%) e nei precursori eritroidi (circa 15%)",
  "In parti uguali in tutte le cellule nucleate dell'organismo",
  ], 0,
  "L'85% dell'eme si forma nei precursori eritroidi per l'emoglobina; il 15% nel fegato, per citocromo P450, citocromi, perossidasi, catalasi e altri enzimi.")

q("u1127-044", C, "l", A(90), "Quale cofattore lega la porfobilinogeno deaminasi?", [
  "Un dipirrometano legato a una cisteina",
  "Un piridossal fosfato legato a una lisina",
  "Uno ione Zn²⁺ coordinato da due lisine",
  "Un FAD che ossida i ponti metilenici",
  "Un eme legato a un'istidina prossimale",
  ], 0,
  "Il dipirrometano (due porfobilinogeni) resta sull'enzima come gruppo prostetico; vi si aggiungono altri quattro porfobilinogeni, poi l'idrossimetilbilano lineare viene staccato. Lo Zn²⁺ è nella porfobilinogeno sintasi.")

C = "bm11-bilirubina"

q("u1127-045", C, "a", A(95), "Perché acidosi e alcuni farmaci come i salicilati aumentano la bilirubina non coniugata libera nel plasma?", [
  "Indeboliscono o competono per il suo legame all'albumina",
  "Inibiscono la glucuroniltransferasi microsomiale epatica",
  "Aumentano l'emolisi e la produzione di biliverdina",
  "Bloccano la secrezione della forma coniugata nella bile",
  "La rendono idrosolubile e la fanno filtrare nel rene",
  ], 0,
  "La bilirubina indiretta viaggia legata all'albumina; in acidosi il legame si indebolisce e antibiotici e salicilati competono per gli stessi siti, così ne resta di più libera e può diffondere nei tessuti.")

q("u1127-046", C, "h", A(97), "Quale abbinamento tra sindrome e difetto del metabolismo della bilirubina è corretto?", [
  "Dubin-Johnson – difetto di escrezione della bilirubina coniugata",
  "Crigler-Najjar – difetto di escrezione della bilirubina coniugata",
  "Gilbert – difetto di escrezione della bilirubina coniugata",
  "Dubin-Johnson – difetto grave di coniugazione della bilirubina",
  "Rotor – assenza completa della glucuroniltransferasi epatica",
  ], 0,
  "Crigler-Najjar: difetto di coniugazione; Gilbert: difetto di captazione e coniugazione; Dubin-Johnson e Rotor: difetto di escrezione. Nei primi due sale l'indiretta, negli ultimi due la diretta.")

C = "bm11-epcidina"

q("u1127-047", C, "m", A(103), "Quali condizioni aumentano la sintesi di epcidina?", [
  "Infiammazione, ferro sierico alto, trasfusioni o somministrazione di ferro",
  "Ipossia, anemia ed eritropoiesi stimolata dall'eritropoietina renale",
  "Digiuno prolungato, ipoglicemia e aumento del glucagone circolante",
  "Emorragia acuta, carenza di ferro e transferrina poco saturata",
  "Acidosi, ipercapnia e insufficienza respiratoria cronica",
  ], 0,
  "L'epcidina sale quando c'è ferro in abbondanza o infiammazione e trattiene il ferro nelle cellule bloccando la ferroportina. Ipossia ed eritropoiesi attiva la riducono, per rendere disponibile più ferro.")

q("u1127-048", C, "m", A(104), "Quali terapie indicano gli appunti per l'emocromatosi e per la sideropenia?", [
  "Salasso e chelanti nella prima; supplementazione di ferro nella seconda",
  "Supplementazione di ferro nella prima; salasso e chelanti nella seconda",
  "Epcidina sintetica nella prima; trasfusioni ripetute nella seconda",
  "Vitamina C ad alte dosi nella prima; chelanti del ferro nella seconda",
  "Eritropoietina nella prima; salasso e restrizione dietetica nella seconda",
  ], 0,
  "L'emocromatosi (poca epcidina, sovraccarico di ferro in fegato, pancreas e cuore) si tratta togliendo ferro; la sideropenia (ingresso ridotto o perdite aumentate) con supplementi.")

C = "bm11-ferro"

q("u1127-049", C, "h", A(104), "Una donna con mestruazioni molto abbondanti è anemica. Quale quadro di laboratorio ti aspetti?", [
  "Ferritina e saturazione della transferrina basse, globuli rossi piccoli e ipocromici",
  "Ferritina alta e transferrina molto saturata, globuli rossi grandi e normocromici",
  "Ferritina normale e saturazione alta, globuli rossi di forma e volume normali",
  "Ferritina bassa e saturazione alta, globuli rossi grandi con nuclei ipersegmentati",
  "Ferritina alta e saturazione bassa, globuli rossi a falce per polimerizzazione dell'HbS",
  ], 0,
  "Le perdite croniche danno sideropenia: depositi vuoti (ferritina bassa), transferrina poco saturata e anemia ipocromica microcitica. Ferritina alta con saturazione bassa è tipica dell'infiammazione.")

C = "bm11-cellule"

q("u1127-050", C, "m", A(103), "Come rilascia il ferro l'epatocita, a differenza dei precursori eritroidi?", [
  "Con la ferroportina, aiutata dalla ceruloplasmina che ossida il ferro esportato",
  "Con il DMT1, che esporta il Fe²⁺ dalla membrana basolaterale verso il plasma",
  "Con il recettore della transferrina, che lo restituisce al plasma per esocitosi",
  "Secernendo ferritina carica di Fe³⁺, che cede il ferro alla transferrina",
  "Non lo rilascia mai: come i precursori eritroidi lo trattiene tutto",
  ], 0,
  "L'epatocita può prendere ferro da varie fonti e rilasciarlo con la ferroportina; la ceruloplasmina ossida il Fe²⁺ per caricarlo sulla transferrina. I precursori eritroidi lo captano solo con transferrina e recettore e non hanno sistemi di secrezione.")
