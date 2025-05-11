---
tags:
  - learning/review
HUB:
  - "[[hub-data-visualization]]"
---

```python
# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col = "Age Category")

# Show plot

plt.show()
```

- Use `sns.set_style()` to set the figure style.
- Use the `col` parameter in `catplot()` to add subplots arranged in columns.
- To add a title to a `FacetGrid` object `g`, use `g.fig.suptitle()`.
- To label the x- and y-axis, use the `set()` function with the `xlabel` and `ylabel` parameters.