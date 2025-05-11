---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
---

método [[pandas-crosstab-method]] para comparação de parametros

Dicionário base para categorização:
```css
sexo = {0:'Masculino',
        1: 'Feminino'}

cor = {0:'Indigena',
       2:'Branca',
       4:'Preta',
       6: 'Amarela',
       8:'Parda',
       9:'Sem declaração'}
```

compara a distribuição  de pessoas por etnia e gênero :
```css
frequencia = pd.crosstab(dados.Sexo,dados.Cor)
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
```

função de agregação de valores:
```css
frequencia = pd.crosstab(dados.Sexo,dados.Cor, aggfunc = 'mean', values = dados.Renda ) 
frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
```
- aggfunc(mean) atribui o valor da média em cada combinação

