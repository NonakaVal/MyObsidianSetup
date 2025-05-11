---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
created: "[[17-01-2024]]"
---


capitalization - strings uppers and downs

```python
# capitalize

marriege_status['marriege_status'] = marriege_status['marriege_status'].str.upper()

# lowercase
marriege_status['marriege_status'] = marriege_status['marriege_status'].str.lower()
marriege_status['marriege_status'].value_counts()

```

trailing spacing

```python
# Strip all spaces
demographics = demographics['marriege_status'].str.strip()
```
