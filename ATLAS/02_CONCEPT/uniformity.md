---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---


- Temerature, 
- weigt, date, money

>[!Treating temperature data]

## $C =(F -32)\times\frac59$

```python
temp_fah = temperatures.loc[temperatures['temperature'] > 40, 'temperature']
temp_cels = (temp_fah - 32) * (5/9)
temperatures.loc[temperatures['temperature'] > 40, 'temperature'] = temp_cels
```

```python
assert temperature['temperature'].max() < 40
```

Treating date data

```python
birthdays['birthday'] = pd.to_datetime(birthdays['birthday'], 
									  # attempt to infer format of each date
									  infer_datetime_format = True
									  #  return NA for rows where conversion failed
									  error = 'coerce')

# using dt.strftime

birthdays['birthday'] = birthdays['birthday'].dt.strftime('%d-%m%Y')
```

