---
tags:
  - learning/review
HUB:
  - "[[hub-visualization-data]]"
  - "[[hub-statistic]]"
---
## Tipos de gráficos para estudo de [[concept-ml-python-correlacao]]

```python
fig, ax = plt.subplots(figsize = (20,6))
ax = dados['variable'].plot()
```


### [[concept-histograma-pandas]]
```python
ax = sns.histplot(dados['variable'], kde=True)
```

### [[python-searborn-Using-PairGrid-and-pairplot]]
```python
ax = sns.pairplot(dados)

ax = sns.pairplot(dados, y_vars = 'variable', x_vars = ['variable', 'variable' , 'temp_max' , 'variable', 'variable'], kind='reg')
```

### [[seaborn-facegrit-catplot-lmplot]]
```python
ax = sns.lmplot(x = 'variable', y = 'variable', data = dados, hue = 'variable', markers = ['o', '*'], legend = False )
```

