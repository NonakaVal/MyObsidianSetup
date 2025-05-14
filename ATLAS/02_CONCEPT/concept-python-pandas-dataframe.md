---
hub:
  - "[[hub-python]]"
tags:
  - learning
  - 
---

## .DataFrame
- criando um DataFrame a partir de um dicionário:
```css
data = {
    'coluna0':{'linha0':1, 'linha1':4,'linha2':8},
    'coluna1':{'linha0':2, 'linha1':5,'linha2':10},
    'coluna2':{'linha0':3, 'linha1':132,'linha2':2}
}
data
```




```css
import pandas as pd

DataFrame1 = pd.DateFrame(data)

```
alteração simples em elementos iguais em um dataframe:
```
DataFrame1[DataFrame1 > 0] = 1 
```
- altera todos os numeros menores que zero para 1


![[concept-organizando-dataframe]]