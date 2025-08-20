```dataviewjs
const dataInicial = moment("<%tp.file.cursor()%>", "YYYY-MM-DD");
const dataFinal = moment("<% tp.date.now("YYYY-MM-DD") %>", "YYYY-MM-DD");

const pages = dv.pages();

const filteredItems = pages.file.lists
    .array() // converte para array JS puro
    .filter(item => item.pomodoro)
    .filter(item => {
        const date = moment(item?.end?.substring(0, 10), "YYYY-MM-DD");
        return date.isBetween(dataInicial, dataFinal, null, '[]');
    })
    .sort((a, b) => moment(b.end).valueOf() - moment(a.end).valueOf());

const table = dv.markdownTable(
    ['Pomodoro', 'Duration', 'Begin', 'End'],
    filteredItems.map(item => [
        item.pomodoro,
        `${item.duration.as("minutes")} m`,
        item.begin,
        item.end
    ])
);

dv.paragraph(table);

// --- SUMÁRIO ---
function calcTotais(tipo) {
    const items = filteredItems.filter(i => i.pomodoro.toLowerCase() === tipo.toLowerCase());
    const minutos = items.reduce((sum, item) => sum + item.duration.as("minutes"), 0);
    return {
        quantidade: items.length,
        minutos,
        horas: (minutos / 60).toFixed(2)
    };
}

const work = calcTotais("work");
const breakT = calcTotais("break");

dv.paragraph(`### Resumo`);
dv.paragraph(`**Work:** ${work.quantidade} pomodoros — ${work.minutos} minutos (${work.horas} horas)`);
dv.paragraph(`**Break:** ${breakT.quantidade} pomodoros — ${breakT.minutos} minutos (${breakT.horas} horas)`);
dv.paragraph(`**Total:** ${filteredItems.length} pomodoros — ${(work.minutos + breakT.minutos)} minutos (${((work.minutos + breakT.minutos) / 60).toFixed(2)} horas)`);
```