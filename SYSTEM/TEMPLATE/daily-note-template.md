---
created: <% tp.file.creation_date() %>
tags:
  - calendar/daily
---

<% tp.web.daily_quote() %>

Last modified : `$= dv.current().file.mtime`

Mood : `INPUT[inlineSelect(option('🙂 – Neutral'), option('😄 – Happy'), option('😐 – Meh'), option('😞 – Sad'), option('😠 – Frustrated'), showcase):daily-mood]`




# Workbench
````tabs
tab: write

tab: Last notes
```dataviewjs
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

const PASTAS_INCLUIR = [
    /.*\+.*/,
    /^EFFORTS/,
    /^ATLAS/
];

const PASTAS_EXCLUIR = [
    /^System\//
];

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function deveIncluir(pasta) {
    return PASTAS_INCLUIR.some(regex => regex.test(pasta)) &&
           !PASTAS_EXCLUIR.some(regex => regex.test(pasta));
}

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
// COLETA E AGRUPAMENTO
//-----------------------------------------------------
const pages = dv.pages("")
    .where(p => deveIncluir(p.file.folder))
    .sort(p => p.file.mtime, 'desc')
    .limit(10);  // 🔥 Alterado para 10 notas

//-----------------------------------------------------
// EXIBIÇÃO
//-----------------------------------------------------
dv.table(
    ["", "📄 Nota", "🕒 Modificação", "⏳ Desde modificação"],
    pages.map(p => [
        getIcon(p.file.folder),
        estilizarLink(p),
        `\`${p.file.mtime.toFormat("yyyy-MM-dd HH:mm")}\``,
        `\`${formatarIdade(p.file.mtime)}\``
    ])
);

```
````


# Tasks

````tabs
tab: Calendar tasks
![[@_dataview_Calendar-tasks]]

tab: Efforts Tasks
![[@_dataview-efforts-tasks]]

tab: All tasks
![[@_dataview-all-tasks]]
````


# Daily LOG 


