---
tags:
  - learning
  - 
HUB:
  - "[[hub-data-visualization]]"
---
# Data Visualization with Matplotlib & Seaborn

## Basic Single Plot Example
Visualizing distribution of 1-bedroom fair market rents:

```python
# Initialize figure and single axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create histogram with KDE line
sns.histplot(data=df, x='fmr_1', ax=ax, kde=True, color='#4e79e7')

# Customize plot labels and range
ax.set(xlabel="1 Bedroom Fair Market Rent ($)",
       ylabel="Frequency",
       xlim=(100, 1500),
       title="US Rental Market: 1 Bedroom Distribution")

plt.tight_layout()
plt.show()
```

**Key Features:**
- Uses `sns.histplot()` for distribution visualization
- KDE line shows probability density
- Clear axis labels with units
- Controlled x-axis range (100-1500)
- Professional color scheme

## Comparative Plot Example
Comparing 1-bedroom vs 2-bedroom rents:

```python
# Create figure with two subplots sharing y-axis
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, 
                               sharey=True,
                               figsize=(12, 6))

# Plot 1-bedroom distribution
sns.histplot(data=df, x='fmr_1', ax=ax0, color='#4e79e7')
ax0.set(xlabel="1 Bedroom Rent ($)",
        xlim=(100, 1500),
        title="1 Bedroom Units")

# Plot 2-bedroom distribution        
sns.histplot(data=df, x='fmr_2', ax=ax1, color='#e74e5a')
ax1.set(xlabel="2 Bedroom Rent ($)",
        xlim=(100, 1500),
        title="2 Bedroom Units")

plt.tight_layout()
plt.show()
```

**Comparison Benefits:**
- Shared y-axis enables direct comparison
- Consistent x-range for both plots
- Different colors for clear distinction
- Balanced layout with `tight_layout()`

## Best Practices
1. Always set explicit figure sizes
2. Include units in axis labels
3. Use constrained layouts to prevent overlap
4. Choose accessible color palettes
5. Add KDE lines for distribution clarity
6. Set consistent axis ranges for comparisons

> **Note:** For publication-quality plots, consider adding:
> - Annotations for key insights
> - Descriptive captions
> - Source citations




This note provides:
1. Ready-to-use code examples
2. Clear explanations of key features
3. Visualization best practices
4. Professional formatting
5. Easy adaptation for different datasets
