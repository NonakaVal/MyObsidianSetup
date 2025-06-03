---
area: PKM-Youtube-Videos
area_category: content-creation
summary: 
tags:
  - area/pkm-youtube-videos
type: area_family
created: 2024-12-29 00:24
HUB:
  - "[[hub-pkm]]"
---
# [[EFFORTS/11_ARCHIVES/PKM-Youtube-Videos/PKM-Youtube-Videos-archived]] 

# Overview


````tabs
tab: Notes
```dataview
table created AS "Created", summary AS "Summary"
from "Efforts/AREAS/pkm-videos"
where file.name != "2025-pkm-videos"
sort created DESC
```

tab: ARCHIVES
```dataview
list from #area/pkm-youtube-videos AND "Efforts/ARCHIVES"
sort type ASC
```
````

# Tasks

- [x] Vídeo supernotes


### on going


```dataview
TASK
FROM "Efforts/AREAS/PKM-Youtube-Videos"
WHERE !completed AND !checked
GROUP BY file.name

```

### Done
```dataview
TASK
FROM "Efforts/AREAS/PKM-Youtube-Videos"
WHERE completed AND checked
GROUP BY file.name


```


