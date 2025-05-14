---
tags:
  - learning
HUB:
  - "[[hub-visualization-data]]"
  - "[[hub-python]]"
---
![Imgur|500](https://i.imgur.com/wwllyeG.png)

- `PairGrid()`
- `PairPlot`

```python
# Create a PairGrid with a scatter plot for fatal_collisions and premiums

g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])

g2 = g.map(sns.scatterplot)

plt.show()
plt.clf()
```
---

```python
# Create the same PairGrid but map a histogram on the diag

g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(sns.histplot)
g3 = g2.map_offdiag(sns.scatterplot)

plt.show()
plt.clf()
```
---
```python
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter')

plt.show()
plt.clf()

sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter',
        hue='Region',
        palette='RdBu',
        diag_kws={'alpha':.5})

plt.show()
plt.clf()
```
---
```python
# plot relationships between insurance_losses and premiums

sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind='kde',
             hue='Region')
plt.clf()
plt.show()
```
