---
tags:
  - learning
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-statistic]]"
  - "[[hub-python]]"
---



> variância é uma medida de dispersão que indica a extensão na qual os valores de um conjunto de dados se afastam da média

### Variância populacional
>quanto se tem todos os dados, e calcula a média dos quadrados de cada valor
# $$\sigma^2 = \frac 1n\sum_{i=1}^{n}(X_i-\mu)^2$$
### Variância amostral
> quando se tem apenas uma amostra do total
# $$S^2 = \frac 1{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$$

>por etapas criando um dataframe: a a partir do calculo do [[concept-statistic-desvio-medio-absoluto]]
```css
notas_fulano['(Desvio)^2'] = notas_fulano['Desvio'].pow(2)
notas_fulano['(Desvio)^2'].sum() / (len(notas_fulano) - 1)
```

> operação direta:
```css
variancia = notas_fulano.Fulano.var()
```
