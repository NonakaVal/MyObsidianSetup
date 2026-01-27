

```dataviewjs
// ===== CONTROLADORES =====
const CONFIG = {
    rangeDays: <% tp.system.prompt("Quantos dias deseja exibir?") %>,
    maxHeaders: <% tp.system.prompt("Limite de headers por nota?") %>,
    maxLines: <% tp.system.prompt("Limite de linhas por seção (0 = sem limite)?") %>,
    folder: "Calendar & Review/Daily Notes",
    headerRegex: /^# (.+)/,   // pode personalizar para ## ou outros níveis
};

// EndDate ajustável (pode criar campo YAML também)
const endDate = moment(); 

// ===== CÁLCULO DAS DATAS =====
const dateRange = {
    start: moment(endDate).subtract(CONFIG.rangeDays - 1, "days"),
    end: endDate
};

// ===== VARIÁVEIS =====
let tableRows = [];
let headerNames = [];

// ===== FILTRO DE NOTAS =====
const pages = dv.pages()
    .where(p => p.file.path.startsWith(CONFIG.folder))
    .where(p => {
        const d = new Date(p.file.name);
        return d >= dateRange.start && d <= dateRange.end;
    })
    .sort(p => p.file.name, "asc");

// ===== LOOP PRINCIPAL =====
for (const page of pages) {
    const lines = (await dv.io.load(page.file.path)).split("\n");
    const headers = [];
    const sections = {};
    let current = null;

    for (const line of lines) {
        const match = line.match(CONFIG.headerRegex);

        if (match && headers.length < CONFIG.maxHeaders) {
            current = match[1].trim();
            headers.push(current);
            sections[current] = [];
        } else if (current && sections[current]) {
            sections[current].push(line.trim());
        }
    }

    // Captura headers da primeira nota válida
    if (headerNames.length === 0 && headers.length > 0) {
        headerNames = [...headers];
    }

    // Compactação opcional
    const formatSection = arr => {
        if (!arr) return "";
        if (CONFIG.maxLines > 0) {
            return arr.slice(0, CONFIG.maxLines).join("\n");
        }
        return arr.join("\n");
    };

    const row = [
        page.file.link,
        ...headerNames.map(h => formatSection(sections[h]))
    ];

    tableRows.push(row);
}

// ===== TABELA FINAL =====
dv.table(["🗓️", ...headerNames], tableRows);

```

