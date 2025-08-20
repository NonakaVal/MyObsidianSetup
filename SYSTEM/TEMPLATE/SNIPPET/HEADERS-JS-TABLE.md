

```dataviewjs
// ⚙️ 
const folderPath = "CALENDAR/DAILY";

const dateRange = {
  start: new Date("2025-02"),
  end: new Date("2025-04-01")
};

const maxHeaders = 3;

let tableRows = [];
let headerNames = []; 

// Filtra páginas por pasta e data
const pages = dv.pages()
  .where(p => p.file.path.startsWith(folderPath))
  .where(p => {
    const d = new Date(p.file.name);
    return d >= dateRange.start && d <= dateRange.end;
  })
  .sort(p => p.file.name, 'asc');

for (const page of pages) {
  const lines = (await dv.io.load(page.file.path)).split('\n');
  const headers = [], sections = {}, headerRegex = /^# (.+)/;
  let current = null;

  for (const l of lines) {
    const m = l.match(headerRegex);
    if (m && headers.length < maxHeaders) {
      current = m[1].trim();
      headers.push(current);
      sections[current] = [];
    } else if (current && headers.includes(current)) {
      sections[current].push(l.trim());
    }
  }

  // Armazena os nomes reais dos headers da primeira nota com headers suficientes
  if (headerNames.length === 0 && headers.length > 0) {
    headerNames = [...headers];
  }

  const row = [page.file.link, ...headerNames.map(h => sections[h]?.join('\n') || "")];
  tableRows.push(row);
}

// Títulos reais das colunas
const columnTitles = ["🗓️", ...headerNames.map(h => `${h}`)];

dv.table(columnTitles, tableRows);

```

