~~~dataviewjs
// =============================
// 📊 HUMOR: CALENDÁRIO + LINE CHART COM DIA DA SEMANA
// =============================
const CONFIG = { tag: "#calendar/daily", rangeDays: <% tp.system.prompt("range days num")%> };

// ---------------------------
// Configuração de visualização padrão
// ---------------------------
const defaultView = '<% tp.system.prompt("calendar or chart")%>'; // "calendar" ou "chart"

// ---------------------------
// Mapas de humor
// ---------------------------
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
const moodLabels = Object.fromEntries(Object.entries(moodScale).map(([k,v]) => [v,k]));

// ---------------------------
// Datas
// ---------------------------
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');
const startDate = moment(endDate).subtract(CONFIG.rangeDays,'days');

// ---------------------------
// Coleta dados
// ---------------------------
const pages = dv.pages(CONFIG.tag).sort(p => p.file.name,'asc');
const days = [];
const chartLabels = [];
const chartData = [];
const chartColors = [];
const moodCount = {};
let totalValue = 0;
let daysWithMood = 0;

for (let p of pages) {
    const d = moment(p.file.name,'YYYY-MM-DD');
    const mood = p["daily-mood"];
    const value = moodScale[mood];
    if (d.isBetween(startDate,endDate,null,'[]') && value) {
        days.push({
            dateISO: d.format('YYYY-MM-DD'),
            emoji: mood.split(' – ')[0],
            label: d.format('D/M'),
            weekday: d.format('ddd'),
            value: value
        });
        chartLabels.push(d.format('DD/MM'));
        chartData.push(value);
        chartColors.push(moodColors[value]);
        moodCount[value] = (moodCount[value] || 0) + 1;
        totalValue += value;
        daysWithMood++;
    }
}

// ---------------------------
// Estatísticas
// ---------------------------
const averageMood = daysWithMood ? (totalValue/daysWithMood).toFixed(1) : 0;
let mostFrequentMood = null;
let maxCount = 0;
for (const [v,c] of Object.entries(moodCount)) {
    if (c > maxCount) {
        maxCount = c;
        mostFrequentMood = parseInt(v);
    }
}
let trend = "→ Estável";
if (chartData.length >= 2) {
    const firstHalf = chartData.slice(0, Math.floor(chartData.length/2));
    const secondHalf = chartData.slice(Math.floor(chartData.length/2));
    const avgFirst = firstHalf.reduce((a,b)=>a+b,0)/firstHalf.length;
    const avgSecond = secondHalf.reduce((a,b)=>a+b,0)/secondHalf.length;
    if (avgSecond > avgFirst + 0.3) trend = "📈 Melhorando";
    else if (avgSecond < avgFirst - 0.3) trend = "📉 Piorando";
}

// ---------------------------
// Container principal
// ---------------------------
const root = dv.el("div","");
root.style.cssText = `
    display:flex; flex-direction:column; gap:8px; color:#fff;
    background: rgba(20,20,25,0.9); padding:10px; border-radius:10px; max-width:2890px;
`;

// ---------------------------
// Botões alternar
// ---------------------------
const btnDiv = document.createElement("div");
btnDiv.style.cssText = "display:flex; gap:6px;";

const btnCal = document.createElement("button");
btnCal.textContent="📅 Calendário";

const btnChart = document.createElement("button");
btnChart.textContent="📈 Gráfico";

[btnCal, btnChart].forEach(btn => {
    btn.style.cssText = `
        padding:4px 8px; border:none; border-radius:6px; background:#333; color:#fff; cursor:pointer;
        font-size:0.85em; flex:1; transition:0.2s;
    `;
    btn.onmouseenter = () => btn.style.background = "#555";
    btn.onmouseleave = () => btn.style.background = "#333";
});

btnDiv.appendChild(btnCal);
btnDiv.appendChild(btnChart);
root.appendChild(btnDiv);

// ---------------------------
// Calendário
// ---------------------------
const calDiv = document.createElement("div");
calDiv.style.display = (defaultView==="calendar") ? "grid" : "none"; // ← padrão inicial
calDiv.style.gridTemplateColumns = "repeat(7,1fr)";
calDiv.style.gap = "4px";

const startDay = startDate.day();
for (let i=0;i<startDay;i++) calDiv.appendChild(document.createElement("div"));

for (const day of days) {
    const cell = document.createElement("div");
    const color = day.value ? moodColors[day.value] : "rgba(255,255,255,0.1)";
    cell.innerHTML = `
        <div style="font-size:1.3em">${day.emoji}</div>
        <div style="font-size:0.65em;opacity:0.8;margin-top:2px;">${day.label}</div>
        <div style="font-size:0.55em;opacity:0.6;">${day.weekday}</div>
    `;
    cell.style.cssText = `
        aspect-ratio:1/1; display:flex; flex-direction:column; justify-content:center; align-items:center;
        background: rgba(255,255,255,0.03); border:1px solid ${color}; border-radius:6px; padding:2px;
        transition: all 0.2s;
    `;
    cell.onmouseenter = () => { cell.style.background = color+"33"; cell.style.transform = "scale(1.08)"; };
    cell.onmouseleave = () => { cell.style.background = "rgba(255,255,255,0.03)"; cell.style.transform = "scale(1)"; };
    calDiv.appendChild(cell);
}
root.appendChild(calDiv);

// ---------------------------
// Line chart
// ---------------------------
const chartDiv = dv.el("div","");
chartDiv.style.cssText = `
    height:250px;width:100%;background-color:rgba(0,0,0,0.7);
    border-radius:8px;padding:8px;
    display:${(defaultView==="chart") ? "block" : "none"};
`;

const chartConfig = {
    type:'line',
    data:{
        labels: chartLabels,
        datasets:[{
            data: chartData,
            borderColor:'#7e57c2',
            backgroundColor:'rgba(126,87,194,0.08)',
            pointBackgroundColor: chartColors,
            pointBorderColor: chartColors,
            borderWidth:2,
            tension:0.3,
            fill:true,
            pointRadius:4,
            pointHoverRadius:6
        }]
    },
    options:{
        responsive:true,
        maintainAspectRatio:false,
        interaction:{intersect:false,mode:'index'},
        plugins:{
            legend:{display:false},
            tooltip:{callbacks:{label:ctx=>`Humor: ${moodLabels[ctx.raw]||ctx.raw}`},
                     backgroundColor:'rgba(30,30,30,0.9)', titleColor:'#fff', bodyColor:'#fff'}
        },
        scales:{
            y:{min:0.5,max:5.5, ticks:{stepSize:1,color:'#fff',backdropColor:'rgba(0,0,0,0.5)',callback:val=>moodLabels[val]||val,padding:4}, grid:{color:'rgba(200,200,200,0.2)'}},
            x:{ticks:{color:'#fff',backdropColor:'rgba(0,0,0,0.5)',padding:4}, grid:{display:false}}
        }
    }
};
root.appendChild(chartDiv);
window.renderChart(chartConfig, chartDiv);

// ---------------------------
// Alternar visibilidade
// ---------------------------
btnCal.onclick = () => { calDiv.style.display = "grid"; chartDiv.style.display = "none"; };
btnChart.onclick = () => { calDiv.style.display = "none"; chartDiv.style.display = "block"; };

dv.container.appendChild(root);
~~~

