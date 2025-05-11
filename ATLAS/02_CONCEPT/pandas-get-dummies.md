---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html
created: "[[30-01-2024]]"
---
2024-01-30 19:17

{{Objetivo do método}}
Utilizado para criar variáveis dummy ou variáveis indicadoras a partir de uma variável categórica, útil para converter uma coluna categórica em um conjunto de colunas binárias

![Imgur|1000](https://i.imgur.com/HYHl22S.png)

{{assinatura básica}}

```python
pandas.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)
```

{{parâmetros}}

- `data` - variável categórica a ser convertida em variáveis dummy
- `prefix` - prefixo a ser adicionado aos nomes das novas colunas dummy
- `prefix_sep` - separador entre o prefixo e o nome original da categoria
- `dummy_na` - se True, cria uma coluna dummy adicional para valores nulos
- `columns` - lista de colunas específicas a serem convertidas
- `sparse` - se True, retorna uma matriz dispersa em vez de um dataFrame denso
- `drop_first` - se True cria um k-1 dummies para k categorias removendo a primeira categoria

```python
import pandas as pd

def criar_dummies(dataset, colunas):
    """
    Converte colunas categóricas de um DataFrame em variáveis dummy e as converte para inteiros.

    Parâmetros:
    dataset (pd.DataFrame): O DataFrame original.
    colunas (list): Lista das colunas categóricas que precisam ser convertidas em variáveis dummy.

    Retorna:
    pd.DataFrame: O DataFrame atualizado com as colunas transformadas.
    """
    # Criar variáveis dummy e remover a primeira categoria para evitar multicolinearidade
    dataset[colunas] = pd.get_dummies(dataset[colunas], drop_first=True)
    
    # Converter as variáveis dummy para inteiros
    dataset[colunas] = dataset[colunas].astype(int)
    
    return dataset

```