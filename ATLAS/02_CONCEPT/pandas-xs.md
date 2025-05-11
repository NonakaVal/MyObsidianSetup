---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html
created: "[[2024-02-10]]"
---
2024-02-10 20:08

{{Objetivo do método}}

{{assinatura básica}}

```python
DataFrame.xs(key, axis=0, level=None, drop_level=True)
```

{{parâmetros}}

- `key` - Rótulo a ser selecionado
- `axis` - eixo ao longo do qual realizar a seleção
- `level` - nível especifico se o df tiver um m multdex
- `drop_level` - bool indicando se os nível utilizados para seleção