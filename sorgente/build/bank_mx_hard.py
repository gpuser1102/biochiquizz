"""Domande Alta e 30 e lode in più per gli argomenti con pochi quesiti difficili (hard mode)."""
from bank_common import q

T = "m1-catabolismo"
q("x1c-01", T, "a", "6–7", "Dopo un pasto, a che cosa servono soprattutto il NADPH e l'ATP prodotti dal catabolismo?", [
  "A sostenere le biosintesi riduttive (anabolismo), che consumano ATP e potere riducente", "A produrre altro glucosio", "A essere eliminati con le urine", "A ridurre l'ossigeno nel citosol"], 0,
  "Catabolismo ossidativo e anabolismo riduttivo sono accoppiati da ATP e coenzimi ridotti.",
  note="Sbobina di Biochimica II, p. 6: c'è scritto che per potere riducente delle biosintesi si intende «soprattutto NADH». Il coenzima delle biosintesi riduttive è il NADPH; il NADH serve soprattutto al catabolismo (lo dice la stessa sbobina a p. 159).")
q("x1c-02", T, "a", "6", "Perché vitamine e sali minerali sono indispensabili pur non fornendo energia?", [
  "Perché da molte vitamine derivano i coenzimi (es. NAD, FAD) delle reazioni di ossidoriduzione", "Perché vengono ossidati nel ciclo di Krebs", "Perché formano ATP direttamente", "Perché sono metaboliti terminali"], 0,
  "Sono micronutrienti: servono in piccole quantità come cofattori.")
q("x1c-03", T, "l", "6", "Come viene eliminato l'azoto in eccesso degli amminoacidi, secondo lo schema del catabolismo?", [
  "L'ammoniaca viene trasformata in urea nel fegato e poi eliminata con le urine", "Viene espirata come NH₃", "Viene eliminata come acido urico", "Viene immagazzinata nel muscolo"], 0,
  "CO₂ con la respirazione, H₂O nel bilancio idrico, NH₃ come urea.")
q("x1c-04", T, "l", "7", "In una cellula che si prepara alla mitosi, quali precursori servono per le nuove membrane?", [
  "Acidi grassi, glicerolo e i composti delle teste polari dei fosfolipidi", "Solo colesterolo", "Amminoacidi e basi azotate", "Glicogeno"], 0,
  "È l'esempio della sbobina: per duplicare la cellula servono DNA nuovo e fosfolipidi nuovi.")

T = "m1-termodinamica"
q("x1t-01", T, "a", "11–12", "Una reazione ha ΔG°' = −20 kJ/mol ma nella cellula ha ΔG ≈ 0. Che cosa significa?", [
  "Le concentrazioni reali sono vicine a quelle di equilibrio: la reazione è reversibile e non è un buon punto di regolazione",
  "Che la reazione è irreversibile", "Che l'enzima manca", "Che il ΔG°' è sbagliato"], 0,
  "Conta il ΔG reale, che dipende dal rapporto [prodotti]/[reagenti].")
q("x1t-02", T, "a", "11", "Se il ΔG°' di una reazione è 0, quanto vale la Keq?", ["1", "0", "10", "Infinito"], 0,
  "ΔG°' = −RT ln Keq: ln 1 = 0.")
q("x1t-03", T, "a", "12", "Perché due reazioni consecutive possono procedere anche se la prima ha ΔG°' positivo?", [
  "Perché i ΔG°' di reazioni accoppiate si sommano: conta il ΔG complessivo", "Perché l'enzima cambia il ΔG", "Perché la temperatura aumenta", "Non possono"], 0,
  "È il principio dell'accoppiamento energetico (es. aldolasi seguita dalle reazioni a valle).")
q("x1t-04", T, "l", "11", "Qual è la relazione tra ΔG e la concentrazione dei reagenti e dei prodotti?", [
  "ΔG = ΔG°' + RT ln([prodotti]/[reagenti])", "ΔG = ΔG°' − RT ln([prodotti]/[reagenti])", "ΔG = −nFΔE + RT", "ΔG = ΔH + TΔS"], 0,
  "Con il rapporto pari a Keq, ΔG = 0 (equilibrio).")

T = "m1-enzimologia"
q("x1e-01", T, "a", "27", "Un inibitore competitivo come modifica KM e Vmax?", ["Aumenta la KM apparente, Vmax invariata", "Diminuisce la Vmax, KM invariata", "Diminuisce entrambe", "Aumenta entrambe"], 0,
  "Aumentando il substrato si supera l'inibizione.")
q("x1e-02", T, "a", "29–30", "Qual è la differenza tra regolazione allosterica e controllo della quantità di enzima?", [
  "L'allosterica è rapida (secondi); la sintesi o degradazione dell'enzima è lenta (ore)", "Sono ugualmente rapide", "L'allosterica è lenta", "La quantità di enzima non è regolabile"], 0,
  "La modificazione covalente (fosforilazione) sta in mezzo: minuti.")

T = "m2-fosforilazione"
q("x2f-01", T, "a", "37–38", "Perché il glucosio 6-fosfato inibisce l'esochinasi ma non la glucochinasi?", [
  "Il fegato deve continuare a fosforilare il glucosio dopo il pasto per immagazzinarlo, anche quando il G6P è alto",
  "Perché la glucochinasi non lega il glucosio", "Perché il G6P non entra nel fegato", "Perché la glucochinasi è mitocondriale"], 0,
  "La glucochinasi è invece regolata dalla proteina regolatrice, che la sequestra nel nucleo.")
q("x2f-02", T, "l", "55–56", "Dove porta la glucochinasi la sua proteina regolatrice (GKRP) in presenza di fruttosio 6-fosfato?", [
  "Nel nucleo, dove resta inattiva", "Nel mitocondrio", "Sulla membrana plasmatica", "Nel reticolo endoplasmatico"], 0,
  "Il glucosio alto la libera e la fa tornare nel citosol.")

T = "m2-navette"
q("x2n-01", T, "a", "53–54", "Perché il NADH prodotto nel citosol dalla glicolisi non entra direttamente nel mitocondrio?", [
  "La membrana mitocondriale interna è impermeabile al NADH: entrano solo i suoi elettroni, tramite le navette", "Perché viene distrutto", "Perché si ossida da solo", "Entra liberamente"], 0,
  "Gli elettroni passano tramite molecole trasportatrici (glicerolo 3-P, malato).")
q("x2n-02", T, "a", "54", "Nella navetta malato-aspartato, quale molecola attraversa la membrana interna portando gli elettroni?", ["Il malato", "L'ossalacetato", "Il NADH", "Il glicerolo 3-fosfato"], 0,
  "L'ossalacetato non attraversa la membrana: torna fuori come aspartato dopo una transaminazione. Il dettaglio della navetta malato-aspartato non è nelle sbobine.")
q("x2n-03", T, "l", "54", "Quale abbreviazione è corretta per il glicerolo 3-fosfato della navetta?", ["Gro3P (o G3P)", "3-PG", "GAP", "DHAP"], 0,
  "3-PG è la sigla del 3-fosfoglicerato, un intermedio diverso della glicolisi.",
  note="Sbobina di Biochimica II, p. 54: il glicerolo 3-fosfato è abbreviato «3-PG», che è la sigla del 3-fosfoglicerato. Attenzione a non confonderli.")
q("x2n-04", T, "l", "54", "Dove si trova la glicerolo 3-fosfato deidrogenasi mitocondriale?", [
  "Sulla faccia esterna della membrana mitocondriale interna, e cede gli elettroni al coenzima Q tramite FAD", "Nella matrice", "Nel citosol", "Nella membrana esterna"], 0,
  "Per questo il glicerolo 3-P non deve entrare nella matrice.")

T = "m3-radicali"
q("x3r-01", T, "a", "109", "Come viene rigenerato il glutatione ridotto dopo l'azione della glutatione perossidasi?", [
  "Dalla glutatione reduttasi, che usa NADPH", "Dalla catalasi", "Dalla superossido dismutasi", "Dal NADH della catena respiratoria"], 0,
  "Per questo la via dei pentoso fosfati è fondamentale contro lo stress ossidativo.")
q("x3r-02", T, "a", "110", "Che cosa fa il fattore HIF nelle cellule tumorali ipossiche?", [
  "Aumenta gli enzimi glicolitici, la LDH e la PDH chinasi (che blocca la PDH), e sostituisce COX4-1 con COX4-2",
  "Aumenta la β-ossidazione", "Inibisce la glicolisi", "Attiva la piruvato deidrogenasi"], 0,
  "Spinge la cellula verso la glicolisi e riduce la produzione di radicali.")
q("x3r-03", T, "l", "109", "Perché la glutatione perossidasi ha la selenocisteina invece della cisteina?", [
  "Il selenolato (Se⁻) è più facilmente ionizzato e più reattivo verso i perossidi del tiolato", "Perché il selenio lega l'ossigeno", "Perché è più stabile", "Perché trasporta elettroni"], 0,
  "Il selenio sta nello stesso gruppo di O e S e cede più facilmente l'H⁺.")
q("x3r-04", T, "l", "108", "Quali vitamine sono classicamente considerate antiossidanti?", ["C, E e il β-carotene (provitamina A)", "K e B12", "B1 e B2", "D e K"], 0,
  "La vitamina E protegge le membrane, la C agisce in ambiente acquoso.",
  note="Sbobina di Biochimica II, p. 108: tra le vitamine antiossidanti è inclusa anche la K. Le antiossidanti classiche sono C, E e A/β-carotene; la K serve alla coagulazione.")

T = "m3-malattie"
q("x3m-01", T, "a", "112", "Nella cellula β, qual è la sequenza che porta alla secrezione di insulina?", [
  "Glucosio (GLUT2) → glicolisi e Krebs → ATP ↑ → chiusura canali K⁺ → depolarizzazione → ingresso di Ca²⁺ → esocitosi",
  "Glucosio → cAMP → PKA → esocitosi", "Glucosio → apertura canali K⁺ → iperpolarizzazione", "Insulina → GLUT4 → ATP"], 0,
  "Se l'ATP cala (es. per UCP2), la secrezione si riduce.")
q("x3m-02", T, "a", "112", "Perché la gravità delle malattie mitocondriali varia tra i figli della stessa madre?", [
  "Per l'eteroplasmia: ogni figlio riceve una quota diversa di mitocondri mutati", "Perché il padre trasmette mitocondri sani", "Per mutazioni nucleari diverse", "Perché il mtDNA si ricombina"], 0,
  "Sotto una soglia di mitocondri mutati i sintomi possono mancare.")
q("x3m-03", T, "l", "113", "Il DNA mitocondriale è più esposto al danno ossidativo del DNA nucleare. Perché?", [
  "È vicino alla catena respiratoria (fonte di radicali), non ha istoni e i suoi sistemi di riparazione sono limitati", "Perché è lineare", "Perché è più lungo", "Perché ha gli istoni"], 0,
  "Questa è la base dell'ipotesi mitocondriale dell'invecchiamento.",
  note="Sbobina di Biochimica II, p. 113: c'è scritto che il DNA mitocondriale «non può ripararsi». È una semplificazione: ha meccanismi di riparazione, ma più limitati di quelli nucleari.")

T = "m4-degradazione"
q("x4d-01", T, "a", "116–117", "La glicogeno fosforilasi lavora finché trova un punto di ramificazione. A quanti residui si ferma?", ["A 4 residui dal punto di ramificazione", "A 1 residuo", "A 10 residui", "Non si ferma"], 0,
  "Resta una «destrina limite» che va sistemata dall'enzima deramificante.")
q("x4d-02", T, "l", "116", "Perché la fosforolisi del glicogeno nel muscolo rende più ATP per glucosio rispetto al glucosio del sangue?", [
  "Il glucosio 1-P diventa G6P senza consumare l'ATP dell'esochinasi: 3 ATP netti in glicolisi anaerobia invece di 2", "Perché produce più NADH", "Perché salta la fosfofruttochinasi", "Non è vero"], 0,
  "È un vantaggio della fosforolisi rispetto all'idrolisi.")
q("x4d-03", T, "l", "115", "Che tipo di legami ha il glicogeno nelle catene e nelle ramificazioni?", ["α-1,4 nelle catene e α-1,6 nelle ramificazioni", "β-1,4 e α-1,6", "α-1,4 e β-1,6", "Solo α-1,4"], 0,
  "Un'unica estremità riducente (legata alla glicogenina) e tante estremità non riducenti.")

T = "m4-sintesi"
q("x4s-01", T, "a", "122–123", "Perché la sintesi e la degradazione del glicogeno usano enzimi diversi?", [
  "Così le due vie sono regolate separatamente e in modo reciproco, evitando un ciclo futile", "Perché la fosforilasi non è reversibile in vitro", "Perché avvengono in organelli diversi", "Per caso"], 0,
  "Lo stesso principio vale per glicolisi e gluconeogenesi.")
q("x4s-02", T, "l", "122", "Su quale estremità del glicogeno lavora la glicogeno sintasi?", ["Sulle estremità non riducenti", "Sull'estremità riducente", "Sui punti di ramificazione", "Sulla glicogenina"], 0,
  "Anche la fosforilasi lavora sulle estremità non riducenti: più rami = più velocità.")
q("x4s-03", T, "l", "122", "Quale nucleotide viene rigenerato dall'UDP con un ATP dopo la sintesi del glicogeno?", ["UTP, dalla nucleoside difosfato chinasi", "GTP, dalla succinil-CoA sintetasi", "CTP, dalla CTP sintetasi", "ATP, dall'adenilato chinasi"], 0,
  "UDP + ATP → UTP + ADP. Il nome dell'enzima non è nelle sbobine.")

T = "m4-ormoni"
q("x4o-01", T, "a", "129–131", "Perché la cascata del glucagone amplifica il segnale?", [
  "Ogni enzima attivato (adenilato ciclasi, PKA, fosforilasi chinasi) attiva molte molecole del passaggio successivo", "Perché il glucagone è molto concentrato", "Perché il glucagone entra nella cellula", "Perché agisce sul DNA"], 0,
  "Poche molecole di ormone liberano moltissimo glucosio.")
q("x4o-02", T, "a", "132", "Come porta l'insulina allo stoccaggio di glicogeno nel muscolo?", [
  "Aumenta GLUT4 in membrana e, tramite PKB, inattiva GSK3 lasciando attiva la glicogeno sintasi", "Attiva la fosforilasi", "Aumenta il cAMP", "Inibisce l'esochinasi"], 0,
  "Attiva anche la PP1.")
q("x4o-03", T, "l", "129–130", "Quale proteina G accoppia il recettore del glucagone all'adenilato ciclasi?", ["Gs", "Gi", "Gq", "Gt (transducina)"], 0,
  "I recettori α1 dell'adrenalina usano Gq (fosfolipasi C, IP₃, Ca²⁺).")

T = "m4-attivita"
q("x4e-01", T, "a", "135", "Che cos'è la supercompensazione del glicogeno?", [
  "Dopo averlo esaurito con lo sforzo, una dieta ricca di carboidrati lo riporta in circa due giorni a livelli superiori a quelli iniziali",
  "Il fegato produce glicogeno dai grassi", "Il glicogeno resta sempre alto", "È una malattia da accumulo"], 0,
  "A digiuno o con una dieta povera di carboidrati il glicogeno non si ricostituisce.")
q("x4e-02", T, "a", "134", "In uno sforzo leggero e prolungato, quanto glicogeno muscolare si consuma?", ["Poco: il muscolo usa soprattutto acidi grassi e glucosio del sangue", "Tutto in pochi minuti", "Solo quello epatico", "Nessuna energia viene da fonti esterne"], 0,
  "Sforzo moderato e soprattutto intenso consumano invece molto glicogeno.")
q("x4e-03", T, "l", "135", "Quando conviene assumere carboidrati per recuperare dopo lo sforzo?", [
  "Subito dopo lo sforzo e poi a intervalli regolari nelle 24 ore successive", "Solo il giorno dopo", "Solo prima dello sforzo", "Mai, bastano le proteine"], 0,
  "Subito dopo l'esercizio la sintesi del glicogeno muscolare è più rapida.")
q("x4e-04", T, "l", "133", "Il grafico delle fonti di energia nello sforzo mostra la quota di metabolismo aerobio e anaerobio. Come si chiamano correttamente?", [
  "Metabolismo aerobio e anaerobio (catabolismo)", "Anabolismo aerobio e anaerobio", "Gluconeogenesi aerobia", "Glicogenosintesi"], 0,
  "Sono vie che producono energia: catabolismo.",
  note="Sbobina di Biochimica II, p. 133: le curve sono chiamate «anabolismo aerobio» e «anabolismo anaerobio». Sono vie cataboliche: metabolismo (o catabolismo) aerobio e anaerobio.")

T = "m4-glicogenosi"
q("x4g-01", T, "a", "137", "Nella von Gierke, perché il glucagone non alza la glicemia?", [
  "La glicogenolisi epatica produce glucosio 6-P, che senza glucosio 6-fosfatasi non diventa glucosio libero", "Perché manca il recettore", "Perché il fegato non ha glicogeno", "Perché il glucagone non viene prodotto"], 0,
  "Anzi: il G6P accumulato alimenta lattato, lipidi e acido urico.")

T = "m5-fonti"
q("x5f-01", T, "a", "140", "Circa quanto glucosio consuma l'organismo al giorno e quanto ne usa il cervello?", ["Circa 160 g, di cui circa il 70% dal cervello", "Circa 50 g, tutto dal muscolo", "Circa 500 g, metà dal fegato", "Circa 20 g"], 0,
  "Il glicogeno epatico non basta per più di circa un giorno: serve la gluconeogenesi.")
q("x5f-02", T, "a", "141", "Tra mezzanotte e colazione, come cambiano glicogenolisi e gluconeogenesi?", [
  "La gluconeogenesi aumenta, la glicogenolisi diminuisce man mano che il glicogeno si esaurisce", "Entrambe si azzerano", "Aumenta solo la glicogenolisi", "Si attiva la glicogeno sintesi"], 0,
  "Dopo i pasti la gluconeogenesi si azzera e riparte la glicogeno sintesi.")
q("x5f-03", T, "l", "142", "Come agisce il cortisolo sulla gluconeogenesi?", [
  "È uno steroide: lega un recettore intracellulare che dimerizza, entra nel nucleo e aumenta la trascrizione degli enzimi (es. PEPCK)",
  "Attiva l'adenilato ciclasi", "Fosforila la PFK2", "Inibisce l'insulina nel sangue"], 0,
  "Sul muscolo ha effetto catabolico: libera amminoacidi come substrati.",
  note="Sbobina di Biochimica II, p. 142: il cortisolo è definito «ormone anabolizzante». Stimola la sintesi di enzimi epatici, ma a livello dell'organismo è catabolico (degrada le proteine muscolari, come dice la sbobina a p. 157).")
q("x5f-04", T, "l", "140", "Quale percentuale della gluconeogenesi avviene nel rene secondo la sbobina?", ["Circa il 10%", "Circa il 50%", "Circa il 90%", "Nessuna"], 0,
  "Il resto (circa 90%) avviene nel fegato. Nel digiuno prolungato la quota renale aumenta (questo non è nelle sbobine).")

T = "m5-glicerolo"
q("x5g-01", T, "a", "141, 147", "Quali due enzimi portano il glicerolo a diidrossiacetone fosfato?", [
  "Glicerolo chinasi e glicerolo 3-fosfato deidrogenasi", "Esochinasi e aldolasi", "Trioso fosfato isomerasi e PEPCK", "Glicerolo fosfatasi e aldolasi"], 0,
  "Il DHAP entra poi nella gluconeogenesi a livello dei triosi.")
q("x5g-02", T, "a", "147", "Da quale tappa della gluconeogenesi entra il glicerolo?", ["Dai triosi fosfati (DHAP), saltando le reazioni del piruvato e del PEP", "Dal piruvato", "Dall'ossalacetato", "Dal glucosio 6-P"], 0,
  "Non servono piruvato carbossilasi e PEPCK.")
q("x5g-03", T, "l", "147", "Il propionil-CoA (dagli acidi grassi a numero dispari di carboni) è glucogenico perché:", [
  "Diventa succinil-CoA e quindi ossalacetato", "Diventa acetil-CoA", "Diventa glicerolo", "Diventa lattato"], 0,
  "Gli acidi grassi a numero pari invece non danno glucosio. Il passaggio per il succinil-CoA non è nella sbobina in questo punto.")
q("x5g-04", T, "l", "148", "Perché il lattato si forma nel muscolo e diventa glucosio nel fegato?", [
  "Nel muscolo sotto sforzo NAD⁺/NADH è basso (lattato); nel fegato è alto, e la LDH lo riossida a piruvato", "Perché il fegato non ha LDH", "Perché il muscolo ha la G6Pasi", "Perché il lattato non entra nel muscolo"], 0,
  "È il ciclo di Cori. Il cuore usa invece il lattato come combustibile (LDH1).")

T = "m5-approfondimenti"
q("x5a-01", T, "a", "157", "Perché nel digiuno prolungato i corpi chetonici «salvano» le proteine muscolari?", [
  "Il cervello li usa come combustibile, quindi serve meno glucosio dalla gluconeogenesi (che usa amminoacidi muscolari)",
  "Perché si trasformano in glucosio", "Perché inibiscono la proteolisi direttamente", "Perché attivano la sintesi proteica"], 0,
  "Per questo dopo alcuni giorni la gluconeogenesi si dimezza.")
q("x5a-02", T, "a", "158", "L'alcol inibisce la gluconeogenesi. Quali due reazioni vengono bloccate dall'aumento di NADH?", [
  "Lattato → piruvato (LDH) e malato → ossalacetato (malato DH citosolica)", "PEP → piruvato e G6P → glucosio", "Piruvato → acetil-CoA e citrato → isocitrato", "Glicerolo → DHAP e F6P → F1,6BP"], 0,
  "Entrambe richiedono NAD⁺.")
q("x5a-03", T, "l", "153", "I topi con PEPCK sovraespressa nel muscolo, oltre a correre di più, avevano:", [
  "Più mitocondri, più uso di acidi grassi, meno lattato e maggiore sensibilità all'insulina (ma erano aggressivi)",
  "Più lattato e più tessuto adiposo", "Meno mitocondri", "Diabete"], 0,
  "La sbobina la cita per mostrare che un solo enzima può cambiare tutto il metabolismo.")
q("x5a-04", T, "l", "159", "Che cosa succede alla zonazione del lobulo epatico in caso di danno?", [
  "È un gradiente plastico: gli epatociti di una zona possono assumere le funzioni di un'altra", "È fissa e non cambia", "Il lobulo smette di fare gluconeogenesi", "Gli epatociti perivenosi muoiono"], 0,
  "Non è una divisione netta ma un gradiente tra vena porta e vena centrale.")

T = "m6-regolazione"
q("x6g-01", T, "a", "165", "Se la cellula sintetizza acidi grassi, che cosa succede alla via dei pentoso fosfati?", [
  "Accelera: la sintesi consuma NADPH, sale il NADP⁺ e la G6PD si attiva", "Si blocca", "Non cambia", "Diventa gluconeogenesi"], 0,
  "Se il NADPH non viene consumato si accumula e blocca la G6PD.")
q("x6g-02", T, "a", "165", "In una cellula in divisione che ha bisogno sia di ribosio sia di NADPH, quale modalità prevale?", [
  "Fase ossidativa completa: il ribulosio 5-P diventa ribosio 5-P, producendo 2 NADPH per glucosio 6-P", "Solo la fase non ossidativa", "Solo la glicolisi", "Il riciclo completo a CO₂"], 0,
  "Le altre modalità servono quando prevale il bisogno di uno solo dei due prodotti.")
q("x6g-03", T, "l", "165", "Quale enzima, oltre alla G6PD, produce NADPH nel citosol per la sintesi degli acidi grassi?", ["L'enzima malico", "La lattato deidrogenasi", "La gliceraldeide 3-P deidrogenasi", "La piruvato carbossilasi"], 0,
  "Malato + NADP⁺ → piruvato + CO₂ + NADPH. Anche l'isocitrato deidrogenasi citosolica usa NADP⁺. L'enzima malico non è in questa parte della sbobina.")
q("x6g-04", T, "l", "159", "Che cosa distingue strutturalmente il NADPH dal NADH?", [
  "Un fosfato sul 2' del ribosio dell'adenosina", "Un fosfato sul 5' del nicotinammide", "Un anello in più", "Lo zolfo"], 0,
  "Il fosfato fa sì che gli enzimi distinguano nettamente i due coenzimi.")
