---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-data-visualization]]"
---

[[concept-linear-regression]]
> Definindo paleta de cores e estilo 

[set_palette](https://seaborn.pydata.org/generated/seaborn.set_palette.html) , [set_style](https://seaborn.pydata.org/generated/seaborn.set_style.html)
``` python
import seaborn as sns

sns.set_palette('terrain')
sns.set_style('darkgrid')
```

Gráfico de dispersão para regressão linear
```python
ax1 = sns.lmplot(data = experimento, x = 'Farinha', y = 'Porcoes', ci = None, hue = 'Chocolate')
ax1.set(xticks = (-1,1))

ax2 = sns.lmplot(data = experimento, x = 'Chocolate', y = 'Porcoes', ci = None, hue = 'Farinha'     )
ax2.set(xticks = (-1,1))
```

