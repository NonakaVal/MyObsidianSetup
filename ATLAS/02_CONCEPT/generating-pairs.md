---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


### Generating pairs

Record linkage
```python
# Import recordlinkage
import recordlinkage

# Create indexing object
indexer = recordlinkage.Index()

# Generate pairs blocked on state
indexer. block('state')
pairs = indexer.index(census_A, census_B)

# Create a Compare object
compare_cl = recordlinkage.Compare()

# Find exact matches for pairs of date_of_birth and state
compare_cl.exact('date_of_birth', 'date_of_birth', label = 'date_of_birth')

# Find similar matches for pairs of surname and address_l using string similarity
compare_cl.string('surname', 'surname', threshold = 0.85, label = 'surname')

# Find matches
potential_matches = compare_cl.compute(pairs, census_A, census_B)

# finding the only pairs we want
potential_matches[potential_matches.sum(axis =1) =>2]
```
