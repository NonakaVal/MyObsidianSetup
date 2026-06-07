---
tags:
  - learning
HUB:
  - "[[hub-tratamento-de-dados]]"
  - "[[hub-python]]"
---

[[cmp-pandas-importing-data|-dados-importados-a-partir-de-um-csv]]
```css
import pandas as pd
dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
```

- criando uma nova coluna a partir da seleção de outras colunas do Dataframe:
```css
dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU'] 

dados['Valorm2'] = dados['Valor'] / dados['Area']
```
- variável 'Valor Bruto' possui o resultado da soma de todos os valores selecionados
	- variável 'Valorm2' possui o resultado da divisão dos valores selecionados

```css
dados['Valorbrutom2'] = dados['Valor Bruto'] / dados['Area']
```
- valor com base em variável recém criada


Criando uma coluna com [[concept-pandas-apply]],  [[concept-python-condicionais]] e [[concept-lambda]]
```css
casa = ['Casa','Casa de Condomínio', 'Casa de Vila']

dados['Tipo agregado'] = dados.Tipo.apply(lambda x: 'casa' if x in casa else 'Apartamento')
dados
```
- primeiro é criado uma [[concept-python-arrays|lista]] para a seleção na função
	- cria-se a variável 'Tipo Agregado'