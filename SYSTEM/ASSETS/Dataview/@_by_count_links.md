
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM ""
WHERE !contains(tag, "#calendar/daily" ) AND (length(file.outlinks) = 0 OR length(file.inlinks) = 0)
SORT length(file.inlinks) desc


LIMIT 1000
```
