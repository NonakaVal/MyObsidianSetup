
~~~dataviewjs
//-----------------------------------------------------
// ID ÚNICO PARA OCULTAR CABEÇALHO APENAS DESTA TABELA
//-----------------------------------------------------
const uid = "dv-" + Math.random().toString(36).slice(2, 7);
this.container.setAttribute("id", uid);
const style = this.container.createEl("style");
style.textContent = `#${uid} thead { display: none; }`;

//-----------------------------------------------------
// CONFIGURAÇÃO
//-----------------------------------------------------
const ICONES = {
  "Learning":            "📚",
  "Val Channel":         "📺",
  "Not A Dev":           "📺",
  "Collectors Guardian": "🧰",
  "Autoconhecimento":    "🫤",
  "DEFAULT":             "📄"
};

const PRIORITY = {
  FRESH:   { maxDays: 0.042,    icon: "⚡" },
  TODAY:   { maxDays: 1,        icon: "🟢" },
  WEEK:    { maxDays: 7,        icon: "🟡" },
  MONTH:   { maxDays: 30,       icon: "🟠" },
  OLD:     { maxDays: 90,       icon: "🔴" },
  ANCIENT: { maxDays: Infinity, icon: "💀" },
};

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function getIcon(folder) {
  const upperFolder = folder.toUpperCase();
  const match = Object.keys(ICONES).find(key =>
    upperFolder.includes(key.toUpperCase())
  );
  return ICONES[match] || ICONES.DEFAULT;
}

function getAgeDays(data) {
  return (Date.now() - data.toJSDate().getTime()) / 864e5;
}

function getPriority(data) {
  if (!data) return { icon: "❓" };
  const age = getAgeDays(data);
  for (const level of Object.values(PRIORITY)) {
    if (age <= level.maxDays) return level;
  }
  return PRIORITY.ANCIENT;
}

function formatarIdade(data) {
  if (!data) return "—";
  const diff = Date.now() - data.toJSDate().getTime();
  const min  = diff / 6e4;

  if (min < 1)    return "agora";
  if (min < 60)   return `${min | 0}min`;
  if (min < 1440) return `${(min / 60) | 0}h`;

  const dias = min / 1440;
  if (dias < 30)  return `${dias | 0}d`;

  const meses = dias / 30.44;
  if (meses < 12) return `${meses | 0}m`;

  return `${(meses / 12) | 0}a`;
}

function contarNotasNaPasta(folderPath) {
  return dv.pages(`"${folderPath}"`).length;
}

//-----------------------------------------------------
// COLETA
//-----------------------------------------------------
const pages = dv.pages('"08 Focus Areas"')
  .where(p => p.type && p.type == "area_family")
  .sort(p => p.file.mtime, 'desc')
  .limit(20);

//-----------------------------------------------------
// TABELA
//-----------------------------------------------------
dv.table(
  ["", "Área", "Notas", "Atualização"],
  pages.map(p => {
    const prio  = getPriority(p.file.mtime);
    const curto = formatarIdade(p.file.mtime);
    const count = contarNotasNaPasta(p.file.folder);

    return [
      `${prio.icon} ${curto}`,
      getIcon(p.file.folder),
      p.file.link,
      count
    ];
  })
);
~~~

