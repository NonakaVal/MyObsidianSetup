---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---

<< [[<% moment(tp.file.title,'YYYY-MM').add(-1,'month').format("YYYY-MM") %>|⏪ Last month(<% moment(tp.file.title,'YYYY-MM').add(-1,'month').format("YYYY-MM") %>)]] | [[<% moment(tp.file.title,'YYYY-MM').add(1,'month').format("YYYY-MM") %>|Next month(<% moment(tp.file.title,'YYYY-MM').add(1,'month').format("YYYY-MM") %>) ⏩]] >>


---

```dataviewjs
const startDate = moment('<% tp.system.prompt("StartDate (YYYY-MM-DD)")%>', 'YYYY-MM-DD');
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');

const pages = dv.pages('#calendar/daily')
    .where(p => {
        const fileDate = moment(p.file.name, "YYYY-MM-DD");
        return fileDate.isBetween(startDate, endDate, null, '[]');
    })
    .sort(p => p.file.name, 'desc');

const headName = "Logs";
let tableRows = [];

const excludePatterns = [
    /\[\[Recording\s\d{14}(\.m4a)?\]\]/,
    /\[.*?\]\(obsidian:\/\/swiftink_transcript_functions\?id=[\w-]+\)/,
    /INPUT\[.*?option\(.*?\).*?\]/,
    /Áudio do WhatsApp de \d{4}-\d{2}-\d{2} à\(s\) \d{2}\.\d{2}\.\d{2}_[\w\d]+\.waptt\.opus/
];

for (const page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split('\n');
    let insideHead = false;
    let sectionContent = [];

    for (const line of lines) {
        if (line.startsWith("# " + headName)) { insideHead = true; continue; }
        if (line.startsWith("# ") && insideHead) break;
        if (insideHead) {
            const trimmedLine = line.trim();
            if (excludePatterns.some(pattern => pattern.test(trimmedLine))) continue;
            sectionContent.push(trimmedLine);
        }
    }

    if (sectionContent.length > 0) {
        tableRows.push([
            page.file.link,
            sectionContent.join('<li>')
        ]);
    }
}

dv.table(["🗓️ Data", "📝 Conteúdo"], tableRows);

```

---
---


```dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const startDate = moment('<% tp.system.prompt("StartDate (YYYY-MM-DD)")%>', 'YYYY-MM-DD');
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');

const moodScale = {
  "😄 – Happy": 5, "🙂 – Neutral": 4, "😐 – Meh": 3, "😞 – Sad": 2, "😠 – Frustrated": 1
};

const moodColors = { 5: '#4caf50', 4: '#8bc34a', 3: '#ffc107', 2: '#ff9800', 1: '#f44336' };
const moodLabels = Object.fromEntries(Object.entries(moodScale).map(([k, v]) => [v, k]));

const labels = [], data = [], colors = [], pointStyles = [];
const moodCount = {}; // contador por humor
let totalValue = 0;

for (let p of dv.pages('#calendar/daily').sort(p => p.file.name, 'asc')) {
  const d = moment(p.file.name, 'YYYY-MM-DD');
  const mood = p["daily-mood"];
  const value = moodScale[mood];

  if (d.isBetween(startDate, endDate, null, '[]') && value) {
    labels.push(d.format('DD/MM/YYYY'));
    data.push(value);
    colors.push(moodColors[value]);
    pointStyles.push('circle');

    // Contagem de cada humor
    moodCount[value] = (moodCount[value] || 0) + 1;

    // Soma para média
    totalValue += value;
  }
}

// --- GRÁFICO ---
const chartData = {
  type: 'line',
  data: {
    labels,
    datasets: [{
      data,
      borderColor: '#7e57c2',
      backgroundColor: 'rgba(126, 87, 194, 0.1)',
      pointBackgroundColor: colors,
      pointBorderColor: colors,
      borderWidth: 2,
      tension: 0.3,
      fill: true,
      pointRadius: 5,
      pointHoverRadius: 7,
      pointStyle: pointStyles
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    interaction: { intersect: false, mode: 'index' },
    scales: {
      y: {
        min: 0.5, max: 5.5,
        ticks: {
          stepSize: 1,
          callback: val => moodLabels[val] || val,
          font: { size: 11 }
        },
        title: { display: true, text: 'Estado Emocional', font: { size: 12, weight: 'bold' } },
        grid: { color: 'rgba(200, 200, 200, 0.1)' }
      },
      x: {
        ticks: { autoSkip: true, maxRotation: 45, minRotation: 30, font: { size: 10 } },
        title: { display: true, text: 'Data', font: { size: 12, weight: 'bold' } },
        grid: { display: false }
      }
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: ctx => `Humor: ${moodLabels[ctx.raw] || ctx.raw}`,
          title: ctx => moment(ctx[0].label, 'DD/MM/YYYY').format('DD MMMM YYYY')
        },
        displayColors: true,
        backgroundColor: 'rgba(30, 30, 30, 0.9)',
        titleFont: { size: 12 }, bodyFont: { size: 12 }
      },
      legend: { display: false },
      title: { display: false }
    }
  }
};

Object.assign(this.container.style, { height: '450px', width: '100%' });
window.renderChart(chartData, this.container);


```



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
  { icon: "🎞️", name: "Estresse / Sobrecarga" },
  { icon: "🎨", name: "Reflexões / Emoções" },
  { icon: "✅", name: "Conquistas / Realizações" },
  { icon: "⚡", name: "Insights / Ideias" },
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




---
---

