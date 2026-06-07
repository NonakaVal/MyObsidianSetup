
```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const SECTION   = "Capture";

const MOOD_EMOJI = {
  "😄 – Happy": "😄",
  "🙂 – Neutral": "🙂",
  "😐 – Meh": "😐",
  "😞 – Sad": "😞",
  "😠 – Frustrated": "😠"
};

const MOOD_COLOR = {
  "😄 – Happy": "#4ade80",
  "🙂 – Neutral": "#818cf8",
  "😐 – Meh": "#facc15",
  "😞 – Sad": "#f472b6",
  "😠 – Frustrated": "#f87171"
};

const pages = dv.pages("#calendar/daily")
  .where(p => moment(p.file.name, "YYYY-MM-DD").isBetween(startDate, endDate, null, "[]"))
  .sort(p => p.file.name, "asc");

function parsePomodoro(text) {
  const m = text.match(/(pomodoro::(WORK|BREAK)).*(duration::\s*(\d+)m)/i);
  if (!m) return null;
  return { type: m[2].toUpperCase(), minutes: parseInt(m[4]) };
}

const ICONS = [
  "💡","⭐","😴","💀","🌱","⚠️","💩","❓","🧭","💬","🗯️","🍅","😞","🥤","😤","✅","💾","🤔", "🔊"
];

function extractIcons(text) {
  return ICONS.filter(ic => text.includes(ic));
}

let entries = [];

for (const page of pages) {

  const lines = (await dv.io.load(page.file.path)).split("\n");
  const date  = moment(page.file.name, "YYYY-MM-DD");
  const mood  = page["daily-mood"] ?? null;

  let ins = false;

  for (const l of lines) {

    if (l.match(new RegExp(`^#\\s+${SECTION}\\s*$`, "i"))) {
      ins = true;
      continue;
    }

    if (l.startsWith("# ") && ins) break;

    if (ins && l.trim()) {
      entries.push({
        date,
        text: l.trim(),
        mood
      });
    }
  }
}

const byDate = {};

for (const e of entries) {

  const key = e.date.format("YYYY-MM-DD");

  if (!byDate[key]) {
    byDate[key] = {
      date: e.date,
      mood: e.mood,
      pomodoros: [],
      others: []
    };
  }

  const p = parsePomodoro(e.text);

  if (p) {
    byDate[key].pomodoros.push(p);
  } else {
    byDate[key].others.push(e.text);
  }
}

// ── Render ─────────────────────────────────────

const root = dv.el("div", "");

root.style.cssText = `
background:#f8fafc;
border-radius:8px;
padding:10px 14px;
color:#1e293b;
width:100%;
box-sizing:border-box;
border:1px solid rgba(0,0,0,0.07);
font-family:inherit;
`;

const days = Object.values(byDate);
const totalEntries = entries.length;

const hdr = document.createElement("div");

hdr.style.cssText = `
display:flex;
justify-content:space-between;
font-size:0.68em;
color:#94a3b8;
margin-bottom:10px;
padding-bottom:7px;
border-bottom:1px solid rgba(0,0,0,0.08);
letter-spacing:0.3px;
`;

hdr.innerHTML =
`<span>📋 capture log · ${startDate.format("DD/MM/YY")} → ${endDate.format("DD/MM/YY")}</span>
<span>${totalEntries} registros · ${days.length}d</span>`;

root.appendChild(hdr);

if (days.length === 0) {

  const empty = document.createElement("div");

  empty.style.cssText = `
  font-size:0.78em;
  color:#94a3b8;
  padding:6px 0;
  `;

  empty.textContent = "nenhum registro no período.";

  root.appendChild(empty);

} else {

  days.forEach((day, idx) => {

    const wrap = document.createElement("div");

    wrap.style.cssText = `
    padding:7px 0 8px;
    ${idx > 0 ? "border-top:1px solid rgba(0,0,0,0.05);" : ""}
    `;

    const dateRow = document.createElement("div");

    dateRow.style.cssText = `
    display:flex;
    align-items:center;
    gap:7px;
    margin-bottom:4px;
    width:100%;
    `;

    const dateSpan = document.createElement("span");

    dateSpan.style.cssText = `
    font-size:0.66em;
    font-weight:700;
    color:#0f172a;
    text-transform:uppercase;
    letter-spacing:0.6px;
    white-space:nowrap;
    `;

    dateSpan.textContent = day.date.format("ddd DD/MM/YYYY");

    dateRow.appendChild(dateSpan);

    const spacer = document.createElement("span");
    spacer.style.cssText = "flex:1;";
    dateRow.appendChild(spacer);

    const rightGroup = document.createElement("span");

    rightGroup.style.cssText = `
    display:inline-flex;
    align-items:center;
    gap:6px;
    `;

    // Pomodoro

    if (day.pomodoros.length > 0) {

      const works  = day.pomodoros.filter(p => p.type === "WORK");
      const breaks = day.pomodoros.filter(p => p.type === "BREAK");

      const wMins  = works.reduce((s, p) => s + p.minutes, 0);
      const bMins  = breaks.reduce((s, p) => s + p.minutes, 0);

      const pomWrap = document.createElement("span");

      pomWrap.style.cssText = `
      display:inline-flex;
      align-items:center;
      gap:4px;
      background:rgba(2,132,199,0.06);
      border:1px solid rgba(2,132,199,0.14);
      border-radius:6px;
      padding:1px 7px;
      `;

      if (works.length) {

        const w = document.createElement("span");

        w.style.cssText = `
        font-size:0.66em;
        color:#0369a1;
        white-space:nowrap;
        `;

        w.textContent = `🍅 ${works.length}× · ${wMins}m`;

        pomWrap.appendChild(w);
      }

      if (breaks.length) {

        if (works.length) {

          const sep = document.createElement("span");

          sep.style.cssText = `
          font-size:0.6em;
          color:#cbd5e1;
          `;

          sep.textContent = "·";

          pomWrap.appendChild(sep);
        }

        const b = document.createElement("span");

        b.style.cssText = `
        font-size:0.66em;
        color:#0369a1;
        white-space:nowrap;
        `;

        b.textContent = `🥤 ${breaks.length}× · ${bMins}m`;

        pomWrap.appendChild(b);
      }

      rightGroup.appendChild(pomWrap);
    }

    // Mood (sempre último)

    if (day.mood && MOOD_EMOJI[day.mood]) {

      const pill = document.createElement("span");

      const c = MOOD_COLOR[day.mood] || "#94a3b8";

      pill.style.cssText = `
      font-size:0.78em;
      padding:1px 6px;
      border-radius:5px;
      background:${c}18;
      border:1px solid ${c}33;
      display:inline-flex;
      align-items:center;
      `;

      pill.textContent = MOOD_EMOJI[day.mood];

      rightGroup.appendChild(pill);
    }

    dateRow.appendChild(rightGroup);
    wrap.appendChild(dateRow);

    const textBlock = document.createElement("div");

    textBlock.style.cssText = `
    display:flex;
    flex-direction:column;
    gap:1px;
    padding-left:9px;
    border-left:2px solid rgba(2,132,199,0.18);
    margin-top:1px;
    `;

    for (const text of day.others) {

      const row = document.createElement("div");

      row.style.cssText = `
      font-size:0.78em;
      line-height:1.55;
      color:#334155;
      `;

      row.textContent = text;

      textBlock.appendChild(row);
    }

    wrap.appendChild(textBlock);
    root.appendChild(wrap);
  });
}

dv.container.appendChild(root);
```