---
created: "[[2025-06-08]]"
cssclasses: wide-page
---
```dataviewjs
// =============================
// 📊 ANÁLISE DE HUMOR (7 dias)
// =============================
const startDate = moment('2025-10-18', 'YYYY-MM-DD');
const endDate = moment('2025-10-25', 'YYYY-MM-DD');

const moodScale = {
    "😄 – Happy": 5, "🙂 – Neutral": 4, "😐 – Meh": 3, "😞 – Sad": 2, "😠 – Frustrated": 1
};

const moodColors = { 5: '#4caf50', 4: '#8bc34a', 3: '#ffc107', 2: '#ff9800', 1: '#f44336' };
const moodLabels = Object.fromEntries(Object.entries(moodScale).map(([k, v]) => [v, k]));

const labels = [], data = [], colors = [];
const moodCount = {};
let totalValue = 0;
let daysWithMood = 0;

// Coleta dados
for (let p of dv.pages('#calendar/daily').sort(p => p.file.name, 'asc')) {
    const d = moment(p.file.name, 'YYYY-MM-DD');
    const mood = p["daily-mood"];
    const value = moodScale[mood];

    if (d.isBetween(startDate, endDate, null, '[]') && value) {
        labels.push(d.format('DD/MM'));
        data.push(value);
        colors.push(moodColors[value]);
        moodCount[value] = (moodCount[value] || 0) + 1;
        totalValue += value;
        daysWithMood++;
    }
}

// =============================
// 📈 RESUMO DE HUMOR
// =============================
const averageMood = daysWithMood > 0 ? (totalValue / daysWithMood).toFixed(1) : 0;

// Encontrar humor mais frequente
let mostFrequentMood = null;
let maxCount = 0;
for (const [value, count] of Object.entries(moodCount)) {
    if (count > maxCount) {
        maxCount = count;
        mostFrequentMood = parseInt(value);
    }
}

// Determinar tendência
let trend = "→ Estável";
if (data.length >= 2) {
    const firstHalf = data.slice(0, Math.floor(data.length / 2));
    const secondHalf = data.slice(Math.floor(data.length / 2));
    const avgFirst = firstHalf.reduce((a, b) => a + b, 0) / firstHalf.length;
    const avgSecond = secondHalf.reduce((a, b) => a + b, 0) / secondHalf.length;
    
    if (avgSecond > avgFirst + 0.3) trend = "📈 Melhorando";
    else if (avgSecond < avgFirst - 0.3) trend = "📉 Piorando";
}

// Criar resumo
const summaryDiv = dv.el("div", "");
summaryDiv.style.cssText = `
    background: rgba(0, 0, 0, 0.7);
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    border-left: 4px solid #7e57c2;
`;

// Estatísticas principais
const statsHTML = `
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-bottom: 15px;">
    <div style="text-align: center; padding: 12px; background: rgba(255,255,255,0.15); border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 0.9em; color: #e0e0e0; margin-bottom: 5px;">📅 Período</div>
        <div style="font-weight: bold; font-size: 1.1em; color: #ffffff;">${startDate.format('DD/MM')} - ${endDate.format('DD/MM')}</div>
    </div>
    <div style="text-align: center; padding: 12px; background: rgba(255,255,255,0.15); border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 0.9em; color: #e0e0e0; margin-bottom: 5px;">📊 Média</div>
        <div style="font-weight: bold; font-size: 1.1em; color: ${moodColors[Math.round(averageMood)] || '#ffffff'}">${averageMood}/5</div>
    </div>
    <div style="text-align: center; padding: 12px; background: rgba(255,255,255,0.15); border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 0.9em; color: #e0e0e0; margin-bottom: 5px;">🎯 Mais Frequente</div>
        <div style="font-weight: bold; font-size: 1.1em; color: #ffffff;">${mostFrequentMood ? moodLabels[mostFrequentMood].split(' – ')[0] : 'N/A'}</div>
    </div>
    <div style="text-align: center; padding: 12px; background: rgba(255,255,255,0.15); border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
        <div style="font-size: 0.9em; color: #e0e0e0; margin-bottom: 5px;">🔍 Tendência</div>
        <div style="font-weight: bold; font-size: 1.1em; color: #ffffff;">${trend}</div>
    </div>
</div>

<div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 8px; background: rgba(255,255,255,0.1); padding: 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.15);">
`;

// Adicionar contadores de cada humor
let summaryHTML = statsHTML;
Object.entries(moodScale).forEach(([label, value]) => {
    const count = moodCount[value] || 0;
    const percentage = daysWithMood > 0 ? ((count / daysWithMood) * 100).toFixed(0) : 0;
    const emoji = label.split(' – ')[0];
    
    summaryHTML += `
    <div style="text-align: center; min-width: 70px; padding: 10px; background: rgba(0,0,0,0.3); border-radius: 6px; border: 1px solid rgba(255,255,255,0.1);">
        <div style="font-size: 1.8em; margin-bottom: 5px;">${emoji}</div>
        <div style="font-weight: bold; font-size: 1.3em; color: #ffffff; margin-bottom: 3px;">${count}</div>
        <div style="font-size: 0.85em; color: #b0b0b0; font-weight: 500;">${percentage}%</div>
    </div>`;
});

summaryHTML += `</div>`;
summaryDiv.innerHTML = summaryHTML;

// =============================
// 📊 GRÁFICO
// =============================
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
            pointRadius: 6,
            pointHoverRadius: 8
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { intersect: false, mode: 'index' },
        layout: {
            padding: 10
        },
        plugins: {
            legend: { display: false },
            tooltip: {
                callbacks: {
                    label: ctx => `Humor: ${moodLabels[ctx.raw] || ctx.raw}`
                },
                backgroundColor: 'rgba(30, 30, 30, 0.9)',
                titleColor: '#ffffff',
                bodyColor: '#ffffff'
            }
        },
        scales: {
            y: {
                min: 0.5, max: 5.5,
                ticks: {
                    stepSize: 1,
                    color: '#ffffff',
                    backdropColor: 'rgba(0, 0, 0, 0.5)',
                    callback: val => moodLabels[val] || val,
                    padding: 6
                },
                grid: { color: 'rgba(200, 200, 200, 0.2)' }
            },
            x: {
                ticks: {
                    color: '#ffffff',
                    backdropColor: 'rgba(0, 0, 0, 0.5)',
                    padding: 6
                },
                grid: { display: false }
            }
        }
    }
};

// Container do gráfico
const chartContainer = dv.el("div", "");
Object.assign(chartContainer.style, {
    height: '250px',
    width: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    borderRadius: '8px',
    padding: '10px',
    marginTop: '10px'
});

// =============================
// 🚀 RENDERIZAÇÃO
// =============================
// Adicionar resumo primeiro
dv.container.appendChild(summaryDiv);

// Adicionar gráfico
dv.container.appendChild(chartContainer);
window.renderChart(chartData, chartContainer);
```
