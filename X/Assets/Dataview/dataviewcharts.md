---
tags:
  - calendar/review
dateCreated: "[[2026-03-04]]"
---

# Totais

```dataviewjs
// 🗺️ OVERVIEW — 7 dias
const DAYS=31;
const SCALE={"😄 – Happy":5,"🙂 – Neutral":4,"😐 – Meh":3,"😞 – Sad":2,"😠 – Frustrated":1};
const EMOJIS={5:'😄',4:'🙂',3:'😐',2:'😞',1:'😠'};
const CATS=[{icon:"💡"},{icon:"⭐"},{icon:"😴"},{icon:"💀"},{icon:"🌱"},{icon:"💩"},{icon:"❓"},{icon:"🧭"},{icon:"💬"},{icon:"🍅"},{icon:"🥤"}];
const now=moment();
const endC=now.clone(),startC=now.clone().subtract(DAYS,'days');
const endP=startC.clone(),startP=endP.clone().subtract(DAYS,'days');
const getStats=async(s,e)=>{
  const ps=dv.pages("#calendar/daily").where(p=>{const d=moment(p.file.name,'YYYY-MM-DD');return d.isBetween(s,e,null,'[]');});
  let mt=0,mn=0,lt=0;
  for(const p of ps){const v=SCALE[p["daily-mood"]];if(v){mt+=v;mn++;}
    const c=await dv.io.load(p.file.path);const ls=c.split('\n');let in_=false;
    for(const l of ls){if(l.startsWith('# Capture')){in_=true;continue;}if(l.startsWith('# ')&&in_)break;if(in_&&l.trim()&&CATS.some(c=>l.includes(c.icon)))lt++;}
  }
  return{avg:mn?mt/mn:0,days:mn,logs:lt};
};
const[cur,prev]=await Promise.all([getStats(startC,endC),getStats(startP,endP)]);
const EMOJIS5={5:'😄',4:'🙂',3:'😐',2:'😞',1:'😠'};
const df=(a,b)=>{if(!b||b===0)return'';const p=((a-b)/b*100).toFixed(0);return a>b?`<span style="color:#4caf50;font-size:0.7em"> +${p}%</span>`:a<b?`<span style="color:#f44336;font-size:0.7em"> ${p}%</span>`:`<span style="opacity:0.3;font-size:0.7em"> —</span>`;};
const root=dv.el("div","");root.style.cssText="background:rgba(15,15,20,0.95);border-radius:8px;padding:10px 14px;color:#fff;";
const g=document.createElement("div");g.style.cssText="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;";
[{l:'Humor médio',v:`${EMOJIS5[Math.round(cur.avg)]||''} ${cur.avg.toFixed(1)}`,d:df(cur.avg,prev.avg)},{l:'Dias',v:cur.days,d:df(cur.days,prev.days)},{l:'Logs',v:cur.logs,d:df(cur.logs,prev.logs)}].forEach(k=>{
  const c=document.createElement("div");c.style.cssText="border:1px solid rgba(255,255,255,0.07);border-radius:6px;padding:8px 10px;";
  c.innerHTML=`<div style="font-size:0.62em;opacity:0.4;margin-bottom:3px;text-transform:uppercase">${k.l}</div><div style="font-size:1.3em;font-weight:700">${k.v}${k.d}</div>`;g.appendChild(c);});
root.appendChild(g);dv.container.appendChild(root);
````

