---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.concat.html
created: "[[30-01-2024]]"
---
2024-01-30 19:08

{{Objetivo do método}}
utilizado para concatenar dois ou mais DataFrames ao longo de um eixo específico, horizontal ou vertical

![Imgur](https://i.imgur.com/pGz6l2u.png)

{{assinatura básica}}

```python
pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)
```

{{parâmetros}}

- `objs` - uma lista ou dicionário de DataFrame a serem concatenados
- `axis` - o eixo ao longo do qual a concatenação será realizada
- `join` - tipo de junção a ser realizada (outer, ou inner)
- `ignore_index` - se True, ignora os índices existentes e gera um novo indice
- `keys` - adiciona rótulos de nivel superior ao longo do eixo de concatenação 
- `levels`, `names` - níveis e nomes de rótulos de níveis para serem usados com multindex
- `verify_integrity` - se True verifica se há sobreposição de indices ao longo do eixo
- `sort` - se True, ordena as chaves de nível
- `copy` - se False, evita copiar dados