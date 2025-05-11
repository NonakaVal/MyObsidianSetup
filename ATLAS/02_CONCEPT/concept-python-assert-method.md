---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
---

```python
# Find length of each row in Phone number column
sanity_check = phone['phone_number'].str.len()

# Assert minmum phone number length is 10
assert sanity_check.min() >= 10

# Assert all numbers do not have '+' or '-'
assert phone['phone_number'].str.contains('+|-').any == False
```
