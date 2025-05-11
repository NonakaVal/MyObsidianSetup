---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_flags.html
created: "[[08-02-2024]]"
---
2024-02-08 11:14

{{Objetivo do método}}

Utilizado para configurar flags de comportamento
{{assinatura básica}}

```python
DataFrame.set_flags(copy=False, allows_duplicate_labels=None)
```

{{parâmetros}}

- `copy` - se True o df resultante sera uma cópia, se false o df pode compartilhar referencias com o original
- `allows_duplicates_labels` - se True, permite rotúlos duplicados