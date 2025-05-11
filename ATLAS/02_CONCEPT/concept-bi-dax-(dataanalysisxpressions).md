---
tags:
  - learning/review
HUB:
  - "[[hub-bi]]"
---
# DAX ( Data Analysis eXpressions)

formula language to create calculations

>[!dax functions]

Function categories

- aggregation - `SUM()`, `AVERAGE()`, `COUNT`
- date and time - `TODAY()`, `MONTH()`, `YEAR()`
- logical -  `IF()`, `AND()`, `OR()`
- text - `CONCATENATE()`, `UPPER()`, `LEFT()`

exemples 

- syntax: `SUM(<column>)`

Creating calculated measures

total_price_w_tax =`SUM(Price_w_tax)`