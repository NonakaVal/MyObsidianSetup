---
created: '[[2025-05-03]]'
type: area_family
area: FORMAT
area_category: 
tags: 
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
---

# Set first
 
Area Category : `INPUT[inlineSelect(option('content-creation'), option('family'), option('work'), option('saude'), showcase):area_category]`

# Overview

````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/AREAS/FORMAT"
where file.name != "FORMAT"
sort created DESC
```

tab: Arquivados
```dataview
list from #area/FORMAT AND "Efforts/ARCHIVES"
sort type ASC

```
````

# Tasks

### on going
```dataview
TASK
FROM "Efforts/AREAS/FORMAT"
WHERE !completed AND !checked
GROUP BY file.name


```

### Done
```dataview
TASK
FROM "Efforts/AREAS/FORMAT"
WHERE completed AND checked
GROUP BY file.name


```






