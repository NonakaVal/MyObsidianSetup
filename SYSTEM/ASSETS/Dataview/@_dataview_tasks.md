---
tags:
  - resources
HUB:
  - "[[hub-pkm]]"
---

```dataview
TABLE WITHOUT ID
	key as Tasks,
	length(rows) AS Total,
	length(filter(rows.tasks, (r) => r.completed)) AS Completed,
	summary AS Resumo
FROM "Efforts" AND !"Efforts/ARCHIVES"
FLATTEN file.tasks as tasks
GROUP BY file.link
SORT length(rows) DESC
```



[[2024-10-31]]