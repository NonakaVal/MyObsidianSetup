---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

```python
# Identify inconsistent blood type categories between study data and reference categories
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])

# Create boolean mask for rows with inconsistent blood types
inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)

# Extract inconsistent data for review
inconsistent_data = study_data[inconsistent_rows]  # Fixed variable name typo (was inconsist_rows)

# Create clean dataset by excluding inconsistent rows
consistent_data = study_data[~inconsistent_rows]  # Fixed variable name typo (was inconsist_rows)

# Alternative one-liner for clean data
consistent_data = study_data[~study_data['blood_type'].isin(inconsistent_categories)]
```



Additional recommendations:
```python
# For production code, consider adding:
print(f"Found {len(inconsistent_data)} inconsistent records")
print("Problematic blood types:", inconsistent_categories)

# To save cleaned data:
consistent_data.to_csv('cleaned_blood_data.csv', index=False)
```