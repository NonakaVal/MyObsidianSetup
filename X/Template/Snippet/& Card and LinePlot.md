```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const COLORS = { 5:'#0284c7', 4:'#6366f1', 3:'#7c3aed', 2:'#db2777', 1:'#dc2626' };
const EMOJIS = { 5:'😄', 4:'🙂', 3:'😐', 2:'😞', 1:'😠' };
const CATS   = [
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
  let moodCount={}, catTotals=Object.fromEntries(CATS.map(c=>[c.name,{icon:c.icon,count:0}]));
  let bestDay=null, worstDay=null, streak=0, streakMax=0, lastDate=null;
  for (const p of pages) {
    const d = moment(p.file.name,"YYYY-MM-DD");
    const v = SCALE[p["daily-mood"]];
    if (v) {
      moodData.push(v); moodTotal+=v; moodN++;
      moodCount[v] = (moodCount[v]||0)+1;
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
      if (ins&&l.trim()) { const cat=CATS.find(c=>l.includes(c.icon)); if(cat){catTotals[cat.name].count++; logTotal++;} }
    }
  }
  const totalDays   = e.diff(s,"days")+1;
  const consistency = totalDays ? Math.round((moodN/totalDays)*100) : 0;
  let trendValue=0;
  if (moodData.length>=4) {
    const h=Math.floor(moodData.length/2);
    const a1=moodData.slice(0,h).reduce((a,b)=>a+b,0)/h;
    const a2=moodData.slice(h).reduce((a,b)=>a+b,0)/(moodData.length-h);
    trendValue=a2-a1;
  }
  const dominant = Object.entries(moodCount).sort((a,b)=>b[1]-a[1])[0];
  const topCats  = Object.entries(catTotals).sort((a,b)=>b[1].count-a[1].count).filter(([,v])=>v.count>0).slice(0,3);
  return { avg:moodN?moodTotal/moodN:0, days:moodN, logs:logTotal, consistency, trendValue, moodCount, dominant, bestDay, worstDay, streakMax, topCats, catTotals };
};

const [cur, prev] = await Promise.all([getData(startDate,endDate), getData(startPrev,endPrev)]);

const moodScore   = (cur.avg/5)*60;
const consScore   = (cur.consistency/100)*30;
const streakScore = Math.min(cur.streakMax/(duration||1),1)*10;
const combinedPct = Math.round(moodScore+consScore+streakScore);
const prevCombPct = Math.round((prev.avg/5)*60+(prev.consistency/100)*30+Math.min(prev.streakMax/(duration||1),1)*10);
const scoreDelta  = combinedPct - prevCombPct;

const barColor  = combinedPct>=75?"#0284c7":combinedPct>=55?"#6366f1":combinedPct>=40?"#7c3aed":combinedPct>=25?"#db2777":"#dc2626";
const barLabel  = combinedPct>=75?"ótimo":combinedPct>=55?"bom":combinedPct>=40?"regular":combinedPct>=25?"baixo":"crítico";
const deltaLabel = scoreDelta>0?`+${scoreDelta}pts`:scoreDelta<0?`${scoreDelta}pts`:"=";
const deltaColor = scoreDelta>0?"#0284c7":scoreDelta<0?"#dc2626":"rgba(0,0,0,0.25)";

const absDiff   = (a,b,u="") => { if(b==null)return"–"; const d=a-b; return `${d>0?"+":""}${d}${u}`; };
const colorDiff = (a,b) => a>b?"#0284c7":a<b?"#dc2626":"rgba(0,0,0,0.2)";

const root = dv.el("div","");
root.style.cssText = `background:#f8fafc;border-radius:8px;padding:10px 14px;color:#1e293b;width:100%;box-sizing:border-box;border:1px solid rgba(0,0,0,0.07);display:flex;flex-direction:row;align-items:stretch;gap:10px;`;

const colA = document.createElement("div");
colA.style.cssText = "display:flex;flex-direction:column;justify-content:center;gap:4px;flex-shrink:0;min-width:80px;";
colA.innerHTML = `
  <div style="display:flex;align-items:center;gap:6px;">
    <span style="font-size:2em;line-height:1">${cur.dominant?EMOJIS[cur.dominant[0]]:"–"}</span>
    <div>
      <div style="font-size:1.3em;font-weight:800;line-height:1;color:#0f172a">${cur.avg.toFixed(1)}<span style="font-size:0.42em;opacity:0.4;font-weight:400"> /5</span></div>
      <div style="font-size:0.6em;font-weight:700;color:${barColor}">${barLabel} <span style="color:${deltaColor};font-weight:400">${deltaLabel}</span></div>
    </div>
  </div>
  <div style="height:5px;border-radius:3px;background:rgba(0,0,0,0.08);overflow:hidden;"><div style="height:100%;width:${combinedPct}%;background:linear-gradient(90deg,${barColor}88,${barColor});border-radius:3px;"></div></div>
  <div style="font-size:0.55em;opacity:0.35;text-align:right">score ${combinedPct}/100</div>`;
root.appendChild(colA);

const sep1=document.createElement("div"); sep1.style.cssText="width:1px;background:rgba(0,0,0,0.08);flex-shrink:0;"; root.appendChild(sep1);

const colB = document.createElement("div");
colB.style.cssText = "display:grid;grid-template-columns:1fr 1fr;gap:5px;flex:1;align-content:center;";
const prevConsDiff = prev.consistency!=null ? cur.consistency-prev.consistency : null;
[
  { label:"consistência", value:`${cur.consistency}%`, sub:prevConsDiff!=null?absDiff(cur.consistency,prev.consistency,"pp"):"–", subColor:colorDiff(cur.consistency,prev.consistency) },
  { label:"streak máx.",  value:`${cur.streakMax}d`,   sub:absDiff(cur.streakMax,prev.streakMax,"d"),                             subColor:colorDiff(cur.streakMax,prev.streakMax) },
  { label:"melhor dia",   value:cur.bestDay?`${EMOJIS[cur.bestDay.v]} ${cur.bestDay.d.format("DD/MM")}`:"–",  sub:"", subColor:"#16a34a" },
  { label:"pior dia",     value:cur.worstDay?`${EMOJIS[cur.worstDay.v]} ${cur.worstDay.d.format("DD/MM")}`:"–", sub:"", subColor:"#dc2626" },
].forEach(m => {
  const c=document.createElement("div");
  c.style.cssText="border:1px solid rgba(0,0,0,0.08);border-radius:5px;padding:4px 7px;background:#fff;";
  c.innerHTML=`<div style="font-size:0.55em;opacity:0.45;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:2px">${m.label}</div><div style="display:flex;align-items:baseline;gap:4px;"><span style="font-size:0.95em;font-weight:700;color:#0f172a">${m.value}</span>${m.sub?`<span style="font-size:0.65em;color:${m.subColor}">${m.sub}</span>`:""}</div>`;
  colB.appendChild(c);
});
root.appendChild(colB);

const sep2=document.createElement("div"); sep2.style.cssText="width:1px;background:rgba(0,0,0,0.08);flex-shrink:0;"; root.appendChild(sep2);

const colC = document.createElement("div");
colC.style.cssText = "display:flex;flex-direction:column;justify-content:center;gap:4px;flex-shrink:0;min-width:64px;";
const catTitle=document.createElement("div"); catTitle.style.cssText="font-size:0.55em;opacity:0.4;text-transform:uppercase;letter-spacing:0.3px;margin-bottom:2px;"; catTitle.textContent="top logs"; colC.appendChild(catTitle);
for (const [name, info] of cur.topCats) {
  const diff=info.count-(prev.catTotals?.[name]?.count||0);
  const diffStr=diff>0?`<span style="color:#0284c7"> +${diff}</span>`:diff<0?`<span style="color:#dc2626"> ${diff}</span>`:"";
  const row=document.createElement("div"); row.title=name; row.style.cssText="display:flex;align-items:center;gap:5px;font-size:0.8em;";
  row.innerHTML=`<span>${info.icon}</span><span style="font-weight:600;color:#0f172a">${info.count}</span><span style="font-size:0.75em;opacity:0.45;color:#475569">${name}</span>${diffStr}`;
  colC.appendChild(row);
}
const foot=document.createElement("div"); foot.style.cssText="font-size:0.52em;opacity:0.3;margin-top:4px;white-space:nowrap;"; foot.textContent=`${startDate.format("DD/MM")} → ${endDate.format("DD/MM")}`; colC.appendChild(foot);
root.appendChild(colC);
dv.container.appendChild(root);
```

<br>

```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");
const defaultView = "chart"; // "chart" ou "calendar"

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const COLORS = { 5:'#38bdf8', 4:'#818cf8', 3:'#a78bfa', 2:'#f472b6', 1:'#f87171' };
const LABELS = Object.fromEntries(Object.entries(SCALE).map(([k,v]) => [v,k]));

const pages=dv.pages("#calendar/daily").sort(p=>p.file.name,"asc");
const days=[],chartLabels=[],chartData=[],chartColors=[];
for(const p of pages){const d=moment(p.file.name,"YYYY-MM-DD");const v=SCALE[p["daily-mood"]];if(d.isBetween(startDate,endDate,null,"[]")&&v){days.push({emoji:p["daily-mood"].split("–")[0].trim(),label:d.format("D/M"),value:v,color:COLORS[v]});chartLabels.push(d.format("DD/MM"));chartData.push(v);chartColors.push(COLORS[v]);}}

const root=dv.el("div","");
root.style.cssText=`background:rgba(10,12,20,0.97);border-radius:8px;padding:8px 10px;color:#fff;width:100%;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;`;

const header=document.createElement("div"); header.style.cssText="display:flex;align-items:center;justify-content:space-between;";
const period=document.createElement("div"); period.style.cssText="font-size:0.68em;opacity:0.3;"; period.textContent=`${startDate.format("DD/MM")} → ${endDate.format("DD/MM/YYYY")}`; header.appendChild(period);
const btnWrap=document.createElement("div"); btnWrap.style.cssText="display:flex;gap:4px;";
const mkBtn=(label,active)=>{const btn=document.createElement("button");btn.textContent=label;btn.style.cssText=`padding:2px 9px;border:1px solid rgba(255,255,255,${active?'0.25':'0.08'});border-radius:20px;background:${active?'rgba(255,255,255,0.1)':'transparent'};color:#fff;cursor:pointer;font-size:0.7em;transition:all 0.15s;`;btn.onmouseenter=()=>{btn.style.borderColor='rgba(255,255,255,0.3)';};btn.onmouseleave=()=>{btn.style.borderColor=`rgba(255,255,255,${btn._active?'0.25':'0.08'})`;};btn._active=active;return btn;};
const btnChart=mkBtn("gráfico",defaultView==="chart");const btnCal=mkBtn("calendário",defaultView==="calendar");
btnWrap.appendChild(btnChart);btnWrap.appendChild(btnCal);header.appendChild(btnWrap);root.appendChild(header);

const VIEW_HEIGHT="220px";
const chartWrap=dv.el("div",""); chartWrap.style.cssText=`height:${VIEW_HEIGHT};width:100%;box-sizing:border-box;display:${defaultView==="chart"?"block":"none"};`;
window.renderChart({type:"line",data:{labels:chartLabels,datasets:[{data:chartData,borderColor:"#38bdf8",backgroundColor:"rgba(56,189,248,0.06)",pointBackgroundColor:chartColors,pointBorderColor:chartColors,borderWidth:1.5,tension:0.4,fill:true,pointRadius:chartData.length>45?0:chartData.length>20?2:3,pointHoverRadius:5}]},options:{responsive:true,maintainAspectRatio:false,interaction:{intersect:false,mode:"index"},plugins:{legend:{display:false},tooltip:{callbacks:{label:ctx=>`${LABELS[ctx.raw]||ctx.raw}`},backgroundColor:"rgba(10,12,28,0.97)",titleColor:"#fff",bodyColor:"rgba(255,255,255,0.6)",padding:8,cornerRadius:6}},scales:{y:{min:Math.max(0.5,Math.min(...chartData)-0.8),max:Math.min(5.5,Math.max(...chartData)+0.8),ticks:{stepSize:1,color:"rgba(255,255,255,0.35)",callback:v=>{if(!Number.isInteger(v)||v<1||v>5)return"";return LABELS[v]?LABELS[v].split("–")[0].trim():v;},padding:4},grid:{color:"rgba(255,255,255,0.05)"},border:{display:false}},x:{ticks:{color:"rgba(255,255,255,0.35)",maxRotation:chartData.length>45?45:0,maxTicksLimit:chartData.length>60?8:chartData.length>30?12:20,font:{size:10},padding:4},grid:{display:false},border:{display:false}}}}},chartWrap);
root.appendChild(chartWrap);

const calWrap=document.createElement("div"); calWrap.style.cssText=`height:${VIEW_HEIGHT};width:100%;box-sizing:border-box;display:${defaultView==="calendar"?"flex":"none"};flex-direction:column;gap:3px;`;
const weekRow=document.createElement("div"); weekRow.style.cssText="display:grid;grid-template-columns:repeat(7,1fr);gap:3px;flex-shrink:0;";
["D","S","T","Q","Q","S","S"].forEach(d=>{const el=document.createElement("div");el.textContent=d;el.style.cssText="text-align:center;font-size:0.6em;opacity:0.28;padding:1px 0;";weekRow.appendChild(el);});
calWrap.appendChild(weekRow);
const grid=document.createElement("div"); grid.style.cssText="display:grid;grid-template-columns:repeat(7,1fr);gap:3px;flex:1;";
const offset=startDate.day(); for(let i=0;i<offset;i++)grid.appendChild(document.createElement("div"));
for(const day of days){const cell=document.createElement("div");cell.innerHTML=`<div style="font-size:1.05em;line-height:1">${day.emoji}</div><div style="font-size:0.5em;opacity:0.5;margin-top:1px">${day.label}</div>`;cell.style.cssText=`display:flex;flex-direction:column;justify-content:center;align-items:center;border:1px solid ${day.color}55;border-radius:5px;background:rgba(56,189,248,0.03);cursor:default;transition:all 0.15s;min-height:0;`;cell.title=`${day.label} · ${day.emoji}`;cell.onmouseenter=()=>{cell.style.background=day.color+"1a";cell.style.transform="scale(1.06)";};cell.onmouseleave=()=>{cell.style.background="rgba(255,255,255,0.02)";cell.style.transform="";};grid.appendChild(cell);}
calWrap.appendChild(grid);root.appendChild(calWrap);

const setView=(view)=>{chartWrap.style.display=view==="chart"?"block":"none";calWrap.style.display=view==="calendar"?"flex":"none";btnChart._active=view==="chart";btnCal._active=view==="calendar";btnChart.style.background=btnChart._active?"rgba(255,255,255,0.1)":"transparent";btnChart.style.borderColor=`rgba(255,255,255,${btnChart._active?'0.25':'0.08'})`;btnCal.style.background=btnCal._active?"rgba(255,255,255,0.1)":"transparent";btnCal.style.borderColor=`rgba(255,255,255,${btnCal._active?'0.25':'0.08'})`;};
btnChart.onclick=()=>setView("chart"); btnCal.onclick=()=>setView("calendar");
dv.container.appendChild(root);
```

