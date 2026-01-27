↪[Collection](Collection.md)

# File explorer styling - Rainbow folder titles

---

- author:: sailKite
- source:: https://discord.com/channels/686053708261228577/702656734631821413/1163095446919585843

---

cover:: ![](https://i.imgur.com/vjXhJdp.png)

```css
/*
author: sailKite
source: https://discord.com/channels/686053708261228577/702656734631821413/1163095446919585843
*/

/* updated snippet for v1.6.3  */

.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder {
  --nav-item-color: var(--folder-color);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:hover {
  filter: brightness(0.9);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 2) {
  --folder-color: rgb(243, 139, 168);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 3) {
  --folder-color: rgb(235, 160, 172);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 4) {
  --folder-color: rgb(250, 179, 135);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 5) {
  --folder-color: rgb(249, 226, 175);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 6) {
  --folder-color: rgb(166, 227, 161);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 7) {
  --folder-color: rgb(148, 226, 213);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 8) {
  --folder-color: rgb(137, 220, 235);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 9) {
  --folder-color: rgb(116, 199, 236);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 10) {
  --folder-color: rgb(135, 176, 249);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 11) {
  --folder-color: rgb(180, 190, 254);
}
.nav-folder-children > .nav-folder,
.nav-files-container > div > .nav-folder:nth-child(11n + 12) {
  --folder-color: rgb(203, 166, 247);
}
```

**Subfolders with same colour as main folder**

```css
/* updated snippet for v1.6.3  */

.nav-files-container > div > .nav-folder {
  --nav-item-color: var(--folder-color);
}

.nav-files-container > div > .nav-folder:hover {
  filter: brightness(0.9);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 2) {
  --folder-color: rgb(243, 139, 168);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 3) {
  --folder-color: rgb(235, 160, 172);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 4) {
  --folder-color: rgb(250, 179, 135);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 5) {
  --folder-color: rgb(249, 226, 175);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 6) {
  --folder-color: rgb(166, 227, 161);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 7) {
  --folder-color: rgb(148, 226, 213);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 8) {
  --folder-color: rgb(137, 220, 235);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 9) {
  --folder-color: rgb(116, 199, 236);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 10) {
  --folder-color: rgb(135, 176, 249);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 11) {
  --folder-color: rgb(180, 190, 254);
}

.nav-files-container > div > .nav-folder:nth-child(11n + 12) {
  --folder-color: rgb(203, 166, 247);
}
```
