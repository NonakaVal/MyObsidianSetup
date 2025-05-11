---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
created: "[[2024-03-13]]"
---
2024-03-13  18:37

# List comprehensions

dobrar valor produtos
método comum
```python
lista = [500,1500,2000, 100]

nova_lista = []

for preco in lista:
	nova_lista.append(preco * 2)
```

método list comprehensions
```python
nova_lista = [preco * 2 for preco in precos]
```

```python
# Create list comprehension: squares

squares = [i**2 for i in range(0,10)]
```

```python
# Create a 5 x 5 matrix using a list of lists: matrix

matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix

for row in matrix:

    print(row)
```

- with conditional

```python
# Create a list of strings: fellowship

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship

new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list

print(new_fellowship)
```

```python
# Create a list of strings: fellowship

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship

new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list

print(new_fellowship)
```

```python
# Create a list of strings: fellowship

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary

print(new_fellowship)
```
