---
tags:
  - learning/review
HUB:
  - "[[hub-visualization-data]]"
---


- `heatmap()`
- `crosstab()`
	- `corr()`

```python
# Create a crosstab table of the data
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()
```

![Imgur](https://i.imgur.com/KgqjWr8.png)