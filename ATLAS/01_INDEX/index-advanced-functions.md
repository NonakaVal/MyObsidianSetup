---
tags:
  - learning
  - tocomplete/explicar
HUB:
  - "[[hub-python]]"
---

# Python Iterators and Generators

## 🔄 Iterators
[[draft-introduction-to-iterators|Introduction to Iterators]]
```python
# Basic iterator protocol
my_iter = iter([1, 2, 3])
next(my_iter)  # 1
next(my_iter)  # 2

# Common iterator tools
for i, val in enumerate(['a', 'b', 'c']):
    print(f"Index {i}: {val}")

for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
    print(f"{x} -> {y}")
```

[[using-iterators-to-load-large-files-into-memory|Memory-Efficient File Loading]]
```python
# Process large files without loading entirely
with open('huge_file.txt') as f:
    for line in iter(f.readline, ''):
        process(line)
```

## 🧩 List Comprehensions
[[python-list-comprehensions|Powerful List Creation]]
```python
# Basic comprehension
squares = [i**2 for i in range(10)]  # [0, 1, 4, 9, 16,...]

# Generator expression (memory efficient)
squares_gen = (i**2 for i in range(10))  # Returns generator object
```

## 🌟 Generators
[[draft-introduction-to-generator-expressions|Generator Expressions]]
```python
# Simple generator
numbers = (num for num in range(30))

# Generator function with yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

## 🛠️ Practical Applications
[[snip-pandas-groupby-function|GroupBy Iteration]]
```python
# Iterating through groups
grouped = df.groupby('category')
for name, group in grouped:
    process_group(name, group)
```

## Key Differences
| Feature        | List Comprehension | Generator Expression |
|---------------|--------------------|----------------------|
| Memory Usage  | High (creates list) | Low (yields items) |
| Evaluation    | Eager              | Lazy               |
| Reusability   | Multiple iterations | Single iteration   |
| Syntax        | [x for x in seq]   | (x for x in seq)   |

> **Pro Tip**: Use generators for memory-intensive operations and list comprehensions when you need immediate access to all items.
```

Key improvements:
1. Organized into clear sections
2. Added practical code examples
3. Included comparison table
4. Maintained all original links
5. Added visual hierarchy with emojis
6. Included memory usage considerations
7. Added generator function example
8. Improved readability with proper spacing
9. Added professional tips
10. Preserved all technical content while making it more accessible