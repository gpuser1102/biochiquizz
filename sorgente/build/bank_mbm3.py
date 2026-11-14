"""Biologia molecolare – glucagone (lezione 5), adrenalina, istamina, volemia e recettori intracellulari (lezione 6),
vitamina D, vista, olfatto, gusto e introduzione ai nucleotidi (lezione 7)."""
from bank_common import q as _q

S = "Biologia molecolare"
L5, L6, L7 = "lezione 5", "lezione 6", "lezione 7"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Glucagone (lezione 5) ───────────────────────────────────────────────────
T = "bm5-glucagone"
q("bg5-01", T, "f", L5, "Quanti amminoacidi ha il glucagone e quali cellule lo producono?", [
  "29, cellule α delle isole", "51, cellule β delle isole", "29, cellule δ delle isole", "14, cellule α delle isole", "84, cellule delle paratiroidi"], 0,
  "È un polipeptide secreto in ipoglicemia, come pro-glucagone, e agisce soprattutto sul fegato.")
q("bg5-02", T, "f", L5, "Che tipo di recettore ha il glucagone?", [
  "Un recettore a 7 eliche accoppiato a Gs",
  "Un recettore tirosina chinasi dimerico",
  "Un recettore nucleare con dita di zinco",
  "Un recettore con attività guanilato ciclasica",
  "Un canale ionico che lascia entrare Ca²⁺",
  ], 0,
  "Gs → adenilato ciclasi → cAMP → PKA.")
q("bg5-03", T, "m", L5, "Nel fegato, come agisce la PKA attivata dal glucagone sul metabolismo del glicogeno?", [
  "Attiva la fosforilasi chinasi e inattiva la glicogeno sintasi",
  "Inattiva la fosforilasi chinasi e attiva la glicogeno sintasi",
  "Attiva direttamente la PP1, che defosforila la fosforilasi",
  "Fosforila la fosforilasi b sulla serina 14 senza intermediari",
  "Attiva sia la glicogeno sintasi sia la glicogeno fosforilasi",
  ], 0,
  "Fosforila anche l'inibitore della PP1, che così sottrae la fosfatasi ai suoi bersagli.")
q("bg5-04", T, "m", L5, "Quale residuo della glicogeno fosforilasi viene fosforilato per passare dalla forma b alla forma a?", [
  "Serina 14 di ogni monomero", "Serina 32 di ogni monomero", "Tirosina 14 di un solo monomero", "Treonina 197 del dimero", "Lisina 680 legata al PLP"], 0,
  "La serina 32 è quella dell'enzima tandem fosforilata dalla PKA.")
q("bg5-05", T, "m", L5, "Come abbassa il glucagone il fruttosio 2,6-bisfosfato?", [
  "La PKA fosforila l'enzima tandem e accende la fosfatasi",
  "La PKA defosforila l'enzima tandem e spegne la chinasi",
  "La PKA fosforila la PFK1 e ne blocca il sito allosterico",
  "La PKA degrada l'enzima tandem attraverso il proteasoma",
  "La PKA inibisce la fosfoesoso isomerasi e riduce il F6P",
  ], 0,
  "Con meno F2,6BP la PFK1 rallenta e la fruttosio 1,6-bisfosfatasi si sblocca: parte la gluconeogenesi.")
q("bg5-06", T, "a", L5, "Perché tra le isoforme della piruvato chinasi solo la L è regolata dal glucagone?", [
  "Perché solo il fegato fa gluconeogenesi per la glicemia",
  "Perché solo il fegato ha recettori per l'insulina sulla membrana",
  "Perché l'isoforma muscolare non lega il fosfoenolpiruvato",
  "Perché l'isoforma L è l'unica che contiene serine",
  "Perché l'isoforma muscolare è inibita solo dall'ATP",
  ], 0,
  "Fosforilata dalla PKA, la PK-L è inattiva: il PEP non torna a piruvato.")
q("bg5-07", T, "a", L5, "Quale effetto non appartiene al glucagone secondo la lezione?", [
  "Stimola la glicogenosintesi epatica",
  "Stimola la chetogenesi",
  "Stimola l'assunzione di amminoacidi",
  "Inibisce la glicolisi epatica",
  "Stimola la gluconeogenesi",
  ], 0,
  "Ha emivita breve e viene inattivato nel fegato.")
q("bg5-08", T, "l", L5, "In quale forma viene sintetizzato il glucagone?", [
  "Pro-glucagone", "Pre-pro-insulina", "Pro-opiomelanocortina", "Peptide C", "Glicentina matura"], 0,
  "Il taglio del pro-glucagone libera il peptide di 29 residui.")
q("bg5-09", T, "h", L5, "Durante un pasto, come cambiano insulina e glucagone e perché?", [
  "L'insulina sale e il glucagone scende",
  "Entrambi salgono per gestire il carico di glucosio",
  "Insulina scende e glucagone sale per stimolare la glicogenolisi",
  "Entrambi scendono finché il glucosio non entra nelle cellule",
  "Insulina sale solo dopo che il glucagone ha esaurito il glicogeno",
  ], 0,
  "Agiscono in modo opposto sugli stessi enzimi (glicogeno, glicolisi/gluconeogenesi). Anche glucagone e somatostatina regolano la secrezione di insulina.")

# ── Adrenalina e istamina (lezione 6) ───────────────────────────────────────
T = "bm6-adrenalina"
q("ba6-01", T, "f", L6, "Quali cofattori usa la tirosina idrossilasi?", [
  "BH₄ e Fe²⁺", "PLP e Mg²⁺", "Ascorbato e Cu⁺", "SAM e Zn²⁺", "FAD e NADH"], 0,
  "Ascorbato e rame servono alla dopamina β-idrossilasi; la SAM alla metiltransferasi (PNMT).")
q("ba6-02", T, "f", L6, "Da quale amminoacido deriva l'istamina?", [
  "Istidina", "Triptofano", "Tirosina", "Arginina", "Glutammato"], 0,
  "Istidina decarbossilasi (PLP).")
q("ba6-03", T, "m", L6, "Quale recettore dell'istamina regola la secrezione gastrica e con quale proteina G?", [
  "H2, con una Gs", "H1, con una Gq", "H3, con una Gi", "H4, con una Gi", "H2, con una Gq"], 0,
  "Gli anti-H2 (ranitidina, cimetidina) riducono l'acidità; gli anti-H1 (loratadina, cetirizina) sono antiallergici.")
q("ba6-04", T, "m", L6, "Quale effetto ha l'adrenalina sui recettori α dei vasi intestinali, cutanei e renali?", [
  "Costrizione delle arteriole e meno sangue a quegli organi",
  "Dilatazione delle arteriole e più sangue a quegli organi",
  "Aumento della permeabilità capillare e formazione di edema",
  "Rilassamento della muscolatura liscia tramite cGMP",
  "Nessun effetto, perché quei vasi hanno solo recettori β",
  ], 0,
  "Tutti gli effetti convergono sullo stesso fine: rifornire i muscoli scheletrici in condizioni di stress.")
q("ba6-05", T, "m", L6, "Secondo la lezione, quante molecole di cAMP e di PKA attiva una singola molecola di adrenalina?", [
  "Circa 40 cAMP, che attivano circa 10 PKA",
  "Circa 10 cAMP, che attivano circa 40 PKA",
  "Circa 40 cAMP, che attivano circa 40 PKA",
  "Circa 2 cAMP, che attivano una PKA",
  "Circa 4 cAMP, che attivano 4 PKA",
  ], 0,
  "Servono 4 cAMP per liberare le due subunità catalitiche. Poi 100 fosforilasi chinasi, 1000 fosforilasi, 10.000 glucosio 1-P: amplificazione a cascata.")
q("ba6-06", T, "a", L6, "Che cosa differenzia la risposta del fegato e quella del muscolo all'adrenalina?", [
  "Il fegato libera glucosio; il muscolo lo usa per sé",
  "Il fegato attiva la glicolisi; il muscolo fa gluconeogenesi",
  "Il fegato sintetizza glicogeno; il muscolo lo degrada",
  "Il fegato non risponde all'adrenalina, solo al glucagone",
  "Il muscolo libera glucosio grazie alla glucosio 6-fosfatasi",
  ], 0,
  "In entrambi la cascata cAMP–PKA–fosforilasi chinasi degrada il glicogeno; cambia il destino del G6P.")
q("ba6-07", T, "a", L6, "Come produce calore il tessuto adiposo bruno stimolato dalla noradrenalina?", [
  "Gli acidi grassi aprono la termogenina e i protoni rientrano",
  "Gli acidi grassi bloccano l'ATP sintasi e la catena si ferma",
  "La PKA fosforila il complesso IV e ne aumenta la velocità",
  "La termogenina pompa protoni fuori dalla matrice consumando ATP",
  "I nucleotidi citosolici aprono la termogenina e liberano calore",
  ], 0,
  "La termogenina è un canale per H⁺ della membrana interna, tenuto chiuso dai nucleotidi: il gradiente si dissipa come calore.")
q("ba6-08", T, "a", L6, "Che cosa distingue un antagonista da un agonista di un recettore ormonale?", [
  "Si lega allo stesso recettore ma non attiva la risposta",
  "Si lega a un altro recettore e attiva una risposta opposta",
  "Degrada l'ormone naturale prima che raggiunga il recettore",
  "Si lega al recettore con affinità sempre più bassa dell'ormone",
  "Attiva il recettore più a lungo dell'ormone naturale",
  ], 0,
  "I β-bloccanti (es. practololo) sono antagonisti dei recettori β; l'isoproterenolo è un agonista più affine dell'adrenalina.")
q("ba6-09", T, "l", L6, "Come si chiama l'enzima che converte la noradrenalina in adrenalina?", [
  "Feniletanolammina N-metiltransferasi (PNMT)", "Catecol-O-metiltransferasi (COMT)", "Dopamina β-idrossilasi", "Decarbossilasi degli L-amminoacidi aromatici", "Monoammino ossidasi (MAO)"], 0,
  "Usa la S-adenosilmetionina come donatore di metile.")
q("ba6-10", T, "l", L6, "Quale metallo usa la dopamina β-idrossilasi?", [
  "Rame", "Ferro", "Zinco", "Molibdeno", "Cobalto"], 0,
  "Il Cu⁺ si ossida a Cu²⁺ durante la reazione e l'ascorbato lo riduce.")
q("ba6-11", T, "h", L6, "Quale affermazione sull'inattivazione e sui recettori dell'istamina è corretta?", [
  "Si inattiva per metilazione o deaminazione; H4 usa una Gi",
  "Si inattiva per fosforilazione; H1 è accoppiato a una Gs",
  "Si inattiva per acetilazione; H2 è accoppiato a una Gq",
  "Si inattiva per idrossilazione; H3 è un canale ionico",
  "Non viene inattivata ma riassorbita; H4 è accoppiato a una Gs",
  ], 0,
  "H1: Gq/PLC (bronchi, allergie); H2: Gs/cAMP (stomaco); H3: SNC; H4: midollo, milza, granulociti (Gi).",
  note="Sbobina di Biologia molecolare, lezione 6: l'enzima della metilazione è chiamato «istidina N-metil transferasi». Il substrato è l'istamina: si chiama istamina N-metiltransferasi.")
q("ba6-12", T, "h", L6, "Nella lezione si legge che glucagone e insulina, attivando l'adenilato ciclasi, aumentano il cAMP in fegato e muscolo. Che cosa è corretto?", [
  "Si intende glucagone e adrenalina; l'insulina abbassa il cAMP",
  "Sono insulina e adrenalina ad attivare l'adenilato ciclasi nel fegato",
  "Il glucagone agisce sul muscolo come sul fegato attraverso il cAMP",
  "L'insulina attiva l'adenilato ciclasi solo nel muscolo scheletrico",
  "Nessuno dei tre ormoni modifica il cAMP nel fegato",
  ], 0,
  "Il muscolo non ha recettori per il glucagone; l'insulina attiva la fosfodiesterasi del cAMP.",
  note="Sbobina di Biologia molecolare, lezione 6: nel confronto fegato/muscolo c'è scritto «gli ormoni (glucagone e insulina) che agiscono attivando l'adenilato ciclasi». Si intende glucagone (fegato) e adrenalina (fegato e muscolo).")

# ── Vasopressina (lezione 6) ────────────────────────────────────────────────
T = "bm6-vasopressina"
q("bv6-01", T, "f", L6, "Dove viene sintetizzata la vasopressina?", [
  "Nei nuclei dell'ipotalamo", "Nella neuroipofisi", "Nella corticale del surrene", "Nei miociti atriali", "Nelle cellule iuxtaglomerulari"], 0,
  "Viaggia lungo gli assoni fino alla neuroipofisi, che la immette in circolo.")
q("bv6-02", T, "m", L6, "Come porta la vasopressina l'acquaporina sulla membrana del tubulo?", [
  "Gs → cAMP → PKA ancorata da AKAP alle vescicole",
  "Gq → IP₃ → Ca²⁺ fa fondere le vescicole con acquaporina",
  "Recettore nucleare → più trascrizione del gene dell'acquaporina",
  "Recettore guanilato ciclasi → PKG fosforila l'acquaporina",
  "JAK/STAT → STAT trasporta l'acquaporina sulla membrana",
  ], 0,
  "Le AKAP localizzano la PKA in membrana e sulle vescicole.")
q("bv6-03", T, "m", L6, "Perché l'alcol aumenta la diuresi?", [
  "Riduce la vasopressina",
  "Stimola la secrezione di aldosterone",
  "Blocca i recettori dell'ANP",
  "Aumenta il numero di acquaporine",
  "Inibisce la renina",
  ], 0,
  "Meno vasopressina, meno riassorbimento di acqua.")
q("bv6-04", T, "a", L6, "Dopo un'emorragia importante, che cosa fa la vasopressina?", [
  "Viene liberata in quantità e fa riassorbire più acqua",
  "Viene soppressa per far eliminare il sodio in eccesso",
  "Viene degradata dall'ANP liberato dall'atrio",
  "Blocca il sistema renina-angiotensina-aldosterone",
  "Aumenta la diuresi per ridurre la viscosità del sangue",
  ], 0,
  "I barocettori sentono il calo di pressione; gli osmocettori l'aumento della concentrazione salina.")
q("bv6-05", T, "l", L6, "Quale proteina ancora la PKA vicino alle vescicole con acquaporina?", [
  "AKAP", "Calmodulina", "Arrestina", "Clatrina", "Hsp90"], 0,
  "A-kinase anchoring protein.")
q("bv6-06", T, "h", L6, "Vasopressina e ANP hanno effetti opposti sulla volemia. Quale coppia di meccanismi è corretta?", [
  "Vasopressina: GPCR e cAMP. ANP: guanilato ciclasi e cGMP",
  "Vasopressina: recettore guanilato ciclasi, cGMP. ANP: GPCR, cAMP",
  "Vasopressina: recettore nucleare. ANP: recettore tirosina chinasi",
  "Entrambi: GPCR accoppiati a Gs e cAMP",
  "Entrambi: recettori nucleari con dita di zinco",
  ], 0,
  "L'ANP aumenta filtrazione ed escrezione di acqua e Na⁺ e inibisce la renina.")

# ── Peptide natriuretico atriale (lezione 6) ────────────────────────────────
T = "bm6-anp"
q("bn6-01", T, "f", L6, "Chi secerne l'ANP?", [
  "I miociti dell'atrio", "Le cellule iuxtaglomerulari", "La neuroipofisi", "La corticale del surrene", "Le cellule α del pancreas"], 0,
  "Lo secernono quando aumentano volume ematico, sali o pressione.")
q("bn6-02", T, "f", L6, "Quanti amminoacidi ha l'ANP attivo?", [
  "28", "9", "50", "8", "84"], 0,
  "Due cisteine formano un ponte disolfuro: la molecola ha una forma ad anello («lazo»).",
  note="La lezione dice che il precursore ha 50 amminoacidi; nei testi di riferimento il pro-ANP ne ha 126. Non sono sicuro di come sia stato detto a lezione.")
q("bn6-03", T, "m", L6, "Com'è fatto il recettore dell'ANP?", [
  "Un dimero di membrana con attività guanilato ciclasi",
  "Un recettore a 7 eliche accoppiato a una Gs",
  "Una guanilato ciclasi solubile che lega l'NO",
  "Un recettore nucleare con dita di zinco",
  "Un canale cationico aperto dal cGMP",
  ], 0,
  "Ha la stessa architettura dei recettori tirosina chinasi, ma produce cGMP. La guanilato ciclasi per l'NO è invece intracellulare.")
q("bn6-04", T, "a", L6, "Quali effetti ha l'ANP sul rene?", [
  "Più filtrazione, meno Na⁺ riassorbito, meno renina",
  "Meno filtrazione, più riassorbimento di Na⁺, più renina",
  "Più acquaporine e meno escrezione di acqua",
  "Più aldosterone e più riassorbimento di sodio",
  "Nessun effetto renale: agisce solo sui vasi",
  ], 0,
  "Antagonizza vasopressina e aldosterone; il cGMP blocca anche la sintesi di aldosterone.")
q("bn6-05", T, "h", L6, "Quale effetto del cGMP prodotto dall'ANP è citato nella lezione a proposito dell'aldosterone?", [
  "Ne blocca sintesi e secrezione",
  "Ne aumenta la sintesi attivando la PKA nella corticale",
  "Ne aumenta la degradazione nel fegato",
  "Ne blocca il recettore nel tubulo distale",
  "Lo converte in cortisolo nella corticale",
  ], 0,
  "L'angiotensina II stimola l'aldosterone tramite PLC e PKC; l'ANP lo frena.")

# ── Sistema renina-angiotensina-aldosterone e ACE2 (lezioni 6–7) ───────────
T = "bm6-raa"
q("br6-01", T, "f", L6, "Che cosa fa la renina?", [
  "Taglia l'angiotensinogeno in angiotensina I",
  "Taglia l'angiotensina I in angiotensina II",
  "Taglia l'angiotensina II in angiotensina III",
  "Sintetizza aldosterone nella corticale",
  "Degrada la bradichinina nel polmone",
  ], 0,
  "È una proteasi attivata dall'ipotensione.")
q("br6-02", T, "m", L6, "Con quale via l'angiotensina II stimola la sintesi di aldosterone?", [
  "GPCR → PLC → PKC", "GPCR → Gs → PKA", "Recettore nucleare", "Recettore guanilato ciclasi → PKG", "JAK/STAT"], 0,
  "La PKC aumenta la sintesi degli enzimi della via dell'aldosterone.")
q("br6-03", T, "m", L6, "Che cosa fa l'aldosterone nella cellula del tubulo?", [
  "Lega un recettore intracellulare e aumenta i canali del Na⁺",
  "Lega un GPCR e apre i canali del Na⁺ tramite il cAMP",
  "Lega un recettore guanilato ciclasi e inibisce il riassorbimento di Na⁺",
  "Entra nel nucleo e reprime il gene della Na⁺/K⁺-ATPasi",
  "Fosforila direttamente le acquaporine sulla membrana",
  ], 0,
  "Più sodio riassorbito, più pressione: l'effetto opposto dell'ANP.")
q("br6-04", T, "a", L6, "Secondo la lezione di Biologia molecolare, quale è il ruolo dell'angiotensina III?", [
  "È attiva come l'angiotensina II nello stimolare l'aldosterone",
  "È un prodotto inattivo della degradazione dell'angiotensina II",
  "È il precursore dell'angiotensina I nel fegato",
  "È un inibitore dell'enzima di conversione dell'angiotensina",
  "È il recettore dell'angiotensina II sulla corticale",
  ], 0,
  "Si forma togliendo l'Asp N-terminale dall'angiotensina II.",
  note="Le due sbobine non sono d'accordo: Biochimica II (p. 303) definisce l'angiotensina III inattiva, Biologia molecolare (lezione 6) attiva. Nei testi di riferimento l'angiotensina III conserva attività (stimola l'aldosterone): è corretta la versione di Biologia molecolare.")
q("br6-05", T, "a", L7, "Come entra SARS-CoV-2 nella cellula?", [
  "S1 lega ACE2; S2 viene processata dalla TMPRSS2",
  "S1 lega TMPRSS2; S2 lega ACE2 e avvia l'endocitosi",
  "La spike lega il recettore dell'angiotensina II e lo attiva",
  "La furina lega ACE2 e trasporta il virus nel citosol",
  "ACE2 taglia la spike e il virus entra per diffusione",
  ], 0,
  "La furina taglia la spike in S1 e S2. Bersagli terapeutici: anticorpi contro ACE2, ACE2 solubile, inibitori di TMPRSS2.")
q("br6-06", T, "l", L6, "Di quanti amminoacidi è fatta l'angiotensina II?", [
  "8", "7", "10", "9", "28"], 0,
  "L'angiotensina I ne ha 10; l'ACE toglie i due C-terminali.",
  note="Sbobina di Biologia molecolare, lezione 6: l'angiotensina II è descritta come un peptide «dall'Asp alla Pro (costituito da 7 aa)». È un ottapeptide (Asp-Arg-Val-Tyr-Ile-His-Pro-Phe).")
q("br6-07", T, "l", L6, "Quale enzima converte l'angiotensina I in angiotensina II?", [
  "ACE", "ACE2", "Renina", "Furina", "Aminopeptidasi A"], 0,
  "ACE2 è una carbossipeptidasi che inattiva l'angiotensina II ed è il recettore di SARS-CoV-2.",
  note="Sbobina di Biologia molecolare, lezione 6: attribuisce la conversione all'«ACE2». È l'ACE; l'ACE2 degrada l'angiotensina II (come dice la sbobina di Biochimica II, p. 303).")
q("br6-08", T, "h", L6, "Quali farmaci agiscono sul sistema renina-angiotensina-aldosterone per abbassare la pressione?", [
  "ACE-inibitori e antagonisti dell'aldosterone",
  "Statine, fibrati, ezetimibe",
  "Inibitori di pompa protonica e anti-H2",
  "Sulfoniluree e insulina",
  "Glicosidi cardiaci e agonisti β",
  ], 0,
  "Gli ACE-inibitori impediscono anche la degradazione della bradichinina, un vasodilatatore.",
  note="L'elenco dei farmaci è nella sbobina di Biochimica II (p. 303), non in quella di Biologia molecolare.")

# ── Ormoni idrofobici e recettori intracellulari (lezione 6) ───────────────
T = "bm6-idrofobici"
q("bi6-01", T, "f", L6, "Quale di questi ormoni non è steroideo ma ha un recettore intracellulare?", [
  "T3", "Cortisolo", "Aldosterone", "Estradiolo", "Vitamina D3"], 0,
  "Anche l'acido retinoico è un ormone idrofobico non steroideo.")
q("bi6-02", T, "f", L6, "Che motivo di legame al DNA hanno i recettori degli ormoni steroidei?", [
  "Dita di zinco di tipo Cys4", "Dita di zinco di tipo Cys2-His2", "Elica-giro-elica", "Cerniera di leucine", "Foglietto β a forcina"], 0,
  "Il dominio è di 66–68 residui e lega il solco maggiore.")
q("bi6-03", T, "m", L6, "Quale proteina tiene inattivo il recettore steroideo in assenza dell'ormone?", [
  "Una Hsp", "La calmodulina", "La β-arrestina", "L'IκBα", "La proteina AKAP"], 0,
  "Lega il dominio C-terminale e quello di legame al DNA; l'ormone la fa staccare.")
q("bi6-04", T, "m", L6, "Come entra il colesterolo nel mitocondrio per la steroidogenesi?", [
  "Con la proteina StAR, indotta dalla PKA",
  "Con la carnitina, come gli acidi grassi",
  "Per diffusione semplice attraverso le due membrane",
  "Con il recettore per le LDL della membrana interna",
  "Legato alla transcortina, che lo porta nella matrice",
  ], 0,
  "La PKA attiva anche l'idrolasi degli esteri del colesterolo. Nel mitocondrio la desmolasi (P450) forma pregnenolone.")
q("bi6-05", T, "m", L6, "Perché gli effetti genomici degli steroidi richiedono ore?", [
  "Perché devono essere sintetizzate nuove proteine",
  "Perché l'ormone si libera lentamente dalla transcortina",
  "Perché il recettore deve essere prima fosforilato",
  "Perché l'ormone deve essere attivato nel fegato",
  "Perché l'ormone deve legare un GPCR prima di entrare",
  ], 0,
  "Esistono anche effetti non genomici rapidi (minuti), mediati dalla membrana.")
q("bi6-06", T, "a", L6, "Perché il cortisolo lascia la transcortina e si lega al suo recettore?", [
  "Il recettore lo lega con affinità circa 100 volte maggiore",
  "La transcortina viene degradata appena entra nella cellula",
  "Il recettore fosforila la transcortina e la fa staccare",
  "Il cortisolo viene ossidato e perde affinità per la transcortina",
  "La transcortina entra nel nucleo insieme al cortisolo",
  ], 0,
  "Transcortina ≈ 10⁷ M⁻¹; recettore ≈ 10⁹ M⁻¹.")
q("bi6-07", T, "a", L6, "Come riducono l'infiammazione i glucocorticoidi tramite NF-κB?", [
  "Inducono IκBα, che trattiene NF-κB nel citosol",
  "Fosforilano NF-κB e lo mandano al proteasoma",
  "Si legano a NF-κB nel citosol e ne impediscono la sintesi",
  "Bloccano la PLC e quindi l'attivazione di NF-κB",
  "Aumentano la COX-2, che degrada NF-κB",
  ], 0,
  "Il recettore con l'ormone può anche legare NF-κB già nel nucleo e bloccarlo.")
q("bi6-08", T, "a", L6, "Che cosa fa l'annessina A1 indotta dai glucocorticoidi?", [
  "Inibisce la fosfolipasi A2",
  "Inibisce la COX-1 e riduce il muco gastrico",
  "Attiva la fosfolipasi C e libera IP₃",
  "Lega l'acido arachidonico e lo trasporta al nucleo",
  "Attiva NF-κB e la sintesi di interleuchine",
  ], 0,
  "I glucocorticoidi riducono anche l'espressione della COX-2 e la sintesi di interleuchine e interferone.")
q("bi6-09", T, "l", L6, "Quale sequenza consenso riconosce il recettore dell'acido retinoico?", [
  "RARE", "GRE", "ERE", "TRE", "VDRE"], 0,
  "GRE glucocorticoidi, ERE estrogeni, TRE ormoni tiroidei, VDRE vitamina D3.",
  note="Sbobina di Biologia molecolare, lezione 6: c'è scritto «RARE è la sequenza consenso per l'acido arachidonico». È per l'acido retinoico (Retinoic Acid Response Element).")
q("bi6-10", T, "l", L6, "Secondo la lezione, dove si trovano i recettori di glucocorticoidi e aldosterone in assenza di ormone?", [
  "Nel citoplasma", "Nel nucleo", "Sulla membrana plasmatica", "Nel mitocondrio", "Nel reticolo endoplasmatico"], 0,
  "Quelli di estradiolo, androgeni e vitamina D3 sono invece indicati come nucleari.")
q("bi6-11", T, "h", L6, "Quale effetto di un eccesso cronico di glucocorticoidi è riportato nella lezione?", [
  "Osteoporosi per meno assorbimento di calcio",
  "Ipoglicemia per inibizione della gluconeogenesi",
  "Aumento della massa muscolare",
  "Guarigione più rapida delle ferite",
  "Minore rischio di infezioni",
  ], 0,
  "Anche debolezza muscolare, ritardo di guarigione e più infezioni.")

# ── Vitamina D ed effetti non genomici (lezione 7) ─────────────────────────
T = "bm7-vitd"
q("bd7-01", T, "f", L7, "Da quale molecola si forma la vitamina D3 nella pelle?", [
  "7-DHC", "Lanosterolo", "Squalene", "Pregnenolone", "Ergosterolo"], 0,
  "La luce rompe il legame tra C9 e C10 dell'anello B: si forma il colecalciferolo.")
q("bd7-02", T, "m", L7, "Come agisce la vitamina D3 attiva?", [
  "Lega un recettore nucleare",
  "Lega un GPCR e aumenta il cAMP",
  "Lega un recettore tirosina chinasi",
  "Attraversa la membrana legata al calcio",
  "Agisce come cofattore delle ATPasi del calcio",
  ], 0,
  "Senza ligando il recettore non riconosce il DNA; controlla per esempio i geni delle ATPasi Ca²⁺-dipendenti.")
q("bd7-03", T, "a", L7, "Che cosa sono gli effetti «non genomici» degli ormoni steroidei?", [
  "Effetti rapidi che partono dalla membrana",
  "Effetti lenti dovuti a mutazioni indotte dall'ormone nel DNA",
  "Effetti che dipendono solo dalla proteina di trasporto plasmatica",
  "Effetti mediati dall'RNA ribosomiale anziché dal DNA",
  "Effetti dovuti alla degradazione dell'ormone nel fegato",
  ], 0,
  "Coinvolgono PKC, DAG, IP₃; possono non essere bloccati dagli antagonisti classici.")
q("bd7-04", T, "l", L7, "Tra quali atomi la luce rompe l'anello del 7-deidrocolesterolo?", [
  "C9 e C10", "C1 e C2", "C17 e C20", "C5 e C6", "C3 e C4"], 0,
  "Poi il colecalciferolo viene idrossilato in 25 (fegato) e in 1 (rene).")

# ── Visione (lezione 7) ─────────────────────────────────────────────────────
T = "bm7-vista"
q("bvi7-01", T, "f", L7, "Quali cellule della retina servono alla visione con poca luce?", [
  "I bastoncelli", "I coni", "Le cellule gangliari", "Le cellule bipolari", "L'epitelio pigmentato"], 0,
  "Sono circa 10⁹ per retina; i coni (colori) circa 10⁶.")
q("bvi7-02", T, "f", L7, "A quale residuo dell'opsina è legato l'11-cis-retinale?", [
  "Lys296 dell'elica 7", "Cys110 dell'elica 3", "Ser14 dell'elica 1", "His211 dell'elica 5", "Glu113 dell'elica 3"], 0,
  "Con una base di Schiff protonata.")
q("bvi7-03", T, "m", L7, "Che cosa fa la transducina attivata?", [
  "Toglie l'inibitore alla fosfodiesterasi del cGMP",
  "Attiva l'adenilato ciclasi del segmento esterno",
  "Apre direttamente i canali per i cationi",
  "Fosforila la rodopsina sulla coda C-terminale",
  "Riconverte il retinale tutto-trans in 11-cis",
  ], 0,
  "La fosfodiesterasi degrada il cGMP.")
q("bvi7-04", T, "m", L7, "Perché al buio il bastoncello ha un potenziale di circa −45 mV?", [
  "Il cGMP tiene semiaperti i canali cationici",
  "Il cAMP chiude i canali del K⁺",
  "La rodopsina pompa Na⁺ fuori dalla cellula",
  "La transducina apre i canali del Cl⁻",
  "Il retinale tutto-trans apre i canali del Ca²⁺",
  ], 0,
  "Con la luce il cGMP scende, i canali si chiudono e il potenziale va verso −75 mV.")
q("bvi7-05", T, "a", L7, "Come si spegne il segnale dopo la stimolazione luminosa?", [
  "Il calo di Ca²⁺ riattiva la guanilato ciclasi e l'arrestina blocca il recettore",
  "Il Ca²⁺ in aumento attiva la fosfodiesterasi; la PKA fosforila la transducina",
  "La rodopsina viene degradata dal proteasoma e risintetizzata",
  "Il cGMP in aumento attiva la rodopsina chinasi",
  "La transducina lega l'arrestina e si stacca dal recettore",
  ], 0,
  "Il retinale tutto-trans si stacca e viene re-isomerizzato a 11-cis.")
q("bvi7-06", T, "a", L7, "Da che cosa dipende l'adattamento al buio dopo un ambiente luminoso?", [
  "Dalla fosforilazione della rodopsina",
  "Da quanto 11-cis-retinale viene sintetizzato ex novo",
  "Da quanto cAMP si accumula nei bastoncelli",
  "Da quante transducine vengono degradate",
  "Da quanti coni passano allo stato attivo",
  ], 0,
  "Man mano che la rodopsina si defosforila, l'arrestina si stacca e la transducina può essere attivata.")
q("bvi7-07", T, "a", L7, "Una madre portatrice di daltonismo e un padre sano: che cosa ci si aspetta nei figli?", [
  "Metà delle figlie portatrici, metà dei maschi malati",
  "Tutti i figli maschi malati e tutte le figlie sane",
  "Metà dei figli malati, indipendentemente dal sesso",
  "Tutte le figlie malate e tutti i figli maschi portatori",
  "Nessun figlio malato, perché il padre è sano",
  ], 0,
  "Ereditarietà recessiva legata all'X.",
  note="La lezione dice che tutti e tre i geni dei pigmenti dei coni sono sull'X. Lo sono quelli del rosso e del verde; il gene del pigmento blu è sul cromosoma 7, quindi la tritanopia non è legata all'X.")
q("bvi7-08", T, "l", L7, "Quale forma di daltonismo aveva John Dalton?", [
  "Deuteranopia (verde)", "Protanopia (rosso)", "Tritanopia (blu)", "Acromatopsia completa", "Cecità notturna"], 0,
  "Lo si è scoperto sequenziando il DNA dei suoi occhi negli anni '90.")
q("bvi7-09", T, "l", L7, "Da quale molecola deriva l'11-cis-retinale?", [
  "β-carotene → retinolo", "Colesterolo → 7-deidrocolesterolo", "Triptofano → niacina", "Tirosina → L-DOPA", "Fenilalanina → tirosina"], 0,
  "Il retinolo (vitamina A) viene ossidato ad aldeide e isomerizzato sul C11.")
q("bvi7-10", T, "h", L7, "La lezione dice che l'isomerizzazione dell'11-cis-retinale avviene in 10⁻² secondi. Che cosa è corretto?", [
  "Avviene in picosecondi",
  "Avviene in circa un secondo, come la risposta del potenziale",
  "Avviene in minuti, il tempo dell'adattamento al buio",
  "Avviene solo dopo l'attivazione della transducina",
  "Non avviene nel bastoncello ma nell'epitelio pigmentato",
  ], 0,
  "La risposta elettrica dura invece circa un secondo.",
  note="Sbobina di Biologia molecolare, lezione 7: indica «10 alla meno 2 secondi». Nei testi di riferimento la fotoisomerizzazione avviene in circa 10⁻¹² secondi.")

# ── Olfatto (lezione 7) ─────────────────────────────────────────────────────
T = "bm7-olfatto"
q("bo7-01", T, "f", L7, "Che tipo di recettori hanno i neuroni olfattivi per la maggior parte degli odori?", [
  "GPCR a 7 eliche", "Recettori tirosina chinasi", "Recettori nucleari", "Canali al cloro", "Recettori JAK/STAT"], 0,
  "Ne esistono circa 1000 tipi, che si combinano per riconoscere gli odori.")
q("bo7-02", T, "m", L7, "Qual è la sequenza della trasduzione olfattiva principale?", [
  "Gα → cAMP → canali del Ca²⁺ → uscita di Cl⁻",
  "Gα-GTP → fosfodiesterasi → meno cGMP → chiusura dei canali",
  "Gα-GTP → PLC → IP₃ → canali del K⁺ chiusi",
  "Recettore → JAK → STAT → trascrizione",
  "Gα-GTP → guanilato ciclasi → cGMP → PKG",
  ], 0,
  "Il Cl⁻ esce e la cellula si depolarizza; il Ca²⁺ chiude poi gli stessi canali (spegnimento).")
q("bo7-03", T, "a", L7, "Perché i due enantiomeri del carvone hanno odori diversi?", [
  "Vengono riconosciuti da recettori diversi",
  "Uno solo dei due è volatile alla temperatura corporea",
  "Uno dei due viene ossidato dalla mucosa prima del legame",
  "Attivano lo stesso recettore con intensità diverse",
  "Uno lega il recettore, l'altro la proteina di trasporto",
  ], 0,
  "Conta la struttura tridimensionale della molecola.",
  note="Sbobina di Biologia molecolare, lezione 7: la molecola è scritta «carbone» e i due odori sono «menta verde» e «vino». È il carvone: R = menta verde (spearmint), S = cumino dei prati (carvi).")
q("bo7-04", T, "h", L7, "Quale via alternativa di trasduzione olfattiva descrive la lezione?", [
  "Recettori guanilato ciclasi: il cGMP apre canali cationici",
  "Recettori nucleari che aumentano la sintesi dei canali ionici",
  "Recettori tirosina chinasi che attivano Ras e MAPK",
  "Canali ionici che si aprono direttamente legando l'odorante",
  "Recettori che attivano la PLC e chiudono i canali del K⁺",
  ], 0,
  "Alcuni odoranti attivano anche Gi o fosfodiesterasi: il risultato netto è sempre il controllo dei canali cationici.")

# ── Gusto (lezione 7) ───────────────────────────────────────────────────────
T = "bm7-gusto"
q("bgu7-01", T, "f", L7, "Come si chiama la proteina G delle cellule del gusto?", [
  "Gustducina", "Transducina", "Golf", "Gq", "Gi"], 0,
  "È espressa solo nelle taste receptor cells.")
q("bgu7-02", T, "m", L7, "Come viene percepito il dolce secondo la lezione?", [
  "Gustducina → cAMP → PKA chiude i canali del K⁺ → depolarizzazione",
  "Gustducina → cGMP → PKG apre i canali del Na⁺",
  "Gustducina → PLC → IP₃ → Ca²⁺ apre i canali del Cl⁻",
  "Il glucosio entra con il GLUT2 e chiude i canali del K⁺ con l'ATP",
  "Il dolce apre direttamente un canale cationico sulla lingua",
  ], 0,
  "I dolcificanti artificiali usano invece βγ della gustducina → PLC → PKC.")
q("bgu7-03", T, "a", L7, "Come viene percepito l'amaro secondo la lezione?", [
  "Via PLC e IP₃, con apertura di canali cationici",
  "Via adenilato ciclasi: il cAMP chiude i canali del K⁺",
  "Via fosfodiesterasi: il cGMP scende e i canali si chiudono",
  "Via JAK/STAT: STAT attiva i geni dei canali",
  "Via recettore nucleare: aumenta la sintesi di gustducina",
  ], 0,
  "Si ottiene comunque una depolarizzazione della membrana.",
  note="La lezione dice che l'IP₃ aumenta il calcio «nel reticolo endoplasmatico»: l'IP₃ fa uscire il Ca²⁺ dal reticolo verso il citosol.")
q("bgu7-04", T, "l", L7, "Quali sono i cinque sapori citati nella lezione?", [
  "Dolce, amaro, acido, salato, umami", "Dolce, amaro, acido, salato, piccante", "Dolce, amaro, salato, grasso, metallico", "Dolce, acido, salato, umami, astringente", "Dolce, amaro, acido, salato, fresco"], 0,
  "Dolce e amaro sono i meglio caratterizzati.")
q("bgu7-05", T, "h", L7, "La lezione descrive una mappa della lingua (dolce sulla punta, amaro dietro). Che cosa è corretto?", [
  "È superata: ogni zona percepisce tutti i sapori",
  "È esatta: ogni zona ha un solo tipo di recettore",
  "È esatta solo per il dolce e l'amaro",
  "La punta percepisce l'amaro e il fondo il dolce",
  "La mappa vale solo per i neonati",
  ], 0,
  "Le cellule del gusto per ogni qualità sono distribuite su tutta la lingua, con piccole differenze di sensibilità.",
  note="Sbobina di Biologia molecolare, lezione 7: presenta la classica mappa della lingua. Non è nella sbobina, ma oggi è considerata una semplificazione non corretta.")

# ── Introduzione ai nucleotidi (lezione 7) ─────────────────────────────────
T = "bm7-nucleotidi"
q("bnu7-01", T, "f", L7, "Quale base purinica è la 2-ammino-6-ossi-purina?", [
  "Guanina", "Adenina", "Ipoxantina", "Xantina", "Citosina"], 0,
  "Adenina = 6-amminopurina; ipoxantina = 6-ossipurina; xantina = 2,6-diossipurina.")
q("bnu7-02", T, "f", L7, "Che cosa distingue la timina dall'uracile?", [
  "Un metile in 5", "Un amminogruppo in 4", "Un carbossile in 6", "Un ossidrile in 2", "Un anello imidazolico"], 0,
  "L'acido orotico è l'uracile con un carbossile in 6; la citosina ha un amminogruppo in 4.")
q("bnu7-03", T, "m", L7, "Quali amminoacidi sono precursori dei nucleotidi?", [
  "Glutammina, glicina, aspartato", "Leucina, lisina, valina", "Fenilalanina, tirosina, triptofano", "Serina, treonina, cisteina", "Alanina, prolina, istidina"], 0,
  "Glicina e succinil-CoA sono anche precursori dell'eme.")
q("bnu7-04", T, "m", L7, "Come si chiama il nucleoside dell'ipoxantina?", [
  "Inosina", "Xantosina", "Guanosina", "Uridina", "Orotidina"], 0,
  "L'IMP è il primo nucleotide purinico completo della sintesi de novo.")
q("bnu7-05", T, "a", L7, "Che cosa significa fissare l'azoto atmosferico?", [
  "Ridurre l'N₂ ad ammoniaca",
  "Ossidare l'N₂ a nitrato, cosa che sanno fare le piante",
  "Ossidare l'ammoniaca a nitriti nel suolo",
  "Ridurre i nitrati ad N₂ nei batteri denitrificanti",
  "Legare l'N₂ al glutammato nel fegato",
  ], 0,
  "Il triplo legame (circa 1000 kJ/mol) rende l'N₂ inutilizzabile per animali e piante.",
  note="Sbobina di Biologia molecolare, lezione 7: c'è scritto «ridurre l'azoto atmosferico per ossidarlo ad ammonio». L'N₂ viene ridotto ad ammonio, non ossidato.")
q("bnu7-06", T, "l", L7, "Quale nome chimico corrisponde all'acido orotico?", [
  "2,4-diossi-6-carbossipirimidina", "2,4-diossi-5-metil-pirimidina", "2-ossi-4-ammino-pirimidina", "2,6-diossi-purina", "2,4-diossi-pirimidina"], 0,
  "Sono, nell'ordine dei distrattori, timina, citosina, xantina e uracile.")
q("bnu7-07", T, "h", L7, "Quale affermazione sui composti derivati dagli amminoacidi, citati nella lezione, è corretta?", [
  "Carnitina da lisina e metionina; creatina da arginina, glicina e metionina",
  "La carnitina si sintetizza da leucina; la creatina da serina e glicina",
  "La taurina deriva dal triptofano; la niacina dalla cisteina",
  "L'istamina deriva dalla tirosina; la serotonina dall'istidina",
  "L'eme deriva da glutammina e acetil-CoA",
  ], 0,
  "La taurina deriva dalla cisteina, la niacina dal triptofano, l'eme da glicina e succinil-CoA.",
  note="Sbobina di Biologia molecolare, lezione 7: c'è scritto che la «degradazione» della carnitina dipende da lisina e metionina. Si intende la sintesi.")
