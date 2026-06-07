---
{}
---
```dataview
TABLE WITHOUT ID
file.link AS "Nota",

choice(
(date(now) - file.mtime).days >= 1,
floor((date(now) - file.mtime).days) + " dias",
choice(
(date(now) - file.mtime).hours >= 1,
floor((date(now) - file.mtime).hours) + " h",
choice(
(date(now) - file.mtime).minutes >= 1,
floor((date(now) - file.mtime).minutes) + " min",
"agora"
)
)
) AS "Modificado há"

FROM ""
SORT file.mtime DESC
LIMIT 9

```
