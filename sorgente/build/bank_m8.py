"""Blocco 8 – Proteine e amminoacidi (sbobina di Biochimica II, p. 226–278)."""
from bank_common import q

# ── Digestione delle proteine (p. 226–232) ──────────────────────────────────
T = "m8-digestione"
q("m8d-01", T, "f", "226", "Perché le proteasi digestive vengono sintetizzate come zimogeni?", [
  "Per non digerire la cellula che le produce prima di essere secrete",
  "Per poter attraversare la membrana con un trasportatore specifico",
  "Per resistere all'acidità dello stomaco durante la secrezione",
  "Per legare il calcio necessario alla loro attività catalitica",
  "Per essere riconosciute dai recettori della mucosa intestinale",
  ], 0,
  "Si attivano solo per proteolisi, fuori dalla cellula. Un'attivazione intracellulare distrugge il pancreas (pancreatite).")
q("m8d-02", T, "f", "227", "Quale triade catalitica ha la chimotripsina?", [
  "Serina, istidina, aspartato", "Cisteina, istidina, asparagina", "Serina, lisina, glutammato", "Aspartato, aspartato, acqua", "Treonina, istidina, aspartato"], 0,
  "L'istidina prende il protone della serina, che attacca il carbonio carbonilico del legame peptidico.")
q("m8d-03", T, "f", "228", "Quali cellule producono il pepsinogeno?", [
  "Le cellule principali", "Le cellule parietali", "Le cellule G dell'antro", "Le cellule mucose del colletto", "Le cellule enterocromaffini"], 0,
  "Le cellule parietali producono HCl, le cellule G la gastrina.")
q("m8d-04", T, "m", "228", "Quale non è una funzione dell'acidità gastrica?", [
  "Attivare la tripsina", "Denaturare le proteine", "Uccidere i batteri", "Attivare il pepsinogeno", "Esporre i legami peptidici"], 0,
  "La tripsina si attiva nell'intestino (enteropeptidasi), a pH circa 8 dopo la neutralizzazione con il bicarbonato.")
q("m8d-05", T, "m", "230", "Come forma l'HCl la cellula parietale?", [
  "L'H⁺ esce con una pompa H⁺/K⁺ ATP-dipendente e il Cl⁻ lo segue; il bicarbonato va nel sangue",
  "L'H⁺ esce con un antiporto Na⁺/H⁺ e il Cl⁻ entra dal lume; il bicarbonato va nel lume gastrico",
  "L'H⁺ esce con una pompa Na⁺/K⁺ e il Cl⁻ esce con un canale; il bicarbonato resta nella cellula",
  "L'HCl si forma nel sangue e viene secreto intero per esocitosi dalla cellula parietale",
  "L'H⁺ deriva dall'idrolisi dell'ATP e il Cl⁻ dal pepsinogeno attivato nel lume",
  ], 0,
  "L'anidrasi carbonica forma H₂CO₃ → H⁺ + HCO₃⁻; il bicarbonato esce in scambio con Cl⁻. Gli inibitori di pompa (omeprazolo) bloccano la H⁺/K⁺-ATPasi.")
q("m8d-06", T, "m", "229", "Perché, secondo la sbobina, un pasto proteico ricco di grassi rallenta la digestione?", [
  "I grassi legano il cuore idrofobico delle proteine denaturate e frenano la pepsina",
  "I grassi neutralizzano l'acido cloridrico e il pepsinogeno non si attiva più",
  "I grassi inibiscono la secrezione di gastrina da parte delle cellule G",
  "I grassi stimolano la secrezione di bicarbonato e alzano troppo il pH gastrico",
  "I grassi competono con le proteine per il sito attivo della pepsina",
  ], 0,
  "Denaturando, la proteina espone il suo cuore idrofobico, che lega i lipidi.")
q("m8d-07", T, "a", "229", "Bere molta acqua durante il pasto rallenta la digestione gastrica soprattutto perché:", [
  "Diluisce la pepsina e ne abbassa la velocità massima",
  "Alza molto il pH gastrico e il pepsinogeno smette di attivarsi del tutto",
  "Inibisce la secrezione di gastrina attraverso i recettori di stiramento",
  "Diluisce i substrati e la pepsina lavora sotto la sua Km",
  "Stimola lo svuotamento gastrico prima che la pepsina agisca",
  ], 0,
  "Vmax = kcat [E]: diluire l'enzima abbassa la velocità. Un paio di bicchieri invece non cambiano molto il pH.")
q("m8d-08", T, "a", "231–232", "Secondo la sbobina, quale apporto proteico è raccomandato a un adulto di 70 kg?", [
  "Circa 56 g al giorno (0,8 g/kg)",
  "Circa 140 g al giorno (2 g/kg)",
  "Circa 105 g al giorno (1,5 g/kg)",
  "Circa 35 g al giorno (0,5 g/kg)",
  "Circa 84 g al giorno (1,2 g/kg)",
  ], 0,
  "Gli sportivi agonisti arrivano a 1–1,2 g/kg; negli anziani 0,9–1 g/kg.")
q("m8d-09", T, "l", "229", "Quale forma di gastrina è un prodotto di degradazione, secondo la sbobina?", [
  "Gastrina 14", "Gastrina 17", "Gastrina 34", "Progastrina", "Pre-progastrina"], 0,
  "Le forme funzionali sono la 34 e la 17 (numero di residui).")
q("m8d-10", T, "l", "226", "Come si chiamano le proteasi con un residuo di cisteina nel sito attivo?", [
  "Cisteinil proteasi", "Serin proteasi", "Aspartil proteasi", "Metalloproteasi", "Treonin proteasi"], 0,
  "Le quattro classi della sbobina: serin, aspartil, cisteinil e metallo proteasi.")
q("m8d-11", T, "h", "230–231", "Quale abbinamento tra secrezione e funzione nella digestione delle proteine è corretto?", [
  "Bicarbonato pancreatico – porta il pH intorno a 8, adatto alla tripsina",
  "Pepsina – taglia preferenzialmente dopo lisina e arginina, come la tripsina",
  "Gastrina – idrolizza i legami peptidici dei residui aromatici nello stomaco",
  "Amminopeptidasi – attivano il pepsinogeno nel lume gastrico",
  "HCl – attiva direttamente il tripsinogeno nel duodeno",
  ], 0,
  "La pepsina preferisce residui idrofobici; la tripsina taglia dopo Lys e Arg; gli oligopeptidi residui li finiscono le peptidasi dell'orletto a spazzola.",
  note="Sbobina di Biochimica II, p. 231: c'è scritto che la colecistochinina «favorisce il nuovo pH dell'intestino». Nei testi di riferimento è la secretina a stimolare il bicarbonato; la CCK stimola la secrezione di enzimi pancreatici e la contrazione della colecisti.")
q("m8d-12", T, "h", "232", "Che cosa succede agli amminoacidi assorbiti in eccesso rispetto al fabbisogno per la sintesi proteica?", [
  "Vengono deaminati e gli scheletri usati per energia o per fare grassi",
  "Vengono immagazzinati in proteine di riserva muscolari pronte per il digiuno",
  "Vengono eliminati intatti con le urine dal tubulo renale prossimale",
  "Restano liberi nel plasma fino al pasto successivo, in un pool di riserva",
  "Vengono trasformati tutti in glucosio e depositati come glicogeno epatico",
  ], 0,
  "Non esistono proteine di deposito: dopo il pasto gli amminoacidi liberi sono pochissimi.")

# ── Degradazione intracellulare: proteasoma e lisosomi (p. 233–238) ─────────
T = "m8-lisosomi"
q("m8l-01", T, "f", "233", "Quale residuo dell'ubiquitina forma il legame con la proteina bersaglio?", [
  "La glicina C-terminale", "La lisina 48", "La serina N-terminale", "La cisteina del sito attivo", "La metionina iniziale"], 0,
  "Il carbossile della Gly C-terminale forma un legame isopeptidico con una lisina del bersaglio; la Lys48 serve a formare le catene di ubiquitina.")
q("m8l-02", T, "f", "234", "Quanti enzimi servono per legare l'ubiquitina a una proteina?", [
  "Tre: E1, E2 ed E3", "Due: E1 ed E2", "Uno solo: l'ubiquitina ligasi", "Quattro: E1, E2, E3 e la deubiquitinasi", "Tre: E1, E2 e il proteasoma 19S"], 0,
  "Un gene per E1, pochi per E2, moltissimi per E3: è E3 a riconoscere il bersaglio.")
q("m8l-03", T, "f", "236", "A che pH lavorano le proteasi lisosomiali?", [
  "Circa 4", "Circa 7,4", "Circa 8", "Circa 2", "Circa 6,5"], 0,
  "Una pompa protonica ATP-dipendente acidifica il lisosoma.",
  note="La sbobina indica pH 4; molti testi riportano un pH lisosomiale intorno a 4,5–5.")
q("m8l-04", T, "m", "234", "Come viene attivata l'ubiquitina da E1?", [
  "ATP → ubiquitina-AMP + PPi, poi tioestere con una cisteina di E1",
  "ATP → ubiquitina fosforilata + ADP, poi l'ubiquitina passa a una serina di E1",
  "GTP → ubiquitina-GMP + PPi, poi l'ubiquitina passa a una lisina di E1",
  "L'ubiquitina viene tagliata da una proteasi e il frammento attivo si lega a E1",
  "ATP → ubiquitina-ADP + Pi, poi l'ubiquitina passa direttamente al bersaglio",
  ], 0,
  "Stessa logica dell'acil-CoA sintetasi: adenilato e poi tioestere. Il passaggio a E2 resta un tioestere.")
q("m8l-05", T, "m", "234", "Qual è il segnale che porta una proteina al proteasoma?", [
  "Almeno 4 ubiquitine legate tramite la lisina 48",
  "Una singola ubiquitina legata alla lisina N-terminale",
  "Un residuo di acido sialico esposto sulla superficie",
  "Una fosforilazione su serina da parte della PKA",
  "Un ponte disolfuro tra due cisteine vicine",
  ], 0,
  "Legame isopeptidico tra il carbossile della Gly C-terminale di un'ubiquitina e l'ε-ammino della Lys48 della successiva.")
q("m8l-06", T, "m", "235", "Come è organizzata la parte catalitica 20S del proteasoma?", [
  "4 anelli eptamerici α-β-β-α; l'attività è nelle subunità β, con una treonina catalitica",
  "4 anelli esamerici α-α-β-β; l'attività è nelle subunità α, con una serina catalitica",
  "2 anelli eptamerici β-β; l'attività è nelle subunità β, con una cisteina catalitica",
  "4 anelli eptamerici β-α-α-β; l'attività è nelle subunità α, con un'istidina catalitica",
  "Un unico anello di 28 subunità identiche, ciascuna con un aspartato catalitico",
  ], 0,
  "Il 19S (regolatore) ha ATPasi AAA che denaturano il bersaglio e una isopeptidasi che ricicla l'ubiquitina.")
q("m8l-07", T, "a", "233", "Secondo la «regola dell'N-terminale», da che cosa dipende l'emivita di una proteina?", [
  "Dal tipo di residuo N-terminale, stabilizzante o no",
  "Dalla lunghezza della catena: le proteine più lunghe durano di più",
  "Dal numero di ponti disolfuro: più ponti, emivita più breve",
  "Dal residuo C-terminale, che viene riconosciuto dal proteasoma",
  "Dalla quantità di acido sialico legato al residuo N-terminale",
  ], 0,
  "Contano anche le sequenze PEST, che accelerano la degradazione.")
q("m8l-08", T, "a", "236", "Perché il pH acido del lisosoma favorisce il rilascio delle LDL dal loro recettore?", [
  "A pH 4 si protonano gli aspartati del recettore e si perde il ponte salino",
  "A pH 4 si denatura l'ApoB-100 e il colesterolo si stacca dal recettore",
  "A pH 4 si attiva l'ACAT, che esterifica il colesterolo e lo stacca dal recettore",
  "A pH 4 il recettore viene fosforilato e perde affinità per l'ApoE",
  "A pH 4 si protonano le lisine dell'ApoB-100, che diventano negative",
  ], 0,
  "Il recettore torna in membrana, la lipoproteina viene degradata.")
q("m8l-09", T, "a", "237", "Che vantaggio ha per la cellula che le proteasi lisosomiali lavorino solo a pH acido?", [
  "Se il lisosoma si rompe, nel citosol sono poco attive",
  "Possono essere sintetizzate già attive nel reticolo endoplasmatico",
  "Non hanno bisogno di essere sintetizzate come zimogeni",
  "Possono degradare anche le proteine ubiquitinate nel citosol",
  "Funzionano anche senza la pompa protonica della membrana lisosomiale",
  ], 0,
  "È probabilmente un sistema di sicurezza contro l'autodigestione.")
q("m8l-10", T, "l", "235", "Quanti amminoacidi hanno circa i frammenti rilasciati dal proteasoma?", [
  "7–9", "2–3", "20–30", "50–60", "Un solo amminoacido"], 0,
  "Sono anche i frammenti presentati sul complesso maggiore di istocompatibilità.")
q("m8l-11", T, "l", "235", "Che cosa sono le proteine AAA del complesso 19S?", [
  "ATPasi che srotolano il bersaglio", "Proteasi a treonina", "Ubiquitina ligasi di tipo E3", "Chaperonine che ripiegano il bersaglio", "Fosfatasi che rimuovono i fosfati"], 0,
  "ATPases Associated with diverse cellular Activities: probabilmente denaturano il substrato.")
q("m8l-12", T, "h", "234", "La sbobina definisce l'unità Svedberg dicendo «maggiore è S, minore è la densità». Che cosa è corretto?", [
  "Un S maggiore indica una sedimentazione più veloce",
  "Un S maggiore indica una particella più leggera e meno densa",
  "Il valore S si somma: 20S + 19S fanno un complesso 39S",
  "Il valore S misura la carica elettrica della particella",
  "Il valore S dipende solo dalla forma, non dalla massa",
  ], 0,
  "Il coefficiente di sedimentazione cresce con massa e densità e non è additivo (il proteasoma completo è 26S).",
  note="Sbobina di Biochimica II, p. 234: c'è scritto che «maggiore è questo [S] minore è la densità». È il contrario: S maggiore = sedimentazione più veloce.")
q("m8l-13", T, "h", "237–238", "Che cosa succede nell'autofagia durante un digiuno prolungato?", [
  "Organelli e aggregati, avvolti da una doppia membrana, finiscono nei lisosomi",
  "Le proteine citosoliche vengono secrete e digerite nel lume intestinale",
  "I mitocondri vengono degradati dal proteasoma 26S dopo ubiquitinazione",
  "Le proteasi lisosomiali vengono rilasciate nel citosol per degradare le proteine",
  "I lisosomi si fondono con la membrana plasmatica e rilasciano amminoacidi",
  ], 0,
  "Il fagoforo si chiude in autofagosoma, che si fonde con il lisosoma; gli amminoacidi tornano al metabolismo.")

# ── Transaminazione, PLP, glutammato deidrogenasi (p. 239–245) ──────────────
T = "m8-transaminazione"
q("m8t-01", T, "f", "239", "Quale vitamina dà il coenzima delle transaminasi?", [
  "Vitamina B6 (piridossina)", "Vitamina B1 (tiamina)", "Vitamina B2 (riboflavina)", "Vitamina B12 (cobalamina)", "Vitamina B9 (folato)"], 0,
  "Il coenzima è il piridossal 5'-fosfato (PLP).")
q("m8t-02", T, "f", "240", "Qual è l'accettore generale dei gruppi amminici nella degradazione degli amminoacidi?", [
  "α-chetoglutarato", "Ossalacetato", "Piruvato", "Fumarato", "Glutammina"], 0,
  "Si forma glutammato, che poi viene deaminato dalla glutammato deidrogenasi.")
q("m8t-03", T, "f", "240", "Che cosa si forma dalla transaminazione tra alanina e α-chetoglutarato?", [
  "Piruvato e glutammato", "Ossalacetato e glutammato", "Piruvato e glutammina", "Lattato e aspartato", "Acetil-CoA e glutammato"], 0,
  "Ogni amminoacido diventa il suo α-chetoacido corrispondente.")
q("m8t-04", T, "m", "242", "Come è legato il PLP all'enzima a riposo?", [
  "Con una base di Schiff tra l'aldeide e una lisina",
  "Con un legame estere tra il suo fosfato e una serina dell'enzima",
  "Con un ponte disolfuro tra il PLP e una cisteina del sito attivo",
  "Con un legame ammidico tra il suo carbossile e una lisina",
  "Non è legato covalentemente: si lega solo insieme al substrato",
  ], 0,
  "Quando entra l'amminoacido si forma l'aldimmina esterna con il suo gruppo amminico.")
q("m8t-05", T, "m", "243", "Perché la transaminazione è una reazione «a ping-pong»?", [
  "Il primo prodotto esce prima che entri il secondo substrato",
  "Entrambi i substrati si legano insieme e formano un complesso ternario con l'enzima",
  "L'enzima oscilla tra forma fosforilata e defosforilata a ogni ciclo",
  "Il gruppo amminico passa avanti e indietro tra i due substrati legati",
  "Il PLP si stacca e si riattacca all'enzima a ogni ciclo catalitico",
  ], 0,
  "Alanina → piruvato (si forma PMP); poi α-chetoglutarato → glutammato (torna il PLP).")
q("m8t-06", T, "m", "244", "Che cosa catalizza la glutammato deidrogenasi?", [
  "La deaminazione ossidativa del glutammato, con NAD(P)⁺",
  "La transaminazione del glutammato con l'ossalacetato, con PLP",
  "La sintesi di glutammina dal glutammato e dall'ammoniaca, con ATP",
  "La decarbossilazione del glutammato a GABA, con PLP",
  "L'idrolisi della glutammina a glutammato e NH₄⁺, senza coenzimi",
  ], 0,
  "Avviene nei mitocondri epatici; è una delle poche reazioni che usa sia NAD⁺ sia NADP⁺.")
q("m8t-07", T, "m", "245", "Come viene regolata allostericamente la glutammato deidrogenasi?", [
  "Attivata dall'ADP, inibita dal GTP",
  "Attivata dal GTP, inibita dall'ADP",
  "Attivata dall'AMP, inibita dall'ATP",
  "Attivata dal NADH, inibita dal NAD⁺",
  "Attivata dal glutammato, inibita dall'ammoniaca",
  ], 0,
  "ADP alto = serve energia: anche gli amminoacidi vengono ossidati. GTP alto (dalla succinil-CoA sintetasi) = ciclo di Krebs a pieno regime.")
q("m8t-08", T, "a", "245", "La somma di transaminazione e glutammato deidrogenasi si chiama transdeaminazione. Qual è il bilancio per l'alanina?", [
  "Alanina + NAD⁺ + H₂O → piruvato + NADH + NH₄⁺",
  "Alanina + α-chetoglutarato → piruvato + glutammato",
  "Alanina + NADH → lattato + NAD⁺ + NH₄⁺",
  "Alanina + ATP + NH₃ → glutammina + ADP",
  "Alanina + O₂ → piruvato + H₂O₂ + NH₄⁺",
  ], 0,
  "L'α-chetoglutarato si consuma e si riforma: il risultato netto è un'ossidazione con liberazione di ammonio.")
q("m8t-09", T, "a", "243", "Perché le transaminasi non sono un buon marker precoce di infarto?", [
  "Aumentano nel sangue solo 24–48 ore dopo l'evento",
  "Non sono presenti nel tessuto cardiaco",
  "Aumentano solo nelle epatiti virali",
  "Vengono degradate subito dal proteasoma plasmatico",
  "Sono identiche a quelle muscolari e non si distinguono",
  ], 0,
  "Marker precoci sono CK-MB e troponina. Le transaminasi restano ottimi indici di danno epatico.")
q("m8t-10", T, "a", "241", "Perché la reazione dell'aspartato transaminasi (Asp + α-KG → OAA + Glu) viene definita anaplerotica?", [
  "Perché produce ossalacetato, un intermedio del ciclo di Krebs",
  "Perché consuma α-chetoglutarato e svuota il ciclo di Krebs",
  "Perché produce ATP con una fosforilazione a livello del substrato",
  "Perché libera ammoniaca nel mitocondrio epatico",
  "Perché è irreversibile e controlla il flusso del ciclo",
  ], 0,
  "Le transaminasi hanno ruoli energetici, glucogenetici e anaplerotici.")
q("m8t-11", T, "l", "242", "Quale intermedio si forma nel meccanismo della transaminasi dopo la perdita dell'H⁺ dall'aldimmina esterna?", [
  "Intermedio chinonoide", "Chetimmina", "Aldimmina interna", "Piridossammina fosfato", "Carbinolammina"], 0,
  "Aldimmina esterna → chinonoide → chetimmina → idrolisi: α-chetoacido + PMP.")
q("m8t-12", T, "l", "240", "Oltre agli enzimi del metabolismo amminoacidico, quale enzima usa il PLP secondo la sbobina?", [
  "Glicogeno fosforilasi", "Piruvato carbossilasi", "Transchetolasi", "Acetil-CoA carbossilasi", "Glucosio 6-fosfatasi"], 0,
  "Nella fosforilasi il fosfato del PLP partecipa come acido/base nella fosforolisi.")
q("m8t-13", T, "h", "244", "La sbobina dice che la glutammato deidrogenasi è «presente esclusivamente nel mitocondrio delle cellule epatiche», ma poco dopo che serve anche nel cervello. Come va inteso?", [
  "Nel fegato serve all'ureogenesi; nel cervello riforma soprattutto glutammato",
  "Nel cervello esiste una glutammato deidrogenasi citosolica che usa solo FAD",
  "Il cervello riceve la glutammato deidrogenasi dal fegato attraverso il sangue",
  "Nel cervello la reazione è catalizzata dalla glutammina sintetasi, non dalla GDH",
  "È un errore: la GDH è solo cerebrale e il fegato usa le transaminasi",
  ], 0,
  "La GDH è presente in molti tessuti; nel fegato il suo ruolo è fornire NH₄⁺ al ciclo dell'urea.",
  note="Sbobina di Biochimica II, p. 244: le due frasi si contraddicono. La GDH non è esclusiva del fegato; la sbobina enfatizza il ruolo epatico.")
q("m8t-14", T, "h", "241", "Quale affermazione sulle transaminasi è corretta?", [
  "Lavorano solo sugli L-amminoacidi",
  "Eliminano il gruppo amminico come ammoniaca libera",
  "Usano NAD⁺ per ossidare l'amminoacido ad α-chetoacido",
  "Sono attive solo nel fegato e nel rene",
  "Formano sempre aspartato come prodotto finale",
  ], 0,
  "Trasferiscono il gruppo amminico senza eliminarlo; a staccarlo come NH₄⁺ è la GDH.",
  note="Sbobina di Biochimica II, p. 241: si dice che esistono 20 transaminasi, una per ogni amminoacido. È una semplificazione: alcune transaminasi accettano più substrati e alcuni amminoacidi (es. lisina, treonina) non vengono transaminati.")

# ── Ciclo dell'urea e destino dell'ammoniaca (p. 246–254) ───────────────────
T = "m8-urea"
q("m8u-01", T, "f", "246", "Quale enzima organica l'ammoniaca all'inizio del ciclo dell'urea?", [
  "Carbamil fosfato sintetasi I", "Carbamil fosfato sintetasi II", "Ornitina transcarbamilasi", "Glutammina sintetasi", "Arginasi"], 0,
  "NH₄⁺ + HCO₃⁻ + 2 ATP → carbamil fosfato. È mitocondriale ed epatica.")
q("m8u-02", T, "f", "249", "Quale enzima libera l'urea?", [
  "Arginasi", "Argininosuccinato liasi", "Ornitina transcarbamilasi", "Ureasi", "Argininosuccinato sintetasi"], 0,
  "Arginina + H₂O → urea + ornitina, che rientra nel mitocondrio.")
q("m8u-03", T, "f", "246", "Come elimina l'azoto in eccesso l'uomo?", [
  "Come urea (ureotelico)", "Come ammoniaca (ammoniotelico)", "Come acido urico (uricotelico)", "Come creatinina soprattutto", "Come glutammina nelle feci"], 0,
  "L'uomo produce acido urico dalle purine, ma è poco solubile: in eccesso dà gotta.")
q("m8u-04", T, "m", "248–249", "Da dove vengono i due atomi di azoto dell'urea?", [
  "Uno dall'NH₄⁺, l'altro dall'aspartato",
  "Entrambi dall'NH₄⁺ liberato dalla glutammato deidrogenasi",
  "Uno dalla glutammina e l'altro dall'asparagina",
  "Uno dall'ornitina e l'altro dalla citrullina",
  "Entrambi dall'arginina della dieta",
  ], 0,
  "Ma l'aspartato prende il suo azoto dal glutammato per transaminazione: alla fine il glutammato è il donatore di entrambi.")
q("m8u-05", T, "m", "247", "Quale molecola attiva allostericamente la carbamil fosfato sintetasi I?", [
  "N-acetilglutammato", "Arginina", "Ornitina", "ATP", "Glutammina"], 0,
  "Lo forma l'N-acetilglutammato sintasi (glutammato + acetil-CoA), che a sua volta è attivata dall'arginina.")
q("m8u-06", T, "m", "248", "Quale differenza tra CPS I e CPS II è corretta?", [
  "CPS I: mitocondrio epatico, NH₄⁺, ciclo dell'urea. CPS II: citosol, glutammina, pirimidine",
  "CPS I: citosol, glutammina, pirimidine. CPS II: mitocondrio epatico, NH₄⁺, ciclo dell'urea",
  "CPS I: mitocondrio, glutammina, purine. CPS II: citosol, NH₄⁺, ciclo dell'urea",
  "CPS I: tutti i tessuti, NH₄⁺, pirimidine. CPS II: solo fegato, glutammina, urea",
  "Sono lo stesso enzima in due compartimenti, con gli stessi regolatori",
  ], 0,
  "CPS I attivata da N-acetilglutammato; CPS II attivata da ATP e inibita da UTP.")
q("m8u-07", T, "m", "248", "In quale ordine lavorano gli enzimi del ciclo dell'urea dopo la CPS I?", [
  "Ornitina transcarbamilasi → argininosuccinato sintetasi → argininosuccinato liasi → arginasi",
  "Argininosuccinato sintetasi → ornitina transcarbamilasi → arginasi → argininosuccinato liasi",
  "Arginasi → ornitina transcarbamilasi → argininosuccinato liasi → argininosuccinato sintetasi",
  "Ornitina transcarbamilasi → arginasi → argininosuccinato sintetasi → argininosuccinato liasi",
  "Argininosuccinato liasi → argininosuccinato sintetasi → ornitina transcarbamilasi → arginasi",
  ], 0,
  "Citrullina (mitocondrio) → esce → argininosuccinato (con Asp e ATP) → arginina + fumarato → urea + ornitina.")
q("m8u-08", T, "a", "250", "Quanti legami ad alta energia costa la sintesi di una molecola di urea?", [
  "4: due per la CPS I e due per l'argininosuccinato sintetasi",
  "3: un ATP per ciascuno dei tre enzimi citosolici del ciclo",
  "2: solo i due ATP della carbamil fosfato sintetasi I",
  "6: due ATP per ciascuna delle tre reazioni che consumano energia",
  "1: l'argininosuccinato sintetasi, perché la CPS I usa il GTP",
  ], 0,
  "3 ATP, ma uno perde due legami fosfoanidridici (il PPi viene idrolizzato).")
q("m8u-09", T, "a", "251–252", "Come sono collegati ciclo dell'urea e ciclo di Krebs?", [
  "Il fumarato diventa ossalacetato, che transaminato rigenera aspartato",
  "Il citrato del ciclo di Krebs cede il suo azoto alla citrullina per formare arginina",
  "L'α-chetoglutarato del ciclo di Krebs viene carbossilato per formare carbamil fosfato",
  "Il succinil-CoA del ciclo di Krebs fornisce il gruppo carbamilico all'ornitina",
  "L'ossalacetato viene trasformato direttamente in ornitina nel mitocondrio",
  ], 0,
  "È lo shunt aspartato-argininosuccinato.")
q("m8u-10", T, "a", "252–253", "Come arriva al fegato l'ammoniaca prodotta nei tessuti periferici?", [
  "Come glutammina, che la glutamminasi epatica scinde",
  "Come ammoniaca libera legata all'albumina, che la cede agli epatociti",
  "Come urea, già sintetizzata nei tessuti periferici e solo filtrata dal fegato",
  "Come carbamil fosfato, prodotto dalla CPS II di tutte le cellule",
  "Come aspartato, che il fegato deamina con la glutammato deidrogenasi",
  ], 0,
  "Dal muscolo arriva anche come alanina (ciclo glucosio-alanina).")
q("m8u-11", T, "a", "253", "Di notte il rene usa la glutammina proveniente dal fegato. A che cosa serve?", [
  "Libera NH₄⁺ nelle urine e rigenera bicarbonato contro l'acidosi",
  "Forma urea con la glutamminasi renale, perché il rene ha un ciclo dell'urea completo",
  "Forma glutammato che il rene secerne come neurotrasmettitore",
  "Fornisce azoto per sintetizzare creatinina e acido urico",
  "Viene ossidata a CO₂ per fornire tutta l'energia al tubulo prossimale",
  ], 0,
  "L'α-chetoglutarato residuo va in gluconeogenesi renale, che produce bicarbonato.",
  note="Sbobina di Biochimica II, p. 253: c'è scritto che nel rene la glutammina viene metabolizzata dalla glutamminasi «e si forma urea». Il rene non sintetizza urea: libera NH₄⁺, che viene escreto come tale.")
q("m8u-12", T, "a", "254", "Perché l'iperammoniemia danneggia il cervello? Indica il meccanismo descritto dalla sbobina.", [
  "Per smaltire NH₄⁺ i neuroni sottraggono α-chetoglutarato al ciclo di Krebs",
  "L'ammoniaca inibisce la glicolisi bloccando l'esochinasi neuronale",
  "L'ammoniaca si lega all'emoglobina e riduce il trasporto di ossigeno al cervello",
  "L'ammoniaca blocca il recettore dell'insulina e il glucosio non entra nei neuroni",
  "L'ammoniaca forma urea nel cervello, che richiama acqua e causa edema",
  ], 0,
  "Altri meccanismi: troppo glutammato (e GABA) alterano la trasmissione; l'NH₃ attraversa le membrane.")
q("m8u-13", T, "l", "248", "Come si chiama l'amminoacido non proteico che esce dal mitocondrio nel ciclo dell'urea?", [
  "Citrullina", "Ornitina", "Argininosuccinato", "Carbamil fosfato", "Omoserina"], 0,
  "Ornitina + carbamil fosfato → citrullina (ornitina transcarbamilasi).")
q("m8u-14", T, "l", "254", "Qual è il range normale dell'ammoniaca nel sangue indicato dalla sbobina?", [
  "5–50 µmol/L", "5–50 mmol/L", "0,5–5 µmol/L", "50–500 µmol/L", "1–2 mol/L"], 0,
  "Sopra questi valori l'ammoniaca supera la barriera ematoencefalica e dà tremori, sonnolenza, edema cerebrale, fino al coma.")
q("m8u-15", T, "h", "254", "Quale intervento è indicato dalla sbobina per ridurre l'ammoniaca in un paziente con iperammoniemia?", [
  "Dieta ipoproteica e lassativi contro i batteri intestinali",
  "Dieta iperproteica per fornire più arginina al ciclo dell'urea",
  "Somministrazione di ureasi per trasformare l'urea in ammoniaca nel fegato",
  "Digiuno prolungato per attivare la gluconeogenesi da amminoacidi",
  "Inibitori di pompa protonica per alzare il pH gastrico",
  ], 0,
  "Meno proteine = meno NH₄⁺ dagli amminoacidi; meno batteri = meno NH₃ da ureasi intestinale.")
q("m8u-16", T, "h", "247–249", "Un neonato ha iperammoniemia grave con citrullina plasmatica molto bassa. Quale enzima è più probabilmente difettoso?", [
  "Ornitina transcarbamilasi",
  "Argininosuccinato sintetasi",
  "Argininosuccinato liasi",
  "Arginasi",
  "Glutamminasi renale",
  ], 0,
  "Se manca un enzima a monte della citrullina, la citrullina non si forma. Nei difetti a valle (sintetasi) la citrullina si accumula.",
  note="Il ragionamento sui metaboliti accumulati non è nella sbobina, che dice solo che i difetti del ciclo dell'urea danno iperammoniemia nelle prime settimane e ritardo mentale.")

# ── Destino degli scheletri carboniosi e sintesi (p. 255–258) ──────────────
T = "m8-scheletri"
q("m8s-01", T, "f", "257", "Quali amminoacidi sono esclusivamente chetogenetici?", [
  "Leucina e lisina", "Alanina e serina", "Isoleucina e fenilalanina", "Glutammato e aspartato", "Valina e metionina"], 0,
  "Danno solo acetil-CoA o acetoacetil-CoA, che non possono diventare glucosio.")
q("m8s-02", T, "f", "255", "Quale amminoacido trasporta azoto e scheletro carbonioso dal muscolo al fegato di notte?", [
  "Alanina", "Glutammato", "Lisina", "Leucina", "Glicina"], 0,
  "Ciclo glucosio-alanina: nel fegato l'alanina dà piruvato per la gluconeogenesi.")
q("m8s-03", T, "f", "258", "Da quale intermedio della glicolisi deriva la serina?", [
  "3-fosfoglicerato", "Piruvato", "Diidrossiacetone fosfato", "Fosfoenolpiruvato", "Glucosio 6-fosfato"], 0,
  "3-P-glicerato → (NAD⁺) 3-fosfoidrossipiruvato → (transaminazione) 3-fosfoserina → serina.")
q("m8s-04", T, "m", "255", "Come favorisce il cortisolo la gluconeogenesi da amminoacidi?", [
  "Induce ubiquitina ligasi E3 nel muscolo e accelera la proteolisi",
  "Inibisce il proteasoma muscolare e libera gli amminoacidi già presenti",
  "Attiva le proteasi lisosomiali del fegato, che digeriscono l'albumina",
  "Blocca la transaminazione nel muscolo e fa uscire gli amminoacidi intatti",
  "Stimola la secrezione di glucagone, che scinde direttamente l'actina",
  ], 0,
  "Agisce come fattore di trascrizione attraverso il suo recettore.")
q("m8s-05", T, "m", "255", "Nel muscolo che cosa succede ai gruppi amminici degli amminoacidi liberati dalle proteine?", [
  "Passano al glutammato e poi al piruvato: escono come alanina",
  "Vengono liberati come NH₄⁺ dalla glutammato deidrogenasi muscolare",
  "Formano urea con il ciclo dell'urea muscolare",
  "Vengono trasferiti all'ossalacetato ed escono come aspartato",
  "Restano sugli amminoacidi, che escono intatti nel sangue",
  ], 0,
  "Il muscolo non ha la GDH: l'NH₄⁺ non viene liberato (la sbobina avverte che le figure su questo sono sbagliate).")
q("m8s-06", T, "m", "256", "Qual è la reazione anaplerotica del muscolo secondo la sbobina?", [
  "Il ciclo dei nucleotidi purinici, che produce fumarato",
  "La piruvato carbossilasi: piruvato → ossalacetato",
  "L'enzima malico: piruvato → malato",
  "La glutammato deidrogenasi: glutammato → α-chetoglutarato",
  "La propionil-CoA carbossilasi: propionil-CoA → succinil-CoA",
  ], 0,
  "L'AMP deaminasi libera NH₄⁺ (smaltito come glutammina); l'aspartato si lega all'IMP con GTP; il fumarato rifornisce il ciclo.")
q("m8s-07", T, "a", "255", "Da dove viene il piruvato che il muscolo transamina ad alanina durante la notte?", [
  "Dalla glicolisi del glicogeno muscolare, stimolata dall'AMP",
  "Dal lattato del sangue, riossidato dalla LDH muscolare",
  "Dalla β-ossidazione degli acidi grassi, che produce piruvato",
  "Dalla gluconeogenesi muscolare, attivata dal glucagone",
  "Dalla degradazione dei corpi chetonici nel mitocondrio",
  ], 0,
  "L'acil-CoA sintetasi libera AMP, che attiva la fosforilasi b (T → R). Il glicogeno muscolare non risponde al glucagone.")
q("m8s-08", T, "a", "257", "Perché isoleucina e fenilalanina sono sia glucogenetiche sia chetogenetiche?", [
  "Lo scheletro si divide: una parte dà acetil-CoA, l'altra un intermedio di Krebs",
  "Possono essere transaminate con due diversi α-chetoacidi a seconda del tessuto",
  "Il fegato le usa per la gluconeogenesi e il cervello per i corpi chetonici",
  "Danno piruvato, che può diventare sia ossalacetato sia acetil-CoA",
  "Vengono prima convertite in leucina, che è glucogenetica e chetogenetica",
  ], 0,
  "Fenilalanina → fumarato + acetoacetil-CoA; isoleucina → succinil-CoA + acetil-CoA.")
q("m8s-09", T, "a", "256", "A quale intermedio del metabolismo convergono glutammina, prolina, arginina e istidina?", [
  "Glutammato", "Piruvato", "Succinil-CoA", "Fumarato", "Acetoacetil-CoA"], 0,
  "Alanina, serina, cisteina, treonina, glicina e triptofano convergono invece sul piruvato.")
q("m8s-10", T, "l", "258", "Quale enzima forma l'asparagina dall'aspartato, e con quale prodotto secondario?", [
  "Asparagina sintetasi, con formazione di AMP", "Asparaginasi, con formazione di NH₄⁺", "Aspartato transaminasi, con formazione di glutammato", "Glutammina sintetasi, con formazione di ADP", "Asparagina sintetasi, con formazione di GDP"], 0,
  "L'ATP viene scisso in AMP + PPi.")
q("m8s-11", T, "l", "256", "Come si chiama il composto che si forma unendo IMP e aspartato nel ciclo dei nucleotidi purinici?", [
  "Adenilosuccinato", "Argininosuccinato", "Succinil-AMP", "Aspartil-IMP", "Fumaril-AMP"], 0,
  "La reazione usa GTP; la scissione dell'adenilosuccinato libera fumarato e AMP.")
q("m8s-12", T, "h", "257", "La sbobina dice che «metionina, valina e isoleucina, amminoacidi a catena ramificata» convergono sul succinil-CoA. Che cosa è corretto?", [
  "Convergono sul succinil-CoA, ma la metionina non è ramificata",
  "Convergono sull'acetil-CoA, e sono tutti e tre a catena ramificata",
  "Convergono sul fumarato, e la valina non è a catena ramificata",
  "Convergono sull'ossalacetato, e l'isoleucina è solo chetogenetica",
  "Convergono sul piruvato, e la metionina è a catena ramificata",
  ], 0,
  "Anche la treonina contribuisce al succinil-CoA (via propionil-CoA).",
  note="Sbobina di Biochimica II, p. 257: la metionina è inclusa tra gli amminoacidi a catena ramificata. I ramificati sono valina, leucina e isoleucina, come dice la stessa sbobina a p. 262.")
q("m8s-13", T, "h", "255", "Perché il ciclo glucosio-alanina è vantaggioso rispetto al solo ciclo di Cori?", [
  "Porta al fegato anche l'azoto, destinato al ciclo dell'urea",
  "Produce più ATP nel muscolo perché l'alanina non richiede NADH per formarsi",
  "Non richiede la gluconeogenesi epatica perché l'alanina diventa direttamente glucosio",
  "Funziona anche senza fegato, perché il rene può usare l'alanina",
  "Evita la glicolisi muscolare, che di notte è completamente spenta",
  ], 0,
  "Il ciclo di Cori riporta solo carbonio (lattato); quello dell'alanina anche i gruppi amminici.")

# ── Difetti del metabolismo amminoacidico (p. 258–263) ──────────────────────
T = "m8-difetti"
q("m8x-01", T, "f", "260", "Quale enzima è carente nella forma più frequente di fenilchetonuria?", [
  "Fenilalanina idrossilasi", "Tirosina idrossilasi", "Omogentisato 1,2-diossigenasi", "Tirosinasi", "Fenilalanina transaminasi"], 0,
  "Altre cause: difetti di sintesi o di rigenerazione della tetraidrobiopterina.")
q("m8x-02", T, "f", "261", "Che cosa caratterizza l'alcaptonuria?", [
  "Urine scure e artrite delle grandi articolazioni",
  "Urine con odore di sciroppo d'acero e ritardo mentale",
  "Calcoli renali di cistina e coliche ricorrenti",
  "Fotosensibilità e sintomi simili alla pellagra",
  "Assenza di melanina in cute, capelli e occhi",
  ], 0,
  "Manca l'omogentisato 1,2-diossigenasi, nella degradazione di fenilalanina e tirosina.")
q("m8x-03", T, "f", "262", "Quali amminoacidi sono coinvolti nella malattia delle urine a sciroppo d'acero?", [
  "Valina, leucina e isoleucina", "Fenilalanina e tirosina", "Cistina, lisina, arginina e ornitina", "Triptofano e istidina", "Metionina e cisteina"], 0,
  "Manca il complesso deidrogenasico degli α-chetoacidi a catena ramificata.")
q("m8x-04", T, "m", "260", "Perché nella PKU la tirosina diventa essenziale?", [
  "Perché la tirosina si forma solo dalla fenilalanina",
  "Perché la tirosina viene tutta trasformata in fenilpiruvato nella PKU",
  "Perché la tirosina viene eliminata con le urine insieme al fenillattato",
  "Perché la tirosina inibisce la fenilalanina idrossilasi residua",
  "Perché la tirosina serve a sintetizzare la tetraidrobiopterina",
  ], 0,
  "Dalla fenilalanina si ricava tirosina, non il contrario.")
q("m8x-05", T, "m", "261", "Quali metaboliti si accumulano nelle urine nella PKU?", [
  "Fenilpiruvato e fenillattato", "Omogentisato e benzochinone acetato", "α-chetoacidi a catena ramificata", "Cistina e ornitina", "Acido urico e xantina"], 0,
  "La fenilalanina in eccesso viene transaminata a fenilpiruvato, che dà fenillattato e fenilacetato.")
q("m8x-06", T, "m", "262", "Perché un difetto della E3 del complesso degli α-chetoacidi ramificati è più grave di uno della E1?", [
  "Perché la E3 è in comune con PDH e α-chetoglutarato DH",
  "Perché la E3 contiene la TPP, che è necessaria anche alla transchetolasi",
  "Perché la E3 è l'unico enzima che riconosce la leucina",
  "Perché la E3 è codificata dal DNA mitocondriale",
  "Perché senza E3 si accumula ammoniaca nel fegato",
  ], 0,
  "E1 riconosce gli α-chetoacidi ramificati, E2 il loro acile; la E3 (diidrolipoil deidrogenasi) è la stessa nei tre complessi.")
q("m8x-07", T, "a", "261", "Perché lo screening della PKU si fa nei primi giorni di vita, anche se alla nascita il bambino può sembrare sano?", [
  "Perché prima della nascita la fenilalanina in eccesso la smaltisce la madre",
  "Perché la fenilalanina idrossilasi si inattiva solo dopo alcune settimane di vita",
  "Perché alla nascita il bambino non ha ancora proteine plasmatiche che contengano fenilalanina",
  "Perché i sintomi neurologici compaiono solo dopo la mielinizzazione completa",
  "Perché il latte materno contiene un inibitore della fenilalanina idrossilasi",
  ], 0,
  "La dieta controllata va mantenuta tutta la vita: anche da adulti la fenilalanina alta abbassa il quoziente intellettivo.")
q("m8x-08", T, "a", "259", "Perché la malattia di Hartnup dà sintomi simili alla pellagra?", [
  "Si assorbe poco triptofano, da cui si forma una parte della niacina",
  "Manca la fenilalanina idrossilasi e la tirosina non forma niacina",
  "Il triptofano si accumula e inibisce l'assorbimento intestinale della niacina",
  "Manca il trasportatore della niacina nel rene e nell'intestino",
  "Il triptofano viene tutto trasformato in serotonina e ne resta poco per le proteine",
  ], 0,
  "Si cura dando nicotinammide.")
q("m8x-09", T, "a", "259", "Nella cistinuria, quali amminoacidi non vengono riassorbiti nel tubulo prossimale?", [
  "Cistina e amminoacidi basici", "Solo la cistina", "Amminoacidi neutri, triptofano compreso", "Amminoacidi ramificati", "Amminoacidi acidi (aspartato, glutammato)"], 0,
  "La cistina è poco solubile e precipita in calcoli che ostruiscono le vie urinarie.")
q("m8x-10", T, "l", "261", "Quale enzima della sintesi della melanina manca nell'albinismo?", [
  "Tirosinasi", "Fenilalanina idrossilasi", "Tirosina idrossilasi", "Dopa decarbossilasi", "Omogentisato ossidasi"], 0,
  "La tirosinasi dei melanociti ossida la tirosina a DOPA e dopachinone.",
  note="Sbobina di Biochimica II, p. 261: l'enzima è chiamato «tirosina monoossigenasi» e l'albinismo è attribuito alla «via di degradazione della fenilalanina». L'enzima è la tirosinasi, e la melanina si forma in una via di sintesi, non di degradazione.")
q("m8x-11", T, "l", "260", "Quale enzima rigenera la tetraidrobiopterina dopo la reazione della fenilalanina idrossilasi?", [
  "Diidropteridina reduttasi", "Diidrofolato reduttasi", "Biopterina sintasi", "Pterina-4a-carbinolammina deidratasi da sola", "Tetraidrofolato deidrogenasi"], 0,
  "La riduzione usa NAD(P)H. La BH₄ si sintetizza dal GTP: non è una vitamina.",
  note="Sbobina di Biochimica II, p. 260: l'enzima è chiamato «diidrobiopterina reduttasi» e il coenzima indicato è il NADPH. Il nome corretto è diidropteridina reduttasi; nel Lehninger usa NADH.")
q("m8x-12", T, "h", "260", "La sbobina dice che il fumarato prodotto dalla degradazione della fenilalanina «può essere considerato chetogenetico». Che cosa è corretto?", [
  "Il fumarato è glucogenetico; chetogenetico è l'acetoacetato",
  "Il fumarato è chetogenetico: diventa acetil-CoA attraverso la fumarasi",
  "Il fumarato non è né glucogenetico né chetogenetico, perché viene escreto",
  "Il fumarato è chetogenetico perché nel fegato forma direttamente acetoacetato",
  "Il fumarato è glucogenetico solo nel rene, chetogenetico nel fegato",
  ], 0,
  "Per questo la fenilalanina è sia glucogenetica sia chetogenetica.",
  note="Sbobina di Biochimica II, p. 260: il fumarato è definito chetogenetico perché forma ossalacetato. Formare ossalacetato significa proprio essere glucogenetico.")
q("m8x-13", T, "h", "262", "In quali complessi enzimatici si trova la tiamina pirofosfato, secondo la sbobina?", [
  "PDH, α-chetoglutarato DH, BCKDH e transchetolasi",
  "Piruvato DH, piruvato carbossilasi, propionil-CoA carbossilasi e transchetolasi",
  "Piruvato DH, glutammato DH, α-chetoglutarato DH e transaldolasi",
  "Solo piruvato DH e α-chetoglutarato DH",
  "Transaminasi, decarbossilasi e glicogeno fosforilasi",
  ], 0,
  "Le carbossilasi usano biotina; transaminasi, decarbossilasi e fosforilasi usano PLP.")

# ── Folato, SAM, omocisteina, B12 (p. 263–272) ─────────────────────────────
T = "m8-folato"
q("m8f-01", T, "f", "263", "Da quali tre parti è formato l'acido folico?", [
  "Pteridina, PABA, glutammato", "Pteridina, ribosio, adenina", "Pirimidina, tiazolo, pirofosfato", "Isoallossazina, ribitolo, fosfato", "Corrina, cobalto, deossiadenosina"], 0,
  "Non sappiamo sintetizzare il PABA: il folato va assunto con la dieta.")
q("m8f-02", T, "f", "264", "Quale enzima forma il tetraidrofolato?", [
  "Diidrofolato reduttasi (NADPH)", "Timidilato sintasi", "Serina idrossimetiltransferasi", "Metionina sintasi", "Folilpoliglutammato sintetasi"], 0,
  "THF è il donatore di unità monocarboniose; gli azoti attivi sono N5 e N10.")
q("m8f-03", T, "f", "268", "Quale vitamina serve alla metionina sintasi?", [
  "Vitamina B12", "Vitamina B6", "Vitamina C", "Biotina", "Riboflavina"], 0,
  "È la seconda reazione B12-dipendente della sbobina, dopo la metilmalonil-CoA mutasi.")
q("m8f-04", T, "m", "264", "Perché la cellula aggiunge fino a circa 10 glutammati al folato?", [
  "Le cariche negative lo trattengono nella cellula",
  "I glutammati sono il gruppo che trasporta le unità monocarboniose",
  "I glutammati legano la vitamina B12 per la metionina sintasi",
  "Serve a trasportare il folato nel nucleo per la sintesi del DNA",
  "Serve a proteggere il folato dalla diidrofolato reduttasi",
  ], 0,
  "È uno dei motivi per cui il fabbisogno è basso.")
q("m8f-05", T, "m", "265", "Come si carica il THF con l'unità monocarboniosa a partire dalla serina?", [
  "La serina idrossimetiltransferasi dà glicina + N5,N10-metilen-THF",
  "La serina idrossilasi trasferisce un metile: serina → alanina + N5-metil-THF",
  "La serina transaminasi trasferisce un formile: serina → piruvato + N10-formil-THF",
  "La serina deidratasi trasferisce un CH: serina → piruvato + N5,N10-metenil-THF",
  "La serina decarbossilasi trasferisce CO₂: serina → etanolammina + formil-THF",
  ], 0,
  "Anche l'enzima di scissione della glicina carica il THF come metilen-THF, liberando NH₄⁺ e CO₂.")
q("m8f-06", T, "m", "267", "Come si forma la S-adenosilmetionina?", [
  "Metionina + ATP, con perdita di tutti e tre i fosfati",
  "Metionina + ADP: l'adenosina si lega al carbossile e si libera un fosfato",
  "Omocisteina + N5-metil-THF: il metile si lega allo zolfo",
  "Metionina + acetil-CoA: l'acetile si lega all'azoto",
  "Cisteina + ATP: l'adenosina si lega al gruppo tiolico",
  ], 0,
  "Dopo aver donato il metile diventa S-adenosilomocisteina; un'idrolasi stacca l'adenosina e resta l'omocisteina.")
q("m8f-07", T, "m", "268", "Che cosa catalizza la cistationina β-sintasi?", [
  "Omocisteina + serina → cistationina",
  "Cistationina → cisteina + α-chetobutirrato",
  "Omocisteina + N5-metil-THF → metionina",
  "Metionina + ATP → S-adenosilmetionina",
  "Cisteina + glutammato → γ-glutamilcisteina",
  ], 0,
  "Poi la cistationina liasi (PLP) libera cisteina, α-chetobutirrato e NH₄⁺. La carenza della sintasi dà omocistinuria.")
q("m8f-08", T, "a", "270", "Che cos'è la «trappola dei folati»?", [
  "Senza B12 il folato resta bloccato come N5-metil-THF",
  "Senza folato la B12 si accumula come metilcobalamina e non può essere usata dalla mutasi",
  "Senza B6 la serina non carica il THF e il folato resta come diidrofolato",
  "L'eccesso di folato satura la diidrofolato reduttasi e blocca la sintesi del DNA",
  "Il folato viene intrappolato nel fegato legato alla proteina R e non circola",
  ], 0,
  "La metilen-THF reduttasi è irreversibile: la carenza di B12 diventa una carenza funzionale di folato, con anemia megaloblastica.")
q("m8f-09", T, "a", "270", "Perché trattare con solo folato un'anemia megaloblastica da carenza di B12 è pericoloso?", [
  "Corregge l'anemia ma non ferma i danni neurologici",
  "Peggiora l'anemia perché il folato compete con la B12 per il fattore intrinseco",
  "Causa omocistinuria perché il folato inibisce la cistationina β-sintasi",
  "Blocca la sintesi del DNA perché il folato inibisce la timidilato sintasi",
  "Non ha effetti, perché senza B12 il folato non viene assorbito",
  ], 0,
  "L'anemia della B12 si chiama perniciosa proprio per i sintomi neuropsichiatrici (atassia, perdita di sensibilità).")
q("m8f-10", T, "a", "269", "Quali carenze possono far aumentare l'omocisteina plasmatica?", [
  "B12, folato o cistationina β-sintasi", "Vitamina C, vitamina D o ferro", "Biotina, tiamina o niacina", "Vitamina K, vitamina E o zinco", "Ferro, rame o vitamina A"], 0,
  "B12 e folato servono alla rimetilazione a metionina; la cistationina β-sintasi alla trasformazione in cisteina (con B6).")
q("m8f-11", T, "a", "270", "Perché la carenza di folato in gravidanza aumenta il rischio di spina bifida?", [
  "Senza folato si sintetizza poco DNA e la divisione cellulare rallenta",
  "Il folato serve alla sintesi del collagene, necessario alla chiusura del tubo neurale",
  "Il folato serve alla mielinizzazione dei neuroni del midollo spinale",
  "Il folato serve all'assorbimento del calcio per le vertebre fetali",
  "Il folato serve a produrre la melatonina che regola lo sviluppo del midollo",
  ], 0,
  "Per questo alle donne in gravidanza si dà un integratore di folato.")
q("m8f-12", T, "l", "270", "Quale mutazione frequente della metilen-THF reduttasi descrive la sbobina?", [
  "Alanina → valina, che facilita la perdita del FAD", "Glutammato → valina, che causa polimerizzazione", "Glicina → serina, che blocca il NADPH", "Arginina → cisteina, che forma ponti disolfuro", "Valina → alanina, che aumenta la Km per il folato"], 0,
  "È un polimorfismo diffuso; un apporto maggiore di folato stabilizza l'enzima.")
q("m8f-13", T, "l", "270", "Quali proteine servono all'assorbimento della vitamina B12?", [
  "Proteina R e fattore intrinseco", "Transferrina e ferritina", "Albumina e transtiretina", "Fattore intrinseco e ceruloplasmina", "Proteina R e lattoferrina"], 0,
  "La quantità di fattore intrinseco limita l'assorbimento; le scorte epatiche bastano per circa tre anni.")
q("m8f-14", T, "h", "264", "Come agiscono i sulfamidici?", [
  "Bloccano la sintesi del folato, che i batteri producono da sé",
  "Inibiscono la diidrofolato reduttasi umana e batterica allo stesso modo",
  "Inibiscono la timidilato sintasi batterica legandosi al dUMP",
  "Bloccano l'assorbimento intestinale del folato alimentare",
  "Sequestrano la vitamina B12 necessaria ai batteri",
  ], 0,
  "Noi assumiamo il folato con la dieta; i batteri devono sintetizzarlo.",
  note="La sbobina dice che i sulfamidici inibiscono la sintesi del PABA. Più precisamente, sono analoghi del PABA e inibiscono la diidropteroato sintasi, l'enzima che lo incorpora nel folato.")
q("m8f-15", T, "h", "263, 271", "Quale confronto tra folato e vitamina B12 è coerente con la sbobina?", [
  "Folato: da vegetali, termolabile. B12: da batteri, serve il fattore intrinseco",
  "Folato: solo da carne, termostabile. B12: sintetizzata dalle piante, assorbita senza proteine",
  "Folato: sintetizzato dall'uomo dal PABA. B12: sintetizzata dall'uomo dal cobalto",
  "Folato: assorbito con il fattore intrinseco. B12: trattenuta con la poliglutammazione",
  "Folato: fabbisogno di grammi. B12: fabbisogno di milligrammi",
  ], 0,
  "Fabbisogni nell'ordine dei microgrammi per entrambe.",
  note="La sbobina indica un fabbisogno di folato di circa 200 µg/die; le raccomandazioni attuali per l'adulto sono circa 400 µg/die.")

# ── Vie specializzate degli amminoacidi (p. 272–278) ────────────────────────
T = "m8-vie"
q("m8v-01", T, "f", "273", "Da quale amminoacido derivano le catecolammine?", [
  "Tirosina", "Triptofano", "Istidina", "Glutammato", "Arginina"], 0,
  "Tirosina → L-DOPA → dopamina → noradrenalina → adrenalina.")
q("m8v-02", T, "f", "274", "Quale amminoacido dà il GABA?", [
  "Glutammato", "Glicina", "Aspartato", "Glutammina", "Alanina"], 0,
  "Glutammato decarbossilasi (PLP). Il GABA è il principale neurotrasmettitore inibitorio del SNC.")
q("m8v-03", T, "f", "274", "Da quale amminoacido derivano serotonina e melatonina?", [
  "Triptofano", "Tirosina", "Fenilalanina", "Istidina", "Serina"], 0,
  "Triptofano → 5-idrossitriptofano → serotonina → N-acetilserotonina → melatonina.")
q("m8v-04", T, "m", "273", "Quali cofattori servono nella sintesi dell'adrenalina, nell'ordine delle reazioni?", [
  "BH₄ e O₂ → PLP → ascorbato e O₂ → S-adenosilmetionina",
  "PLP → BH₄ e O₂ → S-adenosilmetionina → ascorbato e O₂",
  "Ascorbato e O₂ → PLP → BH₄ e O₂ → S-adenosilmetionina",
  "BH₄ e O₂ → ascorbato e O₂ → PLP → N5-metil-THF",
  "NADPH → PLP → FAD → S-adenosilmetionina",
  ], 0,
  "Tirosina idrossilasi, dopa decarbossilasi, dopamina β-idrossilasi, feniletanolammina N-metiltransferasi.")
q("m8v-05", T, "m", "273", "Dove si ferma la sintesi delle catecolammine nei diversi tessuti?", [
  "SNC: dopamina; ortosimpatico: noradrenalina; midollare del surrene: adrenalina",
  "SNC: adrenalina; ortosimpatico: dopamina; midollare del surrene: noradrenalina",
  "SNC: noradrenalina; ortosimpatico: adrenalina; midollare del surrene: dopamina",
  "Ovunque fino all'adrenalina, che poi viene demetilata nei tessuti",
  "SNC: L-DOPA; ortosimpatico: dopamina; corticale del surrene: adrenalina",
  ], 0,
  "La metilazione noradrenalina → adrenalina avviene nella midollare del surrene.")
q("m8v-06", T, "m", "266", "Che cosa decide quale legame del carbonio α viene rotto da un enzima a PLP?", [
  "La proteina, che orienta perpendicolare all'anello del PLP il legame da rompere",
  "Il pH del compartimento in cui si trova l'enzima",
  "La forma del PLP: piridossale per le decarbossilasi, piridossammina per le transaminasi",
  "Il numero di gruppi fosfato legati al piridossale",
  "Il metallo legato al sito attivo dell'enzima",
  ], 0,
  "Transaminasi: H del Cα; decarbossilasi: COO⁻; serina idrossimetiltransferasi: catena laterale.")
q("m8v-07", T, "a", "274", "Perché un inibitore suicida della GABA transaminasi riduce le crisi epilettiche?", [
  "Blocca la degradazione del GABA, che così aumenta",
  "Blocca la sintesi del glutammato, riducendo l'eccitazione neuronale",
  "Aumenta la sintesi di serotonina a partire dal triptofano",
  "Inibisce la glutammato decarbossilasi e riduce il GABA in eccesso",
  "Attiva i recettori del GABA legandosi al loro sito allosterico",
  ], 0,
  "L'epilessia può dipendere da poca sintesi o da troppa degradazione di GABA.")
q("m8v-08", T, "a", "275", "Come è stato sfruttato l'enzima ornitina decarbossilasi contro la malattia del sonno?", [
  "Un inibitore suicida lo blocca in entrambi, ma nell'uomo l'enzima si rinnova in fretta",
  "Un inibitore competitivo lo blocca solo nel parassita, perché l'enzima umano non lega l'ornitina",
  "Un attivatore lo stimola nel parassita, che accumula poliammine tossiche e muore",
  "Un anticorpo lo neutralizza nel sangue, dove il parassita lo secerne",
  "Un analogo dell'ornitina lo blocca nell'uomo, privando il parassita delle poliammine dell'ospite",
  ], 0,
  "Senza poliammine (spermidina, spermina) il parassita non si divide. È un esempio di come l'emivita delle proteine guida la farmacologia.",
  note="Sbobina di Biochimica II, p. 275: si parla dell'ornitina decarbossilasi «della mosca». L'enzima a emivita lunga è quello del parassita (il tripanosoma), che la mosca trasmette; più avanti la sbobina stessa parla del parassita.")
q("m8v-09", T, "a", "276", "Come si forma la creatina?", [
  "Glicina + arginina → guanidinoacetato, poi metilazione con SAM",
  "Glicina + succinil-CoA → aminolevulinato, poi condensazione con arginina",
  "Arginina + ornitina → citrullina, poi metilazione con N5-metil-THF",
  "Serina + metionina → cistationina, poi fosforilazione con ATP",
  "Glutammina + aspartato → carbamil aspartato, poi metilazione",
  ], 0,
  "La creatina chinasi la fosforila vicino al mitocondrio, usando l'ATP appena uscito dalla traslocasi.")
q("m8v-10", T, "l", "273", "Quale vitamina serve alla dopamina β-idrossilasi?", [
  "Vitamina C", "Vitamina B6", "Vitamina B12", "Vitamina E", "Vitamina K"], 0,
  "Dopamina + O₂ + ascorbato → noradrenalina.")
q("m8v-11", T, "l", "276", "Quali molecole si condensano nel primo passaggio della sintesi dell'eme?", [
  "Succinil-CoA e glicina", "Acetil-CoA e glicina", "Succinil-CoA e serina", "Glicina e arginina", "Fumarato e glutammato"], 0,
  "Si forma δ-aminolevulinato, poi porfobilinogeno.")
q("m8v-12", T, "l", "275", "Da quale amminoacido derivano le poliammine spermidina e spermina?", [
  "Ornitina", "Lisina", "Arginina", "Metionina", "Glutammina"], 0,
  "Ornitina decarbossilasi → putrescina; la SAM decarbossilata fornisce i gruppi amminopropilici.")
q("m8v-13", T, "h", "274–275", "Quale affermazione sulle ammine biogene è corretta secondo la sbobina?", [
  "Istamina, GABA e serotonina si formano per decarbossilazione",
  "La melatonina si forma dalla serotonina per idrossilazione con BH₄",
  "L'istamina deriva dal triptofano per decarbossilazione",
  "La serotonina viene prodotta solo nel SNC, non in periferia",
  "Il GABA si forma dal glutammato per transaminazione",
  ], 0,
  "La melatonina si forma per acetilazione e metilazione (SAM); la serotonina è prodotta anche dalle piastrine; l'istamina deriva dall'istidina.")
q("m8v-14", T, "h", "278", "Oltre al ruolo metabolico, quale funzione regolatoria del rapporto acetil-CoA/CoA ricorda la sbobina?", [
  "Influenza l'acetilazione degli istoni e quindi l'espressione genica",
  "Controlla la fosforilazione dei recettori tirosina chinasici",
  "Regola la velocità della catena respiratoria legandosi al complesso I",
  "Determina l'emivita delle proteine tramite il residuo N-terminale",
  "Regola il pH del lisosoma attivando la pompa protonica",
  ], 0,
  "Un metabolita può fare da segnale per la regolazione del metabolismo stesso.")
