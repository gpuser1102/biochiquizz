"""Blocco 4 – Metabolismo del glicogeno (sbobina di Biochimica II, p. 115–139)."""
from bank_common import q

T = "m4-degradazione"
q("m4d-01", T, "f", "115", "Dove si trova soprattutto il glicogeno nell'organismo?", ["Fegato e muscolo scheletrico", "Cervello e rene", "Tessuto adiposo", "Eritrociti"], 0,
  "Il glicogeno epatico serve alla glicemia, quello muscolare al muscolo stesso.")
q("m4d-02", T, "f", "116", "Quale enzima stacca le unità di glucosio dal glicogeno?", ["Glicogeno fosforilasi", "Glicogeno sintasi", "Amilasi", "Esochinasi"], 0,
  "È una fosforolisi: il legame α-1,4 viene scisso dal fosfato inorganico.")
q("m4d-03", T, "f", "116", "Che prodotto libera la glicogeno fosforilasi?", ["Glucosio 1-fosfato", "Glucosio libero", "Glucosio 6-fosfato", "UDP-glucosio"], 0,
  "La fosforolisi conserva l'energia del legame sotto forma di estere fosforico.")
q("m4d-04", T, "m", "116", "Che vantaggio ha la fosforolisi rispetto all'idrolisi?", [
  "Il glucosio esce già fosforilato, senza spendere ATP, e non può uscire dalla cellula", "Produce più glucosio", "È più veloce", "Non richiede enzimi"], 0,
  "Nel muscolo si risparmia l'ATP dell'esochinasi.")
q("m4d-05", T, "m", "116", "Quale enzima trasforma il glucosio 1-fosfato in glucosio 6-fosfato?", ["Fosfoglucomutasi", "Fosfoglucoisomerasi", "Glucosio 6-fosfatasi", "Esochinasi"], 0,
  "Passa per il glucosio 1,6-bisfosfato.",
  note="Sbobina di Biochimica II, p. 116: l'enzima è chiamato «mutazione». Il nome corretto è fosfoglucomutasi.")
q("m4d-06", T, "m", "117", "Perché il muscolo non può rilasciare glucosio nel sangue?", ["Non ha la glucosio 6-fosfatasi", "Non ha la fosforilasi", "Non ha GLUT", "Non ha la fosfoglucomutasi"], 0,
  "Il glucosio 6-P del muscolo entra in glicolisi.")
q("m4d-07", T, "m", "117–118", "Che cosa fa l'enzima deramificante?", [
  "Sposta tre residui di un ramo su una catena vicina (transferasi) e idrolizza l'ultimo legato in α-1,6 come glucosio libero",
  "Forma i legami α-1,6", "Stacca glucosio 1-P dai rami", "Sintetizza la glicogenina"], 0,
  "La fosforilasi si ferma a 4 residui dal punto di ramificazione.")
q("m4d-08", T, "a", "117", "Dove si trova la glucosio 6-fosfatasi e quali organi la possiedono?", [
  "Nel lume del reticolo endoplasmatico; fegato e rene", "Nel citosol; solo fegato", "Nel mitocondrio; fegato e muscolo", "Nel lisosoma; tutti i tessuti"], 0,
  "Il G6P entra nel RE tramite un trasportatore (T1); il glucosio esce con GLUT.",
  note="Sbobina di Biochimica II, p. 117: la glucosio 6-fosfatasi è definita «esclusiva del fegato». È presente anche nel rene (e nell'intestino), come la stessa sbobina dice a p. 137.")
q("m4d-09", T, "a", "116", "Quale cofattore usa la glicogeno fosforilasi?", ["Piridossal fosfato", "Tiamina pirofosfato", "Biotina", "FAD"], 0,
  "Il PLP qui agisce col gruppo fosfato come catalizzatore acido-base, non con la base di Schiff.")
q("m4d-10", T, "a", "118", "Quale percentuale circa del glicogeno viene liberata come glucosio libero e non come glucosio 1-P?", ["Circa il 10%", "Circa il 50%", "Circa il 90%", "Nessuna"], 0,
  "Corrisponde ai residui legati in α-1,6 nei punti di ramificazione.")
q("m4d-11", T, "l", "118", "Quale legame idrolizza l'attività α-1,6-glucosidasi del deramificante?", ["Il legame α-1,6 del residuo rimasto al punto di ramificazione", "I legami α-1,4 terminali", "Il legame con la glicogenina", "Il legame β-1,4"], 0,
  "È un'unica proteina con due attività: transferasi e glucosidasi.")

T = "m4-sintesi"
q("m4s-01", T, "f", "122", "Qual è il donatore di glucosio nella sintesi del glicogeno?", ["UDP-glucosio", "Glucosio 1-fosfato", "ADP-glucosio", "Glucosio 6-fosfato"], 0,
  "Nelle piante il donatore per l'amido è l'ADP-glucosio.")
q("m4s-02", T, "f", "122", "Quale enzima allunga le catene del glicogeno con legami α-1,4?", ["Glicogeno sintasi", "Glicogeno fosforilasi", "Enzima ramificante", "UDP-glucosio pirofosforilasi"], 0,
  "Aggiunge glucosio all'estremità non riducente.")
q("m4s-03", T, "m", "122", "Perché la formazione di UDP-glucosio è irreversibile?", [
  "Il pirofosfato prodotto viene idrolizzato dalla pirofosfatasi inorganica", "Perché consuma GTP", "Perché è nel RE", "Perché l'UTP è un inibitore"], 0,
  "Un trucco comune nelle biosintesi: si sposta l'equilibrio eliminando un prodotto.")
q("m4s-04", T, "m", "123", "Che cosa fa la glicogenina?", [
  "Fa da innesco: si autoglicosila su una tirosina formando una corta catena di glucosio", "Ramifica il glicogeno", "Degrada il glicogeno", "Trasporta glucosio nel fegato"], 0,
  "La glicogeno sintasi non può partire da zero, ha bisogno di un primer.")
q("m4s-05", T, "m", "123", "Come lavora l'enzima ramificante?", [
  "Stacca un pezzo di circa 7 residui e lo attacca con legame α-1,6 più all'interno della catena", "Aggiunge un glucosio con legame α-1,6", "Idrolizza i legami α-1,6", "Forma legami β"], 0,
  "Le ramificazioni aumentano solubilità ed estremità non riducenti per sintesi e degradazione rapide.")
q("m4s-06", T, "a", "122", "Quanti legami fosfoanidridici costa aggiungere un glucosio al glicogeno partendo da glucosio 6-P?", ["Due (UTP → UDP + PPi, poi PPi → 2 Pi)", "Uno", "Tre", "Nessuno"], 0,
  "L'UDP poi viene rifosforilato a UTP spendendo un ATP.")
q("m4s-07", T, "a", "123", "A quale residuo della glicogenina si lega il primo glucosio?", ["Tirosina", "Serina", "Treonina", "Asparagina"], 0,
  "Il legame si forma con l'ossidrile fenolico della Tyr194.")
q("m4s-08", T, "l", "122", "Qual è il nome esatto dell'enzima che forma UDP-glucosio?", ["UDP-glucosio pirofosforilasi", "UDP-glucosio sintasi", "Glucosio 1-P uridiltransferasi chinasi", "Glicogeno sintasi"], 0,
  "Il nome viene dalla reazione inversa (pirofosforolisi).")
q("m4s-09", T, "l", "123", "Come si chiama il nome tecnico dell'enzima ramificante?", ["Amilo-(1,4→1,6)-transglicosilasi", "Amilo-1,6-glucosidasi", "Oligo-(1,4→1,4)-glucantransferasi", "α-amilasi"], 0,
  "Sposta un segmento da un legame 1,4 a un legame 1,6.")

T = "m4-regolazione"
q("m4r-01", T, "f", "124", "La glicogeno fosforilasi è più attiva quando è:", ["Fosforilata (forma a)", "Defosforilata (forma b)", "Legata a UDP-glucosio", "Legata all'insulina"], 0,
  "La fosforilasi chinasi la fosforila su una serina.")
q("m4r-02", T, "f", "126", "La glicogeno sintasi è più attiva quando è:", ["Defosforilata", "Fosforilata", "Legata al cAMP", "Legata all'AMP"], 0,
  "Fosforilazione e defosforilazione hanno effetti opposti su sintasi e fosforilasi.")
q("m4r-03", T, "m", "125", "Nel muscolo, quale regolatore allosterico attiva la fosforilasi b anche senza fosforilazione?", ["AMP", "ATP", "Glucosio 6-fosfato", "Glucosio"], 0,
  "AMP alto = poca energia. ATP e glucosio 6-P la inibiscono.")
q("m4r-04", T, "m", "125", "Nel fegato, quale molecola inattiva la fosforilasi a?", ["Glucosio", "AMP", "Ca²⁺", "cAMP"], 0,
  "Il glucosio la porta nello stato T ed espone le serine alla fosfatasi PP1: il fegato è un sensore della glicemia.")
q("m4r-05", T, "m", "126", "Come agisce l'insulina sulla glicogeno sintasi?", [
  "Attiva PKB, che fosforila e inattiva GSK3: la sintasi resta defosforilata e attiva", "Fosforila direttamente la sintasi", "Attiva la PKA", "Inibisce la PP1"], 0,
  "Inoltre attiva la PP1.",
  note="Sbobina di Biochimica II, p. 126: c'è scritto che la PKB fosforila GSK3 «attivandola» e che così «la glicogeno fosforilasi rimanga defosforilata». La PKB inattiva GSK3 e a restare defosforilata (attiva) è la glicogeno sintasi.")
q("m4r-06", T, "a", "124–125", "Quali stimoli attivano la fosforilasi chinasi?", [
  "Fosforilazione da PKA e Ca²⁺ legato alla subunità δ (calmodulina)", "Solo il glucosio", "L'insulina", "Il glucosio 6-fosfato"], 0,
  "Nel muscolo il Ca²⁺ della contrazione accoppia contrazione e glicogenolisi.")
q("m4r-07", T, "a", "126", "Perché il glucosio 6-fosfato attiva la glicogeno sintasi?", [
  "Rende la sintasi fosforilata (b) un buon substrato per la fosfatasi, e la attiva allostericamente", "Perché è il donatore di glucosio", "Perché inibisce l'insulina", "Perché attiva la PKA"], 0,
  "Se c'è tanto G6P conviene immagazzinarlo.")
q("m4r-08", T, "a", "127", "Che ruolo ha la PP1 legata al glicogeno?", [
  "Defosforila fosforilasi, fosforilasi chinasi e sintasi: spegne la degradazione e accende la sintesi", "Fosforila la sintasi", "Degrada il glicogeno", "Sintetizza cAMP"], 0,
  "La subunità GM la ancora al glicogeno; l'insulina ne favorisce l'attività.")
q("m4r-09", T, "l", "124", "Quale residuo viene fosforilato nella glicogeno fosforilasi?", ["Ser14", "Tyr194", "Ser641", "Thr172"], 0,
  "Una sola serina per subunità basta a passare da b ad a.")
q("m4r-10", T, "l", "126", "Che significa la sigla GSK3?", ["Glicogeno sintasi chinasi 3", "Glucosio sensore chinasi 3", "Glicogeno sintasi kinasi attivata da glucosio", "Guanosina sintasi chinasi"], 0,
  "Fosforila la sintasi in tre serine dopo un innesco dato dalla CKII (caseina chinasi II).")

T = "m4-ormoni"
q("m4o-01", T, "f", "129", "Quale ormone stimola la degradazione del glicogeno nel fegato a digiuno?", ["Glucagone", "Insulina", "Leptina", "Ossitocina"], 0,
  "Il glucagone agisce sul fegato, non sul muscolo.")
q("m4o-02", T, "m", "129–130", "Quale secondo messaggero media l'effetto del glucagone e dell'adrenalina (via β)?", ["cAMP", "cGMP", "IP₃", "NO"], 0,
  "Il cAMP attiva la PKA, che fosforila la fosforilasi chinasi.")
q("m4o-03", T, "m", "130", "Perché il glucagone non agisce sul muscolo?", ["Il muscolo non ha recettori per il glucagone", "Il muscolo non ha cAMP", "Il muscolo non ha glicogeno", "Il glucagone è degradato nel sangue"], 0,
  "Il muscolo risponde invece all'adrenalina.")
q("m4o-04", T, "a", "131", "Come agisce l'adrenalina sui recettori α1 epatici?", ["Via IP₃ e Ca²⁺, attivando la fosforilasi chinasi", "Via cAMP", "Via tirosin-chinasi", "Inibendo la PKA"], 0,
  "Ca²⁺ si lega alla calmodulina della fosforilasi chinasi.")
q("m4o-05", T, "a", "131", "Nel fegato, che effetto ha il glucagone sulla glicogeno sintasi?", [
  "Aumenta il cAMP; la PKA fosforila e inattiva la sintasi, mentre attiva la degradazione", "La attiva tramite PKB", "Non ha effetto sulla sintasi", "La defosforila tramite PP1"], 0,
  "Sintesi e degradazione sono regolate in modo reciproco: non girano mai insieme a pieno regime.",
  note="Sbobina di Biochimica II, p. 131: c'è scritto che il glucagone aumenta «i livelli di AMP» dove si intende cAMP, e si parla di inibizione «della distruzione del glicogeno» dove si intende la sintesi.")
q("m4o-06", T, "l", "132", "Che cosa sono PKB e Akt?", ["Due nomi della stessa chinasi attivata dall'insulina", "Una proteasi e una chinasi", "Due fosfatasi", "Recettori dell'insulina"], 0,
  "La PKB/Akt è una serina/treonina chinasi.",
  note="Sbobina di Biochimica II, p. 132: la PKB è chiamata «proteasi». È una chinasi.")

T = "m4-attivita"
q("m4e-01", T, "f", "134", "Durante uno sprint, da dove ricava energia il muscolo?", ["Dal glicogeno muscolare via glicolisi anaerobia", "Dagli acidi grassi", "Dai corpi chetonici", "Dalle proteine"], 0,
  "Lo sforzo intenso e breve usa la fermentazione lattica.")
q("m4e-02", T, "m", "134–135", "Nella maratona, che cosa cambia rispetto allo sprint?", [
  "Il metabolismo è aerobio e usa sempre più acidi grassi, risparmiando glicogeno", "Usa solo glicogeno", "Usa solo creatina fosfato", "Produce più lattato"], 0,
  "Quando il glicogeno si esaurisce si ha il «muro».")
q("m4e-03", T, "a", "135", "Quale enzima rallenta l'uso del glucosio quando il muscolo usa acidi grassi?", ["La piruvato deidrogenasi, inibita da acetil-CoA e NADH", "La piruvato carbossilasi", "La glicogeno sintasi", "La lattato deidrogenasi"], 0,
  "È uno dei meccanismi del ciclo di Randle.",
  note="Sbobina di Biochimica II, p. 135: c'è scritto che la «piruvato carbossilasi» è irreversibile e inibita. Dal contesto si tratta della piruvato deidrogenasi.")
q("m4e-04", T, "l", "134", "Quanto dura indicativamente la riserva di fosfocreatina in uno sforzo massimale?", ["Pochi secondi", "Circa 10 minuti", "Circa un'ora", "Un giorno"], 0,
  "Dopo pochi secondi subentra la glicolisi anaerobia.")

T = "m4-glicogenosi"
q("m4g-01", T, "f", "136", "Che cosa sono le glicogenosi?", ["Malattie da difetti enzimatici del metabolismo del glicogeno", "Infezioni del fegato", "Forme di diabete", "Malattie del glucagone"], 0,
  "Sono malattie ereditarie, quasi tutte autosomiche recessive.")
q("m4g-02", T, "m", "137", "Quale enzima manca nella malattia di von Gierke (tipo I)?", ["Glucosio 6-fosfatasi", "Fosforilasi muscolare", "Enzima deramificante", "α-glucosidasi lisosomiale"], 0,
  "Ipoglicemia grave a digiuno, epatomegalia, acidosi lattica.")
q("m4g-03", T, "m", "138", "Quale enzima manca nella malattia di McArdle (tipo V)?", ["Glicogeno fosforilasi muscolare", "Glucosio 6-fosfatasi", "Enzima ramificante", "Fosfofruttochinasi epatica"], 0,
  "Crampi e intolleranza all'esercizio; la glicemia è normale.")
q("m4g-04", T, "a", "137", "Perché nella von Gierke si dà amido di mais crudo?", [
  "Viene digerito lentamente e libera glucosio in modo graduale, evitando l'ipoglicemia notturna", "Perché contiene fruttosio", "Perché blocca la glicolisi", "Perché fornisce glucosio 6-fosfatasi"], 0,
  "Si danno anche pasti frequenti.",
  note="Sbobina di Biochimica II, p. 137: c'è scritto che l'amido crudo rilascia glucosio in modo massiccio. Il senso è l'opposto: lo rilascia lentamente e a lungo.")
q("m4g-05", T, "a", "137", "Perché nella von Gierke c'è iperuricemia e iperlipidemia?", [
  "Il glucosio 6-P accumulato va in glicolisi e nella via dei pentoso fosfati: più lattato, acetil-CoA (grassi) e ribosio 5-P (purine → acido urico)",
  "Perché manca l'insulina", "Perché il rene non filtra", "Perché c'è troppo glucagone"], 0,
  "Anche il lattato compete con l'urato per l'escrezione renale.")
q("m4g-06", T, "a", "138", "Nella McArdle, che cosa succede al lattato durante lo sforzo?", ["Non aumenta, perché il muscolo non può usare il glicogeno", "Aumenta molto", "Diventa glucosio", "Si accumula nel fegato"], 0,
  "È alla base del test da sforzo ischemico dell'avambraccio.")
q("m4g-07", T, "l", "138", "Che cos'è la mioglobinuria che si vede nella McArdle?", ["Presenza di mioglobina nelle urine dopo danno muscolare", "Mioglobina nel sangue", "Carenza di mioglobina", "Mioglobina nel fegato"], 0,
  "Le urine diventano scure dopo sforzi intensi.",
  note="Sbobina di Biochimica II, p. 138: la mioglobinuria è definita «presenza di mioglobina nel sangue». È la presenza di mioglobina nelle urine (la mioglobina nel sangue è la mioglobinemia).")
q("m4g-08", T, "l", "136", "Come si chiama la glicogenosi di tipo II e quale enzima manca?", ["Malattia di Pompe, α-glucosidasi acida lisosomiale", "Malattia di Cori, deramificante", "Malattia di Andersen, ramificante", "Malattia di Hers, fosforilasi epatica"], 0,
  "È anche una malattia da accumulo lisosomiale.")
