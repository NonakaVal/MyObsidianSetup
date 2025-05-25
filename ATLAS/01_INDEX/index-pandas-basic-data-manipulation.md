---
tags:
  - resources
  - learning/review
  - concept
  - workflow
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
created: "[[07-02-2024]]"
dg-publish: true
---
[Pandas](https://pandas.pydata.org/docs/reference/index.html)

##### Start
### [[concept-importando-outros-tipos-de-arquivos|Importação de Arquivos com Pandas]]
- `import as pd` , `pd.read_` , `to_csv`

### [[concept-python-pandas-series-and-dataframe|Series e DataFrame em Pandas]]
- `pd.DataFrame()` , `to_frame`
- [[rename-colluns-dataframe|Renomeando Colunas em DataFrame]] :  `df.columns = ['name1','name2']`

---

### <font color = 00bfff>Manipulação e Organização de Dados</font>
- [[concept-organizando-dataframe|Organizando DataFrames]] : `sort_index` , `sort_values`
- [[index-pandas-methods|Resetando e Acessando Índices]] : `.index` , `reset_index`
- [[concept-python-pandas-concat|Concatenando DataFrames com concat]] : `pd.concat()`
- [[concept-python-split|Dividindo Strings com split]] : `palavras = frase.split()`
- [[concept-python-pandas-loc-iloc-method-selection|Selecionando com loc e iloc]] : `loc[]` , `iloc[]`
- [[concept-pandas-isin|Filtrando com isin]] : `selecao  = dados.Bairro.isin(bairros)`
- [[pandas-query-method|Filtrando com query]] : `df.query('idade > 30 and sexo == "Feminino"')`

---

### <font color = 00bfff>Tratamento de Valores Faltantes</font>
- [[concept-pandas-dropna-isnull-fillna|Tratamento com dropna, isnull, fillna]] :
  - `df.dropna(subset = ['variável'], inplace = True)`
  - `selecao = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())`
  - `imoveis = imoveis[~selecao]`
- [[cmp-pandas-fillna-nullvalues-wrangling|Preenchendo Valores Faltantes com fillna]] : `s.fillna(method = 'ffill')`, `s.fillna(method = 'bfill')`

---

### <font color = 00bfff>Manipulação e Análise de Dados</font>
- [[python-variable-types|Tipos de Variáveis e Estrutura do DataFrame]]: `info()` , `dtype` , `name` , `shape`
- [[cmp-pandas-groupby-method|Agrupando Dados com groupby]] : `df.groupby("Categoria")["Vendas"].sum()`
- [[pandas-apply|Aplicando Funções com apply]] : `dataframe.apply(func, axis = 0)`

---

### <font color = 00bfff>Análise Estatística e Descritiva</font> - [[concept-statistic-descritivas|Estatísticas Descritivas com Pandas]]
- [[concept-python-describe|Resumo com describe e aggregate]] : `describe()` , `aggregate()` , `rename()`
- [[pandas-crosstab-method|Análise Cruzada com crosstab]] : `pd.crosstab(dados['Sexo'], dados['Cor'])`
- [[concept-python-pandas-cut|Segmentação com cut]] : `pd.cut(x, bins, labels=None)`
- [[concept-histograma-pandas|Plotando Histograma com Pandas]] : `notas.nota.plot(kind='hist')`

---

### Listas e Recursos de Apoio
- [[pre-tratamento|Pré-Tratamento de Dados]]
- [[lista-tratamento-dados-1|Checklist de Tratamento - Parte 1]]
- [[lista-tratamento-dados-2|Checklist de Tratamento - Parte 2]]
