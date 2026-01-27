  
```dataviewjs

const icon = (status) => {
    switch (status) {
        case "backlog": return "📥";
        case "ideia": return "🌱";
        case "roteiro": return "✍️";
        case "gravando": return "🎤";
        case "edicao": return "🎞️";
        case "publicar": return "🎬";
        case "revisar": return "📈";
        default: return "";
    }
};

// Formata a data como [[YYYY-MM-DD]]
const formatCreatedLink = (date) => {
    if (!date) return "—";
    return `[[${date.toFormat("yyyy-MM-dd")}]]`;
};

const pages = dv.pages("#task")
    .where(p => !p.file.path.includes("X"))
    .where(p => !p.file.name.includes("Master Key (YouTube Tags)"))
    .sort(p => p.file.mtime, "desc")
    .limit(77);

dv.table(
    ["Vídeo", "Status", "Area/Projects", "Modificado"],
    pages.map(p => [
        `${icon(p.status)} ${p.file.link}`,
        p.status,
        p.projects ?? "—",
        moment(p.file.mtime.ts).fromNow()
        
    ])
);

```
---


`BUTTON[task]`     `BUTTON[calendar]`  `BUTTON[board]` 

 

```meta-bind-button
label: Open Task List
hidden: true
icon: check
class: ""
id: task
style: default
actions:
  - type: command
    command: tasknotes:open-tasks-view
```


```meta-bind-button
label: Open Kanban Board
hidden: true
icon: grid
class: ""
id: board
style: default
actions:
  - type: command
    command: tasknotes:open-kanban-view
```

   

```meta-bind-button
label: Open calendar
hidden: true
icon: calendar
class: ""
id: calendar
style: default
actions:
  - type: command
    command: tasknotes:open-advanced-calendar-view
```

