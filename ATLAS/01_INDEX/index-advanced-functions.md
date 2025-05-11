---
tags:
  - learning
  - tocomplete/explicar
HUB:
  - "[[hub-python]]"
---
#### [[draft-introduction-to-iterators]]
- `iter()` , `next`
- `enumerate()` , `zip()`
- [[using-iterators-to-load-large-files-into-memory]]
#### [[python-list-comprehensions]]
 - `squares = [i**2 for i in range(0,10)]`
 - `squares = (i**2 for i in range(0,10))`  
#### [[draft-introduction-to-generator-expressions]]
 - `gen = (num for num in range(30))`
- `yield`
[[snip-andas-groupby-function]]


---

```python
import pandas as pd

tweets_df = pd.DataFrame({
    'lang': ['en', 'es', 'en', 'fr', 'es', 'en', 'fr', 'en']
})

def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count:
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)

```

