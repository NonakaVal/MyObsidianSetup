---
tags:
  - dataview
HUB:
  - "[[hub-pkm]]"
---

by learning

```datavie
table tags, hub
from "" and  #learning and -tag and -#learning/book and tag
WHERE !contains(file.name, "%")
Sort file.ctime desc

```

```datavie
table tagstable tags, hub
from "" and  tag
WHERE !contains(file.name, "%")
Sort file.ctime desc

```

```datavie
table tags,hub
from "" and #learning/book
WHERE !contains(file.name, "%")
Sort file.ctime desc

```

```datavie
table tags,hub
from "" and tag
WHERE !contains(file.name, "%")
Sort file.ctime desc

```

