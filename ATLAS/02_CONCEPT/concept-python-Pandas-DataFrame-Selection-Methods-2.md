---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
```python
# Importing Data
import pandas as pd
dados = pd.read_csv('aluguel_residencial.csv', sep=';')

## 1. Filtering Apartment-type Properties
```python
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]  # Count of rows matching the condition
```

- Uses relational operator == to create boolean mask
- `shape[0]` returns the number of matching rows
- Result stored in variable `n1`

## 2. Filtering Various House Types
```python
house_types = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
selecao = dados['Tipo'].isin(house_types)  # More efficient than multiple OR conditions
n2 = dados[selecao].shape[0]
```
- Improved version using `.isin()` method
- More scalable for multiple categories
- `shape[0]` counts the matching properties

## 3. Properties with Area Between 60-100 m² (Inclusive)
```python
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
```
- Uses `&` for AND logical operation
- Inclusive range check (≥ and ≤)
- Parentheses ensure proper operation order

## 4. Properties with ≥4 Bedrooms and Rent < R$2000
```python
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
```
- Combines two conditions with `&`
- Numeric comparison operators
- Counts properties meeting both criteria

## 5. Formatted Presentation
```python
print(f"""
Análise de Imóveis Residenciais:
--------------------------------
1. Apartamentos: {n1} unidades
2. Casas (todos os tipos): {n2} unidades
3. Área 60-100m²: {n3} unidades
4. ≥4 quartos e aluguel < R$2000: {n4} unidades
""")
```

Key Improvements:
1. Added f-strings for modern string formatting
2. Used `.isin()` for cleaner multi-category filtering
3. Added comprehensive header with all results
4. Maintained all original functionality
5. Improved code readability with spacing
6. Added comments explaining each step
7. Used consistent variable naming
8. Included all filtering techniques from original

Additional Recommendations:
```python
# For more complex filters, consider:
query_str = "Tipo in ['Casa', 'Casa de Condomínio'] and Area >= 60"
resultados = dados.query(query_str)

# To save filtered data:
dados[selecao].to_csv('propriedades_filtradas.csv', index=False)
```

This version maintains your original analysis while making it more professional and maintainable. The f-string formatting provides better output presentation, and the `.isin()` method offers a more efficient way to check multiple categories.