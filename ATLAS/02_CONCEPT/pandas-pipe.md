---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html
created: "[[2024-02-12]]"
---
2024-02-12 11:31

{{Objetivo do método}}

Permite usar os valores de um dataframe como argumentos para uma função, e retorna um novo dataframe.

![Imgur](https://i.imgur.com/LeG8wBF.png)

![Imgur](https://i.imgur.com/PScW0hX.png)

{{assinatura básica}}

```python
DataFrame.pipe(func, *args, **kwarks)
```

{{parâmetros}}

- `func` - a função a ser aplicada
- `*args*` - argumentos adicionais a serem passadas na função
- `**kwargs` - recebe valores do tipo dicionários