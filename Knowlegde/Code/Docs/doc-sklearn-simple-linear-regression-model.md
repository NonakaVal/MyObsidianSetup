---
tags:
  - learning
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-hypothesis-testing]]"
---
##### 💹 [[concept-ml-python-correlacao]]
- `dados.corr(numeric_only=True).round(4)`

##### 📈 [[sklearn-criando-modelos]]
- `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=2811)`
- `modelo = LinearRegression()`, `modelo.fit(X_train, y_train)`, `y_previsto = modelo.predict(X_test)`
    - [[metricas-da-regressao]]
        - `EQM_2 = metrics.mean_squared_error(y2_test, y_previsto_2).round(2)`
        - `REQM_2 = np.sqrt(metrics.mean_squared_error(y2_test, y_previsto_2)).round(2)`
        - `R2_2 = metrics.r2_score(y2_test, y_previsto_2).round(2)`
    - [[concept-python-statsmodel-estimando-o-modelo]]
        - `modelo_statsmodels = sm.OLS(y_train, X_train_com_constante, hasconst=True).fit()`

##### [[concept-regressao-linear-residuos]]
- `residuo = y_train - y_previsto_train`

##### [[concept-python-pickle-exportando-importando-modelos]]
- `output = open('modelo_preco', 'wp')`
- `pickle.dump(modelo, output)`
- `output.close()`
    - [[concept-python-display-para-previsoes]]
