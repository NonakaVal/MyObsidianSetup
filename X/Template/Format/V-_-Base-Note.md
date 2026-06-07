<%*
// ── V-_ · NOTA BASE (Not A Dev) ──────────────────────────────────────
// Template genérico para qualquer nota da área Not A Dev
// Permite escolher a pasta de destino manualmente
const baseFolder = "08 Focus Areas/Not A Dev";
const allFolders = tp.app.vault.getAllLoadedFiles()
  .filter(f => f instanceof tp.obsidian.TFolder && f.path.startsWith(baseFolder));

const selectedFolder = await tp.system.suggester(
  (f) => f.path.replace(baseFolder + "/", ""),
  allFolders,
  false,
  "Selecione a pasta de destino:"
);

const destFolder = selectedFolder ? selectedFolder.path : baseFolder;
-%>
---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
area:
  - "[[Not A Dev]]"
tags:
  - work
---

<%tp.file.cursor()%>

<%*
await tp.file.move(`${destFolder}/${tp.file.title}`);
-%>
