---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
tags:
  - memo
---

<%*
const folderPath = "Memos";
if (!tp.app.vault.getAbstractFileByPathInsensitive(folderPath)) {
  await tp.app.vault.createFolder(folderPath);
}
await tp.file.move(`${folderPath}/${tp.file.title}`);
-%>
