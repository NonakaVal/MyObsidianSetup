---
tags:
  - learning
HUB:
  - "[[hub-python]]"
dg-publish: true
---

## .concat
- contatena dois ou mais DataFrames
	- ex: dataframes armazenados nas variáveis "df1" e "df2"
```css
import pandas as pd
df3 = pd.concat([df1, df2], axis =1)
```
- "axis = 1" é o paramero que inverte a ordem do dataframe, por padrão não é escrito, só quando necessário 
