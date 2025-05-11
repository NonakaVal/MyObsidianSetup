---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
2024-01-09  16:45

### Converting strings to numbers
- remove commas values
- convert to float
- create columns converting currency

- `ps.Series.str.replace()`
	- [[concept-python-cleaning-text-data]]
		- [[index-Verify-DataTypes]]

Adding summary statistics into a DataFrame
- [[cmp-pandas-groupby-method]]

`salaries.groupby('company_size')['salary_usd'].mean()`

- [[concept-lambda]]

![Imgur](https://i.imgur.com/TXIlshc.png)


`salaries['std_dev'] = salaries.groupby('experience')['salary_usd'].transform(lambda x : x.std())`

# exemplos

```python
# Preview the column

print(planes["Duration"].head())
# Remove the string character

planes["Duration"] = planes["Duration"].str.replace("h", "")
# Convert to float data type

planes["Duration"] = planes["Duration"].astype(float)
# Plot a histogram

sns.histplot(data = planes, x = 'Duration')

plt.show()
```

### Handling outliers
- [[concept-statistic-python-pandas-outliers]] | [[removendo-outliers]]

```python
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]
print(planes["Price"].describe())
```

