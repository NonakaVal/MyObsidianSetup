---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-descriptive-analysis]]"
  - "[[hub-tratamento-de-dados]]"
---
2024-01-10  16:26


## Correlation with datatime
- [[concept-ml-python-correlacao]]

- `divorce.corr()`

- [[index-seaborn-matplotlib-charts]]

```python
sns.heatmap(divorce.corr(), annot = True)
plt.show()
```

![Imgur](https://i.imgur.com/KgqjWr8.png)

```python
sns.scatterplot(data= divorce, x ='income_man', y = 'income_woman')
plt.show()
```

![Imgur](https://i.imgur.com/pCvmu7V.png)


```python
sns.pairplot(data= divorce)
plt.show()
```

![Imgur](https://i.imgur.com/wwllyeG.png)

[[python-searborn-Using-PairGrid-and-pairplot]]

```python
sns.pairplot(data= divorce, vars = ['income', income_woman])
plt.show()
```

## exemplos

```python
sns.scatterplot(data=divorce, x="marriage_duration", y="num_kids")

plt.show()
```

```python
sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration"])

plt.show()
```