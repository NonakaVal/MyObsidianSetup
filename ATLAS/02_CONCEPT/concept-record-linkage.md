---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
# Record Linkage Explained

Record linkage is the process of identifying and matching records that refer to the same entity across different datasets. Here's a detailed breakdown of the code:

## 1. Importing the Package
```python
import recordlinkage
```
The `recordlinkage` library provides tools for linking records from different sources.

## 2. Indexing (Blocking)
```python
indexer = recordlinkage.Index()
indexer.block('state')
pairs = indexer.index(census_A, census_B)
```
- **Why?** Comparing every record in A with every record in B is computationally expensive (O(n²))
- **Blocking** reduces comparisons by only matching records with the same state
- Creates candidate pairs that might be matches

## 3. Comparison Rules
```python
compare_cl = recordlinkage.Compare()
```
We create a comparison object to define our matching rules:

### Exact Matching
```python
compare_cl.exact('date_of_birth', 'date_of_birth', label='date_of_birth')
```
- Perfect match required for dates of birth
- Binary result (1=match, 0=no match)

### Fuzzy String Matching
```python
compare_cl.string('surname', 'surname', threshold=0.85, label='surname')
compare_cl.string('address_l', 'address_l', method='jarowinkler', threshold=0.80, label='address')
```
- Compares strings with similarity thresholds
- `threshold=0.85` means 85% similarity required
- `method='jarowinkler'` is good for names/addresses (accounts for typos)
- Returns similarity score between 0-1

## 4. Computing Matches
```python
potential_matches = compare_cl.compute(pairs, census_A, census_B)
```
- Applies all comparison rules to the candidate pairs
- Returns DataFrame with similarity scores for each pair

## 5. Filtering Matches
```python
high_confidence_matches = potential_matches[potential_matches.sum(axis=1) >= 2]
```
- `sum(axis=1)` adds up all similarity scores for each pair
- `>= 2` means we want pairs that match on at least 2 fields
- Adjust this threshold based on your data quality needs

## Practical Considerations

1. **Blocking Strategy**: 
   - Start with blocking on state/zipcode
   - For larger datasets, use `sortedneighbourhood` for names

2. **Threshold Tuning**:
   - Lower thresholds catch more matches (but more false positives)
   - Higher thresholds are more strict (but may miss true matches)

3. **Data Quality**:
   - Pre-clean data (standardize formats, remove typos)
   - Consider phonetic matching (Soundex) for names

4. **Validation**:
   - Manually review sample matches
   - Calculate precision/recall if you have ground truth

This approach is commonly used for:
- Merging customer databases
- Deduplication
- Historical record matching
- Data integration projects

Would you like me to explain any part in more detail?