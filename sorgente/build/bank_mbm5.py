"""Biologia molecolare – terapia della SCID, pirimidine, deossiribonucleotidi e antimetaboliti (lezione 10),
eme, bilirubina e metabolismo del ferro (lezione 11)."""
from bank_common import q as _q

S = "Biologia molecolare"
L10, L11 = "lezione 10", "lezione 11"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Terapie della SCID (inizio lezione 10) ─────────────────────────────────
T = "bm9-scid"
q("bsc9-05", T, "m", L10, "Perché l'adenosina deaminasi usata come farmaco viene coniugata al PEG?", [
  "Per nasconderla al sistema immunitario",
  "Per farla entrare nei linfociti attraverso la membrana",
  "Per aumentarne la velocità catalitica sull'adenosina",
  "Per renderla attiva anche sulla guanosina",
  "Per poterla somministrare per via orale",
  ], 0,
  "Nel lungo periodo possono comunque comparire anticorpi neutralizzanti.")
q("bsc9-06", T, "a", L10, "Quale limite della terapia genica con vettori retrovirali cita la lezione?", [
  "Non si controlla dove si inserisce il gene nel genoma",
  "Il gene non viene mai trascritto nelle cellule ospiti",
  "Il vettore distrugge le cellule del midollo",
  "La proteina prodotta è sempre immunogena",
  "Il gene si perde a ogni divisione cellulare",
  ], 0,
  "Anche attecchimento ed espressione sono bassi; si studia l'approccio con CRISPR-Cas9. In alternativa: trapianto di midollo da donatore compatibile.")

# ── Sintesi delle pirimidine (lezione 10) ──────────────────────────────────
T = "bm10-sintesi"
q("bpy10-01", T, "f", L10, "Da dove vengono gli atomi dell'anello pirimidinico?", [
  "N3 dalla glutammina, C2 dalla CO₂, il resto dall'aspartato",
  "N1 dalla glicina, C2 dal formil-THF, il resto dalla glutammina",
  "Tutto l'anello dall'aspartato e dal ribosio 5-P",
  "N3 dall'aspartato, C2 dalla glicina, il resto dalla glutammina",
  "N1 e N3 dalla glutammina, il resto dalla CO₂",
  ], 0,
  "L'aspartato fornisce N1, C4, C5 e C6: più di mezza molecola.")
q("bpy10-02", T, "f", L10, "Qual è il prodotto finale della sintesi de novo delle pirimidine?", [
  "UMP", "CMP", "TMP", "OMP", "IMP"], 0,
  "Dall'UMP si ottengono UTP, poi CTP; il dTMP si forma dal dUMP.")
q("bpy10-03", T, "m", L10, "Che cosa distingue la sintesi delle pirimidine da quella delle purine?", [
  "L'anello si forma prima del legame al PRPP",
  "L'anello si costruisce direttamente sul PRPP",
  "Non serve il PRPP in nessun passaggio",
  "Avviene tutta nel mitocondrio",
  "Usa il folato in tutte le tappe",
  ], 0,
  "Nelle purine si parte dal PRPP e si costruisce la base sullo zucchero.")
q("bpy10-04", T, "m", L10, "Qual è l'unico enzima mitocondriale della sintesi delle pirimidine?", [
  "Diidroorotato deidrogenasi", "Carbamil fosfato sintetasi II", "Aspartato transcarbamilasi", "Orotato fosforibosiltransferasi", "OMP decarbossilasi"], 0,
  "È una flavoproteina sulla faccia esterna della membrana interna e cede gli elettroni all'ubichinone.")
q("bpy10-05", T, "m", L10, "Quali attività sono riunite nella proteina CAD?", [
  "CPS II, aspartato transcarbamilasi, diidroorotasi",
  "Orotato fosforibosiltransferasi e OMP decarbossilasi",
  "Diidroorotato deidrogenasi e CTP sintetasi",
  "Timidilato sintasi e diidrofolato reduttasi",
  "Ribonucleotide reduttasi e tioredossina",
  ], 0,
  "Le due attività finali formano invece l'UMP sintasi (bifunzionale).")
q("bpy10-06", T, "a", L10, "Perché nell'iperammoniemia epatica compare acido orotico nelle urine?", [
  "Il carbamil fosfato in eccesso passa nel citosol",
  "L'ammoniaca inibisce l'orotato fosforibosiltransferasi",
  "L'ammoniaca attiva direttamente la CPS II citosolica",
  "Il ciclo dell'urea converte l'arginina in orotato",
  "L'orotato si forma dalla degradazione dell'urea",
  ], 0,
  "La CPS I produce troppo carbamil fosfato, che entra nella via delle pirimidine.")
q("bpy10-07", T, "a", L10, "Come viene regolata la CPS II?", [
  "Attivata da ATP e PRPP, inibita da UTP",
  "Attivata da N-acetilglutammato, inibita da arginina",
  "Attivata da UTP, inibita da ATP",
  "Attivata da CTP, inibita da PRPP",
  "Attivata da glutammina, inibita da AMP",
  ], 0,
  "L'UMP inibisce invece l'OMP decarbossilasi.")
q("bpy10-08", T, "a", L10, "Come agisce il CTP sull'aspartato transcarbamilasi?", [
  "Sposta l'equilibrio verso lo stato T",
  "Sposta l'equilibrio verso R e abbassa la soglia",
  "Compete con l'aspartato nel sito attivo",
  "Fosforila le subunità regolatorie",
  "Dissocia le subunità catalitiche",
  ], 0,
  "T/R passa da 200 a circa 1200 con 0,4 mM di CTP e scende a 70 con 2 mM di ATP (attivatore).")
q("bpy10-09", T, "l", L10, "Com'è fatta l'aspartato transcarbamilasi?", [
  "2 trimeri catalitici e 3 dimeri regolatori",
  "3 dimeri catalitici e 2 trimeri regolatori",
  "Un tetramero di subunità identiche",
  "2 subunità R1 e 2 subunità R2",
  "24 subunità H e L",
  ], 0,
  "6 subunità catalitiche e 6 regolatorie; equilibrio T/R di tipo «tutto o nulla».")
q("bpy10-10", T, "l", L10, "Quale molecola fornisce il gruppo amminico nella CTP sintetasi?", [
  "Glutammina", "Aspartato", "Ammoniaca libera", "Glicina", "Asparagina"], 0,
  "UTP + glutammina + ATP → CTP.")
q("bpy10-11", T, "h", L10, "Come si distingue un'orotoaciduria da un'anemia megaloblastica carenziale?", [
  "Non risponde a B12 e folato",
  "Risponde al ferro; si cura con trasfusioni",
  "Risponde alla B12 ma non al folato",
  "Dà microcitosi invece di macrocitosi",
  "Si cura con allopurinolo",
  ], 0,
  "Manca l'orotato fosforibosiltransferasi o l'OMP decarbossilasi: acido orotico nelle urine, ritardo e anemia megaloblastica.",
  note="Sbobina di Biologia molecolare, lezione 10: l'enzima è chiamato «OMP carbossilasi». È la OMP decarbossilasi.")

# ── Degradazione delle pirimidine (lezione 10) ─────────────────────────────
T = "bm10-degradazione"
q("bpd10-01", T, "f", L10, "Quali sono i prodotti finali della degradazione delle pirimidine?", [
  "β-amminoacidi e NH₄⁺", "Acido urico", "Urea e fumarato", "Allantoina", "Acetil-CoA e glicina"], 0,
  "A differenza delle purine, l'anello viene aperto.")
q("bpd10-02", T, "m", L10, "Che cosa si forma dalla degradazione dell'uracile e della timina?", [
  "β-alanina e β-amminoisobutirrato",
  "α-alanina e α-amminobutirrato",
  "Acido urico e xantina",
  "Fumarato e acetoacetato",
  "Glicina e β-idrossibutirrato",
  ], 0,
  "La citosina viene prima deaminata a uracile.")
q("bpd10-03", T, "a", L10, "Perché la diidropirimidina deidrogenasi è un passaggio obbligato?", [
  "Ridurre l'anello permette di aprirlo con l'idrolisi",
  "Ossidare l'anello lo rende solubile per l'escrezione",
  "Toglie il ribosio dalla base",
  "Rimuove il gruppo metilico della timina",
  "Lega la base al PRPP per il salvataggio",
  ], 0,
  "Usa NADPH; poi la diidropirimidinasi taglia il legame N3–C4.")
q("bpd10-04", T, "h", L10, "Che cosa ha di diverso il catabolismo delle pirimidine rispetto a quello delle purine?", [
  "L'anello viene aperto",
  "Si forma acido urico, poco solubile",
  "Non si passa per la base libera",
  "Avviene solo nei linfociti",
  "Richiede la xantina ossidasi",
  ], 0,
  "I β-amminoacidi possono essere eliminati o riconvertiti.")

# ── Ribonucleotide reduttasi (lezione 10) ──────────────────────────────────
T = "bm10-rnr"
q("brn10-01", T, "f", L10, "Su quale forma dei nucleotidi agisce la ribonucleotide reduttasi?", [
  "Difosfati (NDP)", "Monofosfati (NMP)", "Trifosfati (NTP)", "Nucleosidi", "Basi libere"], 0,
  "NDP → dNDP.")
q("brn10-02", T, "f", L10, "Quale molecola riduce la ribonucleotide reduttasi ossidata?", [
  "Tioredossina", "Ferredossina", "Citocromo c", "Ubichinolo", "Ascorbato"], 0,
  "La tioredossina è ridotta dalla tioredossina reduttasi (FAD), che prende elettroni dal NADPH.")
q("brn10-03", T, "m", L10, "Com'è fatta la ribonucleotide reduttasi di classe I?", [
  "Due R1 e due R2, con ferro in R2",
  "Un omotetramero con quattro centri diferrici",
  "Un monomero con eme e rame",
  "Due trimeri catalitici e tre dimeri regolatori",
  "Un dimero con FAD e molibdeno",
  ], 0,
  "Il centro diferrico genera il radicale tirosilico (Tyr122 in E. coli).")
q("brn10-04", T, "m", L10, "Che effetto hanno ATP e dATP sul sito di regolazione primaria?", [
  "L'ATP attiva tutte le riduzioni, il dATP le blocca",
  "Il dATP attiva tutte le riduzioni, l'ATP le blocca",
  "Entrambi attivano l'enzima",
  "Entrambi inibiscono l'enzima",
  "Regolano solo la scelta del substrato",
  ], 0,
  "È il motivo per cui l'accumulo di dATP nella SCID è tossico.")
q("brn10-05", T, "a", L10, "Quale effettore sul sito di specificità favorisce la riduzione del GDP?", [
  "dTTP", "dATP", "dGTP", "ATP", "dCTP"], 0,
  "dATP → riduzione di UDP e CDP; dTTP → GDP; dGTP → ADP. Così i dNTP restano bilanciati.")
q("brn10-06", T, "a", L10, "Come arriva il radicale al sito catalitico nella ribonucleotide reduttasi?", [
  "Lo trasferisce il radicale tirosilico di R2",
  "Il ferro di R1 ossida direttamente il ribosio",
  "La tioredossina porta il radicale nel sito",
  "Il NADPH forma il radicale sul substrato",
  "L'ossigeno attacca direttamente il carbonio 2'",
  ], 0,
  "Il radicale strappa un H dal C3' del ribosio; le cisteine di R1 forniscono gli equivalenti riducenti per il C2'.")
q("brn10-07", T, "l", L10, "Quale residuo forma il radicale stabile nella subunità R2 di E. coli?", [
  "Tirosina 122", "Cisteina 439", "Serina 14", "Istidina 118", "Lisina 296"], 0,
  "È lontano dal sito catalitico: il radicale viene trasferito.")
q("brn10-08", T, "h", L10, "Quale farmaco inibisce la ribonucleotide reduttasi, secondo la lezione?", [
  "Idrossiurea", "Metotrexato", "5-fluorouracile", "Allopurinolo", "Azaserina"], 0,
  "La lezione aggiunge che la bassa affinità ne limita l'uso.",
  note="La sbobina dice che l'idrossiurea non viene usata in clinica. Non è nella sbobina, ma l'idrossiurea è un farmaco in uso (per esempio nell'anemia falciforme e in alcune neoplasie mieloproliferative).")

# ── Timidilato e folato (lezione 10) ───────────────────────────────────────
T = "bm10-timidilato"
q("bty10-01", T, "f", L10, "Da quale molecola si forma il dTMP?", [
  "dUMP", "UMP", "dCMP", "UTP", "dUTP"], 0,
  "La timidilato sintasi aggiunge un metile in posizione 5.")
q("bty10-02", T, "m", L10, "Che cosa succede al folato nella reazione della timidilato sintasi?", [
  "Il metilen-THF dona il carbonio e si ossida a DHF",
  "Il metil-THF dona il metile e resta THF",
  "Il formil-THF dona il formile e diventa metenil-THF",
  "Il THF accetta un metile dal dUMP",
  "Il folato non partecipa: dona la SAM",
  ], 0,
  "Il metilene diventa metile prendendo elettroni dal THF: per questo serve la DHF reduttasi (NADPH).")
q("bty10-03", T, "a", L10, "Perché 5-fluorouracile e metotrexato bloccano entrambi la sintesi del dTMP?", [
  "Il 5-FU inibisce la timidilato sintasi, il metotrexato la DHF reduttasi",
  "Entrambi inibiscono la timidilato sintasi",
  "Entrambi inibiscono la DHF reduttasi",
  "Il 5-FU inibisce la DHF reduttasi, il metotrexato la timidilato sintasi",
  "Entrambi inibiscono la ribonucleotide reduttasi",
  ], 0,
  "Senza DHF reduttasi il THF non si rigenera e il ciclo si ferma.")
q("bty10-04", T, "h", L10, "Quale meccanismo di resistenza al metotrexato cita la lezione?", [
  "Amplificazione del gene della DHF reduttasi",
  "Aumento della folilpoliglutammato sintetasi",
  "Perdita delle pompe di efflusso",
  "Aumento del trasporto del folato nella cellula",
  "Mutazione che rende la DHF reduttasi più sensibile",
  ], 0,
  "Anche: ridotto trasporto, mutazioni della DHFR meno sensibili, meno poliglutammazione, pompe di efflusso.")

# ── Antimetaboliti e antivirali (lezione 10) ───────────────────────────────
T = "bm10-farmaci"
q("bfa10-01", T, "f", L10, "Quale analogo delle basi è usato soprattutto nei tumori solidi?", [
  "5-fluorouracile", "6-mercaptopurina", "6-tioguanina", "Azatioprina", "Aciclovir"], 0,
  "Mercaptopurina e tioguanina sono usate nei tumori liquidi.")
q("bfa10-02", T, "f", L10, "Su quale virus agisce l'aciclovir?", [
  "Herpes", "HIV", "Influenza", "Epatite C", "SARS-CoV-2"], 0,
  "L'AZT (3'-azido-3'-deossitimidina) è invece usato contro l'HIV.")
q("bfa10-03", T, "m", L10, "Perché l'aciclovir è selettivo per le cellule infettate?", [
  "Viene fosforilato dalla timidina chinasi del virus",
  "Entra solo nelle cellule con recettori virali",
  "Viene attivato dalla polimerasi umana",
  "Si lega solo al DNA virale già formato",
  "Viene degradato nelle cellule sane dalla xantina ossidasi",
  ], 0,
  "Trifosforilato, viene incorporato dalla polimerasi virale e blocca l'allungamento perché manca il 3'-OH.")
q("bfa10-04", T, "m", L10, "Perché si associa l'allopurinolo alla 6-mercaptopurina?", [
  "Ne blocca la degradazione",
  "Ne aumenta l'ingresso nella cellula tumorale",
  "La converte nella forma attiva",
  "Riduce la tossicità sul midollo",
  "Inibisce la HGPRT che la inattiva",
  ], 0,
  "Così resta più farmaco per formare tioinosina monofosfato.")
q("bfa10-05", T, "a", L10, "Come agisce la tioinosina monofosfato derivata dalla 6-mercaptopurina?", [
  "Inibisce amidotransferasi e la biforcazione dall'IMP",
  "Inibisce la timidilato sintasi e la DHF reduttasi",
  "Inibisce la ribonucleotide reduttasi legando il ferro",
  "Attiva la xantina ossidasi e produce radicali",
  "Blocca la CPS II e la sintesi delle pirimidine",
  ], 0,
  "Può anche essere incorporata nel DNA. La forma la HGPRT dal PRPP.")
q("bfa10-06", T, "a", L10, "Come danneggia la cellula l'Ara-C (citosina arabinoside)?", [
  "Viene incorporato nel DNA come Ara-CTP",
  "Inibisce la diidroorotato deidrogenasi mitocondriale",
  "Blocca la CTP sintetasi in modo irreversibile",
  "Viene convertito in uracile e poi in acido urico",
  "Lega la tioredossina e blocca la RNR",
  ], 0,
  "La polimerasi non distingue l'arabinosio dal ribosio; il DNA che ne risulta non viene replicato correttamente.")
q("bfa10-07", T, "a", L10, "Quali enzimi colpiscono gli antagonisti della glutammina come l'azaserina?", [
  "Quelli che usano la glutammina",
  "Quelli che usano il folato come donatore di carbonio",
  "Quelli che usano l'aspartato come donatore di ammino",
  "Quelli che usano il NAD⁺ come accettore di elettroni",
  "Quelli che usano il PLP come cofattore",
  ], 0,
  "Amidotransferasi, FGAM sintetasi, XMP → GMP, CPS II, CTP sintetasi.")
q("bfa10-08", T, "l", L10, "Quale profarmaco viene convertito in 6-mercaptopurina ed è usato come immunosoppressore?", [
  "Azatioprina", "Aciclovir", "Tiazofurina", "Metotrexato", "Idrossiurea"], 0,
  "Si usa nei trapiantati e nelle malattie autoimmuni.")
q("bfa10-09", T, "l", L10, "Su quale enzima agisce la tiazofurina, una volta convertita in analogo del NAD?", [
  "IMP deidrogenasi", "Timidilato sintasi", "DHF reduttasi", "Xantina ossidasi", "PRPP sintetasi"], 0,
  "Blocca IMP → XMP e quindi la sintesi del GTP.")
q("bfa10-10", T, "h", L10, "Come agisce il 5-fluorouracile, secondo la lezione?", [
  "Inibisce la timidilato sintasi e altera l'RNA",
  "Inibisce la DHF reduttasi e blocca il riciclo del THF",
  "Inibisce l'amidotransferasi come la tioinosina monofosfato",
  "Viene incorporato nel DNA come analogo della guanina",
  "Inibisce la ribonucleotide reduttasi legando il ferro",
  ], 0,
  "Può anche essere degradato come le pirimidine (riduzione e apertura dell'anello).")
q("bfa10-11", T, "h", L10, "Perché l'AZT funziona come antivirale ma non come antitumorale?", [
  "La trascrittasi inversa lo lega molto meglio",
  "L'AZT viene fosforilato solo dalla chinasi dell'HIV",
  "Le cellule tumorali non hanno la timidina chinasi",
  "L'AZT si lega solo all'RNA virale",
  "Le cellule tumorali lo degradano con la xantina ossidasi",
  ], 0,
  "Come antitumorale servivano dosi tossiche; come antivirale blocca l'allungamento (manca il 3'-OH).")

# ── Sintesi dell'eme e porfirie (lezioni 10–11) ────────────────────────────
T = "bm11-eme"
q("bem11-01", T, "f", L10, "Quali molecole si condensano nel primo passaggio della sintesi dell'eme?", [
  "Succinil-CoA + glicina", "Acetil-CoA e glicina", "Succinil-CoA e serina", "Glutammato e glicina", "Fumarato e aspartato"], 0,
  "L'ALA sintasi (PLP) forma δ-amminolevulinato nella matrice mitocondriale.")
q("bem11-02", T, "f", L11, "Quale enzima inserisce il ferro nella protoporfirina IX?", [
  "Ferrochelatasi", "Eme ossigenasi", "ALA deidratasi", "Uroporfirinogeno decarbossilasi", "Protoporfirinogeno ossidasi"], 0,
  "Richiede Fe²⁺ e agenti riducenti (ascorbato, cisteina).")
q("bem11-03", T, "m", L10, "Come viene regolata l'ALA sintasi?", [
  "Feedback dall'eme, trascrizione, emivita breve, EPO",
  "Attivazione da eme, fosforilazione da PKA, lunga emivita",
  "Inibizione da piombo e attivazione da zinco",
  "Solo dalla disponibilità di glicina",
  "Attivazione da bilirubina e inibizione da ferro",
  ], 0,
  "Nell'eritroide il messaggero ha anche un IRE al 5': senza ferro non viene tradotto.")
q("bem11-04", T, "m", L10, "Perché il piombo blocca la porfobilinogeno sintasi?", [
  "Sostituisce lo zinco del sito attivo",
  "Si lega alla lisina della base di Schiff",
  "Ossida il δ-amminolevulinato",
  "Blocca il trasporto dell'ALA nel citosol",
  "Precipita il porfobilinogeno",
  ], 0,
  "Si accumula ALA, simile al GABA: forse spiega i sintomi psichici. Il piombo inibisce anche la ferrochelatasi.")
q("bem11-05", T, "m", L11, "Che cosa indica la presenza di zinco-protoporfirina?", [
  "Carenza di ferro",
  "Eccesso di ferro nei depositi",
  "Avvelenamento da rame",
  "Deficit di uroporfirinogeno cosintasi",
  "Emolisi intravascolare acuta",
  ], 0,
  "È un indicatore clinico del deficit di ferro.")
q("bem11-06", T, "a", L11, "Che cosa succede se manca l'uroporfirinogeno III cosintasi?", [
  "Si forma spontaneamente uroporfirinogeno I",
  "Si accumula δ-amminolevulinato nel mitocondrio",
  "Si forma eme senza ferro",
  "La sintesi si ferma alla protoporfirina IX",
  "Si forma solo coproporfirinogeno III",
  ], 0,
  "La cosintasi inverte un anello (AP AP AP PA); la chiusura spontanea dà AP AP AP AP. È la porfiria eritropoietica congenita.")
q("bem11-07", T, "a", L11, "Quali sintomi danno le porfirie con accumulo di precursori precoci (ALA, porfobilinogeno)?", [
  "Neurologici e addominali",
  "Cutanei: fotosensibilità e lesioni",
  "Epatici: ittero e cirrosi",
  "Renali: calcoli e insufficienza",
  "Ematologici: policitemia",
  ], 0,
  "L'accumulo di porfirine (precursori tardivi) dà fotosensibilità e lesioni cutanee.")
q("bem11-08", T, "l", L11, "Quale porfiria è dovuta al deficit della porfobilinogeno deaminasi?", [
  "Porfiria intermittente acuta", "Porfiria cutanea tarda", "Porfiria variegata", "Protoporfiria eritropoietica", "Porfiria di Doss"], 0,
  "Doss: porfobilinogeno sintasi; cutanea tarda: uroporfirinogeno decarbossilasi; variegata: protoporfirinogeno ossidasi; protoporfiria: ferrochelatasi.")
q("bem11-09", T, "l", L11, "Che differenza c'è tra eme a ed eme b?", [
  "L'eme a ha un formile e una catena isoprenica",
  "L'eme a è legato covalentemente alla proteina",
  "L'eme a contiene rame al posto del ferro",
  "L'eme a non ha i due gruppi propionato",
  "L'eme a ha il ferro sempre ferrico",
  ], 0,
  "L'eme c è legato covalentemente (citocromo c); l'eme b è quello di Hb e Mb.")
q("bem11-10", T, "h", L11, "Quale affermazione sulle porfirie è corretta secondo i testi di riferimento?", [
  "La più frequente è la porfiria cutanea tarda",
  "La più frequente è la porfiria eritropoietica congenita",
  "Tutte sono causate dal piombo",
  "Nessuna dà sintomi cutanei",
  "Sono malattie del catabolismo dell'eme",
  ], 0,
  "Le porfirie sono difetti della sintesi dell'eme; il piombo dà invece un quadro acquisito.",
  note="Sbobina di Biologia molecolare, lezione 11: definisce la porfiria eritropoietica congenita «la più diffusa». È tra le più rare; la più frequente è la porfiria cutanea tarda.")

# ── Catabolismo dell'eme e bilirubina (lezione 11) ─────────────────────────
T = "bm11-bilirubina"
q("bbi11-01", T, "f", L11, "Che cosa libera l'eme ossigenasi aprendo l'anello?", [
  "Biliverdina, CO e ferro", "Bilirubina, CO₂ e ferro", "Urobilinogeno e ferro", "Protoporfirina e ferro", "Biliverdina e NH₄⁺"], 0,
  "Usa O₂ e NADPH; taglia tra gli anelli A e B.")
q("bbi11-02", T, "f", L11, "Quale enzima coniuga la bilirubina nel fegato?", [
  "Glucuroniltransferasi", "Biliverdina reduttasi", "Eme ossigenasi", "Glutatione transferasi", "Solfotransferasi"], 0,
  "Si forma bilirubina diglucuronide (coniugata o diretta), idrosolubile.")
q("bbi11-03", T, "m", L11, "Come viaggia la bilirubina non coniugata nel sangue?", [
  "Legata all'albumina",
  "Libera, e passa nelle urine",
  "Legata all'aptoglobina",
  "Legata alla transferrina",
  "Dentro le HDL",
  ], 0,
  "Antibiotici e salicilati possono spiazzarla dall'albumina.")
q("bbi11-04", T, "m", L11, "Che cosa dà il colore alle feci e alle urine?", [
  "Stercobilina nelle feci, urobilina nelle urine",
  "Bilirubina nelle feci, biliverdina nelle urine",
  "Urobilina nelle feci, stercobilina nelle urine",
  "Biliverdina in entrambe",
  "Bilirubina coniugata in entrambe",
  ], 0,
  "Nell'intestino i batteri deconiugano la bilirubina e la riducono a urobilinogeno.")
q("bbi11-05", T, "m", L11, "Come vengono recuperati Hb ed eme liberi nel plasma?", [
  "Hb–aptoglobina via CD163; eme–emopessina via CD91",
  "Hb–emopessina via CD91; eme–aptoglobina via CD163",
  "Hb–albumina via recettore LDL",
  "Hb–transferrina via TfR1",
  "Sono filtrati dal rene ed eliminati",
  ], 0,
  "I macrofagi li internalizzano; il ferro va nella ferritina.")
q("bbi11-06", T, "a", L11, "Come si misura la bilirubina indiretta con la reazione di van den Bergh?", [
  "Per differenza tra totale e diretta",
  "Direttamente, perché reagisce senza alcol",
  "Dalla quantità di urobilina nelle urine",
  "Dosando l'albumina plasmatica",
  "Misurando l'assorbimento a 260 nm",
  ], 0,
  "Senza alcol reagisce solo la coniugata (diretta).")
q("bbi11-07", T, "a", L11, "Quale isoforma dell'eme ossigenasi aumenta quando c'è molto eme da degradare?", [
  "HO-1, inducibile da stress", "HO-2, costitutiva", "HO-3, mitocondriale", "Entrambe allo stesso modo", "Nessuna: la quantità è fissa"], 0,
  "Il CO prodotto modula le emoproteine.")
q("bbi11-08", T, "l", L11, "Sopra quale bilirubinemia compare l'ittero, secondo la lezione?", [
  "2–2,5 mg/dl", "Circa 0,2 mg/dl", "Circa 1 mg/dl", "Circa 10 mg/dl", "Circa 25 mg/dl"], 0,
  "Normale 0,1–1 mg/dl; tra 1,5 e 2 si parla di subittero (sclere).")
q("bbi11-09", T, "h", L11, "Quale proteina citosolica lega l'eme libero per limitarne la tossicità?", [
  "Perossiredossina", "Ferritina", "Tioredossina", "Calmodulina", "Metallotioneina"], 0,
  "L'eme libero è pro-ossidante e fotosensibilizzante.")

# ── Ferro: ruoli e chimica (lezione 11) ────────────────────────────────────
T = "bm11-ferro"
q("bfe11-01", T, "f", L11, "In quale proteina si trova la maggior parte del ferro dell'organismo?", [
  "Emoglobina", "Ferritina", "Mioglobina", "Transferrina", "Citocromi"], 0,
  "Circa il 65% (2,5 g); ferritina ed emosiderina circa il 20%, mioglobina il 6%.")
q("bfe11-02", T, "m", L11, "Perché il ferro libero è pericoloso?", [
  "Con l'H₂O₂ forma radicale ossidrile",
  "Precipita nelle membrane come carbonato",
  "Inibisce in modo irreversibile la catalasi",
  "Si lega al DNA e ne blocca la replicazione",
  "Sostituisce il magnesio nell'ATP",
  ], 0,
  "Fe²⁺ + H₂O₂ → Fe³⁺ + OH⁻ + •OH.")
q("bfe11-03", T, "m", L11, "Perché il Fe³⁺ è poco biodisponibile?", [
  "A pH 7 è quasi insolubile",
  "È troppo solubile e viene eliminato con le urine",
  "Si lega solo all'emoglobina",
  "È radioattivo in natura",
  "Non può formare complessi con l'acqua",
  ], 0,
  "Solubilità circa 10⁻¹⁸ M a pH 7. Il Fe²⁺ scambia più rapidamente i ligandi ed è molto più solubile.")
q("bfe11-04", T, "a", L11, "Perché la carenza di ferro aumenta la suscettibilità alle infezioni?", [
  "Calano gli enzimi a ferro che uccidono i microbi",
  "Aumentano i batteri che usano il ferro libero",
  "Si riduce la sintesi di anticorpi per mancanza di eme",
  "Le cellule immunitarie non possono fare glicolisi",
  "Il fegato smette di produrre transferrina",
  ], 0,
  "La carenza riduce anche enzimi antiossidanti e del metabolismo energetico (fatica).")
q("bfe11-05", T, "l", L11, "Quanto ferro viene assorbito e perso ogni giorno?", [
  "Circa 1–2 mg", "Circa 20 mg", "Circa 100 mg", "Circa 0,01 mg", "Circa 1 g"], 0,
  "Circa 20 mg al giorno vengono riciclati dai globuli rossi lisati.")
q("bfe11-06", T, "h", L11, "Quale affermazione sui depositi di ferro nell'organismo è corretta?", [
  "Il maggior deposito è nel fegato, legato alla ferritina",
  "Il maggior deposito è nel muscolo, legato alla mioglobina",
  "Il maggior deposito è nel plasma, legato alla transferrina",
  "Non esistono depositi: il ferro è tutto nell'Hb",
  "Il deposito principale è nel rene",
  ], 0,
  "Circa 1 g nei depositi; nel plasma solo pochi mg legati alla transferrina.",
  note="La lezione cita Borrelia burgdorferi come batterio intestinale che usa il manganese al posto del ferro. Borrelia è lo spirochete della malattia di Lyme, trasmesso dalle zecche, non un batterio intestinale; il fatto che non usi ferro è invece corretto.")

# ── Proteine del ferro (lezione 11) ────────────────────────────────────────
T = "bm11-proteine"
q("bpf11-01", T, "f", L11, "In quale forma lega il ferro la transferrina?", [
  "Fe³⁺, due ioni con carbonato", "Fe²⁺, quattro ioni", "Fe³⁺, un solo ione legato all'eme", "Fe²⁺, insieme a fosfato", "Fe⁰ metallico"], 0,
  "È una catena di circa 78 kDa con due siti.")
q("bpf11-02", T, "f", L11, "Com'è fatta la ferritina?", [
  "24 subunità H e L", "4 subunità α e β", "Una catena con due siti", "6 subunità attorno a un eme", "Un dimero di 80 kDa"], 0,
  "Il diametro esterno è di circa 12 nm; accumula ferro ossidato.")
q("bpf11-03", T, "m", L11, "Perché la transferrina è normalmente saturata solo per circa un terzo?", [
  "Così sottrae ferro libero ai patogeni",
  "Perché il ferro plasmatico è sempre in eccesso",
  "Perché un sito è riservato al rame",
  "Perché la saturazione completa la fa precipitare",
  "Perché il recettore lega solo l'apotransferrina",
  ], 0,
  "Un ruolo simile ha la lattoferrina.")
q("bpf11-04", T, "a", L11, "Che cosa succede alla transferrina dopo l'endocitosi con il suo recettore?", [
  "Rilascia il ferro e torna fuori vuota",
  "Viene degradata nel lisosoma insieme al recettore",
  "Entra nel nucleo e regola la trascrizione",
  "Cede il ferro direttamente al mitocondrio intatta",
  "Resta in membrana e trasporta il ferro come un canale",
  ], 0,
  "L'apotransferrina ha bassa affinità per il recettore e si stacca.")
q("bpf11-05", T, "l", L11, "Quali proteine ossidano il ferro esportato dalla ferroportina?", [
  "Ceruloplasmina, efestina", "Ferritina e transferrina", "DMT1 e Dcytb", "Epcidina e IRP1", "Aptoglobina ed emopessina"], 0,
  "La transferrina lega solo Fe³⁺.")
q("bpf11-06", T, "h", L11, "Quale coppia trasportatore – funzione è corretta?", [
  "DMT1 – ingresso di Fe²⁺ nell'enterocita",
  "Ferroportina – ingresso di Fe³⁺ nel macrofago",
  "TfR1 – uscita del ferro dall'enterocita",
  "CD91 – ingresso dell'emoglobina libera",
  "CD163 – ingresso dell'eme legato all'emopessina",
  ], 0,
  "La ferroportina esporta il ferro; CD163 lega Hb–aptoglobina, CD91 eme–emopessina.")

# ── Cellule che assorbono e rilasciano ferro (lezione 11) ──────────────────
T = "bm11-cellule"
q("bce11-01", T, "f", L11, "Dove avviene soprattutto l'assorbimento del ferro?", [
  "Nel duodeno", "Nello stomaco", "Nell'ileo", "Nel colon", "Nel digiuno distale"], 0,
  "Il Fe²⁺ entra con il DMT1.")
q("bce11-02", T, "m", L11, "Perché l'acido ascorbico favorisce l'assorbimento del ferro?", [
  "Lo mantiene ridotto", "Lo ossida a Fe³⁺", "Lo lega alla transferrina", "Attiva la ferroportina", "Inibisce l'epcidina"], 0,
  "Anche le ferro reduttasi di membrana riducono il Fe³⁺.")
q("bce11-03", T, "a", L11, "Come libera il macrofago il ferro dei globuli rossi fagocitati?", [
  "Il Fe²⁺ esce dall'endosoma acido e poi dalla ferroportina",
  "Il ferro esce legato all'eme intatto",
  "Il macrofago esocita la ferritina nel plasma",
  "Il ferro viene ossidato a Fe³⁺ e diffonde nel sangue",
  "Il macrofago trasferisce l'emoglobina intera agli eritroblasti",
  ], 0,
  "La ceruloplasmina lo riossida per la transferrina.")
q("bce11-04", T, "h", L11, "Che cosa hanno di particolare i precursori eritroidi nel metabolismo del ferro?", [
  "Captano ferro ma non lo rilasciano",
  "Rilasciano ferro con la ferroportina come i macrofagi",
  "Assorbono ferro dalla dieta con il DMT1",
  "Non hanno ferritina né mitocondri",
  "Ricavano il ferro solo dall'eme libero",
  ], 0,
  "Il ferro va nei mitocondri per eme e cluster Fe-S.")

# ── Regolazione intracellulare: IRE/IRP (lezione 11) ───────────────────────
T = "bm11-ireirp"
q("bir11-01", T, "f", L11, "Che cosa sono gli IRE?", [
  "Forcine dell'mRNA legate dalle IRP", "Sequenze del DNA che legano il ferro", "Domini proteici che legano l'eme", "Siti di fosforilazione della ferritina", "Recettori di membrana per il ferro"], 0,
  "Iron Responsive Elements.")
q("bir11-02", T, "m", L11, "Che effetto ha il legame IRP–IRE al 5' o al 3' dell'mRNA?", [
  "Al 5' blocca la traduzione; al 3' stabilizza l'mRNA",
  "Al 5' stabilizza l'mRNA; al 3' blocca la traduzione",
  "In entrambi i casi aumenta la traduzione",
  "In entrambi i casi degrada l'mRNA",
  "Al 5' aumenta lo splicing; al 3' la poliadenilazione",
  ], 0,
  "Al 3' gli IRE sono in più copie, al 5' uno solo.")
q("bir11-03", T, "m", L11, "Con poco ferro, che cosa succede a ferritina e recettore della transferrina?", [
  "Meno ferritina, più recettore",
  "Più ferritina, meno recettore",
  "Più ferritina e più recettore",
  "Meno ferritina e meno recettore",
  "Nessuna variazione",
  ], 0,
  "Ferritina: IRE al 5'. TfR1: IRE al 3'.")
q("bir11-04", T, "a", L11, "Come «sente» il ferro la IRP1?", [
  "Con ferro forma un cluster Fe-S",
  "Con ferro viene fosforilata e degradata",
  "Con ferro lega gli IRE con più affinità",
  "Con ferro entra nel mitocondrio",
  "Con ferro forma un dimero con la IRP2",
  ], 0,
  "La IRP2 invece con il ferro viene degradata dal proteasoma.")
q("bir11-05", T, "a", L11, "Perché con poco ferro la cellula non traduce l'ALA sintasi eritroide e la ferroportina?", [
  "Hanno un IRE al 5' legato dalle IRP",
  "Hanno un IRE al 3', che con poco ferro viene degradato",
  "Vengono inibite direttamente dall'apotransferrina",
  "Vengono degradate dal proteasoma con la IRP2",
  "Mancano i fattori di trascrizione attivati dal ferro",
  ], 0,
  "Anche HIF2α e aconitasi mitocondriale hanno IRE al 5'; il DMT1 al 3'.")
q("bir11-06", T, "l", L11, "Quale aconitasi svolge la doppia funzione di enzima e IRP1?", [
  "Aconitasi 1 citosolica", "Aconitasi 2 mitocondriale", "Entrambe", "Nessuna", "Aconitasi nucleare"], 0,
  "Nel citosol, con l'isocitrato deidrogenasi citosolica, contribuisce al NADPH.")
q("bir11-07", T, "h", L11, "Perché le IRP bloccano HIF2α quando manca il ferro?", [
  "Per non stimolare l'EPO senza ferro",
  "Per aumentare l'EPO e compensare l'anemia",
  "Per attivare la sintesi di ferritina nel rene",
  "Per bloccare l'epcidina nel fegato",
  "Per aumentare l'assorbimento intestinale",
  ], 0,
  "Le IRP coordinano EPO renale e acquisizione del ferro negli eritroidi.")

# ── Epcidina (lezione 11) ──────────────────────────────────────────────────
T = "bm11-epcidina"
q("bep11-01", T, "f", L11, "Quale organo produce l'epcidina?", [
  "Il fegato", "Il rene", "Il duodeno", "Il midollo osseo", "La milza"], 0,
  "È il regolatore sistemico del ferro.")
q("bep11-02", T, "m", L11, "Come agisce l'epcidina?", [
  "Blocca la ferroportina",
  "Lega la transferrina e ne aumenta la saturazione",
  "Attiva il DMT1 e aumenta l'assorbimento",
  "Degrada la ferritina e libera ferro",
  "Si lega agli IRE e blocca la traduzione",
  ], 0,
  "Riduce l'esportazione da enterociti, macrofagi ed epatociti.")
q("bep11-03", T, "a", L11, "Quali condizioni riducono l'epcidina?", [
  "Ipossia ed eritropoiesi stimolata",
  "Trasfusioni e somministrazione di ferro",
  "Infezioni e infiammazione",
  "Depositi di ferro pieni",
  "Eccesso di ferritina epatica",
  ], 0,
  "Quando serve più ferro per fare globuli rossi, l'epcidina scende.")
q("bep11-04", T, "a", L11, "Che cosa causa una produzione insufficiente di epcidina?", [
  "Emocromatosi",
  "Anemia sideropenica grave",
  "Porfiria cutanea tarda",
  "Ittero da bilirubina non coniugata",
  "Carenza di transferrina",
  ], 0,
  "La ferroportina resta attiva e il ferro viene assorbito senza freno.")
q("bep11-05", T, "h", L11, "La lezione, in un passaggio, dice che con molto ferro l'epcidina diminuisce. Che cosa è corretto?", [
  "Con molto ferro l'epcidina aumenta",
  "Con molto ferro l'epcidina diminuisce; con poco aumenta",
  "L'epcidina non dipende dal ferro, solo dall'infiammazione",
  "L'epcidina aumenta sempre, qualunque sia il ferro",
  "L'epcidina dipende solo dall'eritropoietina",
  ], 0,
  "Lo dice anche la stessa lezione poco dopo: è stimolata dall'eccesso di ferro.",
  note="Sbobina di Biologia molecolare, lezione 11: c'è scritto «quando c'è una grande quantità di ferro circolante diminuisce la quantità di epcidina; quando c'è una scarsa quantità aumenta». È invertito: il ferro alto stimola l'epcidina, che blocca la ferroportina.")
