---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-tratamento-de-dados]]"
---
A função `cdf` (Cumulative Distribution Function) calcula a probabilidade acumulada até um certo ponto em uma distribuição normal. Em outras palavras, ela dá a probabilidade de uma variável aleatória ser menor ou igual a um valor específico.

[[concept-statistic-distribuicao-normal-(gaussiana)]] com `cdf`

```css
from scipy.stats import norm

media = 70
desvio_padrao = 5
Z = (85 - media) / desvio_padrao
norm.cdf(Z)
```

Com limites

O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal, com média R$ 300,00 e desvio padrão igual a R$ 50,00. Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:

**1)** Entre R$ 250,00 e R$ 350,00 **2)** Entre R$ 400,00 e R$ 500,00
```css
from scipy.stats import norm

m = 300
d_p = 50

a = 350 # 500
b = 250 # 400

a_limit = (a - m) / d_p
b_limit = (b - m)/d_p

probabilidade = norm.cdf(a_limit) - norm.cdf(b_limit)
probabilidade

```



O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída, com média igual a 720 dias e desvio padrão igual a 30 dias. Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:

**1)** Entre 650 e 750 dias **2)** Mais que 800 dias **3)** Menos que 700 dias

```css
from scipy.stats import norm

media = 720
desvio_padrao = 30

# Item 1
Z_inferior = (650 - media) / desvio_padrao
Z_superior = (750 - media) / desvio_padrao

probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)
print("{0:.2%}".format(probabilidade))

# Item 2
Z = (800 - media) / desvio_padrao

probabilidade = 1 - norm.cdf(Z)
print("{0:.2%}".format(probabilidade))

# Item 3
Z = (700 - media) / desvio_padrao

probabilidade = norm.cdf(Z)
print("{0:.2%}".format(probabilidade))
```

