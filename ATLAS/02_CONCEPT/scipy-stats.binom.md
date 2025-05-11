---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-ml-models]]"
---
A `binom` representa a distribuição binomial, que calcula a probabilidade de obter um certo número de sucessos em uma sequência de `n` tentativas, onde cada tentativa tem uma probabilidade fixa de sucesso.

[[concept-statistic-distribuicao-binomial]]

## [lib](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html)

```python
from scipy.stats import binom

p = 1 / 6   # Probabilidade de sair o número CINCO
n = 10      # Total de lançamentos

print("{0:.2%}".format(binom.sf(2, n, p)))
```


```css
from scipy.stats import binom

p = 1 / 2  # Probabilidade de sair COROA
n = 4      # Total de lançamentos
k = 2      # Total de sucessos (faces COROA voltada para cima)

binom.pmf(k, n, p)
```


