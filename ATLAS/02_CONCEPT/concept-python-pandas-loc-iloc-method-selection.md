---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

.loc[] e uma função em pandas que permite acessar e selecionar dados em um dataFrame com base em rótulos de índice e nomes de colunas específicos: sintaxe : *'dataframe.loc[linhas,colunas]'*

.iloc[] e uma função em pandas que permite acessar e selecionar dados em um dataFrame com base em índices números das linhas e colunas: sintaxe : *'dataframe.iloc[linhas,colunas]'*

### .loc[] 
ex: loc para selecionar uma coluna específica:
```css
import pandas as pd

# DataFrame de exemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['L1', 'L2', 'L3'])

# Selecionando todas as linhas da coluna 'B'
coluna_B = df.loc[:, 'B']
print(coluna_B)

```
- saída será só a coluna 'B'

loc para selecionar linhas e colunas específicas:
```css
import pandas as pd

# DataFrame de exemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['L1', 'L2', 'L3'])

# Selecionando linhas 'L2' e 'L3' e colunas 'B' e 'C'
subset = df.loc[['L2', 'L3'], ['B', 'C']]
print(subset)

```

### .iloc[]

iloc para selecionar uma coluna específica:
```css
import pandas as pd

# DataFrame de exemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Selecionando todas as linhas da coluna de índice 1 (coluna 'B')
coluna_B = df.iloc[:, 1]
print(coluna_B)

```

iloc para selecionar linhas e colunas específicas:

```css
import pandas as pd

# DataFrame de exemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Selecionando linhas de índice 1 e 2 e colunas de índice 1 e 2
subset = df.iloc[1:3, 1:3]
print(subset)

```