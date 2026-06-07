
```dataviewjs
// ── CONFIGURAÇÃO DO INTERVALO ──────────────────────────────────────────
const startDate = moment("2026-<% tp.system.prompt("Start Date - (MM-DD)")%>", "YYYY-MM-DD");
const endDate   = moment("2026-<% tp.system.prompt("End Date - (MM-DD)")%>", "YYYY-MM-DD");
 
const SCALE = { "😄 – Happy":5, "🙂 – Neutral":4, "😐 – Meh":3, "😞 – Sad":2, "😠 – Frustrated":1 };
const COLORS = { 5:'#38bdf8', 4:'#818cf8', 3:'#a78bfa', 2:'#f472b6', 1:'#f87171' };
const LABELS = Object.fromEntries(Object.entries(SCALE).map(([k,v]) => [v, k]));

let labels = [], data = [], colors = [], total = 0, count = 0;
for (const p of dv.pages("#calendar/daily").sort(p => p.file.name, 'asc')) {
  const d = moment(p.file.name, 'YYYY-MM-DD');
  const v = SCALE[p["daily-mood"]];
  if (d.isBetween(startDate, endDate, null, '[]') && v) {
    labels.push(d.format('DD/MM')); data.push(v); colors.push(COLORS[v]); total += v; count++;
  }
}

const avg = count ? (total / count).toFixed(1) : 0;
let trend = "→";
if (data.length >= 4) {
  const h = Math.floor(data.length / 2);
  const a1 = data.slice(0, h).reduce((a,b) => a+b, 0) / h;
  const a2 = data.slice(h).reduce((a,b) => a+b, 0) / (data.length - h);
  if (a2 > a1 + 0.3) trend = "↑"; else if (a2 < a1 - 0.3) trend = "↓";
}

const root = dv.el("div", "");
root.style.cssText = `
  background:rgba(10,12,20,0.97); border-radius:8px;
  padding:10px 12px; color:#fff;
  width:100%; box-sizing:border-box;
`;

const header = document.createElement("div");
header.style.cssText = "display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;font-size:0.78em;opacity:0.55;";
header.innerHTML = `<span>📈 mood diário · ${startDate.format('DD/MM')} → ${endDate.format('DD/MM/YY')}</span><span>${trend} avg ${avg}</span>`;
root.appendChild(header);

const chart = dv.el("div", "");
chart.style.cssText = "width:100%;max-height:640px;min-height:140px;";
root.appendChild(chart);

window.renderChart({
  type: 'line',
  data: {
    labels,
    datasets: [{
      data,
      borderColor: '#ffffff',
      backgroundColor: 'rgba(56,189,248,0.08)',
      pointBackgroundColor: colors,
      pointBorderColor: colors,
      borderWidth: 1.5,
      tension: 0.35,
      fill: true,
      pointRadius: 3,
      pointHoverRadius: 5
    }]
  },
  options: {
    responsive: true, maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: {
        callbacks: { label: c => `${LABELS[c.raw] || c.raw}` },
        backgroundColor: 'rgba(20,20,20,0.95)',
        titleColor: '#fff', bodyColor: '#aaa', padding: 8
      }
    },
    scales: {
      y: {
        min: 0.5, max: 5.5,
        ticks: { stepSize: 1, color: 'rgba(255,255,255,0.4)', callback: v => { if(!Number.isInteger(v)||v<1||v>5) return ''; return LABELS[v]?LABELS[v].split('–')[0].trim():v; } },
        grid: { color: 'rgba(56,189,248,0.07)' }, border: { display: false }
      },
      x: {
        ticks: { color: 'rgba(255,255,255,0.4)', maxRotation: 0, font: { size: 10 } },
        grid: { display: false }, border: { display: false }
      }
    }
  }
}, chart);
dv.container.appendChild(root);
```
