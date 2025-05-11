---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
---

[[concept-boxplot]] : 
![Imgur](https://i.imgur.com/gmAvMdi.png)
>[[removendo-outliers]]


[[cmp-pandas-importing-data]]
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')
```

[[seaborn-box-plot(diagrama-de-caixa)]]
```python
ax = sns.boxplot (x = 'Altura', data = dados, orient = 'h')
ax.figure.set_size_inches(12,4)
```
> orient determina que o grfico sera apresentado na horizontal
> 	seguido definies do tamanho que ter o grfico 


passando dois parmetros e alterando titulo e nome dos eixos,  e filtrando dados especficos  [[concept-pandas-with.query]]
```css
ax = sns.boxplot (x = 'Renda',y = 'Sexo', data = dados.query( 'Renda <= 10000' ), orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Renda', fontsize = 12)
ax.set_xlabel('RS', fontsize =14)
```
>outro exemplo com [[concept-pandas-with.query|query]] para filtrar dados especfico:
```css
ax = sns.boxplot(x = 'Renda', y = 'UF', data = dados.query('(UF==35 or UF==29) and Renda < 10000'), orient = 'h')

ax.figure.set_size_inches(12, 6)
ax.set_title('Renda (R$) - Bahia X So Paulo', fontsize=18)
ax.set_xlabel('R$', fontsize=14)
```

```css
ax = sns.boxplot(x = 'Renda', y = 'Cor', hue = 'Sexo', data = dados.query('Renda < 10000'), orient = 'h')
```