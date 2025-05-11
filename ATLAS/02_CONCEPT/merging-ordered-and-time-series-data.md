---
tags:
  - learning/review
HUB:
  - "[[hub-logic]]"
  - "[[hub-python]]"
---

- [[pandas-merge_ordered-method]] 

- merge_asof() method
```python
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time', suffixes=('_jpm', '_bac'), direction='nearest')
```

[[pandas-query-method]]
```python
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')
```

[[pandas-melt]]