
````tabs
tab: TO DO

```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE !completed AND !checked
  AND type != "area_utils"
  AND contains(area, [[EFFORTS/09_AREAS/<% tp.file.title%>]])
GROUP BY file.name
SORT file.mtime DESC

```


tab: DONE

```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE completed AND checked
  AND type != "area_utils"
  AND contains(area, [[EFFORTS/09_AREAS/<% tp.file.title%>]])
GROUP BY file.name
SORT file.mtime DESC

```

````

