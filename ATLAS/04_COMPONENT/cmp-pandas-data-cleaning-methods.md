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

### [[Verify-DataTypes]]
- `sales['revenue'].srt.strip('$')`
- `sales['revenue'].astype('int')`

### [[how-to-deal-with-out-of-range-data]]
- [[dropna-isnull-fillna]] | [[pandas-drop_duplicates-method]]
	- `movies.loc[movies{'avg_rating'} > 5, ' avg_rating'] = 5`
	- `pd.to_datetime(user_signup['subscription_date']).dt.date`

### 🔍 [[finding-inconsistent-categories]]
- `inconsistent_categories = set(df[column]).difference(df[column])`
	- `inconsistent_rows = df[column].isin(inconsistent_categories)`
		- `consistent_data = df[~inconsistent_rows]`

### [[make-sure-of-value-is--consistent]]
- [[estruturas-de-dados]] | [[strings]]
	- `df[column].str.upper()`
	- `df[column].str.lower()`
	- `df[column].str.strip()`  # removendo espaços vazios

### [[collapsing-data-into-categories]]
- [[frequencia-e-percentuais]] | [[cut]]
	- `pd.qcut`
	- `pd.cut(df[column], bins=ranges, labels=group_names)`

### [[cleaning-text-data]]
- [[strings]]
	- `df[column].str.replace('+', '00')`
	- `df[column].str.replace('_', '')`

### [[uniformity]]
- `pd.to_datetime`, `infer_datetime_format=True`, `errors='coerce'`

### [[cross-field-validation]]

### [[What-is-Missing-Data]]
- [[dropna-isnull-fillna]] | [[matplotlib]]
	- (MCAR)(MAR)(MNAR)
	- `isna()`
	- `import missingno as msno`, `msno.matrix(df)`

### [[how-to-deal-with-missing-data]]
- [[interpolacao-com-fillna()]]

### [[comparing-strings]]
- `from thefuzz import fuzz`, `fuzz.WRatio('reeding', 'reading')`
- `from thefuzz import process`, `process.extract(string, choices, limit=2)`

### [[generating-pairs]]

### [[linking-dataframes]]
