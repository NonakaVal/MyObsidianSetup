---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html
created: "[[10-02-2024]]"
---
2024-02-10 17:48

{{Objetivo do método}}
insere uma nova coluna em um df

![Imgur](https://i.imgur.com/5Unutj9.png)

{{assinatura básica}}

```python
DataFrame.insert(loc, column, value, allow_duplicates=False)
```

{{parâmetros}}
- `loc` - Índice da coluna onde a nova coluna sera inserida
- `column`: rotulo na nova coluna
- `value` - valroes iniciais para a coluna
- `allow_duplicates` - booleano que indica se serão permitidas rotulos duplicados
