"""Giro 2026-11-24, blocco 2 – Biochimica I: editing del DNA e CRISPR (p. 281–289),
vitamine liposolubili (p. 217–218), digestione e trasporto dei grassi (p. 219–221)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Editing del DNA (p. 281–289) ────────────────────────────────────────────
T = "d13-editing"

q("u1124-053", T, "f", "281", "Che cosa significa la sigla CRISPR?", [
  "Clustered Regularly Interspaced Short Palindromic Repeat",
  "Clustered Replicated Interspaced Short Palindromic Repeat",
  "Clustered Regularly Inserted Single Palindromic Repressor",
  "Conserved Regularly Interspaced Short Polymorphic Repeat",
  "Clustered Restriction Interspaced Short Palindromic Region",
  ], 0,
  "Sono ripetizioni geniche, abbondanti in molti genomi batterici, interspaziate regolarmente da spaziatori.")

q("u1124-054", T, "f", "281", "Che cosa indica la sigla Cas?", [
  "CRISPR associated gene",
  "CRISPR activating sequence",
  "Cluster associated spacer",
  "CRISPR antisense silencer",
  "Cleavage associated subunit",
  ], 0,
  "Sono i geni associati alle ripetizioni CRISPR, che codificano le proteine del sistema, fra cui Cas6 e Cas9.")

q("u1124-055", T, "f", "282", "Come sono fatte le sequenze di un locus CRISPR?", [
  "Ripetizioni tutte uguali, separate da spaziatori di sequenza diversa",
  "Ripetizioni tutte diverse, separate da spaziatori di sequenza identica",
  "Ripetizioni e spaziatori con la stessa sequenza, alternati fra loro",
  "Ripetizioni in tandem senza spaziatori, raggruppate in un unico cluster",
  "Spaziatori disposti in tandem, seguiti da un'unica ripetizione terminale",
  ], 0,
  "Le repeats hanno tutte la stessa sequenza, palindromica; gli spacers hanno sequenza variabile.")

q("u1124-056", T, "f", "284", "Quale sequenza deve essere presente perché Cas9 possa tagliare?", [
  "La sequenza PAM, 5'-NGG-3'",
  "La sequenza PAM, 5'-NAA-3'",
  "Una sequenza palindromica di 6 paia di basi",
  "Una sequenza di poliadenilazione, 5'-AAUAAA-3'",
  "Un'origine di replicazione riconosciuta dalla nucleasi",
  ], 0,
  "PAM sta per protospacer adjacent motif: un nucleotide variabile seguito da due guanosine. Cas9 taglia a tre paia di basi dal PAM.")

q("u1124-057", T, "f", "285", "Che cos'è il gRNA usato in laboratorio?", [
  "Una molecola unica che fonde insieme crRNA e tracrRNA",
  "Una molecola unica che fonde insieme il crRNA e la proteina Cas9",
  "Un RNA che sostituisce Cas9 nell'attività di taglio",
  "Un RNA che serve da templato per il riparo omologo",
  "Un RNA che blocca l'attività nucleasica di Cas9",
  ], 0,
  "Serve a semplificare il sistema: in un'unica molecola si ha ciò che viene legato da Cas9 e portato sul genoma da tagliare.")

q("u1124-058", T, "m", "282", "Quali sono, nell'ordine, le tre fasi del sistema CRISPR nel batterio?", [
  "Acquisizione degli spacer, espressione del cluster, interferenza",
  "Espressione del cluster, acquisizione degli spacer, interferenza",
  "Interferenza, acquisizione degli spacer, espressione del cluster",
  "Acquisizione degli spacer, interferenza, espressione del cluster",
  "Espressione del cluster, interferenza, acquisizione degli spacer",
  ], 0,
  "Il genoma fagico viene digerito e inserito fra le repeats, il cluster viene poi trascritto e infine usato per distruggere il DNA dell'invasore.")

q("u1124-059", T, "m", "283", "Quale proteina taglia il trascritto primario CRISPR nei singoli crRNA?", [
  "Cas6, che riconosce delle sequenze nelle repeats",
  "Cas9, che riconosce delle sequenze nelle repeats",
  "L'RNasi H, che degrada l'RNA negli ibridi DNA-RNA",
  "Una endonucleasi di restrizione del batterio ospite",
  "La trascrittasi inversa associata al locus CRISPR",
  ], 0,
  "Dal precursore si ottengono tanti crRNA quanti sono gli spacer acquisiti.")

q("u1124-060", T, "m", "283", "Perché il crRNA presenta una porzione a forcina (stem loop)?", [
  "Perché le repeats da cui deriva sono sequenze palindromiche",
  "Perché gli spacer da cui deriva sono sequenze palindromiche",
  "Perché viene stabilizzato da Cas9 in una struttura ripiegata",
  "Perché contiene una coda poli-A che si ripiega su se stessa",
  "Perché si appaia al DNA bersaglio formando un'ansa di spostamento",
  ], 0,
  "L'RNA ha una porzione a singolo filamento, che riconosce il protospacer, e una porzione ripiegata dovuta alla palindromia delle ripetizioni.")

q("u1124-061", T, "m", "283", "Che ruolo ha il tracrRNA?", [
  "Si appaia alla porzione repeat del crRNA e il complesso è legato da Cas9",
  "Si appaia alla porzione spacer del crRNA e ne impedisce la degradazione",
  "Si appaia al DNA bersaglio e vi richiama direttamente la nucleasi Cas6",
  "Funziona da templato donatore nel riparo omologo dopo il taglio",
  "Trascrive il locus CRISPR generando il precursore comune dei singoli crRNA",
  ], 0,
  "È trascritto da un altro locus del genoma batterico; la sua porzione a singolo filamento è complementare alla repeat, comune a tutti i crRNA. Il risultato è un complesso ribonucleoproteico con Cas9.")

q("u1124-062", T, "m", "284", "Che cosa succede al DNA dopo un taglio CRISPR riparato per NHEJ?", [
  "Si formano inserzioni o delezioni che spostano il frame di lettura",
  "Si ripristina esattamente la sequenza di partenza, senza alcuna alterazione",
  "Si sostituisce la sequenza mutata con quella del cromosoma omologo",
  "Il frammento tagliato viene eliminato e il gene resta interrotto in modo stabile",
  "Si inserisce il DNA donatore fornito in trans dall'esterno della cellula",
  ], 0,
  "Il riparo non omologo salda i due frammenti dopo degradazione o aggiunta casuale di nucleotidi: lo shift del frame porta a una proteina non funzionale, cioè a un knock out.")

q("u1124-063", T, "m", "285", "Che cosa serve, oltre al gRNA e a Cas9, per correggere una mutazione con il riparo omologo?", [
  "Un DNA donatore con la sequenza corretta, fornito in trans",
  "Un secondo gRNA che riconosca il filamento complementare",
  "Una DNA ligasi esogena, che salda i due frammenti tagliati",
  "Una sequenza PAM aggiuntiva, posta a valle del sito di taglio",
  "Un inibitore del riparo omologo, che favorisce la ricombinazione",
  ], 0,
  "Nell'HDR si parte da un templato donatore, di norma il cromosoma omologo, oppure da un DNA fornito dall'esterno con la sequenza da inserire al posto di quella mutata.")

q("u1124-064", T, "m", "289", "Come si ottiene un sistema CRISPR che regola la trascrizione invece di tagliare?", [
  "Mutando Cas9 per bloccarne l'attività nucleasica e legandovi un effettore",
  "Mutando il gRNA perché riconosca il promotore invece della regione codificante",
  "Rimuovendo la sequenza PAM dal DNA bersaglio, così il taglio non avviene",
  "Sostituendo Cas9 con Cas6, che lega il DNA ma non è in grado di tagliarlo",
  "Usando due gRNA contigui, che bloccano fisicamente l'RNA polimerasi",
  ], 0,
  "Cas9 mutata riconosce ancora il bersaglio grazie alla guida ma non lo taglia; attaccandole un attivatore o un repressore trascrizionale, o un effettore che modifica la cromatina, si controlla l'espressione del gene.")

q("u1124-065", T, "a", "285", "Perché un enzima di restrizione non è adatto a tagliare un singolo gene del genoma umano?", [
  "Riconosce 4–8 basi, che in un genoma di 1000–3000 Mb ricorrono in molti punti",
  "Riconosce solo sequenze non palindromiche, rare nel genoma dei mammiferi",
  "Richiede la presenza di una sequenza PAM, assente nel genoma dei mammiferi",
  "Taglia soltanto DNA batterico, perché il DNA umano è protetto dalla metilazione",
  "Produce estremità coesive, che la cellula umana non è in grado di risaldare",
  ], 0,
  "CRISPR-Cas9 riconosce invece 20 paia di basi più il PAM: scegliendo bene la sequenza si può avere un sito unico di taglio su tutto il genoma.")

q("u1124-066", T, "a", "284", "Perché la sequenza PAM è importante anche per la specificità del sistema?", [
  "Perché limita i tagli ai soli siti che la presentano, evitando tagli plurimi",
  "Perché aumenta l'affinità del gRNA per le 20 basi del protospacer",
  "Perché permette a Cas9 di distinguere il filamento stampo da quello codificante",
  "Perché viene riconosciuta dal tracrRNA e stabilizza il complesso sul bersaglio",
  "Perché segnala alla cellula quale sistema di riparo deve essere attivato",
  ], 0,
  "Cas9 taglia solo se a tre paia di basi dal sito è presente la tripletta NGG: questo riduce la probabilità di tagli random sul genoma.")

q("u1124-067", T, "a", "286", "Nella correzione ex vivo di una malattia genetica con CRISPR, qual è la sequenza corretta dei passaggi?", [
  "Isolare le cellule malate, correggerle in coltura, differenziarle e trapiantarle",
  "Trapiantare le cellule sane, correggerle in vivo e poi farle differenziare",
  "Correggere lo zigote, differenziarlo in coltura e trapiantarlo nel paziente",
  "Isolare le cellule malate, differenziarle, trapiantarle e poi correggerle in vivo",
  "Somministrare Cas9 per via sistemica e selezionare in vivo le cellule corrette",
  ], 0,
  "Così si possono correggere patologie anche nell'individuo adulto, non solo nell'embrione.")

q("u1124-068", T, "a", "286", "Come è stata affrontata con CRISPR la distrofia muscolare di Duchenne?", [
  "Rimuovendo la porzione esonica responsabile dell'out-of-frame",
  "Inserendo una copia integra del gene della distrofina nel genoma",
  "Correggendo con riparo omologo la singola mutazione puntiforme del gene",
  "Aumentando i livelli trascrizionali di una proteina che sostituisce la distrofina",
  "Somministrando per tutta la vita oligonucleotidi RNA antisenso ai pazienti",
  ], 0,
  "Si taglia via il tratto fra l'esone 45 e il 55 che causa lo shift del frame: la distrofina risultante è più corta ma si ripiega e funziona. L'approccio con gli oligo antisenso richiedeva invece una terapia a vita.")

q("u1124-069", T, "a", "287", "Che cosa distingue una cellula CAR-T dal linfocita T di partenza?", [
  "La porzione extracellulare del TCR, sostituita per riconoscere il tumore",
  "La porzione intracellulare del TCR, sostituita per attivare il linfocita",
  "L'assenza completa del recettore TCR sulla superficie della cellula",
  "La presenza di un recettore inibitorio PD1 aggiuntivo sulla membrana",
  "L'espressione di molecole HLA di classe I tipiche del donatore eterologo",
  ], 0,
  "La parte intracellulare resta quella del TCR e attiva la cellula T contro l'antigene; cambiando la parte extracellulare si indirizzano i linfociti verso epitopi tumorali diversi.")

q("u1124-070", T, "a", "287", "Perché nelle cellule CAR-T «universali» si eliminano i geni per HLA I e per PD1?", [
  "HLA I renderebbe le cellule riconoscibili come estranee, PD1 ne frena l'attività",
  "HLA I impedirebbe il riconoscimento del tumore, PD1 bloccherebbe l'ingresso di Cas9",
  "HLA I ostacola l'espressione del TCR chimerico, PD1 induce la proliferazione",
  "Entrambi i geni codificano recettori inibitori che spengono il linfocita T",
  "Entrambi i geni sono necessari solo nei linfociti autologhi del paziente",
  ], 0,
  "Eliminando HLA I le cellule di un donatore eterologo possono essere usate su pazienti diversi; eliminando PD1, che funziona da freno, si toglie il recettore inibitorio.")

q("u1124-071", T, "a", "288", "Come si ottiene con CRISPR un'ampia delezione in una regione del genoma?", [
  "Usando due gRNA diretti su regioni distanti, con risaldatura non omologa",
  "Usando un solo gRNA e lasciando agire ripetutamente la nucleasi Cas9 sul locus",
  "Usando un gRNA più lungo, che riconosce un tratto esteso di protospacer",
  "Usando un DNA donatore accorciato come templato per il riparo omologo",
  "Usando Cas9 mutata, che taglia un solo filamento alla volta del DNA",
  ], 0,
  "I due tagli generano la delezione del tratto compreso, e le estremità vengono poi unite dal sistema non omologo.")

q("u1124-072", T, "l", "282", "In quale anno e in quale organismo furono identificate per la prima volta le sequenze CRISPR?", [
  "Nel 1987, in E. coli",
  "Nel 2000, in E. coli",
  "Nel 2002, in Streptococcus thermophilus",
  "Nel 2005, in Streptococcus thermophilus",
  "Nel 2007, in Staphylococcus aureus",
  ], 0,
  "Nel 1987 si videro ripetizioni interspaziate senza capirne la funzione; nel 2000 furono ritrovate in altri batteri, nel 2002 ebbero il nome CRISPR e furono associate ai geni Cas.")

q("u1124-073", T, "l", "282", "In quale batterio si dimostrò per la prima volta, nel 2007, che gli spacer conferiscono resistenza ai fagi?", [
  "Streptococcus thermophilus",
  "Escherichia coli",
  "Staphylococcus aureus",
  "Agrobacterium tumefaciens",
  "Mycobacterium tuberculosis",
  ], 0,
  "In presenza dei sistemi CRISPR lo streptococco risultava più resistente all'infezione fagica: da qui l'idea del «sistema immunitario» batterico.")

q("u1124-074", T, "l", "288", "Quale sequenza deve contenere il plasmide che porta Cas9, perché la proteina raggiunga il bersaglio?", [
  "Una NLS, sequenza di localizzazione nucleare",
  "Una sequenza PAM, posta a valle del gene di Cas9",
  "Una sequenza rbs, riconosciuta dal ribosoma dell'ospite",
  "Una sequenza cos, che permette il packaging del plasmide",
  "Una sequenza ori, riconosciuta dalla DNA polimerasi nucleare",
  ], 0,
  "Il plasmide contiene la guida con promotore e terminatore, il gene di Cas9, le NLS che portano la proteina nel nucleo e spesso un fluoroforo per individuare le cellule trasformate.")

q("u1124-075", T, "l", "282", "Quando è stato chiarito il meccanismo con cui i batteri usano gli spacer come sistema immunitario?", [
  "Nel 2012, da Doudna e Charpentier",
  "Nel 2015, da Doudna e Charpentier",
  "Nel 2007, da Doudna e Charpentier",
  "Nel 2012, da Mullis e Sanger",
  "Nel 2020, da Mullis e Sanger",
  ], 0,
  "Il lavoro che descrive il sistema CRISPR-Cas9 programmabile è del 2012; il Nobel per la chimica alle due ricercatrici è arrivato nel 2020.",
  note="Errore nella sbobina (Biochimica I, p. 282): colloca la scoperta nel 2015. Il lavoro chiave di Doudna e Charpentier è del 2012; il 2020 è l'anno del Nobel.")

q("u1124-076", T, "h", "285", "Si vuole eliminare la funzione di un gene in una linea cellulare umana. Quale strategia è la più diretta?", [
  "Tagliare con Cas9 e lasciare che il riparo non omologo introduca indels",
  "Tagliare con Cas9 e fornire un DNA donatore con la sequenza corretta",
  "Usare Cas9 mutata legata a un attivatore trascrizionale del gene bersaglio",
  "Digerire il gene con un enzima di restrizione specifico per quella sequenza",
  "Fornire oligonucleotidi antisenso che blocchino la traduzione del messaggero",
  ], 0,
  "L'NHEJ aggiunge o toglie nucleotidi in modo casuale: lo shift del frame genera una proteina non funzionale, cioè un knock out. Il donatore serve invece quando si vuole correggere.")

q("u1124-077", T, "h", "288", "Nel trattamento sperimentale dell'infezione da HIV con CRISPR, quale bersaglio viene modificato?", [
  "Il co-recettore CCR5, senza il quale il virus non completa l'ingresso",
  "Il recettore CD4, senza il quale il virus non riconosce il linfocita T",
  "Il gene della trascrittasi inversa, integrato nel genoma della cellula",
  "Il recettore inibitorio PD1, che frena la risposta dei linfociti T",
  "La proteina HLA di classe I, che il virus usa per entrare nella cellula",
  ], 0,
  "HIV riconosce CD4 e ha bisogno di un co-recettore: mutando quest'ultimo l'infezione non si completa. Si agisce sul co-recettore e non su CD4 perché CD4 è indispensabile alla funzione del linfocita.",
  note="Errore nella sbobina (Biochimica I, p. 288): il co-recettore di HIV è indicato come «CXCR5». Il co-recettore corretto è CCR5 (per i ceppi a tropismo macrofagico; l'altro è CXCR4). CXCR5 è un recettore dei linfociti B follicolari.")

q("u1124-078", T, "h", "286", "Nei trial clinici sulle emoglobinopatie con CRISPR, su quale meccanismo si punta?", [
  "Aumentare i livelli trascrizionali dell'emoglobina fetale HbF",
  "Correggere con riparo omologo ogni singola mutazione della catena β",
  "Sostituire le cellule staminali ematopoietiche con cellule di donatore sano",
  "Inserire nel genoma una copia aggiuntiva del gene della catena α",
  "Bloccare la trascrizione del gene della catena α con Cas9 mutata",
  ], 0,
  "Si ingegnerizzano le cellule staminali ematopoietiche: eliminata la funzione patologica della catena β, si rimpiazza quella funzione incrementando l'HbF con una seconda correzione genica.")

q("u1124-079", T, "h", "283", "Un batterio con un sistema CRISPR funzionante viene infettato da un fago già incontrato in passato. Che cosa succede?", [
  "Il crRNA riconosce il protospacer e Cas9 taglia il DNA fagico",
  "Il tracrRNA riconosce il protospacer e Cas6 taglia il DNA fagico",
  "Il DNA fagico viene metilato e reso inattivo senza essere tagliato",
  "Il batterio acquisisce un nuovo spacer ma non elimina il DNA invasore",
  "Gli enzimi di restrizione tagliano il DNA fagico nelle sue sequenze palindromiche",
  ], 0,
  "È la fase di interferenza: il crRNA, prodotto dallo spacer acquisito nella prima infezione, riconosce per complementarietà il DNA estraneo, il tracrRNA si appaia alla repeat e Cas9 esegue il taglio in presenza del PAM.")

q("u1124-080", T, "h", "289", "Si vuole visualizzare in vivo la posizione di un locus genico senza alterarlo. Come si può usare il sistema CRISPR?", [
  "Legando una proteina fluorescente a Cas9 priva di attività nucleasica",
  "Legando una proteina fluorescente al gRNA, che resta legato al locus bersaglio",
  "Usando Cas9 attiva e marcando con un fluoroforo il DNA donatore",
  "Usando Cas6 marcata, che riconosce le repeats sul locus bersaglio",
  "Marcando la sequenza PAM con una sonda fluorescente complementare",
  ], 0,
  "La Cas9 mutata lega il bersaglio senza tagliarlo: attaccandole un fluoroforo si fa imaging, attaccandole un attivatore o un repressore si controlla la trascrizione.")

q("u1124-081", T, "h", "287", "Perché il mais waxy ottenuto con CRISPR solleva un dibattito sulla definizione di OGM?", [
  "Perché è stato modificato un locus proprio, senza inserire DNA estraneo",
  "Perché il gene modificato proviene da una pianta di una specie diversa",
  "Perché la modifica riguarda solo l'RNA e non il DNA della pianta",
  "Perché la stessa varietà non esiste in natura e non ha precedenti noti",
  "Perché la modifica è stata ottenuta infettando la pianta con Agrobacterium",
  ], 0,
  "Con gli OGM in agricoltura si intendono di solito piante in cui viene trapiantato DNA estraneo; qui è stato modificato il locus waxy, che codifica una glicosil transferasi, e la varietà esiste anche in natura.")

q("u1124-082", T, "a", "281", "Che cosa rappresentano, in origine, gli spacer di un locus CRISPR?", [
  "Frammenti di DNA di fagi incontrati in infezioni precedenti",
  "Frammenti di DNA plasmidico trasferiti per coniugazione fra batteri",
  "Copie ripetute di geni batterici essenziali, conservate come riserva",
  "Sequenze palindromiche riconosciute dagli enzimi di restrizione del batterio",
  "Residui della degradazione dell'RNA messaggero batterico, riciclati nel genoma",
  ], 0,
  "È la memoria dell'infezione: il DNA esogeno tagliato viene in parte conservato fra le ripetizioni e trasmesso alle generazioni successive.")

q("u1124-083", T, "m", "285", "Quante paia di basi del DNA bersaglio vengono riconosciute dal sistema CRISPR-Cas9?", [
  "20",
  "12",
  "8",
  "36",
  "45",
  ], 0,
  "Sono i 20 nucleotidi del protospacer, che nella guida vengono cambiati di volta in volta per bersagliare qualunque punto del genoma; resta costante la parte che permette l'interazione fra CRISPR e tracr.")

q("u1124-084", T, "f", "284", "Quale attività enzimatica svolge Cas9?", [
  "Nucleasica, taglia il doppio filamento di DNA",
  "Ligasica, salda le estremità del DNA tagliato",
  "Polimerasica, allunga il filamento a partire dalla guida",
  "Elicasica, separa i due filamenti del DNA bersaglio",
  "Metiltransferasica, modifica le basi del DNA invasore",
  ], 0,
  "Taglia il doppio filamento del DNA estraneo riconosciuto dal protospacer del crRNA, a condizione che sia presente il PAM.")


# ── Vitamine liposolubili (p. 217–218) ──────────────────────────────────────
V = "d11-vitad"

q("u1124-085", V, "f", "217", "In quale forma viene assorbito il retinolo?", [
  "Come estere, per esempio con l'acido palmitico",
  "Come aldeide libera, cioè come retinale",
  "Come acido retinoico, dopo ossidazione nell'enterocita",
  "Come β-carotene intatto, non ancora scisso",
  "Come alcol libero, legato all'albumina plasmatica",
  ], 0,
  "L'esterificazione del gruppo alcolico lo rende idrofobico; nel sangue viene poi trasportato dalla retinol binding protein ai siti di deposito.")

q("u1124-086", V, "f", "218", "Da quale precursore deriva la vitamina D3?", [
  "Dal colesterolo",
  "Dal β-carotene",
  "Dall'acido palmitico",
  "Dall'ergosterolo dei vegetali",
  "Dal retinolo immagazzinato nel fegato",
  ], 0,
  "L'ossidazione del doppio legame fra C7 e C8 dà il 7-deidrocolesterolo, che nella pelle viene attivato dalla luce solare.")

q("u1124-087", V, "m", "217", "Dove vengono depositate nell'organismo le vitamine liposolubili?", [
  "Nei siti di deposito epatici, come lo spazio di Disse",
  "Nel tessuto adiposo bruno, insieme ai trigliceridi di riserva",
  "Nei lisosomi delle cellule intestinali, in forma esterificata",
  "Nel plasma, legate stabilmente all'albumina circolante",
  "Nelle membrane dei globuli rossi, inserite fra i fosfolipidi",
  ], 0,
  "È proprio la possibilità di essere depositate a distinguerle dalle vitamine idrosolubili; di conseguenza possono anche accumularsi fino alla tossicità.")

q("u1124-088", V, "m", "217", "Quale ruolo ha il retinolo nella sintesi delle glicoproteine?", [
  "Funziona da analogo del dolicolo nel trasferimento delle catene oligosaccaridiche",
  "Funziona da coenzima della glicogeno sintasi nell'allungamento della catena",
  "Funziona da trasportatore di gruppi metilici verso le catene glicaniche in formazione",
  "Funziona da attivatore allosterico delle glicosiltransferasi del reticolo",
  "Funziona da donatore di zuccheri attivati nel lume dell'apparato di Golgi",
  ], 0,
  "Il dolicolo è il trasportatore lipidico che porta la catena oligosaccaridica da trasferire alla proteina.")

q("u1124-089", V, "m", "218", "Che cosa provoca la luce solare sul 7-deidrocolesterolo?", [
  "Rompe il legame fra C9 e C10, con formazione di un doppio legame sul C19",
  "Rompe il legame fra C7 e C8, con formazione di un doppio legame sul C19",
  "Introduce un gruppo ossidrilico sul C25, generando il calcidiolo",
  "Introduce un gruppo ossidrilico sul C1, generando la forma attiva",
  "Rompe il legame fra C1 e C25, aprendo il nucleo steroideo in due anelli distinti",
  ], 0,
  "È la rottura fotochimica dell'anello; le idrossilazioni in C25 e C1 vengono dopo, nel fegato e nel rene.")

q("u1124-090", V, "a", "218", "Qual è la sequenza corretta di attivazione della vitamina D3?", [
  "Idrossilazione in C25 nel fegato, poi idrossilazione in C1 nel rene",
  "Idrossilazione in C1 nel fegato, poi idrossilazione in C25 nel rene",
  "Idrossilazione in C25 nel rene, poi idrossilazione in C1 nel fegato",
  "Doppia idrossilazione, in C1 e in C25, entrambe a livello epatico",
  "Doppia idrossilazione, in C1 e in C25, entrambe a livello renale",
  ], 0,
  "Dopo la prima idrossilazione si ottiene il calcidiolo, che può essere accumulato nel fegato o proseguire verso il rene per l'idrossilazione in C1.")

q("u1124-091", V, "a", "218", "Perché la vitamina D viene definita un ormone?", [
  "Agisce in sinergia con il paratormone aumentando la calcemia",
  "Viene trasportata nel sangue da una proteina di trasporto specifica",
  "Deriva dal colesterolo, come tutti i composti a struttura steroidea",
  "Viene assunta con la dieta in quantità molto piccole, come le vitamine",
  "Viene attivata da due idrossilazioni successive in organi diversi",
  ], 0,
  "A livello intestinale favorisce l'assorbimento di calcio e fosfato e nel rene ne aumenta il riassorbimento: ha un bersaglio a distanza e un effetto regolatorio, come un ormone.")

q("u1124-092", V, "l", "217", "Secondo la sbobina, a quale conseguenza porta la carenza di vitamina A per via della ridotta sintesi di glicoproteine?", [
  "All'anemia, per ridotta sintesi di transferrina",
  "All'emofilia, per ridotta sintesi dei fattori della coagulazione",
  "All'osteoporosi, per ridotta sintesi di osteocalcina",
  "Alla steatosi epatica, per ridotta sintesi delle apolipoproteine",
  "Alla trombofilia, per ridotta sintesi di antitrombina III",
  ], 0,
  "Il retinolo serve alla sintesi delle glicoproteine, fra cui la transferrina. La slide della stessa pagina elenca fra le conseguenze della carenza anche xeroftalmia, cecità crepuscolare e ritardo dell'accrescimento.")


# ── Digestione, assorbimento e trasporto dei grassi (p. 219–221) ────────────
D = "d12-digestione"

q("u1124-093", D, "f", "219", "Dove avvengono la digestione e l'assorbimento dei grassi?", [
  "Esclusivamente nell'intestino",
  "Prevalentemente nello stomaco",
  "Nello stomaco e nel duodeno in misura uguale",
  "Nel fegato, dopo il passaggio dal circolo portale",
  "Nel tessuto adiposo, dove i grassi vengono depositati",
  ], 0,
  "L'intestino tenue riceve gli enzimi idrolitici del pancreas e i sali biliari.")

q("u1124-094", D, "f", "220", "Che funzione hanno i sali biliari, come l'acido colico?", [
  "Emulsionano i lipidi formando micelle aggredibili dalla lipasi",
  "Idrolizzano il legame estere dei trigliceridi liberando acidi grassi",
  "Trasportano i trigliceridi assorbiti dall'intestino verso il fegato",
  "Attivano per proteolisi il precursore inattivo della lipasi pancreatica",
  "Neutralizzano l'acidità del chimo prima dell'arrivo degli enzimi pancreatici",
  ], 0,
  "Sono potenti tensioattivi: l'idrolisi del legame estere è invece compito della lipasi pancreatica.")

q("u1124-095", D, "m", "220", "Che cosa rende insolita la lipasi pancreatica?", [
  "Si attiva solo all'interfaccia fra ambiente oleoso e ambiente acquoso",
  "Si attiva solo in presenza di un pH fortemente acido come quello gastrico",
  "Si attiva solo dopo taglio proteolitico operato dalla tripsina nel duodeno",
  "Si attiva solo quando il substrato è completamente solubilizzato in acqua",
  "Si attiva solo in assenza di calcio, che altrimenti ne blocca il sito attivo",
  ], 0,
  "È un enzima Ca²⁺-dipendente che all'interfaccia olio-acqua subisce un cambiamento conformazionale, in presenza dei due substrati.")

q("u1124-096", D, "m", "219", "Qual è la differenza di origine fra chilomicroni e VLDL?", [
  "I chilomicroni sono di origine intestinale, le VLDL di origine epatica",
  "I chilomicroni sono di origine epatica, le VLDL di origine intestinale",
  "Entrambi sono di origine intestinale, ma le VLDL si formano a digiuno",
  "Entrambi sono di origine epatica, ma i chilomicroni si formano dopo i pasti",
  "I chilomicroni derivano dal tessuto adiposo, le VLDL dall'intestino tenue",
  ], 0,
  "I chilomicroni portano ai tessuti i grassi assorbiti con la dieta; il fegato distribuisce con le VLDL il colesterolo e gli acidi grassi che sintetizza.")

q("u1124-097", D, "a", "219", "Perché il trasporto dei grassi nel sangue richiede lipoproteine e albumina?", [
  "Perché i grassi non sono solubili e non circolerebbero liberi nel plasma",
  "Perché i grassi verrebbero altrimenti filtrati ed eliminati dal rene",
  "Perché i grassi liberi sarebbero degradati dalle lipasi plasmatiche",
  "Perché solo in questa forma i grassi attraversano la parete intestinale",
  "Perché le lipoproteine impediscono ai grassi di essere ossidati nel sangue",
  ], 0,
  "Servono sia proteine trasportatrici che li trasferiscano ai tessuti, sia sistemi che ne favoriscano la digestione. L'albumina trasporta gli acidi grassi liberati dal tessuto adiposo.")

q("u1124-098", D, "a", "219", "A che cosa servono i trigliceridi trasportati dai chilomicroni ai tessuti?", [
  "A essere depositati nel tessuto adiposo oppure usati per ricavare energia",
  "A essere trasformati in colesterolo nei tessuti extraepatici",
  "A essere riesportati verso il fegato, dove vengono poi degradati",
  "A entrare nelle membrane cellulari come componente strutturale",
  "A essere coniugati con i sali biliari per essere eliminati con la bile nell'intestino",
  ], 0,
  "I chilomicroni possono portare i trigliceridi al tessuto adiposo per il deposito oppure ai tessuti che li utilizzano a scopo energetico.")

q("u1124-099", D, "h", "220", "Un paziente con ostruzione delle vie biliari presenta grassi non digeriti nelle feci, pur avendo un pancreas funzionante. Perché?", [
  "Senza sali biliari i grassi non vengono emulsionati e la lipasi non li aggredisce",
  "Senza sali biliari la lipasi pancreatica non viene attivata dalla tripsina duodenale",
  "Senza sali biliari manca il calcio necessario all'attività della lipasi",
  "Senza sali biliari i chilomicroni non si formano nella parete intestinale",
  "Senza sali biliari gli acidi grassi liberati non possono legarsi all'albumina",
  ], 0,
  "La lipasi c'è e funziona, ma si attiva all'interfaccia olio-acqua: senza l'emulsione prodotta dai sali biliari quell'interfaccia è troppo piccola e il substrato resta inaccessibile.")


# ── Lipoproteine (p. 220–221) ───────────────────────────────────────────────
L = "d12-lipoproteine"

q("u1124-100", L, "f", "220", "Quale lipoproteina ha la densità più bassa in assoluto?", [
  "Il chilomicrone, che è anche il più grande",
  "La LDL, che trasporta il colesterolo ai tessuti",
  "La VLDL, che è la seconda per diametro",
  "La HDL, che è la più piccola di tutte",
  "La IDL, intermedia fra VLDL e LDL",
  ], 0,
  "La densità dipende dal contenuto proteico: più grassi ci sono, meno proteine, più la densità è bassa.")

q("u1124-101", L, "f", "220", "A che cosa si riferisce la densità che dà il nome alle lipoproteine?", [
  "Al loro contenuto proteico",
  "Al loro contenuto di colesterolo",
  "Al loro diametro in nanometri",
  "Al loro contenuto di fosfolipidi",
  "Alla loro velocità di migrazione elettroforetica",
  ], 0,
  "Le proteine sono più dense dei lipidi: una particella ricca di grassi e povera di proteine, come il chilomicrone, ha densità bassissima.")

q("u1124-102", L, "m", "220", "Quale componente è largamente prevalente in un chilomicrone?", [
  "I triacilgliceroli, che sono circa l'84% del peso secco",
  "Il colesterolo, che è circa il 50% del peso secco",
  "Le proteine, che sono circa il 33% del peso secco",
  "I fosfolipidi, che sono circa il 29% del peso secco",
  "I triacilgliceroli, che sono circa il 31% del peso secco",
  ], 0,
  "Le proteine sono appena l'1–2%. Il 50% di colesterolo è la composizione tipica delle LDL, il 33% di proteine quella delle HDL.")

q("u1124-103", L, "m", "220", "Quali componenti trasportano le VLDL, oltre ai trigliceridi?", [
  "Colesterolo e fosfolipidi",
  "Soltanto acidi grassi liberi",
  "Soltanto esteri del colesterolo",
  "Proteine plasmatiche e vitamine idrosolubili",
  "Sali biliari destinati al ricircolo entero-epatico",
  ], 0,
  "Sono lipoproteine a densità molto bassa prodotte dal fegato, che distribuisce così i grassi che sintetizza.")

q("u1124-104", L, "a", "220", "Due lipoproteine hanno rispettivamente il 25% e il 33% di proteine sul peso secco. Quale affermazione è corretta?", [
  "Quella al 33% è una HDL e ha densità maggiore della prima",
  "Quella al 33% è una LDL e ha densità minore della prima",
  "Quella al 25% è una VLDL e ha il diametro maggiore delle due",
  "Quella al 25% è una HDL e trasporta soprattutto triacilgliceroli",
  "Le due hanno la stessa densità, perché contano solo i lipidi",
  ], 0,
  "Più proteine, più densità: con il 33% si è nelle HDL (1,063–1,21 g/mL, 5–15 nm), con il 25% nelle LDL (1,019–1,063 g/mL, 18–28 nm).")

q("u1124-105", L, "l", "220", "Qual è il diametro tipico di una HDL?", [
  "5–15 nm",
  "18–28 nm",
  "25–50 nm",
  "30–80 nm",
  "100–500 nm",
  ], 0,
  "È la più piccola e la più densa; i chilomicroni, i più grandi, arrivano a 100–500 nm.")
