---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
---
- permite que a [[concept-python-funcoes|funcao]] receba um número variado de argumentos posicionais

### Functions with variable-length arguments `(*args)`

```python
# Define gibberish

def gibberish(*args):

    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge

    hodgepodge = ''
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)



```
### Functions with variable-length keyword arguments `(**kwargs)`


```python
# Define report_status

def report_status(**kwargs):

    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key , value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)  

    print("\nEND REPORT")  

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing") 

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")
```


### another exemples


```python
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)
```
