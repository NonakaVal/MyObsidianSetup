```dataviewjs
// =============================
// 🔹 Pomodoros + TimeEntries minimalista (ícones e sem coluna Fonte)
// =============================
const root = dv.el("div", "");

// Intervalo de datas
// const startDate = new Date("2025-10-01T00:00:00");
// const endDate   = new Date("2025-10-14T23:59:59");

// → Substituir por:
const startDate = moment('<% tp.system.prompt("StartDate (YYYY-MM-DD)") %>', 'YYYY-MM-DD');
const endDate = moment(); // hoje


// -----------------------------
// 🔹 Captura Pomodoros (#calendar/daily)
let pomodoros = [];
for (let page of dv.pages("#calendar/daily").where(p => Array.isArray(p.pomodoros))) {
    for (let p of page.pomodoros) {
        let start = new Date(p.startTime);
        let end = new Date(p.endTime);
        if (isNaN(start) || start < startDate || start > endDate) continue;

        let duration = typeof p.plannedDuration === "number" ? p.plannedDuration : (!isNaN(end) ? (end - start) / 60000 : 0);

        pomodoros.push({
            duration: duration,
            type: p.type ?? "—",
            done: p.completed ? "✅" : "❌",
            source: "Pomodoro",
            file: page.file
        });
    }
}

// -----------------------------
// 🔹 Captura TimeEntries (#task)
let timeEntries = [];
for (let page of dv.pages("#task").where(p => Array.isArray(p.timeEntries))) {
    for (let te of page.timeEntries) {
        let start = new Date(te.startTime);
        let end = new Date(te.endTime);
        if (isNaN(start) || isNaN(end) || start < startDate || start > endDate) continue;

        let duration = (end - start) / 60000; // minutos
        timeEntries.push({
            duration: duration,
            type: te.description ?? "—",
            done: "—",
            source: "TimeEntry",
            file: page.file
        });
    }
}

// -----------------------------
// 🔹 Combina e ordena
const combined = [...pomodoros, ...timeEntries];

// -----------------------------
// 🔹 Resumo
const totalMin = combined.reduce((acc, e) => acc + (e.duration || 0), 0);
const totalPom = combined.filter(e => e.source === "Pomodoro").length;
const totalTE  = combined.filter(e => e.source === "TimeEntry").length;

root.appendChild(dv.el("div", `
##### 🧩 Sessões (${startDate.toISOString().split("T")[0]} → ${endDate.toISOString().split("T")[0]})
- ⏱️ Total: **${Math.ceil(totalMin)} min**
- 🍅 Pomodoros: **${totalPom}**
- ⏳ TimeEntries (#task): **${totalTE}**
`));

// -----------------------------
// 🔹 Tabela minimalista com ícones
const table = document.createElement("table");
table.style.width = "100%";
table.style.borderCollapse = "collapse";

const headers = ["⏱️ Duração", "🎯 Tipo / Descrição", "✅ Feito", "🔗 Nota"];
const thead = document.createElement("thead");
const trHead = document.createElement("tr");

for (let h of headers) {
    const th = document.createElement("th");
    th.textContent = h;
    th.style.textAlign = "left";
    th.style.padding = "4px 8px";
    th.style.borderBottom = "1px solid #ccc";
    trHead.appendChild(th);
}
thead.appendChild(trHead);
table.appendChild(thead);

const tbody = document.createElement("tbody");

// Função para definir ícone
function getIcon(entry) {
    if(entry.source === "Pomodoro") {
        if(entry.type === "break") return "🛌";
        if(entry.type === "long-break") return "☕";
        if(entry.type === "work") return "🍅";
        return "🍅"; // default para pomodoro
    } else if(entry.source === "TimeEntry") {
        return "📝";
    }
    return "—";
}

for (let entry of combined) {
    const tr = document.createElement("tr");

    const tdDur = document.createElement("td");
    tdDur.textContent = `${getIcon(entry)} ${Math.ceil(entry.duration)} min`;
    tdDur.style.padding = "4px 8px";
    tr.appendChild(tdDur);

    const tdType = document.createElement("td");
    tdType.textContent = entry.type ?? "—";
    tdType.style.padding = "4px 8px";
    tr.appendChild(tdType);

    const tdDone = document.createElement("td");
    tdDone.textContent = entry.done ?? "—";
    tdDone.style.padding = "4px 8px";
    tr.appendChild(tdDone);

    const tdLink = document.createElement("td");
    tdLink.style.padding = "4px 8px";
    if (entry.file) tdLink.appendChild(dv.el("span", entry.file.link));
    else tdLink.textContent = "—";
    tr.appendChild(tdLink);

    tbody.appendChild(tr);
}

table.appendChild(tbody);
root.appendChild(table);

```