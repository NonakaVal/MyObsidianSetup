---
area: "[[<% tp.file.folder() %>]]"
tags:
type: area_family
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---

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
<%tp.file.cursor()%>



<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder().toLowerCase().split(" ").join("_");
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `area/${task_tag_value}`; 
    }); 
}); -%>