---
tags:
  - learning
  - 
hub:
  - "[[hub-visualization-data]]"
---

### Gráfico em barra com seaborn

<font color = 00bfff>Gráficos em barras </font>: São semelhantes aos gráficos de colunas, mas a orientação é vertical, tornando-se úteis quando há muitas categorias.

``` css
import seaborn as sns
sns.barplot( x= "original_language", y = "total", data = tmdb)
```
- "sns.barplot" utiliza da bibliotéca seaborn para criar o gráfico
	- "original_language" atribuido ao eixo "x"
	- "total" atribuido ao eixo "y"
	- "data" recebe a varíável onde está o dataframe

![Imgur](https://i.imgur.com/MRVw8Mo.png)
<font color = 00bfff>Gráficos barras e colunas empilhadas </font> :  semelhantes aos gráficos de colunas e barras, mas permitem empilhar  várias series de dados em uma única coluna,  úteis para mostrar contribuição de diferentes partes de um todo
![Imgur](https://i.imgur.com/DuVLg5u.png)
- [[concept-python-barplot-com-matplotlib]]

