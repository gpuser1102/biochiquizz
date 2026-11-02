"""Blocco 1 – Ripasso di propedeutica e Biochimica I (sbobina di Biochimica II, p. 5–30)."""
from bank_common import q

T = "m1-catabolismo"
q("m1c-01", T, "f", "5", "Il catabolismo è:", [
  "La degradazione di molecole complesse in molecole più semplici, con produzione di energia",
  "La sintesi di molecole complesse a partire da molecole semplici",
  "L'insieme delle reazioni che consumano ATP",
  "L'eliminazione dei metaboliti terminali con le urine"], 0,
  "Il catabolismo degrada nutrienti e componenti cellulari ricavando energia (ATP) e potere riducente; l'anabolismo fa il contrario.")
q("m1c-02", T, "f", "6–9", "Quali sono i metaboliti terminali del catabolismo?", [
  "Piruvato e acetil-CoA", "CO₂, H₂O e NH₃ (eliminata come urea)", "Glucosio e acidi grassi", "ATP e NADH"], 1,
  "I metaboliti terminali non rientrano nel metabolismo: CO₂ si elimina con la respirazione, H₂O si unisce all'acqua corporea, NH₃ diventa urea.")
q("m1c-03", T, "f", "8–9", "Verso quali intermedi comuni convergono le vie cataboliche di carboidrati, lipidi e proteine?", [
  "Glucosio e glicerolo", "Piruvato e acetil-CoA", "Urea e CO₂", "Ossalacetato e citrato"], 1,
  "Piruvato e acetil-CoA sono i metaboliti intermedi in cui convergono le vie cataboliche.")
q("m1c-04", T, "m", "9", "Che cosa distingue un metabolita intermedio da uno terminale?", [
  "Il metabolita intermedio può essere sia ossidato per dare energia sia usato per biosintesi",
  "Il metabolita intermedio è sempre più ossidato di quello terminale",
  "Il metabolita terminale entra nel ciclo di Krebs",
  "Il metabolita intermedio viene eliminato con le urine"], 0,
  "L'acetil-CoA, ad esempio, può entrare nel ciclo di Krebs oppure diventare acidi grassi e colesterolo: la cellula decide in base alle sue necessità.")
q("m1c-05", T, "m", "6–7", "Perché l'anabolismo ha bisogno di potere riducente?", [
  "Perché le biosintesi sono in gran parte processi riduttivi",
  "Perché l'anabolismo produce NADH",
  "Perché il potere riducente sostituisce l'ATP",
  "Perché tutte le biosintesi avvengono nel mitocondrio"], 0,
  "Il catabolismo è ossidativo e produce coenzimi ridotti; l'anabolismo è riduttivo e li consuma. Per le biosintesi il coenzima è soprattutto il NADPH.",
  note="Sbobina di Biochimica II, p. 6–7: c'è scritto che il potere riducente per le biosintesi è «soprattutto NADH». Per le biosintesi riduttive (acidi grassi, colesterolo) il coenzima è il NADPH; il NADH serve soprattutto alla fosforilazione ossidativa.")
q("m1c-06", T, "a", "8", "Nella sequenza glicolisi → ciclo di Krebs → fosforilazione ossidativa, dove si forma la maggior parte dell'ATP e perché?", [
  "Nella glicolisi, perché è la via più veloce",
  "Nel ciclo di Krebs, perché ossida completamente l'acetil-CoA",
  "Nella fosforilazione ossidativa, perché riossida i coenzimi ridotti cedendo gli elettroni all'O₂",
  "In tutte e tre in quantità simile"], 2,
  "Glicolisi e Krebs producono poco ATP ma molti coenzimi ridotti; la riossidazione di NADH e FADH₂ con l'ossigeno nella fosforilazione ossidativa produce la gran parte dell'ATP.")
q("m1c-07", T, "a", "7", "L'acetil-CoA è precursore di tutte le seguenti molecole tranne:", [
  "Acidi grassi", "Colesterolo", "Ormoni steroidei", "Glucosio (nell'uomo)"], 3,
  "Nell'uomo l'acetil-CoA non può diventare glucosio: la piruvato deidrogenasi è irreversibile e nel ciclo di Krebs i due carboni dell'acetile escono come CO₂.",
  note="Il fatto che l'acetil-CoA non dia glucosio non è detto esplicitamente in questa parte della sbobina.")
q("m1c-08", T, "l", "6", "Come si chiama la forma ossidata del nicotinammide adenin dinucleotide fosfato?", [
  "NADP⁺", "NADPH", "NAD⁺", "FADP"], 0,
  "NADP⁺ è la forma ossidata, NADPH quella ridotta. Si distingue dal NAD⁺ per un fosfato sul 2' del ribosio legato all'adenina.")

T = "m1-termodinamica"
q("m1t-01", T, "f", "10", "Che cosa dice la termodinamica di una reazione?", [
  "Se può avvenire spontaneamente", "Quanto velocemente avviene", "Quale enzima la catalizza", "Quanta attivazione serve"], 0,
  "La termodinamica (ΔG) dice se una reazione è possibile; la velocità è oggetto della cinetica.")
q("m1t-02", T, "f", "11", "Se Keq > 1, il ΔG°' della reazione è:", ["Positivo", "Negativo", "Zero", "Indeterminabile"], 1,
  "ΔG°' = −RT ln Keq: con Keq > 1 il logaritmo è positivo e il ΔG°' negativo, la reazione procede verso i prodotti.",
  note="Sbobina di Biochimica II, p. 11: parla di «keq > 0», «keq = 0» e «keq < 0». La Keq è sempre positiva: i casi corretti sono Keq > 1, = 1 e < 1. Nella formula manca anche il logaritmo: ΔG°' = −RT ln Keq.")
q("m1t-03", T, "m", "11", "Quali sono le condizioni standard biochimiche a cui si riferisce il ΔG°'?", [
  "pH 7, 25 °C, reagenti e prodotti 1 M", "pH 7,4, 37 °C, concentrazioni cellulari", "pH 0, 0 °C, 1 atm", "pH 7, 37 °C, reagenti 1 mM"], 0,
  "pH 7, 298 K (25 °C) e tutte le specie a 1 M; per questo nella cellula il ΔG reale è diverso.",
  note="Sbobina di Biochimica II, p. 10: c'è scritto «T = 273 °K (+25 °C)». 25 °C sono 298 K; 273 K sono 0 °C.")
q("m1t-04", T, "m", "12", "In una serie A ⇌ B ⇌ C all'equilibrio, cosa succede se la cellula consuma C?", [
  "Si forma più A", "Aumenta la trasformazione di A in B e di B in C", "Non cambia nulla perché le reazioni sono all'equilibrio", "La Keq aumenta"], 1,
  "Per il principio di Le Chatelier, sottrarre il prodotto sposta tutte le reazioni della serie verso destra.")
q("m1t-05", T, "a", "12", "Perché le reazioni regolate di una via metabolica hanno ΔG molto negativo?", [
  "Perché sono le più veloci",
  "Perché sono praticamente irreversibili: lì la via si può accendere o spegnere senza che torni indietro",
  "Perché non hanno bisogno di enzimi",
  "Perché sono all'equilibrio"], 1,
  "Le reazioni vicine all'equilibrio vanno nei due sensi secondo le concentrazioni; quelle con ΔG molto negativo vanno in un solo senso e sono il punto in cui intervengono gli enzimi allosterici.")
q("m1t-06", T, "a", "12", "Una reazione ha ΔG°' = +5 kJ/mol. Nella cellula procede verso destra. Come è possibile?", [
  "Non è possibile: con ΔG°' positivo la reazione va sempre a sinistra",
  "Perché il prodotto viene consumato e il rapporto prodotti/reagenti resta basso, rendendo il ΔG negativo",
  "Perché l'enzima rende il ΔG°' negativo",
  "Perché a 37 °C il ΔG°' cambia segno"], 1,
  "ΔG = ΔG°' + RT ln([P]/[R]): se il prodotto è basso il termine logaritmico è negativo e può superare il ΔG°'. È il caso dell'aldolasi nella glicolisi.")
q("m1t-07", T, "l", "11", "Nella formula ΔG°' = −RT ln Keq, che cosa indica l'apice (')?", [
  "Che il valore è riferito a pH 7", "Che il valore è a 37 °C", "Che è la seconda misura", "Che è espresso in kcal"], 0,
  "L'apice distingue lo standard biochimico (pH 7) da quello chimico (attività dell'H⁺ = 1, pH 0).",
  note="La distinzione tra ΔG° e ΔG°' non è esplicitata nella sbobina.")

T = "m1-atp"
q("m1a-01", T, "f", "13", "Quanto vale il ΔG°' di idrolisi dell'ATP ad ADP + Pi?", ["−30,5 kJ/mol (−7,3 kcal/mol)", "−14 kJ/mol", "−61 kJ/mol", "+30 kJ/mol"], 0,
  "È il valore di riferimento per i composti ad alta energia.",
  note="Sbobina di Biochimica II, p. 13: subito dopo il valore di −30 kJ/mol c'è scritto che il ΔG di idrolisi dell'ATP «è ampiamente positivo». È negativo: l'idrolisi è favorita.")
q("m1a-02", T, "f", "13", "Che legame unisce il fosfato α al ribosio nell'ATP?", ["Fosfoanidridico", "Fosfoestere", "N-glicosidico", "Tioestere"], 1,
  "Ribosio (OH in 5') + fosfato = fosfoestere. Tra α-β e β-γ ci sono legami fosfoanidridici.")
q("m1a-03", T, "f", "19", "Quale di questi composti ha un potenziale di trasferimento del fosfato maggiore dell'ATP?", [
  "Glucosio 6-fosfato", "Fosfoenolpiruvato", "Glicerolo 3-fosfato", "AMP"], 1,
  "PEP, 1,3-bisfosfoglicerato e fosfocreatina superano l'ATP e possono cedergli il fosfato.")
q("m1a-04", T, "m", "14", "Perché l'idrolisi dei legami fosfoanidridici dell'ATP libera molta energia?", [
  "Perché i prodotti sono più stabilizzati (risonanza, solvatazione) e si elimina la repulsione tra cariche negative vicine",
  "Perché il legame P–O è molto più debole dei legami C–C",
  "Perché si forma una molecola d'acqua",
  "Perché il magnesio viene liberato"], 0,
  "Repulsione elettrostatica nel reagente e maggiore stabilizzazione per risonanza e solvatazione dei prodotti.")
q("m1a-05", T, "m", "14", "La scissione ATP → AMP + PPi seguita dall'idrolisi del pirofosfato libera in tutto circa:", [
  "−30 kJ/mol", "−45 kJ/mol", "−60 kJ/mol", "−90 kJ/mol"], 2,
  "Due legami fosfoanidridici scissi: circa −30 + −30. L'idrolisi del PPi rende irreversibili molte biosintesi.")
q("m1a-06", T, "m", "15", "Qual è la forma dell'ATP che partecipa alle reazioni enzimatiche?", ["ATP libero", "Mg-ATP", "Ca-ATP", "ATP protonato"], 1,
  "Il Mg²⁺ si lega ai fosfati, riduce la repulsione tra le cariche ed è la forma riconosciuta dagli enzimi ATP-dipendenti.")
q("m1a-07", T, "m", "20", "Che cosa fa la creatina chinasi all'inizio di uno sforzo muscolare?", [
  "Trasferisce il fosfato della fosfocreatina all'ADP formando ATP",
  "Trasferisce il fosfato dell'ATP alla creatina",
  "Idrolizza la fosfocreatina liberando Pi",
  "Converte la creatina in creatinina"], 0,
  "La fosfocreatina (ΔG°' ≈ −43 kJ/mol) rigenera ATP dall'ADP: è la prima riserva di energia del muscolo. La reazione è reversibile e dipende dalle concentrazioni.",
  note="Sbobina di Biochimica II, p. 20: c'è scritto che la creatina fosfato è in grado di «fosforilare l'ATP per riformare ADP». È il contrario: fosforila l'ADP e riforma ATP.")
q("m1a-08", T, "a", "14–16", "Nel muscolo, dopo un digiuno prolungato, una rialimentazione ricca di carboidrati può causare:", [
  "Ipofosfatemia, perché il fosfato viene richiamato nelle cellule per fosforilare gli zuccheri",
  "Iperfosfatemia per eccesso di ATP",
  "Ipoglicemia per eccesso di insulina",
  "Acidosi lattica immediata"], 0,
  "È la sindrome da rialimentazione: il fosfato plasmatico crolla perché finisce negli zuccheri fosforilati e nell'ATP, con rischio soprattutto per il cuore.")
q("m1a-09", T, "a", "16–17", "Se la carica energetica di una cellula scende da 0,9 a 0,6:", [
  "Aumentano le vie che consumano ATP",
  "Aumentano le vie che generano ATP e rallentano quelle che lo consumano",
  "Catabolismo e anabolismo restano invariati",
  "La cellula sintetizza più glicogeno"], 1,
  "Sotto 0,9 prevalgono le vie cataboliche; sopra prevalgono quelle anaboliche.")
q("m1a-10", T, "a", "17–18", "Durante la sintesi proteica dopo un pasto, perché la nucleotide difosfato chinasi produce GTP solo quando serve?", [
  "Perché è regolata dall'insulina",
  "Perché ha ΔG°' ≈ 0: il consumo di GTP sposta l'equilibrio verso la sua formazione",
  "Perché è inibita dall'ATP",
  "Perché è un enzima allosterico attivato dal GDP"], 1,
  "È un'azione di massa: più GTP viene consumato, più la reazione ATP + GDP ⇌ ADP + GTP va verso destra.")
q("m1a-11", T, "l", "17", "Quale nucleotide trifosfato si usa soprattutto per la biosintesi dei lipidi complessi (fosfolipidi)?", ["UTP", "GTP", "CTP", "TTP"], 2,
  "UTP per i carboidrati (UDP-glucosio), GTP per le proteine, CTP per i lipidi (CDP-diacilglicerolo, CDP-colina).")
q("m1a-12", T, "l", "13", "Nell'ATP, l'adenina è legata al ribosio. Come si chiama correttamente la molecola adenina + ribosio?", ["Adenosina", "Adenina", "Adenilato", "Desossiadenosina"], 0,
  "Adenina è la base, adenosina il nucleoside (base + ribosio), adenilato (AMP) il nucleotide.",
  note="Sbobina di Biochimica II, p. 13: c'è scritto «la base azotata adenosina». La base è l'adenina; l'adenosina è il nucleoside.")
q("m1a-13", T, "l", "20", "Qual è l'isoenzima della creatina chinasi usato come marker precoce di infarto?", ["CK-MM", "CK-BB", "CK-MB", "CK-MiMi"], 2,
  "CK-MB è l'isoenzima cardiaco; CK-MM è muscolare scheletrico, CK-BB cerebrale.")
q("m1a-14", T, "l", "15", "Quale concentrazione plasmatica di fosfato è nel range normale nell'adulto?", ["Circa 3–4,5 mg/dl", "Circa 30 mg/dl", "Circa 0,3 mg/dl", "Circa 100 mg/dl"], 0,
  "La fosfatemia normale nell'adulto è circa 2,5–4,5 mg/dl.",
  note="Sbobina di Biochimica II, p. 15: indica una fosfatemia di «30 mg/decilitro». Il valore normale è circa 3–4,5 mg/dl. Il range non è nella sbobina: viene dai testi di riferimento.")

T = "m1-coenzimi"
q("m1o-01", T, "f", "23", "L'ossidazione di un alcol secondario produce:", ["Un'aldeide", "Un chetone", "Un acido carbossilico", "Un estere"], 1,
  "Alcol primario → aldeide → acido; alcol secondario → chetone.")
q("m1o-02", T, "f", "21", "Da quali vitamine derivano NAD e FAD?", ["Niacina e riboflavina", "Tiamina e piridossina", "Biotina e acido folico", "Cobalamina e acido pantotenico"], 0,
  "NAD da niacina (B3), FAD da riboflavina (B2).")
q("m1o-03", T, "m", "23", "Che cosa riceve il NAD⁺ quando si riduce?", ["Due atomi di idrogeno", "Uno ione idruro (H⁻, cioè 2 elettroni)", "Un protone", "Un elettrone singolo"], 1,
  "Il NAD⁺ accetta un idruro; il secondo protone va in soluzione (NADH + H⁺). Il FAD invece accetta due atomi di idrogeno.")
q("m1o-04", T, "m", "23", "Il passaggio succinato → fumarato:", [
  "È un'idratazione", "È un'ossidazione FAD-dipendente che crea un doppio legame C=C", "È un'ossidazione NAD-dipendente", "Non è una reazione redox"], 1,
  "Da due carboni saturi a un doppio legame si perdono 2 elettroni: il FAD è l'accettore adatto.")
q("m1o-05", T, "m", "24", "A pH 7,4 un acido carbossilico con pKa ≈ 3,5 si trova:", [
  "Quasi tutto protonato (–COOH)", "Metà protonato e metà deprotonato", "Quasi tutto deprotonato (–COO⁻)", "Come estere"], 2,
  "Il pH è molto sopra il pKa: per questo nella cellula si dice piruvato, lattato, malato (suffisso -ato).")
q("m1o-06", T, "a", "22–23", "Ordina dal più ridotto al più ossidato il carbonio in: metano, metanolo, formaldeide, acido formico, CO₂.", [
  "Metano → metanolo → formaldeide → acido formico → CO₂",
  "CO₂ → acido formico → formaldeide → metanolo → metano",
  "Metanolo → metano → formaldeide → CO₂ → acido formico",
  "Formaldeide → metanolo → metano → acido formico → CO₂"], 0,
  "Stati di ossidazione: −4, −2, 0, +2, +4. Ogni passaggio perde 2 elettroni.", fixed=True)
q("m1o-07", T, "a", "23", "Una reazione redox biochimica si scrive con quattro termini. Quali?", [
  "Donatore ridotto + accettore ossidato → donatore ossidato + accettore ridotto",
  "Substrato + enzima → prodotto + enzima",
  "Ossidante + riducente → acqua + energia",
  "Reagente + ATP → prodotto + ADP"], 0,
  "Es. malato (donatore ridotto) + NAD⁺ (accettore ossidato) → ossalacetato + NADH + H⁺.")
q("m1o-08", T, "a", "22–23", "Il passaggio da aldeide a chetone isomerico (es. gliceraldeide 3-P → diidrossiacetone fosfato) è:", [
  "Un'ossidazione", "Una riduzione", "Un'isomerizzazione, senza cambiare lo stato di ossidazione complessivo", "Una decarbossilazione"], 2,
  "Aldeide e chetone isomerici hanno lo stesso numero di elettroni: lo catalizza un'isomerasi, senza NAD.")
q("m1o-09", T, "l", "24", "Qual è il nome corretto della specie deprotonata dell'acido piruvico?", ["Piruvato", "Piruvico", "Piruvile", "Piruvinato"], 0,
  "Suffisso -ico per l'acido protonato, -ato per la base coniugata, che è la forma presente a pH fisiologico.")
q("m1o-10", T, "l", "21", "Quale sigla indica la forma ridotta del flavin adenin dinucleotide?", ["FAD", "FADH₂", "FMN", "FADH⁺"], 1,
  "Il FAD accetta due atomi di idrogeno (2 e⁻ + 2 H⁺) e diventa FADH₂. L'FMN è il flavin mononucleotide (complesso I).")

T = "m1-enzimologia"
q("m1e-01", T, "f", "27", "Che cosa indica la KM?", [
  "La concentrazione di substrato a cui v = ½ Vmax", "La velocità massima dell'enzima", "La concentrazione dell'enzima", "La costante di equilibrio"], 0,
  "Più la KM è bassa, maggiore è l'affinità dell'enzima per il substrato.")
q("m1e-02", T, "f", "28", "Che forma ha la curva v/[S] di un enzima allosterico cooperativo?", ["Iperbolica", "Sigmoide", "Lineare", "Esponenziale decrescente"], 1,
  "Gli enzimi di Michaelis-Menten danno un'iperbole; gli allosterici una sigmoide, descritta dalla K0,5.")
q("m1e-03", T, "f", "28", "Nella forma R un enzima allosterico è:", ["Inattivo (teso)", "Attivo (rilassato)", "Denaturato", "Fosforilato"], 1,
  "R = relaxed, attiva; T = tense, inattiva.")
q("m1e-04", T, "m", "27", "Due enzimi hanno la stessa Vmax e KM₁ < KM₂. Quale è più affine al substrato?", [
  "L'enzima 1", "L'enzima 2", "Sono ugualmente affini", "Dipende dalla concentrazione dell'enzima"], 0,
  "KM più bassa = mezza velocità massima raggiunta a concentrazione di substrato più bassa = maggiore affinità.")
q("m1e-05", T, "m", "29", "Gli ormoni regolano gli enzimi soprattutto con:", [
  "Effettori allosterici", "Modificazioni covalenti come la fosforilazione", "Variazioni di pH", "Variazioni di temperatura"], 1,
  "La regolazione allosterica è locale (cellula per cellula); gli ormoni agiscono con protein chinasi e fosfatasi.")
q("m1e-06", T, "a", "27–29", "Un farmaco abbassa la K0,5 di un enzima allosterico senza cambiare la Vmax. Come si comporta?", [
  "Da effettore allosterico positivo", "Da effettore allosterico negativo", "Da inibitore competitivo", "Da denaturante"], 0,
  "La K0,5 più bassa sposta la sigmoide a sinistra: l'enzima lavora meglio a basse concentrazioni di substrato.")
q("m1e-07", T, "a", "29", "Perché le reazioni vicine all'equilibrio non sono buoni punti di regolazione?", [
  "Perché i loro enzimi sono troppo lenti",
  "Perché il flusso netto dipende dalle concentrazioni di reagenti e prodotti: cambiare l'enzima non sposta il verso",
  "Perché non hanno bisogno di coenzimi",
  "Perché avvengono solo nel mitocondrio"], 1,
  "Il controllo del flusso si esercita sulle tappe lontane dall'equilibrio, catalizzate da enzimi allosterici.")
q("m1e-08", T, "l", "27", "Come si chiama la costante k₂ in Vmax = k₂[E]?", ["Costante catalitica (kcat)", "Costante di Michaelis", "Costante di dissociazione", "Costante di specificità"], 0,
  "kcat è il numero di molecole di substrato trasformate per sito attivo al secondo. kcat/KM è la costante di specificità.")
q("m1e-09", T, "l", "42", "Un enzima con kcat/KM vicino a 10⁸–10⁹ M⁻¹ s⁻¹ si dice:", [
  "A perfezione catalitica (limitato dalla diffusione)", "Allosterico", "Saturato", "Inibito"], 0,
  "È il caso della trioso fosfato isomerasi: il limite è l'incontro tra enzima e substrato.")
q("m1e-10", T, "l", "29", "Quali residui hanno l'ossidrile usato dalle serina/treonina chinasi per legare il fosfato?", [
  "Serina e treonina", "Tirosina e triptofano", "Cisteina e metionina", "Aspartato e glutammato"], 0,
  "Si forma un fosfoestere con l'OH della catena laterale. Esistono anche tirosina chinasi (recettori per l'insulina).")
