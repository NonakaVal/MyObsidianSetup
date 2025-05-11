---
tags:
  - learning
  - tocomplete/explicar
  - tocomplete/atomizar
HUB:
  - "[[hub-python]]"
created: "[[2024-02-13]]"
---
2024-02-13  12:14

### Creating Dates in Python

```python
from datetime import date

# create date
two_hurricanes_dates = [date(2016,10,7), date(2017, 6,21)]

print(two_hurrines_dates[0].year)
print(two_hurrines_dates[0].month)
print(two_hurrines_dates[0].day)
print(two_hurrines_dates[0].weekday())
```


### Math with dates
```python
delta = d1 - d2
print(delta.days)
```

```python
from datetime import timedelta
td = timedelta(days=29)
print(d1 +td)

```

### ISO 8601 format YYYY-MM-DD
```python
from datetime import date
d = date(2019,11,5)

# express the date in ISO 8601 format and put it in to a list
print([d.isoformat()])

print(d.strftime("%Y"))
print(d.strftime("%Y/%m/%d"))

# a few dates that computers once had trouble with

some_dates = ['2000-01-01', '1999-12-31']
print(sorted(some_dates))
```

### Dates and times

```python
from datetime import datetime

dt = datetime(2017,10,1,15,23,25)
```

```python
dt = datetime(year=2018, month=10, day = 1, hour=15, minute =23,second =23, microsecond=50000)
```


