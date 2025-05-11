---
tags:
  - learning/review
HUB:
  - "[[hub-hypothesis-testing]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
  - "[[hub-python]]"
---
![Imgur](https://i.imgur.com/DRcdyBb.png)
![[dist-t-siginficancia.png]]

Verificando teste de significância t_value com barplot

![Imgur](https://i.imgur.com/CwXxRc4.png)

```python
t_valores = modelo_ajustado.tvalues
nome= t_valores.index.tolist()
```

```python
from scipy import stats
distribuicao  = stats.t(df = 4)
distribuicao.ppf(q = 1 - 0.025)
limite = [distribuicao.ppf(q = 1 -0.025  )]*len(nome)
```

```python
pareto = sns.barplot(x = t_valores, y = nome )
pareto.figure.set_size_inches(15,6)
pareto.tick_params(labelsize = 20)
pareto.set_xlabel('t-valores', fontsize = 20)
pareto.plot(limite, nome, 'r')
```



![Imgur](https://i.imgur.com/TR7glYS.png)


![Imgur](https://i.imgur.com/X7h3xna.png)

