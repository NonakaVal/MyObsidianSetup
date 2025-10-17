
```dataviewjs
//-----------------------------------------------------
// ⚙️ CONFIGURAÇÃO DE INTERVALO
//-----------------------------------------------------
const startDate = moment('<% tp.system.prompt("StartDate (YYYY-MM-DD)")%>', 'YYYY-MM-DD');
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');

//-----------------------------------------------------
// 📚 CATEGORIAS DE LOGS
//-----------------------------------------------------
const categories = [
  { icon: "🧩", name: "Aprendizado" },
  { icon: "⭐", name: "Algo muito bom" },
  { icon: "😞", name: "Frustração / Erros" },
  { icon: "😤", name: "Estresse / Sobrecarga" },
  { icon: "🤔", name: "Reflexões / Emoções" },
  { icon: "✅", name: "Conquistas / Realizações" },
  { icon: "💡", name: "Insights / Ideias" },
  { icon: "⚠️", name: "Obstáculos" },
  { icon: "🪴", name: "Hábitos / Rotina" },
];

//-----------------------------------------------------
// 📥 COLETA DE DADOS
//-----------------------------------------------------
let totals = Object.fromEntries(categories.map(c => [c.icon, 0]));
let totalLogs = 0;

for (const page of dv.pages("#calendar/daily")) {
  const fileDate = moment(page.file.name, "YYYY-MM-DD");
  if (!fileDate.isBetween(startDate, endDate, null, "[]")) continue;

  const content = await dv.io.load(page.file.path);
  const lines = content.split("\n");
  let insideLogs = false;

  for (let line of lines) {
    line = line.trim();
    if (/^#{1,3}\s*logs/i.test(line)) { insideLogs = true; continue; }
    if (insideLogs && /^#{1,3}\s+\w+/.test(line)) break;
    if (!insideLogs || !line.startsWith("-")) continue;

    for (const cat of categories) {
      if (line.includes(cat.icon)) {
        totals[cat.icon]++;
        totalLogs++;
        break;
      }
    }
  }
}



//-----------------------------------------------------
// 📊 PREPARAÇÃO DO GRÁFICO
//-----------------------------------------------------
const maxCount = Math.max(...Object.values(totals), 1);
const sortedCategories = categories
  .map(cat => ({ ...cat, count: totals[cat.icon] }))
  .sort((a, b) => b.count - a.count);

//-----------------------------------------------------
// 🖌️ RENDERIZAÇÃO DO GRÁFICO HORIZONTAL
//-----------------------------------------------------
let chartHTML1 = `<h5>📊 Logs (${startDate.format("DD/MM")} → ${endDate.format("DD/MM")})</h5>
<div style="display:flex; flex-direction:column; gap:4px; max-width:500px;">`;

for (const cat of sortedCategories) {
  const widthPercent = (cat.count / maxCount) * 100;
  chartHTML1 += `
  <div style="display:flex; justify-content:space-between; align-items:center; gap:6px;">
    <span style="width:150px;">${cat.icon} ${cat.name}</span>
    <div style="flex-grow:1; background:#ddd; border-radius:6px; height:16px;">
      <div style="width:${widthPercent}%; background:#5b7aaa; height:100%; border-radius:6px;"></div>
    </div>
    <span>${cat.count}</span>
  </div>`;
}

chartHTML1 += `</div>
<p>🧮 Total de logs: <strong>${totalLogs}</strong></p>`;

dv.paragraph(chartHTML1);

```
