---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---
[[cmp-pandas-importing-data]]

### Lista de valores únicos de uma coluna
```css
notas["nota"].unique() ou  notas.nota.unique()
```
- ".unique()" é o metodo que retorna uma lista de todos os valores únicos presentes na coluna ["nota"] dentro do arquivo csv armasenado na variavel "notas".

### Contar quantas vezes cada valor único aparece na coluna
 ```css
notas[nota].value_counts()  ou  notas.nota.value_counts()
```
- "value_counts" é aplicado para criar uma lista que conta quantos vezes cada valor único na coluna "nota" aparece.

