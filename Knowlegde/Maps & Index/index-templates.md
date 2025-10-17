---
created: "[[2025-06-24]]"
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
  - wide-page
---
# 📁 DASHBOARD

Last modified :   `="[[" + dateformat(date(today), "yyyy-MM-dd") + "]]"` - `$= dv.current().file.mtime`
## 🗂 **System Templates**

Modelos estruturais usados na organização de notas, tarefas e logs.

### 📅 Organização de Notas

- 📄 [[daily-note-template]]
- 📄 [[MONTHLY-note-template]]

- 📄 [[TEMPLATE-NEW-SKETCH-NOTE]]

- 📄 [[TEMPLATE-NEW-AREA]]

- 📄 [[+ PYTHON-DRAFT]]
- 📄 [[+ CODE-SNIPPET]]

#### 📘 Snippets Internos

- 📄 [[add Last modified line (link)]]
- 📄 [[%-TASK-DV-GLOBAL-TABS]]
- 📄 [[%-TASK-AREA-TASKS]]
- 📄 [[%-TASK-DV-FOLDER]]
- 📄 [[HEADERS-JS-TABLE]]
- 📄 [[%-DAILY-LOG-DATAVIEW]]
- 📄 [[%-TRACKER-OVERVIEW]]
- 
    

## CODE snippets

- 📄 [[$ py from config import MAIN_PATH]]
- 📄 [[! py list_files(directory_path)]]
- 📄 [[! py get_df_info (df) - print data info pandas]]
- 📄 [[! py check_nulls(series, raise_error=False, threshold=0)]]
- 📄 [[! py to_numeric_safe(series)]]
- 📄 [[! py  filter_outliers_iqr]]
- 📄 [[! py convert_currency(series, symbol='$', decimals=True)]]
- 📄 [[! py to_categorical(series, categories=None, ordered=False)]]
- 📄 [[! py validate_dtype(series, expected_dtype)]]
- 📄 [[! py group_by]]
- 📄 [[! py calcular_percentual_por_faixa(dados, coluna, classes, labels)]]
- 📄 [[% py quick_text_fix]]
- 📄 [[% py _carregar_palavras_comuns]]
- 📄 [[% py confirmar_acao(mensagem. str)]]
    

### 🖥️ WSL / Bash

- 📄 [[% wsl bash FZF Code Search Suite]]
    


---

# DATAVIEW SYSTEM TEMPLATES

```dataviewj
// 🧠 Snippets em Code Block Python com filtro por palavras-chave no título
const folderPath = "SYSTEM/TEMPLATE";
const keywords = [""]; // 🔑 Termos obrigatórios no título

let tableRows = [];

const pages = dv.pages()
  .where(p =>
    p.file.path.startsWith(folderPath) &&
    keywords.some(k => p.file.name.toLowerCase().includes(k.toLowerCase()))
  )
  .sort(p => p.file.name, 'desc');

for (const page of pages) {
  const content = await dv.io.load(page.file.path);
  const safeContent = content.replace(/```/g, "\\`\\`\\`");
  const codeBlock = `\`\`\`\n${safeContent.trim()}\n\`\`\``;

  tableRows.push([page.file.link, codeBlock]);
}

dv.table(["📄 Snippet", "💻 Código"], tableRows);

```

# DATAVIEW CODE SNIPPETS
```dataviewj
// 🧠 Snippets em Code Block Python com filtro por palavras-chave no título
const folderPath = "CODE/05_SNIPPETS";
const keywords = [""]; // 🔑 Termos obrigatórios no título

let tableRows = [];

const pages = dv.pages()
  .where(p =>
    p.file.path.startsWith(folderPath) &&
    keywords.some(k => p.file.name.toLowerCase().includes(k.toLowerCase()))
  )
  .sort(p => p.file.name, 'asc');

for (const page of pages) {
  const content = await dv.io.load(page.file.path);
  const safeContent = content.replace(/```/g, "\\`\\`\\`");
  const codeBlock = `\`\`\`python\n${safeContent.trim()}\n\`\`\``;

  tableRows.push([page.file.link, codeBlock]);
}

dv.table(["📄 Snippet", "💻 Código"], tableRows);

```
