---
tags:
  - learning
  - resources
  - tocomplete
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
link-to-lib: https://docs.streamlit.io/develop/s/architecture/caching
created: "[[2024-08-04]]"
---
{{Objetivo da lib}}

```python
@st.cache_data 
def long_running_function(param1, param2): 
	return …
```

`st.cache_resource` : save global resources as ml models 

![Imgur](https://i.imgur.com/4GITGFu.png)

```python
import streamlit as st
import pandas as pd

@st.cache_data  # 👈 Add the caching decorator

def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
```

```python
@st.cache_resource

def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "pfmegrnargs"
    user = "reader"
    password = "NWDMCE5xdipIjRrp"
    return psycopg2.connect(host=host, database=database, user=user, password=password)

conn = init_connection()
```



{{Métodos}}

`ttl` time-to-live parameter

```python
@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = api.get(...)
    return data
```

`max_entries`
`show_spinner`