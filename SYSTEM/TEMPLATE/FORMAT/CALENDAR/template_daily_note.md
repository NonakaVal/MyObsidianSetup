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



[📁 Documents](file:///C:/Users/desktop/Documents) 





---


## on Going and tasks

````tabs
tab: Area Family
```dataview
table area_category as "Area Category", created as "Date Created" from "EFFORTS/09_AREAS"
WHERE type = "area_family"
SORT file.mtime DESC
```

tab: Writing Notes
![[Writing]]

tab: Estudos 
![[ESTUDOS]]

tab: Career 
![[Career-development]]


tab: Pkm Youtube Videos
![[EFFORTS/09_AREAS/PKM-Youtube-Videos/PKM-Youtube-Videos|PKM-Youtube-Videos]]





````

````tabs
tab: Areas Tasks
```dataview
TASK
FROM "EFFORTS/09_AREAS" 
WHERE !completed AND !checked and type != "area_utils" 
GROUP BY file.name 
SORT file.mtime DESC

```

tab: Calendar Tasks
```dataview
TASK
FROM "CALENDAR" AND -#inlog AND -#lost-codes 
WHERE !completed AND !checked and type != "area_utils"

```

tab: Done Efforts
```dataview
TASK
FROM "EFFORTS" 
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name

```
````






---

# How Was My Day ?


