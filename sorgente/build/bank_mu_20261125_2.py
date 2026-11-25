"""Giro 2026-11-25, blocco 2 – riempimento degli argomenti scarni di Biologia molecolare,
lezioni 8–11: gotta, SCID, pirimidine e deossiribonucleotidi, epcidina, IRE/IRP, bilirubina."""
from bank_common import q as _q

S = "Biologia molecolare"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


L8, L9, L10, L11 = "lezione 8", "lezione 9", "lezione 10", "lezione 11"

# ── Gotta (lezione 9) ──────────────────────────────────────────────────────
C = "bm9-gotta"

q("u1125-101", C, "f", L9, "Quale articolazione colpisce più tipicamente l'attacco di gotta?", [
  "La metatarsofalangea alla base dell'alluce",
  "L'articolazione temporo-mandibolare",
  "L'articolazione sacro-iliaca",
  "L'articolazione coxo-femorale dell'anca",
  "L'articolazione della spalla",
  ], 0,
  "I cristalli di urato si depositano soprattutto alla base dell'alluce, nelle dita, nella tibiotarsica e nel gomito; nell'orecchio si formano i tofi gottosi.")

q("u1125-102", C, "m", L9, "Come agiscono i farmaci uricosurici nella gotta?", [
  "Aumentano l'eliminazione dell'acido urico con le urine",
  "Bloccano la xantina ossidasi e quindi la produzione di urato",
  "Bloccano la fagocitosi dei cristalli da parte dei leucociti",
  "Convertono l'urato in allantoina, più solubile",
  "Inibiscono la PRPP sintetasi e la sintesi de novo",
  ], 0,
  "Tre strategie nella lezione: colchicina (blocca la fagocitosi dei cristalli, meno infiammazione), uricosurici (più escrezione renale), allopurinolo (blocca la xantina ossidasi).")

q("u1125-103", C, "a", L9, "Perché una radioterapia antitumorale estesa può causare iperuricemia?", [
  "La distruzione di molte cellule libera nucleotidi da degradare a urato",
  "Le radiazioni attivano direttamente la xantina ossidasi epatica",
  "Le radiazioni bloccano l'HGPRT e quindi il salvataggio delle basi puriniche",
  "Il danno al DNA attiva la PRPP sintetasi in tutte le cellule",
  "Le radiazioni riducono la solubilità dell'urato nel plasma",
  ], 0,
  "Tra le cause di iperuricemia la lezione cita, oltre alle alterazioni metaboliche, la ridotta escrezione, il danno renale e la terapia radiante, che distrugge cellule e libera grandi quantità di nucleotidi.")

q("u1125-104", C, "m", L9, "Perché l'uomo, a differenza della maggior parte dei mammiferi, accumula acido urico?", [
  "Non ha l'urato ossidasi e non lo converte in allantoina",
  "Ha una xantina ossidasi molto più attiva degli altri mammiferi",
  "Non ha la xantina ossidasi e degrada le purine in altro modo",
  "Ha un rene che non riesce a filtrare l'acido urico",
  "Sintetizza le purine de novo più in fretta degli altri mammiferi",
  ], 0,
  "L'acido urico è poco solubile e l'uomo non riesce a convertirlo in sostanze più solubili. Il nome dell'enzima mancante (urato ossidasi) e l'allantoina sono nella figura, non nel testo della sbobina (Lehninger).")

q("u1125-105", C, "l", L9, "Che cosa distingue strutturalmente l'allopurinolo dall'ipoxantina?", [
  "Le posizioni 7 e 8 sono scambiate: l'azoto sta in 8 e il carbonio in 7",
  "Ha un ossigeno in più in posizione 2, come la xantina",
  "Ha uno zolfo al posto dell'ossigeno in posizione 6",
  "Ha un gruppo amminico al posto dell'ossigeno in posizione 6, come l'adenina",
  "Ha un ribosio legato all'azoto 9, come l'inosina",
  ], 0,
  "L'allopurinolo è un isomero strutturale dell'ipoxantina (pirazolopirimidina): N e C delle posizioni 7 e 8 sono invertiti. Lo zolfo in 6 è della 6-mercaptopurina.")

q("u1125-106", C, "h", L9, "La lezione dice che l'ossipurinolo «rimane legato all'ipoxantina e ne blocca l'attività». Che cosa è corretto?", [
  "L'ossipurinolo resta legato strettamente alla xantina ossidasi e la inattiva",
  "L'ossipurinolo resta legato all'ipoxantina e la trasforma più in fretta in acido urico",
  "L'ossipurinolo lega l'HGPRT e blocca il salvataggio dell'ipoxantina",
  "L'ossipurinolo lega l'urato e lo rende più solubile nel plasma",
  "L'ossipurinolo viene subito ossidato ad acido urico e non ha effetto",
  ], 0,
  "⚠️ Errore nella sbobina: l'allopurinolo è un substrato suicida; la xantina ossidasi lo ossida a ossipurinolo, che resta legato al sito attivo (al molibdeno) e blocca l'enzima. L'ipoxantina non è un enzima.",
  note="La sbobina di Biologia molecolare (lezione 9) scrive che l'ossipurinolo rimane legato «all'ipoxantina»: resta legato alla xantina ossidasi.")

# ── Degradazione delle purine (lezione 9) ──────────────────────────────────
q("u1125-107", "bm9-degradazione", "h", L9, "Nel ciclo dei nucleotidi purinici del muscolo, la lezione dice che l'ossidazione del malato a ossalacetato forma NADPH e 3 ATP. Che cosa è corretto?", [
  "Si forma NADH, che nella catena respiratoria rende circa 2,5 ATP",
  "Si forma NADPH, che nella catena respiratoria rende 3 ATP",
  "Si forma FADH₂, che nella catena respiratoria rende circa 1,5 ATP",
  "Si forma NADPH, che serve alla sintesi degli acidi grassi muscolari",
  "Non si forma alcun coenzima ridotto: la reazione è un'idratazione",
  ], 0,
  "⚠️ Errore nella sbobina: la malato deidrogenasi del ciclo di Krebs usa NAD⁺; con i valori attuali un NADH rende circa 2,5 ATP (3 è il valore storico).",
  note="La sbobina di Biologia molecolare (lezione 9) attribuisce all'ossidazione del malato la formazione di NADPH.")

# ── Vie di salvataggio (lezione 9) ─────────────────────────────────────────
q("u1125-108", "bm9-salvataggio", "l", L9, "Che tipo di inibizione esercitano IMP e GMP sull'HGPRT?", [
  "Competitiva rispetto al PRPP",
  "Competitiva rispetto all'ipoxantina",
  "Allosterica su un sito regolatorio separato",
  "Non competitiva rispetto a entrambi i substrati",
  "Covalente, per fosforilazione dell'enzima",
  ], 0,
  "IMP e GMP sono inibitori competitivi per il legame del PRPP sull'HGPRT; l'AMP lo è sull'APRT. I due enzimi non si sovrappongono nei substrati.")

# ── Regolazione dei nucleotidi purinici (lezione 9) ────────────────────────
C = "bm8-regolazione"

q("u1125-109", C, "l", L9, "Come viene regolata la GMP reduttasi, che riconverte il GMP in IMP?", [
  "È attivata dal GTP e inibita in modo competitivo dall'XMP",
  "È attivata dall'XMP e inibita in modo competitivo dal GTP",
  "È attivata dall'ATP e inibita dal GTP per retroazione",
  "È attivata dal K⁺ e inibita dal fosfato inorganico",
  "È attivata dal PRPP e inibita da AMP e IMP",
  ], 0,
  "Con troppo GTP conviene tornare a IMP: il GTP abbassa la Km per il GMP e aumenta la Vmax. L'XMP, che segnala bisogno di GMP, la inibisce in modo competitivo. K⁺/ATP e Pi regolano invece l'AMP deaminasi.")

q("u1125-110", C, "a", L9, "Che effetto ha il K⁺ sull'AMP deaminasi?", [
  "Abbassa la Km apparente per l'AMP senza cambiare la Vmax",
  "Aumenta la Vmax senza cambiare la Km per l'AMP",
  "Rende sigmoide la curva, che senza K⁺ sarebbe iperbolica",
  "Inibisce l'enzima competendo con l'AMP per il sito attivo",
  "Non ha effetto: l'enzima è regolato solo da ATP e GTP",
  ], 0,
  "In assenza di K⁺ la curva v/[AMP] è sigmoide; il K⁺ è un effettore allosterico positivo che riduce la Km apparente senza alterare la Vmax.")

# ── SCID (lezioni 9–10) ────────────────────────────────────────────────────
C = "bm9-scid"

q("u1125-111", C, "f", L9, "Perché i bambini affetti da SCID devono vivere in condizioni di sterilità?", [
  "Non hanno linfociti funzionanti e qualunque patogeno può essere fatale",
  "Hanno una pelle molto fragile che si infetta a ogni contatto",
  "Non producono acido urico, che protegge dai batteri",
  "Hanno un eccesso di linfociti che reagisce a ogni antigene",
  "Non sintetizzano anticorpi, anche se hanno linfociti T del tutto normali",
  ], 0,
  "SCID = Severe Combined ImmunoDeficiency: i linfociti non si dividono per mancanza di deossiribonucleotidi, e la risposta immunitaria è assente.")

q("u1125-112", C, "m", L10, "Qual è il limite principale del trapianto di midollo nella SCID, secondo la lezione?", [
  "Trovare un donatore compatibile",
  "Il rischio di anticorpi contro l'enzima",
  "L'inserzione casuale del gene nel genoma",
  "La bassa emivita dell'enzima in circolo",
  "La necessità di iniezioni per tutta la vita",
  ], 0,
  "Se il donatore si trova, il trapianto ricostituisce un sistema immunitario integro. Gli altri limiti appartengono alla terapia enzimatica (anticorpi, iniezioni a vita) e alla terapia genica con retrovirus (inserzione non controllata).")

q("u1125-113", C, "h", L10, "Quale abbinamento tra terapia della SCID e suo problema principale è corretto?", [
  "Terapia genica con retrovirus – inserzione del gene in un punto non controllato",
  "Adenosina deaminasi coniugata al PEG – trovare un donatore compatibile",
  "Trapianto di midollo – sviluppo di anticorpi contro l'enzima somministrato",
  "Terapia enzimatica sostitutiva – il gene introdotto si integra in modo casuale nel genoma",
  "Terapia genica con retrovirus – l'enzima va iniettato per tutta la vita",
  ], 0,
  "Enzima-PEG: iniezioni a vita e, a lungo termine, anticorpi neutralizzanti; trapianto: donatore compatibile; retrovirus: basso attecchimento e inserzione non selettiva. Si studia anche un approccio con CRISPR-Cas9.")

q("u1125-114", C, "a", L10, "A che cosa serve coniugare al PEG l'adenosina deaminasi usata come farmaco, oltre a nasconderla al sistema immunitario?", [
  "Ad aumentarne l'emivita in circolo",
  "A farla entrare nei linfociti",
  "A renderla attiva sulla guanosina",
  "A farla legare al DNA dei linfociti",
  "A permetterne l'assunzione per bocca",
  ], 0,
  "Il PEG maschera l'enzima e ne allunga l'emivita; resta il rischio, a lungo termine, di anticorpi neutralizzanti.")

# ── Sintesi de novo delle pirimidine (lezione 10) ──────────────────────────
q("u1125-115", "bm10-sintesi", "m", L10, "Come si tratta l'aciduria orotica, secondo la lezione?", [
  "Somministrando uridina, che viene fosforilata a UMP",
  "Somministrando acido orotico, che manca al paziente",
  "Somministrando allopurinolo, che blocca la xantina ossidasi",
  "Somministrando vitamina B12 e acido folico",
  "Somministrando glutammina, donatore dell'azoto 3",
  ], 0,
  "Il blocco è a valle dell'orotato (orotato fosforibosiltransferasi/OMP decarbossilasi): fornendo uridina, le chinasi la convertono in UMP, UDP e UTP, saltando il passaggio difettoso.")

# ── Degradazione delle pirimidine (lezione 10) ─────────────────────────────
C = "bm10-degradazione"

q("u1125-116", C, "f", L10, "Che cosa succede alla citosina prima che l'anello pirimidinico venga degradato?", [
  "Viene deaminata a uracile",
  "Viene metilata a timina",
  "Viene ossidata a acido orotico",
  "Viene fosforilata a CMP",
  "Viene ridotta a diidrocitosina",
  ], 0,
  "Tolti fosfato e zucchero, la citosina viene deaminata a uracile; uracile e timina vengono poi degradati allo stesso modo.")

q("u1125-117", C, "m", L10, "Quale coenzima usa la deidrogenasi che riduce uracile e timina a diidropirimidine?", [
  "NADPH",
  "NAD⁺",
  "FAD",
  "FMN",
  "NADH",
  ], 0,
  "La diidropirimidina deidrogenasi elimina il doppio legame 5-6 usando NADPH: la riduzione è il passaggio che permette poi di aprire l'anello.")

q("u1125-118", C, "a", L10, "Quale enzima apre l'anello della diidropirimidina e quale legame taglia?", [
  "La diidropirimidinasi, che idrolizza il legame tra le posizioni 3 e 4",
  "La diidropirimidina deidrogenasi, che ossida il legame tra 5 e 6",
  "La diidropirimidinasi, che idrolizza il legame tra le posizioni 1 e 6",
  "La citosina deaminasi, che idrolizza il legame tra le posizioni 2 e 3",
  "La β-ureidopropionasi, che idrolizza il legame tra le posizioni 1 e 2 dell'anello",
  ], 0,
  "La diidropirimidinasi apre l'anello per idrolisi tra N3 e C4; dall'uracile si forma un intermedio che poi libera NH₃ e CO₂ dando β-alanina.")

q("u1125-119", C, "l", L10, "Quale intermedio si forma dalla timina dopo l'apertura dell'anello?", [
  "N-carbammil-β-amminoisobutirrato",
  "N-carbammil-β-alanina metilata",
  "β-amminoisobutirrato libero",
  "Diidrotimina",
  "Acido orotico",
  ], 0,
  "Dalla timina si forma N-carbammil-β-amminoisobutirrato, che per idrolisi libera NH₃ e CO₂ e dà β-amminoisobutirrato (dall'uracile, attraverso la N-carbammil-β-alanina, si ottiene la β-alanina).")

q("u1125-120", C, "h", L10, "Un paziente con deficit di diidropirimidina deidrogenasi riceve 5-fluorouracile a dose standard. Che cosa ci si aspetta?", [
  "Tossicità grave, perché il 5-FU non viene inattivato e si accumula",
  "Nessun effetto del farmaco, perché il 5-FU non viene più attivato",
  "Un effetto normale, perché il 5-FU è eliminato solo dal rene",
  "Iperuricemia, perché il 5-FU viene degradato ad acido urico",
  "Resistenza al farmaco, per amplificazione della timidilato sintasi",
  ], 0,
  "Il 5-FU è un analogo dell'uracile e viene catabolizzato dalla stessa via; senza la deidrogenasi il farmaco si accumula e la tossicità è grave. L'applicazione clinica non è nelle sbobine.")

# ── Timidilato sintasi e chemioterapici (lezione 10) ───────────────────────
C = "bm10-timidilato"

q("u1125-121", C, "f", L10, "Quale enzima riporta il DHF a THF dopo la reazione della timidilato sintasi?", [
  "La DHF reduttasi, con NADPH",
  "La DHF reduttasi, con NADH",
  "La serina idrossimetiltransferasi",
  "La metilen-THF reduttasi, con FAD",
  "La timidilato sintasi stessa",
  ], 0,
  "La timidilato sintasi ossida il THF a DHF; la DHF reduttasi lo riduce con NADPH a THF, che va poi ricaricato di un'unità monocarboniosa.")

q("u1125-122", C, "m", L10, "Come viene ricaricato il THF di un metilene dopo il ciclo della timidilato sintasi?", [
  "Dalla serina idrossimetiltransferasi o dal sistema di taglio della glicina",
  "Dalla timidilato sintasi stessa, che usa la CO₂ come fonte di carbonio",
  "Dalla metionina sintasi, che trasferisce al THF un metile dalla vitamina B12",
  "Dalla DHF reduttasi, che aggiunge il metilene durante la riduzione",
  "Dalla S-adenosilmetionina, che dona il metile al THF",
  ], 0,
  "Il THF rigenerato si carica di nuovo con la SHMT (serina → glicina) o con il sistema di taglio della glicina, formando N5,N10-metilen-THF.")

q("u1125-123", C, "a", L10, "Nella reazione della timidilato sintasi il metilene diventa metile. Da dove vengono gli elettroni per questa riduzione?", [
  "Dallo stesso tetraidrofolato, che si ossida a diidrofolato",
  "Dal NADPH, che si lega alla timidilato sintasi insieme al dUMP",
  "Dal FADH₂ legato alla timidilato sintasi come gruppo prostetico",
  "Dalla tioredossina, come nella ribonucleotide reduttasi",
  "Dal dUMP, che si ossida durante la metilazione",
  ], 0,
  "Il THF cede sia il metilene sia gli equivalenti riducenti: per questo esce come DHF e serve la DHF reduttasi. Per questo il metotrexato blocca indirettamente la sintesi del dTMP.")

q("u1125-124", C, "l", L10, "Quale abbinamento antifolato – bersaglio citato nella lezione è corretto?", [
  "DDATHF – glicinammide ribonucleotide formiltransferasi (GART)",
  "ICI D1694 – DHF reduttasi",
  "Metotrexato – timidilato sintasi",
  "DDATHF – timidilato sintasi",
  "ICI D1694 – glicinammide ribonucleotide formiltransferasi (GART)",
  ], 0,
  "ICI D1694 inibisce la timidilato sintasi; DDATHF la GART della sintesi delle purine; metotrexato la DHF reduttasi.")

q("u1125-125", C, "h", L10, "Perché una riduzione della folil-poliglutammato sintetasi rende le cellule tumorali resistenti al metotrexato?", [
  "Il farmaco non viene poliglutammato e non resta intrappolato nella cellula",
  "Il farmaco non viene più trasportato dentro la cellula dai trasportatori del folato",
  "La DHF reduttasi diventa meno sensibile al farmaco per mutazione",
  "Il gene della DHF reduttasi viene amplificato e l'enzima è in eccesso",
  "Il farmaco viene poliglutammato troppo e non lega più la DHF reduttasi",
  ], 0,
  "Come il folato, il metotrexato va poliglutammato per essere trattenuto nella cellula e avere il massimo effetto. Gli altri meccanismi di resistenza citati (trasporto, mutazione, amplificazione) sono veri ma non c'entrano con questo enzima.")

q("u1125-126", C, "h", L10, "La lezione cita il trimetoprim insieme al metotrexato come farmaco per tumori e malattie autoimmuni. Che cosa è corretto?", [
  "Il trimetoprim inibisce soprattutto la DHF reduttasi batterica: è un antibatterico",
  "Il trimetoprim inibisce la timidilato sintasi umana: è un antitumorale",
  "Il trimetoprim inibisce la DHF reduttasi umana molto più del metotrexato: è un antitumorale",
  "Il trimetoprim inibisce la ribonucleotide reduttasi, come l'idrossiurea",
  "Il trimetoprim è un analogo dell'uracile, come il 5-fluorouracile",
  ], 0,
  "⚠️ Imprecisione della sbobina: il trimetoprim ha un'affinità molto più alta per la DHF reduttasi batterica che per quella umana, per questo si usa come antibatterico (con il sulfametossazolo). Non è nelle sbobine (Lehninger).",
  note="La sbobina di Biologia molecolare (lezione 10) mette il trimetoprim tra gli antifolati usati per tumori e malattie autoimmuni: è un antibatterico.")

# ── Ribonucleotide reduttasi (lezione 10) ──────────────────────────────────
C = "bm10-rnr"

q("u1125-127", C, "f", L10, "Su quale atomo del ribosio agisce la ribonucleotide reduttasi?", [
  "Sul C2', da cui toglie l'ossidrile",
  "Sul C3', da cui toglie l'ossidrile",
  "Sul C5', da cui toglie il fosfato",
  "Sul C1', da cui stacca la base",
  "Sul C4', che viene ridotto",
  ], 0,
  "L'enzima riduce il 2'-OH del ribosio a 2'-H (con eliminazione di una molecola d'acqua), trasformando un NDP in dNDP.")

q("u1125-128", C, "m", L10, "Oltre alla tioredossina, quale sistema riporta allo stato ridotto la ribonucleotide reduttasi?", [
  "La glutaredossina, ridotta dal glutatione",
  "La ferredossina, ridotta dal fotosistema I",
  "La perossiredossina, ridotta dal FADH₂",
  "Il citocromo b5, ridotto dal NADH",
  "Il coenzima Q, ridotto dal succinato",
  ], 0,
  "Due vie: tioredossina ← tioredossina reduttasi (FAD) ← NADPH; oppure glutaredossina ← glutatione ← glutatione reduttasi ← NADPH. In entrambe la fonte finale di elettroni è il NADPH.")

q("u1125-129", C, "l", L10, "Dove si trovano i siti regolatori della ribonucleotide reduttasi?", [
  "Nella subunità R1: per ognuna un sito primario e uno di specificità",
  "Nella subunità R2: per ognuna un sito primario e uno di specificità",
  "Nella subunità R1 il sito primario, nella R2 quello di specificità",
  "Nella subunità R2, vicino al centro diferrico e alla tirosina 122",
  "Nell'interfaccia tra R1 e R2, con un solo sito per tutto l'enzima",
  ], 0,
  "R1 porta le cisteine del sito catalitico e i due siti regolatori; R2 il centro diferrico che genera il radicale tirosilico.")

q("u1125-130", C, "h", L10, "La lezione dice che l'idrossiurea, inibitore della ribonucleotide reduttasi, non si usa come farmaco perché troppo tossica. Che cosa è corretto?", [
  "Si usa, per esempio nella leucemia mieloide cronica e nell'anemia falciforme",
  "Non si usa: la dose efficace sarebbe tossica, come dice la lezione",
  "Si usa solo come antivirale, perché blocca la trascrittasi inversa dell'HIV",
  "Si usa solo come antibatterico, perché inibisce la DHF reduttasi",
  "Si usa solo nella gotta, perché inibisce la xantina ossidasi",
  ], 0,
  "⚠️ Imprecisione della sbobina: l'idrossiurea è un farmaco in uso (spegne il radicale tirosilico di R2); nell'anemia falciforme aumenta anche l'emoglobina fetale. Non è nelle sbobine (Lehninger, Stryer).",
  note="La sbobina di Biologia molecolare (lezione 10) dice che l'idrossiurea non viene usata dal punto di vista farmacologico: è invece un farmaco di uso clinico.")

# ── Antimetaboliti (lezione 10) ────────────────────────────────────────────
q("u1125-131", "bm10-farmaci", "h", L10, "Tra le reazioni bloccate dagli antagonisti della glutammina, la lezione cita la «conversione da UTP a GTP», con l'ammino in posizione 6. Che cosa è corretto?", [
  "È la conversione da UTP a CTP, con l'ammino in posizione 4",
  "È la conversione da UTP a GTP, con l'ammino in posizione 6",
  "È la conversione da IMP a GMP, con l'ammino in posizione 4",
  "È la conversione da UMP a TMP, con un metile in posizione 5",
  "È la conversione da XMP a AMP, con l'ammino in posizione 6",
  ], 0,
  "⚠️ Errore nella sbobina: la CTP sintetasi usa la glutammina per mettere l'ammino sul C4 dell'UTP (la stessa lezione lo dice correttamente poco prima). Gli altri bersagli citati: amidotransferasi, FGAM sintetasi, GMP sintetasi (ammino in 2 sull'XMP), CPS II.",
  note="La sbobina di Biologia molecolare (lezione 10) scrive «da UTP a GTP… posizione 6»: è la conversione UTP → CTP sul C4.")

# ── Epcidina (lezione 11) ──────────────────────────────────────────────────
C = "bm11-epcidina"

q("u1125-132", C, "f", L11, "Che effetto ha l'epcidina su ferro plasmatico e saturazione della transferrina?", [
  "Li abbassa, perché trattiene il ferro dentro le cellule",
  "Li alza, perché libera il ferro dai depositi epatici",
  "Li alza, perché aumenta l'assorbimento intestinale",
  "Li abbassa, perché fa eliminare il ferro in eccesso con le urine",
  "Non li cambia: agisce solo sulla ferritina cellulare",
  ], 0,
  "Bloccando la ferroportina, l'epcidina riduce l'uscita di ferro da enterociti, macrofagi ed epatociti: calano ferro circolante e saturazione della transferrina.")

q("u1125-133", C, "m", L11, "Su quali cellule agisce soprattutto l'epcidina?", [
  "Enterociti duodenali e macrofagi, e in parte epatociti",
  "Eritroblasti del midollo e reticolociti circolanti",
  "Cellule del tubulo renale e del dotto collettore",
  "Cellule muscolari scheletriche e cardiomiociti del ventricolo",
  "Neuroni e cellule della glia del sistema nervoso",
  ], 0,
  "Sono le cellule che rilasciano ferro nel plasma attraverso la ferroportina: assorbimento (enterociti), riciclo dagli eritrociti (macrofagi), depositi (epatociti).")

q("u1125-134", C, "a", L11, "Che cosa succede alla ferroportina quando lega l'epcidina?", [
  "Viene internalizzata e degradata, e il ferro resta nella cellula",
  "Viene fosforilata e trasporta il ferro più in fretta",
  "Viene ossidata dalla ceruloplasmina e cambia selettività",
  "Viene staccata dalla membrana e circola legata alla transferrina",
  "Viene tradotta di più, perché l'epcidina stabilizza l'mRNA",
  ], 0,
  "La lezione dice che il ferro resta intrappolato nella cellula; il meccanismo (internalizzazione e degradazione lisosomiale della ferroportina) non è nelle sbobine (Lehninger).")

q("u1125-135", C, "h", L11, "In un'infiammazione cronica il paziente ha ferro sierico basso ma ferritina e depositi normali o alti. Quale spiegazione è coerente?", [
  "L'infiammazione aumenta l'epcidina, che blocca la ferroportina e sequestra il ferro",
  "L'infiammazione riduce l'epcidina, che lascia uscire troppo ferro con le urine e la bile",
  "L'infiammazione blocca la sintesi della transferrina, che non porta più il ferro",
  "L'infiammazione distrugge la ferritina, che non trattiene più il ferro",
  "L'infiammazione inibisce il DMT1, ma i macrofagi rilasciano più ferro",
  ], 0,
  "La lezione dice che l'epcidina è regolata da ferro e infiammazione e che abbassare il ferro limita i processi infiammatori: ferro intrappolato in macrofagi ed enterociti, plasma povero di ferro. Il nome «anemia delle malattie croniche» non è nelle sbobine.")

# ── IRE/IRP (lezione 11) ───────────────────────────────────────────────────
C = "bm11-ireirp"

q("u1125-136", C, "m", L11, "Che cosa succede alla IRP2 quando nella cellula c'è molto ferro?", [
  "Viene degradata dal proteasoma",
  "Forma un cluster Fe-S e diventa aconitasi",
  "Lega gli IRE con affinità maggiore",
  "Si sposta nel mitocondrio",
  "Viene secreta nel plasma",
  ], 0,
  "Il ferro fa caricare il cluster Fe-S su IRP1 (che diventa aconitasi citosolica) e attiva la degradazione proteasomale di IRP2. Con poco ferro si accumula IRP1 apo e IRP2 si stabilizza.")

q("u1125-137", C, "a", L11, "Con poco ferro, che cosa succede all'mRNA del trasportatore DMT1?", [
  "Viene stabilizzato, perché le IRP legano un IRE al 3'",
  "Viene tradotto di meno, perché le IRP legano un IRE al 5'",
  "Viene degradato, perché le IRP si staccano dall'IRE",
  "Non cambia, perché il DMT1 non ha elementi IRE",
  "Viene tradotto di più, perché l'IRE si apre senza IRP",
  ], 0,
  "Come per il recettore della transferrina, l'IRE al 3' legato dalle IRP stabilizza il messaggero: più DMT1 per far entrare più ferro.")

q("u1125-138", C, "l", L11, "Perché con poco ferro la cellula non traduce l'aconitasi mitocondriale?", [
  "Il suo mRNA ha un IRE al 5', e senza ferro non si formerebbe il cluster",
  "Il suo mRNA ha un IRE al 3', che con poco ferro viene degradato",
  "Il suo gene è represso da HIF2α, che si accumula nel nucleo quando c'è poco ferro",
  "La IRP1 apo occupa il ribosoma mitocondriale che la traduce",
  "L'epcidina blocca il suo trasporto dentro il mitocondrio",
  ], 0,
  "L'aconitasi mitocondriale ha un IRE al 5' (come ferritina, ALAS eritroide, ferroportina e HIF2α): con poco ferro le IRP bloccano la traduzione, inutile perché non si formerebbe il cluster Fe-S.")

q("u1125-139", C, "h", L11, "In una cellula carente di ferro, quale combinazione di effetti delle IRP è attesa?", [
  "Meno ferritina e ferroportina, più recettore della transferrina e DMT1",
  "Più ferritina e ferroportina, meno recettore della transferrina e DMT1",
  "Più ferritina e recettore della transferrina, meno ferroportina e DMT1",
  "Meno ferritina e DMT1, più ferroportina e recettore della transferrina",
  "Nessuna variazione: le IRP agiscono solo quando il ferro è in eccesso",
  ], 0,
  "Con poco ferro le IRP legano gli IRE: al 5' bloccano la traduzione (ferritina, ferroportina), al 3' stabilizzano il messaggero (TfR1, DMT1). La cellula smette di immagazzinare ed esportare e capta di più.")

q("u1125-140", C, "a", L11, "Quale ruolo metabolico ha l'aconitasi 1 citosolica quando il citrato esce dal mitocondrio?", [
  "Forma isocitrato, che l'isocitrato deidrogenasi citosolica ossida producendo NADPH",
  "Forma isocitrato, che l'isocitrato deidrogenasi citosolica ossida producendo NADH",
  "Scinde il citrato in acetil-CoA e ossalacetato per la sintesi degli acidi grassi",
  "Riporta il citrato nel mitocondrio, dove riprende il ciclo di Krebs",
  "Converte il citrato in malato, che poi dà NADPH con l'enzima malico citosolico",
  ], 0,
  "Con il cluster Fe-S IRP1 è l'aconitasi 1: citrato → isocitrato; l'isocitrato deidrogenasi citosolica lo porta ad α-chetoglutarato con produzione di NADPH, utile alla sintesi dei grassi. La scissione del citrato è dell'ATP-citrato liasi.")

# ── Catabolismo dell'eme e bilirubina (lezione 11) ─────────────────────────
C = "bm11-bilirubina"

q("u1125-141", C, "f", L11, "Quali sono i valori normali di bilirubina totale nel sangue, secondo la lezione?", [
  "0,1–1 mg/dl",
  "1–2,5 mg/dl",
  "3–7 mg/dl",
  "10–20 mg/dl",
  "0,01–0,05 mg/dl",
  ], 0,
  "Totale 0,1–1 mg/dl (indiretta 0,1–1, diretta 0–0,2). Sopra 1,5 mg/dl si parla di subittero (sclere), sopra 2,5 di ittero. 3–7 mg/dl è il range dell'acido urico.")

q("u1125-142", C, "m", L11, "Quale coenzima usa la biliverdina reduttasi?", [
  "NADPH",
  "NADH",
  "FADH₂",
  "Glutatione",
  "Ascorbato",
  ], 0,
  "Sia l'eme ossigenasi (con O₂) sia la biliverdina reduttasi usano NADPH; la biliverdina IXα viene ridotta a bilirubina.")

q("u1125-143", C, "l", L11, "Quale trasportatore secerne la bilirubina coniugata dall'epatocita nella bile?", [
  "MRP2",
  "DMT1",
  "CD163",
  "Ligandina",
  "Ferroportina",
  ], 0,
  "Nell'epatocita la bilirubina è legata a ligandina e proteina Z, coniugata con due glucuronati dalla UDP-glucuroniltransferasi e secreta nella bile da MRP2.")

q("u1125-144", C, "a", L11, "Che cosa fanno le β-glucuronidasi dei batteri intestinali?", [
  "Staccano il glucuronato e permettono il riassorbimento nel circolo enteroepatico",
  "Aggiungono glucuronato alla bilirubina per renderla più solubile nella bile",
  "Ossidano la bilirubina a biliverdina, che dà il tipico colore verde alle feci",
  "Degradano l'eme in biliverdina, liberando monossido di carbonio",
  "Legano la bilirubina all'albumina per riportarla nel fegato",
  ], 0,
  "Nell'intestino la bilirubina deconiugata diventa urobilinogeno (in parte riassorbito: circolazione enteroepatica, urobilina nelle urine) e stercobilinogeno/stercobilina nelle feci.")

q("u1125-145", C, "h", L11, "Un paziente ha ittero con bilirubina quasi tutta indiretta, urine di colore normale e anemia. Che cosa è più probabile?", [
  "Un'emolisi, che produce più bilirubina di quanta il fegato riesca a coniugare",
  "Un'ostruzione delle vie biliari, che fa refluire bilirubina coniugata nel sangue",
  "Un difetto di MRP2, che impedisce la secrezione della bilirubina coniugata",
  "Un eccesso di β-glucuronidasi intestinali, che aumenta la bilirubina diretta",
  "Una carenza di eme ossigenasi, che fa accumulare bilirubina nel sangue",
  ], 0,
  "La bilirubina indiretta è legata all'albumina e non passa nelle urine; in eccesso indica sovrapproduzione (emolisi) o difetto di coniugazione. Ostruzione e difetti di secrezione aumentano la diretta (urine scure). Il quadro clinico non è nelle sbobine.")
