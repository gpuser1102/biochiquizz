"""Giro 2026-11-24, blocco 4 – riempimento degli argomenti scarni:
caratteristiche degli enzimi e marcatori di patologia (Biochimica I, p. 112–129)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Caratteristiche degli enzimi (p. 112–117) ──────────────────────────────
C = "d6-caratteristiche"

q("u1124-156", C, "f", "114", "Su che cosa agisce un enzima per accelerare una reazione?", [
  "Sull'energia di attivazione, che abbassa",
  "Sul ΔG della reazione, che rende più negativo",
  "Sulla costante di equilibrio, che sposta verso i prodotti",
  "Sull'energia libera dei prodotti, che abbassa fino allo stato basale",
  "Sulla temperatura del mezzo, che innalza",
  ], 0,
  "L'energia libera della reazione catalizzata è uguale a quella della reazione non catalizzata: la spontaneità non dipende dal catalizzatore.")

q("u1124-157", C, "f", "115", "Che cosa succede all'enzima al termine della reazione che catalizza?", [
  "Non viene consumato né modificato in modo permanente",
  "Viene consumato in quantità equimolare al substrato",
  "Resta legato covalentemente a uno dei due prodotti",
  "Viene degradato e deve essere risintetizzato ogni volta",
  "Perde il cofattore, che va rifornito a ogni ciclo catalitico",
  ], 0,
  "Torna nella forma originaria, pronto ad accogliere nuove molecole di substrato.")

q("u1124-158", C, "m", "115", "Quali reazioni può accelerare un enzima?", [
  "Solo quelle che avvengono già spontaneamente, anche se molto lentamente",
  "Solo quelle che hanno un ΔG positivo, rendendole termodinamicamente possibili",
  "Qualsiasi reazione, anche non spontanea, purché ci sia il cofattore adatto",
  "Solo quelle in cui i reagenti sono presenti in concentrazione molto elevata",
  "Solo quelle bimolecolari, in cui due reagenti danno due prodotti distinti",
  ], 0,
  "L'enzima non rende possibile una reazione impossibile: accelera, da 10⁷ a 10¹⁷ volte, una reazione che è già spontanea ma troppo lenta.")

q("u1124-159", C, "m", "115", "Che cos'è l'energia di legame nell'interazione enzima-substrato?", [
  "L'energia che si libera quando si formano le interazioni fra enzima e substrato",
  "L'energia che serve a rompere il legame covalente fra enzima e substrato",
  "L'energia immagazzinata nei legami chimici del substrato prima della catalisi",
  "L'energia che l'enzima spende per cambiare la propria conformazione nativa",
  "L'energia che il substrato cede alle molecole d'acqua che lo circondano",
  ], 0,
  "Entrando nel sito attivo il substrato sostituisce le interazioni che aveva con l'acqua con quelle con l'enzima: la spontaneità del processo è legata anche alla libertà riacquistata dalle molecole d'acqua.")

q("u1124-160", C, "m", "116", "Che cosa comporta l'adattamento indotto per l'idea di «chiave e serratura»?", [
  "Vale solo in parte: il sito attivo cambia forma quando lega il substrato",
  "La conferma pienamente: sito attivo e substrato combaciano già perfettamente",
  "La smentisce del tutto: il substrato non viene riconosciuto in modo specifico",
  "Vale solo per gli enzimi allosterici, che hanno più di una subunità",
  "Vale solo per gli enzimi che lavorano su due substrati contemporaneamente",
  ], 0,
  "Il legame del substrato induce un cambiamento conformazionale che avvicina e orienta i reagenti, favorendo lo stato di transizione: è alla base dell'abbassamento dell'energia di attivazione.")

q("u1124-161", C, "a", "117", "Perché un pH lontano dall'optimum riduce la velocità di un enzima, anche prima di denaturarlo?", [
  "Cambia lo stato di protonazione delle catene laterali del sito attivo",
  "Cambia la concentrazione del substrato disponibile nella soluzione",
  "Riduce il numero di molecole di enzima presenti nella cellula",
  "Abbassa la temperatura ottimale a cui l'enzima può lavorare",
  "Impedisce al cofattore metallico di legarsi stabilmente al sito attivo dell'enzima",
  ], 0,
  "Nel sito attivo alcune catene laterali donano o strappano protoni: la catalisi acido-base funziona solo a un dato pH. Agli estremi si aggiunge poi la perdita di struttura terziaria o quaternaria.")

q("u1124-162", C, "a", "116", "Perché, pur occupando meno del 5% della superficie, il sito attivo da solo non basta?", [
  "L'intera catena deve ripiegarsi e muoversi per rendere possibile la catalisi",
  "Il resto della proteina serve soltanto a proteggere il sito attivo dall'acqua",
  "La parte restante lega i cofattori, che non entrano nel sito attivo",
  "Il resto della superficie serve a legare altre molecole di enzima",
  "La catena esterna al sito attivo serve solo a dare solubilità alla proteina",
  ], 0,
  "Il sito attivo è una tasca complementare al substrato, ma l'intera catena polipeptidica è necessaria e in genere deve andare incontro a modifiche conformazionali per catalizzare la reazione.")

q("u1124-163", C, "l", "116", "Quali ioni, secondo la sbobina, attivano gli enzimi senza partecipare alla reazione?", [
  "Sodio, potassio, calcio e cloro",
  "Ferro, rame, zinco e manganese",
  "Magnesio, molibdeno, cobalto e selenio",
  "Fosfato, solfato, nitrato e carbonato",
  "Litio, bario, stronzio e alluminio",
  ], 0,
  "Molti cofattori sono invece metalli di transizione, che partecipano direttamente alla catalisi; i cofattori organici si chiamano coenzimi.")

q("u1124-164", C, "h", "115", "Due reazioni hanno lo stesso ΔG negativo, ma una è velocissima e l'altra impercettibile. Come se lo spiega?", [
  "Hanno energie di attivazione diverse, che il ΔG non dice nulla sulla velocità",
  "Hanno costanti di equilibrio diverse, quindi diverse quantità di prodotto",
  "La prima è catalizzata da un enzima, quindi ha un ΔG più favorevole",
  "La seconda avviene a temperatura più bassa, quindi è termodinamicamente sfavorita",
  "La prima è esoergonica e la seconda endoergonica, nonostante il ΔG uguale",
  ], 0,
  "Il ΔG dice se la reazione può avvenire, non quanto in fretta: la velocità dipende dalla barriera dell'energia di attivazione, che è ciò su cui agisce l'enzima.")


# ── Enzimi come marcatori di patologie (p. 129) ────────────────────────────
M = "d6-marcatori"

q("u1124-165", M, "f", "129", "Quanto a lungo resta elevata nel sangue la creatina chinasi dopo un infarto?", [
  "Sale molto rapidamente e nell'arco di 48 ore può scomparire del tutto",
  "Sale lentamente e resta elevata per almeno due settimane",
  "Sale rapidamente e resta elevata per circa un mese",
  "Resta invariata nelle prime 48 ore e poi sale lentamente",
  "Sale soltanto se l'infarto interessa anche il muscolo scheletrico adiacente",
  ], 0,
  "È proprio la rapidità della discesa a rendere insufficiente il dosaggio della sola CK a distanza di qualche giorno.")

q("u1124-166", M, "m", "129", "Quale isoenzima della creatina chinasi è il marcatore cardiaco più usato?", [
  "La CK-MB",
  "La CK-MM",
  "La CK-BB",
  "La LDH-5",
  "La LDH-1",
  ], 0,
  "Viene rilasciato precocemente nel sangue dopo l'infarto del miocardio; si usa insieme alla troponina, anch'essa un buon marcatore precoce.")

q("u1124-167", M, "m", "129", "Perché il contenuto enzimatico del sangue aumenta dopo un danno tissutale?", [
  "Le cellule danneggiate riversano nel sangue il loro contenuto, enzimi compresi",
  "Il fegato aumenta la sintesi degli enzimi per riparare il tessuto colpito",
  "Il rene riduce l'escrezione degli enzimi circolanti durante il danno",
  "Gli enzimi plasmatici vengono attivati per proteolisi limitata dalle cellule lese",
  "Il tessuto danneggiato smette di captare gli enzimi normalmente circolanti",
  ], 0,
  "Un certo passaggio avviene già nel normale ricambio cellulare; il danno lo amplifica. Poiché molti enzimi sono tipici di un tessuto, il loro aumento orienta la diagnosi.")

q("u1124-168", M, "a", "129", "Un paziente arriva riferendo un forte dolore toracico avuto tre giorni prima. La CK è normale. Che cosa conviene dosare?", [
  "La lattato deidrogenasi, che resta elevata più a lungo",
  "Solo la CK, ripetuta a distanza di qualche ora",
  "La fosfatasi alcalina, che segue l'andamento della CK",
  "L'amilasi, che si alza nei danni muscolari tardivi",
  "La creatina chinasi delle urine, più stabile di quella del sangue",
  ], 0,
  "La CK può essere già rientrata a 48 ore: accoppiando la LDH, che permane, si può datare l'evento anche a distanza di giorni.")

q("u1124-169", M, "h", "128", "Quale abbinamento via metabolica – compartimento è corretto secondo la sbobina?", [
  "Sintesi degli acidi grassi – citosol",
  "Sintesi degli acidi grassi – matrice mitocondriale",
  "Ciclo di Krebs – citosol",
  "Ossidazione degli acidi grassi – lisosomi",
  "Decarbossilazione del piruvato – citosol",
  ], 0,
  "Nei mitocondri: ciclo di Krebs, ossidazione degli acidi grassi e decarbossilazione del piruvato. Nel citosol: glicolisi, via dell'HMP e sintesi degli acidi grassi. Nei lisosomi: degradazione di biomolecole complesse.",
  fixed=False)
