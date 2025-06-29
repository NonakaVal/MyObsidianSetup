
````tabs
tab: TO DO

```dataview
TASK
FROM "SYSTEM/TEMPLATE/SNIPPET"
WHERE !completed AND !checked
  AND type != "area_utils"
  AND contains(area, [[EFFORTS/09_AREAS/%-TRACKER-OVERVIEW]])
GROUP BY file.name
SORT file.mtime DESC

```


tab: DONE

```dataview
TASK
FROM "SYSTEM/TEMPLATE/SNIPPET"
WHERE completed AND checked
  AND type != "area_utils"
  AND contains(area, [[EFFORTS/09_AREAS/%-TRACKER-OVERVIEW]])
GROUP BY file.name
SORT file.mtime DESC

```

````

