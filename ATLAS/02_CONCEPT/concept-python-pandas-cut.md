---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
[[pandas-cut]]

Usada para segmentar ou dividir uma variável numérica em inervados:
- útil para agrupar valores contínuos em categorias para análise

```css
pd.cut(x, bins, labels=None, right=True, include_lowest=False)
```

```css
import pandas as pd

# Criar uma Series de exemplo
valores = pd.Series([10, 15, 20, 25, 30, 35, 40, 45, 50])

# Segmentar os valores em 3 intervalos
categorias = pd.cut(valores, bins=3)

print(categorias)

```