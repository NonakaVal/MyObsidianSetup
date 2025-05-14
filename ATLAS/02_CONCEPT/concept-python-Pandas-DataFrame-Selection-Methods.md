---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
concept-python-Pandas-DataFrame-Selection-Methods
## Pandas DataFrame Selection Methods

### 1. Creating a DataFrame from Dictionary
```python
alunos = pd.DataFrame({
    'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
    'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
    'Idade': [15, 27, 56, 32, 42, 21, 19, 35],
    'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
    'Aprovado': [True, False, False, True, True, True, False, False]
})
```

### 2. Basic Selection Examples

#### a) Approved Students
```python
selecao = alunos['Aprovado'] == True
aprovados = alunos[selecao]
```
- Creates a boolean mask (`selecao`) where `True` indicates approved students
- Filters the DataFrame using the mask

#### b) Approved Female Students
```python
selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')
aprovadas = alunos[selecao]
```
- Combines conditions with `&` (AND) operator
- Parentheses are required for proper evaluation order

#### c) Age Range Selection
```python
selecao = ((alunos.Idade > 10) & (alunos.Idade < 20)) | (alunos.Idade >= 40)
idades = alunos[selecao]
```
- Uses both `&` (AND) and `|` (OR) operators
- Complex conditions should be properly grouped with parentheses

### 3. Advanced Selection Techniques

#### a) Failed Students (Specific Columns)
```python
selecao = alunos.Aprovado == False
reprovados = alunos.loc[selecao, ['Nome', 'Sexo', 'Idade']]
```
- Uses `.loc[]` for label-based selection
- Filters rows by condition and selects specific columns

#### b) Top 3 Youngest Students
```python
alunos.sort_values(by=['Idade'], inplace=True)
alunos.iloc[:3]
```
- Sorts DataFrame by age (ascending by default)
- Uses `.iloc[]` for position-based selection of first 3 rows

### Key Concepts:
1. **Boolean Masking**: Create True/False series to filter rows
2. **Logical Operators**:
   - `&` (AND) - Both conditions must be True
   - `|` (OR) - At least one condition must be True
   - `~` (NOT) - Inverts the condition
3. **Selection Methods**:
   - `[]` - Basic selection
   - `.loc[]` - Label-based selection
   - `.iloc[]` - Position-based selection

### Best Practices:
- Use parentheses to group complex conditions
- For multiple conditions, consider `query()` method
- Chain operations carefully to avoid `SettingWithCopyWarning`
- Reset index after filtering if needed: `df.reset_index(drop=True)`

[[concept-python-Pandas-DataFrame-Selection-Methods-2|Continue to Frequency Selection Part 2 →]]
