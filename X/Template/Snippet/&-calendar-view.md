
```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const COLORS = { 5:'#0284c7', 4:'#6366f1', 3:'#7c3aed', 2:'#db2777', 1:'#dc2626' };

let days = [];
for (const p of dv.pages("#calendar/daily").sort(p => p.file.name, "asc")) {
  const d = moment(p.file.name, "YYYY-MM-DD");
  const v = SCALE[p["daily-mood"]];
  if (d.isBetween(startDate, endDate, null, "[]") && v)
    days.push({ emoji: p["daily-mood"].split("–")[0].trim(), label: d.format("D"), value: v, color: COLORS[v] });
}

const root = dv.el("div", "");
root.style.cssText = `background:#f8fafc;border-radius:8px;padding:8px 10px;color:#1e293b;width:100%;box-sizing:border-box;border:1px solid rgba(0,0,0,0.07);`;

const hdr = document.createElement("div");
hdr.style.cssText = "font-size:0.65em;color:#94a3b8;margin-bottom:6px;";
hdr.textContent = `${startDate.format("DD/MM/YY")} → ${endDate.format("DD/MM/YY")}  ·  ${days.length}d`;
root.appendChild(hdr);

const wk = document.createElement("div");
wk.style.cssText = "display:grid;grid-template-columns:repeat(7,1fr);gap:3px;margin-bottom:3px;";
["D","S","T","Q","Q","S","S"].forEach(d => { const el = document.createElement("div"); el.textContent = d; el.style.cssText = "text-align:center;font-size:0.58em;color:#94a3b8;"; wk.appendChild(el); });
root.appendChild(wk);

const grid = document.createElement("div");
grid.style.cssText = "display:grid;grid-template-columns:repeat(7,1fr);gap:3px;";

const offset = startDate.day();
for (let i = 0; i < offset; i++) grid.appendChild(document.createElement("div"));

for (const day of days) {
  const cell = document.createElement("div");
  cell.innerHTML = `<div style="font-size:1.05em;line-height:1">${day.emoji}</div><div style="font-size:0.5em;color:#94a3b8;margin-top:1px">${day.label}</div>`;
  cell.style.cssText = `aspect-ratio:1;display:flex;flex-direction:column;justify-content:center;align-items:center;border:1px solid ${day.color}33;background:${day.color}08;border-radius:4px;cursor:default;transition:all 0.15s;`;
  cell.onmouseenter = () => { cell.style.background = day.color+"22"; cell.style.transform = "scale(1.1)"; };
  cell.onmouseleave = () => { cell.style.background = day.color+"08"; cell.style.transform = ""; };
  grid.appendChild(cell);
}

root.appendChild(grid);
dv.container.appendChild(root);
```
