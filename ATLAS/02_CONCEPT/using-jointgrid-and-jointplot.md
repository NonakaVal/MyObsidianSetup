---
tags:
  - learning
HUB:
  - "[[hub-visualization-data]]"
---

```python
# Build a JointGrid comparing humidity and total_rentals

sns.set_style("whitegrid")

g = sns.JointGrid(x="hum",
                  y="total_rentals",
                  data=df,
                  xlim=(0.1, 1.0))

g.plot(sns.regplot, sns.histplot)

plt.show()

plt.clf()
```

```python
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()

plt.clf()
```
