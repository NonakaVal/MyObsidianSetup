---
created: "[[2025-05-31]]"
type: area_family
area: "[[ESTUDOS]]"
area_category: Learning
tags: area/ESTUDOS
---


# [[ESTUDOS]]




### on going

```dataview
table created AS "Created", summary AS "Summary"
from "EFFORTS/09_AREAS/ESTUDOS"
where file.name != "ESTUDOS" and type = "project-base"
sort created DESC
```


### Tasks

````tabs
tab: TASKs

```dataview
TASK
FROM "EFFORTS/09_AREAS/ESTUDOS"
WHERE !completed AND !checked
GROUP BY file.name

```

tab: Done
```dataview
TASK
FROM "EFFORTS/09_AREAS/ESTUDOS"
WHERE completed AND checked
GROUP BY file.name

```

tab: Arquivados


````











Last modified : `$= dv.current().file.mtime`

