---
tags:
  - calendar/month
---



# Monthly Goals


# Summary of the Month

```dataview
TABLE WITHOUT ID
	key as Tasks,
	length(rows) AS Total,
	length(filter(rows.tasks, (r) => r.completed)) AS Completed
FROM "Efforts" AND !"EFFORTS/11_ARCHIVES"
FLATTEN file.tasks as tasks
GROUP BY file.link

SORT length(rows) DESC
```


# Reflections & Learnings


# Plan for Next Month

