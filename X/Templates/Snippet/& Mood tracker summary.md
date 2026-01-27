
```dataviewjs
// =============================
// 📊 RESUMO DE HUMOR ÚTIL - 30 DIAS
// =============================
const CONFIG = { tag: "#calendar/daily", rangeDays: <% tp.system.prompt("range days num")%>};

const moodScale = { 
    "😄 – Happy": 5, 
    "🙂 – Neutral": 4, 
    "😐 – Meh": 3, 
    "😞 – Sad": 2, 
    "😠 – Frustrated": 1 
};

const moodColors = { 
    5: '#4caf50', 
    4: '#8bc34a', 
    3: '#ffc107', 
    2: '#ff9800', 
    1: '#f44336' 
};

// Datas
const endDate = moment();
const startDate = moment(endDate).subtract(CONFIG.rangeDays - 1, 'days');

// Inicialização
let moodCount = {};
let totalValue = 0;
let daysWithMood = 0;
let lastMood = null;

// Coleta de dados
const pages = dv.pages(CONFIG.tag).sort(p => p.file.name, 'asc');
for (const p of pages) {
    const d = moment(p.file.name, 'YYYY-MM-DD');
    if (!d.isBetween(startDate, endDate, null, '[]')) continue;

    const value = moodScale[p["daily-mood"]];
    if (!value) continue;

    moodCount[value] = (moodCount[value] || 0) + 1;
    totalValue += value;
    daysWithMood++;

    lastMood = p["daily-mood"];
}

// Cálculos
const averageMood = daysWithMood ? (totalValue / daysWithMood).toFixed(1) : 0;
const mostFrequent = Object.entries(moodCount)
    .reduce((a,[v,c]) => c > a.count ? {value:v, count:c} : a, {value:null, count:0});

// Tendência
let trend = { icon: "→", text: "Estável", color: "#fff" };
if (daysWithMood >= 4) {
    const moods = Array.from(
        pages
            .filter(p => p["daily-mood"] && moment(p.file.name, 'YYYY-MM-DD').isBetween(startDate, endDate, null, '[]'))
            .map(p => moodScale[p["daily-mood"]])
            .filter(Boolean)
    );

    const half = Math.floor(moods.length / 2);
    if (half > 0 && moods.length - half > 0) {
        const firstAvg = moods.slice(0, half).reduce((a,b) => a + b, 0) / half;
        const secondAvg = moods.slice(half).reduce((a,b) => a + b, 0) / (moods.length - half);
        
        if (secondAvg > firstAvg + 0.3) trend = { icon: "📈", text: "Melhorando", color: "#4caf50" };
        else if (secondAvg < firstAvg - 0.3) trend = { icon: "📉", text: "Piorando", color: "#f44336" };
    }
}

// Cálculos úteis adicionais
const positiveDays = ((moodCount[5] || 0) + (moodCount[4] || 0));
const neutralDays = (moodCount[3] || 0);
const negativeDays = ((moodCount[2] || 0) + (moodCount[1] || 0));

const pctPositive = daysWithMood ? ((positiveDays / daysWithMood) * 100).toFixed(0) : 0;
const pctNeutral = daysWithMood ? ((neutralDays / daysWithMood) * 100).toFixed(0) : 0;
const pctNegative = daysWithMood ? ((negativeDays / daysWithMood) * 100).toFixed(0) : 0;

// Renderização
const root = dv.el("div", "");
root.style.cssText = `
    display: flex; flex-direction: column; gap: 12px; color: #fff;
    background: rgba(20, 20, 25, 0.95); padding: 16px; border-radius: 12px;
    max-width: 980px; border: 1px solid rgba(255, 255, 255, 0.1);
`;

// Cards de resumo geral
const summaryDiv = document.createElement("div");
summaryDiv.style.cssText = "display: flex; gap: 8px; flex-wrap: wrap; justify-content: space-around;";

[
    { label: "📊 Média", value: `${averageMood}/5`, color: moodColors[Math.round(averageMood)] || '#fff' },
    { label: "🎯 Mais Frequente", value: mostFrequent.value ? Object.entries(moodScale).find(([k,v])=>v==mostFrequent.value)[0] : 'N/A', color: '#fff' },
    { label: trend.icon, value: trend.text, color: trend.color },
    { label: "🗓 Dias Registrados", value: daysWithMood, color: '#fff' },
    { label: "💚 Dias Positivos", value: `${positiveDays} (${pctPositive}%)`, color: '#4caf50' },
    { label: "🟡 Dias Neutros", value: `${neutralDays} (${pctNeutral}%)`, color: '#ffc107' },
    { label: "🔴 Dias Negativos", value: `${negativeDays} (${pctNegative}%)`, color: '#f44336' },
    { label: "🔔 Último Humor", value: lastMood || 'N/A', color: lastMood ? moodColors[moodScale[lastMood]] : '#fff' }
].forEach(item => {
    const card = document.createElement("div");
    card.style.cssText = `
        flex: 1; min-width: 120px; display: flex; flex-direction: column; align-items: center;
        background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    `;
    card.innerHTML = `
        <div style="font-size: 0.75em; color: #ccc; margin-bottom: 4px;">${item.label}</div>
        <div style="font-weight: bold; font-size: 0.9em; color: ${item.color}">${item.value}</div>
    `;
    summaryDiv.appendChild(card);
});

// Cards de detalhamento por humor
const moodsDiv = document.createElement("div");
moodsDiv.style.cssText = "display: flex; gap: 6px; flex-wrap: wrap; justify-content: space-around;";

Object.entries(moodScale).sort((a,b) => b[1]-a[1]).forEach(([label, value]) => {
    const count = moodCount[value] || 0;
    const percentage = daysWithMood ? ((count / daysWithMood) * 100).toFixed(0) : 0;

    const card = document.createElement("div");
    card.style.cssText = `
        aspect-ratio: 1/1; flex: 1 0 70px; display: flex; flex-direction: column; 
        justify-content: center; align-items: center; background: rgba(0, 0, 0, 0.3);
        border-radius: 8px; padding: 6px; margin: 2px;
        border: 2px solid ${moodColors[value]}; box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    `;
    card.innerHTML = `
        <div style="font-size: 1.4em; margin-bottom: 2px;">${label.split(' – ')[0]}</div>
        <div style="font-weight: bold; font-size: 0.95em;">${count}</div>
        <div style="font-size: 0.7em; color: #b0b0b0;">${percentage}%</div>
    `;
    moodsDiv.appendChild(card);
});

root.appendChild(summaryDiv);
root.appendChild(moodsDiv);
dv.container.appendChild(root);

```

