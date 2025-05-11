---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: 
created: "[[30-01-2024]]"
---
2024-01-30 21:50

{{Objetivo do método}}

Utilizado para converter um DataFrame de formato amplo para longo, útil quando você tem variáveis distribuídas ao longo das colunas e deseja reorganizar 




Título: Conversão de DataFrame pandas de largo para longo

Blocos destacados:

Usado para converter um DataFrame de formato amplo para longo, útil quando as variáveis estão distribuídas nas colunas e você deseja reorganizá-las.

{{assinatura básica}}

```python
pandas.wide_to_long(df, stubnames, i, j, sep='', suffix='\d+')
```

{{parâmetros}}

