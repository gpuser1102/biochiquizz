"""Blocco 5 – Gluconeogenesi (sbobina di Biochimica II, p. 140–158)."""
from bank_common import q

T = "m5-fonti"
q("m5f-01", T, "f", "140", "Quali sono i precursori non glucidici della gluconeogenesi?", ["Lattato, amminoacidi (alanina), glicerolo", "Acidi grassi a catena pari", "Acetil-CoA e corpi chetonici", "Colesterolo e glicerolo"], 0,
  "Dagli acidi grassi a catena pari non si forma glucosio; il propionil-CoA dei grassi dispari sì.")
q("m5f-02", T, "f", "140", "Dove avviene la gluconeogenesi?", ["Soprattutto nel fegato (circa 90%) e nel rene", "Nel muscolo scheletrico", "Nel cervello", "Negli eritrociti"], 0,
  "Il rene contribuisce soprattutto di notte e nel digiuno prolungato.")
q("m5f-03", T, "m", "141", "Quali sono le tre fonti di glucosio ematico durante la giornata?", ["Dieta, glicogenolisi, gluconeogenesi", "Dieta, β-ossidazione, chetogenesi", "Glicolisi, glicogenolisi, lipolisi", "Solo dieta e glicogeno"], 0,
  "Dopo i pasti prevale la dieta, tra un pasto e l'altro la glicogenolisi, di notte cresce la gluconeogenesi.")
q("m5f-04", T, "m", "142", "Quale ormone, con ritmo circadiano, sostiene la gluconeogenesi notturna?", ["Cortisolo", "Insulina", "Melatonina", "Ossitocina"], 0,
  "Il cortisolo ha il minimo verso mezzanotte e il picco al mattino.")
q("m5f-05", T, "a", "149", "Su quali tessuti agisce il cortisolo per favorire la gluconeogenesi?", [
  "Fegato (enzimi), muscolo (libera alanina dalle proteine), tessuto adiposo (rende disponibile il glicerolo)",
  "Solo sul fegato", "Pancreas e cervello", "Rene e intestino"], 0,
  "Per questo una terapia cortisonica può peggiorare la glicemia dei diabetici e far perdere massa muscolare.")
q("m5f-06", T, "a", "157", "Nel digiuno prolungato la gluconeogenesi a un certo punto si riduce. Perché?", [
  "Per risparmiare le proteine muscolari: il cervello usa sempre più corpi chetonici",
  "Perché finisce il glicogeno", "Perché il cortisolo scende a zero", "Perché il lattato si esaurisce"], 0,
  "Dopo il picco (circa 24–48 ore) la chetogenesi copre il fabbisogno e protegge la massa muscolare.")
q("m5f-07", T, "l", "140", "Quale enzima, senza cui il fegato non libera glucosio, è legato al reticolo endoplasmatico?", ["Glucosio 6-fosfatasi", "Glucochinasi", "Fruttosio 1,6-bisfosfatasi", "Fosfoglucomutasi"], 0,
  "Il G6P entra nel RE (trasportatore T1), viene idrolizzato e il glucosio esce (T3).")

T = "m5-reazioni"
q("m5r-01", T, "f", "143", "Quali tappe della glicolisi la gluconeogenesi deve aggirare?", [
  "Esochinasi, PFK1, piruvato chinasi", "Aldolasi, enolasi, PGK", "GAPDH, TPI, PGM", "Solo la piruvato chinasi"], 0,
  "Sono le tre reazioni con ΔG molto negativo; le altre sono reversibili e usate al contrario.")
q("m5r-02", T, "f", "144", "Quale coenzima usa la piruvato carbossilasi?", ["Biotina", "Tiamina pirofosfato", "Piridossal fosfato", "Lipoato"], 0,
  "La biotina trasporta il carbossile dal bicarbonato al piruvato.")
q("m5r-03", T, "m", "145", "Perché l'ossalacetato esce dal mitocondrio come malato?", [
  "Perché non ha un trasportatore nella membrana mitocondriale interna", "Perché il malato è più energetico", "Per consumare NADH nel citosol", "Perché l'ossalacetato è instabile"], 0,
  "La malato deidrogenasi mitocondriale lo riduce, quella citosolica lo riossida: così esce anche il NADH che serve alla GAPDH.")
q("m5r-04", T, "m", "147", "Bilancio energetico della gluconeogenesi da 2 piruvato:", ["4 ATP + 2 GTP + 2 NADH", "2 ATP + 2 NADH", "6 ATP", "2 ATP + 2 GTP"], 0,
  "6 legami ad alta energia per un glucosio; il ΔG°' complessivo è circa −38 kJ/mol, mentre la glicolisi inversa sarebbe +84.")
q("m5r-05", T, "m", "145", "Che cosa spinge la reazione della PEPCK verso la formazione del fosfoenolpiruvato?", [
  "La decarbossilazione: esce la CO₂ aggiunta dalla piruvato carbossilasi", "L'idrolisi di due ATP", "L'ossidazione del NADH", "Il trasporto nel mitocondrio"], 0,
  "Formare il PEP costa in tutto due nucleotidi (ATP nella carbossilazione, GTP nella PEPCK).")
q("m5r-06", T, "a", "150", "Se la gluconeogenesi parte dal lattato invece che dall'alanina, come cambia la via?", [
  "Il NADH citosolico viene dalla LDH: l'OAA viene trasformato in PEP già nel mitocondrio dalla PEPCK mitocondriale",
  "Il lattato entra direttamente come PEP", "Serve più biotina", "Non cambia nulla"], 0,
  "Dall'alanina il NADH citosolico si ottiene facendo uscire il malato; dal lattato lo fornisce già la LDH.")
q("m5r-07", T, "a", "146", "Un paziente con deficit di glucosio 6-fosfatasi (glicogenosi di tipo I) ha ipoglicemia grave. Perché?", [
  "Perché né la glicogenolisi né la gluconeogenesi epatiche possono liberare glucosio nel sangue",
  "Perché non può fare glicolisi", "Perché non produce insulina", "Perché non assorbe glucosio"], 0,
  "Entrambe le vie finiscono nel G6P, che senza la fosfatasi non diventa glucosio libero.",
  note="Sbobina di Biochimica II, p. 146: c'è scritto «malattia di tipo 1 di diabete mellito». Dal contesto (nessuna via di ripristino della glicemia funziona) si tratta della glicogenosi di tipo I (malattia di von Gierke).")
q("m5r-08", T, "a", "152", "Durante la gluconeogenesi epatica, perché la piruvato chinasi va bloccata?", [
  "Per non riconvertire il PEP in piruvato in un ciclo futile che sprecherebbe ATP e GTP", "Perché consuma NADH", "Perché produce lattato", "Perché inibisce la PEPCK"], 0,
  "Il glucagone la fa fosforilare dalla PKA, ed è l'isoforma epatica (L) a essere regolata così.")
q("m5r-09", T, "l", "145", "Quale nucleotide usa la PEPCK citosolica?", ["GTP", "ATP", "UTP", "CTP"], 0,
  "OAA + GTP → PEP + GDP + CO₂.",
  note="Sbobina di Biochimica II, p. 145: c'è scritto che si formano PEP, «ADP» e CO₂. Si forma GDP.")
q("m5r-10", T, "l", "144", "Quale molecola attiva allostericamente la piruvato carbossilasi?", ["Acetil-CoA", "ADP", "Fruttosio 2,6-bisfosfato", "Citrato"], 0,
  "Di notte la β-ossidazione epatica produce acetil-CoA, che indirizza il piruvato verso l'ossalacetato.",
  note="Sbobina di Biochimica II, p. 144: c'è scritto che l'acetil-CoA attiva la «piruvato decarbossilazione». Attiva la piruvato carbossilasi.")
q("m5r-11", T, "l", "146", "Nella gluconeogenesi, quale enzima converte il fruttosio 1,6-bisfosfato in fruttosio 6-fosfato?", ["Fruttosio 1,6-bisfosfatasi", "Fosfofruttochinasi 2", "Fruttosio 2,6-bisfosfatasi", "Aldolasi"], 0,
  "Idrolizza il fosfato in C1. Non va confusa con la fruttosio 2,6-bisfosfatasi (dominio della PFK2).")

T = "m5-glicerolo"
q("m5g-01", T, "f", "147", "Da dove viene il glicerolo usato nella gluconeogenesi?", ["Dalla lipolisi dei trigliceridi del tessuto adiposo", "Dalla glicolisi muscolare", "Dagli amminoacidi", "Dai corpi chetonici"], 0,
  "Arriva al fegato col sangue.")
q("m5g-02", T, "m", "147", "Perché la via del glicerolo è «più semplice» della gluconeogenesi dal piruvato?", [
  "Perché entra come diidrossiacetone fosfato, saltando il bypass piruvato → PEP", "Perché non consuma ATP", "Perché non avviene nel fegato", "Perché non serve NAD⁺"], 0,
  "Glicerolo → glicerolo 3-P → DHAP, poi la via prosegue verso il fruttosio 1,6-bisfosfato.")
q("m5g-03", T, "a", "149", "Perché il tessuto adiposo non può usare da sé il glicerolo dei trigliceridi?", [
  "Perché non ha la glicerolo chinasi: il glicerolo deve andare al fegato", "Perché lo consuma tutto nella β-ossidazione", "Perché è tossico", "Perché manca la glicerolo 3-P deidrogenasi"], 0,
  "Per questo il glicerolo liberato dalla lipolisi è un substrato gluconeogenico epatico.",
  note="L'assenza della glicerolo chinasi nell'adipocita non è nella sbobina (Lehninger).")
q("m5g-04", T, "l", "141, 147", "Il glicerolo 3-fosfato della sbobina è chiamato anche glicerolo 1-fosfato. Perché?", [
  "Per la numerazione: è lo stesso composto (sn-glicerolo 3-fosfato = L-glicerolo 3-fosfato)", "Perché sono due isomeri diversi", "Perché uno è nel fegato e l'altro nel muscolo", "È un errore: il glicerolo 1-fosfato non esiste"], 0,
  "La numerazione stereospecifica (sn) dà sn-glicerolo 3-fosfato.")

T = "m5-regolazione"
q("m5reg-01", T, "f", "150", "Come viene regolata soprattutto la PEPCK?", ["Variando la quantità di enzima (sintesi)", "Per fosforilazione", "Allostericamente dall'AMP", "Per compartimentazione nel nucleo"], 0,
  "È un meccanismo lento: elementi di risposta nel promotore controllano la trascrizione.")
q("m5reg-02", T, "f", "153", "Il fruttosio 2,6-bisfosfato:", ["Attiva la PFK1 e inibisce la fruttosio 1,6-bisfosfatasi", "Inibisce la PFK1 e attiva la fruttosio 1,6-bisfosfatasi", "Attiva entrambe", "È un intermedio della glicolisi"], 0,
  "Quando c'è si fa glicolisi, quando manca si fa gluconeogenesi.")
q("m5reg-03", T, "m", "151", "Quali elementi del promotore della PEPCK ne stimolano la sintesi?", [
  "GRE (glucocorticoidi), TRE (ormoni tiroidei), CRE (cAMP/glucagone)", "IRE (insulina)", "SRE (steroli)", "HRE (ipossia)"], 0,
  "L'insulina invece riduce la sintesi.")
q("m5reg-04", T, "m", "153", "Come agisce il glucagone sulla PFK2 epatica?", [
  "La fa fosforilare: prevale l'attività fosfatasica, scende il F2,6BP e parte la gluconeogenesi",
  "La defosforila: sale il F2,6BP", "La degrada", "La sposta nel nucleo"], 0,
  "L'insulina fa l'opposto: defosforila, prevale la chinasi, sale il F2,6BP.",
  note="Sbobina di Biochimica II, p. 154: c'è scritto che con l'insulina «si attiva il dominio fosfatasico (N terminale)» e con il glucagone «il dominio chinasico (C terminale)». È il contrario, come dice la stessa sbobina a p. 153: l'insulina attiva la chinasi (N-terminale), il glucagone la fosfatasi (C-terminale).")
q("m5reg-05", T, "a", "152", "Come fa l'insulina a ridurre la sintesi della PEPCK?", [
  "Attiva la PKB, che fosforila FOXO1: il fattore viene degradato dal proteasoma e non attiva più il gene",
  "Lega direttamente il DNA", "Fosforila la PEPCK", "Aumenta il cAMP"], 0,
  "È il meccanismo con cui l'IRE risponde all'insulina.",
  note="Sbobina di Biochimica II, p. 152: il fattore è chiamato «FOX1». Il nome corretto è FOXO1.")
q("m5reg-06", T, "a", "156–157", "Il glucagone nel fegato aumenta la glicemia agendo su più enzimi. Quale effetto è sbagliato?", [
  "Attiva la glicogeno sintasi", "Attiva la glicogeno fosforilasi", "Abbassa il fruttosio 2,6-bisfosfato", "Inattiva la piruvato chinasi"], 0,
  "La PKA inattiva la glicogeno sintasi: tutto converge sul liberare glucosio.")
q("m5reg-07", T, "a", "155", "La fruttosio 1,6-bisfosfatasi è inibita da F2,6BP e da AMP. Che senso ha l'AMP?", [
  "AMP alto segnala fame energetica: la cellula deve fare glicolisi, non spendere ATP per fare glucosio",
  "L'AMP è un prodotto della gluconeogenesi", "L'AMP attiva la PEPCK", "Non ha senso fisiologico"], 0,
  "Lo stesso AMP attiva la PFK1: le due vie sono regolate in modo reciproco.",
  note="Sbobina di Biochimica II, p. 155: si parla del «fruttosio 1,6 bisfosfato inibito da F2,6BP e AMP». Si intende la fruttosio 1,6-bisfosfatasi.")
q("m5reg-08", T, "l", "154", "Perché la PFK2 si definisce un enzima «tandem» (bifunzionale)?", [
  "Perché ha due attività opposte (chinasi e fosfatasi) su un'unica catena, in due domini diversi", "Perché è formato da due subunità identiche", "Perché lavora in coppia con la PFK1", "Perché usa due ATP"], 0,
  "PFK-2/FBPase-2: la fosforilazione decide quale dominio lavora.")
q("m5reg-09", T, "l", "151", "Come si chiama il fattore di trascrizione inibito dall'insulina che stimola la PEPCK?", ["FOXO1", "CREB", "SREBP", "HIF-1α"], 0,
  "PKB/Akt lo fosforila e ne causa l'esclusione dal nucleo e la degradazione.")
q("m5reg-10", T, "l", "155", "Quale effetto ha l'ADP sulla PEPCK?", ["La inibisce", "La attiva", "Nessun effetto", "La sposta nel mitocondrio"], 0,
  "Con poca energia non conviene spendere GTP per fare PEP.",
  note="Sbobina di Biochimica II, p. 155: c'è scritto che la PEPCK è favorita dall'ADP, con un dubbio aggiunto da chi ha sbobinato. Nei testi di riferimento l'ADP inibisce la PEPCK. Se a lezione è stato detto diversamente, fallo presente segnalandolo.")

T = "m5-approfondimenti"
q("m5a-01", T, "f", "158", "Perché bere alcol a digiuno può causare ipoglicemia?", [
  "L'ossidazione dell'etanolo aumenta il NADH e blocca lattato → piruvato e malato → ossalacetato",
  "L'etanolo stimola l'insulina", "L'etanolo consuma glucosio", "L'etanolo blocca l'assorbimento intestinale"], 0,
  "Senza NAD⁺ i precursori non entrano nella gluconeogenesi.",
  note="Sbobina di Biochimica II, p. 158: c'è scritto che l'acetaldeide viene «ulteriormente ossidata ad ossalacetato». Viene ossidata ad acetato.")
q("m5a-02", T, "m", "156", "Quali stimoli aumentano la secrezione di glucagone?", ["Ipoglicemia, amminoacidi, catecolammine", "Iperglicemia e insulina", "Acidi grassi e corpi chetonici", "Cortisolo e melatonina"], 0,
  "È inibita da iperglicemia e insulina.")
q("m5a-03", T, "m", "156", "Con il jet lag, che cosa succede alla gluconeogenesi nei primi giorni?", [
  "La PEPCK resta espressa con il vecchio ritmo: c'è di giorno e manca di notte, e la glicemia notturna è meno regolata",
  "La gluconeogenesi si blocca", "La PEPCK raddoppia", "Non cambia nulla"], 0,
  "Il ritmo si riallinea in pochi giorni con il cortisolo.")
q("m5a-04", T, "a", "159", "Nel lobulo epatico, dove prevale la gluconeogenesi?", ["Negli epatociti periportali", "Negli epatociti perivenosi (centrolobulari)", "In modo uniforme", "Nelle cellule di Kupffer"], 0,
  "Periportale: gluconeogenesi, ossidazione degli acidi grassi, urea. Perivenoso: glicolisi, lipogenesi, sintesi di glutammina.")
q("m5a-05", T, "a", "153", "Topi con PEPCK espressa in modo costitutivo nel muscolo:", [
  "Correvano molto più a lungo, usavano più acidi grassi e producevano meno lattato",
  "Erano obesi e sedentari", "Avevano ipoglicemia grave", "Non mostravano differenze"], 0,
  "Mostravano anche più mitocondri e più sensibilità all'insulina, ma erano aggressivi.")
q("m5a-06", T, "l", "157", "Nella cascata del glucagone, quale enzima attiva la glicogeno fosforilasi?", ["Fosforilasi chinasi", "Protein chinasi A direttamente", "Adenilato ciclasi", "Glicogeno sintasi chinasi 3"], 0,
  "Glucagone → cAMP → PKA → fosforilasi chinasi → fosforilasi a.",
  note="Sbobina di Biochimica II, p. 156: c'è scritto che il cAMP «fosforila enzimi chiave come la PKA». Il cAMP attiva la PKA legandosi alle subunità regolatrici; a fosforilare è la PKA.")
