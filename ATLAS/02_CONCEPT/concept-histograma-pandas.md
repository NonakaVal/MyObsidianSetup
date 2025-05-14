---
tags:
  - learning
  - 
HUB:
  - "[[hub-visualization-data]]"
---
### Criando um histograma com pandas

[[cmp-pandas-importing-data]]

```css
notas.nota.plot(kind='hist')
notas.nota.describe()
```
- "plot" após o caminho da variável e coluna determina o retorno de um gráfico com dos dados diretamente com o pandas, e "(kind='hist')" determina o tipo de gráfico no caso um histograma
- "describe" é utilidado para gerar um resumo estatístico dos dados
![Imgur](https://i.imgur.com/hmOW1sO.png)


### Criando com seaborn


```css
import seaborn as sns

ax = sns.displot(dados.Altura, kde = True)
ax.figure.set_size_inches(12, 6)
ax.fig.suptitle('Distribuição de Frequência de Altura', fontsize=18)
ax.set_xlabels('Metros', fontsize=14)
```
> kde = True traça a estimativa da função de densidade do kernel no gráfico.



