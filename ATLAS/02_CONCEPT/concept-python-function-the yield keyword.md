---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---
### the "yield" keyword
- cria uma função geradora para criar um iterador,  

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print('hello')
    yield 42
    print('goodbye')

with my_context() as foo:
    print("foo is {}".format(foo))

```

```python
with my_context() as foo:
	print("foo is{}".format(foo))
```