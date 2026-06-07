---
path: '"Calendar & Review/Daily Notes"'
cssclasses:
  - wide-page
---
# Definir Pasta e Colunas


---

| `Marcador`                        | `Nome da Seção`                 | `Expandir na Tabela?`               |
| ------------------------------- | ----------------------------- | --------------------------------- |
| `INPUT[text:configs[0].marker]` | `INPUT[text:configs[0].name]` | `INPUT[toggle:configs[0].expand]` |
| `INPUT[text:configs[1].marker]` | `INPUT[text:configs[1].name]` | `INPUT[toggle:configs[1].expand]` |
| `INPUT[text:configs[2].marker]` | `INPUT[text:configs[2].name]` | `INPUT[toggle:configs[2].expand]` |
| `INPUT[text:configs[3].marker]` | `INPUT[text:configs[3].name]` | `INPUT[toggle:configs[3].expand]` |
| `INPUT[text:configs[4].marker]` | `INPUT[text:configs[4].name]` | `INPUT[toggle:configs[4].expand]` |

---

# Mapas e Conteúdos

```dataviewjs
const configs = dv.current().configs;
const path = dv.current().path;

if (!configs || !path) {
  dv.span("⚠️ Configurações ou caminho não definidos.");
  return;
}

// Força formato expansível
function makeExpandable(calloutType, title, content) {
  return `> [!${calloutType}]- ${title}\n> ${content.join("\n> ")}`;
}

// Extração com toggle
async function extractSection(page, section) {
  const lines = (await dv.io.load(page.file.path)).split("\n");
  let content = [];
  let capturing = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (line.includes(section.marker) && section.marker.trim() !== "") {
      capturing = true;
      continue;
    }

    if (capturing) {
      if (configs.some(c => c.marker && line.includes(c.marker)) && !line.includes(section.marker)) break;
      if (/^#{2,3}\s/.test(line) && line.trim() !== section.marker.trim()) break;
      if (line.trim() === "" && lines[i + 1]?.trim() === "") break;
      if (line.trim()) content.push(line.trim());
    }
  }

  if (content.length > 0) {
    if (section.expand) {
      // 🔹 Usa callout "limpo" com título
      const calloutType = section.marker.match(/\[!(.*?)\]/)?.[1] || "info";
      const title = section.name || section.title || "";
      return makeExpandable(calloutType, title, content);
    } else {
      // 🔹 Retorna apenas conteúdo cru
      return content.join("\n");
    }
  }
  return "";
}

// Monta tabela
const pages = dv.pages(path).sort(p => p.file.name, "asc");
const rows = [];

for (const page of pages) {
  const row = [page.file.link];
  for (const section of configs) {
    row.push(await extractSection(page, section));
  }
  if (row.some((cell, i) => i > 0 && cell)) rows.push(row);
}

dv.table(["Aula", ...configs.map(s => s.name || "(Sem Nome)")], rows);

```