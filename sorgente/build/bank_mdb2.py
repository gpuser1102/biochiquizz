"""Biochimica I – blocco 3, ultimi due argomenti: struttura quaternaria (p. 64–67) e tecniche per lo studio delle proteine (p. 53–54)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


T = "d3-quaternaria"
q("d3q-01", T, "f", "64", "Che cos'è la struttura quaternaria?", [
  "L'associazione di due o più catene polipeptidiche (subunità) in un complesso", "Il ripiegamento 3D di una singola catena", "La sequenza degli amminoacidi", "L'insieme di α-eliche e foglietti β"], 0,
  "Le subunità sono tenute insieme da interazioni deboli, interazioni idrofobiche e talvolta ponti disolfuro.")
q("d3q-02", T, "f", "67", "Come si chiama una proteina formata da più subunità uguali?", ["Omo-oligomero", "Etero-oligomero", "Protomero", "Monomero"], 0,
  "Se le subunità sono diverse è un etero-oligomero (es. l'anticorpo).")
q("d3q-03", T, "m", "66", "Quali sono i vantaggi della struttura quaternaria?", [
  "Stabilità, economia genetica, siti attivi tra subunità, cooperatività", "Solo una maggiore solubilità", "Maggiore velocità di traduzione di un gene lungo", "Resistenza alle proteasi e niente altro"], 0,
  "Un gene per 100 aa è più piccolo e si trascrive e traduce in modo più efficiente di uno per 700 aa.")
q("d3q-04", T, "m", "66", "Che cos'è la cooperatività in una proteina multimerica?", [
  "Il cambio conformazionale di una subunità si trasmette alle altre tramite i contatti tra subunità", "La capacità di legare più substrati diversi", "La formazione di ponti disolfuro tra subunità", "La polimerizzazione in fibre"], 0,
  "È alla base del comportamento dell'emoglobina.")
q("d3q-05", T, "a", "65", "Perché una proteina fatta di L-amminoacidi non può avere subunità disposte come immagini speculari?", [
  "L'immagine speculare richiederebbe una subunità fatta di D-amminoacidi", "Perché i ponti disolfuro lo impediscono", "Perché le subunità sono sempre diverse", "Perché la simmetria ciclica è vietata"], 0,
  "Sono possibili solo simmetrie di rotazione (ciclica, diedrica), non di inversione o riflessione.")
q("d3q-06", T, "a", "67", "Perché i microtubuli polimerizzano e depolimerizzano molto rapidamente?", [
  "I protomeri di tubulina (dimeri αβ) sono associati in modo stabile ma non covalente", "Perché le tubuline sono unite da ponti disolfuro", "Perché la tubulina è una proteina fibrosa a tripla elica", "Perché ogni protomero è un monomero"], 0,
  "Il protomero è l'unità che si ripete: per la tubulina è il dimero αβ.")
q("d3q-07", T, "l", "64", "In quale tipo di associazione due subunità si affacciano con la stessa superficie in modo complementare?", ["Isologa", "Eterologa", "Eterologa aperta", "Diedrica"], 0,
  "Nell'eterologa le subunità si concatenano traslando lungo un asse; due associazioni isologhe ruotate danno il tetramero isologo.")
q("d3q-08", T, "l", "67", "Quante subunità ha GroES e come si definisce?", ["7, è un eptamero a simmetria ciclica", "14, è un tetradecamero", "4, è un tetramero diedrico", "2, è un dimero isologo"], 0,
  "Visto dal basso forma un coperchio regolare: esempio di simmetria ciclica.")
q("dh3q-01", T, "h", "65", "Un tetramero di subunità identiche ha due assi di rotazione di ordine 2 perpendicolari tra loro. Che simmetria ha?", [
  "Diedrica D2, la più comune nei tetrameri", "Ciclica C4", "Speculare", "Elicoidale", "Nessuna simmetria"], 0,
  "La simmetria diedrica si ha quando un asse di rotazione è perpendicolare a un asse doppio: tipica dei tetrameri.")
q("dh3q-02", T, "h", "66", "Un anticorpo è formato da 2 catene pesanti e 2 leggere unite da ponti disolfuro. Come si classifica?", [
  "Etero-oligomero tetramerico, con ponti disolfuro intermolecolari che ne impediscono la dissociazione", "Omo-tetramero a simmetria ciclica", "Proteina monomerica con quattro domini", "Dimero isologo", "Polimero di protomeri come la tubulina"], 0,
  "Le catene sono diverse a due a due; i ponti disolfuro stabilizzano anche i singoli domini, tipico delle proteine extracellulari.")

T = "d3-tecniche"
q("d3x-01", T, "f", "53", "Che cos'è il proteoma?", [
  "L'insieme delle proteine espresse da una cellula in un dato momento", "L'insieme dei geni", "L'insieme delle proteine di tutti i tessuti, sempre uguale", "La sequenza di una proteina"], 0,
  "Cambia con il tipo cellulare, lo sviluppo e il ciclo cellulare: è l'espressione funzionale del genoma.")
q("d3x-02", T, "f", "53", "Su quali proprietà si basano le strategie di purificazione delle proteine?", [
  "Solubilità, carica, dimensione, capacità di legare altre molecole", "Solo la sequenza", "Solo il colore", "Il numero di ponti disolfuro"], 0,
  "Si parte da un estratto cellulare totale e si separa sfruttando queste differenze.")
q("d3x-03", T, "m", "53", "Che rapporto c'è tra purezza e resa in una purificazione?", [
  "Più alta è la purezza richiesta, più bassa è la resa", "Purezza e resa crescono insieme", "La resa è sempre il 100%", "Non c'è relazione"], 0,
  "A ogni passaggio si perde un po' di proteina; per la cristallografia serve una purezza altissima.")
q("d3x-04", T, "m", "54", "Che cosa si separa con una centrifugazione a bassa velocità (500 g per 10 min) dell'omogenato?", [
  "Cellule non lisate e frammenti grossolani, che vanno sul fondo", "I ribosomi", "Le proteine solubili", "I microsomi"], 0,
  "Nel sopranatante restano membrane, organuli più piccoli e molecole solubili.")
q("d3x-05", T, "a", "54", "Perché per la cristallografia ai raggi X serve una proteina estremamente pura?", [
  "Un cristallo si ottiene solo da sostanze molto pure", "Perché le impurità assorbono i raggi X", "Perché la proteina va denaturata", "Perché serve una grande resa"], 0,
  "Il grado di purezza dipende dagli studi che si vogliono fare.")
q("d3x-06", T, "l", "54", "Che caratteristiche ha un'ultracentrifuga?", [
  "Fino a ~80.000 rpm e 600.000 g, camera sotto vuoto, refrigerata e blindata", "Fino a 3000 rpm, a temperatura ambiente", "Usa un campo elettrico", "Funziona solo con proteine precipitate"], 0,
  "Si usa per separare organuli e macromolecole; le centrifughe comuni per cellule, batteri e precipitati con solfato d'ammonio.")
q("d3x-07", T, "l", "54", "In quale ordine sedimentano le frazioni con centrifugazioni via via più forti?", [
  "Nuclei e cellule intere → mitocondri → microsomi → citosol (sopranatante finale)", "Microsomi → mitocondri → nuclei", "Citosol → nuclei → mitocondri", "Tutte insieme a 500 g"], 0,
  "È il principio della centrifugazione differenziale.",
  note="Sbobina di Biochimica I, p. 54: indica 100.000 g per separare i mitocondri. Di norma i mitocondri sedimentano già a ~10.000–20.000 g; a 100.000 g si raccoglie la frazione microsomiale.")
q("dh3x-01", T, "h", "53–54", "Vuoi studiare un enzima della matrice mitocondriale. Quale primo passaggio ha più senso dopo l'omogeneizzazione?", [
  "Centrifugazione differenziale per isolare la frazione mitocondriale, poi purificazione per carica, dimensione o affinità", "Cristallizzare subito l'omogenato", "Ultracentrifugare a 600.000 g e usare il sopranatante", "Precipitare tutte le proteine con urea 8 M", "Ridurre i ponti disolfuro con β-mercaptoetanolo"], 0,
  "Separare prima l'organulo riduce molto il numero di proteine da cui purificare; l'urea denaturerebbe l'enzima.")
