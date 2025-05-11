---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-probabilidade]]"
---
A `poisson` é usada para modelar a probabilidade de um certo número de eventos ocorrer em um intervalo de tempo ou espaço, quando esses eventos acontecem a uma taxa constante e independentemente uns dos outros.

## [lib](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html)

>Um restaurante recebe em média 20 pedidos por hora. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?

[[concept-statistic-distribuicao-poisson]] 
```css
from scipy.stats import poisson

media = 20
k = 15

probabilidade = poisson.pmf( k , media  )
print('%0.8f'%probabilidade)
```

com numpy
```css
probabilidade = ((np.e** ( - media) )*(media **k))/(np.math.factorial(k))

print('%0.8f'%probabilidade)
```


>O número médio de clientes que entram em uma padaria por hora é igual a 20. Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.

```css
media = 20
k = 25

prob = poisson.pmf(k, media)
prob
```
