---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


[[concept-pandas-dropna-isnull-fillna]]


### exemplo 2

[[cmp-pandas-importing-data|importando]] arquivo csv:
```css
import pandas as pd

dados = pd.read_csv('aluguel_residencial.csv', sep = ';')
```

acessando informações úteis:
```css
dados.info()
```

encontrando valores nulos  na coluna "Valor" com método [isnull()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)
```css
dados[dados.Valor.isnull()].shape[0]
```

removendo valores nulos com [dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
```css
A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True)
B = dados.shape[0]
A - B
```
- é o método pandas para remover linhas ou colunas que tenham valores nulos ou ausentes
	- por padrão ou seja, sem chamar o parâmetro "subset", o método removerá todos os valores nulos do dataframe
		- com o parâmetro "subset" declarado passa a ser especificado onde será removido os valores nulos
			- inplace = True indica que a modificação deve ser feito no dataframe original
	- método na estrutura para ver a diferença da alteração


criando uma [[selecao-frequencia-1]] com [isnull()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html) para remover dados específicos:
```css
selecao = (dados.Tipo == 'Apartamento') & (dados.Condominio.isnull())
```
- operador [[concept-python-conjuntos|&]] exige que ambas as condições sejam atendidas para estarem na seleção

removendo dados nulos com base na seleção:
```css
A = dados.shape[0]
dados = dados[~selecao]
B = dados.shape[0]
A-B
```
- importante lembrar que a seleção isnull() cria uma série booleana onde True indica o valor nulo,
	- a função base com 'isnull' removerá todo os valores não nulos nessa função
		- podemos concertar isso com o sinal '~' antes da seleção 
			- ou usando a operação [notnull](https://pandas.pydata.org/docs/reference/api/pandas.notnull.html) que é diretamente oposta ao isnull()


substituindo valores com [fillna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
```css
dados = dados.fillna({'Condominio':0, 'IPTU':0})
```
- [[cmp-pandas-fillna-nullvalues-wrangling]]

