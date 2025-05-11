---
tags:
  - learning
  - 
HUB:
  - "[[hub-data-visualization]]"
---
<font color = 00bfff>Gráficos em linhas</font> : ideal para destacar padrões de crescimento ou declínio e comparar desempenhos.

![Imgur](https://i.imgur.com/pnFTjE7.png)
<font color = 00bfff>gráfico cumulativo </font> :  usados para mostrar a evolução ao longo do tempo de um conjunto de dados. Eles são especialmente úteis para visualizar tendências ou progresso em relação a uma linha de base.
![Imgur](https://i.imgur.com/ZAVx0C9.png)
```
import matplotlib.pyplot as plt
import seaborn as sns`
```

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", data=mpg, kind="line", ci=None)
# Show plot
plt.show()


# Add markers and make each line have the same style
sns.relplot(
    x="model_year",
    y="horsepower",
    data=mpg,
    kind="line",
    ci=None,
    style="origin",
    hue="origin",
    markers=True,
    dashes=False
)
# Show plot
plt.show()

```
