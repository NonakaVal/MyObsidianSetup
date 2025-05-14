---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
type: area_family
area: <% tp.file.folder()%>
area_category: 
tags: 
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
---

Last modified : `$= dv.current().file.mtime`

# Set first
 
Area Category : `INPUT[inlineSelect(option('content-creation'), option('family'), option('work'), option('saude'), showcase):area_category]`

# Overview

````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/AREAS/<% tp.file.folder() %>"
where file.name != "<% tp.file.folder() %>"
sort created DESC
```

tab: Arquivados
```dataview
list from #area/<% tp.file.folder() %> AND "Efforts/ARCHIVES"
sort type ASC

```
````



# Tasks

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
FROM "Efforts/AREAS/<%tp.file.folder() %>"
WHERE completed AND checked
GROUP BY file.name


```


<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder();
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `area/${task_tag_value}`; 
    }); 
}); -%>




last_modified: `=link(dateformat(date(today), "yyyy-MM-dd"))`

