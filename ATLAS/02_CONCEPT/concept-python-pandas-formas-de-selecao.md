---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
# Pandas Data Selection Methods

## DataFrame Setup
```python
import pandas as pd

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16)]

df = pd.DataFrame(data, 
                 index='L1 L2 L3 L4'.split(), 
                 columns='C1 C2 C3 C4'.split())
```

## Basic Selection Methods

### Column Selection
```python
df[['C3', 'C2']]  # Selects only C3 and C2 columns (in this order)
```

### Row Slicing
```python
df[1:3]  # Selects rows L2 to L3 (end index is exclusive)
```

### Combined Row/Column Selection
```python
df[1:][['C3', 'C2']]  # Rows from L2 onward + only C3 and C2 columns
```

## Label-Based Selection (.loc)

### Select Rows by Label
```python
df.loc[['L3', 'L2']]  # Specific rows in specified order
```

### Select Rows and Columns
```python
df.loc[['L3', 'L1'], ['C4', 'C1']]  # Specific rows and columns
```

## Position-Based Selection (.iloc)

### Select Single Value
```python
df.iloc[0, 1]  # Value at row 0 (L1), column 1 (C2) → returns 2
```

### Select Multiple Values
```python
df.iloc[[2, 0], [3, 0]]  # Rows 2,0 and columns 3,0
```

## Boolean Indexing
```python
# Filter rows where 'Tipo' is not 'Casa'
filtered_data = dados[~(dados['Tipo'] == 'Casa')]
```

## Selection Method Comparison

| Method | Selection Type | Returns | Syntax Example |
|--------|----------------|---------|----------------|
| `[]` | Column names | DataFrame | `df[['C1', 'C2']]` |
| `[]` | Row slices | DataFrame | `df[0:2]` |
| `.loc[]` | Label-based | DataFrame/Series | `df.loc['L1':'L3', 'C2']` |
| `.iloc[]` | Position-based | DataFrame/Series | `df.iloc[0:2, 1:3]` |
| Boolean | Conditional | DataFrame | `df[df['C1'] > 5]` |

> **Best Practices**:
> - Use `.loc` for label-based indexing
> - Use `.iloc` for position-based indexing
> - For column selection, prefer `df[['col']]` over `df.col`
> - Chain operations minimally to avoid SettingWithCopyWarning
```