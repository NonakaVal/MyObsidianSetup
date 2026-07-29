---
title: crop 2x2 Grid
id: 4
---

```
mkdir -p faces && for img in *.png *.jpg *.jpeg *.webp; do convert "$img" -crop 2x2@ +repage +adjoin "faces/${img%.*}_%02d.png"; done
```
