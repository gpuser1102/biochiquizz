/**
 * Biochiquiz – raccolta segnalazioni
 * Va incollato in Estensioni → Apps Script del foglio Google "Biochiquiz – Segnalazioni".
 * Ogni segnalazione inviata dall'app diventa una riga del foglio "Segnalazioni".
 */
const NOME_FOGLIO = 'Segnalazioni';
const INTESTAZIONI = ['Ricevuta', 'Telefono (codice)', 'ID segnalazione', 'Versione app', 'ID card', 'Argomento', 'Motivo', 'Nota',
  'Domanda', 'Opzioni', 'Risposta giusta (app)', 'Risposta data', 'Modalità', 'Sistema', 'Stato'];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const r = JSON.parse(e.postData.contents);
    const t = (v, n) => String(v == null ? '' : v).slice(0, n || 500);   // tronca, per sicurezza
    const foglio = prendiFoglio_();
    // niente doppioni se il telefono reinvia la stessa segnalazione
    const ids = foglio.getLastRow() > 1 ? foglio.getRange(2, 3, foglio.getLastRow() - 1, 1).getValues().flat() : [];
    if (ids.indexOf(t(r.reportId, 40)) === -1) {
      foglio.appendRow([new Date(), t(r.device, 20), t(r.reportId, 40), t(r.version, 20), t(r.cardId, 80), t(r.topic, 60), t(r.reason, 60),
        t(r.note, 800), t(r.question, 400), t((r.options || []).join(' | '), 600), t(r.correct, 200), t(r.given, 200),
        t(r.mode, 20), t(r.platform, 20), 'da rivedere']);
    }
    return ContentService.createTextOutput('{"ok":true}').setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput('Biochiquiz: raccolta segnalazioni attiva');
}

function prendiFoglio_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let f = ss.getSheetByName(NOME_FOGLIO);
  if (!f) {
    f = ss.insertSheet(NOME_FOGLIO);
    f.appendRow(INTESTAZIONI);
    f.setFrozenRows(1);
    f.getRange(1, 1, 1, INTESTAZIONI.length).setFontWeight('bold');
  }
  return f;
}
