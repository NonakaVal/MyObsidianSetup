---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
created: "[[31-01-2024]]"
---
2024-01-31 13:29

{{Objetivo do método}}
utilizado para converter os valores de uma série para numéricos, 
[[cmp-categorical-and-numerical-wrangling]]

to-numeric-pandas-image

{{assinatura básica}}

```python
pandas.to_numeric(arg, errors='raise', downcast=None)
```

{{parâmetros}}

- `arg` - a serie, lista, array ou objeto similar que você deseja converter para numérico
- `errors` - Define como lidar com erros durante a conversão, `raise` - lança um erro, `coerce` - converte para NAN, `ignore` - ignora o erro
- `downcast` - especifica uma classe de tipo inferior

