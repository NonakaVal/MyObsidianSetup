---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
created: "[[18-01-2024]]"
---
2024-01-18  13:55

##### Possible issues with categorical data
- inconsistent values: `"ham", "Ham"," ham"`
- misspelled values: `"Ham","Hma"`

Identifying issues
[[pandas-criando-intervalos]]
- `Series.cat.categories`
- `Series.value_counts()`

#### Fixing issues: whitespace
`dogs['get_along_gats'] = dogs['get_along_gats'].str.strip() `

Fixing issues: capitalization
`dogs['get_along_gats'] = dogs['get_along_gats'].str.title()`
- `upper() - lower()`

#### Fixing issues: misspelled words
[[collapsing-categories-setup]]
```python
replace_map = {"Noo": "No"}
dogs['get_along_gats'].replace(replace_map, inplace = True)
```
- convert to categorical

#### Using the str accessor object
[[pandas-converting-and-analyzing-categorical-data]]
`dogs['get_along_gats'].str.contains("Shepherd", regex = False)`

Accessing data with loc : [[concept-python-pandas-loc-iloc-method-selection]]

