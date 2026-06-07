🧱 Build | 🪜 Renovate
~~~dataviewjs
//-----------------------------------------------------
// CONFIGURAÇÃO — ARCHITECT
//-----------------------------------------------------

const PRIORITY = [
  { maxDays: 0.042,    icon: "⚡", color: "#38bdf8" },  // < 1 hora
  { maxDays: 1,        icon: "🟢", color: "#4ade80" },  // até 1 dia
  { maxDays: 7,        icon: "🟡", color: "#facc15" },  // até 7 dias
  { maxDays: 30,       icon: "🟠", color: "#fb923c" },  // até 30 dias
  { maxDays: 90,       icon: "🔴", color: "#f87171" },  // até 90 dias
  { maxDays: Infinity, icon: "💀", color: "#e879f9" },  // > 90 dias
];

const ARCHITECT_ICONS = {
  "#architect/build":    "🧱",
  "#architect/renovate": "🪜",
};

//-----------------------------------------------------
// FUNÇÕES AUXILIARES
//-----------------------------------------------------
function getAgeDays(data) {
  if (!data) return null;
  return (Date.now() - data.toJSDate().getTime()) / 864e5;
}
function getPriority(data) {
  if (!data) return { icon: "❓", color: "#666" };
  const age = getAgeDays(data);
  return PRIORITY.find(p => age <= p.maxDays) || PRIORITY.at(-1);
}
function formatarIdade(data) {
  if (!data) return "—";
  const min = (Date.now() - data.toJSDate().getTime()) / 6e4;
  if (min < 1)    return "agora";
  if (min < 60)   return `${min | 0}min`;
  if (min < 1440) return `${(min / 60) | 0}h`;
  const dias = min / 1440;
  if (dias < 30)  return `${dias | 0}d`;
  const meses = dias / 30.44;
  if (meses < 12) return `${meses | 0}m`;
  return `${(meses / 12) | 0}a`;
}
function formatarExato(data) {
  if (!data) return "";
  const dias = getAgeDays(data);
  if (dias < 1) {
    const h = (dias * 24) | 0;
    const m = ((dias * 1440) % 60) | 0;
    return h > 0 ? `${h}h ${m}min atrás` : `${m}min atrás`;
  }
  if (dias < 2)  return `${(dias * 24) | 0}h atrás`;
  if (dias < 30) return `${dias | 0} dias atrás`;
  const meses = dias / 30.44;
  if (meses < 12) return `${meses | 0} ${meses < 2 ? "mês" : "meses"} atrás`;
  const anos = meses / 12;
  return `${anos | 0} ${anos < 2 ? "ano" : "anos"} atrás`;
}
function getArchitectIcon(tags) {
  if (!tags) return "";
  const arr = Array.isArray(tags) ? tags : [tags];
  for (const [tag, icon] of Object.entries(ARCHITECT_ICONS)) {
    if (arr.some(t => t === tag || t === tag.replace("#", ""))) return icon + " ";
  }
  return "";
}
function getFolderLabel(p) {
  if (p.file.folder.includes("+")) return p.file.folder;
  const match = p.file.path.match(/.+\/([^/]+)\/[^/]+$/);
  return match ? match[1] : p.file.folder;
}
function getArchitectTags(tags) {
  if (!tags) return "";
  const arr = Array.isArray(tags) ? tags : [tags];
  return arr.filter(t => t.startsWith("#architect/") || t.startsWith("architect/")).join(", ");
}

//-----------------------------------------------------
// COLETA
//-----------------------------------------------------
const pages = dv.pages("#architect and -\"30 Knowlegde/35 Recources/Ideaverse Pro 2\"")
  .where(p => !p.file.name.includes("Master Key (Architect Tags)"))
  .sort(p => p.file.mtime, "desc")
  .limit(77);

//-----------------------------------------------------
// RENDER
//-----------------------------------------------------
const root = dv.el("div", "");
root.style.cssText = `
  background: #0d1117;
  border: 1px solid #21262d;
  padding: 12px 16px;
  border-radius: 10px;
  color: #e6edf3;
  font-size: 0.64rem;
  box-shadow: 0 2px 8px #00000040;
`;

const header = document.createElement("div");
header.style.cssText = `
  display: grid;
  grid-template-columns: 1fr 9em 11em 6em;
  gap: 8px;
  padding: 0 4px 8px 4px;
  border-bottom: 1px solid #30363d;
  color: #8b949e;
  font-weight: 700;
  font-size: .64rem;
  letter-spacing: .07em;
  text-transform: uppercase;
`;
header.innerHTML = `<span>📝</span><span>🏷️</span><span>📁</span><span style="text-align:right">🕐</span>`;
root.appendChild(header);

pages.array().forEach(p => {
  const prio   = getPriority(p.file.mtime);
  const curto  = formatarIdade(p.file.mtime);
  const exato  = formatarExato(p.file.mtime);
  const prefix = getArchitectIcon(p.file.tags);
  const tagStr = getArchitectTags(p.file.tags);
  const folder = getFolderLabel(p);

  const row = document.createElement("div");
  row.style.cssText = `
    display: grid;
    grid-template-columns: 1fr 9em 11em 6em;
    gap: 8px;
    align-items: center;
    padding: 6px 4px;
    border-top: 1px solid #21262d;
    transition: background .1s;
  `;
  row.onmouseenter = () => row.style.background = "#161b22";
  row.onmouseleave = () => row.style.background = "";

  const colNote = document.createElement("span");
  colNote.style.cssText = "overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:1rem";
  if (prefix) {
    const em = document.createElement("span");
    em.textContent = prefix;
    colNote.appendChild(em);
  }
  colNote.appendChild(dv.el("span", p.file.link));

  const colTags = document.createElement("span");
  colTags.style.cssText = "font-size:.8rem;color:#8b949e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis";
  colTags.textContent = tagStr;

  const colFolder = document.createElement("span");
  colFolder.style.cssText = `
    font-size: 0.5rem;
    color: #8b949e;
    background: #21262d;
    border-radius: 4px;
    padding: 2px 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  `;
  colFolder.textContent = folder;

  const colTime = document.createElement("span");
  colTime.title = exato;
  colTime.style.cssText = `
    text-align: right;
    white-space: nowrap;
    font-size: .85rem;
    color: ${prio.color};
    font-weight: 600;
    font-variant-numeric: tabular-nums;
  `;
  colTime.textContent = `${prio.icon} ${curto}`;

  row.append(colNote, colTags, colFolder, colTime);
  root.appendChild(row);
});

const footer = document.createElement("div");
footer.style.cssText = "margin-top:8px;text-align:right;color:#484f58;font-size:.75rem";
footer.textContent = `${pages.length} nota${pages.length !== 1 ? "s" : ""}`;
root.appendChild(footer);
~~~
