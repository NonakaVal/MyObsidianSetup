---
tags:
  - learning
HUB:
  - "[[hub-python]]"
created: "[[15-01-2024]]"
---
2024-01-15  09:30

- `my_data = ['A','A','C','B','C','A']`
	- `.nbytes`

```python
my_series1 = pd.Series(my_data, dtype='category')
```

```python
my_series2 = pd.categorical(my_data, categories = ['C','B','A'], ordered=True)
```

```python
# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype="category")

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)
```


[[flow-Verify-DataTypes]]

```python
# Check the dtypes
print(adult.dtypes)

# Create a dictionary with column names as keys and "category" as values

adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}  

# Read in the CSV using the dtypes parameter
# Read in the CSV using the dtype parameter

adult2 = pd.read_csv(
  "adult.csv",
  dtype = adult_dtypes
)

print(adult2.dtypes)
```
