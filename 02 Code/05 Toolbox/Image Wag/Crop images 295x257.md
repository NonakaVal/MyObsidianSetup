---
title: Crop images 295x257
id: 13
---

```
mkdir -p faces

for img in *.{png,jpg,jpeg,webp,PNG,JPG,JPEG,WEBP}; do
  [ -e "$img" ] || continue
  magick "$img" \
    -auto-orient \
    -resize 260x260^ \
    -gravity center \
    -extent 295x257 \
    "faces/${img%.*}_crop.png"
done
```
