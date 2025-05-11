---
tags:
  - learning
  - tocomplete/atomizar
  - 
HUB:
  - "[[hub-python]]"
created: "[[30-01-2024]]"
---
2024-01-30  17:30

# Reading a text file

```python
# Open a file: file

file = open('moby_dick.txt', 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)
# Close file
file.close()

# Check whether file is closed
print(file.closed)
```


```python
with open('huck_fin.txt', 'r') as file:
	print(file.read())
```


# Importing flat files using NumPy

```python
import numpy as np
filename = 'MIst.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols['0','2'])
data
```



```python

# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
```

```python
# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file, delimiter = ',',names=True, dtype=None)

# Print out first three entries of d
print(d[:3])
```


```python
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))
```

### picked files

```python
import pickle
with open('pickled_fruit.pkl', 'rb') as file:
	data = pickle.load(file)
print(data)
```


# Importing SAS/Stata files using pandas

### SAS
```python
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
	df_sas = file.to_data_frame()
```

### STATA
```python
import pandas as pd
data = pd.read_stata('urbanpop.dta')
```


# Importing HDF5 files

```python
import h5py
filename = 'name.hdf5'
data = h5py.File(filename, 'r')
print(type(data))
```

# Importing MATLAB files
```python
import scipy.io
filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))
```

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')

```
# Querying relational databases in Python

```python
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
```


```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect()
rs = con.execute('SELECT * FROM Orders')

df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()

con.close()
```

- using the context manager

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
	rs = con.execute('SELECT OrderID, Orderdate, ShipName FROM Order')
	df = pd.DataFrame(rs.fechmany(size=5))
	df.columns = rs.keys()

```

# Querying relational databases directly with pandas

```python
df = pd.read_sql_querry('SELECT * FROM Orders', engine)
```
