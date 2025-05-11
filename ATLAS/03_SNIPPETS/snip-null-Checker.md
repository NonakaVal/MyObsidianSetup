---
created: "[[2025-05-10]]"
tags:
  - snippet
HUB:
  - "[[hub-tratamento-de-dados]]"
connections:
  - "[[Atlas/06_WORKFLOW/flow-pandas-null-values-wrangling.md|flow-pandas-null-values-wrangling]]"
  - "[[Atlas/04_COMPONENT/cmp-pandas-fillna-nullvalues-wrangling.md|cmp-pandas-fillna-nullvalues-wrangling]]"
  - "[[Atlas/02_CONCEPT/concept-pandas-dropna-isnull-fillna.md|concept-pandas-dropna-isnull-fillna]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

Verificar os valores nulos de uma variavel dataframe pandas


# {código}

## PRIMEIRA FUNÇÃO - {date}

```python

def check_nulls(series, raise_error=False, threshold=0):
    """
    Check for null values in series.
    
    Parameters:
        series (pd.Series): Series to check
        raise_error (bool): Whether to raise error if nulls found
        threshold (int): Maximum allowed null count
    
    Returns:
        int: Number of nulls
    """
    null_count = series.isna().sum()
    if raise_error and null_count > threshold:
        raise ValueError(f"Series contains {null_count} null values")
    return null_count

# Usage:
# nulls = check_nulls(df['email'], raise_error=True)

```