---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---


## organizando dataframe

Criando um [[concept-python-pandas-dataframe]]:
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



