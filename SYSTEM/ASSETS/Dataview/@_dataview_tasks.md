---
tags:
  - resources
HUB:
  - "[[hub-pkm]]"
---
```dataview
task
from "DailyNotes"
WHERE !completed AND !checked
GROUP BY file.name
```
[[2024-10-31]]