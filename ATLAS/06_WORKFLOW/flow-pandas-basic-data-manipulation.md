---
tags:
  - resources
  - learning/review
  - concept
  - workflow
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
created: "[[07-02-2024]]"
---
[Pandas](https://pandas.pydata.org/docs/reference/index.html)
##### Start
### [[importando-outros-tipos-de-arquivos]]
- `import as pd` , `pd.read_` , `to_csv`

### [[concept-python-pandas-series-and-dataframe]]
- `pd.DataFrame()` , `to_frame`
 - [[rename-colluns-dataframe]] :  `df.columns = ['name1','name2']`

### <font color = 00bfff> Manipulação e Organização de Dados</font>
- [[organizando-dataframe]] : `sort_index` , `sort_values`
-  : `.index`   `reset_index`
- [[concat]] : `pd.concat()`
- [[split]] : `palavras = frase.split()`
- [[concept-python-pandas-loc-iloc-method-selection]] :  `loc[]` , `iloc[]`
- [[concept-pandas-isin]] : `selecao  = dados.Bairro.isin(bairros)` , bairros = lista de itens
- [[pandas-query-method]] : `resultado = df.query('idade > 30 and sexo == "Feminino"')`
### <font color = 00bfff> Tratamento de Valores Faltantes</font>
- [[concept-pandas-dropna-isnull-fillna]] : 
	- `df.dropna(subset = ['variável'], inplace = True)`
	- `selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())`
		- `imoveis = imoveis[~selecao]` 
- [[cmp-pandas-fillna-nullvalues-wrangling]] : `s.fillna(method = 'ffill')`, `s.fillna(method = 'bfill')`
### <font color = 00bfff> Manipulação e Análise de Dados</font>
- [[python-variable-types|data-types]]: `info()` , `dtype` , `name` , `shape`
- [[cmp-pandas-groupby-method]] : `df.groupby(by=coluna_ou_colunas)` , `df.groupby("Categoria")["Vendas"].sum()`
- [[concept-pandas-apply]] : `dataframe.apply(func, axis = 0)`
### <font color = 00bfff> Análise Estatística e Descritivas</font> - [[concept-statistic-descritivas]]

- [[concept-python-describe]] : `describe()` , `aggregate()` , `rename()`
- [[pandas-crosstab-method]] : `tabela_cruzada = pd.crosstab(dados['Sexo'], dados['Cor'])`
- [[concept-python-pandas-cut]] : `pd.cut(x, bins, labels=None, right=True, include_lowest=False)`
- [[concept-histograma-pandas]] : `notas.nota.plot(kind='hist')`

[[pre-tratamento]]
[[lista-tratamento-dados-1]]
[[lista-tratamento-dados-2]]