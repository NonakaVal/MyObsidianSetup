---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-probabilidade]]"
---
A função `comb` calcula o número de maneiras de escolher `k` itens de um conjunto de `n` itens, sem se importar com a ordem. Isso é útil para determinar combinações em problemas de probabilidade.

[[concept-statistic-distribuicao-binomial]] e [[scipy-comb]]

> Chance de acertar 6  em 60 com uma tentativa
```css
from scipy.special import comb

combinacao = comb(60 , 6)

probabilidade = 1 /combina
print('%0.10f' % probabilidade)
```


>Chance de passar (acertando 5) em 10
```css
from scipy.special import comb

n = 10
n_alt_q = 3
p =  1/n_alt_q

q = 1 - p
k = 5


prob = (comb(n ,k) * (p**k) * (q**(n - k)))
print('%0.8f' % prob)
```

### [lib](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html)

>Uma moeda, perfeitamente equilibrada, é lançada para o alto <font color = 00bfff>quatro</font> vezes. Utilizando a distribuição binomial, obtenha a probabilidade de a moeda cair com a face coroa voltada para cima <font color = 00bfff>duas</font> vezes.
```css
from scipy.special import comb

n = 4  # Total de lançamentos
n_alt_q = 2  
p =  1/n_alt_q  # Probabilidade de sair COROA
q = 1 - p
k = 2    # Total de sucessos (faces COROA voltada para cima)

prob = (comb(n ,k) * (p**k) * (q**(n - k)))
print('%0.8f' % prob)
```


