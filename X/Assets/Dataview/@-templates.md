## Format
```dataviewjs
// =============================
// 🛠️ Últimos Arquivos Modificados (por pasta) — com ordenação por nome
// =============================
let root = dv.el("div", "");

// Caminho alvo — modifique aqui 👇
const folderPath = "X/Templates/Format";

// Input de limite
let limitLabel = document.createElement("label");
limitLabel.textContent = "";
let limitInput = document.createElement("input");
limitInput.type = "number";
limitInput.value = 100;
limitInput.style.width = "50px";
limitInput.style.marginRight = "10px";
root.appendChild(limitLabel);
root.appendChild(limitInput);

// Botões de ordenação
let sortMode = "date"; // "date" | "name"
let ascending = false;

let sortNameBtn = document.createElement("button");
sortNameBtn.textContent = "Nome ⬇️";
sortNameBtn.style.marginLeft = "5px";

let sortDateBtn = document.createElement("button");
sortDateBtn.textContent = "Data ⬇️";
sortDateBtn.style.marginLeft = "5px";

root.appendChild(sortNameBtn);
root.appendChild(sortDateBtn);

// Div da tabela
let tableDiv = document.createElement("div");
tableDiv.style.marginTop = "10px";
root.appendChild(tableDiv);

// =============================
// ⏳ Função de tempo relativo
// =============================
function formatRelativeTime(date) {
    if (!date) return "—";
    const diffMs = Date.now() - date.toJSDate().getTime();
    const minutes = diffMs / 1000 / 60;

    if (minutes < 60) return `${Math.floor(minutes)} min`;
    if (minutes < 1440) return `${Math.floor(minutes / 60)} h`;
    return `${Math.floor(minutes / 1440)} d`;
}

// =============================
// 🧮 Renderização
// =============================
function renderTable() {
    let limit = parseInt(limitInput.value);

    // 🔍 Filtra apenas os arquivos dentro do caminho especificado
    let pages = dv.pages()
        .where(p => p.file.path.startsWith(folderPath + "/"))
        .array();

    // =============================
    // 🔤 Ordenação
    // =============================
    pages.sort((a, b) => {
        if (sortMode === "name") {
            let nameA = a.file.name.toLowerCase();
            let nameB = b.file.name.toLowerCase();
            return ascending ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
        } else {
            let valA = a.file.mtime?.ts || 0;
            let valB = b.file.mtime?.ts || 0;
            return ascending ? valA - valB : valB - valA;
        }
    });

    pages = pages.slice(0, limit);

    tableDiv.innerHTML = "";
    let table = document.createElement("table");
    table.classList.add("dataview");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";

    let thead = document.createElement("thead");
    let header = document.createElement("tr");
    ["📄 Arquivo", "⏳"].forEach(h => {
        let th = document.createElement("th");
        th.textContent = h;
        th.style.textAlign = "left";
        th.style.padding = "4px 8px";
        th.style.borderBottom = "1px solid #ccc";
        header.appendChild(th);
    });
    thead.appendChild(header);
    table.appendChild(thead);

    let tbody = document.createElement("tbody");
    pages.forEach(p => {
        let row = document.createElement("tr");

        let tdLink = document.createElement("td");
        tdLink.appendChild(dv.el("span", p.file.link));
        tdLink.style.padding = "4px 8px";
        row.appendChild(tdLink);

        let tdDiff = document.createElement("td");
        tdDiff.textContent = formatRelativeTime(p.file.mtime);
        tdDiff.style.padding = "4px 8px";
        row.appendChild(tdDiff);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    tableDiv.appendChild(table);
}

// =============================
// 🎯 Eventos
// =============================
limitInput.onchange = renderTable;

sortNameBtn.onclick = () => {
    if (sortMode === "name") {
        ascending = !ascending;
    } else {
        sortMode = "name";
        ascending = false;
    }
    sortNameBtn.textContent = `Nome ${ascending ? "⬆️" : "⬇️"}`;
    sortDateBtn.textContent = "Data ⬇️";
    renderTable();
};

sortDateBtn.onclick = () => {
    if (sortMode === "date") {
        ascending = !ascending;
    } else {
        sortMode = "date";
        ascending = false;
    }
    sortDateBtn.textContent = `Data ${ascending ? "⬆️" : "⬇️"}`;
    sortNameBtn.textContent = "Nome ⬇️";
    renderTable();
};

// Inicial
renderTable();

```

---
---

## Snippets
```dataviewjs
// =============================
// 🛠️ Últimos Arquivos Modificados (por pasta) — com ordenação por nome
// =============================
let root = dv.el("div", "");

// Caminho alvo — modifique aqui 👇
const folderPath = "X/Templates/Snippet";

// Input de limite
let limitLabel = document.createElement("label");
limitLabel.textContent = "";
let limitInput = document.createElement("input");
limitInput.type = "number";
limitInput.value = 100;
limitInput.style.width = "50px";
limitInput.style.marginRight = "10px";
root.appendChild(limitLabel);
root.appendChild(limitInput);

// Botões de ordenação
let sortMode = "date"; // "date" | "name"
let ascending = false;

let sortNameBtn = document.createElement("button");
sortNameBtn.textContent = "Nome ⬇️";
sortNameBtn.style.marginLeft = "5px";

let sortDateBtn = document.createElement("button");
sortDateBtn.textContent = "Data ⬇️";
sortDateBtn.style.marginLeft = "5px";

root.appendChild(sortNameBtn);
root.appendChild(sortDateBtn);

// Div da tabela
let tableDiv = document.createElement("div");
tableDiv.style.marginTop = "10px";
root.appendChild(tableDiv);

// =============================
// ⏳ Função de tempo relativo
// =============================
function formatRelativeTime(date) {
    if (!date) return "—";
    const diffMs = Date.now() - date.toJSDate().getTime();
    const minutes = diffMs / 1000 / 60;

    if (minutes < 60) return `${Math.floor(minutes)} min`;
    if (minutes < 1440) return `${Math.floor(minutes / 60)} h`;
    return `${Math.floor(minutes / 1440)} d`;
}

// =============================
// 🧮 Renderização
// =============================
function renderTable() {
    let limit = parseInt(limitInput.value);

    // 🔍 Filtra apenas os arquivos dentro do caminho especificado
    let pages = dv.pages()
        .where(p => p.file.path.startsWith(folderPath + "/"))
        .array();

    // =============================
    // 🔤 Ordenação
    // =============================
    pages.sort((a, b) => {
        if (sortMode === "name") {
            let nameA = a.file.name.toLowerCase();
            let nameB = b.file.name.toLowerCase();
            return ascending ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
        } else {
            let valA = a.file.mtime?.ts || 0;
            let valB = b.file.mtime?.ts || 0;
            return ascending ? valA - valB : valB - valA;
        }
    });

    pages = pages.slice(0, limit);

    tableDiv.innerHTML = "";
    let table = document.createElement("table");
    table.classList.add("dataview");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";

    let thead = document.createElement("thead");
    let header = document.createElement("tr");
    ["📄 Arquivo", "⏳"].forEach(h => {
        let th = document.createElement("th");
        th.textContent = h;
        th.style.textAlign = "left";
        th.style.padding = "4px 8px";
        th.style.borderBottom = "1px solid #ccc";
        header.appendChild(th);
    });
    thead.appendChild(header);
    table.appendChild(thead);

    let tbody = document.createElement("tbody");
    pages.forEach(p => {
        let row = document.createElement("tr");

        let tdLink = document.createElement("td");
        tdLink.appendChild(dv.el("span", p.file.link));
        tdLink.style.padding = "4px 8px";
        row.appendChild(tdLink);

        let tdDiff = document.createElement("td");
        tdDiff.textContent = formatRelativeTime(p.file.mtime);
        tdDiff.style.padding = "4px 8px";
        row.appendChild(tdDiff);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    tableDiv.appendChild(table);
}

// =============================
// 🎯 Eventos
// =============================
limitInput.onchange = renderTable;

sortNameBtn.onclick = () => {
    if (sortMode === "name") {
        ascending = !ascending;
    } else {
        sortMode = "name";
        ascending = false;
    }
    sortNameBtn.textContent = `Nome ${ascending ? "⬆️" : "⬇️"}`;
    sortDateBtn.textContent = "Data ⬇️";
    renderTable();
};

sortDateBtn.onclick = () => {
    if (sortMode === "date") {
        ascending = !ascending;
    } else {
        sortMode = "date";
        ascending = false;
    }
    sortDateBtn.textContent = `Data ${ascending ? "⬆️" : "⬇️"}`;
    sortNameBtn.textContent = "Nome ⬇️";
    renderTable();
};

// Inicial
renderTable();

```
