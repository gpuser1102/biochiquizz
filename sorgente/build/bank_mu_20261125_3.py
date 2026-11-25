"""Giro 2026-11-25, blocco 3 – rifiniture sugli argomenti meno coperti di Biochimica I
(inibizione e regolazione degli enzimi, acidi grassi, steroidi) e due errori di Biochimica II."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Inibizione enzimatica (p. 144–148) ─────────────────────────────────────
C = "d6-inibizione"

q("u1125-201", C, "f", "144", "Che cosa caratterizza un inibitore irreversibile?", [
  "Forma un legame covalente con l'enzima, che non torna più attivo",
  "Si lega con legami deboli e si stacca semplicemente diluendo la soluzione",
  "Compete con il substrato e viene spostato da alte [S]",
  "Si lega solo al complesso ES e lo blocca in modo reversibile",
  "Riduce la sintesi dell'enzima agendo sul suo gene",
  ], 0,
  "Gli inibitori reversibili (competitivi, incompetitivi, non competitivi) usano legami non covalenti; l'irreversibile modifica covalentemente l'enzima (es. DIPF sulla serina dell'acetilcolinesterasi).")

q("u1125-202", C, "m", "144", "Nel grafico dei doppi reciproci, come appaiono le rette con e senza un inibitore competitivo?", [
  "Si incrociano sull'asse y: stessa 1/Vmax, pendenza maggiore con l'inibitore",
  "Sono parallele: cambiano entrambe le intercette, la pendenza resta uguale",
  "Si incrociano sull'asse x: stessa −1/Km, 1/Vmax maggiore con l'inibitore",
  "Coincidono: l'inibitore competitivo non si vede nel grafico dei doppi reciproci",
  "Si incrociano nel secondo quadrante, sopra l'asse x e a sinistra dell'asse y",
  ], 0,
  "Con l'inibitore competitivo la Vmax non cambia (stessa intercetta y) e la Km apparente aumenta (pendenza Km/Vmax maggiore). Parallele = incompetitivo; incrocio sull'asse x = non competitivo puro.")

q("u1125-203", C, "l", "147", "Un inibitore misto lega l'enzima libero più di quanto leghi il complesso ES (α > α'). Che cosa succede a Km e Vmax apparenti?", [
  "La Km aumenta e la Vmax diminuisce",
  "La Km diminuisce e la Vmax diminuisce",
  "La Km resta uguale e la Vmax diminuisce",
  "La Km aumenta e la Vmax resta uguale",
  "La Km diminuisce e la Vmax resta uguale",
  ], 0,
  "Km apparente = αKm/α' e Vmax apparente = Vmax/α'. Con α > α' la Km sale; la Vmax scende sempre. Se α = α' (non competitivo puro) la Km non cambia. La formula non è nelle sbobine (Lehninger).")

q("u1125-204", C, "m", "148", "Perché insetticidi come il parathion e gas come il sarin causano paralisi?", [
  "Inibiscono in modo irreversibile l'acetilcolinesterasi e l'acetilcolina resta alta",
  "Bloccano il recettore dell'acetilcolina e impediscono l'apertura del canale",
  "Inibiscono la colina acetiltransferasi e l'acetilcolina non viene più prodotta nei neuroni",
  "Degradano l'acetilcolina nella fessura sinaptica prima che arrivi al recettore",
  "Inibiscono in modo reversibile la pompa Na⁺/K⁺ della fibra muscolare",
  ], 0,
  "Come il DIPF, sono organofosfati che si legano covalentemente alla serina del sito attivo dell'acetilcolinesterasi: l'acetilcolina non viene idrolizzata e i canali ionici restano attivati.")

q("u1125-205", C, "a", "146", "Perché un inibitore incompetitivo è più efficace quando la concentrazione di substrato è alta?", [
  "Lega solo il complesso ES, che è più abbondante quando [S] è alta",
  "Lega solo l'enzima libero, che è più abbondante quando [S] è alta",
  "Compete con il substrato e lo sposta quando [S] è alta",
  "Si lega al substrato libero e ne abbassa la concentrazione",
  "Aumenta la Km e quindi richiede più substrato per agire",
  ], 0,
  "L'inibitore incompetitivo si lega solo dopo la formazione di ES e forma ESI, che non procede: più ES c'è, più bersaglio trova. È l'opposto del competitivo, che viene spostato da alte [S]. Il ragionamento non è esplicito nelle sbobine.")

# ── Regolazione dell'attività enzimatica (p. 148–154) ──────────────────────
C = "d6-regolazione"

q("u1125-206", C, "f", "154", "A quale classe di enzimi appartiene una fosfatasi che toglie un fosfato da una proteina?", [
  "Idrolasi, perché usa l'acqua per staccare il fosfato",
  "Trasferasi, perché sposta il fosfato su un'altra molecola",
  "Liasi, perché rompe il legame senza usare acqua",
  "Ligasi, perché consuma ATP per la reazione",
  "Isomerasi, perché cambia la forma della proteina",
  ], 0,
  "La chinasi (trasferasi) usa ATP per fosforilare; la fosfatasi è un'idrolasi che riporta l'enzima nella forma non fosforilata.")

q("u1125-207", C, "h", "154", "La sbobina presenta la fosforilazione come il processo che «permette l'attivazione dell'enzima». Che cosa è corretto?", [
  "Dipende dall'enzima: la fosforilasi si attiva, PDH e glicogeno sintasi si inattivano",
  "È sempre così: ogni enzima fosforilato è più attivo di quello defosforilato",
  "È il contrario: la fosforilazione inattiva sempre l'enzima bersaglio",
  "La fosforilazione cambia solo la localizzazione dell'enzima nella cellula, mai la sua attività",
  "La fosforilazione attiva solo gli enzimi delle vie anaboliche",
  ], 0,
  "⚠️ Generalizzazione della sbobina: l'esempio (fosforilasi b → a) è giusto, ma la fosforilazione può anche inattivare. Le sbobine di Biochimica II mostrano piruvato deidrogenasi e glicogeno sintasi inattive quando fosforilate.",
  note="La sbobina di Biochimica I (p. 154) dice che le fosforilazioni «permettono l'attivazione dell'enzima»: vale per la glicogeno fosforilasi, non in generale.")

q("u1125-208", C, "m", "154", "Quale modificazione covalente reversibile usa il NAD⁺ come donatore?", [
  "L'ADP-ribosilazione",
  "L'adenilazione",
  "L'uridilazione",
  "La metilazione",
  "La fosforilazione",
  ], 0,
  "ADP-ribosilazione: dal NAD⁺ (con rilascio di nicotinammide) su Arg, Gln, Cys o diftammide. Adenilazione da ATP e uridilazione da UTP su Tyr; metilazione da S-adenosilmetionina su Glu; fosforilazione da ATP su Ser, Thr, Tyr, His.")

q("u1125-209", C, "a", "148", "Quale meccanismo di regolazione degli enzimi è il più lento a produrre effetto?", [
  "Il controllo della quantità di enzima, cioè della sua sintesi",
  "Il legame di un effettore allosterico al sito regolatorio",
  "La fosforilazione dell'enzima da parte di una chinasi",
  "L'inibizione a feedback da parte del prodotto finale della via",
  "L'inibizione competitiva da parte di un analogo del substrato",
  ], 0,
  "Allosteria, feedback e modificazioni covalenti agiscono in secondi o minuti su enzimi già presenti; regolare la sintesi (trascrizione e traduzione) richiede ore. La scala dei tempi non è nelle sbobine.")

# ── Steroidi e terpeni (p. 207–208) ────────────────────────────────────────
C = "d10-steroidi"

q("u1125-210", C, "l", "207", "Quali vitamine sono terpeni secondo la sbobina?", [
  "A, E e K",
  "A, D e K",
  "D, E e K",
  "B12, C e E",
  "Solo la vitamina D",
  ], 0,
  "Tra i terpeni (polimeri dell'isoprene) la sbobina mette le vitamine A, E, K, il coenzima Q e lo squalene. La vitamina D deriva invece dal colesterolo.")

q("u1125-211", C, "a", "208", "Secondo la sbobina, come possono gli esteri del colesterolo accumulati nelle placche portare a una trombosi?", [
  "La placca crea turbolenza, che attiva il fattore di von Willebrand e la coagulazione",
  "Gli esteri del colesterolo attivano direttamente la protrombina in trombina",
  "Gli esteri del colesterolo inibiscono l'antitrombina e la proteina C",
  "La placca consuma la vitamina K e blocca la carbossilazione dei fattori",
  "Gli esteri del colesterolo legano il plasminogeno e bloccano la fibrinolisi fisiologica del coagulo",
  ], 0,
  "Gli esteri del colesterolo sono insolubili, viaggiano in LDL e HDL e sono i principali costituenti delle placche ateromatose; l'ostruzione genera turbolenza e può innescare la coagulazione tramite il vWF.")

# ── Acidi grassi (p. 199–201) ──────────────────────────────────────────────
C = "d10-acidigrassi"

q("u1125-212", C, "f", "199", "Quanti atomi di carbonio hanno di solito gli acidi grassi, secondo la sbobina?", [
  "Tra 14 e 24",
  "Tra 2 e 6",
  "Tra 6 e 10",
  "Tra 30 e 50",
  "Sempre 16",
  ], 0,
  "La lunghezza media va da 14 a 24 atomi di carbonio (l'intervallo completo indicato in tabella è 4–36).")

q("u1125-213", C, "l", "199", "Qual è il nome sistematico dell'acido palmitico?", [
  "Acido n-esadecanoico",
  "Acido n-ottadecanoico",
  "Acido n-tetradecanoico",
  "Acido n-dodecanoico",
  "Acido n-eicosanoico",
  ], 0,
  "Palmitico 16:0 = esadecanoico; stearico 18:0 = ottadecanoico; miristico 14:0 = tetradecanoico; laurico 12:0 = dodecanoico; arachico 20:0 = eicosanoico.")

q("u1125-214", C, "f", "201", "Che cosa distingue un trigliceride semplice (puro) da uno misto?", [
  "Nel semplice i tre acidi grassi sono uguali, nel misto sono diversi",
  "Il semplice ha un acido grasso, il misto ne ha tre",
  "Il semplice è saturo, il misto contiene doppi legami",
  "Il semplice ha come scheletro il glicerolo, il misto ha la sfingosina",
  "Il semplice è di origine animale, il misto vegetale",
  ], 0,
  "In entrambi il glicerolo è esterificato con tre acidi grassi; i grassi naturali sono miscele complesse di trigliceridi semplici e misti.")

q("u1125-215", C, "h", "200", "La sbobina elenca linoleico, linolenico e arachidonico come acidi grassi essenziali. Che cosa è corretto?", [
  "Sono essenziali linoleico e α-linolenico; l'arachidonico si forma dal linoleico",
  "Sono essenziali tutti e tre, perché l'organismo non ne sintetizza nessuno",
  "È essenziale solo l'arachidonico; gli altri due si formano da esso",
  "Nessuno è essenziale: l'uomo sa inserire doppi legami anche oltre il C9 della catena",
  "Sono essenziali palmitico e oleico, che forniscono gli altri tre",
  ], 0,
  "⚠️ Imprecisione della sbobina: i mammiferi non introducono doppi legami oltre il C9, quindi servono linoleico (ω-6) e α-linolenico (ω-3) con la dieta; l'arachidonico si forma dal linoleico per allungamento e desaturazione e diventa essenziale solo se manca il linoleico (Lehninger).",
  note="La sbobina di Biochimica I (p. 200) mette l'arachidonico tra gli acidi grassi essenziali: lo è solo in carenza di linoleico.")

# ── Digestione dei grassi (p. 220) ─────────────────────────────────────────
q("u1125-216", "d12-digestione", "l", "220", "Da quale ione dipende la lipasi pancreatica, secondo la sbobina?", [
  "Ca²⁺",
  "Mg²⁺",
  "Zn²⁺",
  "Fe²⁺",
  "Cu²⁺",
  ], 0,
  "La sbobina la descrive come enzima Ca²⁺-dipendente, attivo solo all'interfaccia olio-acqua. Non è nelle sbobine che lavora con la colipasi, che la ancora alla goccia lipidica.")

# ── Classificazione e cinetica (p. 110, 118) ───────────────────────────────
q("u1125-217", "d6-classificazione", "l", "110", "Che cosa traslocano gli enzimi della sottoclasse EC 7.1?", [
  "Ioni idronio (H⁺)",
  "Cationi inorganici come Na⁺ e K⁺",
  "Anioni inorganici come Cl⁻",
  "Amminoacidi e peptidi",
  "Carboidrati e loro derivati",
  ], 0,
  "EC 7.1 idronio, 7.2 cationi inorganici, 7.3 anioni inorganici, 7.4 amminoacidi e peptidi, 7.5 carboidrati, 7.6 altri composti. La sotto-sottoclasse indica la reazione che fornisce l'energia.")

q("u1125-218", "d6-cinetica", "m", "118", "Che cosa indica l'ordine di una reazione?", [
  "L'esponente della concentrazione nell'equazione cinetica, che può differire dalla molecolarità",
  "Il numero di molecole che si urtano nel passaggio elementare, sempre uguale alla molecolarità",
  "Il numero di prodotti che si formano per ogni molecola di reagente consumata dalla reazione",
  "La posizione della reazione nella sequenza della via metabolica a cui appartiene",
  "Il rapporto tra le costanti di velocità della reazione diretta e di quella inversa",
  ], 0,
  "v = k[A]ⁿ: n è l'ordine. La molecolarità conta i reagenti (mono-, bimolecolare); ordine e molecolarità non sempre coincidono, come nel pseudo-primo ordine.")

# ── Biochimica II: mobilizzazione dei trigliceridi (p. 178) ────────────────
q("u1125-219", "m7-trasporto", "h", "178", "La sbobina dice che glucagone e adrenalina mobilizzano i grassi legandosi allo stesso recettore, un β-adrenergico. Che cosa è corretto?", [
  "Il glucagone ha un suo GPCR; condivide con i recettori β solo la via Gs-cAMP-PKA",
  "Il glucagone lega davvero i recettori β-adrenergici, ma con un'affinità molto minore",
  "Il glucagone lega un recettore tirosin-chinasico, l'adrenalina un GPCR",
  "Il glucagone lega un recettore nucleare, l'adrenalina un recettore β",
  "Il glucagone lega i recettori α2, che attivano una proteina Gi",
  ], 0,
  "⚠️ Imprecisione della sbobina: glucagone e adrenalina hanno recettori diversi, entrambi a 7 eliche accoppiati a Gs; convergono su adenilato ciclasi, cAMP e PKA, che fosforila perilipine e lipasi ormone-sensibile.",
  note="La sbobina di Biochimica II (p. 178) descrive un unico recettore β-adrenergico per glucagone e adrenalina: il glucagone ha un recettore proprio.",
  src="Biochimica II")

q("u1125-220", "m7-lipoproteine", "h", "216", "La sbobina dice che le HDL «hanno solo colesterolo». Che cosa è corretto?", [
  "Sono le lipoproteine più ricche di proteine e contengono anche fosfolipidi",
  "Contengono solo colesterolo libero, senza proteine né fosfolipidi",
  "Contengono soprattutto trigliceridi, come i chilomicroni",
  "Contengono solo esteri del colesterolo, senza alcuna apolipoproteina",
  "Sono le lipoproteine meno dense perché sono le più povere di proteine",
  ], 0,
  "⚠️ Imprecisione della sbobina: le HDL sono le più dense perché le più ricche di proteine (ApoA-I) e contengono molti fosfolipidi; il colesterolo, esterificato dalla LCAT, è solo una parte (Lehninger).",
  note="La sbobina di Biochimica II (p. 216) scrive che le HDL «hanno solo colesterolo».",
  src="Biochimica II")
