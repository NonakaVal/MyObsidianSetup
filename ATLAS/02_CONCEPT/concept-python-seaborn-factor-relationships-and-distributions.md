---
HUB:
  - "[[hub-data-visualization]]"
  - "[[hub-python]]"
tags:
  - learning/review
---

```python
sns.histplot(data=divorce, x ='marriege_duration', binwidth=1)
```

#### 🔅 [[index-seaborn-matplotlib-charts]]

```python
sns.histplot(data=divorce, x ='marriege_duration', hue ='education_man', binwidth=1)
```
```python
sns.kdeplot(data=divorce, x = 'marriege_duration', hue ='education_man')
plt.show
```

![Imgur](https://i.imgur.com/hqlsBYl.png)
- visualizando os dados percebemos que o gráfico sugere que a duração do casamento é negativa ou seja [[concept-statistic-python-pandas-outliers]], para corrigir isso adicionamos o parâmetro cut:

```python
sns.kdeplot(data=divorce, x = 'marriege_duration', hue ='education_man', cut=0)
plt.show
```

- também é possível tornar o gráfico do tipo acumulativo 

```python
sns.kdeplot(data=divorce, x = 'marriege_duration', hue ='education_man', cut=0)
plt.show
```

### Scatter plot with categorical variables
```python
sns.scatterplot(data=divorce, x= 'woman_age_marriege', y ='man_age_marriage')
```

