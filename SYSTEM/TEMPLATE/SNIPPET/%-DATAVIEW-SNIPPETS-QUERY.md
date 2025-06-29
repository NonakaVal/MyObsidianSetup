---
cssclasses:
  - wide-page
---
# DATAVIEW SYSTEM TEMPLATES

```dataviewjs
// 🧠 Lista snippets em arquivos Markdown filtrados por palavras-chave no nome do arquivo
const folderPath = "SYSTEM/TEMPLATE"; // 📁 Caminho da pasta onde estão os templates/snippets
const keywords = [""]; // 🔑 Lista de palavras-chave obrigatórias no título do arquivo (pode ser preenchida)

let tableRows = []; // 🧱 Armazena as linhas da tabela a ser exibida

// 📄 Seleciona e filtra páginas dentro da pasta-alvo, onde o nome do arquivo contém ao menos uma das palavras-chave
const pages = dv.pages()
  .where(p =>
    p.file.path.startsWith(folderPath) &&
    keywords.some(k => p.file.name.toLowerCase().includes(k.toLowerCase()))
  )
  .sort(p => p.file.name, 'desc'); // 🗂️ Ordena pela ordem alfabética decrescente do nome

// 🔁 Itera sobre os arquivos filtrados
for (const page of pages) {
  // 📥 Carrega o conteúdo do arquivo de forma assíncrona
  const content = await dv.io.load(page.file.path);

  // 🔒 Escapa delimitadores de blocos de código (```) para evitar quebra de renderização
  const safeContent = content.replace(/```/g, "\\`\\`\\`");

  // 🧱 Formata como bloco de código Markdown (tripla crase)
  const codeBlock = `\`\`\`markdown\n${safeContent.trim()}\n\`\`\``;

  // ➕ Adiciona uma linha à tabela com o link e o conteúdo formatado
  tableRows.push([page.file.link, codeBlock]);
}

// 📊 Exibe a tabela com duas colunas: nome do snippet e o código
dv.table(["📄 Note", "Content"], tableRows);


```
