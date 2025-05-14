---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---

######  Armazenar em variáveis

- [[cmp-pandas-importing-data]]
	- arquivo armazenado na variável "mdb"

``` css
total_linguas = mdb["original_language"].value_counts()
total_geral = total_linguas.sum()
total_ingles = total_linguas.loc["en"]
total_resto = total_geral - total_ingles
```
- variável "total_linguas" armazena uma lista criada com [[python-unique-value_counts-method|value_counts]] 
	- ".sum" é usado para calcular todos os valores numa série pandas, nesse caso calcula todos os valores armazenados na variável "total_linguas" em "total_geral"
	- ".loc[]" é usado para a contagem de ocorrência de um valor especifico em uma série nesse caso "en"
	- por fim o na variável "total_resto" é armazenado a operação "total_geral - total_ingles"

