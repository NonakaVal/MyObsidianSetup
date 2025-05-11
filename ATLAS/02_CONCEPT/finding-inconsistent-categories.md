---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

```python
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])
```

```python
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
inconsistent_data = study_data[inconsist_rows]
```

```python
# drop inconsistent categories
consistent_data = study_data[~inconsist_rows]
```








