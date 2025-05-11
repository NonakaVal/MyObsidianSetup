---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
  - "[[hub-hypothesis-testing]]"
---


[[concept-statistic-amostragem]]

[[concept-statistic-variaveis-quantitativas-e-populacao-infinita]] com python

O valor do gasto mdio dos clientes de uma loja de convenincia  de R$ 45,50. Assumindo que o desvio padro dos gastos  igual a R$ 15,00, qual deve ser o tamanho da amostra para estimarmos a mdia populacional com um nvel de significncia de 10%?
Considere que o erro mximo aceitvel seja de 10%.

```python
from scipy.stats import norm
media = 45.5
sigma = 15
significancia = 0.10
confianca = 1 - significancia
z = norm.ppf(0.5 + (confianca / 2))
erro_percentual = 0.10
e = media * erro_percentual
n = (z * (sigma / e)) ** 2
n.round()
```

[[concept-statistic-variaveis-quantitativas-e-populacao-infinita]] com python

Um fabricante de farinha verificou que, em uma amostra aleatria formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos, apresentou um desvio padro amostral do peso igual a 480 g.
Considerando um erro mximo associado  mdia populacional igual a 0,3 kg e um nvel de confiana igual a 95%, qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confivel do parmetro populacional?

```python
from scipy.stats import norm

N = 2000
z = norm.ppf(0.5 + (0.95 / 2))
s = 480
e = 0.3 * 1000   # Convertendo kg para g

n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N - 1)))
int(n.round())
```



```python
np.random.seed(75243)

temp = nota_media_dos_filmes_com_pelo_menos_10_votos.sample(frac= 1)

medias = [temp[0:i].mean() for i in range (1, len(temp))]
```
