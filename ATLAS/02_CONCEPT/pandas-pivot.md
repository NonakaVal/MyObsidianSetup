---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.pivot.html
created: "[[30-01-2024]]"
---
2024-01-30 18:10

{{Objetivo do método}}

- inverso do [[pandas-melt]]
	- retorna um dataframe longo em um dataframe largo

![Imgur|700](https://i.imgur.com/A1Fdkzf.png)


{{assinatura básica}}

```python
pd.DataFrame.pivot(index=None, columns=None, values=None)
```

{{parâmetros}}

- `inxex` - nome da coluna ou colunas que serão usadas como indice
- `columns` - Nome da coluna cujo os valores serão usados para criar novas colunas
- `values` - Nome da coluna cujo valores preencherão o df resultante
