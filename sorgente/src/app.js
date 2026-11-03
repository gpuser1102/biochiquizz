/* Biochiquiz — logica dell'app. Dati in window.BQ_DATA = {molecules, content}. */
(function () {
  "use strict";
  const D = window.BQ_DATA;
  const MOL = Object.fromEntries(D.molecules.map(m => [m.id, m]));
  const C = D.content;
  // Indirizzo della web app di Google Apps Script che scrive le segnalazioni nel foglio Google.
  // Vuoto = le segnalazioni restano sul telefono e si possono copiare da Altro.
  const REPORT_URL = "";
  const REPORT_KEY = "bq.reports";
  const STORE_KEY = "bq.v1";
  const $ = (s, el = document) => el.querySelector(s);
  const h = (tag, attrs = {}, ...kids) => {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (v == null || v === false) continue;
      if (k === "class") el.className = v;
      else if (k === "html") el.innerHTML = v;
      else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
      else el.setAttribute(k, v === true ? "" : v);
    }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid.nodeType ? kid : document.createTextNode(kid));
    return el;
  };
  const ICON = {
    feed: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="4"/><path d="M9 9h6M9 13h4"/></svg>',
    topics: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h2M4 12h2M4 18h2M10 6h10M10 12h10M10 18h10"/></svg>',
    stats: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 20V11M12 20V5M19 20v-6"/></svg>',
    info: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></svg>',
    check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    chev: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>',
    down: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg>',
    flag: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V4M5 4h11l-2 4 2 4H5"/></svg>',
    flask: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 006.2 21.5h11.6a2 2 0 001.7-3L14 9V3"/><path d="M7.5 15h9"/></svg>',
    star: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>',
    hex: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3l7.8 4.5v9L12 21l-7.8-4.5v-9z"/></svg>',
    rxn: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h14M13 8l4 4-4 4"/><path d="M20 6v12"/></svg>',
    path: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="5" r="2"/><circle cx="18" cy="19" r="2"/><path d="M6 7v4a4 4 0 004 4h4a4 4 0 014 4"/></svg>',
    share: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M8 7l4-4 4 4"/><path d="M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"/></svg>',
    dots: '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>',
    book: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2z"/><path d="M4 19V5M8 7h7"/></svg>',
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 019.5 4a8 8 0 1010.5 10.5z"/></svg>',
    board: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21l4-4 4 4M7 9h6M7 12h9"/></svg>',
    pen: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>',
  };
  ICON.flame = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 01-10 0c0-2.2 1-3.7 2-4.8.3 1.8 1.2 2.8 2.3 2.8C11 8.5 11 6 12 3z"/></svg>';
  const svgIcon = n => { const s = h("span", { html: ICON[n] }); return s.firstChild; };

  /* ---------------- Stato locale ---------------- */
  const blank = () => ({ selected: [], lastChecked: null, onlyLast: false, mode: "write", theme: "system", welcomed: false, newPerDay: 20, device: "", levels: { f: true, m: true, a: true, l: true }, progressive: true, study: "", hardStats: {}, cards: {}, days: {} });
  let S = blank();
  try { const raw = localStorage.getItem(STORE_KEY); if (raw) S = Object.assign(blank(), JSON.parse(raw)); } catch (e) { /* storage non disponibile */ }
  // dal vecchio sistema a scatole: quelle card ripartono come nuove
  Object.keys(S.cards).forEach(k => { if (!S.cards[k].type) delete S.cards[k]; });
  // modalità di studio: graduale (sblocco al 70%), libera (scegli i livelli), hard (solo domande toste, si scrive)
  if (!["grad", "free", "hard"].includes(S.study)) S.study = S.progressive === false ? "free" : "grad";
  if (!S.hardStats) S.hardStats = {};
  // codice casuale del telefono: raggruppa le segnalazioni della stessa persona senza sapere chi è
  if (!S.device) S.device = "T-" + Math.random().toString(36).slice(2, 6).toUpperCase() + Math.random().toString(36).slice(2, 4).toUpperCase();
  const save = () => { try { localStorage.setItem(STORE_KEY, JSON.stringify(S)); } catch (e) { } };

  /* ---------------- Argomenti ---------------- */
  const TOPICS = {};
  C.topics.forEach(sub => sub.blocks.forEach(b => b.topics.forEach(t => { TOPICS[t.id] = Object.assign({ subject: sub.subject, block: b.name }, t); })));

  /* ---------------- Mazzo di card ---------------- */
  const CARDS = [];
  D.molecules.forEach(m => CARDS.push({ id: "mol:" + m.id, kind: "mol", mol: m.id, topics: C.moleculeTopics[m.id] || [], level: "f" }));
  C.reactions.forEach(r => CARDS.push({ id: "rx:" + r.id, kind: "rx", rx: r, topics: [r.topic], level: "m" }));
  (C.exam || []).forEach(x => CARDS.push({ id: "ex:" + x.id, kind: "ex", ex: x, topics: [x.topic], level: x.level || "m" }));
  (C.bank || []).forEach(x => CARDS.push({ id: "q:" + x.id, kind: "ex", ex: x, bank: true, topics: [x.topic], level: x.level }));
  C.pathways.forEach(p => p.steps.forEach((st, i) => CARDS.push({ id: `nx:${p.id}:${i}`, kind: "nx", path: p, step: st, idx: i, topics: [st.topic || p.topic], level: "m" })));
  const CARD = Object.fromEntries(CARDS.map(c => [c.id, c]));

  const activeTopics = () => {
    if (S.onlyLast && S.lastChecked && S.selected.includes(S.lastChecked)) return [S.lastChecked];
    return S.selected.filter(t => TOPICS[t] && TOPICS[t].ready);
  };
  /* ---------------- Livelli ----------------
     Facile → Medio → Alta → 30 e lode. In modalità progressiva, per ogni argomento il livello successivo si sblocca
     quando almeno il 70% delle card del livello precedente è stato imparato (passato in ripasso). */
  const LEVELS = ["f", "m", "a", "l"];
  const LEVEL_NAME = { f: "Facile", m: "Medio", a: "Alta", l: "30 e lode", h: "Hard" };
  const STUDY_NAME = { grad: "Graduale", free: "Libera", hard: "Hard mode" };
  const isHard = () => S.study === "hard";
  // in hard mode: domande Alta e 30 e lode (anche verificate) + molecole e reazioni da scrivere senza opzioni
  const inHard = c => c.kind === "mol" || c.kind === "rx" || (c.kind === "ex" && (c.level === "a" || c.level === "l"));
  const UNLOCK = 0.7;
  const learned = c => { const x = S.cards[c.id]; return !!x && (x.type === "review" || (x.type === "relearn")); };
  function topicLevelState(tid) {
    const cs = CARDS.filter(c => c.topics.includes(tid));
    const by = {}; LEVELS.forEach(l => { const a = cs.filter(c => c.level === l); by[l] = { n: a.length, ok: a.filter(learned).length }; });
    let open = 0; // indice del livello più alto sbloccato
    for (let i = 0; i < LEVELS.length - 1; i++) {
      const cur = by[LEVELS[i]];
      if (cur.n === 0 || cur.ok / cur.n >= UNLOCK) open = i + 1; else break;
    }
    return { by, open };
  }
  const levelAllowed = (c, unlockCache) => {
    if (isHard()) return inHard(c);
    if (!S.levels[c.level]) return false;
    if (S.study !== "grad") return true;
    return c.topics.some(t => { const st = unlockCache[t] || (unlockCache[t] = topicLevelState(t)); return LEVELS.indexOf(c.level) <= st.open; });
  };
  const eligible = () => {
    const a = new Set(activeTopics()), cache = {};
    return CARDS.filter(c => c.topics.some(t => a.has(t)) && levelAllowed(c, cache));
  };
  const cardsInTopic = id => CARDS.filter(c => c.topics.includes(id)).length;
  const topicMeta = id => {
    if (isHard()) { const n = CARDS.filter(c => c.topics.includes(id) && inHard(c)).length; return `${n} card in hard mode`; }
    if (S.study !== "grad") return `${cardsInTopic(id)} card`;
    const st = topicLevelState(id);
    return `${cardsInTopic(id)} card · ${LEVEL_NAME[LEVELS[st.open]]}`;
  };

  /* ---------------- Ripetizione spaziata: algoritmo SM-2 ----------------
     Card nuove → passi di apprendimento (1 min, 10 min) → ripasso a giorni con intervallo × facilità.
     Errore su una card imparata = "lapse": facilità −20%, intervallo azzerato a 1 giorno, ripasso tra 10 min.
     La giornata inizia alle 4 di mattina. */
  const MIN = 60e3, HOUR = 36e5, DAY = 864e5;
  const CFG = { learn: [1 * MIN, 10 * MIN], relearn: [10 * MIN], gradIvl: 1, easyIvl: 4, startEase: 2.5, minEase: 1.3,
    easyBonus: 1.3, hardMult: 1.2, learnAhead: 20 * MIN, leech: 8, mature: 21, hardRelearn: [1 * MIN, 10 * MIN] };
  const dayStart = t => { const d = new Date(t - 4 * HOUR); d.setHours(4, 0, 0, 0); return d.getTime(); };
  const today = () => { const d = new Date(dayStart(Date.now())); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
  const newState = () => ({ type: "new", step: 0, ease: CFG.startEase, ivl: 0, due: 0, lapses: 0, right: 0, wrong: 0, seen: 0 });
  const fuzz = ivl => { if (ivl < 3) return ivl; const f = Math.max(1, Math.round(ivl * .05)); return ivl + Math.round((Math.random() * 2 - 1) * f); };
  // r: 1 = Di nuovo, 2 = Difficile, 3 = Buono, 4 = Facile
  function schedule(st, r, now, noFuzz) {
    const fz = noFuzz ? x => x : fuzz;
    if (st.type !== "review") {
      const relearning = st.type === "relearn";
      const steps = relearning ? (isHard() ? CFG.hardRelearn : CFG.relearn) : CFG.learn;
      if (st.type === "new") st.type = "learn";
      if (r === 1) { st.step = 0; st.due = now + steps[0]; return; }
      if (r === 2) { const cur = steps[st.step] || steps[0], nxt = steps[st.step + 1]; st.due = now + (nxt ? (cur + nxt) / 2 : cur * 1.5); return; }
      if (r === 3 && st.step + 1 < steps.length) { st.step++; st.due = now + steps[st.step]; return; }
      if (!relearning) st.ivl = r === 4 ? CFG.easyIvl : CFG.gradIvl;
      st.type = "review"; st.step = 0; st.due = dayStart(now) + st.ivl * DAY; return;
    }
    if (r === 1) { const hd = isHard(); st.lapses++; st.ease = Math.max(CFG.minEase, st.ease - (hd ? .25 : .2)); st.ivl = 1; st.type = "relearn"; st.step = 0; st.due = now + (hd ? CFG.hardRelearn[0] : CFG.relearn[0]); return; }
    let ivl;
    if (r === 2) { ivl = Math.max(st.ivl + 1, st.ivl * CFG.hardMult); st.ease = Math.max(CFG.minEase, st.ease - .15); }
    else if (r === 3) ivl = Math.max(st.ivl + 1, st.ivl * st.ease);
    else { ivl = Math.max(st.ivl + 1, st.ivl * st.ease * CFG.easyBonus); st.ease += .15; }
    st.ivl = fz(Math.round(ivl)); st.due = dayStart(now) + st.ivl * DAY;
  }
  const pendingNew = new Set(); // card nuove già messe nel feed ma non ancora risposte
  function grade(id, r, extra) {
    const prev = S.cards[id] ? Object.assign({}, S.cards[id]) : null;
    const now = Date.now();
    const wasNew = !prev || prev.type === "new";
    const apply = rr => {
      const st = Object.assign(newState(), prev || {});
      st.seen++; st.last = now; if (rr === 1) st.wrong++; else st.right++;
      // ripasso extra (card non ancora in scadenza): solo gli errori spostano la programmazione
      if (!(extra && rr > 1)) schedule(st, rr, now);
      st.leech = st.lapses >= CFG.leech;
      S.cards[id] = st;
    };
    apply(r);
    if (isHard() && CARD[id]) CARD[id].topics.forEach(t => { const x = S.hardStats[t] = S.hardStats[t] || { n: 0, ok: 0 }; x.n++; if (r > 1) x.ok++; });
    pendingNew.delete(id);
    const d = today(); S.days[d] = S.days[d] || { n: 0, ok: 0, new: 0 }; S.days[d].n++; if (r > 1) S.days[d].ok++; if (wasNew) S.days[d].new = (S.days[d].new || 0) + 1;
    save();
    return {
      extra, rating: r,
      regrade(rr) { this.rating = rr; apply(rr); save(); },
      preview(rr) { if (extra && rr > 1) return null; const st = Object.assign(newState(), prev || {}); schedule(st, rr, now, true); return st.due - now; },
    };
  }
  const fmtIvl = ms => {
    if (ms == null) return "";
    if (ms < HOUR) return `${Math.max(1, Math.round(ms / MIN))} min`;
    if (ms < DAY * .9) return `${Math.round(ms / HOUR)} h`;
    const d = Math.round(ms / DAY);
    if (d < 30) return d === 1 ? "domani" : `${d} g`;
    return `${(d / 30).toFixed(d < 300 ? 1 : 0).replace(".", ",")} mesi`;
  };
  let shown = 0, recent = [], extraMode = false, doneShown = false;
  const newToday = () => ((S.days[today()] || {}).new || 0) + pendingNew.size;
  function pickNext() {
    const pool = eligible(); if (!pool.length) return null;
    const now = Date.now();
    const fresh = c => !recent.includes(c.id);
    const st = c => S.cards[c.id];
    const learning = c => st(c) && (st(c).type === "learn" || st(c).type === "relearn");
    const byDue = (a, b) => st(a).due - st(b).due;
    let l = pool.filter(c => fresh(c) && learning(c) && st(c).due <= now).sort(byDue);
    if (l.length) return { c: l[0] };
    const rv = pool.filter(c => fresh(c) && st(c) && st(c).type === "review" && st(c).due <= now).sort(byDue);
    if (rv.length) return { c: rv[0] };
    if (newToday() < S.newPerDay) {
      let nw = pool.filter(c => fresh(c) && !pendingNew.has(c.id) && (!st(c) || st(c).type === "new"));
      if (!isHard()) {
        const minLv = Math.min(...nw.map(c => LEVELS.indexOf(c.level)));
        nw = nw.filter(c => LEVELS.indexOf(c.level) === minLv);
      }
      if (nw.length) { const c = nw[Math.floor(Math.random() * nw.length)]; pendingNew.add(c.id); return { c }; }
    }
    l = pool.filter(c => fresh(c) && learning(c) && st(c).due <= now + CFG.learnAhead).sort(byDue);
    if (l.length) return { c: l[0] };
    if (extraMode) {
      // ripasso extra: più probabili le card con facilità bassa o molti errori
      const list = pool.filter(c => fresh(c) && st(c));
      const src = list.length ? list : pool.filter(fresh).length ? pool.filter(fresh) : pool;
      const w = src.map(c => st(c) ? (3.2 - st(c).ease) + st(c).lapses * .5 + (st(c).wrong > st(c).right ? 1 : 0) + .2 : 1);
      let x = Math.random() * w.reduce((a, b) => a + b, 0);
      for (let i = 0; i < src.length; i++) { x -= w[i]; if (x <= 0) return { c: src[i], extra: true }; }
      return { c: src[src.length - 1], extra: true };
    }
    return { done: true };
  }

  /* ---------------- Utilità ---------------- */
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const sample = (arr, n, not = []) => shuffle(arr.filter(x => !not.includes(x))).slice(0, n);
  const norm = s => s.toLowerCase().replace(/α/g, "alfa").replace(/β/g, "beta").normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/\bacido\s+/g, "").replace(/[^a-z0-9]/g, "");
  const digits = s => s.replace(/[^0-9]/g, "");
  function lev(a, b) {
    const m = a.length, n = b.length; if (Math.abs(m - n) > 2) return 9;
    let prev = Array.from({ length: n + 1 }, (_, j) => j);
    for (let i = 1; i <= m; i++) { const cur = [i]; for (let j = 1; j <= n; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); prev = cur; }
    return prev[n];
  }
  function matchName(input, mol) {
    const x = norm(input); if (!x) return false;
    const cands = [mol.name, ...mol.aliases].map(norm);
    if (cands.includes(x)) return true;
    // tolleranza sui refusi solo se i numeri coincidono (2-PG ≠ 3-PG)
    return cands.some(c => c.length >= 6 && digits(c) === digits(x) && lev(c, x) <= (c.length >= 12 ? 2 : 1));
  }
  const molName = id => MOL[id].name;
  // nomi lunghi (enzimi): tollera qualche refuso, ignora le parentesi
  function matchText(input, answer) {
    const x = norm(input); if (!x) return false;
    const cands = [answer, answer.replace(/\s*\(.*?\)/g, "")].map(norm);
    if (cands.includes(x)) return true;
    return cands.some(c => c.length >= 6 && digits(c) === digits(x) && lev(c, x) <= (c.length >= 20 ? 3 : c.length >= 12 ? 2 : 1));
  }
  // casella per scrivere la risposta (hard mode)
  function writeBox(c, placeholder, test, onDone) {
    const inp = h("input", { type: "text", id: "ans-" + c.id.replace(/\W/g, "-") + "-" + shown, placeholder, autocomplete: "off", autocapitalize: "off", spellcheck: "false", enterkeyhint: "done", "aria-label": placeholder });
    const go = h("button", { class: "btn btn-primary", type: "button" }, "Verifica");
    const form = h("div", { class: "write" }, inp, go);
    const check = () => {
      if (!inp.value.trim()) { inp.focus(); return; }
      const ok = test(inp.value); inp.disabled = go.disabled = true; inp.blur();
      form.classList.add(ok ? "right" : "wrong");
      onDone(ok, form);
    };
    go.addEventListener("click", check);
    inp.addEventListener("keydown", e => { if (e.key === "Enter") check(); });
    return form;
  }
  const subjectOf = topic => ((TOPICS[topic] || {}).subject || "Biochimica II");
  const ref = (subject, page) => page ? `Riferimento: sbobina di ${subject}, p. ${page}` : null;
  // "dal glucosio", "dall'ossalacetato", "sull'1,3-bisfosfoglicerato"
  const prep = (p, id) => { const n = molName(id).toLowerCase(); return /^[aeiou1]|^8|^11/.test(n) ? `${p}ll'${n}` : `${p}l ${n}`; };
  const ALL_ENZYMES = [...new Set([...C.reactions.map(r => r.enzyme), ...C.pathways.flatMap(p => p.steps.map(s => s.enzyme)), ...C.extraEnzymes])];
  const topicLabel = c => { const t = TOPICS[c.topics.find(x => activeTopics().includes(x)) || c.topics[0]]; return t ? t.name : ""; };
  let toastTimer;
  function toast(msg) {
    let t = $(".toast"); if (!t) { t = h("div", { class: "toast", role: "status" }); document.body.append(t); }
    t.textContent = msg; t.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => t.hidden = true, 2600);
  }

  /* ---------------- Disegno delle molecole ---------------- */
  const isDark = () => document.documentElement.dataset.theme === "dark" ||
    (document.documentElement.dataset.theme !== "light" && matchMedia("(prefers-color-scheme: dark)").matches);
  const molInk = () => getComputedStyle(document.documentElement).getPropertyValue("--mol-ink").trim() || "#222";
  const SVGNS = "http://www.w3.org/2000/svg";
  const svgEl = (tag, a) => { const e = document.createElementNS(SVGNS, tag); for (const k in a) e.setAttribute(k, a[k]); return e; };

  function drawHaworth(m) {
    const hw = m.haworth, ink = molInk();
    const W = 380, H = 236, X = 20;
    const svg = svgEl("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": "Struttura in proiezione di Haworth" });
    const pyr = hw.size === 6;
    // vertici: [O, C anomerico, ... ] in senso orario visto dall'alto
    const P = pyr
      ? { O: [218 + X, 84], ring: [[262 + X, 120], [222 + X, 158], [128 + X, 158], [86 + X, 120], [124 + X, 84]] }
      : { O: [170 + X, 74], ring: [[250 + X, 116], [214 + X, 160], [126 + X, 160], [90 + X, 116]] };
    const verts = [P.O, ...P.ring];
    const front = pyr ? [[1, 2], [2, 3], [3, 4]] : [[1, 2], [2, 3], [3, 4]];
    for (let i = 0; i < verts.length; i++) {
      const a = verts[i], b = verts[(i + 1) % verts.length];
      const isFront = front.some(([x, y]) => (i === x && (i + 1) % verts.length === y));
      svg.append(svgEl("line", { x1: a[0], y1: a[1], x2: b[0], y2: b[1], stroke: ink, "stroke-width": isFront ? 6 : 2, "stroke-linecap": "round" }));
    }
    const txt = (x, y, s, anchor = "middle", size = 16, weight = 600) => {
      const t = svgEl("text", { x, y, "text-anchor": anchor, "font-size": size, "font-weight": weight, fill: ink, "font-family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" });
      t.textContent = s; return t;
    };
    // O dell'anello su fondo pieno per interrompere le linee
    svg.append(svgEl("circle", { cx: P.O[0], cy: P.O[1], r: 11, fill: getComputedStyle(document.documentElement).getPropertyValue("--surface-2").trim() }));
    svg.append(txt(P.O[0], P.O[1] + 6, "O", "middle", 17, 700));
    const L = 34;
    hw.positions.forEach((pos, i) => {
      const [x, y] = P.ring[i];
      const cnum = hw.firstC + i;
      // numerazione del carbonio, discreta, all'interno dell'anello
      const cx = (pyr ? 175 : 170) + X, cy = 124;
      const nx = x + (cx - x) * .2, ny = y + (cy - y) * .2 + 4;
      const n = txt(nx, ny, String(cnum), "middle", 10, 600); n.setAttribute("opacity", ".55"); svg.append(n);
      const sub = (lbl, dir) => {
        if (!lbl) return;
        const y2 = y + dir * L;
        svg.append(svgEl("line", { x1: x, y1: y, x2: x, y2: y2 + (dir < 0 ? 6 : -6), stroke: ink, "stroke-width": 2, "stroke-linecap": "round" }));
        const isH = lbl === "H";
        let anchor = "middle", dx = 0;
        if (lbl.length > 3) { anchor = x < 190 ? "end" : "start"; dx = x < 190 ? 12 : -12; }
        svg.append(txt(x + dx, dir < 0 ? y2 - 2 : y2 + 14, lbl, anchor, isH ? 14 : 16, isH ? 500 : 600));
      };
      sub(pos.up, -1); sub(pos.down, 1);
    });
    return svg;
  }

  // Formula condensata verticale (stile Lehninger): una riga per carbonio
  function drawFischer(m) {
    const rows = m.fischer, ink = molInk();
    const FS = 21, STEP = 58, TOP = 30, CX = 190, CW = 7.2, BOND = 26, GAP = 5;
    const H = TOP * 2 + (rows.length - 1) * STEP + 8;
    const svg = svgEl("svg", { viewBox: `0 0 380 ${H}`, role: "img", "aria-label": "Formula di struttura condensata" });
    const font = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";
    const text = (x, y, s, anchor) => { const t = svgEl("text", { x, y, "text-anchor": anchor, "font-size": FS, "font-weight": 600, fill: ink, "font-family": font }); t.textContent = s; return t; };
    const line = (x1, y1, x2, y2) => svgEl("line", { x1, y1, x2, y2, stroke: ink, "stroke-width": 2, "stroke-linecap": "round" });
    const hbond = (x1, x2, y, order) => {
      if (order === 2) { svg.append(line(x1, y - 3.5, x2, y - 3.5), line(x1, y + 3.5, x2, y + 3.5)); }
      else svg.append(line(x1, y, x2, y));
    };
    rows.forEach((r, i) => {
      const y = TOP + i * STEP, base = y + FS * .36;
      svg.append(text(CX - CW, base, r.c, "start"));
      if (r.l) { const x1 = CX - CW - GAP, x2 = x1 - BOND; hbond(x1, x2, y, r.lb); svg.append(text(x2 - GAP, base, r.l, "end")); }
      if (r.r) { const x1 = CX + CW + GAP, x2 = x1 + BOND; hbond(x1, x2, y, r.rb); svg.append(text(x2 + GAP, base, r.r, "start")); }
      if (r.down) {
        const y1 = y + FS * .62, y2 = y + STEP - FS * .62;
        if (r.down === 2) svg.append(line(CX - 3.5, y1, CX - 3.5, y2), line(CX + 3.5, y1, CX + 3.5, y2));
        else svg.append(line(CX, y1, CX, y2));
      }
    });
    return svg;
  }
  function molBox(id) {
    const m = MOL[id];
    const box = h("div", { class: "mol-box", "data-mol": id });
    box.append(h("div", { class: "mol-tag" }, m.haworth ? "Haworth" : "Formula condensata"));
    box.append(m.haworth ? drawHaworth(m) : drawFischer(m));
    return box;
  }
  function redrawMolecules() {
    document.querySelectorAll(".mol-box[data-mol]").forEach(box => box.replaceWith(molBox(box.dataset.mol)));
  }

  /* ---------------- Card ---------------- */
  /* ---------------- Segnalazioni ---------------- */
  const REASONS = ["Risposta sbagliata", "Spiegazione sbagliata o poco chiara", "Formula o struttura sbagliata", "Domanda ambigua", "Errore di battitura", "Altro"];
  const loadReports = () => { try { return JSON.parse(localStorage.getItem(REPORT_KEY) || "[]"); } catch (e) { return []; } };
  const saveReports = r => { try { localStorage.setItem(REPORT_KEY, JSON.stringify(r)); } catch (e) { } };
  let sending = false;
  // conteggio anonimo degli accessi: al massimo un segnale al giorno, solo codice casuale, versione e sistema
  async function pingUsage() {
    if (!REPORT_URL || !navigator.onLine) return;
    const d = today(); if (S.lastPing === d) return;
    try {
      await fetch(REPORT_URL, { method: "POST", mode: "no-cors", headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify({ kind: "ping", device: S.device, version: C.version, platform: platform(), standalone: standalone() }) });
      S.lastPing = d; save();
    } catch (e) { }
  }
  async function flushReports() {
    if (!REPORT_URL || sending || !navigator.onLine) return;
    sending = true;
    try {
      for (const r of loadReports().filter(x => !x.sent)) {
        try {
          // text/plain evita il preflight CORS; la risposta è opaca ma la richiesta arriva
          await fetch(REPORT_URL, { method: "POST", mode: "no-cors", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(r) });
          const all = loadReports(); const x = all.find(y => y.reportId === r.reportId); if (x) { x.sent = Date.now(); saveReports(all); }
        } catch (e) { break; }
      }
    } finally { sending = false; }
  }
  function cardSnapshot(card, cardId) {
    const c = CARD[cardId] || {};
    const opts = [...card.querySelectorAll(".opt-label")].map(x => x.textContent);
    const right = card.querySelector(".opt.right .opt-label"), wrong = card.querySelector(".opt.wrong .opt-label");
    const inp = card.querySelector(".write input");
    let correct = right ? right.textContent : "", given = wrong ? wrong.textContent : right ? right.textContent : "";
    if (c.kind === "mol") correct = MOL[c.mol].name;
    if (inp && inp.value) given = inp.value;
    const q = card.querySelector(".q");
    return { cardId, topic: (c.topics || [])[0] || "", question: (q ? q.textContent : "") + (c.kind === "mol" ? ` [${MOL[c.mol].name}]` : ""), options: opts, correct, given: card.classList.contains("answered") ? given : "" };
  }
  function openReport(card, cardId) {
    const snap = cardSnapshot(card, cardId);
    let reason = null;
    const overlay = h("div", { class: "sheet-wrap", role: "dialog", "aria-modal": "true", "aria-label": "Segnala un errore" });
    const close = () => overlay.remove();
    overlay.addEventListener("click", e => { if (e.target === overlay) close(); });
    const chips = h("div", { class: "chips" });
    const send = h("button", { class: "btn btn-primary", type: "button", disabled: true }, "Invia");
    REASONS.forEach(r => {
      const b = h("button", { type: "button", class: "chip", "aria-pressed": "false" }, r);
      b.addEventListener("click", () => { reason = r; chips.querySelectorAll(".chip").forEach(x => x.setAttribute("aria-pressed", String(x === b))); send.disabled = false; });
      chips.append(b);
    });
    const note = h("textarea", { id: "report-note", rows: "3", maxlength: "800", placeholder: "Cosa non torna? Se puoi, scrivi la versione giusta e la pagina della sbobina." });
    const err = h("div", { class: "field-err", role: "alert" }); err.hidden = true;
    send.addEventListener("click", () => {
      const r = Object.assign({ reportId: Date.now().toString(36) + Math.random().toString(36).slice(2, 7), ts: new Date().toISOString(), version: C.version, device: S.device, reason, note: note.value.trim(),
        mode: S.mode, platform: platform() }, snap);
      const all = loadReports(); all.push(r); saveReports(all);
      close();
      toast(REPORT_URL ? (navigator.onLine ? "Segnalazione inviata, grazie" : "Segnalazione salvata: parte appena sei online") : "Segnalazione salvata sul telefono");
      flushReports();
    });
    overlay.append(h("div", { class: "sheet" },
      h("div", { class: "sheet-grip", "aria-hidden": "true" }),
      h("div", { class: "row-title", style: "font-size:18px" }, "Segnala un errore"),
      h("div", { class: "row-sub" }, snap.question.length > 110 ? snap.question.slice(0, 108) + "…" : snap.question),
      h("div", { class: "h2", style: "margin:4px 0 0" }, "Che tipo di errore?"), chips,
      h("label", { class: "h2", for: "report-note", style: "margin:4px 0 0" }, "Dettagli (facoltativo)"), note,
      err,
      h("div", { class: "sheet-btns" }, h("button", { class: "btn btn-ghost", type: "button", onclick: close }, "Annulla"), send)));
    document.body.append(overlay);
  }
  function reportLink(cardId) {
    const a = h("button", { class: "report", type: "button" }, svgIcon("flag"), "Segnala errore");
    a.addEventListener("click", () => openReport(a.closest(".card"), cardId));
    return a;
  }
  function shell(c, kicker, tileClass, icon) {
    const card = h("article", { class: "card" + (isHard() ? " hard" : ""), "data-card": c.id });
    const body = h("div", { class: "card-body" });
    body.append(h("div", { class: "card-head" },
      h("div", { class: "tile " + tileClass }, svgIcon(icon)),
      h("div", { style: "flex:1;min-width:0" }, h("div", { class: "card-kicker" }, kicker), h("div", { class: "card-topic" }, topicLabel(c))),
      isHard() && (c.kind === "mol" || c.kind === "rx") ? h("span", { class: "lv lv-h" }, "Hard")
        : c.level ? h("span", { class: "lv lv-" + c.level }, LEVEL_NAME[c.level]) : null));
    const foot = h("div", { class: "card-foot" }, reportLink(c.id), h("span", { class: "next-hint" }, "Scorri", svgIcon("down")));
    card.append(body, foot);
    return { card, body };
  }
  function noteEl(text) { return h("div", { class: "note" }, h("div", {}, h("b", {}, "⚠ Sbobina · "), text)); }
  // Feedback a pop-up: si apre dalla risposta toccata e si sovrappone un po' alle opzioni sotto
  function finish(card, anchor, ok, text, meta, note, g) {
    card.classList.add("answered");
    const last = false;
    let rate = null;
    if (g && ok && !g.extra) {
      // dopo una risposta giusta puoi dire quanto è stata facile (Buono è già applicato)
      rate = h("div", { class: "rate", role: "group", "aria-label": "Quanto è stata facile" });
      [[2, "Difficile"], [3, "Buono"], [4, "Facile"]].forEach(([r, l]) => {
        const b = h("button", { type: "button", class: "rate-b", "aria-pressed": String(r === 3) }, h("span", {}, l), h("small", {}, fmtIvl(g.preview(r))));
        b.addEventListener("click", e => { e.stopPropagation(); g.regrade(r); rate.querySelectorAll(".rate-b").forEach(x => x.setAttribute("aria-pressed", String(x === b))); });
        rate.append(b);
      });
    }
    const when = g && !ok ? `Torna tra ${fmtIvl(g.preview(1))}` : g && g.extra ? "Ripasso extra: la programmazione non cambia" : null;
    const pop = h("div", { class: "pop " + (ok ? "ok" : "ko") + (last ? " up" : ""), role: "status" },
      h("div", { class: "pop-verdict" }, ok ? "Giusto" : "Sbagliato"),
      text ? h("div", { class: "pop-text" }, text) : null,
      meta ? h("div", { class: "pop-meta" }, meta) : null,
      when ? h("div", { class: "pop-meta" }, when) : null,
      note ? (/^Sbobina /.test(note)
        ? h("div", { class: "pop-note" }, h("b", {}, "⚠ " + note.split(":")[0] + ":"), note.slice(note.indexOf(":") + 1))
        : h("div", { class: "pop-note info" }, h("b", {}, "Nota · "), note)) : null,
      rate);
    anchor.classList.add("has-pop");
    anchor.append(pop);
    // sotto la risposta se c'è spazio nella card, altrimenti sopra
    const body = card.querySelector(".card-body");
    if (body) {
      const pr = pop.getBoundingClientRect(), br = body.getBoundingClientRect(), ar = anchor.getBoundingClientRect();
      if (pr.bottom > br.bottom - 4 && ar.top - br.top > br.bottom - ar.bottom) pop.classList.add("up");
    }
  }
  function optionList(opts, correct, onDone) {
    const wrap = h("div", { class: "options", role: "group" });
    opts.forEach((o, i) => {
      const b = h("button", { class: "opt", type: "button" }, h("span", { class: "key" }, "ABCDE"[i]), h("span", { class: "opt-label" }, o));
      b.addEventListener("click", () => {
        const ok = o === correct;
        wrap.querySelectorAll(".opt").forEach(x => { x.disabled = true; if (x.querySelector(".opt-label").textContent === correct) x.classList.add("right"); });
        if (!ok) b.classList.add("wrong");
        onDone(ok, b);
      });
      wrap.append(b);
    });
    return wrap;
  }

  function molCard(c) {
    const m = MOL[c.mol];
    const { card, body } = shell(c, "Riconosci la molecola", "t-rose", "hex");
    body.append(h("h2", { class: "q" }, "Che molecola è?"), molBox(m.id));
    const detail = `${m.formula} · PubChem CID ${m.cid}`;
    const done = (ok, anchor) => { const g = grade(c.id, ok ? 3 : 1, c.extra); finish(card, anchor, ok, ok ? m.name : `È ${m.name}.`, detail, null, g); };
    const others = D.molecules.filter(x => x.id !== m.id && (C.moleculeTopics[x.id] || []).some(t => c.topics.includes(t))).map(x => x.name);
    const pool = others.length >= 4 ? others : D.molecules.filter(x => x.id !== m.id).map(x => x.name);
    const opts = shuffle([m.name, ...sample(pool, 4)]);
    const showOptions = () => body.append(optionList(opts, m.name, done));
    if (S.mode === "choice" && !isHard()) showOptions();
    else {
      const inp = h("input", { type: "text", id: "ans-" + c.id.replace(/\W/g, "-") + "-" + shown, placeholder: "Scrivi il nome (va bene anche la sigla)", autocomplete: "off", autocapitalize: "off", spellcheck: "false", enterkeyhint: "done", "aria-label": "Nome della molecola" });
      const go = h("button", { class: "btn btn-primary", type: "button" }, "Verifica");
      const form = h("div", { class: "write" }, inp, go);
      const help = h("button", { class: "linkish", type: "button" }, "Non mi viene: mostra 5 opzioni");
      const check = () => {
        if (!inp.value.trim()) { inp.focus(); return; }
        const ok = matchName(inp.value, m); inp.disabled = go.disabled = true; help.remove(); inp.blur();
        form.classList.add(ok ? "right" : "wrong");
        done(ok, form);
      };
      go.addEventListener("click", check);
      inp.addEventListener("keydown", e => { if (e.key === "Enter") check(); });
      help.addEventListener("click", () => { form.remove(); help.remove(); showOptions(); });
      if (isHard()) { body.append(form); help.remove(); } else body.append(form, help);
    }
    return card;
  }

  // Domanda specifica in base a cosa manca nella reazione
  function rxQuestion(r, hid) {
    if (hid.kind === "enz") return "Quale enzima catalizza questa reazione?";
    if (hid.kind === "co") return "Quale coenzima usa questo enzima?";
    const left = hid.side === "left", v = hid.val;
    if (hid.kind === "mol") {
      const sameSide = (left ? r.left : r.right).filter(x => x[0] === "m").length;
      if (left) return sameSide > 1 ? "Quale altro substrato manca?" : "Qual è il substrato di questa reazione?";
      return sameSide > 1 ? "Qual è l'altro prodotto della scissione?" : "Qual è il prodotto di questa reazione?";
    }
    const Q = {
      "ATP": left ? "Quale nucleotide cede il fosfato?" : "Quale nucleotide si forma?",
      "GTP": left ? "Quale nucleotide cede il fosfato?" : "Quale nucleotide si forma?",
      "ADP": left ? "Quale nucleotide accetta il fosfato?" : "Quale nucleotide resta dopo il trasferimento del fosfato?",
      "GDP": left ? "Quale nucleotide accetta il fosfato?" : "Quale nucleotide resta dopo il trasferimento del fosfato?",
      "NAD⁺": left ? "Quale coenzima accetta gli elettroni (si riduce)?" : "In che forma torna il coenzima dopo aver ceduto gli elettroni?",
      "NADH + H⁺": left ? "Quale coenzima cede gli elettroni (si ossida)?" : "In che forma esce il coenzima ridotto?",
      "Pi": left ? "Cosa viene incorporato nel prodotto senza consumare ATP?" : "Cosa viene liberato dall'idrolisi?",
      "H₂O": left ? "Quale molecola serve per l'idrolisi?" : "Quale molecola viene eliminata?",
      "CO₂": "Cosa viene liberato con la decarbossilazione?",
      "HCO₃⁻": "Da dove viene il carbonio aggiunto al piruvato?",
    };
    if (v === "ATP" && left && r.left.some(x => x[1] === "HCO₃⁻")) return "Quale nucleotide viene idrolizzato per attivare il bicarbonato?";
    return Q[v] || "Cosa manca per completare la reazione?";
  }
  const eqText = r => {
    const t = x => x[0] === "m" ? molName(x[1]) : x[1];
    return `${r.left.map(t).join(" + ")} ${r.irreversible ? "→" : "⇌"} ${r.right.map(t).join(" + ")}`;
  };
  function rxCard(c) {
    const r = c.rx;
    const { card, body } = shell(c, "Completa la reazione", "t-peach", "rxn");
    // elementi nascondibili: molecole, cofattori, enzima, coenzima
    const slots = [];
    r.left.forEach((x, i) => slots.push({ side: "left", i, kind: x[0] === "m" ? "mol" : "cof", val: x[1] }));
    r.right.forEach((x, i) => slots.push({ side: "right", i, kind: x[0] === "m" ? "mol" : "cof", val: x[1] }));
    slots.push({ kind: "enz", val: r.enzyme });
    if (r.coenzyme) slots.push({ kind: "co", val: r.coenzyme });
    // in hard mode si nasconde solo una molecola o l'enzima, e la risposta va scritta
    const hidable = isHard() ? slots.filter(s => s.kind === "mol" || s.kind === "enz") : slots;
    const hid = hidable[Math.floor(Math.random() * hidable.length)];
    const question = rxQuestion(r, hid);
    const label = s => s.kind === "mol" ? molName(s.val) : s.val;
    const answer = label(hid);
    const patch = h("span", { class: "patch" }, "?");
    const side = (arr, sideName) => {
      const row = h("div", { class: "rx-side" });
      arr.forEach((x, i) => {
        if (i) row.append(h("span", { class: "rx-plus" }, "+"));
        const isHid = hid.side === sideName && hid.i === i;
        row.append(isHid ? patch : h("span", { class: "rx-item" + (x[0] === "c" ? " cof" : "") }, x[0] === "m" ? molName(x[1]) : x[1]));
      });
      return row;
    };
    const enz = hid.kind === "enz" ? patch : h("span", { class: "enz" }, r.enzyme);
    const co = r.coenzyme ? h("span", { class: "co" }, "coenzima: ", hid.kind === "co" ? patch : r.coenzyme) : null;
    const where = r.where ? h("span", { class: "co" }, "sede: ", r.where) : null;
    body.append(
      h("h2", { class: "q" }, question),
      h("div", { class: "rx" }, side(r.left, "left"),
        h("div", { class: "rx-arrow" }, h("span", { class: "stem" + (r.irreversible ? "" : " rev"), "aria-label": r.irreversible ? "irreversibile" : "reversibile" }), h("div", { class: "rx-enz" }, enz, co, where)),
        side(r.right, "right")));
    let pool;
    if (hid.kind === "mol") pool = D.molecules.map(m => m.name);
    else if (hid.kind === "enz") pool = ALL_ENZYMES;
    else pool = C.cofactorPool;
    const present = slots.filter(s => s !== hid).map(label);
    const opts = shuffle([answer, ...sample(pool, 4, [answer, ...present])]);
    let note = r.note || null;
    if (hid.kind === "enz" && r.enzymeNotInNotes && !note) note = "Il nome dell'enzima non è nelle sbobine.";
    const done = (ok, btn) => {
      const g = grade(c.id, ok ? 3 : 1, c.extra);
      patch.textContent = answer; patch.classList.add("revealed"); if (!ok) patch.classList.add("miss");
      finish(card, btn, ok, `${r.enzyme}: ${eqText(r)}`, ref(subjectOf(r.topic), r.page), note, g);
    };
    if (isHard()) body.append(writeBox(c, hid.kind === "mol" ? "Scrivi il nome della molecola" : "Scrivi il nome dell'enzima",
      v => hid.kind === "mol" ? matchName(v, MOL[hid.val]) : matchText(v, answer), done));
    else body.append(optionList(opts, answer, done));
    return card;
  }

  function nxCard(c) {
    const p = c.path, st = c.step;
    const { card, body } = shell(c, "Cosa succede dopo", "t-sage", "path");
    const askEnzyme = Math.random() < .4;
    const where = st.where ? ` ${st.where}` : "";
    const withTxt = st.with ? ` (insieme al ${MOL[st.with].name.toLowerCase()})` : "";
    const pathName = p.name.charAt(0).toUpperCase() + p.name.slice(1);
    body.append(
      h("h2", { class: "q" }, askEnzyme
        ? `${pathName}: quale enzima agisce ${prep("su", st.from)}${where}?`
        : `${pathName}: cosa si forma ${prep("da", st.from)}${withTxt}${where}?`),
      molBox(st.from));
    const answer = askEnzyme ? st.enzyme : st.to.map(molName).join(" + ");
    let pool;
    if (askEnzyme) pool = ALL_ENZYMES;
    else {
      const inPath = [...new Set(p.steps.flatMap(s => [s.from, ...s.to]))].map(molName);
      pool = [...new Set([...inPath, ...D.molecules.map(m => m.name)])];
      if (st.to.length > 1) pool = ["2 Piruvato", "Glucosio 6-fosfato + Pi", "Fosfoenolpiruvato + Gliceraldeide 3-fosfato", "Diidrossiacetone fosfato + 3-fosfoglicerato", "2 Gliceraldeide 3-fosfato + ATP"];
    }
    const opts = shuffle([answer, ...sample(pool, 4, [answer, molName(st.from)])]);
    body.append(optionList(opts, answer, (ok, btn) => {
      const g = grade(c.id, ok ? 3 : 1, c.extra);
      const full = `${molName(st.from)} → ${st.to.map(molName).join(" + ")} · ${st.enzyme}`;
      const tp = st.topic || p.topic;
      finish(card, btn, ok, full, [ok ? null : `Risposta giusta: ${answer}`, ref(subjectOf(tp), (TOPICS[tp] || {}).pages)].filter(Boolean).join(" · ") || null, st.note || null, g);
    }));
    return card;
  }

  // Domanda verificata (proposta a lezione): opzioni nell'ordine originale (alcune rimandano alle altre: "Tutte e tre", "Nessuno")
  function examCard(c) {
    const x = c.ex;
    const kicker = c.bank ? (x.level === "l" ? "Rifinitura da 30 e lode" : "Domanda") : (x.times > 1 ? `Domanda verificata · uscita ${x.times} volte` : "Domanda verificata");
    const { card, body } = shell(c, kicker, c.bank ? (x.level === "l" ? "t-lilac" : "t-rose") : "t-sky", c.bank ? (x.level === "l" ? "star" : "hex") : "board");
    const qEl = h("h2", { class: "q ex-q" });
    // evidenzia le negazioni, come si fa a penna sul compito
    x.q.split(/(\bnon\b|\bfalsa\b|\btranne\b)/i).forEach(part => qEl.append(/^(non|falsa|tranne)$/i.test(part) ? h("u", {}, part) : part));
    body.append(qEl);
    const correct = x.opts[x.ans];
    const opts = c.bank && !x.fixed ? shuffle(x.opts) : x.opts;
    const letter = "ABCDE"[opts.indexOf(correct)];
    body.append(optionList(opts, correct, (ok, btn) => {
      const g = grade(c.id, ok ? 3 : 1, c.extra);
      finish(card, btn, ok, ok ? x.why : `Risposta: ${letter}. ${x.why}`, x.page ? ref(x.src || subjectOf(x.topic), x.page) : "Non è nelle sbobine", x.note, g);
    }));
    return card;
  }

  /* ---------------- Feed ---------------- */
  const feed = () => $("#feed");
  function emptyFeed() {
    const f = feed(); f.innerHTML = "";
    const any = Object.values(TOPICS).some(t => t.ready);
    f.append(h("div", { class: "empty" }, h("div", { class: "box" },
      h("div", { class: "tile t-lilac" }, svgIcon("topics")),
      h("div", { class: "row-title" }, "Scegli cosa ripassare"),
      h("div", { class: "lead" }, any ? "Spunta gli argomenti che hai già studiato: le domande usciranno solo da quelli." : "Nessun argomento disponibile."),
      h("button", { class: "btn btn-primary", type: "button", onclick: () => go("topics") }, "Vai agli argomenti"))));
  }
  function doneSlide() {
    const pool = eligible();
    const next = pool.map(c => S.cards[c.id]).filter(Boolean).filter(x => x.type !== "new").map(x => x.due).sort((a, b) => a - b)[0];
    const d = S.days[today()] || { n: 0, ok: 0 };
    const extraBtn = h("button", { class: "btn btn-ghost", type: "button" }, "Ripasso extra");
    extraBtn.addEventListener("click", () => { extraMode = true; doneShown = false; extraBtn.disabled = true; if (appendSlide()) setTimeout(() => feed().scrollBy({ top: feed().clientHeight, behavior: "smooth" }), 50); });
    return h("article", { class: "card done-card" }, h("div", { class: "card-body", style: "justify-content:center;align-items:center;text-align:center" },
      h("div", { class: "tile t-sage", style: "width:56px;height:56px;border-radius:18px" }, svgIcon("check")),
      h("h2", { class: "q" }, "Per oggi hai finito"),
      h("p", { class: "lead" }, `${d.n} risposte oggi, ${d.n ? Math.round(d.ok / d.n * 100) : 0}% giuste. ` + (next ? `Prossimo ripasso: tra ${fmtIvl(next - Date.now())}.` : "")),
      h("p", { class: "lead", style: "font-size:13px" }, `Card nuove: ${Math.min(newToday(), S.newPerDay)}/${S.newPerDay} oggi. Il limite si cambia in Altro.`),
      extraBtn));
  }
  function appendSlide() {
    const pick = pickNext(); if (!pick) return false;
    if (pick.done) {
      if (doneShown) return false;
      doneShown = true; feed().append(h("section", { class: "slide" }, doneSlide())); return true;
    }
    doneShown = false;
    const c = Object.assign({}, pick.c, { extra: !!pick.extra });
    shown++; recent.push(c.id); if (recent.length > Math.min(4, Math.max(1, eligible().length - 1))) recent.shift();
    const el = c.kind === "mol" ? molCard(c) : c.kind === "rx" ? rxCard(c) : c.kind === "ex" ? examCard(c) : nxCard(c);
    feed().append(h("section", { class: "slide" }, el));
    fitCard(el);
    return true;
  }
  function fitCard(card) {
    requestAnimationFrame(() => {
      const b = card.querySelector(".card-body"); if (!b || !b.clientHeight) return;
      if (b.scrollHeight > b.clientHeight + 2) card.classList.add("tight");
    });
  }
  /* ---------------- Modalità di studio ---------------- */
  const MODE_INFO = {
    grad: "Parti dalle domande facili. In ogni argomento il livello successivo si sblocca quando hai imparato il 70% di quello prima.",
    free: "Scegli tu quali livelli includere, tutti già sbloccati.",
    hard: "Solo domande Alta e 30 e lode, comprese quelle verificate. Molecole e reazioni si scrivono senza opzioni, e se sbagli la domanda torna dopo un minuto.",
  };
  function setStudy(v) {
    S.study = v; S.progressive = v === "grad"; save(); renderModebar(); resetFeed();
    if (!$("#view-info").hidden) renderInfo();
    if (!$("#view-topics").hidden) renderTopics();
  }
  function levelChips() {
    const chips = h("div", { class: "chips" });
    LEVELS.forEach(l => {
      const b = h("button", { type: "button", class: "chip lv-chip lvc-" + l, "aria-pressed": String(!!S.levels[l]) }, LEVEL_NAME[l]);
      b.addEventListener("click", () => {
        const next = !S.levels[l];
        if (!next && LEVELS.filter(x => S.levels[x]).length === 1) { toast("Lascia attivo almeno un livello"); return; }
        S.levels[l] = next; b.setAttribute("aria-pressed", String(next)); save(); resetFeed();
      });
      chips.append(b);
    });
    return chips;
  }
  function studyPicker(onPick) {
    const list = h("div", { class: "mode-list", role: "group", "aria-label": "Modalità di studio" });
    ["grad", "free", "hard"].forEach(v => {
      const b = h("button", { type: "button", class: "mode-opt", "aria-pressed": String(S.study === v) },
        h("div", { class: "tile " + ({ grad: "t-sage", free: "t-sky", hard: "t-peach" })[v] }, svgIcon(({ grad: "path", free: "topics", hard: "flame" })[v])),
        h("div", { class: "row-text" }, h("div", { class: "row-title" }, STUDY_NAME[v]), h("div", { class: "row-sub" }, MODE_INFO[v])));
      b.addEventListener("click", () => onPick(v));
      list.append(b);
    });
    return list;
  }
  function openModeSheet(focusLevels) {
    const overlay = h("div", { class: "sheet-wrap", role: "dialog", "aria-modal": "true", "aria-label": "Modalità di studio" });
    const close = () => overlay.remove();
    overlay.addEventListener("click", e => { if (e.target === overlay) close(); });
    const draw = () => {
      const sheet = h("div", { class: "sheet" }, h("div", { class: "sheet-grip", "aria-hidden": "true" }),
        h("div", { class: "row-title", style: "font-size:18px" }, "Come vuoi studiare?"),
        studyPicker(v => { setStudy(v); if (v === "free") draw(); else close(); }));
      if (S.study === "free") sheet.append(h("div", { class: "h2", style: "margin:4px 0 0" }, "Livelli inclusi"), levelChips());
      sheet.append(h("div", { class: "sheet-btns" }, h("button", { class: "btn btn-ghost", type: "button", onclick: close }, "Fatto")));
      overlay.innerHTML = ""; overlay.append(sheet);
    };
    draw(); document.body.append(overlay);
  }
  function renderModebar() {
    const bar = $("#modebar"); if (!bar) return; bar.innerHTML = "";
    const seg = h("div", { class: "seg", role: "group", "aria-label": "Modalità di studio" },
      ...["grad", "free", "hard"].map(v => {
        const b = h("button", { type: "button", class: v === "hard" ? "hard-b" : "", "aria-pressed": String(S.study === v) },
          v === "hard" ? svgIcon("flame") : null, v === "free" && S.study === "free" ? "Libera ▾" : v === "hard" ? "Hard" : STUDY_NAME[v]);
        b.addEventListener("click", () => { if (v === S.study) openModeSheet(); else { setStudy(v); if (v === "free") openModeSheet(); else toast(STUDY_NAME[v] + (v === "hard" ? ": solo domande toste" : ": livelli a sblocco")); } });
        return b;
      }));
    bar.append(seg);
  }
  function resetFeed() {
    shown = 0; recent = []; extraMode = false; doneShown = false; pendingNew.clear();
    const f = feed(); f.innerHTML = ""; f.scrollTop = 0;
    if (!eligible().length) { emptyFeed(); return; }
    appendSlide(); appendSlide();
  }
  function onFeedScroll() {
    const f = feed(); const slides = f.querySelectorAll(".slide"); if (!slides.length) return;
    const idx = Math.round(f.scrollTop / f.clientHeight);
    if (idx >= slides.length - 2) appendSlide();
  }

  /* ---------------- Argomenti ---------------- */
  function renderTopics() {
    const root = $("#topics-inner"); root.innerHTML = "";
    const last = S.lastChecked && TOPICS[S.lastChecked];
    root.append(h("h1", { class: "h1" }, "Argomenti"),
      h("p", { class: "lead" }, "Spunta quello che hai già studiato. Le domande escono solo da qui."));
    const onlyLast = h("input", { type: "checkbox", id: "only-last", role: "switch", "aria-label": "Solo l'ultimo argomento spuntato" });
    onlyLast.checked = !!S.onlyLast;
    onlyLast.addEventListener("change", () => { S.onlyLast = onlyLast.checked; save(); resetFeed(); });
    root.append(h("div", { class: "box" }, h("div", { class: "switch-row" },
      h("div", { class: "tile t-sky" }, svgIcon("pen")),
      h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Solo l'ultimo spuntato"), h("div", { class: "row-sub" }, last ? last.name : "Nessun argomento spuntato")),
      h("label", { class: "switch" }, onlyLast, h("span")))));
    const tiles = ["t-rose", "t-peach", "t-sage", "t-sky", "t-lilac"];
    C.topics.forEach(sub => {
      root.append(h("div", { class: "h2" }, sub.subject));
      if (!sub.blocks.length) { root.append(h("div", { class: "box" }, h("div", { class: "row" }, h("div", { class: "tile t-lilac" }, svgIcon("book")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "In preparazione"), h("div", { class: "row-sub" }, "Arriva dopo Biochimica II"))))); return; }
      const box = h("div", { class: "box" });
      sub.blocks.forEach((b, bi) => {
        const readyN = b.topics.filter(t => t.ready).length;
        const selN = b.topics.filter(t => S.selected.includes(t.id)).length;
        const head = h("button", { class: "row block-head", type: "button", "aria-expanded": readyN ? "true" : "false" },
          h("div", { class: "tile " + tiles[bi % tiles.length] }, h("span", { style: "font-weight:800;font-size:15px" }, String(bi + 1))),
          h("div", { class: "row-text" }, h("div", { class: "row-title" }, b.name),
            h("div", { class: "row-sub" }, `p. ${b.pages} · ${readyN ? `${selN}/${readyN} spuntati` : "domande in arrivo"}`)),
          h("span", { class: "chev", html: ICON.chev }));
        const list = h("div", { class: "topics" }); list.hidden = !readyN;
        head.addEventListener("click", () => { list.hidden = !list.hidden; head.setAttribute("aria-expanded", String(!list.hidden)); });
        b.topics.forEach(t => {
          const id = "tp-" + t.id;
          if (!t.ready) { list.append(h("div", { class: "topic soon" }, h("span", { class: "check" }), h("span", { class: "tname" }, t.name), h("span", { class: "tmeta" }, "presto"))); return; }
          const cb = h("input", { type: "checkbox", id });
          cb.checked = S.selected.includes(t.id);
          cb.addEventListener("change", () => {
            S.selected = S.selected.filter(x => x !== t.id);
            if (cb.checked) { S.selected.push(t.id); S.lastChecked = t.id; }
            else if (S.lastChecked === t.id) S.lastChecked = S.selected[S.selected.length - 1] || null;
            save(); renderTopics(); resetFeed();
          });
          const isNew = t.added && (Date.now() - new Date(t.added).getTime()) < 14 * DAY;
          list.append(h("label", { class: "topic", for: id }, cb, h("span", { class: "check", html: ICON.check }),
            h("span", { class: "tname" }, t.name), isNew ? h("span", { class: "badge new" }, "nuovo") : null, h("span", { class: "tmeta" }, topicMeta(t.id))));
        });
        box.append(head, list);
      });
      root.append(box);
    });
  }

  /* ---------------- Statistiche ---------------- */
  function renderStats() {
    const root = $("#stats-inner"); root.innerHTML = "";
    const pool = eligible(), now = Date.now(), eod = dayStart(now) + DAY;
    const st = Object.values(S.cards);
    const tot = st.reduce((a, s) => a + s.seen, 0), ok = st.reduce((a, s) => a + s.right, 0);
    const dueToday = pool.filter(c => S.cards[c.id] && S.cards[c.id].type !== "new" && S.cards[c.id].due < eod).length;
    const dayKeys = new Set(Object.keys(S.days));
    let streak = 0;
    for (let t = dayStart(now); ; t -= DAY) {
      const d = new Date(t), k = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
      if (dayKeys.has(k)) streak++; else if (t !== dayStart(now)) break;
      if (streak > 999) break;
    }
    const nd = (S.days[today()] || {}).new || 0;
    root.append(h("h1", { class: "h1" }, "Statistiche"), h("p", { class: "lead" }, "Salvate solo su questo telefono."),
      h("div", { class: "stats-grid" },
        h("div", { class: "stat" }, h("div", { class: "num" }, String(dueToday)), h("div", { class: "lbl" }, "da ripassare oggi")),
        h("div", { class: "stat" }, h("div", { class: "num" }, `${Math.min(nd, S.newPerDay)}/${S.newPerDay}`), h("div", { class: "lbl" }, "nuove oggi")),
        h("div", { class: "stat" }, h("div", { class: "num" }, String(streak)), h("div", { class: "lbl" }, streak === 1 ? "giorno di fila" : "giorni di fila")),
        h("div", { class: "stat" }, h("div", { class: "num" }, String(tot)), h("div", { class: "lbl" }, "risposte in tutto")),
        h("div", { class: "stat" }, h("div", { class: "num" }, tot ? Math.round(ok / tot * 100) + "%" : "–"), h("div", { class: "lbl" }, "corrette")),
        h("div", { class: "stat" }, h("div", { class: "num" }, String(st.filter(s => s.leech).length)), h("div", { class: "lbl" }, "ostiche"))));
    root.append(h("div", { class: "h2" }, "Per argomento"));
    const box = h("div", { class: "box" });
    Object.values(TOPICS).filter(t => t.ready).forEach(t => {
      const cs = CARDS.filter(c => c.topics.includes(t.id));
      const s_ = c => S.cards[c.id];
      const mature = cs.filter(c => s_(c) && s_(c).type === "review" && s_(c).ivl >= CFG.mature).length;
      const young = cs.filter(c => s_(c) && s_(c).type !== "new" && !(s_(c).type === "review" && s_(c).ivl >= CFG.mature)).length;
      const nnew = cs.length - mature - young;
      const ls = topicLevelState(t.id);
      const lvRow = h("div", { class: "lv-row" }, ...LEVELS.filter(l => ls.by[l].n).map((l, i) => h("span", { class: "lv lv-" + l + (S.study === "grad" && LEVELS.indexOf(l) > ls.open ? " locked" : "") }, `${LEVEL_NAME[l]} ${ls.by[l].ok}/${ls.by[l].n}`)));
      const hs = S.hardStats[t.id];
      if (hs && hs.n) lvRow.append(h("span", { class: "lv lv-h" }, `Hard ${Math.round(hs.ok / hs.n * 100)}% su ${hs.n}`));
      box.append(h("div", { class: "row" }, h("div", { class: "row-text" },
        h("div", { class: "row-title" }, t.name), lvRow,
        h("div", { class: "row-sub" }, `${nnew} nuove · ${young} in studio · ${mature} mature`),
        h("div", { class: "bar two", "aria-hidden": "true" },
          h("i", { style: `width:${Math.round(mature / cs.length * 100)}%` }),
          h("i", { class: "young", style: `width:${Math.round(young / cs.length * 100)}%` })))));
    });
    root.append(box);
    const weak = Object.entries(S.cards).filter(([id, s]) => CARD[id] && (s.lapses > 0 || s.wrong > 0))
      .sort((a, b) => (b[1].lapses - a[1].lapses) || (a[1].ease - b[1].ease) || (b[1].wrong - a[1].wrong)).slice(0, 6);
    if (weak.length) {
      root.append(h("div", { class: "h2" }, "Da rinforzare"));
      const wb = h("div", { class: "box" });
      weak.forEach(([id, s]) => {
        const c = CARD[id];
        const name = c.kind === "mol" ? MOL[c.mol].name : c.kind === "rx" ? c.rx.enzyme : c.kind === "ex" ? (c.ex.q.length > 70 ? c.ex.q.slice(0, 68) + "…" : c.ex.q) : `${MOL[c.step.from].name} → ${c.step.to.map(molName).join(" + ")}`;
        wb.append(h("div", { class: "row" }, h("div", { class: "tile " + ({ mol: "t-rose", rx: "t-peach", ex: "t-sky" }[c.kind] || "t-sage") }, svgIcon({ mol: "hex", rx: "rxn", ex: "board" }[c.kind] || "path")),
          h("div", { class: "row-text" }, h("div", { class: "row-title" }, name),
            h("div", { class: "row-sub" }, `${s.wrong} errori · facilità ${Math.round(s.ease * 100)}%` + (s.leech ? " · ostica" : "")))));
      });
      root.append(wb);
    }
    root.append(h("p", { class: "lead", style: "font-size:13px" }, `Le card "mature" sono quelle con intervallo di almeno ${CFG.mature} giorni. Una card diventa "ostica" dopo ${CFG.leech} errori su card già imparate.`));
  }


  /* ---------------- Info e impostazioni ---------------- */
  function platform() {
    const ua = navigator.userAgent;
    const ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
    return ios ? "ios" : /Android/.test(ua) ? "android" : "other";
  }
  const standalone = () => matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
  function installSteps(pf) {
    const steps = h("div", { class: "box steps" });
    const S_ = (...k) => steps.append(h("div", { class: "step" }, h("div", {}, ...k)));
    if (pf === "ios") {
      S_("Apri questa pagina in ", h("b", {}, "Safari"), ".");
      S_("Tocca ", h("b", {}, "Condividi "), h("span", { class: "inline-ico", html: ICON.share }), " in basso (su iPad è in alto).");
      S_("Scorri e scegli ", h("b", {}, "Aggiungi alla schermata Home"), ", poi ", h("b", {}, "Aggiungi"), ".");
      S_("Apri l'app dall'icona: parte a schermo intero e funziona anche offline.");
    } else if (pf === "android") {
      S_("Apri questa pagina in ", h("b", {}, "Chrome"), ".");
      S_("Tocca il menu ", h("span", { class: "inline-ico", html: ICON.dots }), " in alto a destra.");
      S_("Scegli ", h("b", {}, "Installa app"), " oppure ", h("b", {}, "Aggiungi a schermata Home"), ".");
      S_("Apri l'app dall'icona: parte a schermo intero e funziona anche offline.");
    } else {
      S_("Apri questo link dal telefono.");
      S_("Su iPhone usa Safari → Condividi → Aggiungi alla schermata Home. Su Android usa Chrome → menu ⋮ → Installa app.");
    }
    return steps;
  }
  let deferredPrompt = null;
  window.addEventListener("beforeinstallprompt", e => { e.preventDefault(); deferredPrompt = e; });
  function renderInfo() {
    const root = $("#info-inner"); root.innerHTML = "";
    root.append(h("h1", { class: "h1" }, "Impostazioni"));
    const modeSeg = h("div", { class: "seg", role: "group", "aria-label": "Modalità risposta" },
      ...[["write", "Scrivo il nome"], ["choice", "Scelta multipla"]].map(([v, l]) => {
        const b = h("button", { type: "button", "aria-pressed": String(S.mode === v) }, l);
        b.addEventListener("click", () => { S.mode = v; save(); renderInfo(); });
        return b;
      }));
    const themeSeg = h("div", { class: "seg", role: "group", "aria-label": "Tema" },
      ...[["system", "Sistema"], ["light", "Chiaro"], ["dark", "Scuro"]].map(([v, l]) => {
        const b = h("button", { type: "button", "aria-pressed": String(S.theme === v) }, l);
        b.addEventListener("click", () => { S.theme = v; save(); applyTheme(); renderInfo(); });
        return b;
      }));
    const newSeg = h("div", { class: "seg", role: "group", "aria-label": "Card nuove al giorno" },
      ...[10, 20, 30, 50].map(v => {
        const b = h("button", { type: "button", "aria-pressed": String(S.newPerDay === v) }, String(v));
        b.addEventListener("click", () => { S.newPerDay = v; save(); renderInfo(); resetFeed(); });
        return b;
      }));
    root.append(h("div", { class: "box" },
      h("div", { class: "row" }, h("div", { class: "tile t-rose" }, svgIcon("hex")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Riconosci la molecola"), h("div", { class: "row-sub" }, "Come vuoi rispondere"))),
      h("div", { style: "padding:0 12px 12px" }, modeSeg),
      h("div", { class: "row" }, h("div", { class: "tile t-lilac" }, svgIcon("moon")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Tema"))),
      h("div", { style: "padding:0 12px 12px" }, themeSeg),
      h("div", { class: "row" }, h("div", { class: "tile t-peach" }, svgIcon("feed")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Card nuove al giorno"), h("div", { class: "row-sub" }, "I ripassi in scadenza vengono sempre prima"))),
      h("div", { style: "padding:0 12px 12px" }, newSeg)));

    root.append(h("div", { class: "h2" }, "Modalità di studio"));
    const lvBox = h("div", { class: "box", style: "padding:12px" }, studyPicker(v => setStudy(v)));
    if (S.study === "free") lvBox.append(h("div", { class: "row-sub", style: "margin:12px 0 8px" }, "Livelli inclusi nel ripasso:"), levelChips());
    root.append(lvBox);

    root.append(h("div", { class: "h2" }, "Installa sul telefono"));
    if (standalone()) root.append(h("div", { class: "box" }, h("div", { class: "row" }, h("div", { class: "tile t-sage" }, svgIcon("check")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "App già installata")))));
    else {
      if (deferredPrompt) root.append(h("button", { class: "btn btn-primary", type: "button", onclick: async () => { deferredPrompt.prompt(); deferredPrompt = null; } }, "Installa l'app"));
      root.append(installSteps(platform()));
    }

    root.append(h("div", { class: "h2" }, "Da dove vengono le domande"));
    root.append(h("div", { class: "box" }, h("div", { class: "row" }, h("div", { class: "tile t-peach" }, svgIcon("book")), h("div", { class: "row-text" },
      h("div", { class: "row-title" }, "Sbobine del corso"),
      h("div", { class: "row-sub" }, "Sbobine di Biochimica II e domande d'esame proposte a lezione. Strutture da PubChem, zuccheri in Haworth, gruppi ionizzati a pH fisiologico. Dove la sbobina sbaglia, la card lo segnala con ⚠.")))));
    root.append(h("div", { class: "h2" }, "Privacy"));
    root.append(h("div", { class: "box" }, h("div", { class: "row" }, h("div", { class: "tile t-sage" }, svgIcon("check")), h("div", { class: "row-text" },
      h("div", { class: "row-title" }, "Niente account, niente dati personali"),
      h("div", { class: "row-sub" }, `I progressi restano su questo telefono. Una volta al giorno l'app invia solo un codice casuale (${S.device}), la versione e il sistema, per contare quante persone la usano. Le segnalazioni contengono la domanda e la tua nota.`)))));

    const reps = loadReports(), pending = reps.filter(x => !x.sent);
    root.append(h("div", { class: "h2" }, "Segnalazioni"));
    const repBox = h("div", { class: "box" }, h("div", { class: "row" }, h("div", { class: "tile t-rose" }, svgIcon("flag")),
      h("div", { class: "row-text" }, h("div", { class: "row-title" }, reps.length ? `${reps.length} ${reps.length === 1 ? "segnalazione" : "segnalazioni"} da questo telefono` : "Nessuna segnalazione"),
        h("div", { class: "row-sub" }, pending.length ? (REPORT_URL ? `${pending.length} in attesa di connessione` : `${pending.length} salvate qui: copiale e mandale a chi cura l'app`) : "Usa «Segnala errore» sotto ogni card"))));
    if (pending.length && !REPORT_URL) {
      const copy = h("button", { class: "btn btn-ghost", type: "button", style: "margin:0 12px 12px" }, "Copia segnalazioni");
      copy.addEventListener("click", async () => {
        const txt = JSON.stringify(pending, null, 1);
        try { await navigator.clipboard.writeText(txt); toast("Copiate negli appunti"); }
        catch (e) { const ta = h("textarea", { class: "copy-area", readonly: true, id: "copy-reports" }); ta.value = txt; repBox.append(ta); ta.select(); toast("Seleziona il testo e copialo"); }
      });
      repBox.append(copy);
    }
    root.append(repBox);
    root.append(h("div", { class: "h2" }, "Dati"));
    root.append(backupBox());
    const resetBox = h("div", { class: "box" });
    const askReset = () => {
      resetBox.innerHTML = "";
      resetBox.append(h("div", { class: "confirm" }, h("div", { class: "row-title" }, "Cancellare tutti i progressi?"), h("div", { class: "row-sub" }, "Argomenti spuntati, errori e statistiche di questo telefono. Non si può annullare."),
        h("div", { class: "btns" }, h("button", { class: "btn btn-danger", type: "button", onclick: () => { const keep = { welcomed: true, theme: S.theme, study: "grad" }; S = Object.assign(blank(), keep); save(); applyTheme(); renderAll(); toast("Progressi cancellati"); } }, "Cancella tutto"),
          h("button", { class: "btn btn-ghost", type: "button", onclick: renderInfo }, "Annulla"))));
    };
    resetBox.append(h("button", { class: "row", type: "button", style: "width:100%;background:none;border:0;text-align:left;cursor:pointer", onclick: askReset },
      h("div", { class: "tile t-rose" }, svgIcon("flag")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Azzera i progressi"), h("div", { class: "row-sub" }, "Tutto è salvato solo su questo telefono"))));
    root.append(resetBox,
      h("div", { class: "box credit" }, h("div", { class: "mono", "aria-hidden": "true" }, "GP"),
        h("div", { class: "row-text" }, h("div", { class: "role" }, "Creata da"), h("div", { class: "who" }, "Gabriele Polonio"),
          h("div", { class: "row-sub" }, `Corso di Laurea in Medicina e Chirurgia · Sapienza Università di Roma, Polo Pontino · 2026 · versione ${C.version}`))));
  }

  /* ---------------- Backup dei progressi ---------------- */
  const BACKUP_FIELDS = ["selected", "lastChecked", "onlyLast", "mode", "theme", "newPerDay", "levels", "progressive", "study", "hardStats", "cards", "days"];
  function backupBox() {
    const box = h("div", { class: "box" });
    const status = h("div", { class: "row-sub", style: "padding:0 12px 12px" }); status.hidden = true;
    const say = t => { status.textContent = t; status.hidden = false; };
    const exp = h("button", { class: "row", type: "button", style: "width:100%;background:none;border:0;text-align:left;cursor:pointer" },
      h("div", { class: "tile t-sky" }, svgIcon("share")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Esporta i progressi"), h("div", { class: "row-sub" }, "Salva un file da riaprire su un altro telefono")));
    exp.addEventListener("click", async () => {
      const data = {}; BACKUP_FIELDS.forEach(k => data[k] = S[k]);
      const txt = JSON.stringify({ app: "biochiquiz", v: 1, date: new Date().toISOString(), data });
      const name = `biochiquiz-progressi-${today()}.json`;
      const file = typeof File === "function" ? new File([txt], name, { type: "application/json" }) : null;
      try {
        if (file && navigator.canShare && navigator.canShare({ files: [file] })) { await navigator.share({ files: [file], title: "Progressi Biochiquiz" }); say("File pronto: salvalo in File o mandalo all'altro telefono."); return; }
      } catch (e) { if (e && e.name === "AbortError") return; }
      if (isHosted()) {
        const a = h("a", { href: URL.createObjectURL(new Blob([txt], { type: "application/json" })), download: name }); document.body.append(a); a.click(); a.remove();
        say("File scaricato: " + name);
      } else say("Il file si può salvare solo dall'app installata.");
    });
    const inp = h("input", { type: "file", accept: ".json,application/json", id: "import-file", class: "visually-hidden" });
    const imp = h("label", { class: "row", for: "import-file", style: "cursor:pointer;border-top:1px solid var(--line)" },
      h("div", { class: "tile t-lilac" }, svgIcon("feed")), h("div", { class: "row-text" }, h("div", { class: "row-title" }, "Importa i progressi"), h("div", { class: "row-sub" }, "Apri un file esportato: sostituisce i progressi di questo telefono")));
    inp.addEventListener("change", async () => {
      const f = inp.files && inp.files[0]; inp.value = ""; if (!f) return;
      try {
        const j = JSON.parse(await f.text());
        if (j.app !== "biochiquiz" || !j.data || typeof j.data.cards !== "object") throw new Error("formato");
        BACKUP_FIELDS.forEach(k => { if (k in j.data) S[k] = j.data[k]; });
        save(); applyTheme(); renderTopics(); resetFeed();
        toast(`Progressi importati: ${Object.keys(S.cards).length} card`); renderInfo();
      } catch (e) { say("Questo file non è un backup di Biochiquiz. Scegli il file che hai esportato."); }
    });
    box.append(exp, inp, imp, status);
    return box;
  }

  /* ---------------- Benvenuto ---------------- */
  function showWelcome() {
    const w = h("div", { class: "welcome", role: "dialog", "aria-modal": "true", "aria-label": "Benvenuto" });
    const inner = h("div", { class: "welcome-inner" });
    const pf = platform();
    inner.append(h("div", { class: "hero-mark", html: ICON.flask }),
      h("h1", { class: "h1" }, "Ripassa Biochimica dalle sbobine"),
      h("p", { class: "lead" }, "Una domanda per schermata: rispondi e scorri giù. Le card che sbagli tornano più spesso. I progressi restano solo sul tuo telefono, senza account."));
    if (!standalone()) {
      inner.append(h("div", { class: "h2" }, pf === "ios" ? "Installala su iPhone" : pf === "android" ? "Installala su Android" : "Installala sul telefono"), installSteps(pf));
      if (/claude\.(ai|site)|claudeusercontent/.test(location.hostname)) inner.append(h("p", { class: "lead", style: "font-size:13px" }, "Questa è l'anteprima di prova: l'installazione con funzionamento offline sarà attiva nella versione pubblicata."));
    }
    inner.append(h("button", { class: "btn btn-primary", type: "button", onclick: () => { S.welcomed = true; save(); w.remove(); go(S.selected.length ? "feed" : "topics"); } }, "Inizia"));
    w.append(inner); document.body.append(w);
  }

  /* ---------------- Navigazione e tema ---------------- */
  const VIEWS = ["feed", "topics", "stats", "info"];
  function go(v) {
    VIEWS.forEach(x => { $("#view-" + x).hidden = x !== v; $("#tab-" + x).setAttribute("aria-selected", String(x === v)); });
    if (v === "stats") renderStats();
    if (v === "info") renderInfo();
    if (v === "topics") renderTopics();
  }
  function applyTheme() {
    if (S.theme === "system") delete document.documentElement.dataset.theme;
    else document.documentElement.dataset.theme = S.theme;
    const meta = $('meta[name="theme-color"]'); if (meta) meta.content = getComputedStyle(document.documentElement).getPropertyValue("--bg").trim();
    redrawMolecules();
  }
  function renderAll() { renderModebar(); renderTopics(); resetFeed(); go(S.selected.length ? "feed" : "topics"); }

  /* ---------------- Aggiornamenti (solo app installata / GitHub Pages) ---------------- */
  const isHosted = () => location.protocol === "https:" && !/claude/.test(location.hostname);
  let updateShown = false;
  async function checkUpdate() {
    if (!isHosted() || updateShown || !navigator.onLine) return;
    try {
      const r = await fetch("version.json?t=" + Date.now(), { cache: "no-store" });
      const v = (await r.json()).version;
      if (v && v !== C.version) {
        updateShown = true;
        const bar = h("div", { class: "update-bar", role: "status" }, h("span", {}, "Nuova versione con domande aggiornate"),
          h("button", { type: "button", class: "btn btn-primary", onclick: async () => {
            try { const reg = await navigator.serviceWorker.getRegistration(); if (reg) await reg.update(); } catch (e) { }
            location.reload();
          } }, "Aggiorna"));
        document.body.append(bar);
      }
    } catch (e) { }
  }

  function init() {
    const tabbar = $("#tabbar");
    [["feed", "Studia"], ["topics", "Argomenti"], ["stats", "Statistiche"], ["info", "Altro"]].forEach(([v, l]) => {
      tabbar.append(h("button", { class: "tab", id: "tab-" + v, type: "button", role: "tab", "aria-selected": "false", "aria-controls": "view-" + v, onclick: () => go(v) },
        h("span", { class: "pill", html: ICON[v] }), l));
    });
    feed().addEventListener("scroll", () => requestAnimationFrame(onFeedScroll), { passive: true });
    matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => { if (S.theme === "system") applyTheme(); });
    applyTheme();
    renderAll();
    if (!S.welcomed) showWelcome();
    if ("serviceWorker" in navigator && isHosted()) navigator.serviceWorker.register("sw.js").catch(() => { });
    flushReports(); checkUpdate(); pingUsage();
    window.addEventListener("online", () => { flushReports(); checkUpdate(); pingUsage(); });
    document.addEventListener("visibilitychange", () => { if (document.visibilityState === "visible") { flushReports(); checkUpdate(); pingUsage(); } });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
