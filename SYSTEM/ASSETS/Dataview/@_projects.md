~~~dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES = {
    "PROJETOS": "🛠️",
    "EFFORTS": "⚡",
    "DEFAULT": "📄"
};

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function getIcon(folder) {
    const upperFolder = folder.toUpperCase();
    return ICONES[Object.keys(ICONES).find(key => upperFolder.includes(key))] || ICONES.DEFAULT;
}

function estilizarLink(p) {
    return `**${dv.fileLink(p.file.path, false, p.file.name)}**`;
}

function diasRestantes(entrega) {
    if (!entrega) return "-";
    const hoje = dv.luxon.DateTime.now();
    const dEntrega = dv.date(entrega);
    const diff = dEntrega.diff(hoje, "days").days;
    return diff >= 0 ? `${Math.floor(diff)} d` : `${Math.ceil(diff)} d (atrasado)`;
}

//-----------------------------------------------------
// COLETA E FILTRO
//-----------------------------------------------------
const pages = dv.pages('"Projects & Areas/Projects"')
    .where(p => p.type && p.type == "project")
    .sort(p => p.file.mtime, 'desc');

//-----------------------------------------------------
// EXIBIÇÃO (sem data de criação)
//-----------------------------------------------------
dv.table(
    ["", "📄", "📌 Entrega", "⭐ Status", "⏳"],
    pages.map(p => [
        getIcon(p.file.folder),
        estilizarLink(p),
        p.entrega ? `\`${dv.date(p.entrega).toFormat("yyyy-MM-dd")}\`` : "-",
        p.status ?? "-",
        diasRestantes(p.entrega)
    ])
);

~~~

