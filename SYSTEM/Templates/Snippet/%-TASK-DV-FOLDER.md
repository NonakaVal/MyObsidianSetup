````tabs
tab: TO DO

```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE !completed AND !checked
GROUP BY file.name

```

tab: DONE
```dataview
TASK
FROM "<% tp.file.folder(true) %>"
WHERE completed AND checked
GROUP BY file.name

```


````
