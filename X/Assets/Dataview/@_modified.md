---
{}
---

```dataviewjs
// =============================
// 🛠️ Últimos Arquivos Modificados
// =============================
let root = dv.el("div", "");

// Input de limite
let limitLabel = document.createElement("label");
limitLabel.textContent = "Limite: ";
let limitInput = document.createElement("input");
limitInput.type = "number";
limitInput.value = 10;
limitInput.style.width = "50px";
limitInput.style.marginRight = "10px";
root.appendChild(limitLabel);
root.appendChild(limitInput);

// Botão de ordenação
let orderBtn = document.createElement("button");
orderBtn.textContent = "⬇️";
orderBtn.style.marginLeft = "5px";
root.appendChild(orderBtn);

// Div da tabela
let tableDiv = document.createElement("div");
tableDiv.style.marginTop = "10px";
root.appendChild(tableDiv);

let ascending = false;

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
    let pages = dv.pages().array();

    pages.sort((a, b) => {
        let valA = a.file.mtime?.ts || 0;
        let valB = b.file.mtime?.ts || 0;
        return ascending ? valA - valB : valB - valA;
    });

    pages = pages.slice(0, limit);

    tableDiv.innerHTML = "";
    let table = document.createElement("table");
    table.classList.add("dataview");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";

    let thead = document.createElement("thead");
    let header = document.createElement("tr");
    ["📄", "⏳"].forEach(h => {
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
orderBtn.onclick = () => {
    ascending = !ascending;
    orderBtn.textContent = ascending ? "⬆️" : "⬇️";
    renderTable();
};

// Inicial
renderTable();

```