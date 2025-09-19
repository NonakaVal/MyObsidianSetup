---
area: "[[<% tp.file.folder() %>]]"
tags:
type: area_family
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
HUB:
  - "[[hub-work]]"
  - "[[hub-menagement]]"
---
# [[<%tp.file.folder() %>]] 



 `BUTTON[TEMPLATE-CRIAR-NOVA-AREA]`     

```meta-bind-button
label: Criar Nota da Area
icon: plus
hidden: true
class: ""
id: TEMPLATE-CRIAR-NOVA-AREA
style: primary
actions:
  - type: command
    command: quickadd:choice:6430f0b6-4d07-44f9-9b1a-45e79f6bee19
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
from "EFFORTS/09_AREAS/<% tp.file.folder() %>"
where type != "area"
where type = "area_note"
where type != "area_note_sub"
sort created DESC
```


<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder().toLowerCase().split(" ").join("_");
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `area/${task_tag_value}`; 
    }); 
}); -%>