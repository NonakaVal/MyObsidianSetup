---
dateCreated: "[[2025-06-28]]"
cssclasses:
  - dashboard
---
# SNIPETS

```dataviewjs
// 📑 Lista todos os templates (com conteúdo) a partir de uma pasta específica

const folderPath = "CODE/05_SNIPPETS"; // Caminho da pasta de templates
const keywords = [""]; // Filtra pelo título (ex: ["api", "email"]), ou deixe [""] para exibir tudo

let tableRows = [];

const pages = dv.pages()
  .where(p =>
    p.file.path.startsWith(folderPath) &&
    keywords.some(k => p.file.name.toLowerCase().includes(k.toLowerCase()))
  )
  .sort(p => p.file.name, 'asc');

for (const page of pages) {
  const content = await dv.io.load(page.file.path);
  const safeContent = content.replace(/```/g, "\\`\\`\\`"); // evita conflitos na renderização
  const codeBlock = `\`\`\`\n${safeContent.trim()}\n\`\`\``;

  tableRows.push([page.file.link, codeBlock]);
}

dv.table(["📄 Template", "📋 Conteúdo"], tableRows);

```
# 📁 CODE

## 📂 +

- 📄 [[INDEX-CODE]]
- 📄 [[Similar-Search.py-2025-06-26]]
- 📄 [[Zettell.py-2025-06-16]]
## 📂 05_SNIPPETS

- Auxiliares de Env
	- 📄 [[! py Lazy Commits]]
	- 📄 [[% wsl bash FZF Code Search Suite]]
	- 📄 [[$ py from config import MAIN_PATH]]
- Pandas Utils
	- 📄 [[! py list_files(directory_path)]]
	- 📄 [[! py group_by]]
	- 📄 [[! py get_df_info (df) - print data info pandas]]
	- 📄 [[! py to_categorical(series, categories=None, ordered=False)]]
	- 📄 [[! py validate_dtype(series, expected_dtype)]]
	- 📄 [[! py check_nulls(series, raise_error=False, threshold=0)]]
	- 📄 [[! py convert_currency(series, symbol='$', decimals=True)]]
	- 📄 [[! py to_numeric_safe(series)]]
	- 📄 [[! py calcular_percentual_por_faixa(dados, coluna, classes, labels)]]
	- 📄 [[! py  filter_outliers_iqr]]
- Outros
	- 📄 [[% py _carregar_palavras_comuns]]
	- 📄 [[% py confirmar_acao(mensagem. str)]]
	- 📄 [[% py quick_text_fix]]
## 📂 06_COMPONENT

- 📄 [[cmp-EditNotes]]
- 📄 [[cmp-ambientes-anaconda]]
- 📄 [[cmp-first-ripgrep-regex-queries]]
- 📄 [[cmp-get-dataframe-info]]
- 📄 [[cmp-git-branches]]
- 📄 [[cmp-github]]
- 📄 [[cmp-pandas-fillna-nullvalues-wrangling]]
- 📄 [[cmp-pandas-groupby-method]]
- 📄 [[cmp-pandas-importing-data]]
- 📄 [[cmp-python-datetime(datas)-methods]]
- 📄 [[cmp-streamlit-crewai-market-research-app]]
## 📂 07_DOC

- 📄 [[doc-OlistProductUpdate]]
- 📄 [[doc-metodos-de-testes-hipoteses]]
- 📄 [[doc-obsdian-metabind-plugin]]
- 📄 [[doc-pandas-methods]]
- 📄 [[doc-playbook-ecommerce]]
- 📄 [[doc-python-defined-functions]]
- 📄 [[doc-scoop-package-mageger-guide]]
- 📄 [[doc-seaborn-data-visualization-methods]]
- 📄 [[doc-seaborn-matplotlib-charts]]
- 📄 [[doc-seaborn-plots]]
- 📄 [[doc-sklearn-simple-linear-regression-model]]
- 📄 [[python-combinação-e-comparação-de-dados]]
- 📄 [[python-criação-e-manipulação-de-séries-categóricas]]
- 📄 [[python-manipulação-de-dados]]
- 📄 [[python-manipulação-de-datas]]
- 📄 [[python-manipulação-de-strings-e-pesquisa]]
- 📄 [[snip-git-reset-commit-to-main]]
- 📄 [[snip-rg-search-code]]
## 📂 08_WORKFLOW

- 📄 [[flow-Verify-DataTypes]]
- 📄 [[flow-build-setup-codeSearch-with-ripgrep-fzf-bat]]
- 📄 [[flow-obtencao-dados-amostrais]]
- 📄 [[flow-pandas-basic-data-manipulation]]
- 📄 [[flow-pandas-data-cleaning-methods]]
- 📄 [[flow-pandas-null-values-wrangling]]
- 📄 [[flow-whatsApp-arena-report]]