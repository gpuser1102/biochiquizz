/**
 * Biochiquiz – segnalazioni e conteggio accessi
 * Va incollato in Estensioni → Apps Script del foglio Google "Biochiquiz – Segnalazioni".
 *
 * Fogli:
 *  - Segnalazioni: una riga per ogni errore segnalato dall'app
 *  - Utenti: una riga per telefono (codice casuale anonimo, nessun nome), con giorno e ora di prima e ultima visita
 *  - Giorni: per ogni giorno quanti telefoni hanno aperto l'app e quanti erano nuovi
 */
const FOGLI = {
  Segnalazioni: ['Ricevuta', 'Telefono (codice)', 'ID segnalazione', 'Versione app', 'ID card', 'Argomento', 'Motivo', 'Nota',
    'Domanda', 'Opzioni', 'Risposta giusta (app)', 'Risposta data', 'Modalità', 'Sistema', 'Stato'],
  Utenti: ['Telefono (codice)', 'Prima visita', 'Ultima visita', 'Giorni attivi', 'Versione app', 'Sistema', 'Installata'],
  Giorni: ['Giorno', 'Telefoni attivi', 'Nuovi telefoni'],
};
const FUSO = 'Europe/Rome';

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const r = JSON.parse(e.postData.contents);
    if (r.kind === 'ping') registraAccesso_(r); else registraSegnalazione_(r);
    return ContentService.createTextOutput('{"ok":true}').setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput('Biochiquiz: raccolta attiva');
}

const t_ = (v, n) => String(v == null ? '' : v).slice(0, n || 500);   // tronca, per sicurezza
// date scritte come testo (con l'apostrofo) così il foglio non le riformatta
const ora_ = () => "'" + Utilities.formatDate(new Date(), FUSO, 'yyyy-MM-dd HH:mm');
const oggi_ = () => "'" + Utilities.formatDate(new Date(), FUSO, 'yyyy-MM-dd');

function registraSegnalazione_(r) {
  const f = foglio_('Segnalazioni');
  // niente doppioni se il telefono reinvia la stessa segnalazione
  const ids = f.getLastRow() > 1 ? f.getRange(2, 3, f.getLastRow() - 1, 1).getValues().flat() : [];
  if (ids.indexOf(t_(r.reportId, 40)) !== -1) return;
  f.appendRow([ora_(), t_(r.device, 20), t_(r.reportId, 40), t_(r.version, 20), t_(r.cardId, 80), t_(r.topic, 60), t_(r.reason, 60),
    t_(r.note, 800), t_(r.question, 400), t_((r.options || []).join(' | '), 600), t_(r.correct, 200), t_(r.given, 200),
    t_(r.mode, 20), t_(r.platform, 20), 'da rivedere']);
}

function registraAccesso_(r) {
  const dev = t_(r.device, 20);
  if (!/^T-[A-Z0-9]{4,10}$/.test(dev)) return;
  const giorno = oggi_().slice(1);
  const u = foglio_('Utenti');
  const codici = u.getLastRow() > 1 ? u.getRange(2, 1, u.getLastRow() - 1, 1).getValues().flat().map(String) : [];
  const i = codici.indexOf(dev);
  const installata = r.standalone ? 'sì' : 'no';
  let nuovo = false, primoOggi = false;
  if (i === -1) {
    nuovo = primoOggi = true;
    u.appendRow([dev, ora_(), ora_(), 1, t_(r.version, 20), t_(r.platform, 20), installata]);
  } else {
    const riga = i + 2;
    const ultima = String(u.getRange(riga, 3).getValue()).slice(0, 10);
    if (ultima !== giorno) {
      primoOggi = true;
      u.getRange(riga, 4).setValue(Number(u.getRange(riga, 4).getValue() || 0) + 1);
    }
    u.getRange(riga, 3).setValue(ora_());   // giorno e ora dell'ultimo accesso
    u.getRange(riga, 5, 1, 3).setValues([[t_(r.version, 20), t_(r.platform, 20), installata]]);
  }
  if (!primoOggi) return;
  const g = foglio_('Giorni');
  const giorni = g.getLastRow() > 1 ? g.getRange(2, 1, g.getLastRow() - 1, 1).getValues().flat().map(x => String(x).slice(0, 10)) : [];
  const j = giorni.indexOf(giorno);
  if (j === -1) g.appendRow([oggi_(), 1, nuovo ? 1 : 0]);
  else {
    const riga = j + 2;
    g.getRange(riga, 2).setValue(Number(g.getRange(riga, 2).getValue() || 0) + 1);
    if (nuovo) g.getRange(riga, 3).setValue(Number(g.getRange(riga, 3).getValue() || 0) + 1);
  }
}

function foglio_(nome) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let f = ss.getSheetByName(nome);
  if (!f) {
    f = ss.insertSheet(nome);
    f.appendRow(FOGLI[nome]);
    f.setFrozenRows(1);
    f.getRange(1, 1, 1, FOGLI[nome].length).setFontWeight('bold');
  }
  return f;
}
