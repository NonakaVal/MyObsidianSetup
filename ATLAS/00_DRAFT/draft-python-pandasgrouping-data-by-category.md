---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
created: "[[17-01-2024]]"
---
2024-01-17  18:45


```python
groupby_object = adult.groupby(by=['Above/Below 50K'])
```

```python
# Create a list of user-selected variables
user_list = ["Education", "Above/Below 50k"]

# Create a GroupBy object using this list
gb = adult.groupby(by=user_list)

# Find the mean for the variable "Hours/Week" for each group - Be efficient!
print(gb["Hours/Week"].mean())
```


### Setting category variables
```python
Series.cat.method_name
```

- `new_categories`
- `inplace`
- `ordered`

```python
dogs['coat'] = dogs['coat'].cat.set_categories(new_categories = ['short','medium','long'])

dogs['coat'].value_counts(dropna=False)
```

### Adding categories
```python
dogs['like_people'] = dogs['like_people'].astype('category')
dogs['like_people'] = dogs['like_people'].cat.add_categories(new_categories = ['did not check','could not tell'])

dogs['like_people'].cat.categories


```

### Removing categories

```python
dogs['coat'] = dogs['coat'].astype('category')
dogs['coat'] = dogs['coat'].cat.remove_categories(removals=['wirehaired'])
```


### Renaming categories

```python
Series.cat.rename_categories(new_categories=dict)
```

```python
my_changes = {
			  "Unknow mix":"Unknow"
}

dogs['breed'] = dogs['breed'].cat.rename_categories(my_changes) 

```

#### Renaming categories with a function

```python
dogs['sex'] = dogs['sex'].cat.rename_categories(lambda c : c.title())
```

### Collapsing categories setup
[[concept-python-pandas-collapsing-data-into-categories]]

```python
dogs['main_color'] = dogs['color'].replace(dict)
```
- need reverse to categorical


### Reordering categories

```python
dogs['coat'] = dogs['coat'].cat.reorder_categories(
		new_categories = ['short', 'medium', 'wirehaired', 'long']
		ordered = True
)


dogs['coat'] = dogs['coat'].cat.reorder_categories(
		new_categories = ['short', 'medium',  'long', 'wirehaired',]
		ordered = False
)
```




---
 exemplos

```python
# Check frequency counts while also printing the NaN count
print(dogs["keep_in"].value_counts(dropna=False))

# Switch to a categorical variable
dogs["keep_in"] = dogs["keep_in"].astype("category")

# Add new categories
new_categories = ["Unknown History", "Open Yard (Countryside)"]
dogs["keep_in"] = dogs["keep_in"].cat.add_categories(new_categories)

# Check frequency counts one more time
print(dogs["keep_in"].value_counts(dropna=False))
```

```python
# Set "maybe" to be "no"
dogs.loc[dogs["likes_children"] == "maybe", "likes_children"] = "no"

# Print out categories
print(dogs["likes_children"].cat.categories)

# Print the frequency table
print(dogs["likes_children"].value_counts())

# Remove the `"maybe" category
dogs["likes_children"] = dogs["likes_children"].cat.remove_categories(["maybe"])
print(dogs["likes_children"].value_counts())

# Print the categories one more time
print(print(dogs["likes_children"].cat.categories))
```

```python
# Previous code

dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace=True
)

  

# How many Male/Female dogs are available of each size?
print(dogs.groupby('size')['sex'].value_counts())
  

# Do larger dogs need more room to roam?

print(dogs.groupby('size')['keep_in'].value_counts())
```

