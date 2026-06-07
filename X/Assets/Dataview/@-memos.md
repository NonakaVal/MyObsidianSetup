~~~dataviewjs  
const folderPath = "Memos/Open";

// ── PRIORIDADE ──
const PRIORITY = {
  FRESH:   { maxDays: 0.042,  icon: "⚡" },
  TODAY:   { maxDays: 1,      icon: "🟢" },
  WEEK:    { maxDays: 7,      icon: "🟡" },
  MONTH:   { maxDays: 30,     icon: "🟠" },
  OLD:     { maxDays: 90,     icon: "🔴" },
  ANCIENT: { maxDays: Infinity, icon: "💀" },
};

// ── HELPERS ──
const getAgeDays = d => {
  if (!d) return null;
  return (Date.now() - d.toJSDate().getTime()) / 864e5;
};

const formatAge = d => {
  if (!d) return "—";
  const totalMinutes = (Date.now() - d.toJSDate().getTime()) / 6e4;

  if (totalMinutes < 1) return "agora";
  if (totalMinutes < 60) return `${totalMinutes | 0}min`;

  const hours = totalMinutes / 60;
  if (hours < 24) return `${hours | 0}h`;

  const days = hours / 24;
  if (days < 30) return `${days | 0}d`;

  const months = days / 30.44;
  if (months < 12) return `${months | 0}m`;

  return `${(months / 12) | 0}a`;
};

const formatExact = d => {
  if (!d) return "";
  const days = getAgeDays(d);

  if (days < 1) {
    const h = (days * 24) | 0;
    const m = ((days * 1440) % 60) | 0;
    return h > 0 ? `${h}h ${m}min atrás` : `${m}min atrás`;
  }

  if (days < 2) return `${(days * 24) | 0}h atrás`;
  if (days < 30) return `${days | 0} dias atrás`;

  const months = days / 30.44;
  if (months < 12) return `${months | 0} meses atrás`;

  const years = months / 12;
  return `${years | 0} anos atrás`;
};

const getPriority = d => {
  const age = getAgeDays(d);
  if (age === null) return { icon: "❓" };

  for (const level of Object.values(PRIORITY)) {
    if (age <= level.maxDays) return level;
  }

  return PRIORITY.ANCIENT;
};

// ── COLETA ──
const pages = dv.pages()
  .where(p => p.file.path.startsWith(folderPath + "/"))
  .array()
  .sort((a, b) => (a.file.mtime?.ts || 0) - (b.file.mtime?.ts || 0));

// ── TABELA ──
dv.table(
  ["",""],
  pages.map(p => {
    const prio  = getPriority(p.file.mtime);
    const curto = formatAge(p.file.mtime);
    const exact = formatExact(p.file.mtime);

    const tempo = dv.el("span", `${prio.icon} ${curto}`);
    tempo.title = exact;

    return [
      tempo,
      p.file.link
    ];
  })
);
~~~
