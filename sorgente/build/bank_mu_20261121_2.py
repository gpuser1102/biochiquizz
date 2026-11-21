"""Giro 2026-11-21, blocco 2 – Biochimica I, biologia molecolare: trascrizione (p. 241–244),
controllo dell'espressione genica (p. 245–253), RNA (p. 253–260); terpeni e derivati del colesterolo (p. 207–208)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Trascrizione (p. 241–244) ───────────────────────────────────────────────
T = "d13-trascrizione"
q("u1121-054", T, "f", "241", "Come si chiama la sequenza di DNA riconosciuta prima del sito di inizio della trascrizione?", [
  "Promotore",
  "Operatore",
  "Terminatore",
  "Origine",
  "Introne",
  ], 0,
  "Il promotore precede il sito di inizio (+1); l'operatore è la sequenza vicina al promotore a cui si legano i regolatori nei batteri.")
q("u1121-055", T, "m", "241", "Dove si trovano le regioni conservate dei promotori di E. coli?", [
  "A circa −10 e −35 paia di basi dal sito di inizio",
  "A circa +10 e +35 paia di basi dal sito di inizio",
  "A circa −25 e −70 paia di basi dal sito di inizio",
  "Tra −7 e +6 paia di basi rispetto al sito di inizio",
  "Solo a valle, all'interno della sequenza trascritta",
  ], 0,
  "Due esameri conservati a −10 e −35: se mutati, hanno effetti marcati sulla trascrizione. −25 e −70 sono TATA box e CCAAT box dei promotori dell'RNA polimerasi II.")
q("u1121-056", T, "m", "242", "Il nucleo α₂ββ' dell'RNA polimerasi di E. coli ha attività polimerasica ma non inizia la trascrizione nel punto giusto. Perché?", [
  "Gli manca σ, che riconosce il promotore e vi porta l'enzima",
  "Gli manca un'elicasi separata, che deve aprire la doppia elica",
  "Gli manca un primer di RNA, necessario per iniziare la catena",
  "Gli manca il fattore ρ, che aggancia l'enzima al sito +1",
  "Gli manca una pinza ad anello, che gli dà la processività",
  ], 0,
  "α: assemblaggio e interazione con i regolatori; β e β': centro catalitico; σ: riconoscimento del promotore.")
q("u1121-057", T, "a", "242", "Quale differenza tra RNA polimerasi e DNA polimerasi è corretta?", [
  "L'RNA polimerasi svolge da sé la doppia elica e non ha bisogno di un primer",
  "L'RNA polimerasi ha bisogno di un primer di DNA e di un'elicasi separata",
  "L'RNA polimerasi sintetizza in direzione 3'→5' e usa desossiribonucleotidi",
  "L'RNA polimerasi ha un'esonucleasi 5'→3' con cui rimuove i primer",
  "L'RNA polimerasi copia contemporaneamente i due filamenti dello stesso gene",
  ], 0,
  "Le RNA polimerasi hanno un'attività elicasica intrinseca e incorporano ribonucleotidi trifosfato. Che non serva un primer non è scritto nelle sbobine (Lehninger).")
q("u1121-058", T, "l", "243", "Che cosa succede alla subunità σ quando l'RNA polimerasi batterica passa all'allungamento?", [
  "Si dissocia, e il nucleo dell'enzima prosegue da solo fino al terminatore",
  "Resta legata e guida l'enzima fino al terminatore, dove si stacca con ρ",
  "Viene sostituita dal fattore ρ, che garantisce la processività dell'enzima",
  "Si lega al promotore successivo e vi attende il nucleo dell'enzima libero",
  "Viene degradata, e la cellula ne sintetizza una nuova a ogni trascritto",
  ], 0,
  "Secondo la sbobina σ si stacca quando l'RNA nascente è lungo 10–12 nucleotidi; il nucleo α₂ββ' continua fino al sito di terminazione.")
q("u1121-059", T, "f", "243", "Con quale tipo di nucleotide inizia quasi sempre l'mRNA batterico?", [
  "Una purina",
  "Una pirimidina",
  "Un desossinucleotide",
  "Un nucleotide metilato",
  "Una uridina",
  ], 0,
  "L'RNA polimerasi comincia la sintesi quasi sempre con una purina (ATP o GTP).")
q("u1121-060", T, "f", "243", "Quale RNA polimerasi eucariotica sintetizza i precursori degli mRNA?", [
  "RNA polimerasi II",
  "RNA polimerasi I",
  "RNA polimerasi III",
  "RNA polimerasi mitocondriale",
  "Primasi",
  ], 0,
  "Pol I: precursori degli rRNA nel nucleolo; pol II: precursori degli mRNA; pol III: tRNA, rRNA 5S e snRNA.")
q("u1121-061", T, "l", "243", "Quale RNA polimerasi eucariotica trascrive tRNA e rRNA 5S, e dove si trova il suo promotore?", [
  "La III, con il promotore a valle del sito di inizio",
  "La I, con il promotore a monte, nel nucleolo",
  "La II, con il TATA box a circa −25",
  "La III, con TATA box e CCAAT box a monte",
  "La I, anche lei con il promotore a valle del sito di inizio",
  ], 0,
  "La pol III ha promotori interni, a valle del sito di inizio; la pol II usa TATA box (−25), CCAAT box (−70) ed enhancer.")
q("u1121-062", T, "m", "244", "Che cosa provoca il legame della TBP al TATA box?", [
  "Una piega a gomito del DNA, segnale per l'arrivo degli altri fattori",
  "L'apertura della doppia elica grazie all'idrolisi di ATP",
  "La fosforilazione della coda C-terminale dell'RNA polimerasi II",
  "Il distacco del repressore dall'operatore vicino al promotore",
  "La metilazione del promotore e la conseguente compattazione della cromatina",
  ], 0,
  "La TBP riconosce due solchi maggiori adiacenti e piega il DNA: è il segnale strutturale per l'assemblaggio del complesso di inizio.")
q("u1121-063", T, "h", "244", "In quale ordine si assemblano i fattori del complesso di pre-inizio dell'RNA polimerasi II, secondo la sbobina?", [
  "TBP → TFIIB → TFIIF con la polimerasi → TFIIE → TFIIH",
  "TFIIB → TBP → TFIIH → TFIIF con la polimerasi → TFIIE",
  "TBP → TFIIH → TFIIE → TFIIB → TFIIF con la polimerasi",
  "TFIIF con la polimerasi → TBP → TFIIB → TFIIH → TFIIE",
  "TBP → TFIIE → TFIIF con la polimerasi → TFIIB → TFIIH",
  ], 0,
  "TBP piega il DNA; TFIIB lega TBP e TFIIF; TFIIF porta la polimerasi; TFIIE recluta per ultimo TFIIH, che fosforila la coda C-terminale.")
q("u1121-064", T, "h", "244", "Un farmaco blocca solo l'attività chinasica del TFIIH. Che cosa succede alla trascrizione dei geni dell'RNA polimerasi II?", [
  "Il complesso di pre-inizio si forma, ma la polimerasi non parte perché la coda C-terminale resta non fosforilata",
  "La TBP non riesce più a legare il TATA box, quindi il complesso di pre-inizio non si forma per niente sul promotore",
  "La polimerasi inizia l'allungamento, ma non riconosce più i segnali di terminazione alla fine del gene",
  "Il TFIIB non lega più la TBP, quindi la polimerasi viene reclutata su sequenze casuali del genoma",
  "La polimerasi trascrive normalmente, ma i fattori di trascrizione restano legati al promotore dopo la partenza",
  ], 0,
  "La fosforilazione della coda C-terminale fa disassemblare il complesso di pre-inizio e libera la polimerasi verso l'allungamento.",
  note="Errore nella sbobina (Biochimica I, p. 244): attribuisce al TFIIE l'attività ATPasica ed elicasica che svolge la doppia elica. Secondo Lehninger e Stryer l'elicasi è il TFIIH (che ha anche l'attività chinasica); il TFIIE serve a reclutare il TFIIH.")
q("u1121-065", T, "m", "244", "Perché il riconoscimento del promotore eucariotico richiede tanti fattori che si legano in sequenza?", [
  "Aumenta la specificità ed evita legami aspecifici della polimerasi al DNA",
  "Aumenta la velocità con cui la polimerasi allunga l'RNA lungo il gene",
  "Permette alla polimerasi di sintetizzare il primer di RNA iniziale",
  "Permette di correggere gli errori di incorporazione dei ribonucleotidi nell'RNA",
  "Serve a staccare gli istoni da tutto il gene prima della trascrizione",
  ], 0,
  "Più passaggi di riconoscimento riducono il rischio di trascrivere sequenze che non devono essere trascritte.")
q("u1121-066", T, "a", "243", "Il complesso chiuso RNA polimerasi-promotore ha KD tra 10⁻⁶ e 10⁻⁹ M, quello aperto 10⁻¹⁴ M. Che cosa significa?", [
  "Il complesso aperto, con il DNA svolto, è molto più stabile di quello chiuso",
  "Il complesso chiuso è il più stabile, perché il DNA non è ancora svolto",
  "Il complesso aperto si dissocia più facilmente, per permettere l'allungamento",
  "I due complessi hanno la stessa stabilità, ma il chiuso si forma più in fretta",
  "Il complesso aperto lega σ con più affinità, ma il DNA con meno affinità",
  ], 0,
  "KD più bassa = affinità più alta: dopo lo svolgimento del DNA al promotore il complesso aperto è molto stabile.")

# ── Controllo dell'espressione genica (p. 245–253) ──────────────────────────
T = "d13-espressione"
q("u1121-067", T, "f", "245", "Quale fattore σ di E. coli dirige l'espressione dei geni costitutivi (housekeeping)?", [
  "σ70",
  "σ32",
  "σ54",
  "σS (σ38)",
  "ρ",
  ], 0,
  "σ70 è il fattore primario; gli altri sono alternativi e servono a gruppi di geni specifici.")
q("u1121-068", T, "l", "245", "Quale abbinamento fattore σ – geni di E. coli è corretto?", [
  "σ32 – geni indotti dallo shock termico",
  "σ54 – geni indotti dalla fase stazionaria",
  "σ70 – geni del metabolismo dell'azoto",
  "σS – geni indotti dallo shock termico",
  "σ32 – geni costitutivi (housekeeping)",
  ], 0,
  "σ70 housekeeping; σ54 metabolismo dell'azoto; σ32 shock termico; σS (σ38) fase stazionaria.")
q("u1121-069", T, "f", "245", "Che cos'è un operone?", [
  "Un gruppo di geni per proteine diverse trascritti dallo stesso promotore",
  "Un gene con più promotori, ciascuno dei quali dà una proteina diversa",
  "La sequenza vicino al promotore a cui si lega il repressore trascrizionale",
  "Un gruppo di geni con promotori diversi regolati dalla stessa proteina",
  "Un mRNA eucariotico maturo che contiene gli esoni di più geni diversi",
  ], 0,
  "Un'unica unità trascrizionale (un solo mRNA) per proteine che di solito lavorano insieme nella stessa via. La sequenza del repressore è l'operatore.")
q("u1121-070", T, "l", "247", "Quali proteine codificano i geni lacZ, lacY e lacA?", [
  "β-galattosidasi, galattoside permeasi e transacetilasi",
  "Galattoside permeasi, β-galattosidasi e repressore lac",
  "Repressore lac, β-galattosidasi e transacetilasi",
  "Lattasi, galattochinasi e galattoside permeasi",
  "β-galattosidasi, galattochinasi e repressore lac",
  ], 0,
  "lacZ β-galattosidasi, lacY permeasi, lacA transacetilasi. Il repressore è codificato da lacI, con un suo promotore a monte.")
q("u1121-071", T, "h", "248", "Che effetto ha la delezione del gene lacI in E. coli?", [
  "Le proteine dell'operone lac vengono prodotte sempre, anche senza induttore",
  "Le proteine dell'operone lac non vengono mai prodotte, anche con lattosio",
  "Le proteine dell'operone lac vengono prodotte solo in presenza di glucosio",
  "Viene prodotta solo la β-galattosidasi, perché manca il gene della permeasi",
  "L'operone lac diventa reprimibile e si spegne quando c'è molto lattosio",
  ], 0,
  "lacI codifica il repressore: senza repressore l'operone è espresso in modo costitutivo.")
q("u1121-072", T, "m", "248", "Perché in presenza di lattosio l'operone lac viene trascritto?", [
  "L'induttore lega il repressore e ne cambia la conformazione, così si stacca dall'operatore",
  "Il lattosio lega direttamente l'operatore e ne spinge via il repressore per semplice competizione",
  "Il lattosio attiva l'adenilato ciclasi, e il cAMP prodotto stacca il repressore dal DNA",
  "Il lattosio lega l'RNA polimerasi e ne aumenta l'affinità per il promotore dell'operone",
  "Il lattosio blocca la trascrizione del gene lacI, quindi il repressore non viene prodotto",
  ], 0,
  "Il repressore legato all'induttore perde affinità per il DNA. La sbobina dice «lattosio»; l'induttore fisiologico è il suo isomero allolattosio (Lehninger): semplificazione accettabile.")
q("u1121-073", T, "m", "249", "Nell'operone trp, quando il repressore si lega al DNA?", [
  "Solo dopo aver legato triptofano, che fa da corepressore",
  "Solo quando nella cellula il triptofano è assente",
  "Sempre, ed è il triptofano legato a staccarlo dal DNA",
  "Solo dopo aver legato cAMP, quando il glucosio è basso nel terreno",
  "Solo in presenza di lattosio, che fa da coinduttore",
  ], 0,
  "Operone reprimibile: il repressore (gene trpR) è attivo solo legato al triptofano; senza triptofano i cinque geni vengono trascritti.")
q("u1121-074", T, "h", "249", "Quale confronto tra operone lac e operone trp è corretto?", [
  "In entrambi il repressore attivo blocca la trascrizione; in lac è attivo da libero, in trp da legato all'effettore",
  "In entrambi il repressore attivo è quello legato all'effettore; in lac l'effettore è il prodotto, in trp il substrato",
  "lac è a controllo positivo e trp a controllo negativo, perché in lac il lattosio attiva l'RNA polimerasi",
  "In entrambi l'effettore aumenta l'affinità del repressore per l'operatore e quindi spegne l'operone",
  "lac è reprimibile e trp inducibile, perché nelle vie cataboliche l'effettore è il prodotto finale della via",
  ], 0,
  "Entrambi sono controlli negativi. Vie cataboliche: l'effettore è il substrato (lattosio) e stacca il repressore; vie anaboliche: l'effettore è il prodotto finale (triptofano) e attiva il repressore.")
q("u1121-075", T, "h", "250", "E. coli cresce in un terreno con glucosio e lattosio. Perché l'operone lac è poco trascritto anche se il repressore è staccato?", [
  "Il glucosio abbassa il cAMP, quindi la CRP non può attivare la trascrizione dell'operone",
  "Il glucosio lega il repressore e lo blocca sull'operatore anche in presenza di molto lattosio",
  "Il glucosio alza il cAMP, che lega il repressore e lo stabilizza sull'operatore",
  "Il glucosio sequestra il fattore σ70, che non riconosce più il promotore lac",
  "Il glucosio attiva il fattore ρ, che termina la trascrizione dopo il gene lacZ",
  ], 0,
  "Repressione da catabolita: il glucosio inibisce indirettamente l'adenilato ciclasi; senza cAMP la CRP (attivatore) non lega e la trascrizione resta bassa.")
q("u1121-076", T, "m", "250", "Qual è il segnale della terminazione ρ-indipendente nei batteri?", [
  "Una forcina nell'RNA, da sequenze ripetute invertite, seguita da una serie di U",
  "Una sequenza TATA nel DNA, seguita da una serie di A nel filamento stampo del gene",
  "Il legame del fattore ρ a una forcina dell'RNA, che consuma ATP per staccarlo",
  "Una sequenza palindromica nel DNA a cui si lega il repressore dell'operone",
  "Una coda di poli-A aggiunta all'RNA subito dopo il taglio del trascritto",
  ], 0,
  "La forcina seguita dal poli-U fa perdere affinità alla polimerasi, che rilascia DNA e messaggero. Che la forcina sia ricca in G-C non è nelle sbobine (Lehninger).")
q("u1121-077", T, "m", "251", "Che cos'è il fattore ρ?", [
  "Un'elicasi ATP-dipendente che svolge l'ibrido DNA-RNA e libera il trascritto",
  "Una subunità dell'RNA polimerasi batterica che riconosce il promotore a −10 e −35",
  "Una nucleasi che taglia l'mRNA subito a valle della sequenza poli-U",
  "Una proteina che lega il cAMP e attiva la trascrizione degli operoni",
  "Un repressore che lega l'operatore solo in presenza di triptofano",
  ], 0,
  "È il fattore della terminazione ρ-dipendente.")
q("u1121-078", T, "f", "251", "Quale percentuale dei suoi geni esprime, secondo la sbobina, una tipica cellula umana?", [
  "3–5%",
  "30–50%",
  "80–90%",
  "Meno dello 0,1%",
  "Tutti",
  ], 0,
  "Ogni cellula esprime solo una piccola parte dei suoi geni e adatta l'espressione ai segnali.")
q("u1121-079", T, "a", "251", "Perché l'acetilazione degli istoni favorisce la trascrizione?", [
  "Neutralizza le lisine, così gli istoni diventano meno basici e legano meno il DNA",
  "Aggiunge cariche positive alle lisine, così gli istoni legano di più il DNA e lo aprono",
  "Trasferisce gruppi acetile alle citosine del promotore e così richiama la polimerasi",
  "Stacca l'istone H1 dal nucleosoma, che così si scioglie e libera completamente il DNA",
  "Taglia il DNA linker tra i nucleosomi, che così si allontanano lungo la fibra",
  ], 0,
  "L'acetilazione degli amminoacidi basici riduce l'interazione elettrostatica con il DNA acido e facilita l'accesso del macchinario trascrizionale; la metilazione del DNA ha l'effetto opposto.")
q("u1121-080", T, "h", "251", "Come può un enhancer, lontano dal promotore, stimolare la trascrizione di un gene?", [
  "Lega attivatori che, ripiegando il DNA, vengono portati a contatto con il complesso di inizio",
  "Viene trascritto in un RNA che si appaia al promotore e lo apre per l'RNA polimerasi II",
  "Scorre lungo il DNA fino al promotore e trascina con sé l'RNA polimerasi II",
  "Viene tagliato e riattaccato vicino al promotore, a cui così si avvicina davvero",
  "Rimuove i metili dal promotore a distanza e lo rende accessibile ai fattori",
  ], 0,
  "Gli attivatori legati agli enhancer interagiscono con la polimerasi grazie a un ripiegamento del DNA.")
q("u1121-081", T, "a", "252", "Perché le proteine regolatrici riconoscono la sequenza soprattutto nel solco maggiore?", [
  "Lì ogni coppia di basi espone una combinazione unica di donatori e accettori di legami a idrogeno",
  "Lì sono esposti i gruppi fosfato, che formano legami ionici diversi e specifici per ogni coppia di basi",
  "Lì le basi formano legami covalenti con le catene laterali di asparagina e glutammina",
  "Lì A-T e T-A appaiono uguali, quindi la proteina deve leggere un numero minore di combinazioni",
  "Lì non arrivano gli istoni, che occupano invece il solco minore in tutto il genoma",
  ], 0,
  "Nel solco minore A-T non si distingue da T-A (né G-C da C-G): il solco maggiore è più informativo.")
q("u1121-082", T, "l", "252", "Quanto è maggiore, secondo la sbobina, l'affinità di una proteina regolatrice per la sua sequenza bersaglio rispetto ad altre sequenze?", [
  "10⁴–10⁶ volte",
  "10–100 volte",
  "2–3 volte",
  "10⁹–10¹⁰ volte",
  "10¹⁵ volte",
  ], 0,
  "Non c'è un codice semplice amminoacido-base: la specificità nasce da molti contatti, soprattutto legami a idrogeno.")
q("u1121-083", T, "l", "253", "Quali catene laterali formano più spesso legami a idrogeno con le basi nel solco maggiore?", [
  "Asn, Gln, Lys, Arg",
  "Leu, Ile, Val, Phe",
  "Gly, Ala, Pro, Trp",
  "Met, Cys, Leu, Val",
  "Phe, Tyr, Trp, Pro",
  ], 0,
  "Catene laterali polari o cariche positivamente, capaci di legami a idrogeno.")
q("u1121-084", T, "h", "253", "Quale descrizione dei motivi di legame al DNA è corretta?", [
  "Nella cerniera di leucine due eliche dimerizzano con leucine ogni sette residui, e la regione basica N-terminale lega il DNA",
  "Nell'elica-giro-elica è l'elica 1 a entrare nel solco minore, mentre l'elica 3 media il contatto con altre proteine regolatrici",
  "Nel dito di zinco dei recettori degli ormoni steroidei lo zinco è coordinato da due cisteine e due istidine",
  "Nella cerniera di leucine le leucine sono nella regione N-terminale e legano direttamente le basi del DNA",
  "Nell'elica-ansa-elica è l'ansa a entrare nel solco maggiore, mentre le due eliche legano solo i fosfati",
  ], 0,
  "HTH: l'elica 3 di riconoscimento entra nel solco maggiore. Zinc finger classico: 2 Cys + 2 His; quello dei recettori steroidei: 4 Cys. Leucine zipper ed elica-ansa-elica: eliche per dimerizzare, regione N-terminale basica per il DNA.")

# ── RNA (p. 253–260) ────────────────────────────────────────────────────────
T = "d13-rna"
q("u1121-085", T, "f", "253", "Quale combinazione distingue di solito l'RNA dal DNA?", [
  "Ribosio, uracile e singolo filamento",
  "Deossiribosio, uracile e doppio filamento",
  "Ribosio, timina e singolo filamento",
  "Ribosio, uracile e doppio filamento",
  "Deossiribosio, timina e singolo filamento",
  ], 0,
  "L'RNA è in genere corto e a singolo filamento, ma forma strutture secondarie e terziarie; può contenere basi modificate (tRNA).")
q("u1121-086", T, "l", "254", "Come si chiama la struttura terziaria dell'RNA che si forma quando regioni complementari invertite, anche distanti, si appaiano tra loro?", [
  "Pseudonodo",
  "Forcina",
  "Stem-loop",
  "Trifoglio",
  "Cruciforme",
  ], 0,
  "Forcina (tratto non appaiato piccolo) e stem-loop (tratto più ampio) sono strutture secondarie; il pseudonodo è terziario.")
q("u1121-087", T, "f", "254", "Come appare la struttura del tRNA nel piano e nello spazio?", [
  "A trifoglio nel piano, a forma di L nello spazio",
  "A forma di L nel piano, a trifoglio nello spazio",
  "A forcina semplice nel piano, a pseudonodo nello spazio",
  "A doppia elica continua sia nel piano sia nello spazio",
  "A trifoglio nel piano, a doppia elica lineare nello spazio",
  ], 0,
  "Il trifoglio ha quattro tratti a doppia elica e l'ansa dell'anticodone; nella forma a L l'anticodone non è diametralmente opposto all'amminoacido.")
q("u1121-088", T, "l", "254", "Quali rRNA formano la subunità maggiore del ribosoma eucariotico?", [
  "28S, 5,8S e 5S",
  "23S e 5S",
  "28S, 18S e 5S",
  "18S e 5,8S",
  "23S, 5,8S e 5S",
  ], 0,
  "Eucarioti: 28S, 5,8S e 5S nella maggiore, 18S nella minore. Procarioti: 23S e 5S nella maggiore, 16S nella minore.")
q("u1121-089", T, "f", "254", "Qual è l'RNA più abbondante e più stabile nelle cellule?", [
  "rRNA",
  "mRNA",
  "tRNA",
  "snRNA",
  "miRNA",
  ], 0,
  "L'RNA ribosomiale costituisce le due subunità del ribosoma.")
q("u1121-090", T, "m", "254", "Che cosa sono le strutture cruciformi del DNA?", [
  "Forcine di sequenze palindromiche, appaiate sullo stesso filamento invece che con l'altro",
  "Incroci tra due cromosomi omologhi che si formano durante la ricombinazione meiotica nei gameti",
  "Ibridi DNA-RNA che si formano durante la trascrizione davanti alla polimerasi",
  "Nodi del DNA circolare creati dalle topoisomerasi di tipo II durante la duplicazione",
  "Tratti di DNA avvolti a croce intorno a due ottameri istonici adiacenti",
  ], 0,
  "Le ripetizioni invertite complementari si appaiano nello stesso filamento; queste strutture sono riconosciute da enzimi che tagliano il DNA.")
q("u1121-091", T, "m", "257", "Quale di questi è un RNA catalitico ancora presente nelle cellule?", [
  "L'rRNA 23S, che catalizza la formazione del legame peptidico",
  "L'mRNA, che catalizza la propria traduzione sul ribosoma batterico",
  "Il tRNA, che catalizza il legame del proprio amminoacido",
  "Il miRNA, che catalizza l'aggiunta del cap all'mRNA",
  "L'rRNA 16S, che catalizza la sintesi della coda poli-A",
  ], 0,
  "Ribozimi cellulari: rRNA 23S (peptidil transferasi), snRNA dello spliceosoma, RNasi P, alcuni RNA virali.")
q("u1121-092", T, "l", "257", "Che cos'è la RNasi P?", [
  "Una ribonucleoproteina con subunità catalitica a RNA che matura l'estremità 5' dei tRNA",
  "Una proteina con subunità strutturale a RNA che aggiunge la coda poli-A agli mRNA maturi",
  "Una ribonucleoproteina con subunità catalitica proteica che rimuove gli introni",
  "Un RNA senza proteine che taglia sé stesso in presenza di ioni piombo",
  "Una ribonucleasi proteica che degrada gli mRNA privi di cap e di coda",
  ], 0,
  "La subunità a RNA è catalitica, quella proteica strutturale. La sbobina dice solo che «partecipa alla formazione del 5' nei batteri»: che si tratti dei tRNA è dal Lehninger.")
q("u1121-093", T, "a", "255", "Quale osservazione sostiene l'ipotesi che l'RNA sia stata la molecola ancestrale della vita?", [
  "L'RNA può conservare informazione e catalizzare reazioni, come fanno ancora rRNA e snRNA",
  "Il DNA è più instabile dell'RNA e non avrebbe potuto conservare l'informazione genetica a lungo",
  "Le proteine non riescono a catalizzare nessuna reazione sugli acidi nucleici senza RNA",
  "L'RNA è sempre a doppio filamento e quindi si replica con lo stesso meccanismo del DNA",
  "L'RNA si forma spontaneamente dalla polimerizzazione degli amminoacidi in acqua",
  ], 0,
  "L'RNA ha strutture terziarie simili a quelle delle proteine; i ribozimi attuali sono considerati fossili molecolari.")
q("u1121-094", T, "m", "257", "Quale abbinamento tra acido nucleico terapeutico e meccanismo è corretto?", [
  "siRNA – silenziano l'RNA a cui sono complementari",
  "Aptameri – si appaiano all'mRNA e ne bloccano la traduzione",
  "RNA antisenso – legano proteine grazie a un folding specifico",
  "Ribozimi – legano recettori di membrana come gli anticorpi",
  "Oligonucleotidi antigene – si appaiano all'mRNA nel citosol",
  ], 0,
  "Antisenso: legano l'mRNA. Aptameri: legano molecole bersaglio grazie al folding. Antigene: desossinucleotidi complementari al DNA. Ribozimi: tagliano RNA complementari.")
q("u1121-095", T, "h", "258", "Un riboswitch batterico lega la lisina nel suo dominio aptamero. Che cosa succede ai geni a valle quando la lisina è abbondante?", [
  "Si forma una forcina seguita da poli-U che termina la trascrizione dell'mRNA",
  "Si forma una struttura di antiterminazione e l'mRNA viene trascritto e tradotto",
  "Il riboswitch taglia l'mRNA come un ribozima e ne avvia subito la degradazione",
  "La lisina attiva un repressore proteico che si lega all'operatore del promotore",
  "Il riboswitch recluta un fattore σ alternativo per i geni del metabolismo della lisina",
  ], 0,
  "Legato il ligando, l'aptamero cambia struttura secondaria e si forma un terminatore; senza ligando si forma l'antiterminatore e il gene viene espresso.")
q("u1121-096", T, "a", "258", "Perché i riboswitch sono considerati un possibile bersaglio per nuovi antibiotici?", [
  "Regolano geni importanti per i batteri e non sono stati trovati nei mammiferi",
  "Sono presenti anche nei mammiferi, ma lì legano ligandi molto più grandi e diversi",
  "Sono proteine batteriche con un sito attivo molto diverso da quelli umani",
  "Sono già il bersaglio della maggior parte degli antibiotici oggi in uso",
  "Legano la DNA girasi batterica e ne bloccano l'attività sul cromosoma",
  ], 0,
  "Un farmaco specifico per l'aptamero bloccherebbe geni batterici senza effetti sull'mRNA umano; i riboswitch inoltre legano i ligandi diversamente dalle proteine umane.")
q("u1121-097", T, "m", "258", "Perché gli aptameri sono chiamati «anticorpi chimici»?", [
  "Legano il loro bersaglio con alta affinità e selettività grazie al loro folding",
  "Sono prodotti dalle plasmacellule e circolano nel sangue come immunoglobuline",
  "Hanno la stessa struttura a Y delle immunoglobuline, con due siti di legame",
  "Attivano la cascata del complemento quando si legano al loro bersaglio",
  "Sono piccole proteine sintetiche che imitano la regione variabile degli anticorpi",
  ], 0,
  "Sono acidi nucleici facili da sintetizzare, stabili e privi di immunogenicità; possono anche veicolare farmaci o siRNA nelle cellule bersaglio.")
q("u1121-098", T, "l", "259", "Quale aptamero è stato approvato come farmaco e contro quale bersaglio?", [
  "Pegaptanib, contro il VEGF",
  "Pegaptanib, contro il PDGF",
  "Bevacizumab, contro il VEGF",
  "Pegaptanib, contro il fattore V",
  "Defibrotide, contro il PDGF",
  ], 0,
  "Il pegaptanib è stato poi superato dagli anticorpi monoclonali anti-VEGF.")
q("u1121-099", T, "h", "259", "Quale sequenza della biogenesi dei miRNA nei mammiferi è corretta?", [
  "Pol II trascrive il pri-miRNA → Drosha lo taglia nel nucleo → l'esportina porta il pre-miRNA nel citosol → Dicer → RISC",
  "Pol III trascrive il pre-miRNA → Dicer lo taglia nel nucleo → l'esportina porta il pri-miRNA nel citosol → Drosha → RISC",
  "Pol II trascrive il pre-miRNA → l'esportina lo porta nel citosol → Drosha lo taglia in pri-miRNA → RISC → Dicer",
  "Pol I trascrive il pri-miRNA → Dicer lo taglia nel nucleo → RISC lo porta nel citosol → Drosha lo rende a singolo filamento",
  "Pol II trascrive il pri-miRNA → Dicer lo taglia nel nucleo → l'esportina porta il pre-miRNA nel citosol → Drosha → RISC",
  ], 0,
  "Pri-miRNA (pol II) → Drosha (nucleo) → pre-miRNA → esportina → Dicer (citosol) → RISC con Argonauta → miRNA maturo a singolo filamento.")
q("u1121-100", T, "a", "259", "Che differenza c'è tra miRNA e siRNA, secondo la sbobina?", [
  "I miRNA sono codificati dal nostro genoma, i siRNA derivano da RNA a doppio filamento esogeni",
  "I miRNA derivano da RNA virali a doppio filamento, i siRNA sono codificati dal nostro stesso genoma",
  "I miRNA agiscono nel nucleo sul DNA, i siRNA agiscono solo nel citosol sulle proteine",
  "I miRNA richiedono Dicer e RISC, mentre i siRNA tagliano l'mRNA da soli come ribozimi",
  "I miRNA attivano la traduzione dei bersagli, mentre i siRNA la bloccano degradandoli",
  ], 0,
  "Entrambi agiscono con Dicer e RISC; i siRNA rispondono a RNA estranei (virus, trasposoni, transgeni).")
q("u1121-101", T, "m", "260", "Come può un miRNA legato al suo mRNA bersaglio impedire la sintesi della proteina?", [
  "Tagliando l'mRNA, che poi viene degradato, oppure impedendone la traduzione",
  "Legando il promotore del gene e impedendo il legame dell'RNA polimerasi II al DNA",
  "Aggiungendo all'mRNA una seconda coda di poli-A che lo rende instabile",
  "Legando la proteina appena sintetizzata e marcandola per il proteasoma",
  "Integrandosi nel DNA del gene e interrompendone la sequenza codificante",
  ], 0,
  "L'mRNA tagliato, senza cap o coda poli-A, viene degradato dalle esonucleasi; in alternativa il ribosoma non riesce a procedere.",
  note="Refuso nella sbobina (Biochimica I, p. 260): «non consentono al ribosoma di proseguire la trascrizione»; il ribosoma fa la traduzione.")
q("u1121-102", T, "a", "260", "Quale problema limita la somministrazione sistemica dei siRNA come farmaci?", [
  "Sono grandi, molto polari e vengono degradati dalle RNasi circolanti",
  "Sono piccoli e apolari, quindi attraversano tutte le membrane senza selettività",
  "Vengono riconosciuti come antigeni e neutralizzati dagli anticorpi circolanti",
  "Si integrano nel genoma delle cellule e causano mutagenesi inserzionale",
  "Richiedono la trascrittasi inversa della cellula bersaglio per diventare attivi",
  ], 0,
  "Per questo si preferiscono vie topiche (gocce, aerosol, iniezione intratumorale) o nanocarrier; è anche difficile ottenere una distribuzione specifica per tessuto.")

# ── Terpeni e derivati del colesterolo (p. 207–208) ─────────────────────────
T = "d10-steroidi"
q("u1121-103", T, "f", "207", "Quanti atomi di carbonio ha l'isoprene, l'unità che compone i terpeni?", [
  "5",
  "6",
  "10",
  "15",
  "27",
  ], 0,
  "L'isoprene è un composto a 5 atomi di carbonio con due doppi legami; i terpeni sono suoi polimeri, molto idrofobici.")
q("u1121-104", T, "f", "207", "Di quale molecola è precursore il terpene squalene?", [
  "Colesterolo",
  "Coenzima Q",
  "Vitamina E",
  "Retinolo",
  "Acido arachidonico",
  ], 0,
  "Coenzima Q e vitamine A, E, K sono terpeni anch'essi, ma non derivano dallo squalene; l'acido arachidonico è un acido grasso.")
q("u1121-105", T, "m", "208", "Quale di queste molecole NON deriva dal colesterolo?", [
  "Il coenzima Q",
  "Il cortisolo",
  "La vitamina D",
  "L'acido colico",
  "L'estradiolo",
  ], 0,
  "Dal colesterolo derivano sali biliari, ormoni steroidei e vitamina D; il coenzima Q è un terpene che non passa dal colesterolo.")
q("u1121-106", T, "m", "208", "Che funzione hanno i sali biliari come il colico e il taurocolico?", [
  "Sono tensioattivi che emulsionano i grassi alimentari e ne favoriscono la digestione",
  "Sono ormoni che stimolano la secrezione della lipasi pancreatica nel duodeno",
  "Sono esteri del colesterolo che trasportano i grassi nel sangue dentro le HDL",
  "Sono enzimi che idrolizzano i trigliceridi a livello dell'interfaccia olio-acqua nell'intestino",
  "Sono vitamine liposolubili che regolano l'assorbimento intestinale del calcio",
  ], 0,
  "Hanno un lato idrofobico e uno idrofilico: formano micelle che permettono alla lipasi pancreatica di agire.",
  note="Imprecisione nella sbobina (Biochimica I, p. 208): elenca i sali biliari, gli ormoni steroidei e la vitamina D sotto la voce «Esteri del colesterolo». Sono derivati del colesterolo, non esteri.")
q("u1121-107", T, "a", "208", "Perché gli esteri del colesterolo sono ancora più idrofobici del colesterolo e dove si trovano?", [
  "L'OH in C3 è legato a un acido grasso: senza gruppo polare stanno nel core delle lipoproteine e nelle placche",
  "L'OH in C3 è legato a un fosfato: diventano carichi e si dispongono sulla superficie delle lipoproteine",
  "Gli anelli sono aperti da un acido grasso: diventano lineari e si inseriscono nel doppio strato lipidico di membrana",
  "La catena laterale è legata a una glicina: diventano sali biliari e si accumulano nella colecisti",
  "L'OH in C3 è legato a uno zucchero: diventano glicolipidi e si dispongono sul foglietto esterno",
  ], 0,
  "Esterificando l'unico gruppo polare si ottiene una molecola insolubile: viaggia dentro LDL e HDL ed è il principale costituente delle placche ateromatose. Che l'esterificazione sia sull'OH in C3 è dal Lehninger.")
q("u1121-108", T, "f", "208", "Che cosa sono prednisone e prednisolone?", [
  "Farmaci steroidei con potente attività antinfiammatoria",
  "Sali biliari usati per sciogliere i calcoli della colecisti",
  "Statine che inibiscono l'HMG-CoA reduttasi nel fegato",
  "Precursori vegetali della vitamina D attivati dalla luce",
  "Esteri del colesterolo che viaggiano soprattutto nelle HDL",
  ], 0,
  "Sono derivati sintetici degli ormoni steroidei (glucocorticoidi).")
