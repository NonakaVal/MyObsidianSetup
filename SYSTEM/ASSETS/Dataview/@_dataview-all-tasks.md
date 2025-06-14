
## [[@_dataview-all-tasks]]


```dataviewjs
const pages = dv.pages("")
  .where(p => !p.file.path.startsWith("DRAFTS"))
  .where(p => p.file.tasks && p.file.tasks.length > 0);

let totalTasks = 0;
let totalCompleted = 0;

let tableData = [];

for (let page of pages) {
  const tasks = page.file.tasks || [];
  if (tasks.length === 0) continue;

  const completedTasks = tasks.filter(t => t.completed);
  const pendingTasks = tasks.filter(t => !t.completed);

  totalTasks += tasks.length;
  totalCompleted += completedTasks.length;

  tableData.push({
    file: page.file.link,
    total: tasks.length,
    completed: completedTasks.length,
    pending: pendingTasks.length,
    completedList: completedTasks.map(t => t.text).join(", "),
    pendingList: pendingTasks.length > 0 ? pendingTasks.map(t => t.text).join(", ") : "-"
  });
}

// Ordena pela quantidade de tasks pendentes
tableData = tableData.sort((a, b) => b.pending - a.pending);

// Linha de totais finais
tableData.push({
  file: "**Total Geral**",
  total: totalTasks,
  completed: totalCompleted,
  pending: totalTasks - totalCompleted,
  completedList: "",
  pendingList: ""
});

dv.table(
  ["📘 Nota", "Total", "✔️", "🟢", "🔴"],
  tableData.map(row => [row.file, row.total, row.completed, row.completedList, row.pendingList])
);

```





