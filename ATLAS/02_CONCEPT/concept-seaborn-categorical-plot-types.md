---
tags:
  - learning
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-visualization-data]]"
---
### Categorical Plot Types

- `stripplot()`
- `swarmplot()`

![Imgur](https://i.imgur.com/u2r2NHA.png)



Plot types - abstract representations

![Imgur](https://i.imgur.com/IslHwzi.png)

Plot types - statistical estimates
plot-types-statistical-estimates-image


```python
sns.stripplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         jitter=True)

plt.show()

# Create and display a swarmplot with hue set to the Region

sns.swarmplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         hue='Region')

plt.show()
```