---
tags:
  - learning
  - resources
HUB:
  - "[[hub-ml-models]]"
  - "[[hub-python]]"
  - "[[hub-statistic]]"
---

importando [sklearn.model_selection](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

```python
from sklearn.model_selection import train_test_split

y = dados.consumo
X = dados[['temp_max',-'chuva',-'fds']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=2811)
```
[[concept-linear-regression]]
- `y` definido como a variável dependente 
- `X` definindo a variável independente
- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=2811)` conjuntos de treinamento e de teste com parâmetros definidos 

> importando [sklearn.linear_ model](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
```python
from sklearn.linear_model import LinearRegression
from sklearn import metrics

modelo = LinearRegression()
modelo.fit(X_train, y_train)
```
- `LinearRegression()` e `.fit`  cria e ajusta o modelo aos dados de treinamento, sendo `.fit` responsável por encontrar os coeficientes e intercepto que melhor se ajustam aos dados

[[metricas-da-regressao]]

> comparando e avaliando os valores do modelo com dos dados reais  de treino 
```python
print('R² = {}'.format(modelo.score(X_train, y_train).round(2)))
```
- método `.score()`

```python
y_previsto = modelo.predict(X_test)
```
- `.predict` realiza as previsões com base nos dados de entrada

```python
print('R² = %s' % metrics.r2_score(y_test, y_previsto).round(2)) 
```

previsões com valores específicos 
```python
temp_max = 40
chuva = 0
fds = 1
entrada = [[temp_max,-chuva,-fds]]
print('{0:.2f} litros'.format(modelo.predict(entrada)[0]))
```

