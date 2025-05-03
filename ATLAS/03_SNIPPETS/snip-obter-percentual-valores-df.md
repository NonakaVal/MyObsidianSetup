---
created: "[[2025-04-30]]"
tags:
  - snippet
HUB:
  - "[[hub-tratamento-de-dados]]"
connections:
  - "[[Atlas/02_CONCEPT/ATLAS/percentis.md|percentis]]"
  - "[[Atlas/02_CONCEPT/ATLAS/frequencia-e-percentuais.md|frequencia-e-percentuais]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

obter valores percentuais e proporções do df
# {códigos}

## pandas `value_counts` e `cut`

```python
import pandas as pd

def calcular_percentual_por_faixa(dados, coluna, classes, labels):
    """
    Categoriza os dados com base em intervalos, calcula o percentual de ocorrências em cada categoria,
    e retorna os percentuais arredondados.

    Parâmetros:
    dados (pd.DataFrame): DataFrame contendo os dados.
    coluna (str): Nome da coluna que será categorizada.
    classes (list): Lista de limites para as categorias.
    labels (list): Lista de rótulos para as categorias.

    Retorna:
    pd.Series: Percentual de ocorrências em cada categoria.
    """
    # Categoriza a coluna com base nas faixas especificadas
    percentual = pd.value_counts(
        pd.cut(x = dados[coluna], bins = classes, labels = labels, include_lowest = True),
        normalize = True 
    ) * 100
    
    # Arredonda os percentuais para duas casas decimais
    percentual = percentual.round(2)
    
    return percentual
```