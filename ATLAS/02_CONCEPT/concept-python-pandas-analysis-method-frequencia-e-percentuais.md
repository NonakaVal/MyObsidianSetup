---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
  - "[[hub-descriptive-analysis]]"
---
# Pandas Data Analysis Techniques

## 📊 Variable Analysis
[[tipos-de-variaveis|Variable Types]]
- Categorical
- Numerical (Discrete/Continuous)
- Temporal
- Boolean

## 🔢 Frequency Analysis
[[python-unique-value_counts-method|Value Counts Method]]
```python
# Absolute frequency
frequency = dados['Sexo'].value_counts()

# Relative frequency (%)
percentage = dados['Sexo'].value_counts(normalize=True).mul(100).round(2)

# Display both
pd.DataFrame({
    'Frequency': frequency,
    'Percentage (%)': percentage
})
```

## ✂️ Cross-Tabulation
[[pandas-crosstab-method|Cross-Tab Method]]
```python
# Basic frequency cross-tab
pd.crosstab(index=dados['Sexo'], 
            columns=dados['Cor'])

# With aggregation
pd.crosstab(index=dados['Sexo'],
            columns=dados['Cor'],
            values=dados['Renda'],
            aggfunc='mean')
```

## 📈 Binning & Discretization
[[pandas-criando-intervalos|Creating Bins]]
```python
# Define bins and labels
income_bins = [0, 1576, 3152, 7880, 15760, 200000]
income_labels = ['E', 'D', 'C', 'B', 'A']

# Create categories
dados['Income_Class'] = pd.cut(
    x=dados['Renda'],
    bins=income_bins,
    labels=income_labels,
    include_lowest=True
)

# Calculate distribution
income_distribution = (
    dados['Income_Class']
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .sort_index()
)
```

## 📝 Practical Example
```python
# Complete analysis workflow
def analyze_variable(df, column, bins=None, labels=None):
    analysis = {}
    
    # Basic stats
    analysis['type'] = 'Categorical' if df[column].dtype == 'object' else 'Numerical'
    analysis['unique_values'] = df[column].nunique()
    
    # Frequency analysis
    if analysis['type'] == 'Categorical':
        freq = df[column].value_counts()
        analysis['frequency'] = freq
        analysis['percentage'] = freq.div(freq.sum()).mul(100).round(2)
    
    # Binning for numerical
    elif bins and labels:
        df[f'{column}_class'] = pd.cut(df[column], bins=bins, labels=labels)
        analysis['distribution'] = df[f'{column}_class'].value_counts().sort_index()
    
    return analysis

# Usage
income_analysis = analyze_variable(dados, 'Renda', bins=income_bins, labels=income_labels)
```

> **Pro Tip**: Always check for missing values with `dados.isna().sum()` before analysis!
```

Key improvements:
1. Added clear section headers with icons
2. Organized related methods together
3. Included practical examples for each technique
4. Added a complete analysis workflow function
5. Improved formatting and readability
6. Maintained all original concepts while adding context
7. Added type checking in the example workflow
8. Included missing value check recommendation
9. Standardized code style
10. Added percentage formatting in frequency analysis