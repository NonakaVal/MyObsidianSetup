---
tags:
  - learning
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
2024-01-09  18:17

# Padrões ao longo do tempo

## [[concept-correlation-with-datetime|Correlação com datas]]

## [[concept-introduction-to-line-plots|Gráficos em Linha]]
## Limpando Variáveis com valores de Datas 

```python
divorce = pd.read_csv('divorce.csv', parse_dates=['marriege_date'])
```
- `pd.to_datetime()`
- `dt.month`
- `divorce["marriage_year"] = divorce["marriage_date"].dt.year`
```python
# Define the marriage_year column

divorce["marriage_year"] = divorce["marriage_date"].dt.year

# Create a line plot showing the average number of kids by year

sns.lineplot(data=divorce, x="marriage_year", y="num_kids")

plt.show()
```


#### Extracting month and weekday
```python
planes['month'] = planes['date_of_jurney'].dt.month
planes['month'] = planes['date_of_jurney'].dt.weekday
print(planes[["month"]], [["week"]], [["date_of"]].head())
```

####  Get the month of the response

```python
# Get the month of the response

salaries["month"] = salaries["date_of_response"].dt.month
# Extract the weekday of the response

salaries["weekday"] = salaries["date_of_response"].dt.weekday
# Create a heatmap

sns.heatmap(salaries.corr(), annot=True)

plt.show()
```

