---
tags:
  - learning
HUB:
  - "[[hub-python]]"
created: "[[2024-03-13]]"
---
2024-03-13  18:41


- recall a lista [[python-list-comprehensions|comprehensions]]
	- `[2* num for num in range(10)]`
- return an object generetor
	- `(2* num for num in range(10))`

List comprehension - returns a list
Generators - returns a generator object
Both can be iterated over

```python
# Criando o gerador

gen = (num for num in range(30))

# Acessando o valor 10
for _ in range(11):  # Precisamos chamar next() 11 vezes para chegar ao valor 10
    valor = next(gen)

print(valor)  # Isso imprimirá 10
```


```python
def fibonacci_gerador(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

# Criando um objeto gerador
gen_fibonacci = fibonacci_gerador(50)

# Iterando sobre o gerador
for numero in gen_fibonacci:
    print(numero)

```

```python
# Create a list of strings

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']


# Define generator function get_lengths

def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)
# Print the values generated by get_lengths()
for value in get_lengths(lannister):

    print(value)
```

```python
# Extract the created_at column from df: tweet_time

tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time

tweet_clock_time = [entry[11:19] for entry in tweet_time]
# Print the extracted times

print(tweet_clock_time)
```



