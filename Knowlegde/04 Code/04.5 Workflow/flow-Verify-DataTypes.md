---
tags:
  - learning
  - component
subject:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---



# [[pandas-astype-method]]

```python
# Remove $ from revenue column and convert to integer
sales['revenue'] = sales['revenue'].str.strip('$')  # remove o símbolo '$'
sales['revenue'] = sales['revenue'].astype('int')
```

## Related Methods
- [[! py convert_currency(series, symbol='$', decimals=True)|Corrigindo valores monetários com astype]]
- [[! py validate_dtype(series, expected_dtype)]]
- [[! py to_numeric_safe(series)]]
- [[! py  check_nulls(series, raise_error=False, threshold=0)]]

# [[concept-python-assert-method]]
```python
# Verify that column is now integer type
assert sales['revenue'].dtype == 'int'
```

## Type Conversion
> [!numeric or categorical]
> ```python
> # Convert to categorical
> df['marriage_status'] = df['marriage_status'].astype('category')
> ```

