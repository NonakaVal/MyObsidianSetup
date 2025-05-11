---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---
2024-01-18  13:58

[[concept-seaborn-count-plots-and-bar-plots]] - [[index-seaborn-matplotlib-charts]]
- `sns.catplot(...)`
	- `kind()`
		- `'strip','swarm','box','violin','boxen','point','bar','count'`

### Seaborn bar plots
- [[concept-python-grafico-em-barra-com-seaborn]]

### Point and count plots
- [[point-plots]]
- [[concept-seaborn-count-plots-and-bar-plots]]
- [[matplotlib]] | [[index-seaborn-matplotlib-charts]]
- [[draft-personalizando-graficos]]

```python
sns.catplot(x='traveler type', kind='count', col='user continent', col_wrap=3, palette=sns.color_palette("Set1"), data='reviews')
```

```python
# Adjust the color
ax = sns.catplot(
  x="Free internet", y="Score",
  hue="Traveler type", kind="bar",
  data=reviews,
  palette=sns.color_palette("Set2")
)

# Add a title
ax.fig.suptitle("Hotel Score by Traveler Type and Free Internet Access")

# Update the axis labels
ax.set_axis_labels("Free Internet", "Average Review Rating")

# Adjust the starting height of the graphic
plt.subplots_adjust(top=.93)
plt.show()
```

