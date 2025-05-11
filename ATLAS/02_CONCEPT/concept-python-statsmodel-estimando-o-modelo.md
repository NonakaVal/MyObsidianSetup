---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-statistic]]"
---

criando o modelo :
```python
import statsmodels.api as sm
X_train_com_constante = sm.add_constant(X_train)
modelo_statsmodels = sm.OLS(y_train, X_train_com_constante, hasconst = True).fit()
```

```python
print(modelo_statsmodels.summary())
```

![Imgur](https://i.imgur.com/eoCRuNo.png)