---
created: '[[2025-05-10]]'
tags:
  - snippet
HUB: 
connections:
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

Converte variável de um df para categórico 

# {código}

## PRIMEIRA FUNÇÃO - {date}

```python

def to_categorical(series, categories=None, ordered=False):
    """
    Convert to categorical with optional categories.
    
    Parameters:
        series (pd.Series): Series to convert
        categories (list): Optional predefined categories
        ordered (bool): Whether categories are ordered
    
    Returns:
        pd.Series: Converted categorical series
    """
    return series.astype(
        pd.CategoricalDtype(categories=categories, ordered=ordered)
    )

# Usage:
# df['grade'] = to_categorical(df['grade'], categories=['A','B','C','D','F'])

```