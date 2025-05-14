---
created: <% tp.file.creation_date() %>
tags:
  - calendar/daily
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
---

<% tp.web.daily_quote() %>

Last modified : `$= dv.current().file.mtime`
# How am'I feeling Today ?

Mood : `INPUT[inlineSelect(option('🙂 – Neutral'), option('😄 – Happy'), option('😐 – Meh'), option('😞 – Sad'), option('😠 – Frustrated'), showcase):daily-mood]`



---

# Log



---

## Efforts

````tabs
tab: Tasks
```dataview
TASK
FROM "Efforts" 
WHERE !completed AND !checked
GROUP BY file.name

```
Calendar Tasks
```dataview
TASK
FROM "Calendar" AND -#inlog AND -#lost-codes 
WHERE !completed AND !checked

```
tab: Areas and Projets
```dataview
table area_category as "Area Category", created as "Date Created" from "Efforts/AREAS"
WHERE type = "area_family"
SORT file.mtime DESC
```
```dataview
table created as "Date Created" from "Efforts"
WHERE type = "project-base"
SORT file.mtime DESC
```



````

---

# How Was My Day ?


