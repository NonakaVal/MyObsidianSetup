---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
created: "[[08-02-2024]]"
---
2024-02-08 10:16

{{Objetivo do método}}
retorna informações sobre o dataset

{{assinatura básica}}

```python
DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None)
```

{{parâmetros}}

- `verbose` - controla o detalhamento das informações, se None retorna um resumo, se True retorna informações detalhadas
- `buf` - especifica o objeto onde as mensagens de saida serão gravadas, se None será exibida na tela
- `max_cols` - numero de colunas a serem exibidas
- `memory_usage` - controla a exibição do uso de memória, podendo ser deep, normal, ou None