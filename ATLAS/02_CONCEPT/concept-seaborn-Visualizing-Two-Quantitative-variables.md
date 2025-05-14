---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-visualization-data]]"
---

```python
the plots in rows instead of columns

sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")
plt.show()
```


```python
sns.relplot(
    x="G1",  # x-axis variable, likely a feature named "G1"
    y="G3",  # y-axis variable, likely a target variable named "G3"
    data=student_data,  # DataFrame containing the data
    kind="scatter",  # Type of plot, in this case, a scatter plot
    col="schoolsup",  # Categorize the data by the "schoolsup" variable into columns
    col_order=["yes", "no"],  # Order in which the "schoolsup" categories are displayed in columns
    row="famsup",  # Categorize the data by the "famsup" variable into rows
    row_order=["yes", "no"]  # Order in which the "famsup" categories are displayed in rows
)

# Show the plot
plt.show()

```

[[concept-introduction-to-line-plots]]
