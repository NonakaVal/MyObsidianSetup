---
created: "[[2025-05-10]]"
tags:
  - snippet
HUB:
  - "[[hub-data-wrangling]]"
connections:
  - "[[flow-Verify-DataTypes|flow-Verify-DataTypes]]"
  - "[[pandas-series|pandas-series]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

Verificar se os tipos de dados presentes em uma serie-variavel está correto

# {código}

## PRIMEIRA FUNÇÃO - {date}

```python

def validate_dtype(series, expected_dtype):
    """
    Validate if series has expected dtype.
    
    Parameters:
        series (pd.Series): Series to validate
        expected_dtype (str/dtype): Expected dtype (e.g., 'int', 'float', 'category')
    
    Raises:
        TypeError: If dtype doesn't match
    """
    if not pd.api.types.is_dtype(series.dtype, expected_dtype):
        raise TypeError(f"Expected {expected_dtype}, got {series.dtype}")

# Usage:
# validate_dtype(df['age'], 'int')


```