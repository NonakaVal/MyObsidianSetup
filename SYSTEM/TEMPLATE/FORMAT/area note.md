---
area:
  - "[[<% tp.file.folder() %>]]"
summary:
tags:
type: area_note
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
cssclasses:
  - hide-properties_reading
HUB:
  - "[[hub-work]]"
  - "[[hub-menagement]]"
---

~ [[<%tp.file.folder() %>]] 

---
# Definir Resumo 
`INPUT[textArea(showcase, class(meta-bind-full-width), class(meta-bind-high)):summary]`


# TAREFAS E PROCESSOS

---








<%* tp.hooks.on_all_templates_executed(async () => { const file = tp.file.find_tfile(tp.file.path(true)); const value1 = tp.file.folder().split(" ").map(word => word.toLowerCase()).join("_"); const value2 = tp.file.title.split(" ").map(word => word.toLowerCase()).join("_"); await app.fileManager.processFrontMatter(file, (frontmatter) => { frontmatter["tags"] = `area/${value1}/${value2}`; }); }); -%>