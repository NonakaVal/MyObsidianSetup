↪[Collection](Collection.md)

# Kanban styling - background customized

---

- author:: dev-araujo
- source::

---

cover::![](https://i.pinimg.com/originals/0a/de/07/0ade07fe59d1e3d892a26e7e3dc1de3f.png)

```css
/*
author: dev-araujo
*/

/* --- Kanban With Background Customized --- */

.theme-dark .view-content .kanban-plugin::after,
.theme-light .view-content .kanban-plugin::after {
  content: "";
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: -1;

  /* Change PATH-FOR-YOUR-BACKGROUND to your image path */
  background-image: url(PATH-FOR-YOUR-BACKGROUND) !important;
  background-repeat: no-repeat;
  background-size: cover;
}
```
