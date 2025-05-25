---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


### Linking DataFrames

Get the indices

```python
matches.index
# Get indices from census_B only

duplicate_rows = matches.index.get_level_values(1)

# Finding duplicates in census_B
census_B_duplicates = censos_B[census_B.index.isin(duplicate_rows)]

# Finding new rows in censos_B
census_B_duplicates = censos_B[~census_B.index.isin(duplicate_rows)]

# Link the DataFrames!
full_census = census_A.append(census_B_new)
```
