"""Giro 2026-11-17, blocco 1 – Biochimica I: mioglobina ed emoglobina (p. 68–94)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Eme e mioglobina (p. 68–72) ────────────────────────────────────────────
T = "d4-eme"
q("u1117-001", T, "f", "70", "Che cos'è l'eme dell'emoglobina?", [
  "Ferro-protoporfirina IX con il ferro allo stato ferroso",
  "Ferro-protoporfirina IX con il ferro allo stato ferrico",
  "Un anello di clorina con il magnesio al centro",
  "Un anello di corrina con il cobalto al centro",
  "Un tetrapirrolo lineare che lega il ferro ferroso",
  ], 0,
  "Quattro anelli pirrolici uniti da ponti metinici; il Fe²⁺ forma 4 legami di coordinazione con gli azoti pirrolici.")
q("u1117-002", T, "f", "69", "Quale residuo coordina il ferro dell'eme dal lato opposto all'O₂?", [
  "Istidina prossimale F8", "Istidina distale E7", "Valina E11", "Fenilalanina CD1", "Istidina prossimale E7"], 0,
  "L'istidina prossimale (elica F) è sempre legata al ferro; la distale (elica E) resta troppo lontana per coordinarlo.")
q("u1117-003", T, "m", "69, 72", "Che ruolo ha l'istidina distale E7 nell'ossimioglobina?", [
  "Forma un legame a idrogeno con l'O₂ legato al ferro",
  "Forma il quinto legame di coordinazione del ferro",
  "Riduce il ferro ferrico a ferroso dopo il distacco",
  "Lega il 2,3-BPG nella cavità centrale della proteina",
  "Forma un ponte salino con l'arginina C-terminale",
  ], 0,
  "I suoi piccoli movimenti aprono anche il canale da cui l'O₂ entra ed esce.")
q("u1117-004", T, "m", "72", "Perché è importante che la tasca dell'eme sia idrofobica?", [
  "Tiene fuori l'acqua: l'eme non si perde e lega l'O₂ in modo reversibile",
  "Attira i protoni: favorisce l'effetto Bohr e la cessione dell'O₂ ai tessuti",
  "Lega la CO₂: forma i carbammati e abbassa l'affinità per l'O₂",
  "Ossida il ferro: lo porta a Fe³⁺ e permette il sesto legame",
  "Fa uscire l'eme: ne permette il ricambio a ogni ossigenazione",
  ], 0,
  "In un ambiente polare e idratato l'eme verrebbe perso e il ferro si ossiderebbe.")
q("u1117-005", T, "a", "72", "L'eme libero lega il CO molto più dell'O₂, ma nella mioglobina il vantaggio del CO si riduce a circa 200 volte. Perché?", [
  "L'istidina distale e i residui vicini ostacolano il legame del CO perpendicolare all'eme",
  "Nella mioglobina il CO ossida il ferro a Fe³⁺ e si stacca subito dopo essersi legato all'eme",
  "La globina lega il CO sul gruppo N-terminale, lontano dalla tasca dell'eme",
  "L'istidina prossimale cede il suo legame col ferro all'O₂ ma non al CO",
  "La tasca idrofobica respinge il CO, che è una molecola più polare dell'O₂",
  ], 0,
  "Il CO preferisce legarsi a 90° rispetto al piano dell'eme, l'O₂ a circa 120°: l'ingombro sterico della globina sfavorisce il CO.",
  note="Sbobina di Biochimica I, p. 72: c'è scritto che il CO si lega «in modo irreversibile». Il legame è reversibile, ma con un'affinità così alta che il CO si stacca molto lentamente (Lehninger). Lehninger indica circa 20.000 volte per l'eme libero; la sbobina dice 25.000.")
q("u1117-006", T, "l", "71", "In quale tipo di eme i gruppi vinilici sono legati covalentemente a due cisteine della proteina?", [
  "Eme c", "Eme b", "Eme a", "Protoporfirina IX libera", "Eme dell'emoglobina"], 0,
  "L'eme b (Hb, Mb) non è legato covalentemente; nell'eme a uno dei vinili porta una catena isoprenica.")
q("u1117-007", T, "m", "70, 72", "Quanti legami di coordinazione forma il Fe²⁺ nell'ossiemoglobina, e con chi?", [
  "6: quattro azoti pirrolici, istidina F8 e O₂",
  "6: quattro azoti pirrolici, istidina E7 e O₂",
  "5: quattro azoti pirrolici e la molecola di O₂",
  "4: soltanto i quattro azoti dell'anello pirrolico",
  "6: quattro azoti pirrolici, istidina F8 e acqua",
  ], 0,
  "L'O₂ forma il sesto legame di coordinazione; nella deossi il sesto posto resta libero.")
q("u1117-008", T, "f", "70", "Come si chiama l'emoglobina con il ferro allo stato ferrico?", [
  "Metaemoglobina", "Carbossiemoglobina", "Carbamminoemoglobina", "Deossiemoglobina", "Emoglobina glicata"], 0,
  "Il Fe³⁺ non può legare l'O₂.")
q("u1117-009", T, "m", "71", "Che cosa distingue la funzione dell'eme dei citocromi da quella dell'eme dell'emoglobina?", [
  "Nei citocromi il ferro alterna Fe²⁺ e Fe³⁺ per trasportare elettroni",
  "Nei citocromi il ferro resta sempre Fe²⁺ per legare l'ossigeno molecolare",
  "Nei citocromi l'eme è privo di ferro e trasporta solo protoni",
  "Nei citocromi il ferro resta Fe³⁺ e serve a legare la CO₂",
  "Nei citocromi l'eme trasporta l'O₂ dentro il mitocondrio",
  ], 0,
  "Nell'emoglobina e nella mioglobina il ferro deve restare ferroso per legare l'O₂.")
q("u1117-010", T, "f", "69", "Quale globina monomerica si trova nei neuroni e si pensa protegga il cervello dall'ipossia?", [
  "Neuroglobina", "Citoglobina", "Mioglobina", "Emoglobina Gower", "Emoglobina A2"], 0,
  "La citoglobina è distribuita in tutti i tessuti e ha funzione meno nota.")
q("u1117-011", T, "l", "72", "Con quale geometria si lega l'O₂ al ferro dell'eme?", [
  "Piegato, a circa 120° rispetto al piano dell'eme",
  "Perpendicolare, a 90° rispetto al piano dell'eme",
  "Parallelo al piano, disteso tra due azoti pirrolici",
  "Lineare, in asse con l'istidina distale E7",
  "Piegato, a 120°, dal lato dell'istidina prossimale",
  ], 0,
  "La geometria piegata è ottimale per un legame reversibile; il CO preferirebbe legarsi a 90°.")

# ── Differenze Hb vs Mb (p. 68, 73–75) ─────────────────────────────────────
T = "d4-hbmb"
q("u1117-012", T, "f", "68", "Quale livello di struttura ha l'emoglobina e non la mioglobina?", [
  "Quaternaria", "Terziaria", "Secondaria", "Primaria", "Supersecondaria"], 0,
  "La mioglobina è un monomero; l'emoglobina è un tetramero α2β2.")
q("u1117-013", T, "f", "73", "Quante molecole di O₂ lega al massimo una molecola di emoglobina?", [
  "4", "1", "2", "8", "6"], 0,
  "Ogni subunità ha un eme. La mioglobina ne lega una sola.")
q("u1117-014", T, "l", "73", "Quanti residui hanno, nell'ordine, la mioglobina, la catena α e la catena β dell'emoglobina?", [
  "153, 141 e 146", "141, 146 e 153", "146, 141 e 153", "153, 146 e 141", "141, 153 e 146"], 0,
  "Lo si ricorda anche dai nomi dei residui C-terminali: Arg141 della α e His146 della β.")
q("u1117-015", T, "m", "73–74", "Mioglobina e catene dell'emoglobina hanno solo circa il 18% di identità di sequenza. Che cosa conservano?", [
  "Un ripiegamento globale molto simile, con otto eliche da A ad H",
  "La stessa sequenza nelle regioni di contatto tra le subunità",
  "Lo stesso numero di residui e la stessa sequenza dell'elica F",
  "La stessa struttura quaternaria, con due protomeri per molecola",
  "Lo stesso numero di gruppi eme, quattro per ogni catena",
  ], 0,
  "Pochi residui (9) sono conservati in tutte le globine perché essenziali alla funzione.")
q("u1117-016", T, "a", "74", "Nell'emoglobina alcuni residui apolari avvicinano le catene tra loro; nella mioglobina gli stessi siti sono per lo più polari. Perché?", [
  "Nella mioglobina, unica catena, quei residui sono esposti al solvente",
  "Nella mioglobina quei residui legano il 2,3-BPG, che è molto carico",
  "Nella mioglobina quei residui formano la tasca idrofobica dell'eme",
  "Nella mioglobina quei residui legano l'ossigeno con legami a idrogeno",
  "Nella mioglobina quei residui servono a formare dimeri con altre Mb",
  ], 0,
  "Dove nell'Hb c'è un'interfaccia tra subunità, nella Mb c'è acqua.")
q("u1117-017", T, "m", "73, 75", "Quanto vale il coefficiente di Hill della mioglobina e quello dell'emoglobina?", [
  "1 e circa 2,8", "4 e 1", "1 e 4", "0 e circa 2,8", "circa 2,8 e 1"], 0,
  "Pendenza 1 = nessuna cooperatività; 4 sarebbe la cooperatività massima teorica per quattro siti.")
q("u1117-018", T, "a", "75", "La p50 è circa 26 mmHg per l'emoglobina e pochi mmHg per la mioglobina. Che cosa ne deriva?", [
  "L'Hb cede O₂ alle pO₂ dei tessuti, la Mb lo trattiene",
  "La Mb cede O₂ alle pO₂ dei tessuti, l'Hb lo trattiene",
  "L'Hb ha più affinità e si satura prima nei polmoni",
  "Hb e Mb cedono la stessa frazione di O₂ nei tessuti",
  "La Mb lega 4 O₂ e l'Hb uno solo a basse pressioni",
  ], 0,
  "Una p50 più alta vuol dire affinità più bassa: è ciò che serve a una proteina di trasporto.")
q("u1117-019", T, "h", "75", "Durante uno sforzo la pO₂ nel muscolo scende a circa 20 mmHg. Che cosa succede a emoglobina e mioglobina?", [
  "L'Hb cede gran parte dell'O₂, la Mb resta in buona parte satura",
  "Hb e Mb restano entrambe sature oltre il 90% di siti occupati",
  "La Mb cede quasi tutto il suo O₂, l'Hb resta quasi satura",
  "Hb e Mb cedono la stessa frazione dell'O₂ che trasportano",
  "L'Hb passa in forma R e lega più O₂ di quanto ne leghi a riposo",
  ], 0,
  "A 20 mmHg la sbobina riporta saturazione circa 0,32 per l'Hb e 0,88 per la Mb; a 100 mmHg sono simili.")
q("u1117-020", T, "l", "68", "Come si chiamano i dimeri α1β1 e α2β2, così compatti da comportarsi come unità?", [
  "Protomeri", "Domini", "Oligomeri", "Monomeri", "Motivi"], 0,
  "I due protomeri formano il tetramero.")
q("u1117-021", T, "m", "68", "Quanto O₂ porta un litro di sangue grazie all'emoglobina, rispetto all'O₂ solo disciolto?", [
  "Circa 200 ml contro circa 3 ml",
  "Circa 70 ml contro circa 30 ml",
  "Circa 20 ml contro circa 3 ml",
  "Circa 200 ml contro circa 100 ml",
  "Circa 3 ml contro circa 200 ml",
  ], 0,
  "L'O₂ è poco solubile in acqua (0,1 mM). Ai tessuti ne vengono ceduti circa 70 ml per litro.")

# ── Legame dell'O₂ all'Hb (p. 75–79) ───────────────────────────────────────
T = "d4-legame"
q("u1117-022", T, "m", "75–76", "Che cosa succede al ferro dell'eme quando lega l'O₂?", [
  "Rientra nel piano dell'eme e trascina con sé l'elica F",
  "Esce dal piano dell'eme e si allontana dall'istidina prossimale",
  "Si ossida a Fe³⁺ e resta fuori dal piano dell'eme",
  "Perde il legame con l'istidina prossimale F8",
  "Si sposta verso l'istidina distale E7 e la lega",
  ], 0,
  "Nella deossi il ferro è un po' fuori dal piano (eme «a cupola»); il piccolo spostamento dell'elica F avvia il cambio conformazionale.",
  note="Sbobina di Biochimica I, p. 75: indica uno spostamento di circa 0,3 Å; Lehninger e Stryer riportano circa 0,4 Å. Differenza minima, non rilevante all'esame.")
q("u1117-023", T, "a", "76", "Come si passa dalla forma T alla forma R dell'emoglobina?", [
  "Il protomero α1β1 ruota di circa 15° rispetto ad α2β2",
  "Il protomero α1β1 ruota di circa 90° rispetto ad α2β2",
  "Le catene α si staccano dalle β e si riassociano",
  "La coppia α1α2 ruota di circa 15° rispetto a β1β2",
  "Si rompono i ponti disolfuro tra i due protomeri",
  ], 0,
  "Cambiano i contatti di scorrimento: si rompono i ponti salini della forma T e se ne formano di nuovi.")
q("u1117-024", T, "m", "76, 88", "Quali contatti tra subunità cambiano nella transizione T → R?", [
  "Quelli di scorrimento all'interfaccia α1β2, ricchi di ponti salini",
  "Quelli di impaccamento all'interfaccia α1β1, idrofobici",
  "I ponti disolfuro che uniscono le catene α alle catene β",
  "I legami covalenti tra il gruppo eme e la catena di globina",
  "Quelli di impaccamento all'interfaccia α1α2, ricchi di ponti salini",
  ], 0,
  "Per questo le mutazioni all'interfaccia α1β2 sono tra le più gravi: possono bloccare la transizione.")
q("u1117-025", T, "l", "77", "Nella forma T, con quali residui forma ponti salini l'His146 C-terminale delle catene β?", [
  "Asp94 della catena β e Lys40 della catena α",
  "Asp126 e Lys127 della catena α",
  "Arg141 della catena α e Val34",
  "His143 e Lys82 della catena β",
  "Asp94 della catena α e Lys40 della catena β",
  ], 0,
  "L'His146 protonata contribuisce all'effetto Bohr: deve essere carica per formare il ponte con l'Asp94.",
  note="Sbobina di Biochimica I, p. 77: colloca l'Asp94 sulla catena β2. Secondo Lehninger l'His146 lega l'Asp94 della sua stessa catena β e la Lys40 della catena α del protomero opposto.")
q("u1117-026", T, "a", "77", "Che cosa fa lo ione cloruro nella forma T dell'emoglobina?", [
  "Fa da ponte tra l'N-terminale di α2 e l'Arg141 di α1, entrambi positivi",
  "Fa da ponte tra l'His146 e l'Asp94, che altrimenti si respingerebbero tra loro",
  "Si lega al ferro dell'eme al posto dell'O₂ e lo mantiene ferroso",
  "Neutralizza il 2,3-BPG nella cavità centrale tra le catene β",
  "Rompe i ponti salini della forma T e favorisce la forma R",
  ], 0,
  "Il cloruro stabilizza la forma T: è uno dei modulatori allosterici negativi, insieme a H⁺, CO₂ e 2,3-BPG.")
q("u1117-027", T, "m", "78", "Perché l'istidina è un buon sensore di pH nell'emoglobina?", [
  "Ha un pKa intorno a 6: piccole variazioni di pH la protonano o deprotonano",
  "Ha un pKa intorno a 12,5: a pH neutro è sempre protonata e carica positiva",
  "Ha un pKa intorno a 4: a pH neutro è sempre deprotonata e negativa",
  "Ha un pKa intorno a 10: si protona soltanto in condizioni di alcalosi",
  "Non ha gruppi ionizzabili in catena laterale e risponde solo all'O₂",
  ], 0,
  "L'arginina invece (pK 12,5) a pH fisiologico è sempre protonata.")
q("u1117-028", T, "m", "78–79", "Che cosa distingue il modello sequenziale dal modello concertato?", [
  "Il sequenziale ammette forme ibride con subunità T e R insieme",
  "Il concertato ammette forme ibride con subunità T e R insieme",
  "Il sequenziale esclude che la forma R esista senza O₂ legato",
  "Il concertato prevede quattro stati intermedi obbligati, uno per O₂",
  "Il sequenziale vale solo per proteine monomeriche come la Mb",
  ], 0,
  "Nel concertato la proteina è tutta T o tutta R; nel sequenziale il cambiamento è graduale, subunità per subunità.")
q("u1117-029", T, "a", "78", "Secondo il modello concertato, quale affermazione è corretta?", [
  "La forma R esiste anche senza O₂, ma in assenza di O₂ prevale la T",
  "La forma R esiste solo quando tutti e quattro i siti hanno O₂",
  "La forma T esiste solo in assenza di O₂ e scompare al primo legame",
  "Le subunità cambiano conformazione una alla volta, in sequenza",
  "In assenza di O₂ forma T e forma R sono presenti in quantità uguali",
  ], 0,
  "Il legame dell'O₂ sposta l'equilibrio verso R. Anche la forma T con O₂ legato è possibile, ma poco popolata.")
q("u1117-030", T, "h", "78", "Immagina un'emoglobina bloccata nella forma R, con curva iperbolica ad alta affinità. Che cosa succederebbe?", [
  "Si caricherebbe nei polmoni ma cederebbe pochissimo O₂ ai tessuti",
  "Si caricherebbe poco nei polmoni ma cederebbe tutto l'O₂ ai tessuti",
  "Avrebbe un coefficiente di Hill vicino a 4 e cooperatività massima",
  "Avrebbe una p50 più alta e cederebbe più O₂ ai tessuti periferici",
  "Non sentirebbe il CO e cederebbe O₂ ai tessuti solo in acidosi",
  ], 0,
  "La sigmoide nasce dal passaggio T → R: bassa affinità dove serve cedere O₂, alta dove serve caricarlo.")
q("u1117-031", T, "h", "75", "Nel grafico di Hill dell'emoglobina i tratti iniziale e finale hanno pendenza 1, quello centrale circa 2,8. Come si interpreta?", [
  "Agli estremi i siti legano senza cooperare; al centro avviene la transizione T → R",
  "Agli estremi la cooperatività è massima; al centro le subunità sono tutte indipendenti",
  "Il tratto centrale indica che ogni tetramero lega in media 2,8 molecole di O₂",
  "La pendenza 1 indica che l'emoglobina resta in forma R in tutto il grafico",
  "Il tratto centrale misura la p50 della mioglobina usata come riferimento",
  ], 0,
  "Il tratto iniziale corrisponde alla forma T (log K1), quello finale alla forma R (log K4).")
q("u1117-032", T, "l", "75", "Di quanto aumenta l'affinità per l'O₂ tra il primo e il quarto O₂ che si lega all'emoglobina?", [
  "Circa 100 volte", "Circa 4 volte", "Circa 10 volte", "Circa 10.000 volte", "Non cambia"], 0,
  "Secondo la sbobina la p50 della subunità passa da circa 30 a circa 0,3 mmHg.")

# ── Modulatori allosterici (p. 79–83) ──────────────────────────────────────
T = "d4-modulatori"
q("u1117-033", T, "f", "79–80", "Che cos'è l'effetto Bohr?", [
  "La riduzione dell'affinità dell'Hb per l'O₂ quando aumentano H⁺ e CO₂",
  "L'aumento dell'affinità dell'Hb per l'O₂ quando aumentano H⁺ e CO₂",
  "La riduzione dell'affinità dell'Hb per l'O₂ dovuta al solo 2,3-BPG",
  "Il legame cooperativo dell'O₂ alle quattro subunità dell'emoglobina",
  "L'ossidazione del ferro dell'eme quando il pH del sangue diventa più acido",
  ], 0,
  "Nei tessuti l'Hb cattura protoni e cede O₂; nei polmoni l'O₂ fa rilasciare i protoni.")
q("u1117-034", T, "m", "80", "Come si lega la CO₂ direttamente all'emoglobina?", [
  "Ai gruppi amminici N-terminali, come carbammato, liberando H⁺",
  "Ai gruppi amminici N-terminali, come carbammato, legando H⁺",
  "Al ferro dell'eme, al posto dell'O₂, come sesto legame",
  "Alle istidine distali, come bicarbonato, legando i protoni liberi",
  "Al 2,3-BPG nella cavità centrale, come estere fosforico",
  ], 0,
  "La carbamminoemoglobina abbassa l'affinità per l'O₂, e i protoni liberati rinforzano l'effetto Bohr.",
  note="Sbobina di Biochimica I, p. 80: c'è scritto che la carbamminoemoglobina «non lega l'ossigeno». Più precisamente il carbammato stabilizza la forma T e ne riduce l'affinità, senza impedire il legame (Lehninger).")
q("u1117-035", T, "f", "81", "Nei capillari dei tessuti il bicarbonato esce dall'eritrocita. Che cosa entra in cambio?", [
  "Il cloruro, tramite lo scambiatore di anioni",
  "Il sodio, tramite la pompa Na⁺/K⁺-ATPasi",
  "Il potassio, tramite un canale ionico",
  "Il fosfato, tramite lo scambiatore di anioni",
  "Il lattato, tramite un trasportatore di monocarbossilati",
  ], 0,
  "Serve a mantenere l'elettroneutralità. Anche il cloruro entrato si lega alla deossiemoglobina.")
q("u1117-036", T, "h", "82", "Che cosa succede nei capillari polmonari quando l'emoglobina si ossigena?", [
  "Rilascia H⁺, che riformano CO₂ dal bicarbonato rientrato in cambio di Cl⁻",
  "Lega H⁺, che trasformano la CO₂ in bicarbonato e lo fanno uscire in cambio di Cl⁻",
  "Rilascia 2,3-BPG, che porta fuori la CO₂ in cambio di ioni cloruro",
  "Lega CO₂ come carbammato e la trasporta fino al cuore sinistro",
  "Rilascia Cl⁻ e lega bicarbonato, che resta nell'eritrocita",
  ], 0,
  "L'anidrasi carbonica lavora al contrario: HCO₃⁻ + H⁺ → CO₂, che viene espirata. Il pH leggermente più alcalino favorisce l'ossigenazione.")
q("u1117-037", T, "f", "80", "Quale enzima dell'eritrocita converte la CO₂ in acido carbonico?", [
  "Anidrasi carbonica", "Carbammil fosfato sintetasi", "Piruvato carbossilasi", "Bisfosfoglicerato mutasi", "Carbossipeptidasi"], 0,
  "L'acido carbonico si dissocia subito in HCO₃⁻ e H⁺.")
q("u1117-038", T, "m", "83", "Dove si lega il 2,3-BPG nell'emoglobina?", [
  "Nella cavità centrale della deossi-Hb, tra le catene β",
  "Nella cavità centrale dell'ossi-Hb, tra le catene α",
  "Nella tasca dell'eme di ciascuna delle quattro subunità",
  "Sui gruppi N-terminali delle catene α, come carbammato",
  "Sull'istidina distale E7 di ciascuna catena β",
  ], 0,
  "Nel passaggio T → R la cavità si restringe e il 2,3-BPG viene espulso: ne lega uno per tetramero.",
  note="Sbobina di Biochimica I, p. 83: attribuisce gli N-terminali e l'istidina 2 alle catene α. Il sito è formato solo dalle catene β: Val1, His2, Lys82 e His143 di entrambe (Lehninger, Stryer).")
q("u1117-039", T, "l", "83", "Quali residui positivi formano il sito di legame del 2,3-BPG?", [
  "Val1, His2, Lys82 e His143 delle due catene β",
  "Val1, His2, Lys82 e His143 delle due catene α",
  "His146, Asp94 e Lys40 delle due catene β",
  "Arg141, Asp126 e Lys127 delle due catene α",
  "His92, Phe85 e Leu88 delle due catene β",
  ], 0,
  "In tutto 8 cariche positive che trattengono il 2,3-BPG, molto carico negativamente.",
  note="Sbobina di Biochimica I, p. 83: attribuisce gli N-terminali e l'istidina 2 alle catene α; sono invece residui delle catene β.")
q("u1117-040", T, "a", "82–83", "Salendo ad alta quota, dopo qualche ora, il 2,3-BPG negli eritrociti raddoppia. A che cosa serve?", [
  "Sposta la curva a destra e aumenta l'O₂ ceduto ai tessuti",
  "Sposta la curva a sinistra e aumenta l'O₂ caricato nei polmoni",
  "Sposta la curva a destra e aumenta l'O₂ caricato nei polmoni",
  "Stimola subito la sintesi di eritropoietina e di nuovi eritrociti",
  "Abbassa il pH e attiva l'effetto Bohr solo a livello polmonare",
  ], 0,
  "L'eritropoietina renale è la risposta a lungo termine, più lenta.")
q("u1117-041", T, "h", "82–83", "Il sangue conservato a lungo per le trasfusioni perde gran parte del 2,3-BPG. Che cosa ti aspetti subito dopo la trasfusione?", [
  "Hb ad alta affinità che cede poco O₂ ai tessuti finché il 2,3-BPG non si riforma",
  "Hb a bassa affinità che non riesce più a caricare l'O₂ a livello polmonare",
  "Hb che perde la cooperatività e assume una curva identica a quella della Mb",
  "Hb che si ossida a metaemoglobina perché manca il 2,3-BPG che normalmente la protegge",
  "Hb che lega più CO₂ come carbammato e diventa insensibile all'effetto Bohr",
  ], 0,
  "Senza 2,3-BPG la curva è molto spostata a sinistra. L'esempio delle trasfusioni non è nelle sbobine (Lehninger).")
q("u1117-042", T, "h", "80", "Un paziente è in acidosi (pH del sangue 7,2). Che cosa succede al trasporto dell'O₂?", [
  "Nei polmoni la saturazione cambia poco, nei tessuti l'Hb cede più O₂",
  "Nei polmoni la saturazione crolla, nei tessuti l'Hb cede meno O₂",
  "La curva si sposta a sinistra e l'Hb trattiene l'O₂ nei tessuti periferici",
  "La saturazione resta identica a quella di pH 7,4 ovunque",
  "L'Hb lega più 2,3-BPG ma meno H⁺, e la curva non si sposta",
  ], 0,
  "È l'effetto Bohr: la sbobina mostra che a 100 mmHg le curve a pH 7,2 e 7,4 quasi coincidono, mentre cambia l'O₂ ceduto in periferia.")
q("u1117-043", T, "l", "83", "Come si distinguono allo spettro di assorbimento la deossiemoglobina e l'ossiemoglobina?", [
  "Deossi: un solo picco intorno a 555 nm; ossi: due picchi",
  "Ossi: un solo picco intorno a 555 nm; deossi: due picchi",
  "Deossi e ossi: un solo picco intorno a 280 nm",
  "Deossi: due picchi a 280 e 555 nm; ossi: un picco",
  "Deossi: nessun picco nel visibile; ossi: due picchi",
  ], 0,
  "Lo spettro dell'eme permette di distinguere anche ferro ossidato e ridotto.")

# ── HbF, emoglobine fisiologiche, geni (p. 84–88) ──────────────────────────
T = "d4-hbf"
q("u1117-044", T, "f", "84–86", "Da quali catene è formata l'emoglobina fetale (HbF)?", [
  "α2γ2", "α2β2", "α2δ2", "ζ2ε2", "β4"], 0,
  "Le catene γ sostituiscono le β e hanno la stessa funzione.")
q("u1117-045", T, "m", "84", "Perché l'HbF ha più affinità per l'O₂ dell'HbA materna?", [
  "Le catene γ hanno serina al posto dell'His143 e legano meno 2,3-BPG",
  "Le catene γ hanno valina al posto del Glu6 e legano meno 2,3-BPG",
  "Le catene γ hanno serina al posto dell'His146 e non hanno effetto Bohr",
  "Le catene γ hanno una lisina in più e legano più 2,3-BPG",
  "L'HbF è un monomero e si comporta come la mioglobina",
  ], 0,
  "Così il feto può prendere l'O₂ ceduto dall'Hb materna nella placenta.")
q("u1117-046", T, "f", "86", "Da quali catene è formata l'HbA2?", [
  "α2δ2", "α2γ2", "α2β2", "ζ2ε2", "γ4"], 0,
  "È presente in piccola quantità nell'adulto ed è un parametro diagnostico delle emoglobinopatie.",
  note="Sbobina di Biochimica I, p. 86: dice che l'HbA2 dopo la nascita «viene sostituita dall'HbA» e che è patologica sopra il 2,5%. In realtà l'HbA2 resta per tutta la vita (circa 2–3,5% dell'Hb dell'adulto) e un valore aumentato, oltre circa 3,5%, orienta verso la β-talassemia minor.")
q("u1117-047", T, "m", "86", "Che cos'è l'emoglobina glicata (HbA1c)?", [
  "Hb con glucosio legato in modo non enzimatico all'N-terminale delle catene β",
  "Hb con glucosio legato da una glicosiltransferasi all'N-terminale delle catene β",
  "Hb con glucosio legato al ferro dell'eme, al posto della molecola di O₂",
  "Hb con glucosio legato in modo non enzimatico all'istidina distale E7",
  "Hb con 2,3-BPG legato in modo covalente alla cavità centrale delle catene β",
  ], 0,
  "Il glucosio reagisce con il gruppo amminico N-terminale formando una base di Schiff, poi una chetoammina.",
  note="Sbobina di Biochimica I, p. 86: c'è scritto che la glicemia è controllata «da insulina e glutatione». Si intende insulina e glucagone.")
q("u1117-048", T, "a", "86–87", "Perché l'HbA1c informa sulla glicemia dei tre mesi precedenti e non di quel giorno?", [
  "La glicazione è lenta e si accumula per tutta la vita dell'eritrocita",
  "La glicazione è rapida ma l'HbA1c viene eliminata ogni tre mesi dal rene",
  "La glicazione è catalizzata da un enzima indotto dall'insulina in tre mesi",
  "L'HbA1c si forma solo nel midollo, al momento della sintesi dell'Hb",
  "La glicazione è reversibile in poche ore e riflette la glicemia del momento",
  ], 0,
  "Con glicemia costante il livello di HbA1c è costante; dopo settimane di iperglicemia aumenta. La vita media dell'eritrocita (circa 120 giorni) non è nelle sbobine.")
q("u1117-049", T, "l", "86", "Quale sequenza descrive la formazione dell'HbA1c?", [
  "Base di Schiff → chetoammina → forma ciclica tipo deossifruttosio",
  "Chetoammina → base di Schiff → forma ciclica tipo deossifruttosio",
  "Base di Schiff → emiacetale → glucosio ciclico legato all'eme",
  "Estere fosforico → base di Schiff → glucosio ciclico sulle catene α",
  "Legame glicosidico → base di Schiff → forma ciclica tipo deossiribosio",
  ], 0,
  "Lo spostamento del doppio legame sul C2 (riarrangiamento di Amadori: il nome non è nelle sbobine) è lento e poco reversibile.")
q("u1117-050", T, "f", "87", "Su quale cromosoma si trovano i geni della catena β e delle catene simili (ε, γ, δ)?", [
  "11", "16", "22", "6", "X"], 0,
  "Le catene α e ζ sono sul cromosoma 16; la mioglobina sul 22.")
q("u1117-051", T, "a", "88–89", "Perché le varianti delle catene β si manifestano più spesso di quelle delle catene α?", [
  "I geni β sono 2: un allele mutato tocca il 50% delle catene β",
  "I geni β sono 4: un allele mutato tocca il 25% delle catene β",
  "I geni α sono 2: una loro mutazione è sempre letale in utero",
  "Le catene β sono più lunghe e hanno molti più siti mutabili",
  "I geni β non hanno introni e quindi mutano più facilmente",
  ], 0,
  "I geni α sono quattro (due per cromosoma 16): un allele mutato tocca solo il 25% delle catene α.")
q("u1117-052", T, "m", "85–86", "In che ordine compaiono le emoglobine durante lo sviluppo?", [
  "Gower-1 (ζ2ε2) → HbF (α2γ2) → HbA (α2β2)",
  "HbF (α2γ2) → Gower-1 (ζ2ε2) → HbA (α2β2)",
  "Gower-1 (ζ2ε2) → HbA (α2β2) → HbF (α2γ2)",
  "HbA2 (α2δ2) → HbF (α2γ2) → HbA (α2β2)",
  "HbF (α2γ2) → HbA (α2β2) → Gower-1 (ζ2ε2)",
  ], 0,
  "Nei cromosomi 11 e 16 i geni sono disposti nell'ordine in cui si attivano durante lo sviluppo.")
q("u1117-053", T, "l", "87–88", "Quale esone del gene delle globine codifica la regione che contiene la tasca dell'eme?", [
  "L'esone 2", "L'esone 1", "L'esone 3", "Gli esoni 1 e 3", "L'introne 1"], 0,
  "Esone 1: eliche A-B; esone 2: tratti C-F con la tasca dell'eme; esone 3: eliche G-H.")
q("u1117-054", T, "h", "84–85", "Nell'eritrocita una piccola quota di emoglobina si ossida a metaemoglobina. Che cosa la riporta in forma funzionale?", [
  "La metaemoglobina reduttasi, che usa NADH per ridurre il Fe³⁺ a Fe²⁺",
  "La glutatione reduttasi, che usa NADPH per ridurre il Fe³⁺ a Fe²⁺",
  "La superossido dismutasi, che usa il superossido per ridurre il Fe³⁺",
  "La metaemoglobina reduttasi, che usa NADPH per ossidare il Fe²⁺",
  "La catalasi, che usa H₂O₂ per ridurre il Fe³⁺ dell'eme a Fe²⁺",
  ], 0,
  "Il superossido che si forma viene smaltito da superossido dismutasi e glutatione perossidasi; il glutatione è poi ridotto dalla glutatione reduttasi con NADPH.",
  note="Sbobina di Biochimica I, p. 84: fa nascere il superossido dalla reazione della metaemoglobina reduttasi. Il superossido si forma quando l'ossiemoglobina si autossida a metaemoglobina (Fe²⁺–O₂ → Fe³⁺ + O₂•⁻); la reduttasi poi riporta il ferro a Fe²⁺.")

# ── Mutazioni dell'emoglobina (p. 88–94) ───────────────────────────────────
T = "d4-mutazioni"
q("u1117-055", T, "f", "89", "Quale sostituzione causa l'emoglobina S?", [
  "Glu6 → Val nelle catene β", "Glu6 → Lys nelle catene β", "Glu6 → Val nelle catene α", "His146 → Asp nelle catene β", "Val6 → Glu nelle catene β"], 0,
  "Un residuo acido sostituito da uno apolare: nella deossi-Hb crea un sito «appiccicoso».",
  note="Sbobina di Biochimica I, p. 89: c'è scritto «valina o alanina». Nell'HbS la sostituzione è solo Glu → Val; più avanti la sbobina stessa riporta la valina.")
q("u1117-056", T, "m", "92", "Che cosa distingue l'HbC dall'HbS?", [
  "Nell'HbC il Glu6 delle catene β è sostituito da una lisina, non da una valina",
  "Nell'HbC il Glu6 delle catene α è sostituito da una valina, non da una lisina",
  "Nell'HbC è sostituita l'His146 delle catene β, che diventa un aspartato",
  "Nell'HbC manca uno dei geni β, mentre nell'HbS i geni sono entrambi presenti",
  "Nell'HbC la Val6 delle catene β diventa glutammato, che rende la Hb instabile",
  ], 0,
  "Entrambe sono frequenti in Africa e, secondo studi recenti citati a lezione, ostacolano l'adesione degli eritrociti infettati dal plasmodio.")
q("u1117-057", T, "h", "92", "Perché l'HbS polimerizza soprattutto nella forma deossi?", [
  "Solo nella deossi la Val6 trova la tasca idrofobica (Phe85, Leu88) di un'altra Hb",
  "Solo nella deossi la Val6 forma ponti disolfuro con le cisteine di un'altra Hb",
  "Solo nella ossi la tasca della Phe85 è libera, e la deossi forma i ponti salini",
  "Solo nella deossi il 2,3-BPG fa da ponte tra le catene β di due molecole vicine",
  "Solo nella deossi il ferro si ossida e due gruppi eme di molecole vicine si legano",
  ], 0,
  "Si formano fibre di 14 filamenti che irrigidiscono e deformano l'eritrocita. Con il Glu6, o nella forma ossi, non succede.",
  note="Sbobina di Biochimica I, p. 92: nel tratto Phe85–Leu88 cita «l'istidina 87, l'istidina prossimale». La tasca è formata da Phe85 e Leu88 della catena β; l'istidina prossimale della catena β è la His92 (F8), quella della catena α è la His87.")
q("u1117-058", T, "a", "93", "Perché gli eterozigoti per l'HbS sono protetti dalla malaria grave?", [
  "Il plasmodio acidifica l'eritrocita, che falcizza e viene rimosso dalla milza",
  "Il plasmodio non riesce a entrare negli eritrociti che contengono HbS",
  "L'HbS lega il plasmodio e lo uccide producendo specie reattive dell'ossigeno",
  "Il plasmodio alcalinizza l'eritrocita e l'HbS non cede più O₂ al parassita",
  "L'HbS ha più affinità per l'O₂ e il plasmodio muore per mancanza di ossigeno",
  ], 0,
  "Il pH più basso (circa 0,4 unità) favorisce la forma deossi, che polimerizza. Si riduce anche l'adesione ai capillari.")
q("u1117-059", T, "a", "89", "Perché la sostituzione His146 → Asp nelle catene β riduce l'effetto Bohr?", [
  "L'aspartato è sempre negativo a pH fisiologico e non cambia protonazione",
  "L'aspartato è sempre positivo a pH fisiologico e lega troppo forte il 2,3-BPG",
  "L'aspartato coordina il ferro dell'eme e lo ossida a Fe³⁺",
  "L'aspartato rende la tasca dell'eme polare e fa perdere l'eme",
  "L'aspartato forma un ponte disolfuro che blocca la forma T",
  ], 0,
  "L'His146 (pKa circa 6) è uno dei principali sensori di H⁺: protonata, forma il ponte salino che stabilizza la forma T.")
q("u1117-060", T, "h", "89", "Una mutazione aumenta l'affinità dell'emoglobina per l'O₂. Che cosa ci si aspetta di solito?", [
  "Policitemia, che compensa il minor rilascio di O₂ ai tessuti",
  "Policitemia, che compensa il maggior rilascio di O₂ ai tessuti",
  "Anemia emolitica, perché gli eritrociti si rompono più facilmente",
  "Cianosi, perché il ferro dell'eme si ossida a Fe³⁺",
  "Ipossia, perché l'Hb non riesce a caricarsi nei polmoni",
  ], 0,
  "La curva si sposta a sinistra: l'Hb lega bene l'O₂ ma lo cede male.")
q("u1117-061", T, "l", "89", "Nell'emoglobina M Boston, quale residuo sostituisce l'istidina distale E7 delle catene α?", [
  "Tirosina", "Valina", "Serina", "Glutammato", "Lisina"], 0,
  "La tirosina lega il ferro e lo stabilizza come Fe³⁺: metaemoglobina e cianosi.")
q("u1117-062", T, "h", "89", "In una variante instabile la Phe42 (CD1) delle catene β è sostituita da serina. Qual è il meccanismo del danno?", [
  "La serina polare richiama acqua nella tasca idrofobica e l'eme viene perso",
  "La serina lega il ferro e lo ossida a Fe³⁺, come nelle emoglobine M",
  "La serina crea un sito appiccicoso e l'emoglobina polimerizza in fibre",
  "La serina sostituisce l'istidina prossimale e l'eme non è più coordinato",
  "La serina blocca il legame del 2,3-BPG e la curva si sposta molto verso sinistra",
  ], 0,
  "Mutazioni che idratano la tasca dell'eme fanno perdere l'eme e con esso la funzione.")
q("u1117-063", T, "h", "94", "In un paziente tre dei quattro geni α non funzionano e si forma HbH (β4). Perché non serve ai tessuti?", [
  "Resta in forma R: lega bene l'O₂ ma non lo cede, senza cooperatività né effetto Bohr",
  "Resta in forma T: non lega l'O₂ nei polmoni e non mostra cooperatività né effetto Bohr",
  "Polimerizza in fibre come l'HbS e deforma gli eritrociti nei capillari",
  "Ha il ferro ossidato a Fe³⁺ e causa cianosi, come le emoglobine M",
  "Lega il 2,3-BPG in modo irreversibile e non si satura mai di O₂",
  ], 0,
  "Mancano le interfacce α1β2 la cui alterazione permette la transizione T → R. Lo stesso vale per l'Hb di Bart (γ4).")
q("u1117-064", T, "m", "93", "Che cosa distingue una talassemia da un'emoglobinopatia come l'HbS?", [
  "Nella talassemia un gene globinico non è espresso; nell'HbS la catena c'è ma è mutata",
  "Nella talassemia la catena c'è ma è mutata; nell'HbS un gene globinico non è espresso",
  "Nella talassemia è colpito l'eme; nell'HbS è colpita la parte proteica della molecola",
  "Nella talassemia mancano gli enzimi della glicolisi; nell'HbS manca il 2,3-BPG",
  "Nella talassemia il ferro è Fe³⁺; nell'HbS la catena β è sostituita dalla γ",
  ], 0,
  "α-talassemia: uno o più geni α non espressi; β-talassemia: uno o entrambi i geni β non espressi.")
q("u1117-065", T, "h", "89", "Nell'emoglobina M Milwaukee la Val E11 della catena β è sostituita da glutammato. Che cosa succede?", [
  "Il glutammato occupa il posto dell'O₂ e stabilizza il ferro come Fe³⁺",
  "Il glutammato occupa il posto dell'O₂ e riduce il ferro a Fe⁺",
  "Il glutammato rompe un ponte salino della forma T e aumenta l'affinità",
  "Il glutammato rende la tasca polare e l'eme si stacca dalla globina",
  "Il glutammato crea un sito appiccicoso che fa polimerizzare l'Hb",
  ], 0,
  "Come nell'Hb M Boston, il risultato è metaemoglobina con minore affinità per l'O₂.",
  note="Sbobina di Biochimica I, p. 89: c'è scritto che il glutammato «causa la riduzione del ferro». È il contrario: il carbossilato stabilizza il ferro ossidato (Fe³⁺), cioè la metaemoglobina.")
q("u1117-066", T, "m", "91–92", "Perché nell'anemia falciforme ci sono crisi dolorose e rischio di infarti?", [
  "Gli eritrociti rigidi e falcizzati si impilano e ostruiscono i capillari",
  "Gli eritrociti falcizzati cedono troppo O₂ e i tessuti vanno in iperossia",
  "L'HbS lega il CO con più affinità e blocca il trasporto dell'ossigeno",
  "L'HbS perde l'eme, che si deposita nei vasi e li infiamma",
  "Gli eritrociti falcizzati sono più grandi e non passano dai polmoni",
  ], 0,
  "Le fibre di HbS rendono l'eritrocita rigido e fragile: si ha anche emolisi. Negli eterozigoti le manifestazioni sono più lievi.")
q("u1117-067", T, "l", "94", "Che cos'è l'emoglobina di Bart?", [
  "Un tetramero γ4", "Un tetramero β4", "Un tetramero α4", "Un tetramero ζ2ε2", "Un tetramero α2δ2"], 0,
  "Si forma quando mancano le catene α nel periodo fetale; l'HbH è invece β4.")
