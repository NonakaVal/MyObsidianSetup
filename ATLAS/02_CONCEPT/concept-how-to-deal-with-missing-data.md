---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


Simple approaches:
1. Drop missing data
2. Impute with statistical measures (mean, median, mode..)
More complex approaches:
1. Imputing using an algorithmic approach
2. Impute with machine learning models

``` python
# drop missing values 
airquality_dropped = airquality.dropna(subset = ['CO2'])

# replacing with statistical measures 
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2':co_2mean})
```


treating null one
```python
# Print number of missing values in banking

print(banking.isna().sum())

# Visualize missingness matrix

msno.matrix(banking)

plt.show()
# Isolate missing and non missing values of inv_amount

missing_investors = banking[banking['inv_amount'].isna()]

investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize

banking_sorted = banking.sort_values(by = 'age')

msno.matrix(banking_sorted)

plt.show()
```

