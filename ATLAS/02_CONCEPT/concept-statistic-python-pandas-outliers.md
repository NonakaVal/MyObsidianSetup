---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
  - "[[hub-statistic]]"
---
![Imgur](https://i.imgur.com/gmAvMdi.png)

<font color = 00bfff> Removendo Outliers</font>
- [[removendo-outliers]] | [[concept-statistic-descritivas]]
```python
q1 = valor.quantile(0.25) q3 = valor.quantile(0.75) IIq = q3 - q1 limite_inferior = q1 - 1.5 * IIq limite_superior = q3 + 1.5 * IIq

dados_new = dados[(valor >= limite_inferior) & (valor <= limite_superior)]
```
- [[seaborn-box-plot(diagrama-de-caixa)]]  

```
tmdb.query("runtime>0").runtime.dropna().quantile(q=0.8)
```

```
tmdb_com_mais_de_10_votos = tmdb.query("vote_count >= 10")
```


```python
import random

import pandas as pd


lista_aleatoria = (random.randint(1, 1000) for _ in range(1000))

  # Altere o número 10 para o tamanho desejado da lista
  

df = pd.DataFrame(lista_aleatoria)
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)

  

IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq


limite_superior = q3 + 1.5 * IIq


dados_new = df[(df >= limite_inferior) & (df <= limite_superior)]

  

print(limite_superior)
```