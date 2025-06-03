---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
type: area_family
area: '[[<% tp.file.folder()%>]]'
area_category: 
tags: 
---

Area Category : `INPUT[inlineSelect(option('content-creation'), option('family'), option('work'), option('saude'), option('Learning'), showcase):area_category]`


# [[<% tp.file.title %>]]




### on going

```dataview
table created AS "Created", summary AS "Summary"
from "EFFORTS/09_AREAS/<% tp.file.folder() %>"
where file.name != "<% tp.file.folder() %>" and type = "project-base"
sort created DESC
```


### Tasks

````tabs
tab: TASKs

```dataview
TASK
FROM "EFFORTS/09_AREAS/<%tp.file.folder() %>"
WHERE !completed AND !checked
GROUP BY file.name

```

tab: Done
```dataview
TASK
FROM "EFFORTS/09_AREAS/<%tp.file.folder() %>"
WHERE completed AND checked
GROUP BY file.name

```

tab: Arquivados


````







<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder();
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `area/${task_tag_value}`; 
    }); 
}); -%>




Last modified : `$= dv.current().file.mtime`

