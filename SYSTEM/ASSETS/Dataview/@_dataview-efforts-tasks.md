---
created: "[[2025-06-10]]"
cssclasses: []
tags:
  - dataview
---
# Efforts
````tabs
tab: Areas Tasks

```dataview
TASK
FROM "20 Focus Areas" 
WHERE !completed AND !checked and type != "area_utils" and kanban-plugin != "board"
GROUP BY file.name 
SORT file.name DESC
```
tab: Project Tasks

```dataview
TASK
FROM "50 Projects & Outputs" 
WHERE !completed AND !checked and type != "area_utils" and kanban-plugin != "board"
where type = "project"
where type != "project_note"
GROUP BY file.name 
SORT file.name DESC
```


tab: Done Tasks List

```dataview
TASK
FROM "20 Focus Areas" OR "50 Projects & Outputs"
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name
```

````




