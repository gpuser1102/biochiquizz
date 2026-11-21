"""Giro 2026-11-21, blocco 1 – Biochimica I, biologia molecolare: acidi nucleici (p. 223–228),
studio del DNA (p. 229–230), topologia del DNA e nucleosoma (p. 230–233), duplicazione (p. 234–241)."""
from bank_common import q as _q

S = "Biochimica I"


def q(*a, **k):
    k.setdefault("src", S)
    _q(*a, **k)


# ── Acidi nucleici (p. 223–228) ─────────────────────────────────────────────
T = "d13-acidi"
q("u1121-001", T, "f", "223", "Che cosa distingue il deossiribosio dal ribosio?", [
  "Il deossiribosio non ha l'OH in posizione 2'",
  "Il deossiribosio non ha l'OH in posizione 3'",
  "Il deossiribosio non ha l'OH in posizione 5'",
  "Il deossiribosio ha un carbonio in meno",
  "Il deossiribosio è in forma piranosica",
  ], 0,
  "Ribosio e deossiribosio differiscono solo per l'OH in 2'; in entrambi gli acidi nucleici lo zucchero è in forma furanosica.")
q("u1121-002", T, "f", "224", "Quale base azotata si trova nel DNA ma non nell'RNA?", [
  "Timina",
  "Uracile",
  "Citosina",
  "Adenina",
  "Guanina",
  ], 0,
  "Pirimidine: citosina, timina (solo DNA), uracile (solo RNA). Purine: adenina e guanina, in entrambi.")
q("u1121-003", T, "m", "225", "Quale atomo della base forma il legame N-glicosidico con il C1' dello zucchero?", [
  "N1 nelle pirimidine, N9 nelle purine",
  "N9 nelle pirimidine, N1 nelle purine",
  "N3 nelle pirimidine, N7 nelle purine",
  "N1 sia nelle pirimidine sia nelle purine",
  "C1 della base sia nelle pirimidine sia nelle purine",
  ], 0,
  "Il legame unisce il C1' dello zucchero (OH in β) all'N1 delle pirimidine o all'N9 delle purine.",
  note="Errore nella sbobina (Biochimica I, p. 224): parla di legame «tra il carbonio 1 dello zucchero e il carbonio 1 della base azotata». La base partecipa con un azoto (N1 o N9), come la sbobina stessa dice a p. 225.")
q("u1121-004", T, "l", "225", "Quale coppia base – nucleoside segue la regola dei suffissi -idina e -osina?", [
  "Citosina – citidina",
  "Adenina – adenidina",
  "Guanina – guanidina",
  "Timina – timosina",
  "Uracile – uracosina",
  ], 0,
  "Pirimidine → -idina (citidina, uridina, timidina); purine → -osina (adenosina, guanosina).")
q("u1121-005", T, "f", "226", "Che cosa si libera quando un nucleotide trifosfato viene aggiunto a una catena di acido nucleico?", [
  "Pirofosfato",
  "Fosfato inorganico",
  "AMP",
  "Una molecola di ATP",
  "Un nucleoside libero",
  ], 0,
  "Si usano nucleotidi trifosfato: nel legame fosfodiestere restano il fosfato α, mentre β e γ escono come pirofosfato.")
q("u1121-006", T, "m", "225", "In che verso procede la polimerizzazione degli acidi nucleici e tra quali gruppi si forma il legame?", [
  "5'→3'; tra l'OH in 3' della catena e il fosfato in 5' del nucleotide in arrivo",
  "3'→5'; tra l'OH in 5' della catena e il fosfato in 3' del nucleotide in arrivo",
  "5'→3'; tra l'OH in 2' della catena e il fosfato in 5' del nucleotide in arrivo",
  "3'→5'; tra l'OH in 3' della catena e il fosfato in 5' del nucleotide in arrivo",
  "5'→3'; tra il fosfato in 3' della catena e l'OH in 5' del nucleotide in arrivo",
  ], 0,
  "La catena cresce all'estremità 3'-OH, che attacca il fosfato α in 5' del nucleotide trifosfato in arrivo.")
q("u1121-007", T, "m", "226", "Nell'esperimento di Griffith, quale iniezione uccideva i topi?", [
  "Batteri R vivi insieme a batteri S uccisi dal calore",
  "Solo batteri S uccisi dal calore, in dose elevata",
  "Solo batteri R vivi, in dose elevata",
  "Batteri R e batteri S, entrambi uccisi dal calore",
  "Batteri R vivi insieme a proteine estratte dal ceppo R",
  ], 0,
  "Un «fattore di trasformazione» dei batteri S morti trasformava parte dei batteri R vivi nel ceppo virulento S.")
q("u1121-008", T, "a", "227", "Hershey e Chase infettano batteri con fagi T2 marcati con ³⁵S, poi agitano nel frullatore e centrifugano. Dove si ritrova la radioattività?", [
  "Soprattutto nel surnatante, con i residui virali rimasti fuori",
  "Soprattutto nel sedimento, dentro le cellule batteriche",
  "Divisa in parti uguali tra il surnatante e il sedimento batterico",
  "Soprattutto nel DNA dei fagi figli liberati dopo la lisi",
  "Soprattutto legata al cromosoma del batterio infettato",
  ], 0,
  "Lo zolfo marca le proteine (non c'è nel DNA): il rivestimento proteico resta fuori e finisce nel surnatante. Il ³²P (DNA) invece entra nei batteri.")
q("u1121-009", T, "a", "227", "Un DNA a doppio filamento contiene il 30% di adenina. Quale percentuale di citosina contiene?", [
  "20%",
  "30%",
  "40%",
  "70%",
  "15%",
  ], 0,
  "Regole di Chargaff: A = T = 30%, quindi G + C = 40% e G = C = 20%.")
q("u1121-010", T, "l", "228", "Nel DNA B, quanto misurano circa il diametro dell'elica e la distanza tra due basi successive?", [
  "20 Å e 3,4 Å",
  "12 Å e 3,4 Å",
  "20 Å e 34 Å",
  "34 Å e 3,4 Å",
  "6 Å e 36 Å",
  ], 0,
  "Diametro 20 Å, basi distanziate di 3,4 Å, un giro completo ogni ~34–36 Å (circa 10,5 basi per giro).",
  note="Imprecisione nella sbobina (Biochimica I, p. 228): definisce il passo dell'elica (36 Å) come «la distanza tra due nucleotidi successivi». Il passo è la lunghezza di un giro completo (~34–36 Å, circa 10,5 bp); la distanza tra basi successive è 3,4 Å.")
q("u1121-011", T, "m", "228", "Perché i gruppi fosfato, carichi negativamente, non destabilizzano la doppia elica?", [
  "Stanno all'esterno e interagiscono con cationi come Mg²⁺, che ne schermano la carica",
  "Stanno all'interno e vengono neutralizzati dai legami a idrogeno con le basi azotate",
  "Sono protonati a pH fisiologico, quindi nella cellula non portano carica netta",
  "Formano ponti salini con i gruppi amminici delle basi del filamento complementare",
  "Sono legati covalentemente agli istoni, che ne annullano la carica in ogni caso",
  ], 0,
  "Le interazioni ioniche con i cationi in soluzione minimizzano la repulsione tra fosfati; al centro ci sono le basi, con interazioni idrofobiche.")
q("u1121-012", T, "h", "228", "Quale affermazione sulle forme del DNA è corretta?", [
  "Il DNA Z è sinistrorso, si forma in sequenze alternate GC e ha le G ruotate di 180° sul legame glicosidico",
  "Il DNA A è sinistrorso, si forma negli ibridi DNA-RNA e ha un passo più lungo e un diametro più stretto",
  "Il DNA B è sinistrorso, è la forma descritta da Watson e Crick e ha circa 10,5 paia di basi per giro",
  "Il DNA Z è destrorso, si forma in sequenze ricche di A e T e ha un passo più corto e un diametro più largo",
  "Il DNA A è destrorso, si forma solo nel DNA superavvolto negativo e ha le basi parallele all'asse",
  ], 0,
  "B destrorso (Watson e Crick); A destrorso, passo più corto e diametro più largo (ibridi DNA-RNA); Z sinistrorso. La sbobina chiama il DNA Z «artificiale»: tratti di DNA Z esistono anche nelle cellule (Lehninger).")
q("u1121-013", T, "h", "227", "Un campione di acido nucleico contiene A 25%, U 25%, G 30%, C 20%. Che cosa si può concludere?", [
  "È RNA a singolo filamento, perché c'è uracile e G e C non sono uguali",
  "È DNA a doppio filamento, perché la somma delle purine è il 55%",
  "È RNA a doppio filamento, perché A e U sono presenti nella stessa quantità",
  "È DNA a singolo filamento, perché G e C non sono uguali tra loro",
  "È un ibrido DNA-RNA, perché A e U sono uguali ma G e C no",
  ], 0,
  "L'uracile indica RNA. In un acido nucleico a doppio filamento varrebbero le regole di Chargaff (A = U, G = C): qui G ≠ C, quindi non è appaiato.")

# ── Studio del DNA: spettrofotometria, elettroforesi, fluorimetria (p. 229–230) ──
T = "d13-studio"
q("u1121-014", T, "f", "229", "A quale lunghezza d'onda assorbono al massimo gli acidi nucleici?", [
  "260 nm",
  "280 nm",
  "230 nm",
  "340 nm",
  "450 nm",
  ], 0,
  "Le basi azotate assorbono a ~260 nm; le proteine a 280 nm (amminoacidi aromatici).")
q("u1121-015", T, "m", "229", "Che cos'è l'effetto ipercromico?", [
  "L'aumento dell'assorbanza a 260 nm quando il DNA si denatura",
  "La diminuzione dell'assorbanza a 260 nm quando il DNA si denatura",
  "L'aumento dell'assorbanza a 280 nm quando il DNA lega proteine",
  "Lo spostamento del massimo di assorbimento da 260 a 280 nm",
  "L'aumento di fluorescenza quando un intercalante lega il DNA",
  ], 0,
  "Nella doppia elica le basi impilate assorbono meno; separando i filamenti l'assorbanza a 260 nm aumenta.")
q("u1121-016", T, "m", "229", "Quale di questi DNA ha la temperatura di fusione più alta?", [
  "Un DNA con il 65% di G + C",
  "Un DNA con il 65% di A + T",
  "Un DNA con il 50% di G + C",
  "Un DNA con il 40% di G + C",
  "Un DNA con il 25% di G + C",
  ], 0,
  "Le coppie G-C hanno tre legami a idrogeno, le A-T due: più G + C, più alta la temperatura di transizione.")
q("u1121-017", T, "a", "229", "Un campione di DNA diluito 1:10 ha A₂₆₀ = 0,5. Qual è la concentrazione del campione originale?", [
  "250 µg/mL",
  "25 µg/mL",
  "200 µg/mL",
  "2500 µg/mL",
  "500 µg/mL",
  ], 0,
  "1 unità di A₂₆₀ = 50 µg/mL di DNA: 0,5 × 50 × 10 = 250 µg/mL. Con il fattore dell'RNA (40) verrebbero 200 µg/mL.")
q("u1121-018", T, "a", "230", "Un estratto di DNA ha A₂₆₀/A₂₈₀ = 1,3. Che cosa indica?", [
  "Il campione è contaminato da proteine",
  "Il campione è DNA puro, senza contaminanti",
  "Il campione è contaminato da RNA",
  "Il campione contiene DNA denaturato",
  "Il campione contiene DNA frammentato",
  ], 0,
  "Per un DNA puro il rapporto è 1,6–2,0: un valore più basso indica proteine, che assorbono a 280 nm.")
q("u1121-019", T, "m", "229", "Perché 1 unità di A₂₆₀ corrisponde a 50 µg/mL di DNA ma a 40 µg/mL di RNA?", [
  "Perché l'RNA a singolo filamento assorbe di più, quindi ne basta meno per la stessa assorbanza",
  "Perché il ribosio assorbe a 260 nm, mentre il deossiribosio non assorbe a quella lunghezza d'onda",
  "Perché l'uracile assorbe molto più della timina, quindi ne basta meno per la stessa assorbanza",
  "Perché l'RNA è più corto e le estremità della catena assorbono più delle basi interne",
  "Perché il DNA lega più acqua e lo strato di idratazione riduce l'assorbanza a 260 nm",
  ], 0,
  "È una conseguenza dell'effetto ipercromico: le basi non impilate in una doppia elica assorbono di più.")
q("u1121-020", T, "f", "230", "Verso quale polo migra il DNA nell'elettroforesi su gel e in base a che cosa si separa?", [
  "Verso il polo positivo, in base alle dimensioni",
  "Verso il polo negativo, in base alle dimensioni",
  "Verso il polo positivo, in base alla carica netta",
  "Verso il polo negativo, in base al punto isoelettrico",
  "Verso il polo positivo, in base al contenuto in G + C",
  ], 0,
  "Il DNA è carico negativamente in modo uniforme (fosfati), quindi migra verso l'anodo e il gel separa per lunghezza.")
q("u1121-021", T, "m", "230", "Come funzionano i coloranti usati per vedere il DNA nel gel di agarosio?", [
  "Si inseriscono tra le basi impilate e diventano fluorescenti solo a contatto con il DNA",
  "Si legano ai fosfati e assorbono a 260 nm solo dopo che il DNA si è denaturato",
  "Si legano in modo covalente alle guanine e si colorano solo nel DNA superavvolto",
  "Si legano al solco minore e spengono la fluorescenza naturale delle basi azotate del DNA",
  "Si inseriscono tra le basi e tagliano il DNA nei punti in cui si sono intercalati",
  ], 0,
  "Sono agenti intercalanti (anelli aromatici idrofobici): per questo alterano la struttura del DNA e sono potenzialmente cancerogeni.")
q("u1121-022", T, "a", "230", "Che cosa NON può dire la fluorimetria, a differenza di spettrofotometria ed elettroforesi?", [
  "Se il campione è puro o se il DNA è integro o degradato",
  "Quanto DNA c'è in un campione mille volte più diluito",
  "Quanto DNA c'è anche in presenza di proteine contaminanti",
  "Quanto DNA c'è, usando una curva di taratura con standard",
  "Se nel campione c'è DNA oppure RNA, con sonde specifiche",
  ], 0,
  "La fluorimetria è ~1000 volte più sensibile e le proteine non interferiscono, ma non dà né il rapporto A₂₆₀/A₂₈₀ né le bande del gel.")
q("u1121-023", T, "h", "230", "Bisogna quantificare circa 5 ng/mL di DNA in un estratto che contiene proteine e capire se il DNA è integro. Quale combinazione è più adatta?", [
  "Fluorimetria per la quantità, elettroforesi su gel per l'integrità",
  "Spettrofotometria a 260 nm per la quantità, rapporto A₂₆₀/A₂₈₀ per l'integrità",
  "Fluorimetria per la quantità, rapporto A₂₆₀/A₂₈₀ per l'integrità",
  "Spettrofotometria a 280 nm per la quantità, fluorimetria per l'integrità",
  "Elettroforesi su gel per la quantità, fluorimetria per l'integrità",
  ], 0,
  "5 ng/mL dà un'A₂₆₀ di circa 0,0001 (1 unità = 50 µg/mL): serve la fluorimetria, su cui le proteine non interferiscono. L'integrità si vede solo dalle bande del gel; A₂₆₀/A₂₈₀ dice la purezza.")
q("u1121-024", T, "h", "229", "Due DNA vengono scaldati lentamente misurando A₂₆₀: X raggiunge metà dell'aumento a 85 °C, Y a 75 °C. Quale conclusione è corretta?", [
  "X è più ricco in G-C di Y, perché le coppie G-C hanno tre legami a idrogeno",
  "Y è più ricco in G-C di X, perché le coppie G-C si separano a temperatura più bassa",
  "X è più ricco in A-T di Y, perché le coppie A-T hanno tre legami a idrogeno",
  "X e Y hanno la stessa composizione, ma X era già a singolo filamento all'inizio",
  "Y è più ricco in G-C di X, perché il suo aumento di A₂₆₀ è avvenuto prima",
  ], 0,
  "La temperatura di transizione sale con la percentuale di G-C: è anche il modo per stimare la composizione in basi di un genoma.")

# ── Topologia del DNA e nucleosoma (p. 230–233) ──────────────────────────────
T = "d13-topologia"
q("u1121-025", T, "f", "230", "Quali di queste molecole di DNA sono di solito circolari?", [
  "Cromosoma batterico, plasmidi e DNA mitocondriale",
  "Cromosomi nucleari umani, plasmidi e DNA mitocondriale",
  "Cromosoma batterico, cromosomi nucleari e telomeri",
  "Plasmidi, cromosomi di lievito e DNA dei centromeri",
  "DNA mitocondriale, cromosomi metafasici e telomeri",
  ], 0,
  "Sono circolari cromosomi batterici, plasmidi, DNA mitocondriale e dei cloroplasti e i genomi di molti virus animali.")
q("u1121-026", T, "m", "231", "Perché nel gel il DNA superavvolto corre più veloce dello stesso DNA rilassato?", [
  "È più compatto e incontra meno attrito nella maglia del gel",
  "Ha più cariche negative per unità di lunghezza del rilassato",
  "Ha meno paia di basi, perché il superavvolgimento ne elimina",
  "Lega meno colorante intercalante, quindi è più leggero",
  "Ha tratti a singolo filamento che scivolano meglio nel gel",
  ], 0,
  "Stesso numero di basi e stessa carica, ma forma più compatta: maggiore mobilità elettroforetica.")
q("u1121-027", T, "m", "231", "Nella relazione Lk = Tw + Wr, che cosa indicano Tw e Wr?", [
  "Tw il numero di giri della doppia elica, Wr il numero di superavvolgimenti",
  "Tw il numero di superavvolgimenti, Wr il numero di giri della doppia elica",
  "Tw il numero di paia di basi per giro, Wr il numero di tagli sul filamento",
  "Tw il numero di tagli della topoisomerasi, Wr il numero di ATP consumati",
  "Tw il numero di nucleosomi, Wr il numero di giri intorno a ogni ottamero",
  ], 0,
  "Twist e writhe possono cambiare l'uno a spese dell'altro; Lk cambia solo se si taglia un filamento.")
q("u1121-028", T, "a", "231", "Un DNA circolare rilassato è lungo 2080 bp. Quanto vale il suo numero di legame Lk₀?", [
  "200",
  "208",
  "20",
  "104",
  "2000",
  ], 0,
  "Lk₀ = bp / 10,4 = 2080 / 10,4 = 200.")
q("u1121-029", T, "a", "231", "Un DNA circolare rilassato ha Lk = 20; una topoisomerasi lo porta a Lk = 18. Quanto valgono ΔLk e σ?", [
  "ΔLk = −2; σ = −0,1",
  "ΔLk = +2; σ = +0,1",
  "ΔLk = −2; σ = −0,9",
  "ΔLk = −18; σ = −0,9",
  "ΔLk = −2; σ = −10",
  ], 0,
  "ΔLk = Lk − Lk₀ = 18 − 20 = −2; σ = ΔLk / Lk₀ = −2/20 = −0,1: superavvolgimento negativo.",
  note="Refuso nella sbobina (Biochimica I, p. 231): «20 + 2 = 2». Con il superavvolgimento positivo Lk = 22.")
q("u1121-030", T, "a", "232", "Un DNA rilassato di 84 bp ha Lk ≈ 8. Se si toglie un giro (Lk = 7) senza formare superavvolgimenti, ogni quante paia di basi si incrocerebbero i filamenti?", [
  "12",
  "10,4",
  "9",
  "7",
  "14",
  ], 0,
  "84 / 7 = 12 invece di 10,4: è la deformazione che il DNA compensa formando superavvolgimenti.")
q("u1121-031", T, "m", "232", "Quale vantaggio funzionale danno i superavvolgimenti negativi?", [
  "Facilitano l'apertura della doppia elica per duplicazione e trascrizione",
  "Impediscono la separazione dei due filamenti durante la duplicazione e la trascrizione",
  "Proteggono il DNA dagli enzimi di restrizione dei batteri",
  "Aumentano il numero di paia di basi per giro della doppia elica",
  "Rendono il DNA più rigido e quindi più difficile da compattare",
  ], 0,
  "Il DNA meno avvolto è predisposto alla fusione (separazione dei filamenti); il superavvolgimento serve anche alla compattazione.")
q("u1121-032", T, "h", "232", "Quale affermazione sulle DNA topoisomerasi è corretta?", [
  "Quelle di tipo I tagliano un solo filamento e non richiedono ATP; quelle di tipo II tagliano entrambi i filamenti",
  "Quelle di tipo I tagliano entrambi i filamenti e richiedono ATP; quelle di tipo II tagliano un solo filamento",
  "Tutte introducono superavvolgimenti negativi nel DNA e richiedono l'idrolisi di una molecola di ATP a ogni ciclo",
  "Cambiano il numero di paia di basi del DNA circolare, lasciando invariato il suo numero di legame",
  "Quelle di tipo II tagliano un solo filamento e la DNA girasi introduce superavvolgimenti positivi",
  ], 0,
  "Tipo I: taglio di un filamento, Lk cambia di 1, senza ATP. Tipo II: taglio di entrambi, Lk cambia di 2; la DNA girasi batterica introduce superavvolgimenti negativi consumando ATP (Lehninger).",
  note="Errori nella sbobina (Biochimica I, p. 232 e 238): a p. 232 attribuisce a tutte le topoisomerasi l'introduzione di superavvolgimenti negativi con consumo di ATP (vale per la girasi, non per le topoisomerasi di tipo I, che rilassano il DNA senza ATP); a p. 238 scrive «le DNA polimerasi catalizzano la rottura di uno (tipo I) o di due (tipo II) legami fosfodiesterici»: si tratta delle topoisomerasi.")
q("u1121-033", T, "f", "232", "Perché il DNA umano deve essere compattato in cromatina?", [
  "Circa 2 m di DNA devono stare in un nucleo di circa 5 µm",
  "Circa 2 cm di DNA devono stare in un nucleo di circa 5 mm",
  "Circa 2 mm di DNA devono stare in un nucleo di circa 5 nm",
  "Circa 20 m di DNA devono stare in un nucleo di circa 5 mm",
  "Circa 2 µm di DNA devono stare in un nucleo di circa 5 nm",
  ], 0,
  "46 cromosomi × ~5 cm di DNA B ciascuno ≈ 2 m.",
  note="Errore nella sbobina (Biochimica I, p. 232): indica una cellula di 20 mm con un nucleo di 5 mm; le unità corrette sono micrometri (µm).")
q("u1121-034", T, "f", "233", "Quali istoni formano l'ottamero del nucleosoma?", [
  "H2A, H2B, H3 e H4, in due copie ciascuno",
  "H1, H2A, H2B e H3, in due copie ciascuno",
  "H1, H2A, H3 e H4, in due copie ciascuno",
  "H2A, H2B, H3 e H4, con quattro copie di H1",
  "H1 in otto copie, legato al DNA linker",
  ], 0,
  "L'ottamero è (H2A, H2B, H3, H4)₂; H1 sta all'esterno, dove il DNA entra ed esce dal nucleosoma.")
q("u1121-035", T, "m", "233", "Quale ruolo ha l'istone H1?", [
  "Lega il DNA dove entra ed esce dal nucleosoma e rende la cromatina più compatta",
  "Forma il core dell'ottamero intorno a cui il DNA si avvolge con circa due giri",
  "Acetila le lisine degli altri istoni per rendere la cromatina accessibile",
  "Taglia il DNA linker tra un nucleosoma e il successivo durante la mitosi",
  "Lega il DNA solo durante la duplicazione, insieme alle proteine SSB",
  ], 0,
  "Senza H1 i nucleosomi sono molto distanziati e la cromatina è meno compatta.")
q("u1121-036", T, "l", "233", "Come si avvolge il DNA intorno all'ottamero istonico?", [
  "In senso sinistrorso, con circa due giri",
  "In senso destrorso, con circa due giri",
  "In senso sinistrorso, con circa dieci giri",
  "In senso destrorso, con circa mezzo giro",
  "In senso destrorso, con circa dieci giri",
  ], 0,
  "Avvolgimento sinistrorso; il valore preciso è ~1,7 giri, circa 147 bp (Lehninger; la sbobina dice «due giri»).")

# ── Duplicazione del DNA (p. 234–241) ───────────────────────────────────────
T = "d13-duplicazione"
q("u1121-037", T, "m", "234", "Quale abbinamento enzima – funzione nella forcella replicativa è corretto?", [
  "Elicasi – separa i due filamenti della doppia elica",
  "Primasi – unisce i frammenti di Okazaki tra loro",
  "DNA ligasi – sintetizza i primer di RNA",
  "SSB – rimuove i superavvolgimenti davanti alla forcella",
  "Topoisomerasi – impedisce che i filamenti singoli si riappaino",
  ], 0,
  "Primasi = primer di RNA; ligasi = saldatura dei frammenti di Okazaki; topoisomerasi = superavvolgimenti; SSB = protezione del singolo filamento.")
q("u1121-038", T, "f", "234", "Quali attività hanno tutte e tre le DNA polimerasi di E. coli?", [
  "Polimerasi 5'→3' ed esonucleasi 3'→5'",
  "Polimerasi 3'→5' ed esonucleasi 5'→3'",
  "Polimerasi 5'→3' ed esonucleasi 5'→3'",
  "Polimerasi 5'→3' e attività primasica",
  "Polimerasi 3'→5' e attività elicasica",
  ], 0,
  "Tutte sintetizzano 5'→3' e correggono le bozze con l'esonucleasi 3'→5'; nessuna può iniziare senza primer.")
q("u1121-039", T, "m", "234", "A che cosa serve l'attività esonucleasica 3'→5' delle DNA polimerasi?", [
  "Correzione di bozze: rimuove il nucleotide sbagliato appena aggiunto",
  "Rimozione dei primer di RNA davanti al frammento di Okazaki",
  "Allungamento del filamento in ritardo nel verso opposto",
  "Taglio del DNA davanti alla forcella per eliminare i superavvolgimenti",
  "Saldatura dei frammenti di Okazaki con un legame fosfodiestere",
  ], 0,
  "L'enzima torna indietro di un passo (verso 3'→5') e idrolizza il legame fosfodiestere del nucleotide errato.")
q("u1121-040", T, "a", "235", "Quale attività possiede solo la DNA polimerasi I, e a che cosa le serve?", [
  "Esonucleasi 5'→3', per rimuovere i primer di RNA che trova davanti",
  "Esonucleasi 3'→5', per correggere i nucleotidi appena inseriti",
  "Primasi, per innescare i frammenti di Okazaki sul filamento lento",
  "Elicasi, per aprire la doppia elica all'origine di replicazione oriC",
  "Ligasi, per saldare i frammenti di Okazaki al filamento continuo",
  ], 0,
  "L'esonucleasi 5'→3' rimuove nucleotidi nel verso della sintesi: serve a togliere i primer (e tratti errati) e a sostituirli con DNA.")
q("u1121-041", T, "l", "235", "Quale dato indica che la replicasi di E. coli è la DNA polimerasi III e non la I?", [
  "È circa 50 volte più veloce, anche se ce ne sono solo 10–20 copie per cellula",
  "È presente in circa 400 copie per cellula, quindi molte più della polimerasi I",
  "È l'unica che può iniziare la sintesi senza primer, direttamente all'origine",
  "È l'unica con esonucleasi 5'→3', che le serve per rimuovere i primer",
  "È l'unica che polimerizza 3'→5' e può quindi copiare il filamento lento",
  ], 0,
  "In vitro: polimerasi III ~30.000 nucleotidi/min contro ~600 della I; 10–20 molecole di III per cellula contro 400 di I.",
  note="Errore nella sbobina (Biochimica I, p. 235): descrive la DNA polimerasi II come «un retaggio evolutivo» che avrebbe perso le sue funzioni. Secondo il Lehninger la polimerasi II è attiva e partecipa alla riparazione del DNA.")
q("u1121-042", T, "m", "236", "Quale subunità della DNA polimerasi III ne determina l'alta processività?", [
  "La subunità β, che forma un anello intorno al DNA",
  "La subunità α, che porta il sito attivo polimerasico",
  "La subunità ε, con l'attività esonucleasica 3'→5'",
  "La subunità θ, che fa parte del nucleo catalitico",
  "La subunità σ, che riconosce la sequenza dell'origine",
  ], 0,
  "Due subunità β formano una pinza ad anello che aggancia l'enzima al DNA. α, ε e θ formano il nucleo; σ è dell'RNA polimerasi.")
q("u1121-043", T, "f", "236", "Che cosa si intende per processività di una polimerasi?", [
  "Il numero di nucleotidi aggiunti prima che l'enzima si stacchi dal DNA",
  "Il numero di nucleotidi aggiunti in un secondo, in condizioni di saturazione",
  "La frazione di nucleotidi sbagliati corretti dall'esonucleasi 3'→5'",
  "Il numero di forcelle replicative servite insieme da un solo enzima",
  "La distanza tra l'origine e il punto in cui la duplicazione termina",
  ], 0,
  "Processività = nucleotidi aggiunti senza che la polimerasi si stacchi; nella polimerasi III la garantisce la pinza β.")
q("u1121-044", T, "a", "237", "Nell'inizio della duplicazione in E. coli, che cosa fa DnaA?", [
  "Lega le ripetizioni di 9 bp di oriC e fa denaturare le vicine sequenze di 13 bp ricche di A=T",
  "Scorre lungo la doppia elica come esamero e la svolge consumando ATP alla forcella replicativa",
  "Sintetizza i primer di RNA sulle sequenze di 13 bp ricche di G≡C dell'origine di replicazione",
  "Lega le ripetizioni di 13 bp e taglia un filamento per avviare la replicazione a cerchio rotante",
  "Carica la pinza β sul DNA e recluta la DNA polimerasi III sulle ripetizioni di 9 bp di oriC",
  ], 0,
  "Circa 20 DnaA con ATP legano le 4 ripetizioni di 9 bp; le 3 ripetizioni di 13 bp ricche di A=T si aprono; poi entrano gli esameri di DnaB, l'elicasi.",
  note="Imprecisione nella sbobina (Biochimica I, p. 237): chiama DnaA «elicasi». DnaA è la proteina di inizio (fattore di avvio, come la sbobina stessa dice poco dopo); l'elicasi replicativa è DnaB.")
q("u1121-045", T, "m", "237", "Perché le sequenze di 13 bp di oriC che si aprono per prime sono ricche di A=T?", [
  "Le coppie A=T hanno due legami a idrogeno e si separano più facilmente",
  "Le coppie A=T hanno tre legami a idrogeno e legano meglio la proteina DnaA",
  "Le coppie A=T sono riconosciute dalla primasi come sito di inizio dei primer",
  "Le coppie A=T vengono metilate e così si distinguono dal resto del cromosoma",
  "Le coppie A=T formano DNA Z sinistrorso, che si apre in modo spontaneo",
  ], 0,
  "Due legami a idrogeno contro i tre delle G≡C: le regioni A=T fondono più facilmente.")
q("u1121-046", T, "m", "239", "A che cosa servono le proteine SSB nella duplicazione?", [
  "Impediscono che i filamenti singoli si riappaino tra loro",
  "Aprono la doppia elica rompendo i legami a idrogeno tra le basi",
  "Rimuovono i superavvolgimenti positivi davanti alla forcella",
  "Legano la doppia elica neosintetizzata e la proteggono dalle nucleasi",
  "Sintetizzano brevi primer di RNA sul filamento in ritardo",
  ], 0,
  "Il singolo filamento tende a riassociarsi; le SSB legano solo il singolo filamento perché la loro tasca è troppo piccola per la doppia elica.")
q("u1121-047", T, "a", "238", "Perché il filamento in ritardo viene sintetizzato in frammenti di Okazaki?", [
  "La polimerasi sintetizza solo 5'→3' e quello stampo si apre nel verso opposto",
  "La polimerasi sintetizza solo 3'→5' e quello stampo si apre nello stesso verso",
  "Su quel filamento la primasi è più veloce della polimerasi e la precede",
  "Su quel filamento le SSB staccano la polimerasi ogni mille basi circa",
  "Quel filamento è più ricco in A=T e quindi si denatura solo a tratti",
  ], 0,
  "Sul filamento in ritardo la sintesi 5'→3' va in verso opposto all'avanzamento della forcella: si fa a pezzi, ognuno con il suo primer.")
q("u1121-048", T, "h", "238", "Come fa la DNA polimerasi III dimerica a copiare contemporaneamente i due filamenti?", [
  "Lo stampo del filamento in ritardo forma un'ansa, così entrambi vengono letti nello stesso verso di avanzamento",
  "La subunità catalitica del filamento in ritardo polimerizza 3'→5', così segue la forcella senza interruzioni",
  "Il filamento in ritardo viene copiato solo dopo che il filamento guida è stato completato fino al termine",
  "Le due subunità catalitiche si muovono in direzioni opposte, allontanandosi l'una dall'altra dall'origine",
  "La primasi sintetizza un unico primer lungo che copre tutto il filamento in ritardo fino alla forcella",
  ], 0,
  "Il filamento in ritardo «fa un giro di 180°» e si dispone nello stesso verso del filamento guida: il dimero procede insieme sui due stampi.")
q("u1121-049", T, "l", "240", "Quando un frammento di Okazaki è completato, che cosa succede alla pinza β?", [
  "Viene sfilata, e una nuova pinza caricata sul primer successivo riporta lì il core catalitico",
  "Resta sul frammento finito e trascina il core catalitico fino al primer successivo, senza staccarsi",
  "Viene degradata, e la polimerasi prosegue con bassa processività fino alla fine",
  "Passa al filamento guida, dove sostituisce la subunità ε nella correzione di bozze",
  "Si apre e lega la DNA ligasi, che salda subito il frammento a quello precedente",
  ], 0,
  "La pinza viene rilasciata e una nuova pinza, già posizionata, riassocia il core catalitico per il filamento in ritardo.")
q("u1121-050", T, "m", "241", "Che ruolo ha il PCNA nella DNA polimerasi δ eucariotica?", [
  "Lo stesso della subunità β di E. coli, la pinza che aumenta la processività",
  "Lo stesso della subunità α di E. coli, che porta il sito attivo polimerasico",
  "Lo stesso della subunità ε di E. coli, con l'esonucleasi di correzione",
  "Lo stesso della proteina DnaA di E. coli, che riconosce l'origine ori",
  "Lo stesso della proteina DnaB di E. coli, l'elicasi replicativa principale",
  ], 0,
  "PCNA (antigene nucleare di proliferazione cellulare) è altamente omologo alla subunità β.")
q("u1121-051", T, "l", "241", "Quale DNA polimerasi eucariotica ha localizzazione mitocondriale?", [
  "γ",
  "α",
  "δ",
  "ε",
  "β",
  ], 0,
  "Tutte le DNA polimerasi eucariotiche sono nucleari tranne la γ, che duplica il DNA mitocondriale.")
q("u1121-052", T, "h", "234", "Una mutazione elimina solo l'attività esonucleasica 3'→5' della DNA polimerasi III. Che cosa succede?", [
  "La duplicazione procede, ma il tasso di mutazione aumenta molto perché gli errori non vengono corretti",
  "La duplicazione si blocca, perché senza esonucleasi la polimerasi non riesce ad allungare la catena",
  "I primer di RNA non vengono più rimossi, quindi i frammenti di Okazaki restano tutti separati",
  "La processività crolla, perché è l'esonucleasi a tenere agganciato l'enzima al DNA stampo",
  "Il filamento guida diventa discontinuo e si formano frammenti di Okazaki su entrambi gli stampi",
  ], 0,
  "L'esonucleasi 3'→5' è la correzione di bozze: senza, la sintesi va avanti ma con molti più errori. I primer li toglie l'esonucleasi 5'→3' della polimerasi I; la processività dipende dalla pinza β.")
q("u1121-053", T, "h", "234", "Un ceppo di E. coli ha una DNA ligasi che non funziona a 42 °C. Che cosa si accumula a quella temperatura?", [
  "Frammenti di Okazaki non saldati sul filamento in ritardo",
  "Primer di RNA non rimossi all'inizio del filamento guida",
  "DNA superavvolto positivamente davanti alle due forcelle",
  "DNA a singolo filamento coperto di SSB su tutto il cromosoma",
  "Interruzioni ogni 1000–2000 nucleotidi sul filamento guida",
  ], 0,
  "La ligasi salda i frammenti di Okazaki (dopo che la polimerasi I ha sostituito i primer): senza ligasi restano interruzioni sul filamento in ritardo.")
