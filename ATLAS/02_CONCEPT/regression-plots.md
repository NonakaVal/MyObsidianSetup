---
tags:
  - learning
HUB:
  - "[[hub-data-visualization]]"
---
Plotting with regplot()
```python
# Display a regression plot for Tuition

sns.regplot(data=df,
         y='Tuition',
         x='SAT_AVG_ALL',
         marker='^',
         color='g')

plt.show()

plt.clf()
```

```python
# Create another plot that estimates the tuition by PCTPELL

sns.regplot(data=df,
            y='Tuition',
            x='PCTPELL',
            x_bins=5)
            
plt.show()
plt.clf()
```
