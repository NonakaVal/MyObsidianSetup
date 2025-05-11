---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---


## extraindo dataframe como arquivo csv

exemplo do do dataframe filtrado em [[pandas-isin-method|dados_residencial]]:
```css
dados_residencial.to_csv('aluguel_residencial.csv', sep = ';', index = False)
```
- cria um arquivo csv na pasta base onde esta o nb, 
	- sep determina o parametro "; " para separação das colunas
		- "index = False" impede de o index seja importado com uma nova coluna


