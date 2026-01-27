
````tabs
tab: Modified


```dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES_POR_PASTA = {
    "NonakaLab Channel": "🧪",
    "Areas": "🗂️",
    "Projects & Areas": "⚡",
    "Index & Bases": "📚",
    "+": "📝",
    "Maps": "🌍",
    "X": "🛠️"
};

const ICONE_DEFAULT = "📄";

const PASTAS_INCLUIR = [
    /^Projects & Areas/,
    /^Index & Bases/
];

const PASTAS_EXCLUIR = [
    /^X\//
];

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function deveIncluir(pasta) {
    return PASTAS_INCLUIR.some(r => r.test(pasta)) &&
           !PASTAS_EXCLUIR.some(r => r.test(pasta));
}

function getIcon(folderPath) {
    const parts = folderPath.split("/").map(p => p.toUpperCase());

    for (let i = parts.length - 1; i >= 0; i--) {
        const key = Object.keys(ICONES_POR_PASTA).find(
            k => k.toUpperCase() === parts[i]
        );
        if (key) return ICONES_POR_PASTA[key];
    }

    return ICONE_DEFAULT;
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
// COLETA
//-----------------------------------------------------
const pages = dv.pages("")
    .where(p => deveIncluir(p.file.folder))
    .sort(p => p.file.mtime, 'desc')
    .limit(6);

//-----------------------------------------------------
// EXIBIÇÃO
//-----------------------------------------------------
dv.table(
    ["", "📄 Nota", "🕒 Modificação", "⏳"],
    pages.map(p => [
        getIcon(p.file.folder),
        estilizarLink(p),
        `\`${p.file.mtime.toFormat("yyyy-MM-dd HH:mm")}\``,
        `\`${formatarIdade(p.file.mtime)}\``
    ])
);


```

tab: Created 

```dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES_POR_PASTA = {
    "NonakaLab Channel": "🧪",
    "Areas": "🗂️",
    "Projects & Areas": "⚡",
    "Index & Bases": "📚",
    "+": "📝",
    "Maps": "🌍",
    "X": "🛠️"
};

const ICONE_DEFAULT = "📄";

const PASTAS_INCLUIR = [
    /^Projects & Areas/,
    /^Index & Bases/
];

const PASTAS_EXCLUIR = [
    /^X\//
];

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function deveIncluir(pasta) {
    return PASTAS_INCLUIR.some(r => r.test(pasta)) &&
           !PASTAS_EXCLUIR.some(r => r.test(pasta));
}

function getIcon(folderPath) {
    const parts = folderPath.split("/").map(p => p.toUpperCase());

    for (let i = parts.length - 1; i >= 0; i--) {
        const key = Object.keys(ICONES_POR_PASTA).find(
            k => k.toUpperCase() === parts[i]
        );
        if (key) return ICONES_POR_PASTA[key];
    }

    return ICONE_DEFAULT;
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
// COLETA
//-----------------------------------------------------
const pages = dv.pages("")
    .where(p => deveIncluir(p.file.folder))
    .sort(p => p.file.ctime, 'desc')
    .limit(6);

//-----------------------------------------------------
// EXIBIÇÃO
//-----------------------------------------------------
dv.table(
    ["", "📄 Nota", "🕒 Criada", "⏳"],
    pages.map(p => [
        getIcon(p.file.folder),
        estilizarLink(p),
        `\`${p.file.mtime.toFormat("yyyy-MM-dd HH:mm")}\``,
        `\`${formatarIdade(p.file.mtime)}\``
    ])
);

```

````







