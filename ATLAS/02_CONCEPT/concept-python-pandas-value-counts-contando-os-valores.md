---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---
Frequência e percentuais com [[python-unique-value_counts-method|value_counts]]()

[[cmp-pandas-importing-data|-dados]] como csv:
```css
import pandas as pd 
dados = pd.read_csv('dados.csv')
```
- dados demográficos referentes a distribuição de renda por sexo, etimologia, dados de altura etc. 

```css
frequencia = dados.Sexo.value_counts()
percentual = dados.Sexo.value_counts(normalize = True) * 100

dist_freq_quali = pd.DataFrame({'Fraquencia': frequencia, ' Porcentagem(%)':percentual})
dist_freq_quali.rename(index = {0: 'Masculino', 1:'Feminino'}, inplace = True)

dist_freq_quali.rename_axis('Sexo', axis = 'columns', inplace = True)
```
- método de [[python-unique-value_counts-method|-value_counts]] com parâmetro 'normalize = 'True' multiplicado por 100 para frequência e percentuais
	- [[concept-python-pandas-dicionario-para-dataframe]] com os parâmetros de 'frequencia' e 'percentual'
		- método [[concept-python-describe|rename]] para nomear o indice
