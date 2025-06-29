````tabs
tab: TO DO

```dataview
TASK
FROM "SYSTEM/TEMPLATE/SNIPPET"
WHERE !completed AND !checked
GROUP BY file.name

```

tab: DONE
```dataview
TASK
FROM "SYSTEM/TEMPLATE/SNIPPET"
WHERE completed AND checked
GROUP BY file.name

```


````
