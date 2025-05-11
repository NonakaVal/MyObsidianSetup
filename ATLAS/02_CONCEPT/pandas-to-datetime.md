---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
created: "[[07-02-2024]]"
---
2024-02-07 13:58

{{Objetivo do método}}
Converte objetos em formato de data e hora

{{assinatura básica}}

```python
pd.to_datetime(arg, errors='raise', format=None, infer_datetime_format=False, origin='unix', cache=True)
```

{{parâmetros}}

- `arg` - objeto a ser convertido para datetime, pode ser uma série, df. lista ou array
- `errors` - define como lidar com erros durante uma conversão, pode ser 'raise', 'coerce' ou ignore
- `format` - especifica o formato da data
- `infer_datetime_format` - se True, tenta inferir o formato da data automaticamente
- `origin` - defina a referencia para a data
- `cache` - se True, ativa o armazenamento em cache para melhorar o desempenho