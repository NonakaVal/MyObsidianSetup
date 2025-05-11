---
tags:
  - learning
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---



# [[pandas-astype-method]]

```python
# Remove $ from revenue column and convert to integer
sales['revenue'] = sales['revenue'].str.strip('$')  # remove o símbolo '$'
sales['revenue'] = sales['revenue'].astype('int')
```

## Related Methods
- [[snip-convert-currency-string-to-numeric|Corrigindo valores monetários com astype]]
- [[snip-validate-series-datatype-in-dataframe]]
- [[snip-convert-pandas-df-var-to-numeric]]
- [[snip-null-Checker]]

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

