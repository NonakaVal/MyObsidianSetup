
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Atlas"
WHERE !contains(tag, "#calendar/daily" ) AND (length(file.outlinks) >= 1 OR length(file.inlinks) >= 1)
SORT length(file.inlinks) desc


LIMIT 100
```
