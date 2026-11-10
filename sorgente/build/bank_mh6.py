"""Domande HARD (livello h), modulo 6: via dei pentoso fosfati (pp. 159–170)."""
from bank_common import q

T = "m6-reazioni"
q("h6r-01", T, "h", "160", "Quale sequenza descrive la fase ossidativa della via dei pentoso fosfati?", [
  'G6PD → lattonasi → 6-fosfogluconato deidrogenasi',
  'Isomerasi → G6PD → lattonasi',
  'Lattonasi → G6PD → 6-fosfogluconato deidrogenasi',
  'Fosfoglucoisomerasi → G6PD → transchetolasi',
  'Transchetolasi → transaldolasi → G6PD, con produzione di 2 NADPH',
  ], 0,
  'G6P → 6-fosfogluconolattone (NADPH) → 6-fosfogluconato → ribulosio 5-P + CO₂ (NADPH). Per ogni G6P: 2 NADPH e 1 CO₂.')
q("h6r-02", T, "h", "162", "Quale bilancio corrisponde alla completa ossidazione di 6 G6P tramite la via dei pentoso fosfati con ricircolo (fase ricombinativa + gluconeogenesi)?", [
  '5 G6P + 6 CO₂ + 12 NADPH',
  '6 ribosio 5-P + 6 NADPH',
  '5 G6P + 1 CO₂ + 2 NADPH',
  '12 piruvato + 12 NADPH',
  '6 CO₂ + 6 NADPH, senza G6P residuo',
  ], 0,
  '6 G6P + 12 NADP⁺ → 5 G6P + 6 CO₂ + 12 NADPH: in pratica un G6P è ossidato a 6 CO₂.',
  note="Sbobina di Biochimica II, p. 162: c'è scritto che delle 6 molecole di glucosio «se ne perde una sottoforma di anidride carbonica». Più precisamente si liberano 6 CO₂ (una per ciascun G6P entrato), che equivalgono a un glucosio.")
q("h6r-03", T, "h", "162–163", "Quale enzima della fase ricombinativa usa la tiamina pirofosfato e che cosa trasferisce?", [
  'Transchetolasi: unità a 2 C',
  'Transaldolasi: unità a 3 C',
  'Ribosio 5-P isomerasi: unità a 1 C',
  'G6PD: unità a 2 C',
  "Lattonasi: unità a 3 C, con apertura dell'anello",
  ], 0,
  'La transchetolasi trasferisce unità a 2 C da un chetoso (es. xilulosio 5-P) a un aldoso. La transaldolasi (unità a 3 C) non ha coenzimi.')
q("h6r-04", T, "h", "162–163", "Un alcolista con carenza di tiamina. Quale attività della via dei pentoso fosfati si riduce e come si può dosare?", [
  'La transchetolasi, dosabile negli eritrociti',
  'La G6PD, dosabile con il NADPH',
  'La transaldolasi, dosabile nel plasma',
  'La 6-fosfogluconato deidrogenasi',
  'La lattonasi, dosabile nelle urine come 6-fosfogluconato',
  ], 0,
  'La transchetolasi è TPP-dipendente. Il test della transchetolasi eritrocitaria non è nelle sbobine (Lehninger).')
q("h6r-05", T, "h", "164", "Una cellula in rapida divisione ha bisogno di molto ribosio 5-P ma di poco NADPH. Quale percorso usa?", [
  'Usa al contrario la fase non ossidativa partendo da F6P e GAP',
  'Fa solo la fase ossidativa e scarta il NADPH prodotto',
  'Converte il NADPH in eccesso in ribosio 5-fosfato',
  'Usa la gluconeogenesi per ottenere il ribosio',
  'Ossida il ribosio a CO₂ per smaltire il NADPH e poi lo risintetizza dal G6P',
  ], 0,
  'Salta la fase ossidativa: le reazioni di transchetolasi e transaldolasi sono reversibili.')
q("h6r-06", T, "h", "164", "Una cellula ha bisogno sia di NADPH sia di ribosio 5-P in proporzioni simili. Quale parte della via è attiva?", [
  'Solo la fase ossidativa',
  'Solo la fase ricombinativa',
  'Tutta la via con ricircolo',
  'Solo la glicolisi',
  'La gluconeogenesi, che produce sia NADPH sia ribosio dal lattato',
  ], 0,
  'Il ribulosio 5-P viene isomerizzato a ribosio 5-P e usato per i nucleotidi. È la seconda finalità della via nella sbobina.')
q("h6r-07", T, "h", "164", "Un adipocita sta sintetizzando acidi grassi e ha bisogno solo di NADPH. Che fine fanno i pentosi?", [
  'Tornano F6P e GAP con la fase ricombinativa',
  'Si accumulano come ribosio 5-fosfato',
  'Vengono eliminati come ribosio libero',
  'Diventano glicogeno',
  'Vengono ossidati a CO₂ nella fase ricombinativa, producendo altro NADPH',
  ], 0,
  'F6P e GAP rientrano in glicolisi o, nel fegato, possono tornare a G6P (ricircolo).',
  note="Sbobina di Biochimica II, p. 164: il ritorno da F6P e GAP a G6P viene chiamato «gluconeogenesi» e si dice che avviene solo nel fegato. Usa gli enzimi della gluconeogenesi (es. FBPasi1), ma la gluconeogenesi in senso stretto parte da precursori non glucidici.")
q("h6r-08", T, "h", "160", "Che cosa distingue il NADPH dal NADH e perché è importante?", [
  "Un fosfato in 2' sul ribosio: gli enzimi distinguono i due pool",
  "Il NADPH ha un'adenina in più che lega le reduttasi",
  'Il NADPH porta 4 elettroni invece di 2',
  'Il NADPH si trova solo nel mitocondrio',
  'Non ci sono differenze funzionali: gli enzimi usano indifferentemente NADH e NADPH',
  ], 0,
  'Il pool NADPH (anabolico) è soprattutto ridotto, il pool NAD⁺ (catabolico) soprattutto ossidato.')

T = "m6-regolazione"
q("h6g-01", T, "h", "165", "Qual è il principale punto di controllo della via dei pentoso fosfati?", [
  'La G6PD, controllata dal rapporto NADP⁺/NADPH',
  'La transchetolasi, inibita dalla tiamina',
  'La transaldolasi, attivata dal F6P',
  "La ribosio 5-P isomerasi, inibita dall'ATP",
  'La 6-fosfogluconato deidrogenasi, inibita dal ribosio 5-fosfato',
  ], 0,
  'Il NADPH la inibisce, il NADP⁺ prodotto dalle biosintesi la attiva: il flusso segue il consumo di NADPH.')
q("h6g-02", T, "h", "165", "In un epatocita dopo un pasto ricco di carboidrati, la sintesi di acidi grassi è molto attiva. Che cosa succede alla via dei pentoso fosfati?", [
  'Il NADP⁺ aumenta e la G6PD accelera',
  'Il NADPH è alto e la via si blocca',
  'La via si sposta nel mitocondrio',
  'La via produce NADH invece di NADPH',
  'Non cambia nulla, perché la via è regolata solo dagli ormoni',
  ], 0,
  "Il NADPH viene consumato dalla sintesi degli acidi grassi e il flusso del G6P nella via aumenta. Non è nelle sbobine che l'insulina aumenta anche la sintesi di G6PD.")
q("h6g-03", T, "h", "159", "In quali tessuti la via dei pentoso fosfati è particolarmente attiva e perché?", [
  'Fegato, adiposo, mammella, surrene, eritrociti, tessuti proliferanti',
  'Solo muscolo scheletrico e cuore',
  'Solo cervello e retina',
  'Solo i tessuti che fanno gluconeogenesi',
  'Solo gli eritrociti, perché non hanno mitocondri e altre vie per il NADPH',
  ], 0,
  'Biosintesi di lipidi e steroidi (fegato, adiposo, mammella in lattazione, corteccia surrenale); glutatione (eritrociti); ribosio (tessuti in rapida proliferazione).')
q("h6g-04", T, "h", "165", "Perché nel muscolo scheletrico la fase ossidativa della via è poco attiva?", [
  'Fa poche biosintesi riduttive: il NADPH resta alto',
  'Non ha glucosio 6-fosfato nel citosol',
  'Non ha bisogno di ribosio',
  'È inibita dal glucagone',
  'Non contiene NADP⁺, ma solo NAD⁺ legato agli enzimi glicolitici',
  ], 0,
  'Il NADPH alto inibisce la G6PD: la via segue la domanda di NADPH.')
q("h6g-05", T, "h", "160–164", "Perché le reazioni della fase non ossidativa sono reversibili mentre la fase ossidativa no?", [
  'La fase ossidativa ha deidrogenazioni e una decarbossilazione con ΔG molto negativo',
  'La fase non ossidativa consuma ATP a ogni trasferimento, e questo la rende reversibile',
  'La fase ossidativa avviene nel mitocondrio',
  'La fase non ossidativa usa NADPH',
  'In realtà sono tutte irreversibili',
  ], 0,
  'La fase non ossidativa trasferisce unità carboniose tra zuccheri fosfato con ΔG ≈ 0: può lavorare nei due sensi a seconda dei bisogni.')
q("h6g-06", T, "h", "164", "Se la G6PD è inibita, una cellula in divisione può ancora produrre ribosio 5-P?", [
  'Sì, dalla fase non ossidativa invertita, ma senza NADPH',
  'No, perché il ribosio deriva solo dalla fase ossidativa',
  'Sì, ma solo nel mitocondrio',
  'Sì, tramite la gluconeogenesi',
  'No, perché la transchetolasi richiede NADPH come coenzima',
  ], 0,
  'F6P + GAP → pentosi: ribosio e NADPH hanno vie di produzione separabili.')
q("h6g-07", T, "h", "159", "Perché il ribosio 5-P è importante anche per i coenzimi?", [
  'Serve per i nucleotidi presenti anche in NAD, FAD e CoA',
  'Il ribosio è esso stesso un coenzima delle deidrogenasi',
  'Il ribosio trasporta elettroni come il NADPH',
  "Il ribosio fornisce il fosfato all'ATP",
  'Il ribosio è il precursore diretto del glucosio nel fegato e quindi delle vitamine idrosolubili',
  ], 0,
  'Le vitamine vengono «attivate» legandole a parti di nucleotidi (es. AMP in NAD, FAD e CoA).')
q("h6g-08", T, "h", "160", "Che cosa succede se il ribosio 5-P non viene usato ma serve NADPH?", [
  'Diventa ribulosio 5-P e poi xilulosio 5-P, ed entra nella fase ricombinativa',
  'Il ribosio 5-P inibisce la G6PD e blocca la via',
  'Il ribosio 5-P viene ossidato a CO₂ dalla transaldolasi',
  'Il ribosio 5-P esce dalla cellula con i GLUT',
  'Il ribosio 5-P viene trasformato in NADPH dalla 6-fosfogluconato deidrogenasi',
  ], 0,
  "Il ribosio 5-P accumulato torna ribulosio 5-P (isomerasi) e l'epimerasi produce xilulosio 5-P. Ribulosio 5-P e xilulosio 5-P sono epimeri al C3.")

T = "m6-nadph"
q("h6n-01", T, "h", "170", "Un uomo con deficit di G6PD mangia fave e dopo un giorno ha urine scure, ittero e anemia. Quale meccanismo?", [
  "Senza NADPH il glutatione non si rigenera: l'Hb si ossida e gli eritrociti si lisano",
  'Le fave contengono un inibitore della piruvato chinasi eritrocitaria',
  "Le fave bloccano la sintesi dell'emoglobina nei reticolociti",
  'Le fave causano una carenza acuta di ferro e folati',
  'Le fave contengono anticorpi diretti contro la membrana degli eritrociti del soggetto',
  ], 0,
  "Le sostanze ossidanti delle fave aumentano i perossidi; l'emoglobina ossidata precipita (corpi di Heinz). È il favismo; anche farmaci e infezioni possono scatenare crisi.",
  note="Sbobina di Biochimica II, p. 170: si attribuisce l'azione ossidativa al «polline di fava». Le crisi sono scatenate soprattutto dall'ingestione delle fave (vicina e convicina); l'inalazione del polline è un'evenienza molto più rara.")
q("h6n-02", T, "h", "170", "Perché il deficit di G6PD colpisce soprattutto gli eritrociti e soprattutto i maschi?", [
  "L'eritrocita non ha altre fonti di NADPH; il gene è sul cromosoma X",
  'Solo gli eritrociti hanno la G6PD',
  'Il gene è sul cromosoma Y',
  'Le donne non hanno eritrociti con G6PD',
  'È autosomico dominante ma più grave nei maschi per motivi ormonali',
  ], 0,
  "L'eritrocita non ha mitocondri; i maschi emizigoti esprimono il difetto. Le femmine eterozigoti possono essere affette in parte per inattivazione dell'X.")
q("h6n-03", T, "h", "166–167", "Come funziona il citocromo P450 epatico nella idrossilazione di un farmaco?", [
  "Usa O₂ e due elettroni del NADPH: un O al substrato, l'altro all'acqua",
  "Usa NADH come donatore e produce ATP durante l'idrossilazione",
  "Trasferisce il fosfato dall'ATP al farmaco per renderlo solubile",
  'Usa il glutatione come donatore di ossigeno per il farmaco',
  "Idrolizza il farmaco con una molecola d'acqua",
  ], 0,
  'Gli elettroni arrivano tramite la P450 reduttasi (FAD/FMN): RH → ROH. È una monoossigenasi (ossidasi a funzione mista).',
  note="Sbobina di Biochimica II, pp. 166 e 168: compaiono «citocromo p5» e «P450 (cye2I)». Sono il citocromo b5 e il CYP2E1. Inoltre l'adrenodossina è descritta per il sistema mitocondriale, ma nella spiegazione del meccanismo viene usata anche per quello del reticolo, dove gli elettroni arrivano dalla P450 reduttasi.")
q("h6n-04", T, "h", "168–169", "Un forte bevitore assume dosi abituali di paracetamolo e sviluppa epatite acuta. Perché?", [
  "L'alcol induce il CYP2E1: più metabolita tossico e meno glutatione",
  "L'alcol inibisce tutti i citocromi P450 e il paracetamolo si accumula",
  "Il paracetamolo inibisce l'alcol deidrogenasi e l'acetaldeide si accumula",
  "L'alcol aumenta la glucuronazione del paracetamolo",
  'Il paracetamolo viene trasformato in acetaldeide dal CYP2E1 indotto',
  ], 0,
  "Il CYP2E1 trasforma più paracetamolo nel metabolita tossico NAPQI; il glutatione, già impoverito, non basta a coniugarlo. L'antidoto (N-acetilcisteina) ricostituisce il glutatione: non è nelle sbobine.",
  note="Sbobina di Biochimica II, p. 168: il metabolita è chiamato «N-acetil-β-benzochinone imina»; è la N-acetil-p-benzochinone imina (NAPQI).")
q("h6n-05", T, "h", "169", "Nei neutrofili e nei macrofagi, a che cosa serve il NADPH durante la fagocitosi?", [
  'La NADPH ossidasi produce superossido nel fagolisosoma',
  "Serve a produrre l'ATP necessario alla fagocitosi",
  'Serve a sintetizzare gli anticorpi',
  'Serve a ridurre il glutatione dei batteri',
  "Serve a degradare il lattato prodotto durante l'infiammazione",
  ], 0,
  'Dal superossido derivano H₂O₂ e, tramite mieloperossidasi, acido ipocloroso, che uccidono i batteri. Un difetto della NADPH ossidasi causa la malattia granulomatosa cronica (non nelle sbobine).',
  note="Sbobina di Biochimica II, p. 169: si parla di «ipoclorito di sodio». La mieloperossidasi produce acido ipocloroso (HOCl) da H₂O₂ e Cl⁻.")
q("h6n-06", T, "h", "167", "Come può il citocromo P450 aumentare la tossicità di una sostanza?", [
  'Producendo metaboliti più reattivi, come dal benzopirene',
  'Il P450 inattiva sempre le sostanze che idrossila',
  'Il P450 rende le sostanze più idrofobiche',
  'Il P450 consuma tutto il NADPH della cellula',
  'Il P450 non agisce sugli xenobiotici ma solo sugli steroidi',
  ], 0,
  'Il benzopirene del fumo idrossilato diventa cancerogeno. Altre volte il P450 attiva un profarmaco (es. alcuni antistaminici) o inattiva un farmaco (ibuprofene, diazepam).')
q("h6n-07", T, "h", "169", "Perché due pazienti possono rispondere in modo molto diverso alla stessa dose di un chemioterapico come il 5-fluorouracile?", [
  'Per i polimorfismi degli enzimi che lo metabolizzano',
  'Perché il farmaco viene eliminato solo dai reni',
  'Perché la risposta dipende solo dal peso corporeo',
  'Perché il farmaco agisce solo nelle donne',
  'Perché il farmaco non viene metabolizzato e resta in circolo per settimane',
  ], 0,
  "Chi inattiva il farmaco più rapidamente ha meno farmaco attivo, chi lentamente rischia più tossicità: è la base della medicina di precisione. Non è nelle sbobine che per il 5-FU l'enzima chiave è la diidropirimidina deidrogenasi (DPD), più che un P450.")
q("h6n-08", T, "h", "168", "Nel metabolismo del paracetamolo, perché il NADPH serve due volte?", [
  'Per il citocromo P450 e per rigenerare il glutatione',
  'Per produrre ATP e per sintetizzare il farmaco',
  'Per ridurre il farmaco e per ossidare il glutatione',
  'Per attivare due volte la G6PD',
  "Per idrolizzare il farmaco e poi coniugarlo con l'acido glucuronico",
  ], 0,
  'Il NADPH fornisce elettroni al P450 e alla glutatione reduttasi; il glutatione ridotto coniuga il metabolita tossico (glutatione S-transferasi).')
