"""Giro 2026-11-17, blocco 3 – Biochimica I, enzimi: localizzazione delle vie e marcatori (p. 128–130),
meccanismi catalitici (p. 130–143), inibizione (p. 144–148), regolazione (p. 148–154)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Localizzazione delle vie ed enzimi come marcatori (p. 128–130) ─────────
T = "d6-marcatori"
q("u1117-124", T, "f", "128", "Quale abbinamento via metabolica – compartimento è corretto?", [
  "Ciclo di Krebs – mitocondrio",
  "Sintesi degli acidi grassi – mitocondrio",
  "Glicolisi – mitocondrio",
  "Ossidazione degli acidi grassi – citosol",
  "Via dei pentoso fosfati – lisosoma",
  ], 0,
  "Mitocondrio: Krebs, β-ossidazione, decarbossilazione del piruvato. Citosol: glicolisi, via dei pentoso fosfati (HMP), sintesi degli acidi grassi. Lisosomi: degradazione delle biomolecole complesse.")
q("u1117-125", T, "a", "129", "Perché nel sospetto di un infarto si dosano insieme creatina chinasi e lattato deidrogenasi?", [
  "La CK sale presto e sparisce in circa due giorni, la LDH resta più a lungo: insieme datano l'evento",
  "La CK è specifica del cuore e la LDH del fegato: insieme dicono quale dei due organi è stato danneggiato",
  "La CK sale solo dopo una settimana e la LDH subito: insieme coprono le prime ore dall'evento",
  "La CK misura l'estensione dell'infarto e la LDH la sua sede: servono entrambe per la terapia",
  "La CK e la LDH salgono e scendono insieme: il doppio dosaggio serve solo a confermare il dato",
  ], 0,
  "Se si dosasse solo la CK, un infarto avvenuto due giorni prima potrebbe sfuggire.",
  note="Sbobina di Biochimica I, p. 129–130: scrive «cheratinachinasi». L'enzima è la creatina chinasi (CK).")
q("u1117-126", T, "f", "129", "Perché l'aumento di un enzima nel sangue può indicare il danno di un organo?", [
  "Molti enzimi sono tipici di certi tessuti e passano nel sangue quando le cellule si danneggiano",
  "Gli enzimi sono prodotti dal fegato solo quando un altro organo è danneggiato",
  "Gli enzimi plasmatici vengono attivati dall'infiammazione e quindi la loro quantità nel sangue cresce",
  "Il danno d'organo blocca l'eliminazione renale degli enzimi, che si accumulano",
  "Gli enzimi nel sangue sono anticorpi diretti contro le proteine del tessuto danneggiato",
  ], 0,
  "Anche il normale ricambio cellulare riversa enzimi nel sangue; un danno ne aumenta i livelli.")
q("u1117-127", T, "a", "130", "Come aiutano le isoforme della creatina chinasi (CK1, CK2, CK3) a localizzare un danno?", [
  "Sono distribuite in quantità diverse nei tessuti: l'isoforma che sale indica l'organo",
  "Hanno Km diverse: quella più alta indica da quanti giorni è avvenuto il danno al tessuto",
  "Sono prodotte in tempi diversi: la prima che compare indica un danno cerebrale",
  "Hanno pH ottimali diversi: quella attiva nel sangue indica il tessuto più acido",
  "Sono tutte uguali nei tessuti: servono solo a confermare il dosaggio della LDH",
  ], 0,
  "Lo stesso vale per gli isoenzimi della LDH.")

# ── Meccanismi catalitici (p. 130–143) ─────────────────────────────────────
T = "d6-meccanismi"
q("u1117-128", T, "f", "130", "Che cosa caratterizza la catalisi covalente?", [
  "Si forma un legame covalente transitorio tra enzima e substrato",
  "Il metallo del sito attivo forma un legame stabile con il prodotto",
  "Il substrato resta legato all'enzima in modo permanente e lo inattiva",
  "Si trasferiscono solo protoni, senza alcun legame con l'enzima",
  "L'enzima si lega covalentemente a un coenzima che fa la reazione",
  ], 0,
  "Spesso è accompagnata da catalisi acido-base, come nelle serin-proteasi.")
q("u1117-129", T, "h", "131", "Con un estere del p-nitrofenolo la chimotripsina libera subito un «burst» di p-nitrofenolo, poi la reazione rallenta a velocità costante. Che cosa dimostra?", [
  "Si forma un intermedio acil-enzima, e la sua idrolisi da parte dell'acqua è la tappa lenta",
  "Il p-nitrofenolo inibisce la chimotripsina, che si ferma dopo i primi cicli catalitici",
  "La chimotripsina è allosterica e dopo il primo ciclo passa dalla forma R alla forma T",
  "Il substrato si esaurisce dopo pochi millisecondi e resta solo l'idrolisi spontanea",
  "L'enzima libera prima la parte acile e poi lega il p-nitrofenolo in modo covalente e stabile",
  ], 0,
  "È uno studio di cinetica pre-stazionaria: la sola cinetica dello stato stazionario non avrebbe rivelato l'ordine dei passaggi.")
q("u1117-130", T, "a", "132", "Nel meccanismo della chimotripsina, che cosa stabilizza il «buco dell'ossianione»?", [
  "La carica negativa sull'ossigeno carbonilico nell'intermedio tetraedrico",
  "La carica positiva sull'istidina 57 dopo che ha strappato il protone",
  "La carica negativa dell'aspartato 102, che è sempre deprotonato",
  "La carica positiva dell'azoto del legame peptidico prima del taglio",
  "La carica negativa del gruppo carbossilico C-terminale del prodotto rilasciato",
  ], 0,
  "L'intermedio tetraedrico si forma due volte: nell'acilazione e nella deacilazione.")
q("u1117-131", T, "h", "133", "Dopo la prima fase del meccanismo della chimotripsina, quale parte del substrato resta legata all'enzima, e come?", [
  "La parte N-terminale, il cui carbonile forma un estere con la Ser195 (acil-enzima)",
  "La parte C-terminale, legata alla Ser195 con un legame ammidico stabile",
  "La parte N-terminale, legata alla Ser195 con un ponte disolfuro reversibile",
  "La parte C-terminale, legata covalentemente all'azoto dell'His57",
  "Nessuna: il legame peptidico è idrolizzato direttamente da una molecola d'acqua attivata",
  ], 0,
  "La parte C-terminale (dopo l'azoto del legame) esce subito; poi l'acqua, attivata dall'His57, idrolizza l'acil-enzima (fase lenta).")
q("u1117-132", T, "m", "135", "Quale abbinamento proteasi – residuo riconosciuto prima del legame tagliato è corretto?", [
  "Elastasi – residui piccoli come alanina e glicina",
  "Tripsina – residui aromatici come la fenilalanina",
  "Chimotripsina – residui basici come lisina e arginina",
  "Elastasi – residui basici come lisina e arginina",
  "Tripsina – residui piccoli come alanina e valina",
  ], 0,
  "Tripsina: lisina e arginina (tasca profonda con carica negativa); chimotripsina: aromatici; elastasi: piccoli e idrofobici. Sono tutte serin-proteasi.",
  note="Sbobina di Biochimica I, p. 132 e 153: in due punti attribuisce alla tripsina il riconoscimento di residui idrofobici o aromatici. Questa è la specificità della chimotripsina; la tripsina taglia dopo lisina e arginina, come dice correttamente la sbobina a p. 135.")
q("u1117-133", T, "h", "136", "Nella subtilisina, sostituendo con alanina la serina catalitica, la kcat crolla di circa un milione di volte, ma l'enzima resta comunque migliaia di volte più veloce della reazione non catalizzata. Che cosa dimostra?", [
  "Anche senza triade il sito attivo favorisce la reazione, ad esempio legando e orientando il substrato",
  "La serina non partecipa alla catalisi: il calo di kcat dipende solo dalla perdita di struttura dell'enzima",
  "La reazione non catalizzata è in realtà più veloce di quella dell'enzima con la serina",
  "L'alanina sostituisce la serina come nucleofilo, ma con una velocità più bassa",
  "Il sito attivo mutato usa un metallo al posto della triade per attivare l'acqua",
  ], 0,
  "Mutando tutti e tre i residui della triade il calo resta di circa 10⁶–10⁷ volte.",
  note="Sbobina di Biochimica I, p. 136: scrive «più veloce rispetto alla reazione catalizzata»; si intende la reazione non catalizzata.")
q("u1117-134", T, "a", "136", "Nella subtilisina, mutando in alanina l'aspartato della triade, la kcat cala di circa 10⁴ volte. Che cosa indica?", [
  "L'aspartato, pur senza attaccare il substrato, rende l'istidina capace di strappare il protone alla serina",
  "L'aspartato è il nucleofilo che attacca il carbonile del substrato, e senza di lui la reazione si ferma del tutto",
  "L'aspartato lega il substrato nella tasca di specificità, e senza di lui il substrato non entra",
  "L'aspartato stabilizza l'ossianione, e senza di lui l'intermedio tetraedrico non si forma",
  "L'aspartato coordina un metallo del sito attivo, e senza di lui l'acqua non viene attivata",
  ], 0,
  "Nella chimotripsina sono Asp102, His57 e Ser195: lontani nella sequenza, vicini nel ripiegamento.")
q("u1117-135", T, "m", "137–138", "Che cosa distingue le aspartil proteasi dalle serin-proteasi?", [
  "Attivano l'acqua con due aspartati, senza intermedio covalente con l'enzima",
  "Attivano l'acqua con uno ione zinco, senza intermedio covalente con l'enzima",
  "Formano un acil-enzima su un aspartato, come la chimotripsina sulla serina",
  "Usano una triade Asp–His–Ser identica, ma lavorano solo a pH basico",
  "Tagliano solo dopo residui di aspartato, grazie a una tasca carica positiva",
  ], 0,
  "Sono un esempio di catalisi acido-base generale: pepsina, catepsina D, renina, proteasi dell'HIV.")
q("u1117-136", T, "a", "137–138", "Com'è fatto il sito attivo della proteasi dell'HIV?", [
  "È un omodimero: ogni subunità porta un Asp25, uno protonato e uno deprotonato",
  "È un monomero con una triade Asp–His–Ser identica a quella della chimotripsina",
  "È un omodimero: ogni subunità porta una Ser195 e un'His57 affacciate",
  "È un monomero con uno ione zinco coordinato da tre residui di istidina",
  "È un eterodimero: una subunità lega il substrato, l'altra lo idrolizza",
  ], 0,
  "Il contesto del sito attivo dà ai due aspartati pKa diversi.")
q("u1117-137", T, "h", "138", "Nella proteasi dell'HIV, che ruolo ha l'Asp25 deprotonato?", [
  "Strappa un protone all'acqua, che attacca il carbonile del legame Phe–Pro",
  "Attacca direttamente il carbonile del legame Phe–Pro e forma un acil-enzima",
  "Dona un protone all'azoto del legame Phe–Pro e lo rende un buon gruppo uscente",
  "Coordina uno ione zinco che polarizza il carbonile del legame Phe–Pro",
  "Stabilizza la carica positiva del carbocatione che si forma sulla prolina",
  ], 0,
  "L'Asp25 protonato dell'altra subunità stabilizza l'ossianione. L'intermedio tetraedrico si forma solo con l'acqua, non con l'enzima.")
q("u1117-138", T, "m", "142", "Quali residui partecipano alla catalisi del lisozima?", [
  "Glu35 e Asp52", "Ser195 e His57", "Asp25 di due subunità", "His57 e Asp102", "Glu35 e His57"], 0,
  "Il Glu35 fa da acido e poi da base; l'Asp52 stabilizza il carbocatione o forma l'intermedio covalente.")
q("u1117-139", T, "a", "142", "Che differenza c'è tra il meccanismo SN1 e il meccanismo SN2 proposti per il lisozima?", [
  "Nell'SN2 l'Asp52 forma un intermedio covalente; nell'SN1 si forma un carbocatione stabilizzato",
  "Nell'SN1 l'Asp52 forma un intermedio covalente; nell'SN2 si forma un carbocatione stabilizzato",
  "Nell'SN2 il Glu35 forma un intermedio covalente; nell'SN1 è l'acqua ad attaccare il NAG",
  "Nell'SN1 non serve l'acqua; nell'SN2 l'acqua attacca il carbonio 4 del NAG",
  "Nell'SN2 si forma un acil-enzima su una serina; nell'SN1 serve uno ione zinco",
  ], 0,
  "In entrambi il primo passaggio è lo stesso: il Glu35 dona un protone all'ossigeno del legame glicosidico e il NAG si stacca.")
q("u1117-140", T, "f", "140–141", "Quale legame idrolizza il lisozima?", [
  "Il legame glicosidico tra NAM e NAG del peptidoglicano",
  "Il legame peptidico tra gli amminoacidi del peptidoglicano",
  "Il legame fosfodiestere tra i nucleotidi del DNA batterico",
  "Il legame estere tra glicerolo e acidi grassi della membrana",
  "Il legame glicosidico α(1→4) del glicogeno batterico",
  ], 0,
  "Ha azione antibatterica: si trova nell'albume e nelle lacrime. Nella sua fessura si collocano sei unità di zucchero.")
q("u1117-141", T, "h", "142", "Nel lisozima il Glu35 si comporta prima da acido e poi da base. Perché?", [
  "Prima dona H⁺ all'ossigeno glicosidico, poi toglie H⁺ all'acqua che attacca il C1 del NAM",
  "Prima toglie H⁺ all'acqua, poi dona H⁺ all'ossigeno glicosidico del NAG che così si stacca",
  "Prima dona H⁺ all'Asp52, poi lo riprende quando l'Asp52 lascia il carbocatione",
  "Prima forma un estere con il NAM, poi lo idrolizza togliendo H⁺ alla serina vicina",
  "Prima dona H⁺ al carbocatione, poi toglie H⁺ al gruppo acetile del NAG",
  ], 0,
  "È catalisi acido-base generale: alla fine il residuo torna nello stato di partenza.")
q("u1117-142", T, "a", "143", "Come agisce lo Zn²⁺ nel sito attivo dell'anidrasi carbonica?", [
  "Lega l'acqua e ne favorisce la dissociazione: l'OH⁻ attacca il carbonio della CO₂",
  "Lega la CO₂ e la riduce: l'acqua si somma poi al carbonio ridotto",
  "Lega il bicarbonato e lo trattiene finché non arriva una molecola di CO₂",
  "Forma un legame covalente con la CO₂ e poi la cede all'istidina del sito attivo",
  "Lega l'acqua e ne dona i protoni all'ossigeno della CO₂, senza mai dissociarla",
  ], 0,
  "Lo zinco è coordinato da residui di istidina. Il carbonio della CO₂, tra due ossigeni, è un buon elettrofilo.",
  note="Sbobina di Biochimica I, p. 142: presenta l'anidrasi carbonica come esempio di «metallo-proteasi». È un esempio di catalisi da ioni metallici, ma non è una proteasi: catalizza CO₂ + H₂O ⇌ HCO₃⁻ + H⁺.")

# ── Inibizione (p. 144–148) ────────────────────────────────────────────────
T = "d6-inibizione"
q("u1117-143", T, "m", "146", "Come modifica Km e Vmax un inibitore incompetitivo?", [
  "Le abbassa entrambe", "Aumenta la Km e lascia uguale la Vmax", "Abbassa la Vmax e lascia uguale la Km", "Le aumenta entrambe", "Non le modifica"], 0,
  "Si lega solo al complesso ES e forma ESI, che non dà prodotto. Nei doppi reciproci le rette sono parallele.")
q("u1117-144", T, "a", "147", "Un inibitore non competitivo puro (α = α') come modifica Km e Vmax?", [
  "Abbassa la Vmax e lascia invariata la Km",
  "Aumenta la Km e lascia invariata la Vmax",
  "Abbassa sia la Vmax sia la Km in proporzione",
  "Aumenta la Vmax e abbassa la Km",
  "Aumenta sia la Km sia la Vmax",
  ], 0,
  "Lega con la stessa affinità l'enzima libero e il complesso ES: è un caso particolare di inibizione mista.")
q("u1117-145", T, "f", "145", "Il malonato inibisce la succinato deidrogenasi. Che tipo di inibitore è, e perché?", [
  "Competitivo: è simile al succinato e occupa il sito attivo",
  "Incompetitivo: si lega solo al complesso enzima-succinato già formato",
  "Irreversibile: forma un legame covalente con il FAD",
  "Allosterico: si lega a un sito lontano dal sito attivo",
  "Non competitivo: si lega al succinato e lo inattiva",
  ], 0,
  "Ha tre atomi di carbonio, uno meno del succinato, e due gruppi carbossilici.")
q("u1117-146", T, "h", "144–147", "In presenza di un inibitore, nel grafico dei doppi reciproci ottieni una retta parallela a quella senza inibitore. Che tipo di inibizione è?", [
  "Incompetitiva", "Competitiva", "Non competitiva pura", "Irreversibile", "Allosterica omotropica"], 0,
  "Competitiva: le rette si incontrano sull'asse y (Vmax uguale). Non competitiva pura: si incontrano sull'asse x (Km uguale).")
q("u1117-147", T, "a", "147–148", "Perché il DIPF (diisopropilfluorofosfato) inibisce in modo irreversibile l'acetilcolinesterasi?", [
  "La serina del sito attivo attacca il fosforo, il fluoro esce e resta un legame covalente stabile",
  "Il fluoro si lega all'istidina del sito attivo e la blocca con un legame a idrogeno molto forte e stabile",
  "Il DIPF somiglia all'acetilcolina e occupa il sito attivo con un legame non covalente",
  "Il DIPF si lega a un sito allosterico e porta l'enzima nella forma T in modo permanente",
  "Il fosforo del DIPF ossida la serina del sito attivo e la trasforma in alanina",
  ], 0,
  "L'acetilcolina non viene idrolizzata e resta alta, con attivazione continua dei canali ionici.")
q("u1117-148", T, "a", "144", "Perché con un inibitore competitivo la Vmax resta la stessa?", [
  "A [S] molto alta il substrato sposta l'inibitore, e il complesso ES procede normalmente",
  "L'inibitore si lega solo al complesso ES e lascia libero l'enzima che non ha ancora substrato",
  "L'inibitore abbassa la Km, e questo compensa esattamente la perdita di enzima attivo",
  "L'inibitore si lega in un sito lontano e non tocca il sito attivo dell'enzima",
  "L'inibitore viene trasformato in prodotto e quindi non sottrae enzima alla reazione",
  ], 0,
  "Cambia solo la Km apparente (aumenta di un fattore α, che dipende da [I] e dalla Ki).")

# ── Regolazione (p. 148–154) ───────────────────────────────────────────────
T = "d6-regolazione"
q("u1117-149", T, "a", "149", "Che effetto ha il CTP sull'aspartato transcarbamilasi?", [
  "È un inibitore allosterico eterotropico: sposta la sigmoide verso destra",
  "È un inibitore allosterico omotropico: sposta la sigmoide verso sinistra",
  "È un attivatore allosterico eterotropico: sposta la sigmoide verso sinistra",
  "È un inibitore competitivo: occupa il sito del carbamil fosfato",
  "È un inibitore irreversibile: si lega in modo covalente alle catalitiche",
  ], 0,
  "Il CTP è il prodotto finale della via (retroinibizione); l'ATP è invece un effettore positivo.",
  note="Sbobina di Biochimica I, p. 149: dice che la curva spostata «verso sinistra» mostra l'effetto del CTP. Con il CTP la curva si sposta a destra: servono più substrato per la stessa velocità, come spiega la sbobina subito dopo.")
q("u1117-150", T, "h", "150", "Come inibisce il CTP l'aspartato transcarbamilasi a livello strutturale?", [
  "Si lega alle subunità regolatrici e avvicina le catalitiche, chiudendo l'accesso ai substrati",
  "Si lega alle subunità catalitiche e le allontana tra loro, aprendo troppo la cavità centrale",
  "Si lega al sito attivo delle subunità catalitiche al posto dell'aspartato",
  "Fa dissociare le subunità regolatrici, che si legano ai substrati e li sequestrano lontano dal sito",
  "Fosforila le subunità regolatrici, che bloccano le catalitiche nella forma R",
  ], 0,
  "L'enzima ha 6 subunità catalitiche e 6 regolatrici. Senza CTP le regolatrici tengono distanziate le catalitiche: stato R, attivo.")
q("u1117-151", T, "h", "152–153", "Quale sequenza di tagli porta il chimotripsinogeno ad α-chimotripsina?", [
  "La tripsina taglia Arg15–Ile16 (π-chimotripsina), poi l'autolisi toglie i dipeptidi 14–15 e 147–148",
  "L'enteropeptidasi taglia Lys6–Ile7 (π-chimotripsina), poi la tripsina toglie il dipeptide 14–15",
  "La tripsina taglia Lys6–Ile7 (α-chimotripsina) e libera un esapeptide N-terminale",
  "La π-chimotripsina taglia Arg15–Ile16, poi la tripsina toglie i due dipeptidi 14–15 e 147–148",
  "La pepsina taglia Arg15–Ile16 nello stomaco, poi l'autolisi completa l'attivazione nel duodeno",
  ], 0,
  "La π-chimotripsina è già attiva. Dopo i tagli restano tre catene (A, B, C) unite da ponti disolfuro.",
  note="Sbobina di Biochimica I, p. 153: dice che la tripsina «riconosce legami peptidici contenenti aa aromatici» e poi taglia Arg15–Ile16. La tripsina taglia dopo lisina e arginina: proprio per questo taglia dopo l'Arg15.")
q("u1117-152", T, "a", "153", "Da quante catene è formata l'α-chimotripsina, e come restano unite?", [
  "Tre catene (A, B e C) unite da ponti disolfuro",
  "Due catene (A e B) unite da ponti salini",
  "Una sola catena, con due ponti disolfuro interni",
  "Tre catene (A, B e C) unite da legami peptidici",
  "Quattro catene uguali unite da interazioni idrofobiche",
  ], 0,
  "Il chimotripsinogeno ha 245 aa; l'autolisi elimina i dipeptidi Ser14–Arg15 e Thr147–Asn148.")
q("u1117-153", T, "a", "153", "Quale legame del tripsinogeno taglia l'enteropeptidasi, e che cosa la guida?", [
  "Lys6–Ile7, preceduto da quattro aspartati: si libera un esapeptide",
  "Arg15–Ile16, preceduto da quattro glutammati: si libera un dipeptide",
  "Lys6–Ile7, preceduto da quattro lisine: si libera un tetrapeptide",
  "Arg15–Ile16, preceduto da una tasca aromatica: si libera un esapeptide",
  "Tyr146–Thr147, preceduto da due asparagine: si libera un dipeptide",
  ], 0,
  "Basta poca enteropeptidasi: la tripsina formata attiva altro tripsinogeno, chimotripsinogeno, procarbossipeptidasi e proelastasi.")
q("u1117-154", T, "a", "148, 152–154", "Perché la fosforilazione è una regolazione reversibile e l'attivazione degli zimogeni no?", [
  "Il fosfato viene tolto da una fosfatasi; un taglio proteolitico non si può annullare",
  "Il fosfato si stacca da solo in pochi secondi; il taglio proteolitico richiede ATP",
  "La fosforilazione cambia la sequenza dell'enzima; il taglio cambia solo la conformazione",
  "Il fosfato è legato in modo non covalente; il taglio forma un nuovo legame covalente",
  "La fosforilazione avviene solo nel nucleo; i tagli proteolitici solo nel lume intestinale",
  ], 0,
  "Esempio: glicogeno fosforilasi a (fosforilata, più attiva) e b (defosforilata). Altre modifiche reversibili: adenilazione, uridilazione, ADP-ribosilazione, metilazione.",
  note="Sbobina di Biochimica I, p. 154: dice che le fosforilazioni «permettono l'attivazione dell'enzima». Dipende dall'enzima: la fosforilazione attiva la glicogeno fosforilasi ma inattiva, ad esempio, la glicogeno sintasi.")
q("u1117-155", T, "f", "148", "Che cos'è l'inibizione a feedback (retroinibizione)?", [
  "Il prodotto finale di una via inibisce un enzima della stessa via",
  "Il substrato iniziale di una via inibisce l'ultimo enzima della via",
  "Un ormone inibisce la sintesi dell'enzima che lo produce",
  "Un enzima inibisce sé stesso tagliandosi in modo autocatalitico",
  "Il prodotto di una via attiva il primo enzima della via opposta",
  ], 0,
  "Esempio: il CTP che inibisce l'aspartato transcarbamilasi.")
