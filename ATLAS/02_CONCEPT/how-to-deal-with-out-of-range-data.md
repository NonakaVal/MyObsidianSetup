---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---

[[concept-statistic-python-pandas-outliers]]
[[concept-pandas-dropna-isnull-fillna]]
 
1. drop data(take care of losing information)

```python
# droping using filfering

movies = movies[movies['avg_rating']<= 5]

# drop values using drop method

movies.drop(movies[movies['avg_rating'<= 5].index, inplace = True 

# convert avg_rating
movies.loc[movies{'avg_rating'} > 5, ' avg_rating'] = 5

assert movies['avg_rating'].max() <= 5

```

>[!datetime]
```python
# convert to time 
import datatime as dt
import pandas as pd
user_sigups.dtypes

today_date = dt.data.today()

user_sigups['subscription_date'] = pd.to_datetime(user_sugbnup['subscription_date']).dt.date

user_sigups.loc[user_sigups['subscription_date']> today_date, 'subscription_date'] = today

assert user_signups.subscriptin_date.max().date() <= today_date

```

duplicate values

[[concept-pandas-drop_duplicates-method]]   

```python
# finding duplicates

duplicates = height_weight.duplicates()
print(duplicates)

# column names to check for duplication

column_names = ['first_name', 'last_name', 'adress']

duplicates = height_weight.duplicated(subset= column_manes, keep = False)

# output duplicates

height_weigth[duplicates].sort_values(by = 'first_name')

height_weigth.drop_duplicates(inplace = True)
```

```python

# groupby and agg mothods

column_names = ['first_name', 'last_name', 'adress']
summaries = {'height:''max', 'weight': 'mean'}

height_weight = height_weight.groupby(by=column_names).agg(summaries).reset_index()

```

