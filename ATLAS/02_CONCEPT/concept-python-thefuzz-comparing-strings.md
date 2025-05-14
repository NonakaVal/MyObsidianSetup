---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---

###  Comparing strings

Minimum edit distance

```python
# simple string comparison
# lets us compare between two strings

from thefuzz import fuzz

# compare reeding vs reading
fuzz.WRatio('reeding', 'reading')
```

```python
# Comparison with arrays
from thefuzz import process
# Define string and array of possible matches
string = "Houston Rockets vs Los Angeles Lakers"
choices = pd.Series([' Rockets vsLakers', 'Lakersvs Rockets' ,'HOUSOn vs Los Angeles' ,'Heat vs BUIIS'])
process.extract(string, choices, limit = 2)
```

Collapsing all of the state
```python
# For each correct category
for state in categories['state']:
	# Find potential matches in states with typoes
	matches = process.extract(state, survey['state'], limit = survey.shape[0])
	# For each potential match match
	for potential_match in matches:
		# If high similarity score
		if potential_match[1]>= 80:
		# replace typo with correct category 
		survey.loc[survey['state'] == potential_match[0], 'state'] = state
```

```python
# Iterate through categories

for cuisine in categories:  
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))
  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['cuisine_type'] == match[0], 'cuisine_type'] = cuisine
# Inspect the final result

print(restaurants['cuisine_type'].unique())
```

