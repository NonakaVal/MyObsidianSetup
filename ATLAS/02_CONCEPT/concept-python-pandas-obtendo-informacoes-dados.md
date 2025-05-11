---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---

```python
type(dados)
dados.info()
```
- método "type()" define o tipo de qualquer objeto
	- método ".info()" fornece um resumo conciso, numero de linhas, nome das colunas, tipo de dados e quantidade de valores não nulos.

### .dtype

partindo de um dataframe válido. ex1
``` python
import pandas as pd

arquivo = pd.DataFrame({
	'coluna1':[1, 2, 3],
	'coluna2':[1.5, 1.8, 2.5],
	'coluna3':["A", "B", "C"],
	'coluna4':[True, False, True]
})

planilha = pd.DataFrame(arquivo.dtypes, columns = ["tipos de dados"])
planilha
```
- "arquivo" recebe e corverte o dicionário em um DataFrame
	- em seguida "planilha" cria outra DataFrame com base no primeiro "arquivo" e então aplica o metodo "dtypes", seguido de nomear a primeira coluna "tipos de dados"

### .name
- o resultado é uma coluna só com os tipos de dados nomeda ,
```python 
planilha.columns.name = "colunas"
planilha
```
 - atribui um nome para a coluna 

### .shape
```python
planilha.shape
```
- retorna as dimenções do DataFrame.
	- ex (4,5)
		- 4 colunas e 5 linhas


