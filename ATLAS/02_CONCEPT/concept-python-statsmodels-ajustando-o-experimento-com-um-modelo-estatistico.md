---
tags:
  - learning
  - tocomplete/explicar
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-statistic]]"
---
![Imgur](https://i.imgur.com/66t1jnI.png)

```python
import statsmodels.api as sm 
import statsmodels.formula.api as smf
```

```python
modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')
modelo_ajustado = modelo.fit()
print(modelo_ajustado.summary() )
```

