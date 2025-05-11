---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html
created: "[[2024-02-12]]"
---
2024-02-12 11:41

{{Objetivo do método}}
Aplica operações sobre um eixo de um dataframe

{{assinatura básica}}

```python
DataFrame.agg(func, axis=0, *args, **kwargs)
```

{{parâmetros}}


`func` - função ou lista de funções a serem aplicadas
`axis` - eixo na qual será aplicada
`*args*` - argumentos adicionais a serem passadas na função
`**kwargs` - recebe valores do tipo dicionários