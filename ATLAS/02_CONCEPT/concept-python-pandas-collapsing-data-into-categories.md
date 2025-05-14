---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---


```python
# using qcut()
import pandas as pd
group_names = ['0-200k','200k-500k','500k+']

demographics['income_group'] = pd.qcut(demographics['household_income'], q =3,
									  labels = group_names)

# print income_group column
demographics[['income_group',-'housesold_income']]
```

```python
# using cut() - create category ranges and names

ranges = [0,200000, 500000, np.inf]
group_names = ['0-200k','200k-500k','500k+']

# create income group column

demographics['income_group'] = pd.cut(demographics['household_income'], bins =ranges,
									  labels = group_names)

demographics[['income_group',-'housesold_income']]
```

reducing categories in categorical column
operating_system colum is: 'Microsoft , 'Android', 'Linux'' 'MacOS', 'IOS' ,

operating_system column should become: 'Desktop0S' , 'mobileOS'

```python
# create mapping dictionary and replace

mapping = {'Microsoft: DesktopOS', 'MacOS':'DesktopOS', 'Linux': 'DesktopOS',
		   'IOS':'MobileOS','Android':'MobileOS'}
devices['operating_system'] = devices['operating_system'].replace(mapping)
devices['operating_system'].unique()
```
