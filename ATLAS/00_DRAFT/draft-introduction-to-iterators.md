---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
created: "[[2024-03-13]]"
---
2024-03-13  18:30

### iter() > next()
`iter()` > `next()`

``` python
# Criando uma lista
frutas = ['maçã', 'banana', 'uva']

# Criando um iterador a partir da lista
iterador_frutas = iter(frutas)

# Obtendo o próximo elemento do iterador
print(next(iterador_frutas))  # Saída: maçã

# Obtendo o próximo elemento do iterador
print(next(iterador_frutas))  # Saída: banana

# Obtendo o próximo elemento do iterador
print(next(iterador_frutas))  # Saída: uva

# Obtendo o próximo elemento do iterador
# Isso levanta uma exceção StopIteration, indicando que não há mais elementos
# a serem iterados.
print(next(iterador_frutas))  # Saída: StopIteration
```
### Playing with iterators

`enumarate()` -  `zip()`

```python
# Create a list of strings: mutants
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))  

# Print the list of tuples
print(mutant_list)  

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
```

```python
# Create a list of tuples: mutant_data

mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# reate a zip object using the three lists: mutant_zip

mutant_zip = zip(mutants, aliases, powers)
# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for mutant, alias, power in mutant_zip:

    print(mutant, alias, power)
```

### Using iterators to load large files into memory

There can be too much data to hold in memory

pandas 

`chunksize`

```python
# Initialize an empty dictionary: counts_dict

counts_dict = {}

fn = 'https://assets.datacamp.com/production/course_1342/datasets/tweets.csv'
from urllib.request import urlretrieve
urlretrieve(fn, 'tweets.csv')

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary

print(counts_dict)
```


```python
# Define count_entries()

def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}  

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
                
    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')
# Print result_counts

print(result_counts)
```

