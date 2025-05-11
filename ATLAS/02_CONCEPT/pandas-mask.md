---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html
created: "[[2024-02-10]]"
---
2024-02-10 20:18

{{Objetivo do método}}
Substitui valores em um dataframe por um valor específico quando uma condição é atendida

![Imgur](https://i.imgur.com/3U4gX4X.png)

{{assinatura básica}}

```python
DataFrame.mask(cond, other=nan, inplace=False)
```

{{parâmetros}}

- `cond` - condição bool que determina se a substituição sera realizada
- `other` - valor a ser atribuido
- `inplace`