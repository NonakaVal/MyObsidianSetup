

````tabs


tab: MOOD

```dataviewjs
const startDate = moment('01/05/2025', 'DD/MM/YYYY');
const endDate = moment('30/05/2025', 'DD/MM/YYYY');

const moodScale = {
  "😄 – Happy": 5, "🙂 – Neutral": 4, "😐 – Meh": 3, "😞 – Sad": 2, "😠 – Frustrated": 1
};

const moodColors = { 5: '#4caf50', 4: '#8bc34a', 3: '#ffc107', 2: '#ff9800', 1: '#f44336' };
const moodLabels = Object.fromEntries(Object.entries(moodScale).map(([k, v]) => [v, k]));

const labels = [], data = [], colors = [], pointStyles = [];
for (let p of dv.pages('#calendar/daily').sort(p => p.file.name, 'asc')) {
  const d = moment(p.file.name, 'YYYY-MM-DD');
  const mood = p["daily-mood"];
  const value = moodScale[mood];
  if (d.isBetween(startDate, endDate, null, '[]') && value) {
    labels.push(d.format('DD/MM/YY'));
    data.push(value);
    colors.push(moodColors[value]);
    pointStyles.push('circle');
  }
}

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
        title: {
          display: true,
          text: 'Estado Emocional',
          font: { size: 12, weight: 'bold' }
        },
        grid: { color: 'rgba(200, 200, 200, 0.1)' }
      },
      x: {
        ticks: {
          autoSkip: true,
          maxRotation: 45,
          minRotation: 30,
          font: { size: 10 }
        },
        title: {
          display: true,
          text: 'Data',
          font: { size: 12, weight: 'bold' }
        },
        grid: { display: false }
      }
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: ctx => `Humor: ${moodLabels[ctx.raw] || ctx.raw}`,
          title: ctx => moment(ctx[0].label, 'DD/MM/YY').format('DD MMMM YYYY')
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


tab: FOCUS

```dataviewjs
const pages = dv.pages();

// Defina o intervalo
const dataInicial = "2025-05-01";
const dataFinal = "2025-06-16";

const table = dv.markdownTable(
  ['Pomodoro', 'Duration', 'Begin', 'End'],
  pages.file.lists
    .filter(item => item.pomodoro)
    .filter(item => {
      const date = item?.end?.substring(0, 10);
      return date && date >= dataInicial && date <= dataFinal;
    })
    .sort(item => item.end, 'desc')
    .map(item => [
      item.pomodoro,
      `${item.duration.as("minutes")} m`,
      item.begin,
      item.end
    ])
);
dv.paragraph(table);



```
tab: DAILY LOG

```dataviewjs
// 📅 Define date range
const startDate = new Date("2025-01-01");
const endDate = new Date("2025-05-01");

// Load and filter pages by date
const pages = dv.pages('#calendar/daily')
    .where(p => {
        const fileDate = new Date(p.file.name);
        return fileDate >= startDate && fileDate <= endDate;
    })
    .sort(p => p.file.name, 'desc');

const headName = "Daily Log";
let tableRows = [];

for (const page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split('\n');
    let insideHead = false;
    let sectionContent = [];

    for (const line of lines) {
        if (line.startsWith("# " + headName)) {
            insideHead = true;
            continue;[[SNIP-DAILY-LOG-DATAVIEW]]
        }
        if (line.startsWith("# ") && insideHead) {
            break;
        }
        if (insideHead) {
            const trimmedLine = line.trim();

            // Ignore Recording links in wikilink format
            if (/\[\[Recording\s\d{14}(\.m4a)?\]\]/.test(trimmedLine)) continue;

            // Ignore Swiftink-style obsidian:// links
            if (/\[.*?\]\(obsidian:\/\/swiftink_transcript_functions\?id=[\w-]+\)/.test(trimmedLine)) continue;

            sectionContent.push(trimmedLine);
        }
    }

    if (sectionContent.length > 0) {
        tableRows.push([
            page.file.link,
            sectionContent.join('\n')
        ]);
    }
}

dv.table(["🗓️", "📝"], tableRows);
```
````