---
tags:
  - learning/review
HUB:
  - "[[hub-data-wrangling]]"
  - "[[hub-statistic]]"
---
método 1.5 IIQ com [seaborn-Box-plot(Diagrama de caixa)](app://obsidian.md/seaborn-Box-plot(Diagrama%20de%20caixa)).
```python
valor = dados.Valor

q1 = valor.quantile(.25)
q3 = valor.quantile(.75)
IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq
limite_superior = q3 + 1.5 * IIq
```
```python
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]
```
