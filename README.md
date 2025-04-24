  A \

# Estrutura da Vault

- 📂 <font color = 00bbfff>Atlas</font> - Notas de estudo e literárias
	- ATLAS
	- FLEETING
	- LITERATURE
	- MAPS
	- PERMANENT
	- RESOURCES
- 📂 <font color = 00bbfff>Calendar</font> - Calendários e notas Diárias ou periódicas
	- DAILY
	- MONTHLY
	- WEEKLY
	- YARLY
- 📂 <font color = 00bbfff>Drafts</font> - Rascunhos
- 📂 <font color = 00bbfff>Efforts</font>  - Direcionamento de esforços e projetos
	- ARCHIVES
	- AREAS
	- PROJECTS
	- RESOURCES
	- WORKSTATION
- 📂 <font color = 00bbfff>System</font> - Notas sobre o sistema e organização
	- ASSETS
	- MEDIA


# Propriedades das Notas
### TAG
- ! Classificar TIPO ou OBJETIVO da nota, se está INCOMPLETA e gestão de TAREFAS
```
`learning` - notas de estudo
`resources`- ferramentas ou listas de materiais externos para execução de tafefas.
`tocomplete` - notas incompletas
`reading` - notas sobre livros
`lab` - planejamento e relatórios e projetos e ideias
`calendar` - notas de planejamento pelo calendário e notas diárias
`walkthrough` - MOCS de passo a passo.
`dataview` - notas de dataview
`dashboard` 

`to-do` - tarefas
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


# Plugins não oficiais

- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin)
- [Checklist](https://github.com/delashum/obsidian-checklist-plugin)
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview)
- [Force note view mode](https://github.com/bwydoogh/obsidian-force-view-mode-of-note)
- [Homepage](https://github.com/mirnovov/obsidian-homepage)
- [Hotkeys for specific files](https://github.com/Vinzent03/obsidian-hotkeys-for-specific-files)
- [Kanban](https://github.com/mgmeyers/obsidian-kanban) 
- [List Callouts](https://github.com/mgmeyers/obsidian-list-callouts)
- [Meta Bind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin)
- [Omnisearch](https://github.com/scambier/obsidian-omnisearch)
- [Outliner](https://github.com/vslinko/obsidian-outliner)
- [Paste URL into selection](https://github.com/denolehov/obsidian-url-into-selection)
- [PDF++](https://github.com/RyotaUshio/obsidian-pdf-plus)
- [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes)
- [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph)
- [Projects](https://github.com/marcusolsson/obsidian-projects)
- [QuickAdd](https://github.com/chhoumann/quickadd)
- [Recent Files](http://github.com/tgrosinger/recent-files-obsidian)
- [Share Note](https://github.com/alangrainger/share-note)
- [Tabs](https://github.com/xhuajin/obsidian-tabs)
- [Templater](https://github.com/SilentVoid13/Templater)


### SNIPPETS
#### Dashboard ++
```CSS
/* Updated 2022-02-28 */

.dashboard {
    padding-left: 25px !important;
    padding-right: 25px !important;
    padding-top: 25px !important;
}

.dashboard .markdown-preview-section {
    max-width: 100%;
}

/* Title at top of the document */
.dashboard .markdown-preview-section .title {
    top: 40px;
    position: absolute;
    font-size: 24pt !important;
    font-weight: bolder;
    letter-spacing: 10px;
}

.dashboard h1 {
    border-bottom-style: dotted !important;
    border-width: 1px !important;
    padding-bottom: 3px !important;
}

.dashboard div > ul {
    list-style: none;
    display: flex;
    column-gap: 50px;
    flex-flow: row wrap;
}

.dashboard div > ul > li {
    min-width: 250px;
    width: 15%;
}
```

#### dashmargins

```css
/* 
Optional css that can be added to make dashboards use wide margin 
if "Readable line length" is enabled in Editor
 
Updated 2022-02-28
*/

.dashboard .markdown-preview-section {
    width: 100% !important;
    max-width: 100% !important;
 }
```


### Nomenclaturas
`_ ! @ % + =`

! - MOCs de maior nível ou  DASHBOARDS
@ - NOTAS DE CONTROLE E DATAVIEW
% - TEMPLATES
evitar uso de espaços e acentos,
##### Modelos de Nomenclatura


Notas de Estudo
   - `[topic]-[subtopic]-[description]`
     - Exemplo: `python-fundamentals-introduction`
   - `[tool]-[method]-[description]`
      - Exemplo : `pandas-loc-iloc-method-selection`

Notas Sobre Livros
   - `[book-title]-[autor]-[ano]`
     - Exemplo: `introducao-estatistica-12edicao-mario-f-triola-2017`
 - `[book-title]-[chapter/topic]-[description]-`

Planejamento e Relatórios de Projetos e Ideias
   - `[project-name]-[task/idea]-[description]-[inicio]-[fim]`

https://github.com/DuskWasHere/dusk-obsidian-vault
https://fortelabs.com/blog/para/