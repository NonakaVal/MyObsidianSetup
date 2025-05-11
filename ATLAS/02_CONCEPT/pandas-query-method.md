---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---


[[concept-pandas-with.query]]

### Média com condição

.query =  é uma função do pandas que permite filtrar dados no dataframe
[[cmp-pandas-importing-data]]
```css
notas.query("filmeid==1").nota.mean()

resultado = df.query('idade > 30 and sexo == "Feminino"')
```
- no arquivo armazenado na variável "notas" a função "query" verifica se o "filmeid" é igual a 1 então calcula a média da coluna "nota" de todos os valores.

``` css
notas_por_filme = notas.query("filmeid==1").nota.mean()
```
- média das notas sendo armazenada na variável "notas_por_filme"