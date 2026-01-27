~~~dataviewjs
//-----------------------------------------------------
// ⚙️ CONFIGURAÇÕES — altere APENAS esta seção
//-----------------------------------------------------
const rangeDays = <% tp.system.prompt("Daily Logs Dayrange config")%>; // Alterar o número de dias
const CONFIG = {
    tag: "#calendar/daily",      // Tag usada para filtrar notas
    sectionHeader: "Capture #capture",       // Cabeçalho da seção alvo
    rangeDays: rangeDays,        // Intervalo em dias
    sortOrder: "desc"            // Opções: "asc" | "desc"
};

//-----------------------------------------------------
// 🎯 CATEGORIAS PARA AGRUPAMENTO
//-----------------------------------------------------
const categories = [
  { icon: "💡", name: "Ideia" },
  { icon: "⭐", name: "Algo bom" },
  { icon: "😴", name: "Even" },
  { icon: "💀", name: "Puts" },
  { icon: "🌱", name: "Motivação" },
  { icon: "💩", name: "Cagada" },
  { icon: "❓", name: "???" },
  { icon: "🧭", name: "Intenção" },
  { icon: "💬", name: "Gratidão" },
  
  
];

//-----------------------------------------------------
// 🗓️ INTERVALO DE DATAS
//-----------------------------------------------------
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');
const startDate = moment(endDate).subtract(CONFIG.rangeDays, 'days'); // X dias atrás

//-----------------------------------------------------
// 📄 CAPTURA DE PÁGINAS VÁLIDAS
//-----------------------------------------------------
const pages = dv.pages(CONFIG.tag)
    .where(p => {
        const fileDate = moment(p.file.name, "YYYY-MM-DD");
        return fileDate.isBetween(startDate, endDate, null, '[]');
    })
    .sort(p => p.file.name, CONFIG.sortOrder);

//-----------------------------------------------------
// 🧩 EXTRAÇÃO DO CONTEÚDO DA SEÇÃO DEFINIDA
//-----------------------------------------------------
let allEntries = [];
let categoryTotals = Object.fromEntries(categories.map(c => [c.name, 0]));
let totalLogs = 0;

for (const page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split('\n');
    let insideTarget = false;
    let sectionContent = [];

    for (const line of lines) {
        if (line.startsWith("# " + CONFIG.sectionHeader)) {
            insideTarget = true;
            continue;
        }
        if (line.startsWith("# ") && insideTarget) break;
        if (insideTarget && line.trim() !== "") {
            sectionContent.push(line.trim());
        }
    }

    if (sectionContent.length > 0) {
        sectionContent.forEach(line => {
            // Detectar categoria baseada no emoji
            let detectedCategory = "Outros";
            let categoryIcon = "📄";
            
            for (const category of categories) {
                if (line.includes(category.icon)) {
                    detectedCategory = category.name;
                    categoryIcon = category.icon;
                    categoryTotals[category.name]++;
                    totalLogs++;
                    break;
                }
            }
            
            allEntries.push({
                date: page.file.link,
                content: line,
                category: detectedCategory,
                icon: categoryIcon,
                rawContent: line.replace(/[💡⭐😴💀🌱💩❓💬🧭]/g, '').trim()
            });
        });
    }
}

//-----------------------------------------------------
// 📊 CARD DE CONTAGEM NO TOPO
//-----------------------------------------------------
function renderStatsCard() {
    const statsCard = document.createElement("div");
    statsCard.style.marginBottom = "12px";
    statsCard.style.padding = "12px";
    statsCard.style.border = "1px solid var(--background-modifier-border)";
    statsCard.style.borderRadius = "6px";
    statsCard.style.backgroundColor = "var(--background-secondary)";
    
    let statsHTML = `<div style="display: flex; justify-content: center; align-items: center; gap: 16px; margin-bottom: 8px;">`;
    
    for (const cat of categories) {
        const count = categoryTotals[cat.name] || 0;
        const percentage = totalLogs > 0 ? ((count / totalLogs) * 100).toFixed(1) : 0;
        
        statsHTML += `
            <div style="display: flex; flex-direction: column; align-items: center;">
                <span style="font-size: 1.5em;">${cat.icon}</span>
                <span style="font-weight: bold; font-size: 1.1em;">${count}</span>
                <span style="font-size: 0.8em; color: var(--text-muted);">${percentage}%</span>
            </div>
        `;
    }
    
    statsHTML += `</div>`;
    
    statsHTML += `
        <div style="text-align: center; padding-top: 6px; border-top: 1px solid var(--background-modifier-border);">
            <span style="font-weight: bold; font-size: 1em;">🧮 Total: ${totalLogs}</span>
        </div>
    `;
    
    statsCard.innerHTML = statsHTML;
    return statsCard;
}

//-----------------------------------------------------
// 🎛️ CONTROLES DE SELEÇÃO
//-----------------------------------------------------
const controls = document.createElement("div");
controls.style.marginBottom = "16px";
controls.style.padding = "8px";
controls.style.border = "1px solid var(--background-modifier-border)";
controls.style.borderRadius = "8px";

// Select para agrupamento
const groupSelect = document.createElement("select");
groupSelect.style.marginRight = "12px";

const groupOptions = [
    { value: "none", text: "📅 Ordenar por Data" },
    { value: "category", text: "🎯 Agrupar por Categoria" }
];

categories.forEach(category => {
    const count = categoryTotals[category.name] || 0;
    groupOptions.push({
        value: `cat-${category.name}`,
        text: `${category.icon} ${category.name} (${count})`
    });
});

groupOptions.forEach(opt => {
    const option = document.createElement("option");
    option.value = opt.value;
    option.textContent = opt.text;
    groupSelect.appendChild(option);
});

// Select para ordenação
const sortSelect = document.createElement("select");
const sortOptions = [
    { value: "desc", text: "⬆️" },
    { value: "asc", text: "⬇️" },
    { value: "category", text: "🔤" }
];

sortOptions.forEach(opt => {
    const option = document.createElement("option");
    option.value = opt.value;
    option.textContent = opt.text;
    option.selected = opt.value === CONFIG.sortOrder;
    sortSelect.appendChild(option);
});

controls.appendChild(document.createTextNode("Agrupar por: "));
controls.appendChild(groupSelect);
controls.appendChild(document.createTextNode(" Ordenar por: "));
controls.appendChild(sortSelect);

//-----------------------------------------------------
// 📊 FUNÇÃO PARA RENDERIZAR TABELA
//-----------------------------------------------------
function renderTable(entries, groupBy = "none", sortBy = CONFIG.sortOrder) {
    const oldTable = dv.container.querySelector("table");
    if (oldTable) oldTable.remove();
    
    let processedEntries = [...entries];
    
    if (sortBy === "asc") processedEntries.sort((a,b) => a.date > b.date ? 1 : -1);
    else if (sortBy === "desc") processedEntries.sort((a,b) => a.date < b.date ? 1 : -1);
    else if (sortBy === "category") processedEntries.sort((a,b) => a.category.localeCompare(b.category));
    
    const table = document.createElement("table");
    table.style.width = "100%";
    table.style.borderCollapse = "collapse";
    
    const thead = document.createElement("thead");
    const trHead = document.createElement("tr");
    ["🗓️", "📝"].forEach(h => {
        const th = document.createElement("th");
        th.textContent = h;
        th.style.textAlign = "left";
        th.style.padding = "8px 12px";
        th.style.borderBottom = "2px solid var(--background-modifier-border)";
        th.style.backgroundColor = "var(--background-secondary)";
        trHead.appendChild(th);
    });
    thead.appendChild(trHead);
    table.appendChild(thead);
    
    const tbody = document.createElement("tbody");
    
    if (groupBy === "none" || groupBy.startsWith("cat-")) {
        let filteredEntries = processedEntries;
        if (groupBy.startsWith("cat-")) {
            const selectedCategory = groupBy.replace("cat-", "");
            filteredEntries = processedEntries.filter(entry => entry.category === selectedCategory);
        }
        
        filteredEntries.forEach(entry => {
            const tr = document.createElement("tr");
            const tdDate = document.createElement("td");
            tdDate.style.padding = "6px 12px";
            tdDate.style.borderBottom = "1px solid var(--background-modifier-border)";
            tdDate.appendChild(dv.el("span", entry.date));
            tr.appendChild(tdDate);
            
            const tdContent = document.createElement("td");
            tdContent.style.padding = "6px 12px";
            tdContent.style.borderBottom = "1px solid var(--background-modifier-border)";
            tdContent.innerHTML = `<strong>${entry.icon}</strong> ${entry.rawContent}`;
            tr.appendChild(tdContent);
            
            tbody.appendChild(tr);
        });
        
    } else if (groupBy === "category") {
        const grouped = {};
        processedEntries.forEach(entry => {
            if (!grouped[entry.category]) grouped[entry.category] = [];
            grouped[entry.category].push(entry);
        });
        
        const sortedCategories = Object.keys(grouped).sort();
        
        sortedCategories.forEach(category => {
            const categoryEntries = grouped[category];
            const categoryInfo = categories.find(cat => cat.name === category) || { icon: "📄", name: category };
            
            const trHeader = document.createElement("tr");
            const tdHeader = document.createElement("td");
            tdHeader.colSpan = 2;
            tdHeader.style.padding = "8px 12px";
            tdHeader.style.backgroundColor = "var(--background-secondary)";
            tdHeader.style.fontWeight = "bold";
            tdHeader.style.borderBottom = "2px solid var(--background-modifier-border)";
            tdHeader.textContent = `${categoryInfo.icon} ${category} (${categoryEntries.length} entradas)`;
            trHeader.appendChild(tdHeader);
            tbody.appendChild(trHeader);
            
            categoryEntries.forEach(entry => {
                const tr = document.createElement("tr");
                const tdDate = document.createElement("td");
                tdDate.style.padding = "6px 12px";
                tdDate.style.borderBottom = "1px solid var(--background-modifier-border)";
                tdDate.appendChild(dv.el("span", entry.date));
                tr.appendChild(tdDate);
                
                const tdContent = document.createElement("td");
                tdContent.style.padding = "6px 12px";
                tdContent.style.borderBottom = "1px solid var(--background-modifier-border)";
                tdContent.innerHTML = `<strong>${entry.icon}</strong> ${entry.rawContent}`;
                tr.appendChild(tdContent);
                
                tbody.appendChild(tr);
            });
        });
    }
    
    table.appendChild(tbody);
    dv.container.appendChild(table);
}

//-----------------------------------------------------
// 🚀 EXECUÇÃO INICIAL
//-----------------------------------------------------
dv.container.appendChild(renderStatsCard());
dv.container.appendChild(controls);
renderTable(allEntries);

//-----------------------------------------------------
// 🎛️ EVENT LISTENERS PARA OS CONTROLES
//-----------------------------------------------------
groupSelect.addEventListener("change", (e) => {
    renderTable(allEntries, e.target.value, sortSelect.value);
});

sortSelect.addEventListener("change", (e) => {
    renderTable(allEntries, groupSelect.value, e.target.value);
});

~~~

