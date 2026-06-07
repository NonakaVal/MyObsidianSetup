~~~dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES_POR_PRAZO = {
    TRANQUILO: "🟢",
    ATENCAO: "🟡",
    ATRASADO: "🔴",
    SEM_DATA: "⚪"
};

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function getIconPorPrazo(entrega) {
    if (!entrega) return ICONES_POR_PRAZO.SEM_DATA;

    const hoje = dv.luxon.DateTime.now();
    const dEntrega = dv.date(entrega);
    const diff = Math.floor(dEntrega.diff(hoje, "days").days);

    if (diff < 0) return ICONES_POR_PRAZO.ATRASADO;
    if (diff <= 7) return ICONES_POR_PRAZO.ATENCAO;
    return ICONES_POR_PRAZO.TRANQUILO;
}

function estilizarLink(p) {
    return `**${dv.fileLink(p.file.path, false, p.file.name)}**`;
}

function diasRestantes(entrega) {
    if (!entrega) return "-";
    const hoje = dv.luxon.DateTime.now();
    const dEntrega = dv.date(entrega);
    const diff = Math.floor(dEntrega.diff(hoje, "days").days);
    return diff >= 0 ? `${diff} d` : `${diff} d (atrasado)`;
}

//-----------------------------------------------------
// COLETA E FILTRO
//-----------------------------------------------------
const pages = dv.pages('"06 MissionsProjects/Ongoing"')
    .where(p => p.type && p.type == "project")
    .sort(p => p.file.mtime, 'desc');

//-----------------------------------------------------
// EXIBIÇÃO
//-----------------------------------------------------
dv.table(
    ["", "📄", "📅 Entrega", "⭐ Status", "⏳ Prazo"],
    pages.map(p => [
        getIconPorPrazo(p.entrega),
        estilizarLink(p),
        p.entrega ? `\`${dv.date(p.entrega).toFormat("yyyy-MM-dd")}\`` : "-",
        p.status ?? "-",
        diasRestantes(p.entrega)
    ])
);
~~~
