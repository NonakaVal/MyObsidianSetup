---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
### cross field validation

the use of mulple fields in a dataset to sanity check data integrity

```python
sum_classes = flights[['economy_class',-'business_class',-'first_class']].sum(axis = 1)
passenger_equ = sum_classes == flights['total_passangers']

# Find and filter out rows whith inconsistent passenger totals

inconsistent_pass = flights[~passenger_equ]
consistent_pass = flights[passenger_equ]
```

```python
# convert to datatime and get todays date
users['birthday'] = pd.to_datetime(users['birthday'])
today = dt.date.today()

# for each row in the birthday column, calculate year difference 
age_manual = today.year - user['birthday'].dt.year

# find instances where ages match

age_equ = age_manual == users['age']

# find and filter out rows with inconsistent age

inconsitent_age = user[~age_aqu]
consistent_age = user[age_equ]

```

>[!What to do when we catch inconsistencies?]
>> Requires a deep undertending of the dataset
>> > - Droping data
>> > - Set to messing and impute
>> >- Apply rules from domain knowledge




