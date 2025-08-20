---
project: "[[<% tp.file.folder() %>]]"
summary:
tags:
type: project_note
"created:": '[[<% tp.date.now("YYYY-MM-DD") %>]]'
cssclasses:
  - hide-properties_reading
  - hide-properties_editing
---
# [[<%tp.file.folder() %>]] 


---

# Definir Resumo 
`INPUT[textArea(showcase, class(meta-bind-full-width), class(meta-bind-high)):resumo]`



# TAREFAS E PROCESSOS

---
 `BUTTON[tasks-button]`     

```meta-bind-button
label: Adicionar ou Editar Tarefa 
hidden: true
icon: plus
class: ""
id: tasks-button
style: destructive
actions:
  - type: open
    link: obsidian://adv-uri?vault=ALEX-OBSIDIAN-PROTOTYPE&commandid=obsidian-tasks-plugin%3Aedit-task

```









<%* tp.hooks.on_all_templates_executed(async () => { const file = tp.file.find_tfile(tp.file.path(true)); const value1 = tp.file.folder().split(" ").map(word => word.toLowerCase()).join("_"); const value2 = tp.file.title.split(" ").map(word => word.toLowerCase()).join("_"); await app.fileManager.processFrontMatter(file, (frontmatter) => { frontmatter["tags"] = `project/${value1}/${value2}`; }); }); -%>