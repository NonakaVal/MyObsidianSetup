---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
---


Criando dataFrame com amostras para estudo do  [[teorema-do-limite-central]]

> Importando dados
```css
import pandas as pd
dados = pd.read_csv('dados.csv')
```

> Parâmetros 
```css
n = 2000 # tamanho da amostra
total_amostra = 1500  # quandidade de amostras a serem geradas 
```

> Criando um dataframe vazio
```css
amostas = pd.DataFrame()
```

>Gerando amostras com sample()
```css
for i in range(total_amostras): 
    _ = dados.Idade.sample(n)
    _.index = range(0, len(_))
    amostras['amostra_' + str(i)] = _
    
amostras 
```

