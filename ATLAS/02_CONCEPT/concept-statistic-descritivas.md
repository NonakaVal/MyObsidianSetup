---
tags:
  - learning
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-tratamento-de-dados]]"
---


- [[tipos-de-variaveis]]

- [[concept-python-pandas-value-counts-contando-os-valores]]  | [[python-unique-value_counts-method|value_counts]]
	- `frequencia = dados.Sexo.value_counts()`
	- `percentual = dados.Sexo.value_counts(normalize = True) * 100`


- [[concept-python-crosstab-comparando-multiplas-variaveis]]
	- `pd.crosstab(dados.Sexo,dados.Cor, aggfunc = 'mean', values = dados.Renda )`


- [[pandas-criando-intervalos]]
```python
classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E','D', 'C','B', 'A']

percentual = pd.value_counts(
    pd.cut(x = dados.Renda, bins = classes, labels = labels, include_lowest = True),
    normalize = True 
) *100

percentual = percentual.round(2)
```

