
```dataviewjs
// ═══════════════════════════════════════════════════
// 📍 KPI CARD 3 — light · sinal direcional simples
// ═══════════════════════════════════════════════════

// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const EMOJIS = { 5:'😄', 4:'🙂', 3:'😐', 2:'😞', 1:'😠' };
const CATS   = [
  {icon:"💡",name:"Ideia"},{icon:"⭐",name:"Algo bom"},{icon:"😴",name:"Evento"},
  {icon:"💀",name:"Puts"},{icon:"🌱",name:"Motivação"},{icon:"💩",name:"Cagada"},
  {icon:"❓",name:"???"},{icon:"🧭",name:"Intenção"},{icon:"💬",name:"Gratidão"},
  {icon:"🍅",name:"Work"},{icon:"🥤",name:"Break"}
];

const duration  = endDate.diff(startDate, "days") + 1;
const endPrev   = startDate.clone().subtract(1, "days");
const startPrev = endPrev.clone().subtract(duration - 1, "days");

const getData = async (s, e) => {
  const pages = dv.pages("#calendar/daily")
    .where(p => moment(p.file.name,"YYYY-MM-DD").isBetween(s,e,null,"[]"))
    .sort(p => p.file.name, "asc");
  let moodData=[], moodTotal=0, moodN=0, logTotal=0;
  for (const p of pages) {
    const v = SCALE[p["daily-mood"]];
    if (v) { moodData.push(v); moodTotal+=v; moodN++; }
    const lines = (await dv.io.load(p.file.path)).split("\n");
    let ins=false;
    for (const l of lines) {
      if (l.startsWith("# Capture")){ins=true;continue;}
      if (l.startsWith("# ")&&ins) break;
      if (ins&&l.trim()&&CATS.some(c=>l.includes(c.icon))) logTotal++;
    }
  }
  const totalDays = e.diff(s,"days") + 1;
  const consistency = totalDays ? Math.round((moodN/totalDays)*100) : 0;
  let trendValue = 0;
  if (moodData.length >= 4) {
    const h  = Math.floor(moodData.length/2);
    const a1 = moodData.slice(0,h).reduce((a,b)=>a+b,0)/h;
    const a2 = moodData.slice(h).reduce((a,b)=>a+b,0)/(moodData.length-h);
    trendValue = a2 - a1;
  }
  return { avg:moodN?moodTotal/moodN:0, days:moodN, logs:logTotal, consistency, trendValue };
};

const [cur, prev] = await Promise.all([getData(startDate,endDate), getData(startPrev,endPrev)]);

const moodDelta        = cur.avg - prev.avg;
const consistencyDelta = cur.consistency - prev.consistency;
const combinedScore    = moodDelta + (consistencyDelta / 100);

let signal, signalColor, signalDesc;
if (combinedScore > 0.2) {
  signal = "↑"; signalColor = "#0284c7";
  signalDesc = moodDelta > 0.3 ? "humor melhorando" : "mais consistente";
} else if (combinedScore < -0.2) {
  signal = "↓"; signalColor = "#dc2626";
  signalDesc = moodDelta < -0.3 ? "humor caindo" : "menos consistente";
} else {
  signal = "→"; signalColor = "rgba(0,0,0,0.3)";
  signalDesc = "estável";
}

const root = dv.el("div","");
root.style.cssText = `
  background:#f8fafc; border-radius:8px;
  padding:10px 12px; color:#1e293b;
  width:100%; box-sizing:border-box;
  border:1px solid rgba(0,0,0,0.07);
`;

const hero = document.createElement("div");
hero.style.cssText = "display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;";
hero.innerHTML = `
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:2em;line-height:1">${EMOJIS[Math.round(cur.avg)]||"–"}</span>
    <div>
      <div style="font-size:1.4em;font-weight:800;line-height:1;color:#0f172a">${cur.avg.toFixed(1)}<span style="font-size:0.45em;opacity:0.4;font-weight:400"> /5</span></div>
      <div style="font-size:0.65em;color:#64748b;margin-top:1px">humor médio</div>
    </div>
  </div>
  <div style="text-align:center;">
    <div style="font-size:2.2em;line-height:1;color:${signalColor};font-weight:700">${signal}</div>
    <div style="font-size:0.62em;color:#64748b;margin-top:2px">${signalDesc}</div>
  </div>
`;
root.appendChild(hero);

const hr = document.createElement("div");
hr.style.cssText = "height:1px;background:rgba(0,0,0,0.07);margin-bottom:8px;";
root.appendChild(hr);

const metrics = document.createElement("div");
metrics.style.cssText = "display:grid;grid-template-columns:1fr 1fr;gap:6px;";

const prevConsDiff  = prev.consistency ? cur.consistency - prev.consistency : null;
[
  {
    label: "consistência", value: `${cur.consistency}%`,
    sub: prevConsDiff !== null ? (prevConsDiff > 0 ? `+${prevConsDiff}pp` : `${prevConsDiff}pp`) : "–",
    subColor: prevConsDiff > 0 ? "#0284c7" : prevConsDiff < 0 ? "#dc2626" : "rgba(0,0,0,0.2)"
  },
  {
    label: "logs", value: cur.logs,
    sub: prev.logs ? (cur.logs > prev.logs ? `+${cur.logs-prev.logs}` : `${cur.logs-prev.logs}`) : "–",
    subColor: cur.logs >= prev.logs ? "#0284c7" : "#dc2626"
  }
].forEach(m => {
  const card = document.createElement("div");
  card.style.cssText = "border:1px solid rgba(0,0,0,0.08);border-radius:6px;padding:6px 8px;background:#fff;";
  card.innerHTML = `
    <div style="font-size:0.6em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:3px">${m.label}</div>
    <div style="display:flex;align-items:baseline;gap:5px;">
      <span style="font-size:1.15em;font-weight:700;color:#0f172a">${m.value}</span>
      <span style="font-size:0.7em;color:${m.subColor}">${m.sub}</span>
    </div>
  `;
  metrics.appendChild(card);
});
root.appendChild(metrics);

const foot = document.createElement("div");
foot.style.cssText = "font-size:0.6em;color:#94a3b8;margin-top:7px;text-align:right;";
foot.textContent   = `${startDate.format("DD/MM")} → ${endDate.format("DD/MM/YYYY")}`;
root.appendChild(foot);
dv.container.appendChild(root);
```
