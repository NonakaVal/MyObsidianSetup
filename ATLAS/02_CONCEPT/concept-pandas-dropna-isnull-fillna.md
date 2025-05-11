---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

1) criando um dataFrame
```css
import pandas as pd

imoveis = pd.DataFrame([['Apartamento', None, 970, 68], 
                        ['Apartamento', 2000, 878, 112], 
                        ['Casa', 5000, None, 500], 
                        ['Apartamento', None, 1010, 170], 
                        ['Apartamento', 1500, 850, None], 
                        ['Casa', None, None, None], 
                        ['Apartamento', 2000, 878, None], 
                        ['Apartamento', 1550, None, 228], 
                        ['Apartamento', 2500, 880, 195]], 
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])
```

2) Elimina os registros que não apresentam a variável Valor
```python
imoveis.dropna(subset = ['Valor'], inplace = True)
imoveis
```
- [dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html) é o método pandas para remover linhas ou colunas que tenham valores nulos ou ausentes
	- por padrão ou seja, sem chamar o parâmetro "subset", o método removerá todos os valores nulos do dataframe
		- com o parâmetro "subset" declarado passa a ser especificado onde será removido os valores nulos
			- inplace = True indica que a modificação deve ser feito no dataframe original


3) Elimina os imóveis do tipo Apartamento que não apresentam valor Condomínio
```css
selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
imoveis = imoveis[~selecao]
```
- seleção criada por [[concept-python-Pandas-DataFrame-Selection-Methods]] e método [isnull()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)


4) Substitui os valores faltantes que restam nas variáveis Condominio e IPTU por zero
```css
imoveis = imoveis.fillna({'Condominio': 0, 'IPTU': 0})
```
- método [fillna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) usado para sobrescrever os valores nulos 
	- os parâmetros são passados dentro do método
		- [[cmp-pandas-fillna-nullvalues-wrangling]]

5) Reconstrói o [[index]] do DataFrame resultante:
```css
imoveis.index = range(imoveis.shape[0])
imoveis
```

