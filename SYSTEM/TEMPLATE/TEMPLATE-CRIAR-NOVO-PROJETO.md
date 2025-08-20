---
project: "[[<% tp.file.folder() %>]]"
tags: 
type: project
"created:": '[[<% tp.date.now("YYYY-MM-DD") %>]]'
cssclasses:
  - hide-properties_reading
  - hide-properties_editing
---
# [[<%tp.file.folder() %>]] 

|Data Início|Data Entrega|Status|
| --- | --- |---|
| `INPUT[datePicker(showcase, defaultValue(null)):inicio]`| `INPUT[datePicker(showcase, defaultValue(null)):entrega]` |`INPUT[inlineSelect(option('Em andamento'), option('Finalizada'), option('Arquivado'), option('Aguardando')):status]` |

---

 `BUTTON[TEMPLATE-CRIAR-NOVA-NOTA-PROJETO]`

```meta-bind-button
label: Criar Nota de Projeto
icon: plus
hidden: true
class: ""
id: TEMPLATE-CRIAR-NOVA-NOTA-PROJETO
style: default
actions:
  - type: command
    command: quickadd:choice:e7c0cfff-583f-4da9-a201-79b4d5a12de4
```



# Tarefas 
````tabs
tab: Em Aberto

```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE !completed AND !checked
GROUP BY file.name

```

tab: Concluídas 
```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE completed AND checked
GROUP BY file.name

```


````

#  Notas

```dataview
table created AS "Created", summary AS "Resumo"
from "EFFORTS/PROJECTS/<% tp.file.folder() %>"
where type != "project"
where type = "project_note"
sort created DESC
```


<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder().toLowerCase().split(" ").join("_");
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `project/${task_tag_value}`; 
    }); 
}); -%>