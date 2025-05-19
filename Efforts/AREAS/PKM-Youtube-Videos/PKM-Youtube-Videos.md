---
area: "[[Efforts/AREAS/PKM-Youtube-Videos/PKM-Youtube-Videos]]"
summary: videos de pkm e obsidian
tags:
  - area/PKM-Youtube-Videos
created: "[[2025-04-27]]"
type: area_family
area_category: content-creation
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
---
area/PKM-Youtube-Videos# [[Efforts/AREAS/PKM-Youtube-Videos/PKM-Youtube-Videos]] 

# Overview


````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/AREAS/PKM-Youtube-Videos"
where file.name != "PKM-Youtube-Videos" AND type = "project-base"
sort created DESC
```

tab: Arquivados
```dataview
table created AS "Created"
from "Efforts/ARCHIVES/PKM-Youtube-Videos" 
```
````

# Tasks

#todo-schedule 
- [ ] [[importancia-nota-diaria|Importancia nota diária]]
- [ ] [Explorar Exemplos de Vaults](https://johnnydecimal.com/)
- [ ] [[serie-plugins-da-comunidade]]

### Done
```dataview
TASK
FROM "Efforts/AREAS/PKM-Youtube-Videos"
WHERE completed AND checked
GROUP BY file.name


```




