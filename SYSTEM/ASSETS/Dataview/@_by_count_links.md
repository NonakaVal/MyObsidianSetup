---
created: "[[2025-06-10]]"
cssclasses:
  - wide-page
---

````tabs

tab: ATLAS

```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "ATLAS"
WHERE !contains(tags, "#calendar/daily" ) AND (length(file.outlinks) >= 1 OR length(file.inlinks) >= 1)
SORT length(file.inlinks) desc


LIMIT 30
```

tab: Efforts
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "EFFORTS"
WHERE !contains(tags, "#calendar/daily" ) AND (length(file.outlinks) >= 1 OR length(file.inlinks) >= 1)
SORT length(file.inlinks) desc


LIMIT 30
```
tab: Calendar
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "CALENDAR"
WHERE (length(file.outlinks) >= 1 OR length(file.inlinks) >= 1)
SORT length(file.inlinks) desc


LIMIT 30
```

````
