```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");

const SCALE  = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const COLORS = { 5:'#38bdf8', 4:'#818cf8', 3:'#a78bfa', 2:'#f472b6', 1:'#f87171' };
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
  const pages = dv.pages("#calendar/daily").where(p => moment(p.file.name,"YYYY-MM-DD").isBetween(s,e,null,"[]"));
  let moodCount={}, moodData=[], moodTotal=0, moodN=0;
  let catTotals=Object.fromEntries(CATS.map(c=>[c.name,{icon:c.icon,count:0}])); let logTotal=0;
  for (const p of pages) {
    const v=SCALE[p["daily-mood"]];
    if(v){moodCount[v]=(moodCount[v]||0)+1; moodData.push(v); moodTotal+=v; moodN++;}
    const lines=(await dv.io.load(p.file.path)).split("\n"); let ins=false;
    for(const l of lines){if(l.startsWith("# Capture")){ins=true;continue;}if(l.startsWith("# ")&&ins)break;if(ins&&l.trim()){const cat=CATS.find(c=>l.includes(c.icon));if(cat){catTotals[cat.name].count++;logTotal++;}}}
  }
  let trend="→";
  if(moodData.length>=4){const h=Math.floor(moodData.length/2);const a1=moodData.slice(0,h).reduce((a,b)=>a+b,0)/h;const a2=moodData.slice(h).reduce((a,b)=>a+b,0)/(moodData.length-h);if(a2>a1+0.3)trend="↑";else if(a2<a1-0.3)trend="↓";}
  return {avg:moodN?moodTotal/moodN:0,days:moodN,logs:logTotal,moodCount,catTotals,trend};
};

const [cur,prev]=await Promise.all([getData(startDate,endDate),getData(startPrev,endPrev)]);

const delta=(a,b)=>{if(!b)return"";const p=((a-b)/b*100).toFixed(0);if(a>b)return`<span style="color:#38bdf8"> +${p}%</span>`;if(a<b)return`<span style="color:#f87171"> ${p}%</span>`;return`<span style="opacity:0.25"> —</span>`;};

const root=dv.el("div","");
root.style.cssText=`background:rgba(10,12,20,0.97);border-radius:8px;padding:8px 10px;color:#fff;display:flex;flex-direction:column;gap:8px;width:100%;box-sizing:border-box;font-size:0.85em;`;

const period=document.createElement("div"); period.style.cssText="font-size:0.68em;opacity:0.3;"; period.textContent=`${startDate.format("DD/MM")} → ${endDate.format("DD/MM/YYYY")} · ${duration}d`; root.appendChild(period);

const kpiRow=document.createElement("div"); kpiRow.style.cssText="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;";
[{label:"humor",value:`${EMOJIS[Math.round(cur.avg)]||""} ${cur.avg.toFixed(1)}`,d:delta(cur.avg,prev.avg)},{label:"dias",value:cur.days,d:delta(cur.days,prev.days)},{label:"logs",value:cur.logs,d:delta(cur.logs,prev.logs)}].forEach(k=>{const c=document.createElement("div");c.style.cssText="border:1px solid rgba(56,189,248,0.08);border-radius:5px;padding:5px 7px;";c.innerHTML=`<div style="font-size:0.6em;opacity:0.35;text-transform:uppercase;letter-spacing:0.3px">${k.label}</div><div style="font-size:1.05em;font-weight:700;line-height:1.3">${k.value}<span style="font-size:0.7em">${k.d}</span></div>`;kpiRow.appendChild(c);});
root.appendChild(kpiRow);

const dom=Object.entries(cur.moodCount).sort((a,b)=>b[1]-a[1])[0];
const moodRow=document.createElement("div"); moodRow.style.cssText="display:flex;align-items:center;gap:8px;";
const moodLabel=document.createElement("div"); moodLabel.style.cssText="flex-shrink:0;font-size:1.4em;line-height:1;"; moodLabel.textContent=dom?EMOJIS[dom[0]]:"–"; moodRow.appendChild(moodLabel);
const bars=document.createElement("div"); bars.style.cssText="flex:1;display:flex;flex-direction:column;gap:2px;";
for(let v=5;v>=1;v--){const pct=cur.days?Math.round(((cur.moodCount[v]||0)/cur.days)*100):0;const b=document.createElement("div");b.style.cssText="display:grid;grid-template-columns:14px 1fr 20px;gap:4px;align-items:center;";b.innerHTML=`<span style="font-size:0.7em;text-align:center">${EMOJIS[v]}</span><div style="height:4px;border-radius:2px;background:rgba(56,189,248,0.07)"><div style="height:100%;width:${pct}%;background:${COLORS[v]};border-radius:2px"></div></div><span style="font-size:0.6em;opacity:0.35;text-align:right">${cur.moodCount[v]||0}</span>`;bars.appendChild(b);}
moodRow.appendChild(bars);
const trendBadge=document.createElement("div"); trendBadge.style.cssText="flex-shrink:0;font-size:0.7em;opacity:0.45;text-align:right;line-height:1.4;"; trendBadge.innerHTML=`${cur.trend}<br><span style="opacity:0.6">${cur.avg.toFixed(1)}/5</span>`; moodRow.appendChild(trendBadge);
root.appendChild(moodRow);

const catWrap=document.createElement("div"); catWrap.style.cssText="display:flex;flex-wrap:wrap;gap:4px;";
const sortedCats=Object.entries(cur.catTotals).sort((a,b)=>b[1].count-a[1].count).filter(([,v])=>v.count>0);
for(const [name,info] of sortedCats){const prevCount=prev.catTotals[name]?.count||0;const pill=document.createElement("div");pill.title=name;pill.style.cssText=`display:inline-flex;align-items:center;gap:3px;padding:3px 7px;background:rgba(255,255,255,0.04);border:1px solid rgba(56,189,248,0.08);border-radius:20px;font-size:0.75em;white-space:nowrap;`;pill.innerHTML=`${info.icon} <span style="font-weight:600">${info.count}</span> <span style="font-size:0.8em">${delta(info.count,prevCount)}</span>`;catWrap.appendChild(pill);}
root.appendChild(catWrap);
dv.container.appendChild(root);
```
****