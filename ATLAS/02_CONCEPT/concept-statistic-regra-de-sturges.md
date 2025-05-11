---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
---


permite encontrar a estimativa de intervalos para um histograma:
# $$k = 1 + \frac {10}{3}\log_{10}n$$
com numpy
```css
import numpy as np
n = dados.shape[0]

k = 1 + (10/3) * np.log10(n)
k = int(k.round(0))
```





