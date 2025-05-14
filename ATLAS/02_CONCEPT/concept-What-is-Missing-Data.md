---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---


##### .query/catplot

- [[cmp-pandas-importing-data]]
	- arquivo armazenado na variável "mdb"

```css
import seaborn as sns
total_outras = mdb.query("original_language != 'en'")
sns.catplot(x="original_language", kind ="count", data= total_outras, aspect = 2, order= total_linguas.index, palette = "GnBu_d")
```
- método "query" está sendo usado para filtrar a coluna "original_language" dentro do dataframe "mdb" e então se verifica cada valor é igual a "en", e o resultado é armazenado em "total_outras"
- [[concept-python-grafico-em-barra-com-seaborn|sns.catplot]] cria um gráfico de barras os parametros [seaborn.catplot](https://seaborn.pydata.org/generated/seaborn.catplot.html)


selecionando dados especificos 

```python
tmdb_com_mais_de_10_votos  =  tmdb.query('vote_count >= 10')
```

```python
tmdb.query("runtime>0").runtime.dropna().quantile(q=0.8)
```
