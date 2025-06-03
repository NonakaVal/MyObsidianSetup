---
area: "[[PKM-Youtube-Videos]]"
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
# [[PKM-Youtube-Videos|PKM-Youtube-Videos]]

# Overview


 [▶️  Abrir Carnac](file:///C:/Users/desktop/Documents/Release/Carnac.exe)


````tabs
tab: Notes
## [📁 Gravações](file:///D:/PKM-Yt-Videos)

```dataview
table created AS "Created", summary AS "Summary"
from "EFFORTS/09_AREAS/PKM-Youtube-Videos"
where file.name != "PKM-Youtube-Videos" AND type = "project-base"
sort created DESC
```

tab: Arquivados
```dataview
table created AS "Created"
from "EFFORTS/11_ARCHIVES/PKM-Youtube-Videos" 
```
````

# Tasks

#todo-schedule 
- [x] [[importancia-nota-diaria|Importancia nota diária]]
- [ ] [Explorar Exemplos de Vaults](https://discord.com/channels/686053708261228577/1279147107298705493)
- [ ] [[serie-plugins-da-comunidade]]

### Done
```dataview
TASK
FROM "EFFORTS/09_AREAS/PKM-Youtube-Videos"
WHERE completed AND checked
GROUP BY file.name


```




