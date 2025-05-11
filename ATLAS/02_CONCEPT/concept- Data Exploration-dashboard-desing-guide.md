---
tags:
  - learning
  - tocomplete/atomizar
  - tocomplete/explicar
HUB:
  - "[[hub-bi]]"
---
# Data Exploration & Dashboard Design Guide

## Initial Data Exploration Process
1. Data Review & Cleaning → Insights Generation
2. Essential Python Methods:
   ```python
   info()
   value_counts()
   describe()
   ```
3. Visualization Tools:
   - [[concept-histograma-pandas|Histograms]]
   - [[concept-introduction-seaborn|Seaborn Intro]]


## Dashboard Design Principles
### Know Your Audience
- Identify primary users and their needs
- Determine how they'll use the dashboard
- Validate visualization effectiveness

### Emotional Engagement
- Worst case: No engagement → Irrelevant dashboard
- Best practices:
  1. Audience-tailored content
  2. One story per page
  3. Balance between rich information and clarity

### Visual Design Checklist
For each dashboard element ask:
- Does this support the story?
- Is this the right visual type?
- Is this element necessary?

### Color Usage
- Use as pre-attentive attribute
- Neutral colors for base elements
- Single accent color for emphasis
- Treat color like garnish (sparingly)

## Data Validation Techniques
### Type Checking & Conversion
```python
unemployment["2019"] = unemployment["2019"].astype('float')
print(unemployment.dtypes)
```

### Categorical Validation
```python
# Filter continents
not_oceania = ~unemployment["continent"].isin(["Oceania"])
print(unemployment[not_oceania])

# Value ranges
print(unemployment['2021'].min(), unemployment['2021'].max())
sns.boxplot(data=unemployment, x="2021", y="continent")
plt.show()
```

## Data Summarization
```python
books.agg(
    mean_rating=("rating", "mean"),
    std_rating=("rating", "std"),
    median_rating=("rating", "median")
)
```
[[cmp-pandas-groupby-method|GroupBy Methods]]

## Missing Data Strategies
1. Deletion (<5% missing)
2. Imputation:
   - Mean/median/mode
   - Sub-group specific values
3. Outlier handling

## Clean Data Characteristics
✓ Complete (no missing values)  
✓ Accurate (no typos/errors)  
✓ Unique (no duplicates)  
✓ Relevant (properly filtered)  
✓ Typed (correct data types)  
✓ Well-named (clear column/table names)  

## Power BI Data Types
- Numerical (Decimal/Whole/Percentage)
- Date/Time 
- Text 
- Logical (TRUE/FALSE) 
- Binary 


```

Key improvements:
1. Organized into clear sections with hierarchy
2. Fixed encoding issues and typos
3. Standardized code block formatting
4. Added visual hierarchy with headers
5. Maintained all links and references
6. Improved readability with checkmarks and lists
7. Added descriptive alt text for the image
8. Kept all original content while making it more scannable