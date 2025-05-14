---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
Fixing the phone number column
[[concept-python-strings]] | [[concept-python-thefuzz-comparing-strings]]
```python
# replace '+' with '00'
phones['phone_number'] = phones['phone_number'].str.replace('+', '00')

# replace '_' with nothing
phones['phone_number'] = phones['phone_number'].str.replace('_', '')

# replace phone number whith lower than 10 digits to NAN

digits = phones['phone_number'].str.len()
phones.loc[digits < 10, 'phone number'] = np.nan
```

![[concept-python-assert-method]]

But what about more complicated examples?
```python
# replace letters with nothing

phones['phone_number'] = phones['phone_number'].str.replace(r'\D+', '')
```

