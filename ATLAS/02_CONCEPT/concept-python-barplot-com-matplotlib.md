---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
---
```css
%matplotlib inline
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))
```
plotando o barplot
```css
fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')
```
Editando o gr�fico
```css
[fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')](<fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do aluguel')
fig.set_title('Valor m�dio do aluguel por Bairro', {'fontsize':22})>)
```

![Imgur](https://i.imgur.com/MRVw8Mo.png)

mesmo exemplo com seaborn:

considerando o dataframe:
```css
df1 = grupo_bairro.Valor.aggregate(['min','std']).round(2).reset_index()
```

```python
import seaborn as sns

font1 = {'family':'serif','color':'blue','size':30}

sns.barplot(x = 'Bairro', y = 'std', data=df1)
plt.title("Sports Watch Data",fontdict = font1)
plt.show()
```


