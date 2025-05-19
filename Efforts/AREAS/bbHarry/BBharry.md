---
area: bbHarry
area_category: family
tags:
  - area/bbharry
created: "[[2025-04-27]]"
type: area_family
---
# [[Efforts/AREAS/bbHarry/BBharry|BBharry]]



### on going
```dataview
TASK
FROM "Efforts/AREAS/bbHarry"
WHERE !completed AND !checked
GROUP BY file.name


```



# Overview


````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/AREAS/bbHarry"
where file.name != "BBharry" AND type != "area_utils"
sort created DESC
```

tab: Arquivados
```dataview
table created as created
from "Efforts/ARCHIVES/HarryLearning" 
sort created DESC

```
````


### Done
```dataview
TASK
FROM "Efforts/AREAS/bbHarry" AND "Efforts/AREAS/bbHarry"
WHERE completed AND checked
GROUP BY file.name


```




