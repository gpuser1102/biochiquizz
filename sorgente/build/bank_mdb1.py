"""Biochimica I – blocchi 1–3 (propedeutica, amminoacidi e peptidi, struttura delle proteine), p. 6–63.
Livelli f/m/a/l a 4 opzioni, livello h a 5 opzioni."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ---------------------------------------------------------------- 1. Ripasso di propedeutica
T = "d1-chimica"
q("d1c-01", T, "f", "6", "Quali sono i quattro elementi più abbondanti negli organismi viventi?", ["H, O, N, C", "C, O, P, S", "H, O, Na, K", "C, N, Fe, Ca"], 0,
  "Insieme sono circa il 99% della massa cellulare: sono i più leggeri e formano rispettivamente 1, 2, 3 e 4 legami.")
q("d1c-02", T, "f", "7", "Che cosa si ottiene ossidando un alcol secondario?", ["Un chetone", "Un'aldeide", "Un acido carbossilico", "Un estere"], 0,
  "L'alcol primario dà aldeide (e poi acido carbossilico); il secondario dà chetone.")
q("d1c-03", T, "m", "7", "Che fine fanno gli elettroni persi da un carbonio che si ossida nel metabolismo?", [
  "Passano a NAD⁺ o FAD, poi alla catena respiratoria e infine all'O₂, che diventa acqua", "Vengono ceduti direttamente all'O₂ nel citosol", "Restano sul carbonio come carica negativa", "Vengono usati per sintetizzare ATP dalla glicolisi"], 0,
  "Ogni ossidazione toglie 2 elettroni, raccolti dai cofattori e portati fino alla citocromo ossidasi.")
q("d1c-04", T, "m", "8", "Qual è la differenza tra configurazione e conformazione?", [
  "La configurazione cambia solo rompendo legami; la conformazione cambia per rotazione attorno ai legami singoli",
  "La conformazione cambia solo rompendo legami; la configurazione per rotazione", "Sono sinonimi", "La configurazione riguarda solo i doppi legami"], 0,
  "Configurazione: doppi legami (cis-trans) e centri chirali. Conformazione: disposizioni dovute alla libera rotazione.")
q("d1c-05", T, "a", "8", "Quanti stereoisomeri può avere una molecola con 3 centri chirali?", ["8", "6", "3", "9"], 0,
  "Con n centri chirali gli stereoisomeri sono 2ⁿ: 2³ = 8.")
q("d1c-06", T, "l", "8", "Acido maleico e acido fumarico sono:", ["Isomeri geometrici (cis-trans)", "Enantiomeri", "Isomeri di struttura", "Conformeri"], 0,
  "Differiscono per la disposizione dei sostituenti rispetto a un doppio legame che non ruota: maleico è cis, fumarico è trans.")
q("d1c-07", T, "l", "7", "Quale estremità di un polisaccaride si chiama \"riducente\"?", ["Quella con il carbonio carbonilico (anomerico) libero", "Quella con più gruppi alcolici", "Quella legata alle proteine", "Quella che contiene il legame α1→6"], 0,
  "Le macromolecole hanno una polarità: 5'/3' negli acidi nucleici, N/C nelle proteine, riducente/non riducente nei polisaccaridi.")
q("d1h-01", T, "h", "6–8", "Una molecola ha 2 centri chirali. Due suoi stereoisomeri non sono immagini speculari tra loro. Come si definiscono?", [
  "Diastereoisomeri", "Enantiomeri", "Isomeri geometrici", "Conformeri sfalsati", "Racemi"], 0,
  "Gli enantiomeri sono immagini speculari non sovrapponibili; gli stereoisomeri non speculari sono diastereoisomeri. Su 4 stereoisomeri possibili (2²) si formano 2 coppie di enantiomeri.")

T = "d1-acqua"
q("d1a-01", T, "f", "8", "Con quante molecole d'acqua può formare legami a idrogeno una molecola d'acqua (es. nel ghiaccio)?", ["4", "2", "3", "6"], 0,
  "La disposizione quasi tetraedrica degli orbitali dell'ossigeno permette 4 legami a H.")
q("d1a-02", T, "f", "9", "Perché i gas come O₂ e CO₂ sono poco solubili in acqua?", ["Sono apolari", "Sono troppo grandi", "Sono carichi", "Reagiscono con l'acqua"], 0,
  "Per questo l'O₂ è trasportato da emoglobina e mioglobina e la CO₂ soprattutto come bicarbonato.")
q("d1a-03", T, "m", "9", "Che cos'è un clatrato?", [
  "La gabbia ordinata di molecole d'acqua attorno a un soluto apolare", "Un aggregato di molecole anfipatiche", "Un legame a idrogeno tra tre atomi", "Una micella con il core polare"], 0,
  "È una struttura termodinamicamente sfavorita: l'acqua perde entropia.")
q("d1a-04", T, "a", "9", "Perché la formazione spontanea delle membrane biologiche è termodinamicamente favorita?", [
  "Perché l'aggregazione delle code apolari libera l'acqua dei clatrati, aumentandone l'entropia",
  "Perché si formano molti legami covalenti tra i fosfolipidi", "Perché le teste polari si respingono", "Perché l'acqua si lega alle code apolari"], 0,
  "È l'effetto idrofobico: lo stesso principio spiega micelle, legame enzima-substrato e ripiegamento delle proteine.")
q("d1a-05", T, "l", "8", "Qual è la caratteristica geometrica che rende più forte un legame a idrogeno?", [
  "I tre atomi coinvolti allineati su una retta", "Un angolo di 90° tra donatore e accettore", "La presenza di un doppio legame vicino", "La distanza massima tra i due atomi elettronegativi"], 0,
  "Il legame a idrogeno è direzionale: è massimo quando l'H sta tra i due atomi elettronegativi in linea.")
q("d1h-02", T, "h", "9–10", "Un enzima e il suo substrato si legano anche se il legame non forma interazioni particolarmente forti. Quale contributo termodinamico favorisce il complesso?", [
  "L'aumento di entropia delle molecole d'acqua liberate dalle superfici a contatto", "La diminuzione di entropia del complesso", "La formazione di legami covalenti transitori", "L'aumento di entalpia dovuto alla rottura dei legami a H", "La riduzione del numero di molecole d'acqua libere"], 0,
  "Separati, enzima e substrato ordinano l'acqua intorno a sé; legandosi ne liberano una parte, che guadagna disordine.")

T = "d1-metabolismo"
q("d1m-01", T, "f", "10", "Dove si accumula il glucosio come riserva negli animali?", ["Come glicogeno in fegato e muscolo", "Come amido nel fegato", "Come trigliceridi nel muscolo", "Come cellulosa nell'adipe"], 0,
  "I lipidi di riserva stanno invece nel tessuto adiposo.")
q("d1m-02", T, "m", "10", "Quale ruolo hanno soprattutto gli amminoacidi nel metabolismo secondo la sbobina?", [
  "Sintesi delle proteine; come fonte di energia sono secondari", "Fonte principale di energia", "Riserva energetica a lungo termine", "Componente principale delle membrane"], 0,
  "Le principali fonti di energia sono carboidrati e lipidi.")
q("d1m-03", T, "a", "10", "Quale di questi è un lavoro cellulare che consuma ATP per mantenere la vitalità della cellula?", [
  "Il mantenimento del potenziale di membrana", "La diffusione dell'O₂ attraverso la membrana", "La formazione dei legami a idrogeno dell'acqua", "La rotazione attorno ai legami singoli"], 0,
  "L'ATP serve a contrazione muscolare, biosintesi e mantenimento dei gradienti ionici.")
q("d1m-04", T, "l", "7", "Come si chiama l'insieme delle molecole contenenti carboidrati di una cellula?", ["Glicoma", "Lipidoma", "Proteoma", "Metaboloma"], 0,
  "Proteoma = proteine, genoma = DNA, glicoma = carboidrati, lipidoma = lipidi.")

# ---------------------------------------------------------------- 2. Amminoacidi e peptidi
T = "d2-strutturali"
q("d2s-01", T, "f", "11", "Quale amminoacido non ha un carbonio α chirale?", ["Glicina", "Alanina", "Prolina", "Serina"], 0,
  "La catena laterale della glicina è un H: il carbonio α ha due sostituenti uguali.")
q("d2s-02", T, "f", "11", "A quale serie appartengono gli amminoacidi delle proteine?", ["L", "D", "Sia L sia D in egual misura", "Nessuna delle due"], 0,
  "I D-amminoacidi si trovano solo in piccoli peptidi (parete batterica, antibiotici), sintetizzati senza ribosomi.")
q("d2s-03", T, "m", "12", "Gli L-amminoacidi sono tutti levogiri?", [
  "No, non c'è relazione tra serie D/L e verso di rotazione della luce polarizzata", "Sì, per definizione", "Sì, tranne la glicina", "No, sono tutti destrogiri"], 0,
  "D/L è una convenzione basata sulla gliceraldeide; il segno +/− si misura al polarimetro.")
q("d2s-04", T, "m", "13", "Nel sistema R/S, gli L-amminoacidi sono quasi tutti S. Qual è l'eccezione?", ["L-cisteina (R)", "L-prolina (R)", "L-serina (R)", "L-treonina (R)"], 0,
  "Lo zolfo della catena laterale ha priorità sul carbossile, quindi la sequenza dei sostituenti risulta in verso orario.")
q("d2s-05", T, "a", "14", "Quali amminoacidi hanno due centri chirali?", ["Isoleucina e treonina", "Leucina e valina", "Serina e cisteina", "Prolina e istidina"], 0,
  "Oltre al carbonio α è chirale il carbonio β; esistono i diastereoisomeri L-alloisoleucina e L-allotreonina.")
q("d2s-06", T, "a", "15", "La talidomide è un esempio di:", [
  "Enantiomeri con effetti diversi: R sedativo, S teratogeno", "Diastereoisomeri con la stessa attività", "Farmaco attivo solo come miscela racemica", "Isomeri geometrici del legame peptidico"], 0,
  "Eutomero = enantiomero attivo, distomero = inattivo o con effetti indesiderati. Oggi è usata nel mieloma multiplo.")
q("d2s-07", T, "l", "15", "Come si chiama l'enantiomero di un farmaco biologicamente attivo?", ["Eutomero", "Distomero", "Racemo", "Anomero"], 0,
  "Il distomero è quello inattivo o dannoso.")
q("d2h-01", T, "h", "12–13", "Un campione di alanina non ruota il piano della luce polarizzata. La spiegazione più probabile è:", [
  "È una miscela racemica di D- e L-alanina in parti uguali", "È L-alanina pura, che non è otticamente attiva", "L'alanina non ha centri chirali", "È D-alanina pura, che non ruota la luce", "Il polarimetro misura solo i D-amminoacidi"], 0,
  "D- e L-alanina ruotano la luce dello stesso angolo in verso opposto: in un racemo le rotazioni si annullano.")

T = "d2-classificazione"
q("d2c-01", T, "f", "16", "Quale amminoacido è un \"imminoacido\"?", ["Prolina", "Istidina", "Triptofano", "Glicina"], 0,
  "La catena laterale si richiude sul gruppo amminico, che resta senza H.")
q("d2c-02", T, "f", "16", "Quale amminoacido assorbe di più a 280 nm?", ["Triptofano", "Fenilalanina", "Tirosina", "Istidina"], 0,
  "Assorbono gli aromatici: triptofano più di tirosina, la fenilalanina meno.")
q("d2c-03", T, "m", "16", "Perché la metionina si comporta da amminoacido apolare pur contenendo zolfo?", [
  "Lo zolfo è all'interno della catena (tioetere), non è un gruppo polare libero", "Perché lo zolfo è sempre ossidato", "Perché forma ponti disolfuro", "Perché ha un anello aromatico"], 0,
  "Diverso è il caso della cisteina, con il gruppo −SH libero.")
q("d2c-04", T, "m", "16", "La prolina destabilizza l'α-elica ma è frequente in un'altra struttura. Quale?", ["Nei ripiegamenti β", "Nei foglietti β paralleli", "Nell'α-elica dell'α-cheratina", "Nel nucleo idrofobico"], 0,
  "Il suo legame peptidico può stare anche in cis, utile per invertire la catena di 180°.")
q("d2c-05", T, "a", "12", "Che cos'è la cistina?", ["Il dimero di due cisteine unite da un ponte disolfuro", "La forma ridotta della cisteina", "Un precursore della metionina", "Un derivato della serina"], 0,
  "Si forma per ossidazione e stabilizza la struttura di molte proteine.")
q("d2c-06", T, "l", "16", "In quante classi si dividono gli amminoacidi in base al gruppo R?", ["5", "3", "4", "6"], 0,
  "Apolari alifatici, aromatici, polari non carichi, carichi positivamente, carichi negativamente.")

T = "d2-acidobase"
q("d2a-01", T, "f", "17", "In che forma si trova un amminoacido in soluzione a pH neutro?", ["Ione dipolare (zwitterione)", "Molecola neutra", "Anione", "Catione"], 0,
  "Gruppo amminico protonato e carbossile deprotonato: è una sostanza anfotera.")
q("d2a-02", T, "f", "19", "Che cos'è il pKa di un gruppo?", ["Il pH a cui il gruppo è dissociato al 50%", "Il pH a cui la carica netta è zero", "Il pH a cui il gruppo è tutto protonato", "Il pH fisiologico"], 0,
  "Al pKa forma protonata e deprotonata sono in uguale concentrazione.")
q("d2a-03", T, "m", "17", "Perché il carbossile della glicina (pK ≈ 2,3) è più acido di quello dell'acido acetico (pK ≈ 4,8)?", [
  "Il gruppo amminico vicino attira elettroni e favorisce la perdita del protone", "Perché la glicina è più piccola", "Perché la glicina ha due carbossili", "Perché il gruppo amminico cede il suo protone al carbossile"], 0,
  "I due gruppi si influenzano a vicenda.")
q("d2a-04", T, "m", "19", "Come si calcola il punto isoelettrico di un amminoacido acido come il glutammato?", [
  "Media tra il pK dell'α-carbossile e quello del carbossile laterale", "Media dei pK dei gruppi amminici", "Media di tutti e tre i pK", "È uguale al pK dell'α-carbossile"], 0,
  "Si mediano i due pK che delimitano la forma a carica netta zero; per i basici i due pK dei gruppi amminici.")
q("d2a-05", T, "a", "17", "Glicina: pK₁ = 2,3 e pK₂ = 9,6. Qual è il suo punto isoelettrico?", ["≈ 5,97", "≈ 7,3", "≈ 3,6", "≈ 11,9"], 0,
  "Senza catene laterali ionizzabili il pI è la media dei due pK: (2,3 + 9,6)/2.",
  note="Sbobina di Biochimica I, p. 17: nella curva di titolazione il pK₁ della glicina è indicato come «circa 1», mentre poche righe prima è dato correttamente come 2,3.")
q("d2a-06", T, "a", "19", "Perché l'istidina è molto usata nei siti catalitici?", [
  "Ha un pKa vicino a 6: a pH fisiologico può sia cedere sia accettare protoni", "Ha un pKa di 12, sempre protonata", "È l'unico amminoacido aromatico", "Forma ponti disolfuro"], 0,
  "È un buon tampone e un ottimo donatore/accettore di protoni nella catalisi.")
q("d2a-07", T, "l", "18", "A pH 1 il glutammato ha carica netta:", ["+1", "0", "−1", "+2"], 0,
  "Tutti i gruppi sono protonati: i due carbossili sono neutri, il gruppo amminico è positivo.")
q("d2h-02", T, "h", "17–19", "Un amminoacido ha pK₁ = 2,2 (α-COOH), pK₂ = 9,0 (α-NH₃⁺) e pKR = 10,5 (gruppo amminico laterale). Qual è il suo pI e quale carica ha a pH 7?", [
  "pI ≈ 9,75; carica positiva a pH 7", "pI ≈ 5,6; carica netta zero a pH 7", "pI ≈ 7,2; carica negativa a pH 7", "pI ≈ 6,35; carica positiva a pH 7", "pI ≈ 9,75; carica negativa a pH 7"], 0,
  "Per un amminoacido basico si mediano i due pK dei gruppi amminici: (9,0 + 10,5)/2. Sotto il pI la molecola è carica positivamente.")
q("d2h-03", T, "h", "17–18", "Titolando la glicina partendo da pH 1, quando il pH sale bruscamente tra le due zone tampone?", [
  "Quando tutto il carbossile è deprotonato e il gruppo amminico non ha ancora iniziato a cedere protoni", "Quando inizia a dissociarsi il carbossile", "Quando il gruppo amminico è dissociato al 50%", "Quando la glicina raggiunge carica −1", "La curva della glicina non ha salti di pH"], 0,
  "Nella zona tra le due regioni tampone non c'è nessun gruppo che neutralizzi gli OH⁻ aggiunti: passato il primo equivalente il pH sale rapidamente fino a ~8.")

T = "d2-nutrizionale"
q("d2n-01", T, "f", "20", "Che cosa sono gli amminoacidi essenziali?", ["Quelli che l'organismo non sa sintetizzare", "Quelli più abbondanti nelle proteine", "Quelli necessari solo nei bambini", "Quelli con catena laterale carica"], 0,
  "Vanno assunti con la dieta.")
q("d2n-02", T, "f", "20", "Da quale amminoacido si ricava la cisteina?", ["Metionina", "Serina", "Treonina", "Glicina"], 0,
  "Cisteina e tirosina sono semiessenziali: si formano da altri amminoacidi se questi sono assunti a sufficienza.")
q("d2n-03", T, "m", "20", "Come si forma l'alanina dal piruvato?", [
  "Per transaminazione, prendendo il gruppo amminico dal glutammato", "Per decarbossilazione", "Per idrossilazione", "Per carbossilazione con biotina"], 0,
  "Il glutammato diventa α-chetoglutarato.")
q("d2n-04", T, "a", "21", "Perché il γ-carbossiglutammato della protrombina è importante?", [
  "Con due cariche negative lega bene il Ca²⁺ nella coagulazione", "Forma ponti disolfuro", "Stabilizza la tripla elica", "Assorbe a 280 nm"], 0,
  "È una modificazione post-traduzionale (vitamina K-dipendente).")
q("d2n-05", T, "l", "21", "Da cosa deriva la β-alanina?", ["Dalla decarbossilazione dell'aspartato", "Dalla transaminazione del piruvato", "Dall'idrossilazione dell'alanina", "Dalla degradazione della glicina"], 0,
  "Altri amminoacidi non comuni: 4-idrossiprolina e 5-idrossilisina (collagene), 6-N-metillisina (miosina).")

T = "d2-peptidico"
q("d2p-01", T, "f", "22", "Come si forma il legame peptidico?", [
  "Per condensazione tra α-carbossile di un amminoacido e α-ammino del successivo, con uscita di H₂O", "Per idrolisi", "Tra due catene laterali", "Tra due gruppi amminici"], 0,
  "Richiede energia: nella sintesi proteica si consuma GTP.")
q("d2p-02", T, "f", "27", "Perché il legame peptidico non ruota?", [
  "Per risonanza ha un parziale carattere di doppio legame", "Perché è un legame ionico", "Per l'ingombro delle catene laterali", "Perché è un legame a idrogeno"], 0,
  "Lunghezza 1,33 Å, intermedia tra singolo e doppio legame; è planare.")
q("d2p-03", T, "m", "27", "Perché il legame peptidico è quasi sempre in trans?", [
  "In cis i carboni α e le catene laterali sarebbero dallo stesso lato, con ingombro sterico", "Perché il cis non può risuonare", "Perché il trans ha più legami a H", "Perché è imposto dal ribosoma"], 0,
  "Il cis è meno stabile di circa 2 kcal/mol.")
q("d2p-04", T, "m", "26", "Quali sono le estremità del glutatione?", [
  "N-terminale del glutammato, C-terminale della glicina", "N-terminale della glicina, C-terminale del glutammato", "Entrambe della cisteina", "Non ha estremità, è ciclico"], 0,
  "È γ-glutammil-cisteinil-glicina, principale antiossidante cellulare; due molecole si uniscono con un ponte disolfuro.")
q("d2p-05", T, "a", "27", "In un tetrapeptide senza catene laterali ionizzabili, quali gruppi determinano il punto isoelettrico?", [
  "Solo l'N-terminale (~9,6) e il C-terminale (~2,2)", "Tutti e quattro i carbossili", "I legami peptidici", "I gruppi amminici di ogni residuo"], 0,
  "I gruppi impegnati nei legami peptidici non si ionizzano più.")
q("d2p-06", T, "l", "23", "Come si chiama la parte non amminoacidica di una proteina coniugata?", ["Gruppo prostetico", "Coenzima libero", "Dominio", "Apoproteina"], 0,
  "Lipoproteine, glicoproteine e metalloproteine sono esempi di proteine coniugate.")
q("d2p-07", T, "l", "26", "Peptide e polipeptide: qual è la soglia convenzionale usata nella sbobina?", ["50 amminoacidi", "10 amminoacidi", "100 amminoacidi", "20 amminoacidi"], 0,
  "Peptide < 50 aa, polipeptide > 50 aa.")
q("d2h-04", T, "h", "28", "Attorno a quali legami può ruotare lo scheletro polipeptidico?", [
  "N–Cα (φ) e Cα–C carbonilico (ψ)", "Solo attorno al legame peptidico C–N", "C=O e N–H", "Attorno ai legami delle catene laterali soltanto", "Attorno a nessun legame"], 0,
  "Il legame peptidico C–N è rigido; la catena si ripiega ruotando i due legami adiacenti al carbonio α.")

# ---------------------------------------------------------------- 3. Struttura delle proteine
T = "d3-primaria"
q("d3p-01", T, "f", "26", "Da quante catene e di quanti amminoacidi è formata l'insulina?", ["Catena A di 21 aa e catena B di 30 aa", "Catena A di 30 aa e catena B di 21 aa", "Una sola catena di 51 aa", "Tre catene di 17 aa"], 0,
  "Sequenziata da Sanger nel 1953.")
q("d3p-02", T, "f", "24", "Dove si trova il codone?", ["Sull'mRNA", "Sul tRNA", "Sul ribosoma", "Sul DNA stampo"], 0,
  "L'anticodone è la tripletta complementare sul tRNA.",
  note="Sbobina di Biochimica I, p. 24: in una frase chiama «anticodone» la tripletta dell'mRNA e «codone» quella del tRNA, poi usa i termini correttamente.")
q("d3p-03", T, "m", "26", "Quanti ponti disolfuro ha l'insulina e di che tipo?", [
  "Due intercatena (A7–B7, A20–B19) e uno intracatena (A6–A11)", "Tre intercatena", "Uno intercatena e due intracatena", "Due intracatena"], 0,
  "Grazie ai ponti disolfuro le catene assumono la conformazione funzionale.")
q("d3p-04", T, "m", "26", "Perché i ponti disolfuro si formano più facilmente fuori dalla cellula?", [
  "L'ambiente extracellulare è più ossidante", "Perché fuori c'è più cisteina", "Perché servono enzimi extracellulari", "Perché nel citosol manca l'ossigeno"], 0,
  "Nel citosol prevale un ambiente riducente.")
q("d3p-05", T, "a", "23", "Quante catene servono perché si possa parlare di struttura quaternaria?", ["Almeno due", "Esattamente quattro", "Almeno tre", "Una sola, ripiegata due volte"], 0,
  "La struttura quaternaria è l'associazione di più subunità.",
  note="Sbobina di Biochimica I, p. 23: parla di «quattro catene polipeptidiche»; bastano due o più catene.")
q("d3p-06", T, "l", "24", "Quale interazione in genere contribuisce di più alla stabilità della conformazione nativa?", ["L'effetto idrofobico", "I ponti disolfuro", "I legami ionici", "I legami peptidici"], 0,
  "Le catene apolari si raggruppano formando il nucleo idrofobico.")
q("d3h-01", T, "h", "24", "Una malattia genetica è causata dalla sostituzione di un solo amminoacido. Perché può essere così grave?", [
  "La sequenza determina la struttura 3D e quindi la funzione: un solo residuo può alterare il ripiegamento o il sito attivo", "Perché cambia il codice genetico", "Perché accorcia sempre la proteina", "Perché impedisce la trascrizione del gene", "Perché rende la proteina insolubile in ogni caso"], 0,
  "La struttura primaria contiene l'informazione per il ripiegamento; per questo dalla somiglianza tra sequenze si riconoscono anche famiglie di proteine.")

T = "d3-secondaria"
q("d3s-01", T, "f", "29", "Quanti residui ci sono per giro nell'α-elica?", ["3,6", "3", "4,2", "2"], 0,
  "Passo 5,4 Å; il C=O di un residuo lega l'N–H del residuo 4 posizioni più avanti.")
q("d3s-02", T, "f", "28", "Cosa stabilizza α-eliche e foglietti β?", [
  "Legami a idrogeno tra C=O e N–H dello scheletro", "Legami a H tra catene laterali", "Ponti disolfuro", "Interazioni ioniche"], 0,
  "Le catene laterali non partecipano, ma con la loro natura favoriscono un tipo di struttura o un altro.")
q("d3s-03", T, "m", "29", "Quali amminoacidi destabilizzano l'α-elica?", ["Prolina e glicina", "Alanina e leucina", "Glutammato e lisina", "Metionina e cisteina"], 0,
  "La prolina non ha H sull'azoto ed è rigida; la glicina è troppo flessibile.")
q("d3s-04", T, "m", "27", "Che cosa ha mostrato il grafico di Ramachandran?", [
  "Che gli angoli φ e ψ osservati occupano solo poche regioni: circa ¾ del grafico è vuoto", "Che tutte le combinazioni di φ e ψ sono possibili", "La sequenza delle proteine", "Le distanze dei ponti disolfuro"], 0,
  "Le zone popolate corrispondono ad α-elica, foglietti β e tripla elica del collagene.")
q("d3s-05", T, "a", "30", "Come è stabilizzato un ripiegamento β di 4 residui (i → i+3)?", [
  "Legame a H tra il C=O del residuo i e l'N–H del residuo i+3", "Ponte disolfuro tra i e i+3", "Legame ionico tra i+1 e i+2", "Legame a H tra le catene laterali di i+1 e i+2"], 0,
  "Inverte la catena di 180°; prolina tipica in i+1, glicina in i+2.")
q("d3s-06", T, "l", "29", "Quali sono gli angoli φ e ψ tipici dell'α-elica?", ["φ ≈ −60°, ψ ≈ −45/−50°", "φ ≈ −120°, ψ ≈ +130°", "φ ≈ +60°, ψ ≈ +45°", "φ = 0°, ψ = 0°"], 0,
  "Entrambi ruotati in senso antiorario (negativi).")
q("d3h-02", T, "h", "29–31", "Una sequenza ricca di prolina e glicina è più probabile che formi:", [
  "Ripiegamenti β o regioni senza struttura regolare", "Un'α-elica lunga e stabile", "Un foglietto β parallelo ideale", "Il nucleo idrofobico della proteina", "Una superelica coiled coil"], 0,
  "Entrambi destabilizzano l'α-elica; la prolina in cis e la glicina flessibile sono invece tipiche dei β-turn.")

T = "d3-collagene"
q("d3c-01", T, "f", "35", "Qual è l'unità tripeptidica ripetuta del collagene?", ["Gly-X-Y (X spesso Pro, Y spesso 4-Hyp)", "Ala-Gly-Ser", "Pro-Pro-Gly-Cys", "Lys-X-Y"], 0,
  "Mancano cisteina e triptofano.")
q("d3c-02", T, "f", "36", "Quale vitamina serve all'idrossilazione della prolina del collagene?", ["Vitamina C", "Vitamina K", "Vitamina B12", "Vitamina D"], 0,
  "L'acido ascorbico riporta il ferro dell'enzima da Fe³⁺ a Fe²⁺.")
q("d3c-03", T, "m", "35", "Com'è avvolta la tripla elica del collagene?", [
  "Tre catene sinistrorse avvolte tra loro in una superelica destrorsa", "Tre α-eliche destrorse in superelica sinistrorsa", "Due catene β antiparallele", "Tre catene destrorse in superelica destrorsa"], 0,
  "Ogni catena ha ~3,3 residui per giro; è diversa dall'α-elica.")
q("d3c-04", T, "m", "36", "Perché serve una glicina ogni tre residui?", [
  "È l'unico residuo abbastanza piccolo da stare al centro della tripla elica", "Perché forma i legami crociati", "Perché viene idrossilata", "Perché lega gli zuccheri"], 0,
  "I suoi N–H formano i legami a H tra le tre catene.")
q("d3c-05", T, "a", "37", "Nella reazione della prolil-idrossilasi, che fine fa l'α-chetoglutarato?", [
  "Viene decarbossilato e ossidato a succinato + CO₂", "Viene ridotto a glutammato", "Si lega alla prolina", "Non partecipa, è solo un effettore"], 0,
  "Un atomo dell'O₂ va sulla prolina, l'altro sull'α-chetoglutarato.",
  note="Sbobina di Biochimica I, p. 40: dice che l'α-chetoglutarato viene «ridotto» ad acido succinico; è una decarbossilazione ossidativa.")
q("d3c-06", T, "a", "39", "Perché lo scorbuto dà gengive sanguinanti e ferite che si riaprono?", [
  "Senza vitamina C il collagene non viene idrossilato e la tripla elica è instabile", "Perché manca la vitamina K per la coagulazione", "Perché si accumulano legami crociati", "Perché il collagene non viene secreto"], 0,
  "Senza idrossiprolina il collagene si denatura alla temperatura corporea.")
q("d3c-07", T, "a", "40", "Perché i domini globulari del procollagene vengono rimossi solo fuori dalla cellula?", [
  "Altrimenti il collagene polimerizzerebbe in fibrille dentro la cellula", "Perché servono per la glicosilazione", "Perché la peptidasi è solo nel Golgi", "Perché proteggono dalla collagenasi"], 0,
  "La procollagene peptidasi agisce nello spazio extracellulare: si forma il tropocollagene.")
q("d3c-08", T, "l", "42", "Quale enzima trasforma la lisina in allisina per i legami crociati?", ["Lisil ossidasi", "Lisil idrossilasi", "Prolil idrossilasi", "Procollagene peptidasi"], 0,
  "Il latirismo (tossina di alcune leguminose) blocca proprio la lisil ossidasi.")
q("d3c-09", T, "l", "40", "Su quale residuo avviene la glicosilazione del collagene?", ["Idrossilisina", "Idrossiprolina", "Prolina", "Glicina"], 0,
  "Si legano glucosio e galattosio; i tipi II e IV sono i più glicosilati.",
  note="Sbobina di Biochimica I, p. 40: indica la glicosilazione «a livello di Pro o OH-Pro»; avviene sull'idrossilisina.")
q("d3c-10", T, "l", "34", "Quale caratteristica strutturale dell'α-cheratina le dà durezza?", ["Alto contenuto di cisteina con ponti disolfuro", "Tripla elica", "Foglietti β ricchi di glicina", "Glicosilazione"], 0,
  "Due α-eliche destrorse in coiled coil sinistrorso; la permanente rompe e riforma i ponti disolfuro.")
q("d3h-03", T, "h", "44", "Un bambino ha fratture multiple da traumi minimi; un altro ha articolazioni ipermobili e pelle iperestensibile. Entrambi hanno probabilmente:", [
  "Difetti genetici del collagene: osteogenesi imperfetta il primo, Ehlers-Danlos il secondo", "Scorbuto, da carenza di vitamina C", "Latirismo", "Deficit di elastina", "Carenza di vitamina D in entrambi"], 0,
  "Le malattie ereditarie del collagene; scorbuto e latirismo dipendono invece dalla dieta.")
q("d3h-04", T, "h", "42", "Con l'età tendini e articolazioni diventano più rigidi. Il meccanismo molecolare principale è:", [
  "L'accumulo di legami crociati covalenti tra le molecole di collagene", "La perdita delle glicine della tripla elica", "La riduzione dell'idrossiprolina", "La sostituzione del collagene con elastina", "L'aumento della glicosilazione"], 0,
  "I legami crociati tra allisine (o allisina e lisina) aumentano col tempo e irrigidiscono le fibre.")
q("d3h-05", T, "h", "36–37", "La prolil-idrossilasi a volte lavora senza prolina. Cosa succede e perché serve la vitamina C?", [
  "L'α-chetoglutarato viene decarbossilato lo stesso e il ferro resta Fe³⁺: l'ascorbato lo riporta a Fe²⁺", "L'enzima idrossila un'altra prolina vicina", "Il ferro passa a Fe⁴⁺ e l'enzima si degrada", "L'ascorbato sostituisce l'α-chetoglutarato", "Non succede nulla, la vitamina C serve ad altre reazioni"], 0,
  "Senza ascorbato l'enzima resterebbe bloccato nella forma ossidata.")

T = "d3-terziaria"
q("d3t-01", T, "f", "32", "Quali proteine hanno un solo tipo di struttura secondaria e funzione strutturale?", ["Le proteine fibrose", "Le proteine globulari", "Gli enzimi", "Le immunoglobuline"], 0,
  "Sono insolubili in acqua e conferiscono resistenza ed elasticità.")
q("d3t-02", T, "m", "46", "Che differenza c'è tra motivo e dominio?", [
  "Motivo: combinazione di pochi elementi di struttura secondaria; dominio: unità globulare compatta e funzionale", "Sono sinonimi", "Il motivo è più grande del dominio", "Il dominio è solo una α-elica"], 0,
  "Un dominio (≈40–100+ residui) è formato da più motivi.")
q("d3t-03", T, "a", "32", "Mioglobina di 153 aa: quanto sarebbe lunga se fosse tutta in conformazione β?", ["≈ 540 Å", "≈ 230 Å", "≈ 54 Å", "≈ 5400 Å"], 0,
  "In α-elica sarebbe un bastoncello di ≈230 Å; solo la forma globulare compatta è funzionale.",
  note="Sbobina di Biochimica I, p. 32: scrive «540 aa»; sono 540 Å.")
q("d3t-04", T, "l", "47", "Come si chiama la struttura formata da più cappi β-α-β ripetuti che si richiudono su sé stessi?", ["Barile α/β", "Chiave greca", "Coiled coil", "Foglietto β piatto"], 0,
  "La chiave greca è fatta solo di filamenti β.")
q("d3h-06", T, "h", "33", "Una soluzione proteica ha A₂₈₀ = 0,5 in una cuvetta da 1 cm. In una cuvetta da 2 cm l'assorbanza sarebbe:", ["1,0", "0,25", "0,5", "2,0", "0,75"], 0,
  "A = ε·c·l: raddoppiando il cammino ottico l'assorbanza raddoppia.",
  note="Sbobina di Biochimica I, p. 33: definisce l'assorbanza come log del rapporto «trasmessa/incidente»; è log(I₀/I), incidente su trasmessa (la formula riportata è corretta).")

T = "d3-folding"
q("d3f-01", T, "f", "55", "Con quale proteina Anfinsen studiò il folding?", ["Ribonucleasi A", "Mioglobina", "Lisozima", "Insulina"], 0,
  "Piccolo enzima monomerico di 124 aa con 4 ponti disolfuro.")
q("d3f-02", T, "f", "55", "A cosa serve il β-mercaptoetanolo nell'esperimento di Anfinsen?", ["Riduce i ponti disolfuro", "Denatura rompendo le interazioni idrofobiche", "Ossida le cisteine", "Idrolizza i legami peptidici"], 0,
  "L'urea (agente caotropico) denatura; il β-mercaptoetanolo riduce.")
q("d3f-03", T, "m", "55", "Che cosa dimostrò Anfinsen rimuovendo insieme urea e β-mercaptoetanolo?", [
  "La ribonucleasi si ripiega da sola e riacquista tutta l'attività: la sequenza contiene l'informazione del folding", "Che servono i chaperoni", "Che i ponti disolfuro si formano a caso", "Che la proteina resta inattiva"], 0,
  "Nobel 1972: la struttura nativa è la più stabile termodinamicamente.")
q("d3f-04", T, "m", "54", "Che cosa afferma il paradosso di Levinthal?", [
  "Esplorando a caso tutte le conformazioni il folding richiederebbe un tempo incompatibile con la vita", "Che le proteine non si ripiegano mai da sole", "Che il folding non è spontaneo", "Che il folding avviene solo nel ribosoma"], 0,
  "Il ripiegamento segue vie dirette, determinate dalla sequenza.")
q("d3f-05", T, "m", "58", "Quale coppia di chaperonine forma la camera di ripiegamento in E. coli?", ["GroEL (14 subunità) e GroES (7 subunità)", "DnaK e DnaJ", "Hsp90 e Hsp70", "PDI e GrpE"], 0,
  "GroES fa da coperchio alla camera di GroEL.")
q("d3f-06", T, "a", "49–50", "Il folding riduce il disordine della catena. Perché è comunque spontaneo?", [
  "Il collasso idrofobico libera l'acqua ordinata attorno alle catene apolari, aumentandone l'entropia", "Perché si formano molti ponti disolfuro", "Perché i residui polari liberano energia", "Perché consuma ATP"], 0,
  "Il contributo dei residui polari è circa nullo.")
q("d3f-07", T, "a", "57", "Con 8 cisteine, quante combinazioni di 4 ponti disolfuro sono possibili?", ["105", "28", "16", "840"], 0,
  "7 × 5 × 3 × 1 = 105, di cui una sola corretta: il folding è deterministico.")
q("d3f-08", T, "a", "58", "Nel ciclo di Hsp70, che cosa fanno DnaJ e GrpE?", [
  "DnaJ stimola l'idrolisi dell'ATP (DnaK si chiude sulla proteina); GrpE scambia ADP con ATP (DnaK la rilascia)", "DnaJ rilascia la proteina, GrpE la lega", "Sono due subunità di GroEL", "Degradano le proteine misfoldate"], 0,
  "DnaK-ADP è la forma chiusa ad alta affinità.")
q("d3f-09", T, "l", "59", "Quale percentuale delle proteine neosintetizzate richiede anche GroEL/GroES secondo la sbobina?", ["≈ 15%", "≈ 85%", "≈ 50%", "≈ 1%"], 0,
  "L'85% si ripiega da sola o con Hsp70.")
q("d3f-10", T, "l", "56", "Che effetto ha lo iodoacetato sulle cisteine?", ["Le carbossimetila covalentemente", "Le ossida ad acido cisteico", "Riduce i ponti disolfuro", "Le trasforma in serine"], 0,
  "L'acido performico invece le ossida ad acido cisteico (−SO₃⁻).")
q("d3f-11", T, "l", "60", "Dove agisce la proteina disolfuro isomerasi?", ["Nel reticolo endoplasmatico", "Nel citosol", "Nei mitocondri", "Nel nucleo"], 0,
  "Rompe e riforma i ponti disolfuro finché non si ottengono quelli corretti.")
q("d3h-07", T, "h", "55", "Anfinsen riossida la ribonucleasi denaturata lasciando l'urea. Ottiene un enzima inattivo. Cosa lo riattiva?", [
  "Togliere l'urea e aggiungere tracce di β-mercaptoetanolo, che rimescola i ponti disolfuro finché si formano quelli giusti", "Aggiungere altra urea", "Aggiungere chaperoni GroEL", "Riscaldare a 90 °C", "Aggiungere iodoacetato"], 0,
  "I ponti disolfuro formati a caso bloccano la proteina «rimescolata»; con poco riducente si rompono e riformano nella configurazione nativa, più stabile.")
q("d3h-08", T, "h", "62", "Perché nelle malattie da aggregati (Alzheimer, Parkinson, prioni) è difficile intervenire una volta iniziata la malattia?", [
  "I controlli funzionano prima dell'oligomerizzazione: formati gli oligomeri di foglietti β, la crescita delle fibrille accelera", "Perché le proteine aggregate sono troppo piccole", "Perché il proteasoma degrada solo le fibrille", "Perché le fibrille sono fatte di α-eliche stabili", "Perché le proteine coinvolte non hanno sequenza nota"], 0,
  "Il passaggio chiave è la conversione verso strutture piatte ricche di foglietti β che si impilano.")
q("d3h-09", T, "h", "62", "Una proteina non si ripiega nonostante Hsp70 e GroEL/ES. Qual è il suo destino normale?", [
  "Marcatura con ubiquitina e degradazione nel proteasoma o per autofagia", "Secrezione all'esterno", "Ritorno al ribosoma per essere riletta", "Conversione in collagene", "Accumulo nei mitocondri"], 0,
  "Se l'eliminazione fallisce si formano oligomeri e aggregati.",
  note="Sbobina di Biochimica I, p. 62: dice che l'ubiquitina «riconosce» le proteine misfoldate; la riconoscono gli enzimi della via di ubiquitinazione (E3 ligasi), che poi attaccano l'ubiquitina. Semplificazione accettabile.")
