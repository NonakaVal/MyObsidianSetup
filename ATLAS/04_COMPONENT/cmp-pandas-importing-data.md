---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
### Importar pandas e ler arquivo.
```python

import pandas as pd
notas = pd.read_csv("ratings.csv") 
notas.head()
```
- Importar a biblioteca pandas com o nome pd
	- Variável "notas" onde armazenamos a biblioteca pandas (pd) usada para ler tipo de arquivo "csv" , selecionando o caminho do arquivo dentro do ("")
- Notas.head é um comando de imprime no console as 5 primeiras informações guardadas do dataframe "ratings.csv" que está armazenado no "notas"

###  seperar colunas . sep
- "alt" + "tab" te permite ter acesso a metadados sobre o arquivo e regras de separação de colunas etc.
```css
import pandas as pd

dados = pd.read_csv("aluguel.csv", sep";")
```
-  o arquivo passa a separar as colunas por ";"

![[concept-importando-outros-tipos-de-arquivos]]


![[concept-dataframe-para-csv]]

