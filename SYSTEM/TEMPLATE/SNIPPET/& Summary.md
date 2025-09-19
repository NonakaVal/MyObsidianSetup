
```dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO DE INTERVALO
//-----------------------------------------------------
const startDate = moment("<% tp.system.prompt("StartDate")%>", "YYYY-MM-DD");
const endDate = moment("<% tp.date.now("YYYY-MM-DD") %>", "YYYY-MM-DD");

//-----------------------------------------------------
// RESUMO HUMOR
//-----------------------------------------------------
const moodScale = {
  "😄 – Happy": 5, "🙂 – Neutral": 4, "😐 – Meh": 3, "😞 – Sad": 2, "😠 – Frustrated": 1
};
const moodLabels = Object.fromEntries(Object.entries(moodScale).map(([k, v]) => [v, k]));

let moodCount = {};
let totalMoodValue = 0;
let moodDays = 0;

for (let p of dv.pages('#calendar/daily')) {
    const d = moment(p.file.name, 'YYYY-MM-DD');
    const mood = p["daily-mood"];
    const value = moodScale[mood];
    if (d.isBetween(startDate, endDate, null, '[]') && value) {
        moodCount[value] = (moodCount[value] || 0) + 1;
        totalMoodValue += value;
        moodDays++;
    }
}

const avgMood = moodDays ? (totalMoodValue / moodDays).toFixed(2) : "—";
const avgMoodLabel = moodLabels[Math.round(avgMood)] || "";

//-----------------------------------------------------
// RESUMO DAILY LOG
//-----------------------------------------------------
let logCount = 0;

for (const page of dv.pages('#calendar/daily')) {
    const fileDate = moment(page.file.name, "YYYY-MM-DD");
    if (!fileDate.isBetween(startDate, endDate, null, '[]')) continue;

    const content = await dv.io.load(page.file.path);
    if (content.includes("# Daily LOG")) logCount++;
}

//-----------------------------------------------------
// RESUMO POMODOROS
//-----------------------------------------------------
const allItems = dv.pages().file.lists
    .array()
    .filter(item => item.pomodoro)
    .filter(item => {
        const date = moment(item?.end?.substring(0, 10), "YYYY-MM-DD");
        return date.isBetween(startDate, endDate, null, '[]');
    });

function calcPomodoro(tipo) {
    const items = allItems.filter(i => i.pomodoro.toLowerCase() === tipo.toLowerCase());
    const minutos = items.reduce((sum, i) => sum + i.duration.as("minutes"), 0);
    return {
        qtd: items.length,
        min: minutos,
        hrs: (minutos / 60).toFixed(2)
    };
}

const work = calcPomodoro("work");
const breakT = calcPomodoro("break");
const totalPom = {
    qtd: allItems.length,
    min: work.min + breakT.min,
    hrs: ((work.min + breakT.min) / 60).toFixed(2)
};

//-----------------------------------------------------
// SAÍDA RESUMO
//-----------------------------------------------------
dv.paragraph(`## 📊 Resumo Geral (${startDate.format('DD/MM/YYYY')} a ${endDate.format('DD/MM/YYYY')})`);

dv.table(["Categoria", "Resumo"], [
    ["😊 Humor", `Média: **${avgMood}** ${avgMoodLabel} — ${moodDays} dia(s) com registro`],
    ...Object.entries(moodCount).sort((a,b) => b[0] - a[0])
        .map(([val,count]) => [`↳ ${moodLabels[val]}`, `${count} dia(s)`]),

    ["📓 Daily LOG", `${logCount} notas com seção "Daily LOG"`],

    ["⏳ Pomodoros", `Work: ${work.qtd} (${work.min} min / ${work.hrs}h)  
Break: ${breakT.qtd} (${breakT.min} min / ${breakT.hrs}h)  
Total: ${totalPom.qtd} (${totalPom.min} min / ${totalPom.hrs}h)`]
]);

```