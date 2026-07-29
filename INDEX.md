---
banner: https://imgur.com/Npz1TE7.png
banner_y: 14.50385
cssclasses:
  - wide-page
  - hide-properties_reading
  - hide-properties_editing
---

![[Boards.base]]

````tabs
tab: À Fazer 

```dataview
TASK
FROM "Daily Notes"
WHERE !completed AND !checked

```

tab: Concluídas
```dataview
TASK
FROM "Daily Notes"
WHERE completed AND checked
SORT file.mtime DESC

```


````

---


![[Recents.base]]

---


<br>

[[README]]