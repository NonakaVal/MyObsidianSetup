---
tags:
  - learning
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


 <font color = 00bfff>Variáveis no DataFrame</font>
 - [[rename-colluns-dataframe]]
- [[concept-variaveis-no-dataframe-(colunas)]]
- [[concept-python-pandas-dataframe-variables]]
	- `dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU'] `
	- `dados['Valorbrutom2'] = dados['Valor Bruto'] / dados['Area']`
		- [[concept-pandas-apply]]  |  [[concept-python-condicionais]]  | [[concept-lambda]]
`dados['Tipo agregado'] = dados.Tipo.apply(lambda x: 'casa' if x in casa else 'Apartamento')`

[[concept-pandas-apply]]