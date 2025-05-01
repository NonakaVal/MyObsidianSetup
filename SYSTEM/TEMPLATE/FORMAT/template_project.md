---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
type: project
project: <% tp.file.folder()%>
goal: ""
Due_Date: 
Status: 
cssclasses:
  - hide-properties_editing
---

# Set first


Goal - `INPUT[text(showcase):goal]` - Started : [[<% tp.date.now("YYYY-MM-DD") %>]] - to End `INPUT[datePicker(showcase):Due_Date]` 

Area Notes Related : `INPUT[inlineListSuggester(optionQuery(#area)):connections]` 


# Overview

Status : `INPUT[inlineSelect(option('À começar'), option('Em Andamento'), option('Em Espera'), option('Finalizado'), showcase):Status]`

````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/PROJECTS/<% tp.file.folder() %>"
where file.name != "<% tp.file.folder() %>"
sort created DESC
```

tab: Arquivados
```dataview
list from #project/<% tp.file.folder() %> AND "Efforts/ARCHIVES"
sort type ASC

```
````

## Tasks

### on going
```dataview
TASK
FROM "Efforts/AREAS/<%tp.file.folder() %>"
WHERE !completed AND !checked
GROUP BY file.name


```

### Done
```dataview
TASK
FROM "Efforts/PROJECTS/<%tp.file.folder() %>"
WHERE completed AND checked
GROUP BY file.name


```


<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder();
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `project/${task_tag_value}`; 
    }); 
}); -%>




