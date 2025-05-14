---
tags:
  - learning
  - learning/review
HUB:
  - "[[hub-python]]"
---
# Python Sequence Structures

## 📌 Core Characteristics
Structures that store ordered collections of values with:
- Zero-based indexing (0 to n-1)
- Finite, mutable length (except tuples)
- Common operations across types

## 🔄 Common Sequence Operations
[[concept-python-string-operations|Sequence Operations]]
```python
x in s        # Membership test
s1 + s2       # Concatenation  
s * n         # Repetition
s[i]          # Indexing
s[i:j:k]      # Slicing
len(s)        # Length
min(s)/max(s) # Extremes
s.count(x)    # Occurrences
```

## 📝 Text Sequences
[[concept-python-strings|String Manipulation]]
```python
"Hello".lower()       # 'hello'
"text".upper()        # 'TEXT'
"a,b,c".split(",")    # ['a', 'b', 'c']
```

## 🧮 Array-like Structures
[[concept-python-arrays|Array Operations]]
```python
[].append(x)          # Add to end
[].insert(i, x)       # Insert at position
[].pop()              # Remove last
sorted([3,1,2])       # [1,2,3]
list(map(lambda x: x*2, [1,2,3]))  # [2,4,6]
```

## 🔒 Immutable Sequences
[[concept-python-tuplas|Tuples]]
```python
# Tuple unpacking
person = ("Gabriel", 27, True)
name, age, is_admin = person  # Destructuring
```

## 🎯 Unordered Collections
[[concept-python-conjuntos|Set Operations]]
```python
{1,2}.union({3})        # {1,2,3}
{1,2}.intersection({2,3}) # {2}
{1,2}.difference({2})    # {1}
```

## 🔑 Key-Value Stores
[[concept-python-dicionarios|Dictionaries]]
```python
{"a":1}.items()    # [('a', 1)]
{"a":1}.keys()     # ['a']
{"a":1}.values()   # [1]
```

## ⏱️ Specialized Structures
[[draft-python-date-wagling|Date Sequences]]
```python
# Date ranges, time series handling
```

## 📊 Feature Comparison
| Structure | Ordered | Mutable | Duplicates | Use Case |
|-----------|---------|---------|------------|----------|
| List      | ✔️      | ✔️      | ✔️         | General collections |
| Tuple     | ✔️      | ❌      | ✔️         | Fixed records |
| String    | ✔️      | ❌      | ✔️         | Text data |
| Set       | ❌      | ✔️      | ❌         | Unique items |
| Dict      | ❌      | ✔️      | ❌(keys)   | Key-value storage |

> **Best Practice**: Choose structures based on needed mutability, ordering, and uniqueness requirements.
```

Key improvements:
1. Added clear section headers with icons
2. Organized by structure type and characteristics
3. Included practical code examples for each
4. Added a comparison table
5. Maintained all original links
6. Improved visual hierarchy
7. Added type-specific best practices
8. Enhanced readability while preserving technical accuracy
9. Standardized formatting
10. Added context for when to use each structure