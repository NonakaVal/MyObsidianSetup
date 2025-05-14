---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
created: "[[2024-01-10]]"
---

# String Pattern Matching and Categorical Data Creation

## 🔍 Basic String Matching
### Finding designations starting with "Data"
```python
salaries['designation'].str.contains('^Data')  # Regex for starts with "Data"
```

### Matching multiple phrases
```python
salaries['designation'].str.contains('machine|AI')  # Contains "machine" OR "AI"
```

## 🏷️ Creating Categorical Columns

### Method 1: Simple Categorization
```python
import numpy as np

salaries['job_category'] = np.select(
    conditions,          # List of boolean conditions
    job_categories,      # List of corresponding categories
    default='Other'      # Default value
)
```

### Method 2: Advanced Pattern Matching
```python
# 1. Define patterns
data_science = "Data Scientist|NLP"
data_analyst = "Analyst|analytics"
ml_engineer = "Machine Learning|ML Engineer"

# 2. Create conditions
conditions = [
    salaries["Designation"].str.contains(data_analyst),
    salaries["Designation"].str.contains(ml_engineer),
    salaries["Designation"].str.contains(data_science)
]

# 3. Define corresponding categories
job_categories = ["Data Analyst", "ML Engineer", "Data Scientist"]

# 4. Apply categorization
salaries['job_category'] = np.select(conditions, job_categories, default='Other')
```

## ✈️ Practical Example: Flight Duration Categorization
```python
# Define categories and patterns
flight_categories = ["Short-haul", "Medium", "Long-haul"]
short_flights = "^0h|^1h|^2h|^3h|^4h"  # 0-4 hours
medium_flights = "^5h|^6h|^7h|^8h|^9h"  # 5-9 hours
long_flights = "10h|11h|12h|13h|14h|15h|16h"  # 10+ hours

# Create conditions
conditions = [
    planes["Duration"].str.contains(short_flights),
    planes["Duration"].str.contains(medium_flights),
    planes["Duration"].str.contains(long_flights)
]

# Apply categorization
planes["Duration_Category"] = np.select(
    conditions,
    flight_categories,
    default="Extreme duration"
)

# Visualize results
sns.countplot(data=planes, x="Duration_Category")
plt.show()
```

## 🔎 Data Exploration Helper
```python
# Inspect non-numeric columns
non_numeric = planes.select_dtypes("object")

for col in non_numeric.columns:
    print(f"Number of unique values in {col} column:", non_numeric[col].nunique())
```

## 💡 Pro Tips:
1. Use `^` in regex to match patterns at the start of strings
2. Order conditions from most to least specific
3. Always include a default category
4. Pre-compile complex regex patterns for better performance
5. Validate categories with value_counts() after creation

> **Note**: For large datasets, consider using `str.match()` instead of `str.contains()` for better performance with start/end patterns.
```

Key improvements:
1. Organized into clear sections with emoji icons
2. Added explanatory comments
3. Included both basic and advanced examples
4. Preserved all original code while improving formatting
5. Added practical tips
6. Included the flight duration case study
7. Added data exploration helper code
8. Improved readability with consistent spacing
9. Added performance considerations
10. Maintained all original functionality