---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---
### DRY and "Do One Thing"
function example
- cada função deve fazer apenas uma coisa:


```python

def load_data(path):
	"""Load a dataset 
	Args:
		path(str): the location of a csv file
	Returns:
		tuple of ndappay: (features, labels)
	"""
	data = pd.read_csv(path)
	y = data['label'].values
	X = data[col for col in data.columns if col != 'label'].values
	return X, y
```
```python

def plot_data(X):
	"""Plot the fist two principal components of a matrix.
	Args:
		X (numpy.ndarray): the data to plot
	"""

	pca = PCA(n_components=2).fit_transform(X)
	plt.scatter(pca[:,0], pca[:,1])
```


```python
def standardize(column):
	"""Standardize the values in a column
	Args:
		column(pandas Series): The data to standardize
	Returns:
		pandas Series:  the values as z-scores
	"""
	Z_score = (column - column.mean()) / column.std()

	
df['y1_z'] = standardize(df.y1_gpa)

df['y2_z'] = standardize(df.y2_gpa)

df['y3_z'] = standardize(df.y3_gpa)

df['y4_z'] = standardize(df.y4_gpa)
```