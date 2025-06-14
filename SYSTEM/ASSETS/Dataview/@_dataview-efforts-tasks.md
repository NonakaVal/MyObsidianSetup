---
created: "[[2025-06-10]]"
cssclasses:
  - dashboard
tags:
  - dataview
---
# [[@_dataview-efforts-tasks]]

# Efforts
````tabs
tab: Areas Tasks
```dataview
TASK
FROM "EFFORTS/09_AREAS" 
WHERE !completed AND !checked and type != "area_utils" 
GROUP BY file.name 
SORT file.mtime DESC
```


tab: Efforts Overview

```dataviewjs
const pages = dv.pages('"EFFORTS"')
  .where(p => !p.file.path.startsWith("EFFORTS/11_ARCHIVES"));

let totalTasks = 0;
let totalCompleted = 0;
const tableData = [];

for (let page of pages) {
  const tasks = page.file.tasks || [];
  if (tasks.length === 0) continue;

  const completedTasks = tasks.filter(t => t.completed && t.checked && t.type !== "area_utils");

  totalTasks += tasks.length;
  totalCompleted += completedTasks.length;

  tableData.push({
    file: page.file.link,
    total: tasks.length,
    completed: completedTasks.length
  });
}

dv.table(
  ["Arquivo", "Total de Tasks", "Concluídas"],
  tableData.map(row => [row.file, row.total, row.completed])
);

dv.paragraph(`**Total Geral de Tasks:** ${totalTasks}`);
dv.paragraph(`**Total Geral Concluídas:** ${totalCompleted}`);
```

---

tab: Efforts Detalhado

## Pendentes

```dataviewjs
const pages = dv.pages('"EFFORTS"')
  .where(p => !(p.tags?.includes("#inlog") || p.tags?.includes("#lost-codes")))
  .where(p => !p.file.path.startsWith("EFFORTS/11_ARCHIVES"));

let totalTasksPending = 0;
const tableDataPending = [];

for (let page of pages) {
  const tasks = page.file.tasks || [];
  const filteredTasks = tasks.filter(t => !t.completed && !t.checked && t.type !== "area_utils");

  if (filteredTasks.length === 0) continue;

  totalTasksPending += filteredTasks.length;

  tableDataPending.push({
    file: page.file.link,
    totalPending: filteredTasks.length,
    pendingTexts: filteredTasks.map(t => t.text).join(", "),
    created: page.created ? `[[${dv.date(page.created).toFormat("yyyy-MM-dd")}]]` : "–",
    mtime: page.file.mtime
  });
}

tableDataPending.sort((a, b) => b.mtime - a.mtime);

dv.table(
  ["Arquivo", "Pendentes", "Tarefas Pendentes", "Criado"],
  tableDataPending.map(row => [row.file, row.totalPending, row.pendingTexts, row.created])
);

dv.paragraph(`**Total Geral de Tarefas Pendentes:** ${totalTasksPending}`);
```

---

## Concluídas 

```dataviewjs
const startDate = dv.date("2025-05-01");
const endDate = dv.date("2025-05-31");

const pages = dv.pages('"EFFORTS"')
  .where(p => !(p.tags?.includes("#inlog") || p.tags?.includes("#lost-codes")))
  .where(p => !p.file.path.startsWith("EFFORTS/11_ARCHIVES"))
  .where(p => p.created && dv.date(p.created) >= startDate && dv.date(p.created) <= endDate);

let totalTasksCompleted = 0;
const tableDataCompleted = [];

for (let page of pages) {
  const tasks = page.file.tasks || [];
  const completedTasks = tasks.filter(t => t.completed && t.checked && t.type !== "area_utils");

  if (completedTasks.length === 0) continue;

  totalTasksCompleted += completedTasks.length;

  tableDataCompleted.push({
    file: page.file.link,
    totalCompleted: completedTasks.length,
    completedTexts: completedTasks.map(t => t.text).join(", "),
    created: page.created ? `[[${dv.date(page.created).toFormat("yyyy-MM-dd")}]]` : "–",
    mtime: page.file.mtime
  });
}

tableDataCompleted.sort((a, b) => b.mtime - a.mtime);

dv.table(
  ["Arquivo", "Concluídas", "Tarefas Concluídas", "Criado"],
  tableDataCompleted.map(row => [row.file, row.totalCompleted, row.completedTexts, row.created])
);

dv.paragraph(`**Total Geral de Tarefas Concluídas:** ${totalTasksCompleted}`);


```


tab: Done Tasks List

```dataview
TASK
FROM "EFFORTS"
WHERE completed AND checked and type != "area_utils"
GROUP BY file.name
```

````




