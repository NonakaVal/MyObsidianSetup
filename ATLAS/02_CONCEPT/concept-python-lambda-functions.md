---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
---
[[concept-lambda]]

# Lambda functions
```python
# Create a list of strings: spells

spells = ["protego", "accio", "expecto patronum", "legilimens"] 

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells) 

# Print the result
print(shout_spells_list)
```


```python
# Create a list of strings: fellowship

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member : len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)
```
