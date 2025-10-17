~~~dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES = {
    "AULAS": "📚",
    "PROJETOS": "🛠️",
    "EFFORTS": "⚡",
    "NOTAS": "📝",
    "ATLAS": "🌍",
    "DEFAULT": "📄"
};

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function getIcon(folder) {
    const upperFolder = folder.toUpperCase();
    return ICONES[Object.keys(ICONES).find(key => upperFolder.includes(key))] || ICONES.DEFAULT;
}

function formatarIdade(data) {
    const diff = Date.now() - data.toJSDate().getTime();
    const minutos = diff / 1000 / 60;

    if (minutos < 60) return `${Math.floor(minutos)} min`;
    if (minutos < 1440) return `${Math.floor(minutos / 60)} h`;
    if (minutos < 43200) return `${Math.floor(minutos / 1440)} d`;
    if (minutos < 525600) return `${Math.floor(minutos / 43200)} m`;
    return `${Math.floor(minutos / 525600)} a`;
}

function estilizarLink(p) {
    return `**${dv.fileLink(p.file.path, false, p.file.name)}**`;
}

//-----------------------------------------------------
// COLETA E FILTRO
//-----------------------------------------------------
const pages = dv.pages('"Projects & Areas/Areas"')
    .where(p => p.type && p.type == "area_family")
    .sort(p => p.file.mtime, 'desc')
    .limit(20);

//-----------------------------------------------------
// EXIBIÇÃO (sem coluna de data)
//-----------------------------------------------------
dv.table(
    ["", "📄", "🕐"],
    pages.map(p => [
        getIcon(p.file.folder),
        estilizarLink(p),
        `\`${formatarIdade(p.file.mtime)}\``
    ])
);

~~~
