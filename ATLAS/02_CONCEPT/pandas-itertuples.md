---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html
created: "[[2024-02-10]]"
---
2024-02-10 20:03

{{Objetivo do método}}
itera sobre as linhas (rows) de um dataframe retornando tuplas para cada linha

![Imgur](https://i.imgur.com/16rZouW.png)

{{assinatura básica}}

```python
DataFrame.itertuples(index=True, name='Pandas')
```

{{parâmetros}}

- `index` = bool para criar ou não um indice
- `name` = nome a ser atribuido a tupla