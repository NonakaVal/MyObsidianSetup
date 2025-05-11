---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-data-visualization]]"
---
preset styles
- 'write', 'dark', 'writegrid','darkdrig','' ticks'
`sns.set_style()`

`sns.set_palette()`
- 'RdBu', 'PRGn', 'RdBu_r', 'PRGn_r'

Sequential palettes
- 'Greys', 'Bues', 'PuRd', 'GnBu'

`sns.set_context()`
- paper, notebook, talk, poster

```python
# Import Seaborn and Matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style to "whitegrid"
sns.set_style("whitegrid")

# Set Seaborn color palette to "RdBu"
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]

sns.catplot(x="Parents Advice", data=survey_data, kind="count", order=category_order)

# Show the plot
plt.show()

```


```python
# Change the context to "notebook"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show the plot
plt.show()

```
