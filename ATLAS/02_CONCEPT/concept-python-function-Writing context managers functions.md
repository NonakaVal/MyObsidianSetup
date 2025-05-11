---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---
### Writing context managers functions

```python
@contextlib.contextmanager
def my_context():
	# add any set up code you need
	yeild
	# any teardown code you need
	
```