---
created: "[[2025-05-20]]"
type: area_family
area: "[[Digital-Garden]]"
area_category: content-creation
tags:
  - area/Digital-Garden
summary: controle das minhas notas do digital garden
---

Area Category : `INPUT[inlineSelect(option('content-creation'), option('family'), option('work'), option('saude'), showcase):area_category]`


# [[Digital-Garden]]

https://nonaka-garden.vercel.app/


### on going

```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/PROJECTS/Digital-Garden"
where file.name != "Digital-Garden"
sort created DESC
```



### Tasks

````tabs
tab: TASKs

```dataview
TASK
FROM "Efforts/PROJECTS/Digital-Garden"
WHERE !completed AND !checked AND type != "area_utils"
GROUP BY file.name

```

tab: Done
```dataview
TASK
FROM "Efforts/PROJECTS/Digital-Garden"
WHERE completed AND checked AND type != "area_utils"
GROUP BY file.name

```

tab: Arquivados


````











Last modified : `$= dv.current().file.mtime`

