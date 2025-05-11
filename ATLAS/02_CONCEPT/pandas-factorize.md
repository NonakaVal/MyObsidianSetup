---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.factorize.html
created: "[[30-01-2024]]"
---
2024-01-30 19:31

{{Objetivo do método}}

Codifica variáveis categóricas, retornando códigos únicos associados a cada valor único na variável


![Imgur](https://i.imgur.com/UXYg4Ze.png)

{{assinatura básica}}

```python
pandas.factorize(values, sort=False, order=None, na_sentinel=-1, size_hint=None)
```

{{parâmetros}}

- `values` - a variável categórica a ser codificada
- `sort` - se True, os codigos serão ordenados
- `order` - Lista de valores únicos que especifica a ordem dos códigos gerados
- `na_sentinel` - valor inteiro a ser usado para representar valores nulos
- `size_hint` - tamanho estimado do array de códigos