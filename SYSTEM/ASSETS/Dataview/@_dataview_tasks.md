---
tags:
  - resources
HUB:
  - "[[hub-pkm]]"
---

# Contar tasks concluídas
```dataview
TABLE WITHOUT ID
	key as Tasks,
	length(rows) AS Total,
	length(filter(rows.tasks, (r) => r.completed)) AS Completed
FROM "Efforts" AND !"Efforts/ARCHIVES" 
WHERE type != "area_utils" 
FLATTEN file.tasks as tasks
GROUP BY file.link
SORT length(rows) DESC
```


# [[template_daily_note]] task queries

---

````tabs
tab: Areas Tasks
```dataview
TASK
FROM "Efforts/AREAS" 
WHERE !completed AND !checked and type != "area_utils"
GROUP BY file.name
SORT file.mtime DESC

```

tab: Calendar Tasks
```dataview
TASK
FROM "Calendar" AND -#inlog AND -#lost-codes 
WHERE !completed AND !checked and type != "area_utils"

```

tab: Done Efforts
```dataview
TASK
FROM "Efforts" 
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name

```
````






[[2024-10-31]]
