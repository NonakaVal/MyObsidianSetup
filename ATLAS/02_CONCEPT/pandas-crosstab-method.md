---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
Cria uma tabela de contingência, ou tabela cruzada
útil para analisar a relação entre duas ou mais variáveis categóricas e contas as ocorrências de cada combinação possível de variáveis:

[crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html)

[[pandas-crosstab]]
```css
pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All')
```
- index: a variável ou lista de variáveis que será usada como o índice
	- columns: colunas que serão usadas

```css
import pandas as pd

# Criar um DataFrame de exemplo
dados = pd.DataFrame({'Sexo': ['Masculino', 'Feminino', 'Masculino', 'Masculino', 'Feminino'],
                      'Cor': ['Branca', 'Parda', 'Preta', 'Parda', 'Preta'],
                      'Idade': [30, 25, 35, 40, 25]})

# Calcular a tabela cruzada entre Sexo e Cor
tabela_cruzada = pd.crosstab(dados['Sexo'], dados['Cor'])

print(tabela_cruzada)

```

##### aggregated values with pd.crosstab()
```python
pd.crosstab(planes['Source'], planes['Destination'], values =planes['Price'], aggfunc='median')
```
