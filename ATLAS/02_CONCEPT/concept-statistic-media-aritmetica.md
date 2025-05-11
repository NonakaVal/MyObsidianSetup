---
tags:
  - learning
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-statistic]]"
  - "[[hub-python]]"
---

## <font color=#39b8fa>3.1 Média aritmética</font>
***

É representada por $\mu$ quando se refere à população e por $\bar{X}$ quando se refere à amostra

# $$\mu = \frac 1n\sum_{i=1}^{n}X_i$$

> $n$ = número de observações (registros)

> $X_i$ = valor da i-ésima observação (registro)

[[concept-python-pandas-agrupamentos]]

```css
dados.groupby(['Sexo'])['Renda'].mean()
```

