"""Pacchetto 2026-11-12 – Biochimica I, blocchi 1–3 (p. 6–67): domande Medie, Hard e 30 e lode in più
sugli argomenti che avevano pochi quesiti difficili."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Ripasso di propedeutica (p. 6–10) ─────────────────────────────────────
T = "d1-chimica"
q("yd1c-01", T, "m", "7", "Da che cosa dipende soprattutto la solubilità in acqua di una biomolecola?", [
  "Dai gruppi funzionali, che decidono se può formare legami a idrogeno con l'acqua",
  "Dal numero di atomi di carbonio, indipendentemente dai gruppi funzionali legati",
  "Dalla presenza di centri chirali, che rendono la molecola otticamente attiva",
  "Dal peso molecolare: le molecole sotto i 500 Da sono sempre solubili in acqua",
  "Dai doppi legami, che rendono la molecola rigida e quindi più facile da idratare",
  ], 0,
  "Un alcano non forma legami a idrogeno: non è né reattivo né solubile.")
q("yd1c-02", T, "h", "7", "Quale sequenza ordina correttamente lo stato di ossidazione del carbonio, dal meno al più ossidato?", [
  "Alcano → alcol primario → aldeide → acido carbossilico",
  "Alcano → aldeide → alcol primario → acido carbossilico",
  "Alcol primario → alcano → aldeide → acido carbossilico",
  "Alcano → alcol secondario → aldeide → chetone",
  "Acido carbossilico → aldeide → alcol primario → alcano",
  ], 0,
  "Ogni ossidazione toglie due elettroni, ceduti a NAD⁺ o FAD. Un alcol secondario si ossida a chetone.")
q("yd1c-03", T, "h", "8", "Una molecola ha 4 centri chirali. Quanti stereoisomeri ha, e uno di essi quanti enantiomeri e diastereoisomeri ha?", [
  "16 stereoisomeri; 1 enantiomero e 14 diastereoisomeri",
  "8 stereoisomeri; 1 enantiomero e 6 diastereoisomeri",
  "16 stereoisomeri; 2 enantiomeri e 13 diastereoisomeri",
  "16 stereoisomeri; 4 enantiomeri e 11 diastereoisomeri",
  "4 stereoisomeri; 1 enantiomero e 2 diastereoisomeri",
  ], 0,
  "2ⁿ = 2⁴ = 16. L'immagine speculare è una sola; tutti gli altri 14 sono diastereoisomeri.")
q("yd1c-04", T, "l", "8", "Quale conformazione attorno a un legame singolo C–C è la più stabile?", [
  "Sfalsata", "Eclissata", "Cis", "Trans", "Gauche eclissata",
  ], 0,
  "Nella sfalsata i sostituenti sono alla massima distanza; cis e trans riguardano invece i doppi legami (configurazione).")
q("yd1c-05", T, "l", "7", "Secondo la sbobina, oltre quale peso molecolare si parla di macromolecole e quanto pesano in genere i loro monomeri?", [
  "Oltre 5000; monomeri ≤ 500", "Oltre 500; monomeri ≤ 50", "Oltre 50.000; monomeri ≤ 5000", "Oltre 1000; monomeri ≤ 110", "Oltre 5000; monomeri ≤ 110",
  ], 0,
  "I polimeri più corti si chiamano oligomeri.")

T = "d1-acqua"
q("yd1a-01", T, "m", "9", "Perché l'acqua scioglie bene il cloruro di sodio?", [
  "Idrata e stabilizza Na⁺ e Cl⁻, indebolendo le interazioni elettrostatiche tra loro",
  "Forma legami covalenti con Na⁺ e Cl⁻ che sostituiscono il legame ionico del cristallo",
  "Forma clatrati ordinati attorno a Na⁺ e Cl⁻, aumentando la propria entropia",
  "Cede protoni al Cl⁻ e prende elettroni dal Na⁺, neutralizzando le due cariche",
  "È apolare e si inserisce tra gli ioni del cristallo grazie alle forze di van der Waals",
  ], 0,
  "I clatrati si formano invece attorno ai soluti apolari e sono sfavoriti.")
q("yd1a-02", T, "h", "8–9", "Perché l'acqua ha punti di fusione e di ebollizione così alti nonostante il legame a idrogeno sia debole?", [
  "I legami a idrogeno sono numerosissimi e serve molta energia per romperne abbastanza",
  "Ogni legame a idrogeno è più forte di un legame covalente C–C e richiede molta energia",
  "L'acqua forma clatrati con sé stessa che si sciolgono solo ad alta temperatura",
  "La molecola d'acqua è lineare e simmetrica, quindi le sue molecole si impaccano bene",
  "L'ossigeno forma con l'idrogeno un doppio legame che richiede molta energia per rompersi",
  ], 0,
  "Ogni molecola può formare legami a H con altre quattro (geometria quasi tetraedrica, completa nel ghiaccio).")
q("yd1a-03", T, "h", "9", "La CO₂ è un gas apolare poco solubile in acqua. In che forma è trasportata soprattutto nel sangue, e perché?", [
  "Come bicarbonato, molto solubile, dopo essere diventata acido carbonico",
  "Legata al ferro dell'eme dell'emoglobina, che ha un sito apposito per la CO₂",
  "Disciolta come gas, perché nel plasma i clatrati la stabilizzano",
  "Come carbonato di calcio, che precipita e viene poi riassorbito",
  "Legata all'albumina, che trasporta tutte le molecole apolari",
  ], 0,
  "L'O₂, anch'esso poco solubile, viaggia invece legato a emoglobina e mioglobina.")
q("yd1a-04", T, "l", "8", "Quanta energia contiene un legame a idrogeno secondo la sbobina?", [
  "≈ 22 kJ", "≈ 2,2 kJ", "≈ 220 kJ", "≈ 350 kJ", "≈ 0,6 kJ",
  ], 0,
  "È debole, ma i legami a idrogeno sono molto numerosi e si rompono e riformano di continuo.")

T = "d1-metabolismo"
q("yd1m-01", T, "m", "10", "Che rapporto c'è tra catabolismo e anabolismo?", [
  "Il catabolismo degrada i nutrienti e produce ATP, che l'anabolismo usa per le biosintesi",
  "L'anabolismo degrada i nutrienti e produce ATP, che il catabolismo usa per le biosintesi",
  "Sono vie indipendenti: il catabolismo produce calore e l'anabolismo produce ATP",
  "Il catabolismo sintetizza le macromolecole consumando l'ATP prodotto dall'anabolismo",
  "Entrambi producono ATP, ma l'anabolismo avviene solo nel tessuto adiposo",
  ], 0,
  "L'ATP serve anche alla contrazione muscolare e al mantenimento del potenziale di membrana.")
q("yd1m-02", T, "h", "7–8", "Che cosa hanno in comune le reazioni con cui si formano proteine, acidi nucleici e polisaccaridi?", [
  "Uniscono monomeri perdendo una molecola d'acqua e danno polimeri con due estremità diverse",
  "Uniscono monomeri liberando CO₂ e danno polimeri simmetrici senza un verso di lettura",
  "Uniscono monomeri con legami a idrogeno e danno polimeri che si sciolgono a 37 °C",
  "Uniscono monomeri aggiungendo una molecola d'acqua e danno polimeri con due estremità identiche",
  "Uniscono monomeri senza consumare energia e danno polimeri ramificati",
  ], 0,
  "Acidi nucleici 5'/3', proteine N/C-terminale, polisaccaridi estremità riducente/non riducente.")
q("yd1m-03", T, "l", "7", "Come si chiama l'insieme delle molecole che contengono lipidi in una cellula?", [
  "Lipidoma", "Glicoma", "Proteoma", "Metaboloma", "Lipoproteoma",
  ], 0,
  "Proteoma: proteine funzionanti; glicoma: molecole con carboidrati; genoma: l'intera sequenza del DNA.")

# ── Amminoacidi e peptidi (p. 11–23) ──────────────────────────────────────
T = "d2-strutturali"
q("yd2s-01", T, "m", "11", "Per trasformare un L-amminoacido nel suo enantiomero D che cosa bisogna fare?", [
  "Rompere e riformare un legame del carbonio α, invertendone la configurazione",
  "Ruotare la molecola di 180° attorno al legame tra carbonio α e carbossile",
  "Ruotare il piano della luce polarizzata facendola passare in un polarimetro",
  "Protonare il gruppo amminico, che passa così dal lato sinistro al lato destro",
  "Cambiare la conformazione attorno ai legami singoli della catena laterale",
  ], 0,
  "La configurazione cambia solo rompendo legami; la conformazione cambia per rotazione attorno ai legami singoli.")
q("yd2s-02", T, "h", "15", "La parete batterica contiene D-amminoacidi, ma i ribosomi non li incorporano mai. Come si spiega?", [
  "La sintesi ribosomiale è stereospecifica; i D-amminoacidi della parete li inseriscono altri enzimi",
  "I D-amminoacidi vengono convertiti in L dai ribosomi batterici durante la traduzione",
  "I batteri hanno tRNA speciali per i D-amminoacidi, che i ribosomi umani invece non riconoscono affatto",
  "I D-amminoacidi si formano solo dopo la morte della cellula, per racemizzazione spontanea",
  "I ribosomi incorporano D-amminoacidi solo nei peptidi con meno di 50 residui",
  ], 0,
  "D-amminoacidi si trovano solo in pochi piccoli peptidi, come quelli della parete batterica e alcuni antibiotici.")
q("yd2s-03", T, "h", "14", "Rispetto alla L-isoleucina, la L-alloisoleucina è:", [
  "Un diastereoisomero, con configurazione diversa al solo carbonio β",
  "Un enantiomero, con configurazione opposta a entrambi i centri chirali",
  "Un isomero geometrico cis-trans attorno al legame tra carbonio α e β",
  "Un conformero, che si forma per rotazione attorno al legame Cα–Cβ",
  "Lo stesso composto, perché entrambi i centri chirali restano di tipo S",
  ], 0,
  "Ile e Thr hanno due centri chirali (α e β). Allo-Ile e allo-Thr non sono nelle proteine, se non per modificazioni.")
q("yd2s-04", T, "l", "13", "Su quale molecola di riferimento si basa la convenzione D/L di Fischer (1891)?", [
  "Gliceraldeide", "Alanina", "Glucosio", "Acido lattico", "Diidrossiacetone",
  ], 0,
  "Il gruppo amminico a sinistra in proiezione di Fischer indica la serie L.",
  note="Sbobina di Biochimica I, p. 13: c'è scritto che Fischer «assegnò alla gliceraldeide l'isomeria L». Fischer assegnò arbitrariamente la configurazione D alla (+)-gliceraldeide; l'altra è la L.")

T = "d2-classificazione"
q("yd2c-01", T, "m", "16", "Perché la tirosina può essere classificata anche tra gli amminoacidi polari?", [
  "Per il gruppo -OH sull'anello della catena laterale",
  "Per il gruppo amminico in più sulla catena laterale",
  "Per l'atomo di zolfo all'interno della catena laterale",
  "Per il gruppo carbossilico in più sulla catena laterale",
  "Perché assorbe la luce UV a 280 nm",
  ], 0,
  "È aromatica come fenilalanina e triptofano.")
q("yd2c-02", T, "h", "16", "Secondo la sbobina, perché la prolina non partecipa ad α-eliche e foglietti β?", [
  "Il suo gruppo amminico è chiuso in un anello con la catena laterale: è un imminoacido",
  "La sua catena laterale è troppo grande e ingombra lo spazio al centro dell'elica",
  "Ha due centri chirali e non può assumere gli angoli φ e ψ tipici dell'α-elica e del foglietto",
  "La sua catena laterale è carica a pH 7 e respinge i residui vicini",
  "Forma sempre un ponte disolfuro con le cisteine vicine e blocca la catena",
  ], 0,
  "L'azoto legato covalentemente alla catena laterale non ha l'H per il legame a idrogeno. La prolina è invece frequente nei ripiegamenti β.")
q("yd2c-03", T, "h", "16", "In un nucleo idrofobico una leucina viene sostituita da una metionina. Che effetto è più probabile?", [
  "Piccolo: lo zolfo della metionina è interno alla catena e il residuo resta apolare",
  "Grave: lo zolfo forma subito un ponte disolfuro con la cisteina più vicina",
  "Grave: la metionina è carica a pH fisiologico e destabilizza il nucleo idrofobico",
  "Piccolo, ma solo perché la metionina ha la stessa catena laterale ramificata",
  "Grave: la metionina è un imminoacido come la prolina e interrompe le strutture secondarie",
  ], 0,
  "La metionina è un tioetere, senza gruppo -SH libero: si comporta da apolare.")
q("yd2c-04", T, "l", "16", "Come sono costruite le sigle a tre lettere degli amminoacidi?", [
  "Con le prime tre lettere del nome inglese", "Con le prime tre lettere del nome italiano", "Con le iniziali dei gruppi della catena laterale",
  "Con le prime tre lettere del nome latino", "Con la prima, la terza e l'ultima lettera del nome",
  ], 0,
  "Es. Trp (tryptophan), Gln (glutamine).")

T = "d2-acidobase"
q("yd2a-01", T, "m", "19", "A un pH superiore al suo punto isoelettrico, che carica netta ha un amminoacido?", [
  "Negativa", "Positiva", "Zero", "Dipende solo dalla catena laterale", "Positiva se il pH supera 7",
  ], 0,
  "Sopra il pI prevalgono i gruppi deprotonati; sotto il pI la carica netta è positiva.")
q("yd2a-02", T, "h", "18–19", "Glutammato: pK₁ (α-COOH) = 2,2, pKR (COOH laterale) = 4,3, pK₂ (α-NH₃⁺) = 9,7. Qual è il pI?", [
  "≈ 3,25", "≈ 5,95", "≈ 6,95", "≈ 7,00", "≈ 5,40",
  ], 0,
  "Per un amminoacido acido si fa la media tra i due pK dei carbossili: (2,2 + 4,3)/2 = 3,25.")
q("yd2a-03", T, "h", "19", "Perché serina, treonina e cisteina sono considerate «eccezioni» tra le catene laterali ionizzabili?", [
  "Dissociano solo a pH molto alti, ma in certi contesti proteici il loro -OH o -SH può dissociarsi",
  "Hanno un pKa vicino a 6, quindi a pH fisiologico cedono e accettano protoni con grande facilità",
  "Sono sempre cariche negativamente a pH 7, come aspartato e glutammato",
  "Sono sempre protonate a pH 7, come lisina e arginina, ma senza carica positiva",
  "Non hanno gruppi ionizzabili, ma diventano ionizzabili dopo modificazione post-traduzionale",
  ], 0,
  "Il pKa vicino a 6 è quello dell'istidina, che per questo è versatile nella catalisi.")
q("yd2a-04", T, "l", "19", "A pH 7, come si trovano le catene laterali di Asp/Glu e di Lys/Arg?", [
  "Asp e Glu deprotonati (carica −), Lys e Arg protonati (carica +)",
  "Asp e Glu protonati (carica 0), Lys e Arg deprotonati (carica 0)",
  "Asp e Glu deprotonati (carica −), Lys e Arg deprotonati (carica 0)",
  "Asp e Glu protonati (carica +), Lys e Arg protonati (carica +)",
  "Tutti e quattro neutri, perché a pH 7 sono in forma di zwitterione",
  ], 0,
  "Il pI di un amminoacido basico si calcola con la media dei due pK dei gruppi amminici.")

T = "d2-nutrizionale"
q("yd2n-01", T, "m", "20", "Che cosa sono gli amminoacidi condizionalmente essenziali?", [
  "Sintetizzabili, ma da assumere anche con la dieta in alcune fasi, come la crescita",
  "Non sintetizzabili in nessuna fase della vita, quindi sempre da assumere con la dieta",
  "Ricavati da altri amminoacidi, se questi sono introdotti a sufficienza con la dieta",
  "Sintetizzabili solo dalla flora intestinale, che li cede poi all'organismo",
  "Necessari soltanto negli anziani, quando la sintesi proteica è rallentata",
  ], 0,
  "I semiessenziali (cisteina, tirosina) si ricavano da altri amminoacidi: la cisteina dalla metionina.")
q("yd2n-02", T, "h", "20", "Una dieta è povera sia di metionina sia di cisteina. Quale amminoacido rischia di mancare oltre alla metionina?", [
  "La cisteina, che è semiessenziale e si ricava dalla metionina",
  "La tirosina, che si ricava dalla metionina per transaminazione",
  "L'alanina, che si forma dal piruvato solo in presenza di metionina",
  "La glicina, che deriva dalla demetilazione della metionina",
  "Il glutammato, che cede il gruppo amminico alla metionina",
  ], 0,
  "La tirosina è l'altro semiessenziale, ma si ricava dalla fenilalanina (non è nelle sbobine, è nel Lehninger).")
q("yd2n-03", T, "h", "20–21", "Perché idrossiprolina e idrossilisina non hanno un codone nel codice genetico?", [
  "Si formano per modificazione post-traduzionale di residui già inseriti nella catena",
  "Vengono inserite dal ribosoma con un tRNA speciale che legge il codone di stop",
  "Sono D-amminoacidi e i ribosomi non li incorporano, quindi servono enzimi della parete",
  "Si formano nel sangue per ossidazione spontanea di prolina e lisina libere",
  "Sono assorbite già idrossilate dalla dieta e inserite durante la sintesi proteica",
  ], 0,
  "Lo stesso vale per il γ-carbossiglutammato della protrombina e la 6-N-metillisina della miosina.")
q("yd2n-04", T, "l", "21", "In quale proteina si trova la 6-N-metillisina?", [
  "Miosina", "Collagene", "Protrombina", "Elastina", "Istoni",
  ], 0,
  "Collagene: 4-idrossiprolina e 5-idrossilisina; protrombina: γ-carbossiglutammato.")

T = "d2-peptidico"
q("yd2p-01", T, "m", "22", "Perché la formazione del legame peptidico richiede energia?", [
  "L'uscita del gruppo -OH dal carbonio carbonilico è sfavorita: l'amminoacido va attivato sul tRNA",
  "L'azoto non ha doppietti liberi e quindi non può attaccare il carbonio carbonilico senza consumare ATP",
  "Si forma un doppio legame C=N stabile che richiede energia per essere spezzato",
  "Bisogna prima deprotonare il carbossile, che a pH 7 è sempre nella forma -COOH",
  "La reazione libera acqua, che deve essere pompata fuori dalla cellula con ATP",
  ], 0,
  "L'azoto può attaccare il carbonio carbonilico grazie al suo doppietto, ma il gruppo uscente non se ne va facilmente.")
q("yd2p-02", T, "h", "22–23", "Quali cariche parziali crea la risonanza del legame peptidico, e con quale conseguenza?", [
  "δ+ sull'azoto e δ− sull'ossigeno: il legame è planare, dipolare e non ruota",
  "δ− sull'azoto e δ+ sull'ossigeno: il legame è planare, apolare e ruota liberamente",
  "δ+ sul carbonio α e δ− sull'azoto: il legame è tetraedrico e ruota liberamente",
  "δ+ sull'ossigeno e δ− sul carbonio: il legame è un doppio C=O non planare",
  "Nessuna carica: la risonanza rende il legame un singolo C–N che ruota",
  ], 0,
  "La coppia di elettroni dell'azoto si delocalizza verso l'ossigeno carbonilico.")
q("yd2p-03", T, "h", "23", "Una proteina pesa ≈ 55 kDa. Quanti residui contiene circa?", [
  "≈ 500", "≈ 50", "≈ 250", "≈ 1100", "≈ 5000",
  ], 0,
  "Peso medio di un residuo ≈ 110 Da: 55.000/110 ≈ 500.")
q("yd2p-04", T, "l", "23", "Che cosa sono le metalloproteine?", [
  "Proteine coniugate il cui gruppo prostetico è un metallo",
  "Proteasi che tagliano i legami peptidici con un metallo",
  "Proteine che legano metalli solo nel plasma per trasportarli",
  "Proteine che contengono amminoacidi con zolfo nel sito attivo",
  "Proteine fibrose rinforzate da ioni metallici tra le catene",
  ], 0,
  "Lo stesso vale per lipoproteine (lipidi) e glicoproteine (carboidrati).")

# ── Struttura delle proteine (p. 24–67) ───────────────────────────────────
T = "d3-primaria"
q("yd3p-01", T, "m", "25", "Che informazioni dà conoscere la sequenza amminoacidica di una proteina?", [
  "Su struttura tridimensionale, funzione, localizzazione cellulare ed evoluzione",
  "Solo sul peso molecolare e sul numero di ponti disolfuro della proteina",
  "Solo sulla funzione, perché la struttura 3D non dipende dalla sequenza",
  "Sulla quantità di proteina presente in una cellula in un dato momento",
  "Solo sulla localizzazione cellulare, tramite la sequenza segnale N-terminale",
  ], 0,
  "Dalla somiglianza tra sequenze si identificano famiglie di proteine con struttura e funzione comuni.")
q("yd3p-02", T, "h", "26", "Si trattano l'insulina con un agente riducente in eccesso. Che cosa si ottiene?", [
  "Catene A e B separate, perché sono unite solo dai due ponti disolfuro intercatena",
  "Un'unica catena di 51 aa, perché i ponti disolfuro sono tutti intracatena",
  "Le catene restano unite, perché A e B sono legate da legami peptidici",
  "Proinsulina con il peptide C, che si riforma quando si rompono i ponti disolfuro",
  "Catene A e B separate, ma solo se prima si taglia il peptide C con una proteasi",
  ], 0,
  "Ponti intercatena A7–B7 e A20–B19; intracatena A6–A11.")
q("yd3p-03", T, "h", "25", "Una malattia genetica è dovuta alla sostituzione di un solo amminoacido. Perché la funzione può crollare?", [
  "La sequenza determina il ripiegamento tridimensionale, da cui dipende la funzione",
  "Ogni sostituzione introduce un codone di stop e la proteina resta tronca",
  "La sostituzione cambia il codice genetico e quindi tutte le proteine della cellula",
  "Un amminoacido diverso impedisce sempre la formazione dei legami peptidici vicini",
  "La sostituzione rende la proteina un D-polipeptide che i ribosomi non riconoscono",
  ], 0,
  "Migliaia di malattie genetiche dell'uomo derivano da proteine difettose, spesso per un solo residuo sostituito.")
q("yd3p-04", T, "l", "26", "Qual è il nome sistematico del glutatione?", [
  "γ-Glutammil-cisteinil-glicina", "Glicil-cisteinil-glutammato", "α-Glutammil-glicil-cisteina", "Cisteinil-glutammil-glicina", "γ-Glutammil-glicil-cisteina",
  ], 0,
  "N-terminale del glutammato, C-terminale della glicina. Due glutationi si uniscono con un ponte disolfuro tra le cisteine.",
  note="Sbobina di Biochimica I, p. 26: lo chiama «glutammil-cisteil glicina». Il glutammato è legato alla cisteina con il carbossile γ della catena laterale, non con l'α-carbossile: per questo il nome corretto è γ-glutammil-cisteinil-glicina (Lehninger).")

T = "d3-secondaria"
q("yd3s-01", T, "m", "30", "Perché nell'α-elica le catene laterali puntano tutte verso l'esterno?", [
  "Il legame peptidico è in trans e la catena occupa lo spazio nel modo migliore",
  "Le catene laterali formano i legami a idrogeno che stabilizzano l'elica",
  "Il centro dell'elica è occupato dai ponti disolfuro tra le cisteine",
  "Le catene laterali sono tutte idrofiliche e cercano il contatto con l'acqua",
  "Il legame peptidico è in cis e spinge tutti i gruppi R lontano dall'asse dell'elica",
  ], 0,
  "I legami a idrogeno coinvolgono solo C=O e N–H dello scheletro; il centro dell'elica è vuoto.")
q("yd3s-02", T, "h", "30", "Con passo 5,4 Å e 3,6 residui per giro, di quanto sale l'α-elica per ogni residuo?", [
  "≈ 1,5 Å", "≈ 3,6 Å", "≈ 5,4 Å", "≈ 0,67 Å", "≈ 19,4 Å",
  ], 0,
  "5,4/3,6 = 1,5 Å. Per questo 153 residui in α-elica danno un bastoncello di ≈ 230 Å.")
q("yd3s-03", T, "h", "31", "Che cosa distingue un ripiegamento β di tipo I da uno di tipo II?", [
  "L'orientamento del C=O tra secondo e terzo residuo; nel tipo II in terza posizione c'è tipicamente glicina",
  "Il numero di residui: il tipo I ne ha 4 e il tipo II ne ha 6, con prolina in quarta posizione",
  "Il legame a idrogeno: nel tipo I è tra il residuo i e i+3, nel tipo II tra il residuo i e il residuo i+4 della catena",
  "Il tipo I si trova nei foglietti paralleli, il tipo II solo in quelli antiparalleli",
  "Il tipo I ha il legame peptidico in trans, il tipo II ha tutti i legami peptidici in cis",
  ], 0,
  "In entrambi il legame a H unisce il C=O del primo residuo e l'N–H del quarto (i → i+3).")
q("yd3s-04", T, "l", "29–30", "Con quale residuo forma il legame a idrogeno il C=O del residuo i in un'α-elica?", [
  "Con l'N–H del residuo i+4", "Con l'N–H del residuo i+3", "Con l'N–H del residuo i+2", "Con l'N–H del residuo i+5", "Con la catena laterale del residuo i+4",
  ], 0,
  "Nella sbobina: «a 3 legami peptidici di distanza». L'anello chiuso dal legame a H comprende 13 atomi; ogni giro ha 3,6 residui.")

T = "d3-collagene"
q("yd3c-01", T, "m", "40–41", "Dove avvengono l'idrossilazione e la rimozione dei domini globulari del procollagene?", [
  "Idrossilazione nel reticolo endoplasmatico; rimozione dei domini fuori dalla cellula",
  "Idrossilazione fuori dalla cellula; rimozione dei domini nel reticolo endoplasmatico",
  "Entrambe nel Golgi, prima che le tre catene si avvolgano nella tripla elica",
  "Entrambe fuori dalla cellula, ad opera delle metalloproteasi della matrice",
  "Idrossilazione nel citosol; rimozione dei domini nei lisosomi dei fibroblasti",
  ], 0,
  "Le procollagene peptidasi extracellulari tagliano i domini N- e C-terminali; poi si formano fibrille e legami crociati.",
  note="Sbobina di Biochimica I, p. 41: (1) dice che la glicosilazione avviene «a livello di Pro o OH-Pro»: avviene sull'idrossilisina, come dice la stessa sbobina a p. 38; (2) dice che il procollagene è secreto «nello spazio extracellulare (citosol)»: lo spazio extracellulare non è il citosol.")
q("yd3c-02", T, "h", "45", "Una persona ha mangiato a lungo legumi contenenti una sostanza tossica e ha fibre di collagene lasse. Quale meccanismo è più probabile?", [
  "Latirismo: la tossina blocca la lisil ossidasi e non si formano i legami crociati",
  "Scorbuto: la tossina distrugge la vitamina C e la prolina non viene idrossilata",
  "Osteogenesi imperfetta: la tossina muta il gene del collagene di tipo I",
  "Ehlers-Danlos: la tossina impedisce la glicosilazione delle idrossilisine del collagene",
  "La tossina attiva la collagenasi della matrice e il collagene viene degradato",
  ], 0,
  "Il latirismo dà problemi agli arti inferiori per alterazioni del midollo spinale e disturbi neurologici.")
q("yd3c-03", T, "h", "42", "Perché l'idrossiprolina nelle urine è un indice del metabolismo del collagene?", [
  "Non viene metabolizzata: quella liberata dalla degradazione finisce nelle urine",
  "Viene sintetizzata dal rene solo quando il collagene osseo è in eccesso nel sangue",
  "È un amminoacido essenziale che si elimina quando la dieta ne è ricca",
  "Si forma nelle urine per ossidazione della prolina libera filtrata",
  "È prodotta dalla collagenasi batterica solo durante le infezioni",
  ], 0,
  "Il turnover del collagene è lento (60–70 giorni) e dipende da stato nutrizionale e ormoni.")
q("yd3c-04", T, "h", "42", "Come fa il batterio della gangrena gassosa a invadere i muscoli?", [
  "Produce una collagenasi che degrada il collagene dei tessuti",
  "Produce una tossina che ADP-ribosila il collagene fibrillare",
  "Blocca la lisil ossidasi e impedisce i legami crociati",
  "Produce una gelatinasi che degrada solo il collagene fetale",
  "Inibisce la prolil-idrossilasi sottraendo la vitamina C",
  ], 0,
  "È un clostridio anaerobio. Nell'uomo collagenasi e gelatinasi sono metalloproteasi della matrice.")
q("yd3c-05", T, "l", "43", "Come si chiama il legame crociato che si forma riducendo la base di Schiff tra una lisina e un'allisina?", [
  "Lisinonorleucina", "Idrossipiridinio", "Desmosina", "Aldolo di allisina", "Idrossilisinonorleucina",
  ], 0,
  "Due allisine danno invece una condensazione aldolica; idrossipiridinio da una lisina e due idrossilisine.")
q("yd3c-06", T, "l", "44", "Quali tipi di collagene sono i più glicosilati, e quindi più idratati?", [
  "Il tipo II e il tipo IV", "Il tipo I e il tipo III", "Il tipo I e il tipo II", "I FACIT di tipo IX e XII", "Il tipo III e il tipo IV",
  ], 0,
  "Hanno più idrossilisine glicosilabili; il tipo I (anche nell'osso) e il III sono meno glicosilati.")

T = "d3-terziaria"
q("yd3t-01", T, "m", "33", "Perché le proteine a bastoncello, tutte α-elica, sono poco adatte a funzioni come la catalisi?", [
  "Sono rigide e non fanno i cambi conformazionali che servono alla funzione",
  "Non contengono amminoacidi aromatici e non assorbono la luce a 280 nm",
  "Hanno tutte le catene laterali rivolte all'interno e non riescono a legare i substrati",
  "Sono troppo idrofiliche e si sciolgono senza mantenere la struttura",
  "Non hanno legami a idrogeno e la loro struttura si disfa a 37 °C",
  ], 0,
  "Hanno per lo più funzione strutturale; la forma globulare è più compatta e funzionale.")
q("yd3t-02", T, "h", "33", "Se i 153 residui della mioglobina fossero tutti in α-elica, quanto sarebbe lungo il bastoncello?", [
  "≈ 230 Å", "≈ 540 Å", "≈ 826 Å", "≈ 153 Å", "≈ 42 Å",
  ], 0,
  "153/3,6 × 5,4 Å ≈ 230 Å. In conformazione β sarebbe ≈ 540 Å.")
q("yd3t-03", T, "h", "48", "Che cos'è il ripiegamento «a chiave greca»?", [
  "Un ripiegamento di soli filamenti β uniti da connessioni lunghe, senza α-eliche",
  "Un ripiegamento di sole α-eliche avvolte a coppie in un coiled coil sinistrorso",
  "Un barile di filamenti β paralleli alternati ad α-eliche che si richiude su sé stesso",
  "Un motivo con due α-eliche unite da un'ansa che lega il Ca²⁺",
  "Un foglietto piatto di filamenti paralleli che fa da superficie di contatto",
  ], 0,
  "Il barile α/β nasce invece da più cappi β-α-β (crossover connection) ripetuti.")
q("yd3t-04", T, "l", "47", "Quanto è lungo in genere un dominio secondo la sbobina?", [
  "Da 40 a 100 residui", "Da 5 a 10 residui", "Da 300 a 500 residui", "Da 10 a 20 residui", "Più di 1000 residui",
  ], 0,
  "Il dominio è l'unità fondamentale della struttura terziaria e anche un'unità funzionale; si può scomporre in motivi.")

T = "d3-folding"
q("yd3f-01", T, "m", "50", "Perché i residui polari contribuiscono poco all'energia libera del folding in acqua?", [
  "Interagiscono con l'acqua sia nella proteina denaturata sia in quella nativa: non liberano acqua",
  "Formano ponti disolfuro solo dopo il folding e quindi non contano nel bilancio",
  "Sono sempre all'interno della proteina, dove l'acqua non arriva mai",
  "Si caricano solo a pH acido e a pH 7 si comportano come residui apolari",
  "Rompono i clatrati che si formano attorno ai residui apolari e annullano così il loro contributo entropico",
  ], 0,
  "A guidare il folding è il collasso idrofobico: l'acqua liberata dai clatrati aumenta la sua entropia.")
q("yd3f-02", T, "h", "61", "Che differenza c'è tra la proteina disolfuro isomerasi ridotta e quella ossidata nel loro ciclo?", [
  "La ridotta riarrangia ponti sbagliati ed esce ridotta; l'ossidata forma ponti ed esce ridotta, va riossidata",
  "La ridotta forma nuovi ponti disolfuro ed esce ossidata; l'ossidata rompe i ponti ed esce ridotta, va riossidata",
  "La ridotta lavora nel citosol e l'ossidata nei mitocondri, ed escono entrambe ossidate",
  "La ridotta lega le zone idrofobiche esposte, l'ossidata idrolizza ATP per rilasciare la proteina",
  "Entrambe formano un disolfuro misto, ma solo la ridotta ha bisogno di agenti ossidanti",
  ], 0,
  "Agisce nel reticolo endoplasmatico formando un disolfuro misto con la proteina.")
q("yd3f-03", T, "h", "58", "Come agiscono i detergenti come denaturanti, e perché la denaturazione è reversibile?", [
  "Si dispongono attorno alle catene apolari come l'urea; tolti, la proteina può ripiegarsi",
  "Rompono i legami peptidici dello scheletro; tolti, la proteina viene risintetizzata",
  "Riducono i ponti disolfuro come il β-mercaptoetanolo; tolti, i ponti si riformano a caso",
  "Ossidano le cisteine ad acido cisteico; tolti, le cisteine tornano ridotte da sole",
  "Legano il sito attivo come inibitori competitivi; tolti, il sito torna libero",
  ], 0,
  "Con la parte polare interagiscono anche con le catene laterali cariche. Si denatura anche con calore e pH.")
q("yd3f-04", T, "l", "57", "Che effetto ha l'acido performico sulle cisteine?", [
  "Le ossida ad acido cisteico (-SO₃⁻) e impedisce per sempre i ponti disolfuro",
  "Le carbossimetila covalentemente e impedisce per sempre i ponti disolfuro",
  "Le riduce e rompe i ponti disolfuro, che però possono riformarsi",
  "Le converte in cistina formando ponti disolfuro stabili tra le cisteine vicine",
  "Le deamina ad allisina, che forma poi legami crociati tra le catene",
  ], 0,
  "Lo iodoacetato le carbossimetila; β-mercaptoetanolo e DTT sono riducenti.")
q("yd3f-05", T, "l", "61", "Quante molecole di ATP consuma un ciclo completo di GroEL/GroES che rilascia una proteina ripiegata?", [
  "14", "7", "1", "21", "2",
  ], 0,
  "7 ATP per anello di GroEL. Se la proteina non è ripiegata, il ciclo ricomincia nella camera opposta.")
q("yd3f-06", T, "l", "60", "Quanto sono lunghe le subunità di GroEL e di GroES?", [
  "GroEL 547 aa, GroES 97 aa", "GroEL 97 aa, GroES 547 aa", "GroEL 124 aa, GroES 97 aa", "GroEL 547 aa, GroES 153 aa", "GroEL 700 aa, GroES 70 aa",
  ], 0,
  "124 aa è la ribonucleasi A di Anfinsen; 153 la mioglobina.")

T = "d3-quaternaria"
q("yd3q-01", T, "m", "64", "Quali interazioni tengono insieme le subunità nella struttura quaternaria?", [
  "Interazioni deboli (legami a H, salini), interazioni idrofobiche e talvolta ponti disolfuro",
  "Solo legami peptidici tra l'estremità C-terminale di una subunità e l'N-terminale dell'altra",
  "Solo ponti disolfuro, perché le interazioni deboli non bastano a tenere unite le catene",
  "Solo legami a idrogeno tra C=O e N–H degli scheletri delle diverse subunità",
  "Legami glicosidici tra zuccheri legati alla superficie delle varie subunità",
  ], 0,
  "Se l'interfaccia è idrofobica, come accade di solito, la struttura è molto più compatta.")
q("yd3q-02", T, "h", "66", "Un anticorpo viene trattato con un riducente in condizioni denaturanti. Che cosa si ottiene?", [
  "Catene pesanti e leggere separate, perché unite da ponti disolfuro intermolecolari",
  "Un'unica catena lunga, perché pesanti e leggere sono unite da legami peptidici",
  "L'anticorpo intatto, perché le catene sono tenute insieme solo da interazioni idrofobiche",
  "Quattro catene identiche, perché l'anticorpo è un omo-oligomero tetramerico",
  "Due catene ibride pesante-leggera, perché si rompono solo i ponti intracatena",
  ], 0,
  "È un etero-oligomero: due catene pesanti e due leggere, uguali a due a due.")
q("yd3q-03", T, "h", "65", "Da che cosa deriva un tetramero isologo?", [
  "Da due associazioni isologhe, con un dimero ruotato rispetto all'altro",
  "Da quattro associazioni eterologhe in fila lungo un asse, senza chiusura",
  "Da due subunità speculari, una di L- e una di D-amminoacidi",
  "Da un'associazione eterologa chiusa di quattro subunità diverse tra loro",
  "Da un dimero che si duplica per taglio proteolitico in quattro catene",
  ], 0,
  "Nell'associazione isologa due subunità si affacciano con la stessa superficie in modo complementare.")
q("yd3q-04", T, "l", "65", "In quale tipo di simmetria due subunità sono poste a 180° per rotazione attorno a un asse?", [
  "Ciclica", "Diedrica", "Speculare", "Di inversione", "Elicoidale",
  ], 0,
  "La diedrica (D2 la più comune) aggiunge un secondo asse di ordine 2 perpendicolare. Simmetrie speculari o di inversione sono impossibili con L-amminoacidi.")

T = "d3-tecniche"
q("yd3x-01", T, "m", "54", "Che cosa si separa con una centrifuga comune, rispetto all'ultracentrifuga?", [
  "Particelle che sedimentano in fretta: cellule, frammenti, organelli grandi, proteine precipitate",
  "Macromolecole e organelli piccoli, che richiedono fino a 600.000 g e una camera del rotore sotto vuoto",
  "Solo le proteine solubili, separate in base al loro punto isoelettrico",
  "Solo gli acidi nucleici, separati in base alla loro carica netta negativa",
  "Molecole piccole come sali e zuccheri, che passano attraverso una membrana",
  ], 0,
  "L'ultracentrifuga (≈ 80.000 rpm, refrigerata e blindata) serve per organelli più piccoli e macromolecole.")
q("yd3x-02", T, "h", "54", "Hai fatto precipitare una proteina con solfato d'ammonio. Che cosa basta per raccoglierla?", [
  "Una centrifuga comune: il precipitato sedimenta rapidamente",
  "Un'ultracentrifuga a 600.000 g per molte ore con il rotore sotto vuoto",
  "Una dialisi, che trattiene il precipitato sulla membrana",
  "Uno spettrofotometro, che misura l'assorbanza a 280 nm",
  "Un polarimetro, che separa le molecole otticamente attive",
  ], 0,
  "Il solfato d'ammonio sfrutta la solubilità: la proteina precipitata si comporta come una particella pesante.")
q("yd3x-03", T, "h", "23", "In una preparazione proteica vuoi eliminare sali e piccole molecole senza perdere la proteina. Quale tecnica usi?", [
  "La dialisi, che sfrutta le dimensioni maggiori delle proteine",
  "La precipitazione selettiva, che sfrutta il cambio di temperatura",
  "La centrifugazione a 500 g, che sedimenta le piccole molecole",
  "L'elettroforesi su strato sottile di silice idrofobica",
  "La riduzione con β-mercaptoetanolo dei ponti disolfuro",
  ], 0,
  "Le piccole molecole attraversano la membrana; la proteina resta dentro.")
q("yd3x-04", T, "l", "54", "Nella procedura descritta, dopo la centrifugazione a 500 g per 10 minuti, che cosa resta nel sopranatante?", [
  "Le membrane e le molecole solubili", "Le cellule non lisate", "I frammenti cellulari grossolani e i nuclei", "Solo i nuclei", "Nulla: sedimenta tutto",
  ], 0,
  "Una centrifugazione più forte separa poi i mitocondri; tempi ancora più lunghi separano microsomi e citosol.",
  note="Sbobina di Biochimica I, p. 54: indica 100.000 g per 20 minuti per separare i mitocondri. Di solito i mitocondri sedimentano già a ≈ 15.000–20.000 g; 100.000 g servono per i microsomi (Lehninger). La sequenza delle frazioni resta corretta.")
