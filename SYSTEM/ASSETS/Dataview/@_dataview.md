---
tags:
  - dataview
HUB:
  - "[[hub-pkm]]"
---
lab
```dataview
list
from "Knowledge" 
WHERE contains(file.name, "hub-")
Sort file.ctime desc

```



```datavie
list file.name
FROM "" 
GROUP BY hub
```
