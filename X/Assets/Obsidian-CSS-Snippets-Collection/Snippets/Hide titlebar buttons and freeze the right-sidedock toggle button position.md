↪[Collection](Collection.md)

# Hide titlebar buttons and freeze the right-sidedock toggle button position

---

- author:: cerenkov
- source:: 

---

cover:: ![](https://i.imgur.com/GD4gqWJ.gif)

```css
/* hide window's titlebar buttons (minimize, maximize, close)
   and freeze the right-sidedock toggle button position to the right corner
   (making the left- and right-sidedock behaviours symmetrical, at last)
   only when obsidian is using hidden-frameless style and is maximized but not fullscreen */
/* author: cerenkov */

/* hide titlebar buttons */
body.is-hidden-frameless.is-maximized:not(.is-fullscreen)
  .titlebar-button-container.mod-right {
    display: none !important;
}

/* expand the tabbar to full width like when there's no titlebar buttons */
body.is-hidden-frameless.is-maximized:not(.is-fullscreen)
  .workspace-tab-header-container {
    padding-right: 8px !important;
}

/* remove the tabbar::after placeholder of titlebar buttons */
body.is-hidden-frameless.is-maximized:not(.is-fullscreen)
  .workspace-tab-header-container::after {
    display: none !important;
}

/* move the right-sidedock toggle button to the right corner when right-sidedock is open
   with a caveat that it might overlap with right-sidedock tab icons
   but you can use a horizontal split and keep most icons in the lower workspace */
body.is-hidden-frameless.is-maximized:not(.is-fullscreen):has(.is-right-sidedock-open)
  .sidebar-toggle-button.mod-right {
    position: fixed !important;
    right: 8px !important;
    z-index: 5;
}

/* modify the right-sidedock spacer element to be a no-drag region
   so that the right-sidedock toggle button can receive mouse click events
   with a caveat that the right spacer region can no longer double click to maximize/restore
   but you can still double click / right click on the left-sidedock spacer region */
body.is-hidden-frameless.is-maximized:not(.is-fullscreen):has(.is-right-sidedock-open)
  .mod-sidedock.mod-right-split
  .workspace-tab-header-spacer {
    app-region: no-drag !important;
}
```