~~~dataviewjs
// =============================
// 🛠️ Últimos Arquivos Modificados — versão simplificada
// =============================
let root = dv.el("div", "");

// Caminho base
const basePath = "06 MissionsProjects/Archives";

// =============================
// 🎛️ Controles de interface
// =============================
let controlsDiv = document.createElement("div");
controlsDiv.style.marginBottom = "10px";
controlsDiv.style.display = "flex";
controlsDiv.style.alignItems = "center";
controlsDiv.style.gap = "8px";
root.appendChild(controlsDiv);

// Filtro por pasta
let folderSelect = document.createElement("select");
folderSelect.style.minWidth = "180px";
controlsDiv.appendChild(folderSelect);

// Limite de resultados
let limitInput = document.createElement("input");
limitInput.type = "number";
limitInput.value = 14;
limitInput.title = "Limite de resultados";
limitInput.style.width = "60px";
controlsDiv.appendChild(limitInput);

// Botão de ordenação
let orderBtn = document.createElement("button");
orderBtn.textContent = "⬇️";
orderBtn.title = "Ordenar por data de modificação";
controlsDiv.appendChild(orderBtn);

// Div da tabela
let tableDiv = document.createElement("div");
root.appendChild(tableDiv);

let ascending = false;

// =============================
// 🕓 Tempo relativo
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
// 🧭 Pasta de nível 1
// =============================
function getTopFolder(p) {
    const rel = p.file.folder.replace(basePath + "/", "");
    return rel.split("/")[0] || "—";
}

// =============================
// 🔍 Popula o seletor de pastas
// =============================
function populateFolderValues() {
    let pages = dv.pages().where(p => p.file.path.startsWith(basePath + "/")).array();
    let folders = [...new Set(pages.map(p => getTopFolder(p)))].filter(v => v && v !== "—").sort();

    folderSelect.innerHTML = "";

    let allOpt = document.createElement("option");
    allOpt.value = "";
    allOpt.textContent = "📁 Todas as pastas";
    folderSelect.appendChild(allOpt);

    for (let f of folders) {
        let opt = document.createElement("option");
        opt.value = f;
        opt.textContent = f;
        folderSelect.appendChild(opt);
    }
}

// =============================
// 📊 Renderização da tabela
// =============================
function renderTable() {
    let limit = parseInt(limitInput.value);
    let selectedFolder = folderSelect.value;

    let pages = dv.pages().where(p => p.file.path.startsWith(basePath + "/")).array();

    // Filtro de pasta
    if (selectedFolder) {
        pages = pages.filter(p => getTopFolder(p) === selectedFolder);
    }

    // Ordenação
    pages.sort((a, b) => {
        let valA = a.file.mtime?.ts || 0;
        let valB = b.file.mtime?.ts || 0;
        return ascending ? valA - valB : valB - valA;
    });

    // Limite
    pages = pages.slice(0, limit);

    // Renderização
    tableDiv.innerHTML = "";
    let table = document.createElement("table");
    table.classList.add("dataview");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";
    table.style.fontSize = "0.9em";

    let thead = document.createElement("thead");
    let header = document.createElement("tr");
    ["📄 Arquivo", "📁 Pasta (nível 1)", "🕒 Criado                                                                                                  ", "🧭 Resumo", "⏳"].forEach(h => {
        let th = document.createElement("th");
        th.textContent = h;
        th.style.textAlign = "left";
        th.style.padding = "6px 10px";
        th.style.borderBottom = "1px solid #444";
        th.style.color = "#66b3ff";
        header.appendChild(th);
    });
    thead.appendChild(header);
    table.appendChild(thead);

    let tbody = document.createElement("tbody");

    if (pages.length === 0) {
        let tr = document.createElement("tr");
        let td = document.createElement("td");
        td.colSpan = 5;
        td.textContent = "Nenhum arquivo encontrado.";
        td.style.textAlign = "center";
        td.style.padding = "8px";
        tr.appendChild(td);
        tbody.appendChild(tr);
    } else {
        pages.forEach(p => {
            let row = document.createElement("tr");

            // 📄 Arquivo
            let tdLink = document.createElement("td");
            tdLink.appendChild(dv.el("span", p.file.link));
            tdLink.style.padding = "6px 10px";
            row.appendChild(tdLink);

            // 📁 Pasta (nível 1)
            let tdFolder = document.createElement("td");
            tdFolder.textContent = getTopFolder(p);
            tdFolder.style.padding = "6px 10px";
            row.appendChild(tdFolder);

            // 🕒 Criado
            let tdCreated = document.createElement("td");
            tdCreated.textContent = p.file.ctime ? p.file.ctime.toFormat("yyyy-MM-dd") : "—";
            tdCreated.style.padding = "6px 10px";
            row.appendChild(tdCreated);

            // 🧭 Resumo
            let tdSummary = document.createElement("td");
            tdSummary.textContent = p.summary || "—";
            tdSummary.style.padding = "6px 10px";
            tdSummary.style.color = "#bbb";
            row.appendChild(tdSummary);

            // ⏳ Modificado
            let tdDiff = document.createElement("td");
            tdDiff.textContent = formatRelativeTime(p.file.mtime);
            tdDiff.style.padding = "6px 10px";
            tdDiff.style.textAlign = "center";
            row.appendChild(tdDiff);

            tbody.appendChild(row);
        });
    }

    table.appendChild(tbody);
    tableDiv.appendChild(table);
}

// =============================
// 🎯 Eventos
// =============================
folderSelect.onchange = renderTable;
limitInput.onchange = renderTable;
orderBtn.onclick = () => {
    ascending = !ascending;
    orderBtn.textContent = ascending ? "⬆️" : "⬇️";
    renderTable();
};

// Inicialização
populateFolderValues();
renderTable();

~~~
