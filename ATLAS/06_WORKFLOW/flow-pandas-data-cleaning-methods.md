---
tags:
  - learning
  - walkthrough
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
created: "[[10-02-2024]]"
---
### [[possible-issues-w-categorical-data]]

### [[index-Verify-DataTypes]]
- `sales['revenue'].srt.strip('$')`
- `sales['revenue'].astype('int')`

### [[how-to-deal-with-out-of-range-data]]
- [[concept-pandas-dropna-isnull-fillna]] | [[concept-pandas-drop_duplicates-method]]
	- `movies.loc[movies{'avg_rating'} > 5, ' avg_rating'] = 5`
	- `pd.to_datetime(user_signup['subscription_date']).dt.date`

### 🔍 [[finding-inconsistent-categories]]
- `inconsistent_categories = set(df[column]).difference(df[column])`
	- `inconsistent_rows = df[column].isin(inconsistent_categories)`
		- `consistent_data = df[~inconsistent_rows]`

### [[make-sure-of-value-is--consistent]]
- [[concept-estruturas-de-dados]] | [[strings]]
	- `df[column].str.upper()`
	- `df[column].str.lower()`
	- `df[column].str.strip()`  # removendo espaços vazios

### [[concept-python-pandas-collapsing-data-into-categories]]
- [[concept-python-pandas-analysis-method-frequencia-e-percentuais]] | [[concept-python-pandas-cut]]
	- `pd.qcut`
	- `pd.cut(df[column], bins=ranges, labels=group_names)`

### [[concept-python-cleaning-text-data]]
- [[strings]]
	- `df[column].str.replace('+', '00')`
	- `df[column].str.replace('_', '')`

### [[uniformity]]
- `pd.to_datetime`, `infer_datetime_format=True`, `errors='coerce'`

### [[concept-python-cross-field-validation]]

### [[concept-What-is-Missing-Data]]
- [[concept-pandas-dropna-isnull-fillna]] | [[matplotlib]]
	- (MCAR)(MAR)(MNAR)
	- `isna()`
	- `import missingno as msno`, `msno.matrix(df)`

### [[how-to-deal-with-missing-data]]
- [[cmp-pandas-fillna-nullvalues-wrangling]]

### [[concept-python-thefuzz-comparing-strings]]
- `from thefuzz import fuzz`, `fuzz.WRatio('reeding', 'reading')`
- `from thefuzz import process`, `process.extract(string, choices, limit=2)`

### [[generating-pairs]]

### [[concept-python-pandas-linking-dataframes]]
