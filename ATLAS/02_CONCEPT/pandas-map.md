---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html
created: "[[2024-02-12]]"
---
2024-02-12 11:01

{{Objetivo do método}}

Aplica uma função pré-definida em todo to df:


![Imgur](https://i.imgur.com/8fJ9BqH.png)

{{assinatura básica}}

```python
DataFrame.map(func, na_action=None, **kwargs)
```

{{parâmetros}}

- `func` - a função a ser aplicada
- `na_action` - se "ignore" ignora valores nulos
- `**kwargs` - recebe valores do tipo dicionários