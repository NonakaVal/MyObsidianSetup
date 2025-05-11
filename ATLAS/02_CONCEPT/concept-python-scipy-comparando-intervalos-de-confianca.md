---
tags:
  - learning/review
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-hypothesis-testing]]"
---


> notas1 com cálculos nota
```python
zconfint(notas.rating, notas1.rating)
```

> nota1,  
```python
from scipy.stats import ttest_ind
ttest_ind(notas1.rating, notas.rating)
```

```python
from statsmodels.stats.weightstats import DescrStatsW
todas_notas = DescrStatsW(notas.rating)
toy_notas = DescrStatsW(notas1.rating)
comparacao = todas_notas.get_compare(toy_notas)
```

Z-test ou T-test
```python
comparacao.summary(use_t = True)
comparacao.summary(use_t = False)
```


