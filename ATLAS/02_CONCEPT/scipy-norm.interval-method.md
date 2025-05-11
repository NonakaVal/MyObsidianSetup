---
tags:
  - learning/review
HUB:
  - "[[hub-probabilidade]]"
---
Para calcular o [[obtendo-intervalos-de-confianca|-intervalos-de-confianca]] de uma distribuição normal, você pode usar a função `ppf` para encontrar os valores que delimitam a faixa onde uma certa porcentagem dos dados deve estar. Por exemplo, um intervalo de confiança de 95% abrange do percentil 2,5% ao percentil 97,5%, que você pode calcular usando `ppf(0.025)` e `ppf(0.975)`.

>Problema2: Uma amostra aleatória simples de 1976 itens de uma população normalmente distribuída, com desvio padrão populacional igual a 11, resultou em uma média amostral de 28.

Qual o intervalo de confiança de 90% para a média populacional?
```python
media_amostral = 28
desvio_padrao = 11
n = 1976

norm.interval(confidence = 0.90, loc = media_amostral, scale = desvio_padrao / np.sqrt(n))
```

