---
tags:
  - learning/review
  - learning/review
HUB:
  - "[[hub-descriptive-analysis]]"
  - "[[hub-statistic]]"
---
- [[concept-percentis]] | [[removendo-outliers]]
	- `q1 = valor.quantile(.25)`
	- `q3 = valor.quantile(.75)`
- `dados.Renda.quantile([i / 10 for i in range(1, 10)])`

```python
# Calculate total co2_emission per country: emissions_by_country

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr


# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]

print(outliers)
```
