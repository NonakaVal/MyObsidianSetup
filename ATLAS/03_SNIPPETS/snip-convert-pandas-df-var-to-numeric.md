---
created: '[[2025-05-10]]'
tags:
  - snippet
HUB: 
connections:
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}
converter uma coluna de um data-frame para numeric 


# {código}

## PRIMEIRA FUNÇÃO - {date}

```python

def to_numeric_safe(series):
    """
    Convert to numeric, coercing errors to NaN.
    
    Parameters:
        series (pd.Series): Series to convert
    
    Returns:
        pd.Series: Converted numeric series
    """
    return pd.to_numeric(series, errors='coerce')

# Usage:
# df['quantity'] = to_numeric_safe(df['quantity'])

```