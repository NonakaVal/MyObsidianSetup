---
cssclasses:
---

```dataviewjs
// =============================
// CONFIGURAÇÃO
// =============================
const pastas = [
    "System/Templates/Format",
    "System/Templates/Snippet"
];

// =============================
// ELEMENTOS DE INTERFACE
// =============================
let root = dv.el("div", "");

// Dropdown de pastas
let folderSelect = document.createElement("select");
pastas.forEach(p => {
    let opt = document.createElement("option");
    opt.value = p;
    opt.text = p;
    folderSelect.appendChild(opt);
});
root.appendChild(folderSelect);

// Dropdown de ordenação
let sortSelect = document.createElement("select");
["Nome do arquivo", "Última modificação", "Tempo desde modificação"].forEach(optText => {
    let opt = document.createElement("option");
    opt.value = optText;
    opt.text = optText;
    sortSelect.appendChild(opt);
});
sortSelect.style.marginLeft = "10px";
root.appendChild(sortSelect);

// Botão ASC/DESC
let orderBtn = document.createElement("button");
orderBtn.textContent = "⬆️ Asc";
orderBtn.style.marginLeft = "10px";
root.appendChild(orderBtn);

// Div da tabela
let tableDiv = document.createElement("div");
root.appendChild(tableDiv);

// =============================
// ESTADO
// =============================
let ascending = true;

// =============================
// FUNÇÃO DE FORMATAÇÃO DE DIFERENÇA
// =============================
function formatTimeDiff(ts) {
    const diffMs = dv.date("now").ts - ts;
    const diffMinutes = Math.floor(diffMs / (1000 * 60));
    const diffHours = Math.floor(diffMinutes / 60);
    const diffDays = Math.floor(diffHours / 24);

    if (diffMinutes < 60) {
        return `${diffMinutes} minuto${diffMinutes !== 1 ? "s" : ""} atrás`;
    } else if (diffHours < 24) {
        return `${diffHours} hora${diffHours !== 1 ? "s" : ""} atrás`;
    } else {
        return `${diffDays} dia${diffDays !== 1 ? "s" : ""} atrás`;
    }
}

// =============================
// FUNÇÃO DE RENDERIZAÇÃO
// =============================
function renderTable(folder, sortKey) {
    let pages = dv.pages()
        .where(p => p.file.folder.startsWith(folder))
        .array();

    // Ordenação
    pages.sort((a, b) => {
        let valA, valB;
        if (sortKey === "Nome do arquivo") {
            valA = a.file.name || "";
            valB = b.file.name || "";
        } else if (sortKey === "Última modificação" || sortKey === "Tempo desde modificação") {
            valA = a.file.mtime?.ts || 0;
            valB = b.file.mtime?.ts || 0;
        }
        if (valA < valB) return ascending ? -1 : 1;
        if (valA > valB) return ascending ? 1 : -1;
        return 0;
    });

    // Limpar tabela antiga
    tableDiv.innerHTML = "";

    // Criar tabela
    let table = document.createElement("table");
    table.classList.add("dataview");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";

    // Cabeçalho
    let thead = document.createElement("thead");
    let headerRow = document.createElement("tr");
    ["📄 Arquivo", "🕒 Última modificação", "⏳ Tempo desde modificação"].forEach(h => {
        let th = document.createElement("th");
        th.textContent = h;
        th.style.textAlign = "left";
        th.style.padding = "4px 8px";
        th.style.borderBottom = "1px solid #ccc";
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Corpo
    let tbody = document.createElement("tbody");
    pages.forEach(p => {
        let row = document.createElement("tr");

        // Arquivo
        let tdLink = document.createElement("td");
        tdLink.appendChild(dv.el("span", p.file.link));
        tdLink.style.padding = "4px 8px";
        row.appendChild(tdLink);

        // Última modificação
        let tdMtime = document.createElement("td");
        tdMtime.style.padding = "4px 8px";
        tdMtime.textContent = p.file.mtime ? dv.date(p.file.mtime).toFormat("yyyy-MM-dd HH:mm") : "—";
        row.appendChild(tdMtime);

        // Tempo desde modificação (min, horas, dias)
        let tdDiff = document.createElement("td");
        tdDiff.style.padding = "4px 8px";
        if (p.file.mtime) {
            tdDiff.textContent = formatTimeDiff(p.file.mtime.ts);
        } else {
            tdDiff.textContent = "—";
            tdDiff.style.color = "#888";
            tdDiff.style.fontStyle = "italic";
        }
        row.appendChild(tdDiff);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    tableDiv.appendChild(table);
}

// =============================
// EVENTOS
// =============================
folderSelect.onchange = () => renderTable(folderSelect.value, sortSelect.value);
sortSelect.onchange = () => renderTable(folderSelect.value, sortSelect.value);
orderBtn.onclick = () => {
    ascending = !ascending;
    orderBtn.textContent = ascending ? "⬆️ Asc" : "⬇️ Desc";
    renderTable(folderSelect.value, sortSelect.value);
};

// Render inicial
renderTable(pastas[0], "Nome do arquivo");

```
