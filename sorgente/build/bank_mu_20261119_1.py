"""Giro 2026-11-19, blocco 1 – Biochimica I: vitamine idrosolubili e coenzimi (p. 155–168),
coagulazione del sangue (p. 169–181)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Vitamine idrosolubili e coenzimi (p. 155–168) ──────────────────────────
T = "d7-coenzimi"
q("u1119-001", T, "f", "155", "Da quale tipo di vitamine derivano i coenzimi come TPP, FAD, NAD, CoA e PLP?", [
  "Dalle vitamine idrosolubili",
  "Dalle vitamine liposolubili",
  "Dagli amminoacidi essenziali",
  "Dagli acidi grassi essenziali",
  "Dai nucleotidi della dieta",
  ], 0,
  "Le vitamine idrosolubili vengono modificate chimicamente (fosforilate, legate a nucleotidi) per diventare coenzimi.")
q("u1119-002", T, "m", "155", "Che differenza c'è tra un cosubstrato e un gruppo prostetico?", [
  "Il cosubstrato si associa all'enzima solo temporaneamente, il gruppo prostetico in modo permanente",
  "Il cosubstrato è sempre uno ione metallico, il gruppo prostetico è sempre una molecola organica",
  "Il cosubstrato deriva da vitamine liposolubili, il gruppo prostetico da vitamine idrosolubili",
  "Il cosubstrato si lega al sito allosterico, il gruppo prostetico al sito attivo dell'enzima",
  "Il cosubstrato è legato con un legame covalente, il gruppo prostetico con legami deboli",
  ], 0,
  "Metalli e coenzimi sono entrambi cofattori; cosubstrato e gruppo prostetico si distinguono per quanto restano legati (es. NAD⁺ cosubstrato, biotina e lipoato gruppi prostetici legati a una lisina).")
q("u1119-003", T, "m", "155", "Come si calcola la dose consigliata di una vitamina?", [
  "Fabbisogno medio più due deviazioni standard",
  "Fabbisogno medio più una deviazione standard",
  "Fabbisogno medio moltiplicato per due",
  "Fabbisogno massimo osservato nella popolazione",
  "Fabbisogno medio meno due deviazioni standard",
  ], 0,
  "Aggiungere 2 DS al fabbisogno medio copre quasi tutta la popolazione (circa il 97–98%).")
q("u1119-004", T, "l", "156", "Quale enzima trasforma la tiamina nel coenzima tiamina pirofosfato?", [
  "Tiamina pirofosfochinasi",
  "Tiamina pirofosfatasi",
  "Tiaminasi",
  "Flavochinasi",
  "Tiamina sintetasi",
  ], 0,
  "Aggiunge i due fosfati (come pirofosfato). La tiaminasi invece degrada la tiamina: è quella della flora intestinale alterata negli alcolisti.")
q("u1119-005", T, "h", "157", "Nella decarbossilazione del piruvato da parte della TPP, quale sequenza di eventi è corretta?", [
  "Il carbanione della TPP attacca il carbonile del piruvato, esce CO₂ e si forma l'idrossietil-TPP",
  "Il piruvato libero perde CO₂, poi il carbanione della TPP lega l'acetaldeide come idrossietil-TPP",
  "Il carbanione della TPP attacca il carbossile del piruvato, esce acetaldeide e la CO₂ resta legata",
  "Il piruvato forma una base di Schiff con la TPP, poi esce CO₂ e viene liberato subito l'acetil-CoA",
  "Il carbanione della TPP attacca il metile del piruvato, esce CO₂ e si forma il lattil-TPP stabile",
  ], 0,
  "L'attacco nucleofilo sul carbonio carbonilico dà un intermedio tetraedrico; la decarbossilazione dà un intermedio stabilizzato per risonanza che, protonato, è l'idrossietil-TPP.")
q("u1119-006", T, "m", "157", "Nel lievito, quale enzima che usa la TPP trasforma il piruvato in acetaldeide?", [
  "Piruvato decarbossilasi",
  "Piruvato deidrogenasi",
  "Alcol deidrogenasi",
  "Piruvato carbossilasi",
  "Lattato deidrogenasi",
  ], 0,
  "Poi l'alcol deidrogenasi riduce l'acetaldeide a etanolo con il NADH.",
  note="Sbobina di Biochimica I, p. 157: scrive «nel lievito la piruvato deidrogenasi dà luogo ad acetaldeide». È la piruvato decarbossilasi; la piruvato deidrogenasi forma acetil-CoA.")
q("u1119-007", T, "a", "157", "Perché l'alcolismo predispone alla carenza di tiamina (encefalopatia di Wernicke-Korsakoff)?", [
  "Altera la flora intestinale (tiaminasi) e il danno epatico riduce la conversione in TPP",
  "L'etanolo lega la tiamina in un complesso inattivo che viene eliminato con le urine",
  "L'acetaldeide inibisce in modo irreversibile la tiamina pirofosfochinasi dell'intestino",
  "L'alcol consuma tutta la TPP disponibile nella reazione dell'alcol deidrogenasi epatica",
  "L'alcol stimola la sintesi epatica di fosfatasi che staccano il pirofosfato dalla TPP",
  ], 0,
  "Sono le due cause indicate nella sbobina: meno tiamina disponibile e minore attivazione nel fegato.")
q("u1119-008", T, "f", "157", "Che cosa distingue il beriberi umido da quello secco?", [
  "Alla polineurite si aggiungono edema diffuso e insufficienza respiratoria",
  "Manca la polineurite periferica e compaiono solo disturbi intestinali cronici",
  "È dovuto alla carenza di riboflavina invece che di tiamina",
  "Colpisce solo il sistema nervoso centrale e non quello periferico",
  "Compare solo nei bambini allattati con latte materno carente",
  ], 0,
  "Beriberi secco: polineurite periferica cronica. Umido: polineurite + edema diffuso e insufficienza respiratoria. È tipico di chi mangia riso brillato, privato della cuticola che contiene la B1.")
q("u1119-009", T, "a", "157", "Un alcolista ha confusione e disturbi dei movimenti oculari. Quale enzima dei globuli rossi si dosa per confermare la carenza di tiamina?", [
  "Transchetolasi",
  "Piruvato deidrogenasi",
  "Transaldolasi",
  "Glucosio 6-fosfato deidrogenasi",
  "Lattato deidrogenasi",
  ], 0,
  "È l'enzima TPP-dipendente della via dei pentoso fosfati, presente nei globuli rossi; la PDH no, perché i globuli rossi non hanno mitocondri. Il test sull'attività della transchetolasi non è nelle sbobine (Lehninger).")
q("u1119-010", T, "l", "158", "Quale polialcol, derivato per riduzione del ribosio, è legato all'anello isoallosazinico nella riboflavina?", [
  "Ribitolo",
  "Sorbitolo",
  "Inositolo",
  "Glicerolo",
  "Xilitolo",
  ], 0,
  "L'anello è la 7,8-dimetilisoallosazina; sul ribitolo vengono aggiunti il fosfato (FMN) e poi l'AMP (FAD).")
q("u1119-011", T, "m", "158", "Come si forma il FAD a partire dalla riboflavina?", [
  "La flavochinasi la fosforila a FMN, poi la FAD sintetasi aggiunge un AMP",
  "La FAD sintetasi aggiunge un AMP, poi la flavochinasi fosforila il prodotto",
  "La flavochinasi aggiunge un pirofosfato, poi una ligasi aggiunge l'adenosina",
  "Una reduttasi riduce il ribosio a ribitolo, poi una chinasi aggiunge un ATP",
  "La FAD sintetasi aggiunge un ADP, poi la flavochinasi toglie un fosfato",
  ], 0,
  "Entrambe le tappe usano ATP: la prima cede un fosfato, la seconda un AMP (con rilascio di pirofosfato).")
q("u1119-012", T, "a", "159", "Che cosa può fare il FAD che il NAD⁺ non può fare?", [
  "Accettare un elettrone alla volta, passando per la forma semichinonica",
  "Accettare uno ione idruro sul C4 dell'anello piridinico della nicotinamide",
  "Legarsi all'enzima solo temporaneamente, come fa un cosubstrato",
  "Trasportare gruppi acilici legandoli con un legame tioestere",
  "Trasportare unità monocarboniose a diversi stati di ossidazione",
  ], 0,
  "FAD e FMN accettano 1 o 2 elettroni (FADH· poi FADH₂); il NAD⁺ accetta sempre la coppia di elettroni insieme, come idruro.")
q("u1119-013", T, "l", "159", "Su quale atomo della flavina si lega l'idrogeno nella forma semichinonica (FADH· o FMNH·)?", [
  "N5",
  "N1",
  "N3",
  "N10",
  "C4",
  ], 0,
  "Il legame dell'H all'N5 rompe il doppio legame C4a–N5 e dà la specie semichinonica; con il secondo elettrone si arriva a FADH₂.")
q("u1119-014", T, "m", "159", "Su quale atomo il NAD⁺ accetta lo ione idruro?", [
  "Sul C4 dell'anello della nicotinamide",
  "Sull'azoto dell'anello della nicotinamide",
  "Sul C2' del ribosio legato all'adenina",
  "Sull'azoto 6 dell'anello dell'adenina",
  "Sull'ossigeno del gruppo carbossammidico",
  ], 0,
  "Il C4 accetta i due elettroni con un protone (idruro); l'altro protone va in soluzione: NADH + H⁺.")
q("u1119-015", T, "f", "160", "In che cosa differisce il NADP⁺ dal NAD⁺?", [
  "Ha un fosfato in più sul C2' del ribosio legato all'adenina",
  "Ha un fosfato in più sul C3' del ribosio legato alla nicotinamide",
  "Ha l'acido nicotinico al posto della nicotinamide",
  "Ha una guanina al posto dell'adenina",
  "Ha un ribitolo al posto del secondo ribosio",
  ], 0,
  "Il NAD⁺ è un ADP legato a un secondo ribosio che porta la nicotinamide; il NADP⁺ è fosforilato in 2' sul ribosio dell'adenosina.")
q("u1119-016", T, "m", "160", "Da quali due componenti è formato l'acido pantotenico (vitamina B5)?", [
  "Acido pantoico e β-alanina",
  "Acido pantoico e cisteamina",
  "β-alanina e cisteamina",
  "Acido pantoico e glicina",
  "β-alanina e adenosina",
  ], 0,
  "L'acido pantoico perde un OH e si lega con legame ammidico alla β-alanina.")
q("u1119-017", T, "a", "160", "Quale gruppo del coenzima A forma il legame tioestere con l'acile?", [
  "Il tiolo della β-mercaptoetilammina",
  "Il tiolo di una cisteina dell'enzima",
  "L'ossidrile dell'acido pantoico",
  "Il gruppo amminico della β-alanina",
  "Il fosfato in 3' del ribosio dell'ADP",
  ], 0,
  "Il CoA è formato da ADP 3'-fosfato, acido pantotenico e β-mercaptoetilammina (cisteamina); il tioestere con l'acile è ricco di energia.",
  note="Sbobina di Biochimica I, p. 160: scrive «β-mercaptoetilalanina» e mette il gruppo acetile tra i componenti del CoA. È la β-mercaptoetilammina, e l'acile non fa parte del CoA: è il gruppo che il CoA trasporta.")
q("u1119-018", T, "l", "161", "Come si chiama il passaggio in cui l'amminoacido substrato prende il posto della lisina dell'enzima nel legame con il PLP?", [
  "Transaldiminazione",
  "Transaminazione",
  "Transamidazione",
  "Tautomerizzazione",
  "Transesterificazione",
  ], 0,
  "Si passa dall'aldimina interna (PLP–lisina) a una base di Schiff tra il PLP e l'amminoacido (aldimina esterna), da cui parte la reazione.",
  note="Sbobina di Biochimica I, p. 161: descrive la piridossina con un «anello pirimidinico». È un anello piridinico (da cui il nome).")
q("u1119-019", T, "m", "162", "Come è legata la biotina all'enzima nella biocitina?", [
  "Con un legame ammidico tra il carbossile del valerato e l'ε-NH₂ di una lisina",
  "Con un legame estere tra il carbossile del valerato e l'OH di una serina",
  "Con una base di Schiff tra un'aldeide della biotina e una lisina dell'enzima",
  "Con un legame tioestere tra il carbossile del valerato e una cisteina",
  "Con un ponte disolfuro tra lo zolfo dell'anello e una cisteina dell'enzima",
  ], 0,
  "È un legame isopeptidico con la catena laterale della lisina; sull'N1' dell'anello si lega poi la CO₂ (carbossibiotina).")
q("u1119-020", T, "h", "165", "Biotina, S-adenosilmetionina e tetraidrofolato trasferiscono tutti unità a un carbonio. Come si dividono i compiti?", [
  "Biotina il carbonio più ossidato (CO₂), SAM il più ridotto (metile), THF gli altri stati e anche il metile",
  "Biotina il carbonio più ridotto (metile), SAM il più ossidato (CO₂), THF gli altri stati e anche il formile",
  "Biotina e SAM gli stati intermedi (metilene e formile), THF solo il carbonio più ossidato sotto forma di CO₂",
  "Biotina il formile, SAM il metilene, THF solo il carbonio più ossidato (CO₂) e quello più ridotto (metile)",
  "Tutti e tre il metile, ma la biotina lo cede ai carbossili, la SAM alle ammine e il THF solo alle purine",
  ], 0,
  "La biotina serve alle carbossilazioni, la SAM dona metili, il THF trasporta metile, metilene, metenile, formile e formimino.")
q("u1119-021", T, "m", "163", "A quale parte del folato somiglia la sulfanilamide?", [
  "Al p-amminobenzoato, con un gruppo sulfonammidico al posto del carbossile",
  "All'anello pteridinico, con un gruppo sulfonammidico al posto di un azoto",
  "Al glutammato, con un gruppo sulfonammidico al posto del carbossile γ",
  "Al diidrofolato intero, con un atomo di zolfo al posto dell'azoto 5",
  "Alla β-alanina, con un gruppo sulfonammidico al posto del carbossile",
  ], 0,
  "Per questo impedisce ai batteri di incorporare il p-amminobenzoato e di sintetizzare il folato; noi il folato lo prendiamo con la dieta.")
q("u1119-022", T, "a", "165", "Quale serie di unità monocarboniose trasportate dal THF va dalla più ridotta alla più ossidata?", [
  "Metile → metilene → metenile → formile",
  "Metilene → metile → formile → metenile",
  "Formile → metenile → metilene → metile",
  "Metile → metenile → metilene → formile",
  "Metenile → metile → metilene → formile",
  ], 0,
  "N5-metil-THF; N5,N10-metilen-THF; N5,N10-metenil-THF; N5- o N10-formil-THF. Il formimino deriva dal formile che reagisce con l'ammoniaca.")
q("u1119-023", T, "f", "167", "Quale metallo si trova al centro dell'anello corrinico della vitamina B12?", [
  "Cobalto",
  "Ferro",
  "Zinco",
  "Magnesio",
  "Rame",
  ], 0,
  "Il Co³⁺ è coordinato dagli azoti dell'anello corrinico e del dimetilbenzimidazolo; il sesto ligando è un metile, un cianuro o un 5'-deossiadenosile.")
q("u1119-024", T, "m", "167", "Che cosa causa l'anemia perniciosa?", [
  "Il mancato assorbimento della vitamina B12 per mancanza di fattore intrinseco",
  "La carenza alimentare di acido folico nelle diete povere di verdure a foglia verde",
  "La carenza di ferro dovuta a perdite croniche di sangue intestinali",
  "La carenza di vitamina B6 che blocca la sintesi dell'eme nel midollo",
  "L'emolisi dei globuli rossi dovuta al deficit di G6PD dopo le fave",
  ], 0,
  "Il fattore intrinseco è prodotto dalle cellule parietali dello stomaco e serve all'assorbimento della B12 nell'ileo.",
  note="Sbobina di Biochimica I, p. 167: scrive che anche la carenza di acido folico dà l'anemia perniciosa. Folato e B12 danno entrambi l'anemia megaloblastica; «perniciosa» indica solo quella da B12 per mancanza di fattore intrinseco.")
q("u1119-025", T, "l", "168", "Quali carboni dell'acido lipoico portano i due gruppi tiolici?", [
  "C6 e C8",
  "C1 e C8",
  "C2 e C3",
  "C4 e C6",
  "C7 e C8",
  ], 0,
  "L'acido lipoico ha 8 carboni: i tioli su C6 e C8 formano il ponte disolfuro nella forma ossidata. Il C1 è il carbossile che si lega alla lisina (lipoammide).")

# ── Coagulazione del sangue (p. 169–181) ───────────────────────────────────
T = "d8-cascata"
q("u1119-026", T, "f", "169", "Che cosa forma il primo tappo dopo la lesione di un vaso, prima della rete di fibrina?", [
  "Le piastrine, che formano il trombo bianco",
  "I globuli rossi, che formano il trombo rosso",
  "La fibrina, che forma subito una rete stabile",
  "Il collagene, che chiude la lesione da solo",
  "I leucociti, che formano il tappo infiammatorio",
  ], 0,
  "Sequenza: vasocostrizione e tappo piastrinico (trombo bianco), poi la fibrina intrappola le cellule (trombo rosso), infine la riparazione del tessuto.")
q("u1119-027", T, "f", "170", "In quale fattore convergono la via intrinseca e la via estrinseca della coagulazione?", [
  "Fattore X",
  "Fattore VII",
  "Fattore XII",
  "Fattore XIII",
  "Fattore VIII",
  ], 0,
  "Il fattore Xa (con il Va) attiva la protrombina a trombina.")
q("u1119-028", T, "m", "170", "Perché la via estrinseca si attiva più rapidamente di quella intrinseca?", [
  "Basta l'incontro tra il fattore VII e il fattore tissutale per arrivare al fattore X",
  "Il fattore X circola già in forma attiva e aspetta solo il contatto con il collagene",
  "Comprende più tappe enzimatiche, e ogni tappa amplifica il segnale della precedente",
  "Il fattore tissutale si trova sulle piastrine, che sono le prime ad arrivare sul posto",
  "Non richiede ioni calcio, che vengono liberati solo più tardi dai tessuti danneggiati",
  ], 0,
  "Il fattore tissutale è esposto da quasi tutte le cellule tranne quelle endoteliali: con la lesione entra subito in contatto con il fattore VII.")
q("u1119-029", T, "m", "170", "Quali cofattori servono, nella cascata, per il passaggio da uno zimogeno al successivo?", [
  "Ioni calcio e fosfolipidi, soprattutto fosfatidilserina",
  "Ioni magnesio e fosfolipidi, soprattutto fosfatidilcolina",
  "ATP e ioni calcio, che fosforilano gli zimogeni",
  "Vitamina K e ioni magnesio, legati ai fattori attivi",
  "Ioni zinco e sfingomielina delle cellule endoteliali",
  ], 0,
  "Il calcio fa da ponte tra i residui Gla dei fattori e i fosfolipidi delle membrane danneggiate.")
q("u1119-030", T, "a", "171", "Quale affermazione sul fattore di von Willebrand è corretta?", [
  "Srotolato dal flusso, fa da ponte tra il collagene e la GP Ib-V-IX delle piastrine",
  "È un vasodilatatore dell'endotelio integro che impedisce la formazione del trombo",
  "È una serin proteasi della via intrinseca che attiva direttamente il fattore X",
  "È il recettore piastrinico del fibrinogeno che media l'aggregazione tra piastrine",
  "È un enzima del plasma che degrada la fibrina e scioglie il coagulo già formato",
  ], 0,
  "Lo shear stress lo srotola ed espone i siti per il collagene e per il recettore piastrinico: serve all'adesione.",
  note="Sbobina di Biochimica I, p. 171: mette il vWF tra le sostanze dell'endotelio che «impediscono la formazione del trombo». Prostaciclina e NO sono antitrombotici; il vWF favorisce invece l'adesione delle piastrine.")
q("u1119-031", T, "l", "175", "Quale fattore della coagulazione viaggia nel sangue legato al fattore di von Willebrand?", [
  "Fattore VIII",
  "Fattore XIII",
  "Fattore IX",
  "Fattore V",
  "Fattore VII",
  ], 0,
  "Il legame al vWF protegge il fattore VIII (antiemofilico A); per questo nella malattia di von Willebrand cala anche il fattore VIII (questo non è nelle sbobine).",
  note="Sbobina di Biochimica I, p. 175: scrive che il vWF viaggia con il fattore XIII («il fattore emofilico»). Il fattore antiemofilico trasportato dal vWF è l'VIII; il XIII è la transglutamminasi.")
q("u1119-032", T, "l", "171", "Quale recettore piastrinico lega direttamente il collagene?", [
  "GP Ia-IIa (integrina α2β1)",
  "GP IIb-IIIa (integrina αIIbβ3)",
  "GP Ib-V-IX",
  "P2Y12",
  "PAR1",
  ], 0,
  "GP Ib-V-IX lega il vWF, GP IIb-IIIa il fibrinogeno, P2Y12 l'ADP, PAR1/PAR4 la trombina.")
q("u1119-033", T, "a", "172", "Che cosa succede quando il trombossano A₂ lega il suo recettore sulla piastrina?", [
  "Tramite una proteina G attiva la PLCβ: l'IP₃ libera Ca²⁺ e la piastrina rilascia ADP",
  "Tramite una proteina G attiva l'adenilato ciclasi: l'AMPc libera Ca²⁺ e rilascia ADP",
  "Apre direttamente un canale del Ca²⁺ della membrana, senza secondi messaggeri",
  "Attiva la guanilato ciclasi: il GMPc fa uscire ADP dalle vescicole della piastrina",
  "Entra nel nucleo della piastrina e attiva la trascrizione del gene del fibrinogeno",
  ], 0,
  "Il TxA₂ agisce sulla stessa piastrina che lo produce; il Ca²⁺ attiva chinasi e il rilascio di ADP, che amplifica l'aggregazione.")
q("u1119-034", T, "a", "172", "Perché prostaciclina e NO si oppongono all'aggregazione delle piastrine?", [
  "Aumentano AMPc e GMPc, che riducono il Ca²⁺ e quindi la sintesi di trombossano",
  "Bloccano il recettore P2Y12, che non può più legare l'ADP liberato dalle piastrine",
  "Inibiscono in modo irreversibile la cicloossigenasi presente nelle piastrine",
  "Legano il fibrinogeno e gli impediscono di fare da ponte tra le piastrine",
  "Degradano il trombossano già formato prima che raggiunga il suo recettore",
  ], 0,
  "Meno Ca²⁺ significa meno attivazione della PLA2, quindi meno acido arachidonico e meno TxA₂.")
q("u1119-035", T, "m", "173", "Come agiscono le tienopiridine, come la ticlopidina?", [
  "Bloccano l'interazione tra l'ADP e il suo recettore piastrinico",
  "Inibiscono in modo irreversibile la cicloossigenasi delle piastrine",
  "Bloccano la GP IIb-IIIa e il legame del fibrinogeno alle piastrine",
  "Inibiscono l'enzima che riduce la vitamina K epossido nel fegato",
  "Attivano il plasminogeno e accelerano la degradazione della fibrina",
  ], 0,
  "Il recettore dell'ADP è il P2Y12; l'aspirina agisce invece sulla cicloossigenasi.")
q("u1119-036", T, "l", "173", "Quali due attività catalitiche ha la prostaglandina endoperossido sintasi?", [
  "Ciclossigenasica e idroperossidasica",
  "Lipossigenasica e ciclossigenasica",
  "Fosfolipasica e ciclossigenasica",
  "Idroperossidasica e trombossano sintasica",
  "Epossidasica e reduttasica",
  ], 0,
  "La prima forma PGG₂ con O₂ (due perossidi), la seconda riduce un perossido a OH dando PGH₂, precursore di prostaciclina e trombossano.")
q("u1119-037", T, "h", "174", "Perché una piccola dose di aspirina al giorno riduce l'aggregazione per giorni, anche dopo che il farmaco è stato eliminato?", [
  "Inibisce la COX in modo irreversibile e la piastrina, senza nucleo, non può sintetizzarne di nuova",
  "Si accumula nelle piastrine e viene liberata lentamente, inibendo la COX in modo reversibile",
  "Blocca in modo irreversibile il recettore dell'ADP sulla piastrina per tutta la durata della sua vita",
  "Inibisce la prostaciclina dell'endotelio, che poi non può più essere sintetizzata di nuovo",
  "Acetila il fibrinogeno, che non lega più la GP IIb-IIIa per tutta la durata del coagulo",
  ], 0,
  "L'aspirina è un inibitore irreversibile della cicloossigenasi (acetila il sito attivo). L'endotelio, che ha il nucleo, risintetizza la COX; la piastrina no. Il ruolo dell'assenza del nucleo non è nelle sbobine (Lehninger).")
q("u1119-038", T, "m", "174", "Perché l'aspirina può causare emorragie gastriche?", [
  "Inibisce anche la COX-1, che produce le prostaglandine della normale fisiologia",
  "Inibisce solo la COX-2, che protegge la mucosa gastrica dall'acidità dello stomaco",
  "Attiva la COX-1, che produce prostaglandine che aumentano la secrezione acida",
  "Blocca la pompa protonica e altera il pH dello stomaco e la sua mucosa",
  "Inibisce la vitamina K epossido reduttasi nelle cellule della mucosa gastrica",
  ], 0,
  "La COX-1 è presente quasi ovunque; la COX-2 è indotta nell'infiammazione. Per questo si cercano inibitori selettivi della COX-2.")
q("u1119-039", T, "m", "175", "Quale farmaco si usa nella malattia di von Willebrand e come agisce?", [
  "Desmopressina, che aumenta il vWF prodotto dalle cellule endoteliali",
  "Warfarin, che riduce la carbossilazione dei fattori e il rischio di trombi",
  "Vitamina K, che aumenta la carbossilazione del vWF nelle piastrine",
  "Eparina, che potenzia l'antitrombina e prolunga la vita del vWF",
  "Aspirina, che inibisce la COX-1 e aumenta la sintesi di vWF",
  ], 0,
  "La desmopressina è un analogo sintetico della vasopressina. La malattia è la più comune delle anomalie della coagulazione.")

T = "d8-fibrina"
q("u1119-040", T, "f", "175", "Da quante catene polipeptidiche è formato il fibrinogeno?", [
  "Sei: due α, due β e due γ",
  "Quattro: due α e due β",
  "Tre: una α, una β e una γ",
  "Due: una α e una β",
  "Otto: due α, due β, due γ e due δ",
  ], 0,
  "Le catene sono tenute insieme da ponti disolfuro; le α e le β portano all'N-terminale i fibrinopeptidi A e B.")
q("u1119-041", T, "m", "176", "Perché il fibrinogeno, molto abbondante nel sangue, non polimerizza spontaneamente?", [
  "I fibrinopeptidi della regione centrale sono carichi negativamente e le molecole si respingono",
  "È legato all'antitrombina, che lo tiene inattivo finché la trombina non lo stacca dal complesso",
  "Manca il calcio, che viene liberato solo dalle cellule dei tessuti danneggiati",
  "Le sue catene α sono glicosilate e la glicosilazione impedisce ogni contatto",
  "Il fattore XIII circola già legato alle sue estremità e ne blocca i contatti",
  ], 0,
  "I fibrinopeptidi sono ricchi di residui acidi e modificati.")
q("u1119-042", T, "a", "176", "Che cosa cambia nella molecola quando la trombina rimuove i fibrinopeptidi?", [
  "La regione centrale diventa positiva e si associa alle estremità negative di altre molecole, sfalsate di mezza molecola",
  "Le estremità diventano positive e si legano tra loro testa-testa, formando lunghi filamenti lineari senza sfalsamento",
  "La molecola si scinde in sei catene libere, che si riassociano poi con ponti disolfuro in una rete casuale",
  "Si forma subito un legame isopeptidico tra le catene centrali, che rende il coagulo stabile senza altri enzimi",
  "La molecola perde tutte le cariche e precipita, intrappolando i globuli rossi senza un'organizzazione precisa",
  ], 0,
  "Le estremità restano negative (−4 nella sbobina); è l'attrazione tra centro positivo ed estremità negative a guidare la polimerizzazione.")
q("u1119-043", T, "h", "177", "In un paziente con deficit di fattore XIII la trombina e la fibrina si formano normalmente, ma il coagulo è fragile e sanguina dopo giorni. Perché?", [
  "La fibrina polimerizza ma mancano i legami isopeptidici lisina-glutammina che stabilizzano il coagulo",
  "Senza fattore XIII i fibrinopeptidi non vengono rimossi e la fibrina resta solubile nel plasma",
  "Il fattore XIII è il cofattore del fattore Xa e senza di esso la trombina si forma troppo lentamente",
  "Il fattore XIII inibisce la plasmina, quindi in sua assenza la fibrina viene degradata subito",
  "Il fattore XIII forma i ponti disolfuro tra le catene del fibrinogeno, che senza di essi si separano",
  ], 0,
  "Il fattore XIIIa è una transglutamminasi: lega la catena laterale di una lisina a quella di una glutammina di un'altra fibrina e libera NH₄⁺; il coagulo passa da lasso a stabile. Il quadro clinico non è nelle sbobine.")
q("u1119-044", T, "m", "177", "Quali cofattori non enzimatici accelerano rispettivamente il fattore IXa e il fattore Xa?", [
  "Il fattore VIIIa accelera il IXa, il fattore Va accelera il Xa",
  "Il fattore Va accelera il IXa, il fattore VIIIa accelera il Xa",
  "Il fattore XIIIa accelera il IXa, il fattore VIIa accelera il Xa",
  "Il fattore tissutale accelera il IXa, il fattore VIIIa il Xa",
  "La proteina S accelera il IXa, la proteina C accelera il Xa",
  ], 0,
  "VIII = antiemofilico A; V = proaccelerina, che accelera di migliaia di volte la reazione del fattore X.")
q("u1119-045", T, "l", "178", "Quale porzione della protrombina contiene i residui di γ-carbossiglutammato?", [
  "La regione N-terminale, che viene staccata dal fattore Xa durante l'attivazione",
  "La porzione serin proteasica C-terminale, che taglia i fibrinopeptidi",
  "Il peptide di 49 aa trattenuto dal ponte disolfuro con la porzione serin proteasica",
  "Tutta la catena, con i residui Gla distribuiti in modo regolare",
  "Solo il sito attivo, dove i residui Gla legano il fibrinogeno",
  ], 0,
  "La regione Gla (nei primi 274 aa) lega il calcio e richiama la protrombina sulle membrane; la serin proteasi attiva sono gli ultimi 259 aa.")

T = "d8-vitk"
q("u1119-046", T, "f", "180", "Quale enzima dipende dalla vitamina K?", [
  "γ-glutammil carbossilasi",
  "Prolil idrossilasi",
  "Transglutamminasi",
  "Glutammato decarbossilasi",
  "Lisil ossidasi",
  ], 0,
  "Nel fegato aggiunge una CO₂ come carbossile sul carbonio γ dei glutammati, formando il Gla.")
q("u1119-047", T, "m", "180", "Qual è la forma attiva della vitamina K e in che cosa si trasforma durante la carbossilazione?", [
  "L'idrochinone (ridotto), che si ossida a epossido",
  "Il chinone (ossidato), che si riduce a idrochinone",
  "L'epossido, che si riduce a idrochinone",
  "L'idrochinone, che si ossida a chinone senza ossigeno",
  "Il menachinone, che si trasforma in filochinone",
  ], 0,
  "La reazione richiede O₂. Poi la vitamina K epossido reduttasi (nella sbobina «vitamina K ossidoreduttasi») la riporta a chinone e a idrochinone.")
q("u1119-048", T, "a", "181", "Come agisce il warfarin?", [
  "Inibisce la reduttasi che rigenera l'idrochinone dall'epossido di vitamina K",
  "Inibisce la γ-carbossilasi competendo con la CO₂ per il sito attivo",
  "Lega il Ca²⁺ del plasma e impedisce ai fattori di legarsi alle membrane",
  "Inibisce direttamente la trombina, come fa l'eparina con l'antitrombina",
  "Blocca l'assorbimento della vitamina K nell'ileo e la sua produzione nel colon",
  ], 0,
  "Ha una struttura simile alla vitamina K; senza idrochinone le carbossilazioni si fermano. Il dicumarolo, di origine naturale (trifoglio dolce), agisce allo stesso modo.")
q("u1119-049", T, "h", "181", "Un paziente prende warfarin. Quali fattori della coagulazione risultano poco funzionanti e perché?", [
  "II, VII, IX e X: escono dal fegato senza Gla e non legano bene Ca²⁺ e fosfolipidi",
  "Solo la trombina: è l'unico fattore che ha residui Gla nella regione N-terminale",
  "V e VIII: sono cofattori che devono essere carbossilati per accelerare la cascata",
  "Fibrinogeno e XIII: senza carbossilazione non possono più polimerizzare",
  "VII e XII: il warfarin blocca il fattore tissutale e il contatto con il collagene",
  ], 0,
  "Oltre alla protrombina, VII, IX e X hanno bisogno della γ-carbossilazione vitamina K-dipendente per concentrarsi nel sito della lesione.")
q("u1119-050", T, "l", "180", "Come si chiama la vitamina K1 e da dove proviene?", [
  "Filochinone: di origine vegetale, assorbito nell'ileo",
  "Menachinone: di origine vegetale, assorbito nell'ileo",
  "Filochinone: prodotto dai batteri intestinali nel colon",
  "Menachinone: prodotto dalle cellule del fegato",
  "Menadione: prodotto dalle piastrine attivate",
  ], 0,
  "La K2 (menachinone) è prodotta dai batteri nel colon. Entrambe hanno una catena laterale isoprenica (terpenica).")

T = "d8-fibrinolisi"
q("u1119-051", T, "f", "181", "Quale enzima degrada la rete di fibrina?", [
  "Plasmina",
  "Trombina",
  "Fattore XIIIa",
  "Antitrombina",
  "Fattore Xa",
  ], 0,
  "È una serin proteasi che si forma dal plasminogeno; i frammenti vengono eliminati dal fegato.")
q("u1119-052", T, "m", "181", "Come agisce l'antitrombina?", [
  "Inattiva la trombina e i fattori IXa e Xa; l'eparina ne potenzia l'azione",
  "Degrada la fibrina già formata e scioglie il coagulo; l'eparina la attiva",
  "Attiva la proteina C legandosi alla trombomodulina dell'endotelio",
  "Inibisce la vitamina K epossido reduttasi come fa il warfarin",
  "Lega gli ioni calcio e impedisce il legame dei fattori alle membrane",
  ], 0,
  "È uno degli inibitori fisiologici che impediscono alla coagulazione di partire quando non serve.")
q("u1119-053", T, "a", "181", "Come viene attivata la proteina C e che cosa fa?", [
  "Dal complesso trombina-trombomodulina; con la proteina S taglia i fattori Va e VIIIa",
  "Dal fattore Xa; con la proteina S taglia la fibrina e scioglie il coagulo già formato",
  "Dalla plasmina; con la proteina S inattiva la trombina e il fattore XIIIa circolanti",
  "Dal t-PA; con l'antitrombina inattiva i fattori IXa e Xa sulla superficie endoteliale",
  "Dal fattore XIIIa; con la proteina S rimuove i legami crociati della fibrina",
  ], 0,
  "È una proteolisi limitata dei cofattori che accelerano i fattori IX e X: la trombina, legata alla trombomodulina, contribuisce a spegnere la cascata.")
q("u1119-054", T, "h", "181", "Una mutazione rende il fattore Va resistente al taglio della proteina C attivata. Che cosa ti aspetti?", [
  "Tendenza alla trombosi, perché il Va resta attivo e continua ad accelerare il fattore Xa",
  "Tendenza alle emorragie, perché il Va mutato non riesce più ad accelerare il fattore Xa",
  "Tendenza alla trombosi, perché il Va mutato attiva direttamente il fibrinogeno a fibrina",
  "Nessun effetto, perché l'antitrombina inattiva comunque il fattore Va al posto della proteina C",
  "Tendenza alle emorragie, perché la proteina C si accumula e taglia di più il fattore VIIIa",
  ], 0,
  "È il caso del fattore V di Leiden, che non è nelle sbobine: il ragionamento segue dal ruolo della proteina C descritto a p. 181.")
q("u1119-055", T, "l", "181", "Quale attivatore del plasminogeno è di origine batterica?", [
  "Streptochinasi",
  "Urochinasi",
  "t-PA",
  "Trombomodulina",
  "Proteina S",
  ], 0,
  "Il t-PA è l'attivatore fisiologico tissutale; l'urochinasi è prodotta dai reni.")
