---
created: "[[2025-05-10]]"
tags:
  - snippet
HUB:
  - "[[hub-python]]"
connections:
  - "[[index-Verify-DataTypes|index-Verify-DataTypes]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}
Converter valores monetários de strings para numericos


# {código}

## PRIMEIRA FUNÇÃO - {date}

```python
def convert_currency(series, symbol='$', decimals=True):
    """
    Convert currency string to numeric value.
    
    Parameters:
        series (pd.Series): Series containing currency values
        symbol (str): Currency symbol to remove (default '$')
        decimals (bool): Whether to keep decimals (default True)
    
    Returns:
        pd.Series: Converted numeric values
    """
    dtype = float if decimals else int
    return (
        series.str.replace(f'[{symbol},]', '', regex=True)
        .astype(dtype)
    )

# Usage:
# df['price'] = convert_currency(df['price'], symbol='€')

```