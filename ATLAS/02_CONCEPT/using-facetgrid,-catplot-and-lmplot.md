---
tags:
  - learning
HUB:
  - "[[]]"
  - "[[hub-data-visualization]]"
---



- `sns.FaceGrid()`
- `sns.catplot()`
- `sns.lmplot()`

```python
# Create FacetGrid with Degree_Type and specify the order of the rows using row_order

g2 = sns.FacetGrid(df, 
             row="Degree_Type",
             row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid

g2.map(sns.pointplot, 'SAT_AVG_ALL')


# Show the plot
plt.show()
plt.clf()
```

```python
sns.catplot(data=df,
        x='SAT_AVG_ALL',
        kind='point',
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

plt.clf()
plt.show()
```

```python
# Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column

sns.lmplot(data=df,
        x='SAT_AVG_ALL',
        y='Tuition',
        hue='WOMENONLY',
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors'],
        col='Ownership',
        col_order=inst_ord)

plt.show()

plt.clf()
```
