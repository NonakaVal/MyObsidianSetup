---
tags:
  - resources
  - dataview
HUB:
  - "[[hub-pkm]]"
cssclasses:
  - wide-page
---
## [[@_dataview_Calendar-tasks]]

# Calendar
````tabs
tab: Calendar Tasks
```dataview
TASK
FROM "CALENDAR" AND -#inlog AND -#lost-codes 
WHERE !completed AND !checked and type != "area_utils"
```

tab: Calendar Overview

```dataviewjs
const pages = dv.pages('"CALENDAR"')
  .where(p => !(p.tags?.includes("#inlog") || p.tags?.includes("#lost-codes")));

let totalTasks = 0;
const tableData = [];

for (let page of pages) {
  const tasks = page.file.tasks || [];
  const filteredTasks = tasks.filter(t => !t.completed && !t.checked && t.type !== "area_utils");

  if (filteredTasks.length === 0) continue;

  totalTasks += filteredTasks.length;

  tableData.push({
    file: page.file.link,
    total: filteredTasks.length,
    tasks: filteredTasks.map(t => t.text).join(", "),
    mtime: page.file.mtime
  });
}

tableData.sort((a, b) => b.mtime - a.mtime);

dv.table(
  ["Arquivo", "Tarefas Pendentes", "Total de Tarefas"],
  tableData.map(row => [row.file, row.tasks, row.total])
);

dv.paragraph(`**Total Geral de Tarefas Pendentes:** ${totalTasks}`);
```

---


tab: Done Tasks List

```dataview
TASK
FROM "CALENDAR"
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name
```
````

