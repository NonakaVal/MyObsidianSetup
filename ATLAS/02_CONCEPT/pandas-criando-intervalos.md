---
tags:
  - learning
  - learning/review
HUB:
  - "[[hub-hypothesis-testing]]"
  - "[[hub-python]]"
  - "[[hub-statistic]]"
---

`calculando média salarial com [[cut]]()`

![Imgur](https://i.imgur.com/WrQkgkJ.png)

```python
classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E','D', 'C','B', 'A']

percentual = pd.value_counts(
    pd.cut(x = dados.Renda, bins = classes, labels = labels, include_lowest = True),
    normalize = True 
) *100

percentual = percentual.round(2)
```
- classes: intervalos definidos
	- labels - nomes que serão dados aos intervalos
		- include_lowest = True - permite incluir valores = 0
			- normalize = True  parâmetro que torna percentual

```css
dist_freq_quanti = pd.DataFrame({'Fraquencia': frequencia, ' Porcentagem(%)':percentual})
dist_freq_quanti.sort_index(ascending = False)
```



```python
import pandas as pd

def calcular_percentual_por_faixa(dados, coluna, classes, labels):
    """
    Categoriza os dados com base em intervalos, calcula o percentual de ocorrências em cada categoria,
    e retorna os percentuais arredondados.

    Parâmetros:
    dados (pd.DataFrame): DataFrame contendo os dados.
    coluna (str): Nome da coluna que será categorizada.
    classes (list): Lista de limites para as categorias.
    labels (list): Lista de rótulos para as categorias.

    Retorna:
    pd.Series: Percentual de ocorrências em cada categoria.
    """
    # Categoriza a coluna com base nas faixas especificadas
    percentual = pd.value_counts(
        pd.cut(x = dados[coluna], bins = classes, labels = labels, include_lowest = True),
        normalize = True 
    ) * 100
    
    # Arredonda os percentuais para duas casas decimais
    percentual = percentual.round(2)
    
    return percentual

```

[[concept-statistic-regra-de-sturges]]



```python
# Create salary labels

salary_labels = ["entry", "mid", "senior", "exec"]

# Create the salary ranges list
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]

# Create salary_level
salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                  bins=salary_ranges,
                                  labels=salary_labels)

  

# Plot the count of salary levels at companies of different sizes

sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()
```
