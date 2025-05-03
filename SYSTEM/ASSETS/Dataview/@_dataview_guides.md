---
tags:
  - resources
HUB:
  - "[[hub-pkm]]"
---

2024-01-12  17:13

**List** Creates a list of all the notes you specifie

```
dataview
list
```
**From**
Determines from where you get the notes
```
dataview
listDA
from
```
**From TAG**
```
dataview
list
from # tag (sem espaço)
```
**From FOLDER**
```
dataview
list
from "foldername"
```
**From LINKS**
Add all the notes from links coming into a note
```
dataview
list
from [[]]
```
Or going out a note
```
dataview
list
from outgoing[[]]
```

**Combining sources**
You can use the 3 basic logical operators to create more complex `from` queries
- *and*
```
dataview
list
from # tag and # btag
```
- *or*
```
dataview
list
from # tag or # btag
```
- *-*
```
dataview
list
from -# tag
```
- *and -*
```
dataview
list
from [[]] and - [[]]
```

**String Concatenation**
In the result of a *list* you can add strings
```
dataview
list "File.path: " + File.path + " :)"
from # tag
```
**List of lists**
```
dataview
list authors
from [[]]
```
**Tasks**
`Task` searches for all checkboxes `- []` in your vault
It returns a list with all tasks, grouped by their parent note.
```
dataview
task from # tag
```

**Where**

After choosing from which notes to use, you can use `where` to narrow down the list further
This lets you use the various comparisons operators on the metadata from your notes
`>, >=, =, <, <=, !=`
> where{condition}
```
dataview
list
where file.name != "; 000 Home"
```
```
dataview
list
where file.mtime >= date(today) - dur(1 day)
```
```
dataview
list from
where !complete
```
```
dataview
list from
where !date updated
```

**Tables**
`Table` can show you a table of various metadata fields linked into each note.
`table {field1} {field2}`
```
dataview
table file.name
from [[]]
```
```
dataview
table autores
from [[]]
```
```
dataview
table dificuldade
from [[]]
```
**Sort**
Sort the order of the results from your list.
`Sort field1 asc/desc field2 asc/desc`
```
dataview
table file.name
from [[]]
sort asc
```

**Flatten**
Use `Flatten` to "unroll" each result in their on roll at the table.
```
dataview
table authors
from [[]]
flatten authors
```
**Group by**
`Group by` makes you gather together resoults based on the value of the field.
- Group tasks based on `completed`
- Group books by `rating`
#### Neat Examples
**Snipet showcase**
https://forum.obsidian.md/t/dataview-plugin-snippet-showcase/13673/38