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
