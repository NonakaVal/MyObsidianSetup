---
tags:
  - learning
HUB:
  - "[[hub-visualization-data]]"
---
  -  | [[concept-matplot-scatterplot]]

[[concept-boxplot]]

```python
fig = plt.figure(figsize=(8,5))
eixo = fig.add_axes([0,0,1,1])

cores = ['red', 'blue', 'orange', 'green']

caixas = eixo.boxplot(df.drop('espécie', axis=1).values, patch_artist=True)
eixo.set_title('Gráfico de caixa', fontsize=15, pad=10)
eixo.set_xticklabels(df.drop('espécie', axis=1).columns)

for caixa, cor in zip(caixas['boxes'], cores):
    caixa.set(color=cor)

for outlier in caixas['fliers']:
    outlier.set(marker='x', markersize=8)
```

```python
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

eixo.hist(df['comprimento_pétala'])
eixo.set_title('Histograma', fontsize=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
eixo.grid(True)
```

![Imgur](https://i.imgur.com/IslHwzi.png)

[[concept-histograma-pandas]]

```python
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

eixo.hist(df['comprimento_pétala'])
eixo.set_title('Histograma', fontsize=15, pad=10)
eixo.set_xlabel('Comprimento da pétala', fontsize=15)
eixo.grid(True)
```

``` python
import seaborn as sns

ax = sns.distplot(tmdb.query("runtime>0").runtime.dropna(),
                 hist_kws={'cumulative':True},
                 kde_kws={'cumulative':True})
ax.set(xlabel='Tempo de duração', ylabel='Densidade')
ax.set_title('Duração dos filmes no TMDB 5000')
```

![Imgur](https://i.imgur.com/hmOW1sO.png)