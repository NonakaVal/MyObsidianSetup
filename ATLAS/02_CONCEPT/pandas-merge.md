---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.merge.html
created: "[[30-01-2024]]"
---
2024-01-30 18:55

{{Objetivo do método}}

Combinar dois DataFrames com base em uma ou mais colunas

![Imgur](https://i.imgur.com/yW4R5kB.png)

{{assinatura básica}}

```python
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, suffixes=('_x', '_y'), sort=False, copy=True, indicator=False, validate=None)

```

{{parâmetros}}

- `left` - o Dataframe à esquerda da operação
- `right` - o Dataframe à direita da operação
- `how` - o tipo de função a ser realizad (left, right, outer ou inner)
- `on` - nome das colunas que serão usadas como chaves para junção
- `left_on` - `right_on` - colunas do df a esquerda ou direita a serem usadas como chaves
- `left_index` - `right_index` - se True, usada o indice do dataFrame a esquerda ou a direita como chave
- `suffixes` - sufixos a serem adicionados aos nomes de coluna sobrepostos
- `sort` - se True ordena os resultados pela coluna de junção
- `copy` - se False, evita copiar os dados se possível
- `indicator` - se True adiciona uma coluna `_merge` indicando a fonte dos dados
- `validate` - string que especifica se a junção é `one_to_one`, `one_to_many` etc.