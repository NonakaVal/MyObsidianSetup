~~~dataviewjs
// =============================
// ⚙️ CONFIGURAÇÕES
// =============================
const CONFIG = {
    tag: "#calendar/daily",
    rangeDays: <% tp.system.prompt("Número de dias para análise de Pomodoros") %>,
    chartHeight: "260px"
};

// =============================
// 🗓️ INTERVALO DE DATAS
// =============================
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');
const startDate = moment(endDate).subtract(CONFIG.rangeDays, 'days');

// =============================
// 📊 COLETA DE DADOS
// =============================
const pages = dv.pages(CONFIG.tag)
    .where(p => p.file.name >= startDate.format("YYYY-MM-DD") && p.file.name <= endDate.format("YYYY-MM-DD"))
    .sort(p => p.file.name, 'asc');

const allDates = [], workData = [], breakData = [], moods = [];
let totalWork = 0, totalBreak = 0;

for (let i = 0; i < CONFIG.rangeDays; i++) {
    const currentDate = moment(startDate).add(i, 'days').format("YYYY-MM-DD");
    const page = pages.find(p => p.file.name === currentDate);

    let workMin = 0, breakMin = 0, mood = "";

    if (page && page.pomodoros) {
        page.pomodoros.forEach(pom => {
            if (pom.type === "work") workMin += pom.plannedDuration || 0;
            if (pom.type?.includes("break")) breakMin += pom.plannedDuration || 0;
        });
        mood = page["daily-mood"] || "";
    }

    workData.push(workMin);
    breakData.push(breakMin);
    moods.push(mood);
    allDates.push(currentDate);
    totalWork += workMin;
    totalBreak += breakMin;
}

const avgWork = totalWork / CONFIG.rangeDays;
const avgBreak = totalBreak / CONFIG.rangeDays;
const productivityRatio = totalWork > 0 ? (totalWork / (totalWork + totalBreak) * 100).toFixed(1) : 0;

// =============================
// 🎨 RESUMO
// =============================
function renderSummary() {
    const el = dv.el("div", "");
    el.className = "pomodoro-summary";
    el.innerHTML = `
        <div class="summary-grid">
            <div class="summary-card"><span>📅</span><div>${startDate.format('DD/MM')}–${endDate.format('DD/MM')}</div></div>
            <div class="summary-card work"><span>💼</span><div>${totalWork}m</div></div>
            <div class="summary-card break"><span>☕</span><div>${totalBreak}m</div></div>
            <div class="summary-card"><span>📈</span><div>${avgWork.toFixed(1)}m/dia</div></div>
        </div>
        <div class="ratio">
            <div class="label">🎯 Produtividade</div>
            <div class="bar"><div class="fill" style="width:${productivityRatio}%"></div></div>
            <div class="value">${productivityRatio}%</div>
        </div>`;
    return el;
}

// =============================
// 📊 CONFIG GRÁFICO
// =============================
const chartData = {
    type: 'line',
    data: {
        labels: allDates.map(d => moment(d).format("DD/MM")),
        datasets: [
            {
                label: 'Work',
                data: workData,
                borderColor: '#9575cd',
                backgroundColor: 'rgba(149,117,205,0.15)',
                borderWidth: 2,
                pointBackgroundColor: '#b388ff',
                pointRadius: 3,
                tension: 0.35,
                fill: true
            },
            {
                label: 'Break',
                data: breakData,
                borderColor: '#ffb74d',
                backgroundColor: 'rgba(255,183,77,0.1)',
                borderWidth: 1.5,
                pointBackgroundColor: '#ffd54f',
                pointRadius: 2.5,
                tension: 0.35,
                fill: true
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { intersect: false, mode: 'index' },
        plugins: {
            legend: { display: false },
            tooltip: {
                backgroundColor: 'rgba(30,30,30,0.9)',
                titleColor: '#fff',
                bodyColor: '#fff',
                callbacks: {
                    label: ctx => `${ctx.dataset.label}: ${ctx.raw} min`,
                    afterLabel: ctx => {
                        const mood = moods[ctx.dataIndex];
                        return mood ? `Humor: ${mood}` : '';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: { color: '#ccc', stepSize: 25, font: { size: 10 } },
                grid: { color: 'rgba(255,255,255,0.08)', drawBorder: false }
            },
            x: {
                ticks: {
                    color: '#ccc',
                    font: { size: 10 },
                    callback: function(val, index) {
                        const emoji = moods[index]?.split("–")[0]?.trim() || "";
                        return `${this.getLabelForValue(index)}${emoji ? `\n${emoji}` : ''}`;
                    }
                },
                grid: { display: false }
            }
        }
    }
};

// =============================
// 💅 ESTILO
// =============================
const styles = `
<style>
.pomodoro-summary {
    background: rgba(35,35,50,0.8);
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
.summary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(90px,1fr));
    gap: 8px;
    margin-bottom: 10px;
}
.summary-card {
    display:flex;flex-direction:column;align-items:center;
    background:rgba(255,255,255,0.06);
    border-radius:8px;
    padding:10px 6px;
    font-size:0.85em;
    color:#e0e0e0;
}
.summary-card span{font-size:1.2em;margin-bottom:4px;}
.summary-card.work{border-left:3px solid #7e57c2;}
.summary-card.break{border-left:3px solid #ff9800;}
.ratio{padding:8px 4px;text-align:center;}
.ratio .label{font-size:0.8em;color:#aaa;margin-bottom:6px;}
.ratio .bar{height:6px;background:rgba(255,255,255,0.1);border-radius:4px;overflow:hidden;margin-bottom:6px;}
.ratio .fill{height:100%;background:linear-gradient(90deg,#4caf50,#8bc34a);}
.ratio .value{font-size:0.95em;color:#4caf50;font-weight:bold;}
.chart-container{
    background:rgba(30,30,45,0.8);
    border-radius:10px;
    padding:12px;
    border:1px solid rgba(255,255,255,0.08);
}
</style>`;

// =============================
// 🚀 EXECUÇÃO
// =============================
dv.container.appendChild(document.createRange().createContextualFragment(styles));
dv.container.appendChild(renderSummary());
const chartContainer = dv.el("div", "");
chartContainer.className = "chart-container";
chartContainer.style.height = CONFIG.chartHeight;
chartContainer.style.width = "100%";
dv.container.appendChild(chartContainer);
window.renderChart(chartData, chartContainer);

~~~