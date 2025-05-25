---
tags:
  - learning
  - walkthrough
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
created: "[[10-02-2024]]"
dg-publish: true
---
### [[possible-issues-w-categorical-data|Possíveis Problemas com Dados Categóricos]]

### [[flow-Verify-DataTypes|Verificando Tipos de Dados]]
- `sales['revenue'].srt.strip('$')`
- `sales['revenue'].astype('int')`

### [[how-to-deal-with-out-of-range-data|Tratando Dados Fora do Intervalo]]
- [[concept-pandas-dropna-isnull-fillna|Tratamento de Valores Faltantes]] | [[concept-pandas-drop_duplicates-method|Remoção de Duplicatas]]
	- `movies.loc[movies{'avg_rating'} > 5, ' avg_rating'] = 5`
	- `pd.to_datetime(user_signup['subscription_date']).dt.date`

### 🔍 [[concept-finding-inconsistent-categories|Identificando Categorias Inconsistentes]]
- `inconsistent_categories = set(df[column]).difference(df[column])`
	- `inconsistent_rows = df[column].isin(inconsistent_categories)`
		- `consistent_data = df[~inconsistent_rows]`

### [[make-sure-of-value-is--consistent|Garantindo Consistência dos Valores]]
- [[concept-estruturas-de-dados|Estruturas de Dados]] | [[concept-python-strings|Manipulação de Strings]]
	- `df[column].str.upper()`
	- `df[column].str.lower()`
	- `df[column].str.strip()`  # removendo espaços vazios

### [[concept-python-pandas-collapsing-data-into-categories|Agrupando Dados em Categorias]]
- [[concept-python-pandas-analysis-method-frequencia-e-percentuais|Análise de Frequências e Percentuais]] | [[concept-python-pandas-cut|Segmentação com cut]]
	- `pd.qcut`
	- `pd.cut(df[column], bins=ranges, labels=group_names)`

### [[concept-python-cleaning-text-data|Limpeza de Dados Textuais]]
- [[concept-python-strings|Manipulação de Strings]]
	- `df[column].str.replace('+', '00')`
	- `df[column].str.replace('_', '')`

### [[uniformity|Garantindo Uniformidade dos Dados]]
- `pd.to_datetime`, `infer_datetime_format=True`, `errors='coerce'`

### [[concept-python-cross-field-validation|Validação Cruzada de Campos]]

### [[concept-What-is-Missing-Data|O que é Dados Faltantes?]]
- [[concept-pandas-dropna-isnull-fillna|Tratamento de Valores Faltantes]] | [[matplotlib|Visualização de Dados com Matplotlib]]
	- (MCAR)(MAR)(MNAR)
	- `isna()`
	- `import missingno as msno`, `msno.matrix(df)`

### [[concept-how-to-deal-with-missing-data|Tratamento de Dados Faltantes]]
- [[cmp-pandas-fillna-nullvalues-wrangling|Preenchimento de Valores Faltantes com fillna]]

### [[concept-python-thefuzz-comparing-strings|Comparando Strings com TheFuzz]]
- `from thefuzz import fuzz`, `fuzz.WRatio('reeding', 'reading')`
- `from thefuzz import process`, `process.extract(string, choices, limit=2)`

### [[concept-record-linkage|Linkagem de Registros]]

### [[concept-python-pandas-linking-dataframes|Linkando DataFrames com Pandas]]
