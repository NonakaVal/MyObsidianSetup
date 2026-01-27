---
cssclasses:
  - cards
  - wide-page
---
```dataview
TABLE without id cover AS "Cover", file.link AS "Name", "<span style='text-decoration: underline 2px orange'>" + author AS "Author"
FROM "System/Assets/Obsidian-CSS-Snippets-Collection/Snippets"
SORT file.name
```
