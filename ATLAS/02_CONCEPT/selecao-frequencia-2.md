---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

[[cmp-pandas-importing-data|-dados-impordados-como-csv]] na variável dados
```css
import pandas as pd 
dados = pd. read_csv('aluguel_residencial.csv', sep = ';')
```

selecione somente imóveis classificados como tipo "Apartamento"
```css
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]
```
- [[operadores-relacionais|-uso-de-operadores-relacionais]] para criar uma série booleana com base na condição "Apartamento"  na coluna "Tipo" no dataframe armazenado na variável 'dados', 
	- armenando esse resultado na variável "selecao"
		- [[tipos-de-dados|-dado-extraido-com-.shape]]

selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e "Casa de Vila":
```css
selecao = (dados.Tipo == 'Casa') | (dados.Tipo == 'Casa de Condomínio') | (dados.Tipo == 'Cada de Vila')
n2 = dados[selecao].shape[0]
```
- usado o operador lógico "|" para verificar se uma das condições é verdadeira  e então adiciona no valor de [[tipos-de-dados|.shape]]
	- [[concept-python-conjuntos|outro-exemplo-do-operadores]]

selecione os imóveis com área entre os 60 e 100 metros quadrados inclindo os limires
```css
selecao = (dados.Area >= 60) & (dados.Area <= 100)
dados[selecao].shape[0]
```
- o operador & exige que todas as condições sejam verdadeiras

selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00
```css
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
dados[selecao].shape[0]
```
- o operador & exige que todas as condições sejam verdadeiras

exemplo de formatação para apresentação
```css
print("Imóveis classificados como tipo 'Apartamento' ->{}".format(n1) )
```

