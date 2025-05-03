---
tags:
  - learning/review
  - snippet
created: "[[2024-04-01]]"
hub:
  - "[[hub-python]]"
origin: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
connections:
  - "[[grouping-data-by-category-in-pandas]]"
---
Criar um agrupamento de variaveis de um dataframe

```python
import pandas as pd

def group_by(data, *args,**kwargs):
	grouped_data = data.groupby(list(args), **kwargs)
	return grouped_data
```

