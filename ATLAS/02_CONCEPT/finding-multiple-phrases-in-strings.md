---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
2024-01-10  16:22

#### Finding multiple phrases in strings
• Words of interest: Ang that start with Data
`salaries['designation'].str.contains('^Data')`

##### Creating the categorical column
`salaries['job_category'] = np.select(condition, job_categories, defaut = 'Other' )`


##### Finding multiple phrases in strings

`salaries['designation'].str.contains(machine|AI)`

#### Finding multiple phrases in strings
- first create a list with the worlds
-  then variables as jobs_categories `data_science = "Data Scientist|NLP" or data_analys = "Analys|analytics"`
- than a list with the conditions
```python
conditions = 
(salaries["Designation"].str.contains(data_analyst)) ,
(salaries["Designation"]..contains(ml_engineer)) 
```
##### Creating the categorical column
```python
salaries['job_categories'] = np.select(conditions, job_categories, default = 'Other')
```

# exemples

```python
non_numeric = planes.select_dtypes("object")

for col in non_numeric.columns:

  print(f"Number of unique values in {col} column: ", non_numeric[col].nunique())
```

```python
# Solution code from the previous exercise

flight_categories = ["Short-haul", "Medium", "Long-haul"]
short_flights = "^0h|^1h|^2h|^3h|^4h"
medium_flights = "^5h|^6h|^7h|^8h|^9h"
long_flights = "10h|11h|12h|13h|14h|15h|16h"

# Create conditions for values in flight_categories to be created

conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

  

# Apply the conditions list to the flight_categories

planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()
```