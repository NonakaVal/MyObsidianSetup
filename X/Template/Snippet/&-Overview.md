
```dataviewjs
// ═══════════════════════════════════════════════════════════════════════
// 🧭 MASTER SUMMARY CARD — light
// Card principal · topo de controle · intervalo completo
// ═══════════════════════════════════════════════════════════════════════

// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");
// ──────────────────────────────────────────────────────────────────────

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const EMOJIS = { 5:"😄", 4:"🙂", 3:"😐", 2:"😞", 1:"😠" };
const COLORS  = { 5:"#0284c7", 4:"#6366f1", 3:"#7c3aed", 2:"#db2777", 1:"#dc2626" };
const CATS    = [
  {icon:"💡",name:"Ideia"},  {icon:"⭐",name:"Algo bom"}, {icon:"😴",name:"Evento"},
  {icon:"💀",name:"Puts"},   {icon:"🌱",name:"Motivação"},{icon:"💩",name:"Cagada"},
  {icon:"❓",name:"???"},    {icon:"🧭",name:"Intenção"}, {icon:"💬",name:"Gratidão"},
  {icon:"🍅",name:"Work"},   {icon:"🥤",name:"Break"}
];

const duration  = endDate.diff(startDate, "days") + 1;
const endPrev   = startDate.clone().subtract(1, "days");
const startPrev = endPrev.clone().subtract(duration - 1, "days");

const getData = async (s, e) => {
  const pages = dv.pages("#calendar/daily")
    .where(p => moment(p.file.name,"YYYY-MM-DD").isBetween(s,e,null,"[]"))
    .sort(p => p.file.name, "asc");

  let moodData=[], moodTotal=0, moodN=0, logTotal=0;
  let moodCount={}, monthlyAvg={};
  let catTotals = Object.fromEntries(CATS.map(c=>[c.name,{icon:c.icon,count:0}]));
  let bestDay=null, worstDay=null, streak=0, streakMax=0, lastDate=null;

  for (const p of pages) {
    const d = moment(p.file.name,"YYYY-MM-DD");
    const v = SCALE[p["daily-mood"]];
    if (v) {
      moodData.push({ d, v });
      moodTotal += v; moodN++;
      moodCount[v] = (moodCount[v]||0)+1;

      const monthKey = d.format("YYYY-MM");
      if (!monthlyAvg[monthKey]) monthlyAvg[monthKey] = { sum:0, n:0 };
      monthlyAvg[monthKey].sum += v;
      monthlyAvg[monthKey].n++;

      if (!bestDay  || v > bestDay.v)  bestDay  = { d, v };
      if (!worstDay || v < worstDay.v) worstDay = { d, v };
      if (lastDate && d.diff(lastDate,"days")===1) streak++;
      else streak = 1;
      if (streak > streakMax) streakMax = streak;
      lastDate = d;
    }
    const lines = (await dv.io.load(p.file.path)).split("\n");
    let ins=false;
    for (const l of lines) {
      if (l.startsWith("# Capture")){ins=true;continue;}
      if (l.startsWith("# ")&&ins) break;
      if (ins&&l.trim()) {
        const cat=CATS.find(c=>l.includes(c.icon));
        if(cat){catTotals[cat.name].count++; logTotal++;}
      }
    }
  }

  const totalDays   = e.diff(s,"days")+1;
  const consistency = totalDays ? Math.round((moodN/totalDays)*100) : 0;
  const avgVal      = moodN ? moodTotal/moodN : 0;

  let trendValue=0;
  if (moodData.length>=4) {
    const h  = Math.floor(moodData.length/2);
    const a1 = moodData.slice(0,h).reduce((a,b)=>a+b.v,0)/h;
    const a2 = moodData.slice(h).reduce((a,b)=>a+b.v,0)/(moodData.length-h);
    trendValue = a2-a1;
  }

  const dominant = Object.entries(moodCount).sort((a,b)=>b[1]-a[1])[0];
  const topCats  = Object.entries(catTotals)
    .sort((a,b)=>b[1].count-a[1].count)
    .filter(([,v])=>v.count>0).slice(0,5);
  const monthlyPoints = Object.entries(monthlyAvg)
    .sort(([a],[b])=>a.localeCompare(b))
    .map(([k,v])=>({ k, avg: v.sum/v.n }));

  return { avg:avgVal, days:moodN, totalDays, logs:logTotal,
           consistency, trendValue, moodCount, catTotals,
           dominant, bestDay, worstDay, streakMax, topCats,
           monthlyPoints };
};

const [cur, prev] = await Promise.all([getData(startDate,endDate), getData(startPrev,endPrev)]);

const moodScore   = (cur.avg/5)*60;
const consScore   = (cur.consistency/100)*30;
const streakScore = Math.min(cur.streakMax/(duration||1),1)*10;
const score       = Math.round(moodScore+consScore+streakScore);
const prevScore   = Math.round((prev.avg/5)*60+(prev.consistency/100)*30+Math.min(prev.streakMax/(duration||1),1)*10);
const scoreDelta  = score - prevScore;

const scoreColor  = score>=75?"#0284c7":score>=55?"#6366f1":score>=40?"#7c3aed":score>=25?"#db2777":"#dc2626";
const scoreLabel  = score>=75?"ótimo":score>=55?"bom":score>=40?"regular":score>=25?"baixo":"crítico";
const moodDelta   = cur.avg - prev.avg;
const trendArrow  = moodDelta>0.15?"↑":moodDelta<-0.15?"↓":"→";
const trendColor  = moodDelta>0.15?"#16a34a":moodDelta<-0.15?"#dc2626":"#94a3b8";
const trendLabel  = moodDelta>0.15?"melhorando":moodDelta<-0.15?"piorando":"estável";
const deltaLabel  = scoreDelta>0?`+${scoreDelta}`:scoreDelta<0?`${scoreDelta}`:"±0";
const deltaColor  = scoreDelta>0?"#16a34a":scoreDelta<0?"#dc2626":"#94a3b8";
const total       = Object.values(cur.moodCount).reduce((a,b)=>a+b,0)||1;

const clr  = (a,b) => a>b?"#16a34a":a<b?"#dc2626":"#94a3b8";
const diff = (a,b,u="") => { if(b==null)return"–"; const d=a-b; return `${d>=0?"+":""}${d}${u}`; };

const pts   = cur.monthlyPoints;
const minV  = pts.length ? Math.min(...pts.map(p=>p.avg)) : 1;
const maxV  = pts.length ? Math.max(...pts.map(p=>p.avg)) : 5;
const range = maxV-minV || 1;
const W=140, H=34, pad=3;
const sparkPath = pts.map((p,i)=>{
  const x = pad + (i/(Math.max(pts.length-1,1)))*(W-pad*2);
  const y = H-pad - ((p.avg-minV)/range)*(H-pad*2);
  return `${i===0?"M":"L"}${x.toFixed(1)},${y.toFixed(1)}`;
}).join(" ");
const lastPt = pts[pts.length-1];
const dotX = lastPt ? pad+(1*(W-pad*2)) : W-pad;
const dotY = lastPt ? H-pad-((lastPt.avg-minV)/range)*(H-pad*2) : H/2;
const moodBars = [5,4,3,2,1].map(v => ({
  v, pct: Math.round(((cur.moodCount[v]||0)/total)*100),
  count: cur.moodCount[v]||0
}));

const root = dv.el("div","");
root.style.cssText = `
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f8fafc;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 12px;
  padding: 18px 20px 14px;
  color: #0f172a;
  width: 100%;
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
`;

const glow = document.createElement("div");
glow.style.cssText = `
  position:absolute;top:-60px;left:-40px;
  width:260px;height:200px;
  background:radial-gradient(ellipse,${scoreColor}10 0%,transparent 70%);
  pointer-events:none;
`;
root.appendChild(glow);

// header
const header = document.createElement("div");
header.style.cssText = "display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:14px;position:relative;z-index:1;";

const headerLeft = document.createElement("div");
headerLeft.innerHTML = `
  <div style="font-size:0.6em;letter-spacing:0.12em;text-transform:uppercase;color:#94a3b8;margin-bottom:3px;font-weight:600">
    controle geral · ${startDate.format("DD/MM/YY")} → ${endDate.format("DD/MM/YY")}
  </div>
  <div style="display:flex;align-items:center;gap:10px;">
    <span style="font-size:2.6em;line-height:1">${cur.dominant?EMOJIS[cur.dominant[0]]:"–"}</span>
    <div>
      <div style="font-size:2em;font-weight:900;line-height:1;letter-spacing:-1px;color:#0f172a">
        ${cur.avg.toFixed(2)}<span style="font-size:0.35em;color:#cbd5e1;font-weight:400"> /5.00</span>
      </div>
      <div style="display:flex;align-items:center;gap:6px;margin-top:1px;">
        <span style="font-size:0.65em;font-weight:700;color:${scoreColor};text-transform:uppercase;letter-spacing:0.05em">${scoreLabel}</span>
        <span style="font-size:0.6em;color:${trendColor};font-weight:600">${trendArrow} ${trendLabel}</span>
      </div>
    </div>
  </div>
`;
header.appendChild(headerLeft);

const badge = document.createElement("div");
badge.style.cssText = `
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:#fff;border:1px solid ${scoreColor}30;
  border-radius:10px;padding:8px 14px;min-width:70px;flex-shrink:0;
  box-shadow:0 1px 4px rgba(0,0,0,0.06);
`;
badge.innerHTML = `
  <div style="font-size:1.9em;font-weight:900;line-height:1;color:${scoreColor}">${score}</div>
  <div style="font-size:0.5em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.1em;margin-top:1px">score</div>
  <div style="font-size:0.6em;color:${deltaColor};font-weight:700;margin-top:3px">${deltaLabel} pts</div>
`;
header.appendChild(badge);
root.appendChild(header);

const barWrap = document.createElement("div");
barWrap.style.cssText = "height:4px;border-radius:2px;background:rgba(0,0,0,0.07);overflow:hidden;margin-bottom:14px;position:relative;z-index:1;";
barWrap.innerHTML = `<div style="height:100%;width:${score}%;background:linear-gradient(90deg,${scoreColor}70,${scoreColor});border-radius:2px;"></div>`;
root.appendChild(barWrap);

// Grid KPIs
const grid = document.createElement("div");
grid.style.cssText = "display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:14px;position:relative;z-index:1;";

const mkKpi = (label, value, sub, subColor, detail="") => {
  const c = document.createElement("div");
  c.style.cssText = "background:#fff;border:1px solid rgba(0,0,0,0.07);border-radius:8px;padding:8px 10px;box-shadow:0 1px 3px rgba(0,0,0,0.04);";
  c.innerHTML = `
    <div style="font-size:0.52em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:4px">${label}</div>
    <div style="font-size:1.1em;font-weight:800;line-height:1;color:#0f172a">${value}</div>
    ${sub ? `<div style="font-size:0.6em;color:${subColor||"#94a3b8"};margin-top:3px;font-weight:600">${sub}</div>` : ""}
    ${detail ? `<div style="font-size:0.52em;color:#cbd5e1;margin-top:2px">${detail}</div>` : ""}
  `;
  return c;
};

grid.appendChild(mkKpi("dias registrados", `${cur.days}d`, `de ${cur.totalDays}d totais`, "#94a3b8", ""));
grid.appendChild(mkKpi("consistência", `${cur.consistency}%`, diff(cur.consistency,prev.consistency,"pp"), clr(cur.consistency,prev.consistency), "vs período ant."));
grid.appendChild(mkKpi("streak máximo", `${cur.streakMax}d`, diff(cur.streakMax,prev.streakMax,"d"), clr(cur.streakMax,prev.streakMax), "consecutivos"));
grid.appendChild(mkKpi("total de logs", `${cur.logs}`, diff(cur.logs,prev.logs), clr(cur.logs,prev.logs), "capturas"));
grid.appendChild(mkKpi("melhor dia", cur.bestDay?`${EMOJIS[cur.bestDay.v]} ${cur.bestDay.d.format("DD/MM/YY")}`:"–", cur.bestDay?`humor ${cur.bestDay.v}/5`:"", "#16a34a", ""));
grid.appendChild(mkKpi("pior dia", cur.worstDay?`${EMOJIS[cur.worstDay.v]} ${cur.worstDay.d.format("DD/MM/YY")}`:"–", cur.worstDay?`humor ${cur.worstDay.v}/5`:"", "#dc2626", ""));
grid.appendChild(mkKpi("humor dominante", cur.dominant?`${EMOJIS[cur.dominant[0]]} ×${cur.dominant[1]}`:"–", cur.dominant?`${Math.round((cur.dominant[1]/total)*100)}% dos dias`:"", scoreColor, ""));
grid.appendChild(mkKpi("média normaliz.", cur.avg?`${((cur.avg-1)/4*100).toFixed(0)}%`:"–", `${cur.avg.toFixed(2)} /5.00`, scoreColor, "escala 0–100%"));
root.appendChild(grid);

// Bottom
const bottom = document.createElement("div");
bottom.style.cssText = "display:flex;gap:8px;align-items:stretch;position:relative;z-index:1;";

const sparkBox = document.createElement("div");
sparkBox.style.cssText = "background:#fff;border:1px solid rgba(0,0,0,0.07);border-radius:8px;padding:8px 10px;flex:1.2;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 1px 3px rgba(0,0,0,0.04);";
const sparkTitle = document.createElement("div");
sparkTitle.style.cssText = "font-size:0.52em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:4px;";
sparkTitle.textContent = pts.length>1 ? "evolução mensal do humor" : "sparkline (sem dados mensais)";
sparkBox.appendChild(sparkTitle);
if (pts.length > 1) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg","svg");
  svg.setAttribute("viewBox",`0 0 ${W} ${H}`);
  svg.setAttribute("width","100%");
  svg.setAttribute("height","34");
  svg.style.display="block";
  const area = document.createElementNS("http://www.w3.org/2000/svg","path");
  area.setAttribute("d", sparkPath+` L${(W-pad).toFixed(1)},${H-pad} L${pad},${H-pad} Z`);
  area.setAttribute("fill",`${scoreColor}15`);
  svg.appendChild(area);
  const line = document.createElementNS("http://www.w3.org/2000/svg","path");
  line.setAttribute("d", sparkPath);
  line.setAttribute("fill","none");
  line.setAttribute("stroke",scoreColor);
  line.setAttribute("stroke-width","1.5");
  line.setAttribute("stroke-linecap","round");
  line.setAttribute("stroke-linejoin","round");
  svg.appendChild(line);
  const dot = document.createElementNS("http://www.w3.org/2000/svg","circle");
  dot.setAttribute("cx",dotX.toFixed(1));
  dot.setAttribute("cy",dotY.toFixed(1));
  dot.setAttribute("r","3");
  dot.setAttribute("fill",scoreColor);
  svg.appendChild(dot);
  sparkBox.appendChild(svg);
  const sparkFoot = document.createElement("div");
  sparkFoot.style.cssText = "display:flex;justify-content:space-between;font-size:0.52em;color:#cbd5e1;margin-top:3px;";
  sparkFoot.innerHTML = `<span>${pts[0].k}</span><span>${pts[pts.length-1].k}</span>`;
  sparkBox.appendChild(sparkFoot);
}
bottom.appendChild(sparkBox);

const distBox = document.createElement("div");
distBox.style.cssText = "background:#fff;border:1px solid rgba(0,0,0,0.07);border-radius:8px;padding:8px 10px;flex:1.1;display:flex;flex-direction:column;gap:3px;box-shadow:0 1px 3px rgba(0,0,0,0.04);";
const distTitle = document.createElement("div");
distTitle.style.cssText = "font-size:0.52em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:3px;";
distTitle.textContent = "distribuição de humor";
distBox.appendChild(distTitle);
for (const {v, pct, count} of moodBars) {
  const row = document.createElement("div");
  row.style.cssText = "display:flex;align-items:center;gap:5px;";
  row.innerHTML = `
    <span style="font-size:0.85em;width:16px;text-align:center">${EMOJIS[v]}</span>
    <div style="flex:1;height:4px;border-radius:2px;background:rgba(0,0,0,0.06);overflow:hidden;">
      <div style="height:100%;width:${pct}%;background:${COLORS[v]};border-radius:2px;"></div>
    </div>
    <span style="font-size:0.58em;color:#94a3b8;min-width:26px;text-align:right">${pct}%</span>
    <span style="font-size:0.52em;color:#cbd5e1;min-width:18px;">${count}d</span>
  `;
  distBox.appendChild(row);
}
bottom.appendChild(distBox);

const catsBox = document.createElement("div");
catsBox.style.cssText = "background:#fff;border:1px solid rgba(0,0,0,0.07);border-radius:8px;padding:8px 10px;flex:0.9;display:flex;flex-direction:column;gap:3px;box-shadow:0 1px 3px rgba(0,0,0,0.04);";
const catsTitle = document.createElement("div");
catsTitle.style.cssText = "font-size:0.52em;color:#94a3b8;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:3px;";
catsTitle.textContent = "top categorias";
catsBox.appendChild(catsTitle);
for (const [name, info] of cur.topCats) {
  const prevCount = prev.catTotals?.[name]?.count||0;
  const d = info.count-prevCount;
  const row = document.createElement("div");
  row.style.cssText = "display:flex;align-items:center;gap:5px;";
  row.innerHTML = `
    <span style="width:16px;text-align:center">${info.icon}</span>
    <div style="flex:1;height:4px;border-radius:2px;background:rgba(0,0,0,0.06);overflow:hidden;">
      <div style="height:100%;width:${Math.round((info.count/(cur.logs||1))*100)}%;background:${scoreColor}70;border-radius:2px;"></div>
    </div>
    <span style="font-size:0.62em;font-weight:700;color:#334155;min-width:20px;text-align:right">${info.count}</span>
    <span style="font-size:0.55em;color:${d>0?"#16a34a":d<0?"#dc2626":"#94a3b8"}">${d>0?"+":""}${d}</span>
  `;
  catsBox.appendChild(row);
}
bottom.appendChild(catsBox);

root.appendChild(bottom);

const footer = document.createElement("div");
footer.style.cssText = "display:flex;justify-content:space-between;align-items:center;margin-top:10px;position:relative;z-index:1;";
footer.innerHTML = `
  <span style="font-size:0.52em;color:#e2e8f0">
    ${duration}d de intervalo · ${cur.totalDays}d calendário · ${cur.days}d registrados
  </span>
  <span style="font-size:0.52em;color:#e2e8f0">
    atualizado em ${moment().format("DD/MM/YY [às] HH:mm")}
  </span>
`;
root.appendChild(footer);

dv.container.appendChild(root);
```
```