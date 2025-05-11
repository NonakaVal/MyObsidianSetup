---
tags:
  - calendar/daily
created: <% tp.file.creation_date()%>
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
---

<% tp.web.daily_quote() %>

# How am'I feeling Today ?

# Tasks 

```dataview
TASK
FROM "Efforts"
WHERE !completed AND !checked
GROUP BY file.name

```


# Log



# now doing

```dataview
table area_category as "Area Category", created as "Date Created" from "Efforts/AREAS"
WHERE type = "area_family"
```

```dataview
table created AS "Created", summary AS "goal"
from "Efforts/PROJECTS"
where file.name != "collectors-tutorials"
sort created DESC
```



## Areas Tasks
```dataview
TASK
FROM "Efforts/AREAS"
WHERE !completed AND !checked
GROUP BY file.name

```

---

# How Was My Day ?


