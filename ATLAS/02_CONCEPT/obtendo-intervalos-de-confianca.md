---
tags:
  - reading
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-hypothesis-testing]]"
  - "[[hub-statistic]]"
---
```python
from statsmodels.stats.weightstats import zconfint
zconfint(nota_media_dos_filmes_com_pelo_menos_10_votos)
```

```python
from statsmodels.stats.weightstats import DescrStatsW

descr_todos_com_10_votos = DescrStatsW(nota_media_dos_filmes_com_pelo_menos_10_votos)
descr_todos_com_10_votos.tconfint_mean()
```



