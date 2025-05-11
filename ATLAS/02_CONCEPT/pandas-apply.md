---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
---

- é usada para aplicar uma função  personalizada em uma coluna ou em um dataframe como um todo:
	- é aplicado em cada elemento

sintaxe básica:

```css
dataframe.apply(func, axis = 0)
```
- dataframe - é o df no qual se quer aplicar a função
	- func a função q deseja aplicar
		- axis =0 especifica se será aplicado as colunas = 0 ou as linhas = 1
			- a função pode ser uma [[concept-lambda]] ou [[concept-python-funcoes]] definidas

ex
```css
import pandas as pd

dados = pd.DataFrame({'Idade': [25, 30, 35, 40]})

def alter(x):
	if x == 25:
		return x + 10
	else:
		return x - 10

dados['alter'] = dados['Idade'].apply(alter)
print(dados)
```

![Imgur](https://i.imgur.com/NGeSKVG.png)