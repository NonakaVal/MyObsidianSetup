---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

-  é um método pandas que verifica se cada valor  está condito em  uma *lista* retornando uma Series booleana com "True" para os valores que estão na lista e "False" para os que não estão.

ex: 
criação de um dataframe a partir de numeros e letras
```css
import pandas as pd

numeros = [i for i in range(11)]
letras = [chr(i + 65) for i in range(11)]
nome_coluna = ['N']

df = pd.DataFrame(data = numeros, index = numeros, columns = nome_coluna)
```

seleção isin.

```css
selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
df = df[selecao]
```
- novo dataframe só com números pares