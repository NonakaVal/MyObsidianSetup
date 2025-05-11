---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.qcut.html
created: "[[30-01-2024]]"
---
2024-01-30 18:42

{{Objetivo do método}}

utilizado para discretizar variáveis em intervalos com base nos quantis dos dados
dividindo os dados em quantis especificos

![Imgur](https://i.imgur.com/CCHky2W.png)

{{assinatura básica}}

```python
pandas.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise', ordered=True)
```

{{parâmetros}}

- `x` - A variável que você deseja discretizar
- `q` - numero de quantis desejados, ou quantis
- `labels` - rótulos para os intervalos
- `retbins` - se True retorna os intervalos usados
- `precision` - Número de casas decimais a serem usadas ao arrendar valores
- `duplicates` - como lidar com valores duplicados(raise, drop, raise)
- `ordered` - se os quantis devem ser ordenados
