# Sorgente di Biochiquiz

- `data/` – contenuti: argomenti, reazioni, vie metaboliche (`content.json`), domande verificate (`exam.json`), molecole con SMILES da PubChem (`molecules.json`).
- `src/` – app (HTML, CSS, JS).
- `build/` – script Python che generano i dati e assemblano l'app.
- `segnalazioni/` – codice Apps Script del foglio Google che riceve le segnalazioni.

Per rigenerare il sito (dalla cartella `sorgente/`):

    python3 build/exam_questions.py
    python3 build/build_molecules.py
    python3 build/build_app.py

Poi copiare il contenuto di `dist/pwa/` nella radice del repository. Gli ID delle card non vanno mai rinominati: sono la chiave dei progressi salvati sui telefoni.

La banca domande (`data/bank.json`) si rigenera con `python3 build/build_bank.py`. Le domande Hard (livello `h`, 5 opzioni, ragionate in stile esame) stanno in `build/bank_mh*.py` e sono le sole usate dalla Hard mode.

Regola sulle opzioni: la risposta giusta non deve essere riconoscibile dalla lunghezza. I distrattori devono avere lunghezza e struttura (es. «…, perché…») simili alla giusta. Le revisioni stanno in `build/opts_v2_*.py` e `build/opts_v3_*.py` (FIX = distrattori riscritti, OVERRIDE = correzioni, PATCH = singoli distrattori sostituiti). `build_bank.py` stampa la posizione della risposta giusta per lunghezza: «la più lunga» deve restare intorno al 20%.
