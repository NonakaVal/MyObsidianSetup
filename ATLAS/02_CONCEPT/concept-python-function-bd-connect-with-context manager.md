---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---
###  conectando a um banco de dados com context manager

```python
from contexlib import contextmanager
import prosgres

@contextmanager
def database(url):
	db = posgres.connect(url)
	try:
		yiel db
	finally:
		db.disconnect()

url = "link do db"
with database(url) as my_db:
	course_list = my_db.execute('SELECT * FROM courses')
```