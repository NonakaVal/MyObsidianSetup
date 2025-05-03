---
created: '[[2025-05-03]]'
type: project
project: SNIPTETS
goal: ""
Due_Date: 
Status: 
cssclasses:
  - hide-properties_editing
---

# Set first


Goal - `INPUT[text(showcase):goal]` - Started : [[2025-05-03]] - to End `INPUT[datePicker(showcase):Due_Date]` 

Area Notes Related : `INPUT[inlineListSuggester(optionQuery(#area)):connections]` 


# Overview

Status : `INPUT[inlineSelect(option('À começar'), option('Em Andamento'), option('Em Espera'), option('Finalizado'), showcase):Status]`

````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/PROJECTS/SNIPTETS"
where file.name != "SNIPTETS"
sort created DESC
```

tab: Arquivados
```dataview
list from #project/SNIPTETS AND "Efforts/ARCHIVES"
sort type ASC

```
````

## Tasks

### on going
```dataview
TASK
FROM "Efforts/AREAS/SNIPTETS"
WHERE !completed AND !checked
GROUP BY file.name


```

### Done
```dataview
TASK
FROM "Efforts/PROJECTS/SNIPTETS"
WHERE completed AND checked
GROUP BY file.name


```






