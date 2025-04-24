---
cssclasses:
  - wide-page
---

```meta-bind-button
label: Search Notes
icon: lucide-map-pinned
hidden: true
class: ""
tooltip: Open Map of Content
id: open_moc
style: primary
actions:
  - type: command
    command: obsidian-hotkeys-for-specific-files:HUB/Map of Content.md

```
```meta-bind-button
label: Today
icon: calendar
hidden: false
class: “”
tooltip: “”
id: today
style: primary
actions:
  - type: command
    command: periodic-notes:open-daily-note
```
```meta-bind-button
label: Create Note
icon: lucide-plus-circle
hidden: true
class: ""
tooltip: Create a New Note
id: create_new_note
style: primary
actions:
  - type: command
    command: quickadd:choice:a019f4b7-7f8e-4937-8069-7a9ad8c4b10e

```
```meta-bind-button
label: Recent Files
icon: lucide-navigation
hidden: true
class: ""
tooltip: Open Quick Switcher
id: quick_switcher
style: primary
actions:
  - type: command
    command: switcher:open

```

```meta-bind-button
label: Switch to Light Mode
hidden: true
id: light_mode
style: destructive
actions:
  - type: command
    command: theme:use-light
tooltip: Switch to Light Mode
```
```meta-bind-button
label: Switch to Dark Mode
hidden: true
id: dark_mode
style: primary
actions:
  - type: command
    command: theme:use-dark
tooltip: Switch to Dark Mode
```
`BUTTON[create_new_note]` 

`BUTTON[quick_switcher]` 



---



> [!multi-column]
>
>> [!blank|center]
> [![brain icon|70](https://img.icons8.com/ios/250/FFFFFF/brain.png) <br/> *Atlas*](knowledge-mocs.md)
>
>> [!blank|center]
> [![briefcase icon|70](https://img.icons8.com/ios/250/FFFFFF/business.png) <br/> *Work*](moc-collectors.md)
>
>> [!blank|center]
> [![home icon|70](https://img.icons8.com/?size=100&id=71186&format=png&color=FFFFFF) <br/> *Efforts*](moc-efforts.md)
>
>> [!blank|center]
> [![home icon|70](https://img.icons8.com/?size=100&id=3447&format=png&color=FFFFFF) <br/> *Social*](moc-social.md)


---

### Areas
```dataview
table area_category as "Area Category", created as "Date Created" from "Efforts/AREAS"
WHERE type = "area_family"
```




## Tasks


```dataview
TASK
FROM "Efforts"
WHERE !completed AND !checked
GROUP BY file.name

```



```dataview
TASK
FROM "Calendar/DAILY"
WHERE !completed AND !checked


```

---

## Projects
```dataviewjs
let pages = dv.pages('"Efforts/PROJECTS"')
    .where(p => (p.type == "project_note" || p.type == "project_family") && p.Status != "4 Completed");

// Separate pages with and without due dates
let withDueDates = pages.where(p => p.Due_Date != null);
let withoutDueDates = pages.where(p => p.Due_Date == null);

// Sort pages with due dates by: Due Date -> Priority Level (A-Z) -> Status (Z-A)
withDueDates = withDueDates.sort(p => p.Due_Date)
    .sort(p => p.Priority_Level)
    .sort(p => p.Status, 'desc');

// Sort pages without due dates by: Priority Level (A-Z) -> Status (Z-A)
withoutDueDates = withoutDueDates.sort(p => p.Priority_Level)
    .sort(p => p.Status, 'desc');

// Combine both lists
let allPages = withDueDates.concat(withoutDueDates);

// Render the table with clickable project links
dv.table(
    ["Days", "Project", "Priority Level", "Status", "Due Date"],
    allPages.map(p => [
        p.Due_Date ? Math.floor(dv.date(p.Due_Date).diff(dv.date("today"), 'days').days) : "-", // Display whole number of days
        p.file.link, // Use p.file.link to render the project name as a clickable link
        p.Priority_Level || "-",
        p.Status || "-",
        p.Due_Date ? dv.date(p.Due_Date).toFormat("MM-dd") : "-"
    ])
);
```
