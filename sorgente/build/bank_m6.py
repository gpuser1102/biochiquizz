"""Blocco 6 – Via dei pentoso fosfati (sbobina di Biochimica II, p. 158–170)."""
from bank_common import q

T = "m6-reazioni"
q("m6r-01", T, "f", "159", "Quali sono i due prodotti principali della via dei pentoso fosfati?", ["NADPH e ribosio 5-fosfato", "ATP e NADH", "Lattato e CO₂", "Acetil-CoA e FADH₂"], 0,
  "Il NADPH serve alle biosintesi riduttive e alla difesa antiossidante; il ribosio 5-P ai nucleotidi.")
q("m6r-02", T, "f", "159", "Dove avviene la via dei pentoso fosfati?", ["Nel citosol", "Nella matrice mitocondriale", "Nel reticolo endoplasmatico", "Nel nucleo"], 0,
  "Come la glicolisi, con cui condivide intermedi.")
q("m6r-03", T, "f", "160", "Quale enzima catalizza la prima reazione della via?", ["Glucosio 6-fosfato deidrogenasi", "Transchetolasi", "Esochinasi", "6-fosfogluconato deidrogenasi"], 0,
  "Ossida il glucosio 6-P a 6-fosfoglucono-δ-lattone, riducendo NADP⁺.")
q("m6r-04", T, "m", "160–161", "Quanti NADPH produce la fase ossidativa per glucosio 6-fosfato?", ["2", "1", "3", "4"], 0,
  "Uno dalla G6PD, uno dalla 6-fosfogluconato deidrogenasi; si libera anche una CO₂.")
q("m6r-05", T, "m", "162", "Che cosa trasferisce la transchetolasi?", ["Un frammento di 2 atomi di carbonio", "Un frammento di 3 atomi di carbonio", "Un gruppo fosfato", "Un'unità di CO₂"], 0,
  "La transaldolasi trasferisce invece 3 carboni.")
q("m6r-06", T, "m", "162", "Quale coenzima usa la transchetolasi?", ["Tiamina pirofosfato", "Piridossal fosfato", "Biotina", "NADP⁺"], 0,
  "Per questo l'attività della transchetolasi eritrocitaria si usa per valutare la carenza di tiamina.")
q("m6r-07", T, "a", "161", "Quale enzima converte il ribulosio 5-P in ribosio 5-P?", ["Ribosio 5-fosfato isomerasi", "Ribulosio 5-fosfato epimerasi", "Transaldolasi", "Fosfopentosio mutasi"], 0,
  "L'epimerasi forma invece lo xilulosio 5-P.")
q("m6r-08", T, "a", "163", "Se la cellula ha bisogno solo di NADPH e non di ribosio, che cosa succede ai pentosi?", [
  "Transchetolasi e transaldolasi li riconvertono in fruttosio 6-P e gliceraldeide 3-P, che possono rigenerare glucosio 6-P",
  "Vengono escreti", "Si accumulano", "Vanno nel ciclo di Krebs direttamente"], 0,
  "Riciclando, in teoria tutto il glucosio può essere ossidato a CO₂ producendo 12 NADPH.")
q("m6r-09", T, "a", "164", "Se la cellula ha bisogno di ribosio e non di NADPH?", [
  "Usa solo la fase non ossidativa al contrario, partendo da fruttosio 6-P e gliceraldeide 3-P della glicolisi", "Non può produrre ribosio", "Usa la gluconeogenesi", "Usa solo la G6PD"], 0,
  "La fase non ossidativa è completamente reversibile.",
  note="Sbobina di Biochimica II, p. 164: c'è scritto che «questa via è detta gluconeogenesi». Riformare glucosio 6-P dai pentosi non è la gluconeogenesi vera e propria, che parte da precursori non glucidici.")
q("m6r-10", T, "l", "160", "Come si chiama il prodotto della glucosio 6-fosfato deidrogenasi?", ["6-Fosfoglucono-δ-lattone", "6-Fosfogluconato", "Ribulosio 5-fosfato", "Gluconolattone 1-fosfato"], 0,
  "Una lattonasi lo idrolizza poi a 6-fosfogluconato.")
q("m6r-11", T, "l", "160", "Quale enzima idrolizza il lattone in 6-fosfogluconato?", ["6-Fosfogluconolattonasi", "Glucosio 6-fosfatasi", "Lattato deidrogenasi", "6-Fosfogluconato deidrogenasi"], 0,
  "La reazione avverrebbe anche spontaneamente, ma più lentamente.")
q("m6r-12", T, "l", "162", "Quale zucchero a 7 atomi di carbonio si forma nella fase non ossidativa?", ["Sedoeptulosio 7-fosfato", "Eritrosio 7-fosfato", "Xilulosio 7-fosfato", "Ribulosio 7-fosfato"], 0,
  "L'eritrosio 4-P invece ha 4 carboni ed è precursore degli amminoacidi aromatici nelle piante.")

T = "m6-regolazione"
q("m6g-01", T, "f", "165", "Qual è l'enzima regolatore della via dei pentoso fosfati?", ["Glucosio 6-fosfato deidrogenasi", "Transaldolasi", "Ribosio 5-P isomerasi", "Transchetolasi"], 0,
  "Catalizza la prima reazione, irreversibile.")
q("m6g-02", T, "m", "165", "Che cosa regola principalmente la G6PD?", ["Il rapporto NADP⁺/NADPH", "Il livello di ATP", "Il glucagone", "Il calcio"], 0,
  "Il NADPH la inibisce; quando viene consumato, il NADP⁺ la attiva.")
q("m6g-03", T, "a", "165", "In quali tessuti la via dei pentoso fosfati è particolarmente attiva?", [
  "Fegato, tessuto adiposo, ghiandola mammaria in lattazione, surrene, eritrociti", "Muscolo scheletrico", "Cervello", "Osso"], 0,
  "Sono tessuti con molta sintesi di acidi grassi o steroidi, o con forte stress ossidativo.")
q("m6g-04", T, "a", "165", "Che cosa decide il destino del glucosio 6-P tra glicolisi e via dei pentosi?", [
  "Le richieste di NADPH, ribosio 5-P e ATP della cellula", "La sola concentrazione di glucosio", "Solo l'insulina", "La temperatura"], 0,
  "Ci sono quattro modalità a seconda di cosa serve.")

T = "m6-nadph"
q("m6n-01", T, "f", "166", "Perché il NADPH è indispensabile all'eritrocita?", ["Mantiene ridotto il glutatione, che protegge dagli ossidanti", "Produce ATP", "Sintetizza emoglobina", "Trasporta ossigeno"], 0,
  "L'eritrocita non ha mitocondri: la via dei pentosi è l'unica fonte di NADPH.")
q("m6n-02", T, "f", "169", "Che cos'è il favismo?", ["Una crisi emolitica da deficit di G6PD scatenata dalle fave", "Un'allergia alle fave", "Un deficit di vitamina B12", "Una malattia del fegato"], 0,
  "Il deficit di G6PD è legato al cromosoma X.")
q("m6n-03", T, "m", "167", "In quali biosintesi serve NADPH?", ["Acidi grassi, colesterolo e steroidi, deossiribonucleotidi", "Glicogeno", "Proteine", "Urea"], 0,
  "Il NADPH è il trasportatore di elettroni per le reazioni riduttive.")
q("m6n-04", T, "m", "167", "A che cosa serve il NADPH nei neutrofili?", [
  "Alla NADPH ossidasi, che produce superossido per uccidere i batteri (burst respiratorio)", "A produrre ATP", "A sintetizzare anticorpi", "Al movimento"], 0,
  "Difetti della NADPH ossidasi causano la malattia granulomatosa cronica.")
q("m6n-05", T, "m", "168", "A che cosa servono i citocromi P450?", ["A idrossilare farmaci e steroidi usando O₂ e NADPH", "A trasportare elettroni nella catena respiratoria", "A trasportare ossigeno", "A produrre glucosio"], 0,
  "Sono monossigenasi: un atomo di O va nel substrato, l'altro forma acqua.")
q("m6n-06", T, "a", "169", "Perché il deficit di G6PD è diffuso nelle zone malariche?", ["Dà una certa protezione contro il Plasmodium falciparum", "Per mutazioni indotte dalla malaria", "Perché le fave crescono lì", "Per caso"], 0,
  "Il parassita sopporta male lo stress ossidativo dei globuli rossi carenti.")
q("m6n-07", T, "a", "169", "Che cosa sono i corpi di Heinz?", ["Precipitati di emoglobina ossidata e denaturata negli eritrociti", "Frammenti di nucleo", "Granuli di ferro", "Inclusioni batteriche"], 0,
  "Si vedono nelle crisi emolitiche da deficit di G6PD.")
q("m6n-08", T, "a", "168", "Perché un sovradosaggio di paracetamolo danneggia il fegato?", [
  "Il P450 lo trasforma in NAPQI, che normalmente è coniugato al glutatione; quando il glutatione si esaurisce, il NAPQI lega le proteine epatiche",
  "Perché inibisce la G6PD", "Perché blocca il complesso IV", "Perché consuma tutto il glicogeno"], 0,
  "L'antidoto è la N-acetilcisteina, che rigenera il glutatione.",
  note="Sbobina di Biochimica II, p. 168: il metabolita tossico e il citocromo sono scritti in modo storpiato («cye2I»). Si tratta del NAPQI (N-acetil-p-benzochinone imina) prodotto soprattutto dal CYP2E1.")
q("m6n-09", T, "a", "169", "Quali sostanze nelle fave scatenano l'emolisi nel deficit di G6PD?", ["Vicina e convicina", "Solanina e caffeina", "Lattosio e galattosio", "Amilasi e lectine"], 0,
  "Generano specie reattive dell'ossigeno. Anche farmaci come primachina e sulfamidici possono scatenarla.",
  note="Sbobina di Biochimica II, p. 169: c'è scritto che è «il polline di fava» ad avere azione ossidativa. La causa principale è l'ingestione delle fave (vicina e convicina); il polline è una causa rara e discussa.")
q("m6n-10", T, "l", "168", "Come si chiama per esteso il metabolita tossico del paracetamolo?", ["N-acetil-p-benzochinone imina", "N-acetil-p-amminofenolo", "Paracetamolo glucuronide", "Acido acetilsalicilico"], 0,
  "Sigla NAPQI.")
q("m6n-11", T, "l", "168", "Quale isoforma del P450 produce soprattutto il NAPQI, indotta dall'alcol?", ["CYP2E1", "CYP3A4", "CYP1A2", "CYP2D6"], 0,
  "Per questo chi beve cronicamente è più esposto alla tossicità del paracetamolo.")
q("m6n-12", T, "l", "169", "Nei neutrofili, quale enzima trasforma H₂O₂ in acido ipocloroso?", ["Mieloperossidasi", "Catalasi", "NADPH ossidasi", "Superossido dismutasi"], 0,
  "L'ipoclorito è un ossidante molto potente contro i batteri.",
  note="Sbobina di Biochimica II, p. 169: c'è scritto che i cloruri reagiscono con i radicali formando «ipoclorito di sodio». È la mieloperossidasi a formare acido ipocloroso (HOCl) da H₂O₂ e Cl⁻.")
q("m6n-13", T, "l", "169", "Nelle reazioni di coniugazione dei farmaci (fase II), che cosa sono glutatione, UDP-glucuronato e PAPS?", [
  "Molecole coniugate al farmaco per renderlo più idrosolubile", "Trasportatori proteici di membrana", "Enzimi del P450", "Ormoni"], 0,
  "Il PAPS (3'-fosfoadenosina 5'-fosfosolfato) è il donatore di solfato.",
  note="Sbobina di Biochimica II, p. 169: glutatione, UDP-glucuronico e PAPS sono definiti «trasportatori proteici». Sono molecole che si coniugano al farmaco, non proteine trasportatrici.")
q("m6n-14", T, "l", "169", "A quale classe di farmaci appartengono le benzodiazepine?", ["Ansiolitici e ipnotico-sedativi", "Antidepressivi triciclici", "Inibitori della ricaptazione della serotonina", "Antipsicotici"], 0,
  "Agiscono potenziando il recettore GABA-A; con l'alcol l'effetto sedativo si somma.",
  note="Sbobina di Biochimica II, p. 169: le benzodiazepine sono chiamate «farmaci antidepressivi». Sono ansiolitici/ipnotici. Non è nelle sbobine il meccanismo GABA-A.")
