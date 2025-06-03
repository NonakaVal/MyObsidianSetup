# 📂 Estrutura da Vault

## Folder System

- **📂 <font color = 00bbfff>Atlas</font>** — Notas de estudo e literárias  
	- **00_DRAFT** — Rascunhos brutos de ideias e estudos ainda em construção  
	- **01_INDEX** — Mapas e índices para navegar e interconectar as notas  
	- **02_CONCEPT** — Conceitos teóricos, definições e modelos explicativos  
	- **03_SNIPPETS** — Trechos de código reutilizáveis e exemplos práticos  
	- **04_COMPONENT** — Blocos reutilizáveis, funções, algoritmos e padrões  
	- **05_DOC** — Documentações explicativas ou tutoriais  
	- **06_WORKFLOW** — Passo a passo de processos práticos ou pipelines  
	- **07 _RESOURCES** — Links, artigos, livros, PDFs, vídeos e materiais externos  
	- **08_MAPS** — Mapas mentais e representações visuais de temas  

- **📂 <font color = 00bbfff>Calendar</font>** — Calendários e notas diárias ou periódicas  
	- **DAILY** — Anotações diárias, diário de bordo, tarefas e insights  
	- **MONTHLY** — Planejamento e reflexões mensais  
	- **WEEKLY** — Planejamento e revisão semanal  
	- **YARLY** — Revisões e metas anuais  

- **📂 <font color = 00bbfff>Drafts</font> — Rascunhos avulsos e notas não categorizadas**

- **📂 <font color = 00bbfff>Efforts</font>** — Direcionamento de esforços e projetos ativos 
	- **09_AREAS** — Áreas de foco contínuo (saúde, finanças, carreira, etc.)  
	- **10_PROJECTS** — Projetos com começo, meio e fim definidos  
	- **11_ARCHIVES** — Projetos concluídos ou pausados  
	- **12_RESOURCES** — Materiais de apoio e referência específica para projetos  
	- **13_WORKSTATION** — Anotações operacionais do dia a dia de execução  

- **📂 <font color = 00bbfff>LEISURE</font>** — Conteúdos de lazer, cultura e hobbies
	- **MUSIC** — Músicas, playlists, artistas favoritos e estudos musicais  

- **📂 <font color = 00bbfff>Social</font>** — Reflexões pessoais e interações humanas
	- **PEOPLE** — Notas sobre pessoas, contatos, redes ou perfis importantes  
	- **THINKING** — Pensamentos, filosofia pessoal, crenças e reflexões internas  

- **📂 <font color = 00bbfff>System</font>** — Sistema de organização e infraestrutura da base 
	- **ASSETS** — Templates, ícones, imagens, estilos e componentes visuais  
	- **MEDIA** — Repositório de arquivos multimídia utilizados nas notas  
	- **TEMPLATE** — Meus Templates  

---

# Modelos de Nomenclatura
### Atlas

- `draft-[tema]-[descricao]`  
	- Ex: `draft-matematica-conjuntos-iniciais`
- `index-[tema]-[tipo-mapa]`  
	- Ex: `index-python-mapa-conceitual`
- `concept-[tema]-[descricao-teorica]`  
	- Ex: `concept-estatistica-distribuicao-normal`
- `snip-[biblioteca]-[acao]-[descricao]`  
	- Ex: `snip-seaborn-plot-grafico-barras`
- `cmp-[dominio]-[acao]-[descricao]`  
	- Ex: `cmp-string-utils-remocao-acentos`
- `doc-[ferramenta]-[modulo/metodo]-[descricao]`  
	- Ex: `doc-pandas-merge-combinacao-tabelas`
- `flow-[tipo]-[descricao-curta]`  
	- Ex: `flow-datascience-limpeza-dados`
- `res-[tipo]-[origem]-[descricao]`  
	- Ex: `res-pdf-artigo-random-forest`
- `map-[tema]-[forma-representacao]`  
	- Ex: `map-ml-deep-learning-esquema-vis`

### Calendar

- `YYYY-MM-DD`  
	- Ex: `2025-05-11`
- `YYYY-[W]ww`  
	- Ex: `2025-W19`
- `YYYY-MM`  
	- Ex: `2025-05`
- `YYYY`  
	- Ex: `2025`

### Drafts
- `note-[tema]-[descricao-breve]`  
	- Ex: `note-ai-etica-uso-cotidiano`

### Efforts
- `project-[nome]-[data-inicio]-[data-fim]`  
	- Ex: `project-app-organizador-2025-01-01-2025-06-30`
- `area-[dominio]-[descricao]`  
	- Ex: `area-financas-controle-pessoal`
- `res-proj-[nome]-[tipo-material]`  
	- Ex: `res-proj-curso-dados-slides`
- `wrk-[contexto]-[acao/descricao]`  
	- Ex: `wrk-ecommerce-processo-envio`
- `archive-[nome-projeto]-[ano]`  
	- Ex: `archive-reestrutura-site-2024`

### Entertainment

- `ent-music-[artista]-[descricao]`  
	- Ex: `ent-music-ludovico-einaudi-playlist-calma`
### Social
- `soc-people-[nome]-[contexto]`  
	- Ex: `soc-people-carlos-rede-linkedin`
- `soc-thinking-[tema]-[reflexao]`  
	- Ex: `soc-thinking-autenticidade-criativa`

### System
- `asset-[tipo]-[descricao]`  
	- Ex: `asset-icone-folder-gaming`
- `media-[tipo]-[descricao]`  
	- Ex: `media-video-tutorial-git`
- `template-[tipo]-[uso]`  
	- Ex: `template-projeto-pesquisa-cientifica`


# Principais Propriedades das Notas `tag` e `Hubs`


### TAG
- ! Classificar TIPO ou OBJETIVO da nota, se está INCOMPLETA e gestão de TAREFAS
```
`learning` - notas de estudo
`snipet` - 
`workflow` - 
...
`resources`- ferramentas ou listas de materiais externos para execução de tafefas.
`tocomplete` - notas incompletas1
`reading` - notas sobre livros
`lab` - planejamento e relatórios e projetos e ideias
`calendar` - notas de planejamento pelo calendário e notas diárias
`walkthrough` - MOCS de passo a passo.
`dataview` - notas de dataview
`dashboard` 

```

### HUB
- ! Classificar diferentes CONTEÚDOS e TEMAS abordados na nota.
```
- hub-pkm
- hub-tec
- hub-git
- hub-sql
- hub-python
- hub-tratamento-de-dados
- hub-descriptive-analysis
- hub-data-visualization
- hub-hypothesis-testing
- hub-ml-models
- hub-math
- hub-statistic
- hub-logic
- hub-probabilidade
- hub-BI
- hub-mkt
- hub-copy
- hub-growth
- hub-my-writing
- hub-filosofia
- ...
```

# Community Plugins

- [Background Image](https://github.com/shmolf/obsidian-editor-background)
- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin)
- [Callout Manager](https://github.com/eth-p/obsidian-callout-manager)
- [Checklist](https://github.com/delashum/obsidian-checklist-plugin)
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview)
- [Force note view mode](https://github.com/bwydoogh/obsidian-force-view-mode-of-note)
- [Homepage](https://github.com/mirnovov/obsidian-homepage)
- [Hotkeys for specific files](https://github.com/Vinzent03/obsidian-hotkeys-for-specific-files)
- [Kanban](https://github.com/mgmeyers/obsidian-kanban)
- [List Callouts](https://github.com/mgmeyers/obsidian-list-callouts)
- [Meta Bind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin)
- [Minimal Theme Settings](https://github.com/obsidian-community/obsidian-minimal-theme-settings)
- [Omnisearch](https://github.com/scambier/obsidian-omnisearch)
- [Outliner](https://github.com/vslinko/obsidian-outliner)
- [Paste URL into selection](https://github.com/denolehov/obsidian-url-into-selection)
- Pomodoro Timer
- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes)
- [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph)
- [Projects](https://github.com/marcusolsson/obsidian-projects)
- [QuickAdd](https://github.com/chhoumann/quickadd)
- [Recent Files](http://github.com/tgrosinger/recent-files-obsidian)
- [Share Note](https://github.com/alangrainger/share-note)
- Shell commands
- [Tabs](https://github.com/xhuajin/obsidian-tabs)
- [Templater](https://github.com/SilentVoid13/Templater)
- Vimrc Support
- [YTranscript](https://github.com/obsidian-community/obsidian-ytranscript)




# Inspirações e Recursos

- https://github.com/DuskWasHere/dusk-obsidian-vault
- https://fortelabs.com/blog/para/
- https://github.com/NonakaVal/Obsidian-CSS-Snippets
- [Dashboard ++](https://github.com/TfTHacker/DashboardPlusPlus)
- [Multi-Column Markdown](https://github.com/ckRobinson/multi-column-markdown)
- [Modular CSS Layout for Obsidian](https://github.com/efemkay/obsidian-modular-css-layout)



# Códigos 

### [Repo - MarkdownObsidianScripts](https://github.com/NonakaVal/MarkdownObsidianScripts) - Diversos códigos Python que uso

- [GetVoutInfo](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/GetVoutInfo.ipynb) - `.ipynb` Jupyter notebook para obter informações
- [EditNotes](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/EditNotes.ipynb) - `.ipynb` Editor de notas em massa
- [GetAllnotesList](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/GetAllnotesList.ipynb) - `.ipynb` Cria o arquivo [_index_notas.md](https://github.com/NonakaVal/MyObsidianStructure/blob/main/_index_notas.md)
- [Zettelizer](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/Zettelizer.ipynb) - `.ipynb` Automaticamente atomiza notas com base no header
- [ipynbToMarkdownFile](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/ipynbToMarkdownFile.ipynb) - `.ipynb` para converter notebooks em notas `.md`
- [LLM-Explore-TESTS](https://github.com/NonakaVal/MarkdownObsidianScripts/blob/main/LLM-Explore-TESTS.ipynb) - `.ipynb` Testes com LLMs