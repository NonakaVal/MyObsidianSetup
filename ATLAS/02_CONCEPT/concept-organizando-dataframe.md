---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
dg-publish: true
---


## organizando dataframe

[[concept-python-pandas-dataframe|criando um DataFrame a partir de um dicionário]]


```css
import pandas as pd
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, list('zyx'), list('cba'))
```

Organizando o DataFrame:
```css
df.sort_index()
ou 
df.sort_index(axis = 1)
```

```css
dataframe.sort_values(by, axis=0, ascending=True, inplace=False, na_position='last')

```
- ordena os valores 



