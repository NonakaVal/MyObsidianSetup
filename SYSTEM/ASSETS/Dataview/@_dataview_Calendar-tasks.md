---
tags:
  - resources
  - dataview
subject:
  - "[[hub-pkm]]"
cssclasses: []
---

````tabs
tab: 40 Calendar & Review Tasks
```dataview
TASK
FROM "40 Calendar & Review" AND -#inlog AND -#lost-codes AND !"40 40 Calendar & Review & Review/43 YEARLY" AND !"40 40 Calendar & Review & Review/42 MONTHLY"
WHERE !completed AND !checked and type != "area_utils"
SORT file.mtime DESC
```

tab: Metas e Objetivos



```dataview
TASK
FROM "40 Calendar & Review" AND -#inlog AND -#lost-codes AND !"40 40 Calendar & Review & Review/41 DAILY"
WHERE !completed AND !checked and type != "area_utils"
GROUP BY file.name
SORT file.mtime DESC
```



tab: Done Tasks List

```dataview
TASK
FROM "40 Calendar & Review"
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name
SORT file.mtime ASC

```

tab: 40 Calendar & Review Overview

```dataviewjs
const pages = dv.pages('"40 Calendar & Review"')
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

````

