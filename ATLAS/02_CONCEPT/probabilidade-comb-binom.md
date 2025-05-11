---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
---
![[scipy-comb]]

>chance em acertar 5 ou mais

[[scipy-stats.binom]]

>com *pmf*:
```css
from scipy.stats import binom

probabilidade = binom.pmf(k,n,p)
print('%0.13f' % probabilidade)

binom.pmf([5,6,7,8,9,10], n , p).sum()

```

>com cdf

```css
1 - binom.cdf(4,n,p)
```


