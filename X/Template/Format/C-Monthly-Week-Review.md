---
cssclasses:
  - wide-page
dateCreated: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
tags:
  - calendar/review
date-start: <% tp.system.prompt("start-date YYYY-MM-DD") %>
date-end: <% tp.system.prompt("end-date YYYY-MM-DD") %>
period: '[[<% tp.date.now("YYYY [Week] WW") %>]]'
month-ref: '[[<% tp.date.now("YYYY-MM") %>]]'
---


```dataviewjs
// =============================
// 📊 MOOD: LINE CHART BY NOTE PROPERTIES (NO TOP-LEVEL RETURN)
// =============================
const CONFIG = { tag: "#calendar/daily" };

// ---------------------------
// Mood maps
// ---------------------------
const moodScale = {
  "😄 – Happy": 5,
  "🙂 – Neutral": 4,
  "😐 – Meh": 3,
  "😞 – Sad": 2,
  "😠 – Frustrated": 1
};

const moodColors = {
  5: "#4caf50",
  4: "#8bc34a",
  3: "#ffc107",
  2: "#ff9800",
  1: "#f44336"
};

const moodLabels = Object.fromEntries(
  Object.entries(moodScale).map(([k, v]) => [v, k])
);

// ---------------------------
// Read note properties
// ---------------------------
const current = dv.current();
const startRaw = current["date-start"];
const endRaw = current["date-end"];
const period = current["period"];

let ok = true;

if (!startRaw || !endRaw) {
  dv.paragraph("⚠️ Missing frontmatter properties: `date-start` and/or `date-end`.");
  ok = false;
}

const startDate = ok ? moment(startRaw, "YYYY-MM-DD", true) : null;
const endDate = ok ? moment(endRaw, "YYYY-MM-DD", true) : null;

if (ok && (!startDate.isValid() || !endDate.isValid())) {
  dv.paragraph("⚠️ Invalid date format. Use `YYYY-MM-DD` in `date-start` and `date-end`.");
  ok = false;
}

if (ok && endDate.isBefore(startDate)) {
  dv.paragraph("⚠️ `date-end` is before `date-start`. Please fix the range.");
  ok = false;
}

// ---------------------------
// Collect data
// ---------------------------
if (ok) {
  const pages = dv.pages(CONFIG.tag).sort(p => p.file.name, "asc");

  const chartLabels = [];
  const chartData = [];
  const chartColors = [];

  let totalValue = 0;
  let daysWithMood = 0;

  for (const p of pages) {
    const d = moment(p.file.name, "YYYY-MM-DD", true);
    if (!d.isValid()) continue;

    const mood = p["daily-mood"];
    const value = moodScale[mood];

    if (d.isBetween(startDate, endDate, null, "[]") && value) {
      chartLabels.push(d.format("DD/MM"));
      chartData.push(value);
      chartColors.push(moodColors[value]);
      totalValue += value;
      daysWithMood++;
    }
  }

  const averageMood = daysWithMood ? (totalValue / daysWithMood).toFixed(1) : "0.0";

  let trend = "→ Stable";
  if (chartData.length >= 2) {
    const splitIndex = Math.floor(chartData.length / 2);
    const firstHalf = chartData.slice(0, splitIndex);
    const secondHalf = chartData.slice(splitIndex);

    if (firstHalf.length && secondHalf.length) {
      const avgFirst = firstHalf.reduce((a, b) => a + b, 0) / firstHalf.length;
      const avgSecond = secondHalf.reduce((a, b) => a + b, 0) / secondHalf.length;

      if (avgSecond > avgFirst + 0.3) trend = "📈 Improving";
      else if (avgSecond < avgFirst - 0.3) trend = "📉 Declining";
    }
  }

  // ---------------------------
  // Root container
  // ---------------------------
  const root = dv.el("div", "");
  root.style.cssText = `
    display:flex;
    flex-direction:column;
    gap:8px;
    color:#fff;
    background: rgba(20,20,25,0.9);
    padding:10px;
    border-radius:10px;
    max-width:2890px;
  `;

  const meta = document.createElement("div");
  meta.style.cssText = `
    font-size:0.9em;
    opacity:0.9;
    margin-bottom:6px;
  `;
  meta.innerHTML = `
    <div><strong>${period ?? "Selected Period"}</strong></div>
    <div>${startDate.format("DD/MM/YYYY")} → ${endDate.format("DD/MM/YYYY")}</div>
    <div>Average: ${averageMood} | Trend: ${trend}</div>
  `;
  root.appendChild(meta);

  // ---------------------------
  // Line chart
  // ---------------------------
  const chartDiv = dv.el("div", "");
  chartDiv.style.cssText = `
    height:250px;
    width:100%;
    background-color:rgba(0,0,0,0.7);
    border-radius:8px;
    padding:8px;
    display:block;
  `;

  const chartConfig = {
    type: "line",
    data: {
      labels: chartLabels,
      datasets: [{
        data: chartData,
        borderColor: "#7e57c2",
        backgroundColor: "rgba(126,87,194,0.08)",
        pointBackgroundColor: chartColors,
        pointBorderColor: chartColors,
        borderWidth: 2,
        tension: 0.3,
        fill: true,
        pointRadius: 4,
        pointHoverRadius: 6
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { intersect: false, mode: "index" },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => `Mood: ${moodLabels[ctx.raw] || ctx.raw}` },
          backgroundColor: "rgba(30,30,30,0.9)",
          titleColor: "#fff",
          bodyColor: "#fff"
        }
      },
      scales: {
        y: {
          min: 0.5,
          max: 5.5,
          ticks: {
            stepSize: 1,
            color: "#fff",
            callback: val => moodLabels[val] || val,
            padding: 4
          },
          grid: { color: "rgba(200,200,200,0.2)" }
        },
        x: {
          ticks: { color: "#fff", padding: 4 },
          grid: { display: false }
        }
      }
    }
  };

  root.appendChild(chartDiv);
  window.renderChart(chartConfig, chartDiv);
  dv.container.appendChild(root);
}
```