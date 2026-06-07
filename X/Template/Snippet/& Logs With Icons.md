
<br>

```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const CATS = [
  {icon:"💡",name:"Ideia"},  {icon:"⭐",name:"Algo bom"}, {icon:"😴",name:"Evento"},
  {icon:"💀",name:"Puts"},   {icon:"🌱",name:"Motivação"},{icon:"💩",name:"Cagada"},
  {icon:"❓",name:"???"},    {icon:"🧭",name:"Intenção"}, {icon:"💬",name:"Gratidão"},
  {icon:"🍅",name:"Work"},   {icon:"🥤",name:"Break"} ,{ icon:"🔊", name:"Audio" }
];

const pages = dv.pages("#calendar/daily")
  .where(p => moment(p.file.name, "YYYY-MM-DD").isBetween(startDate, endDate, null, "[]"))
  .sort(p => p.file.name, "desc");

let entries = [], totals = Object.fromEntries(CATS.map(c => [c.name, 0]));
for (const page of pages) {
  const lines = (await dv.io.load(page.file.path)).split("\n");
  let ins = false, sec = [];
  for (const l of lines) {
    if (l.startsWith("# Capture")) { ins = true; continue; }
    if (l.startsWith("# ") && ins) break;
    if (ins && l.trim()) sec.push(l.trim());
  }
  for (const line of sec) {
    const cat = CATS.find(c => line.includes(c.icon));
    if (cat) { totals[cat.name]++; entries.push({ date: moment(page.file.name,"YYYY-MM-DD").format("DD/MM"), cat: cat.name, icon: cat.icon, text: line.replace(cat.icon,"").trim() }); }
  }
}

const root = dv.el("div", "");
root.style.cssText = `background:rgba(10,12,20,0.97);border-radius:8px;padding:10px 12px;color:#fff;width:100%;box-sizing:border-box;`;

const total = Object.values(totals).reduce((a, b) => a + b, 0);
const hdr = document.createElement("div");
hdr.style.cssText = "display:flex;justify-content:space-between;font-size:0.72em;opacity:0.4;margin-bottom:8px;";
hdr.innerHTML = `<span>📋 logs · ${startDate.format("DD/MM")} → ${endDate.format("DD/MM/YY")}</span><span>${total}</span>`;
root.appendChild(hdr);

const pills = document.createElement("div");
pills.style.cssText = "display:flex;flex-wrap:wrap;gap:4px;margin-bottom:8px;";

const list = document.createElement("div");
list.style.cssText = "max-height:340px;overflow-y:auto;";

const render = f => {
  list.innerHTML = "";
  const fl = f ? entries.filter(e => e.cat === f) : entries;
  for (const e of fl) {
    const row = document.createElement("div");
    row.style.cssText = "display:grid;grid-template-columns:40px 1fr;gap:4px;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.04);";
    row.innerHTML = `<span style="font-size:0.68em;opacity:0.28">${e.date}</span><span style="font-size:0.82em">${e.icon} ${e.text}</span>`;
    list.appendChild(row);
  }
};

let active = null;
CATS.forEach(c => {
  if (!totals[c.name]) return;
  const btn = document.createElement("button");
  btn.textContent = `${c.icon}${totals[c.name]}`;
  btn.title = c.name;
  btn.style.cssText = "padding:2px 6px;border:1px solid rgba(255,255,255,0.1);border-radius:20px;background:transparent;color:#fff;font-size:0.7em;cursor:pointer;transition:all 0.15s;";
  btn.onclick = () => {
    active = (active === c.name ? null : c.name);
    pills.querySelectorAll("button").forEach(b => b.style.background = "transparent");
    if (active) btn.style.background = "rgba(255,255,255,0.12)";
    render(active);
  };
  pills.appendChild(btn);
});

root.appendChild(pills);
root.appendChild(list);
render(null);
dv.container.appendChild(root);
```
z