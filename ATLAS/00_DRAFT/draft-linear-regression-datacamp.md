---
tags:
  - draf
created: '[[2025-05-13]]'
---


## Regression
[[concept-linear-regression]]

- map **Statistical models** to explore the relationship a **response variable** and some **explanatory variables**
	- *Response Variable* : the variable you want to predict.
	- *Explanatory Variables* : explain how the response variable will change.
- pen **Linear regression**
	- The response variable are numeric
- pen **Logistic regression**
	- the response variable is logic
- pen **Simple linear/logistic regression**
	- there is only one explanatory

Chart to pair plots  : [[concept-correlation-with-datetime|scatterplot]] or [[regression-plots|regplot]] .

- info Straight Lines
	- *Intercept* : the y value at the point when x is zero
	- *Slope (inclinação)* : the amount the y value increases if you increase x by one
	- *Equation* : $y=intercept+slope\times x$

![Imgur|500](https://i.imgur.com/zrZ0VYU.png)
 
  $y=intercept+slope\times x$
 
#### Running StatsModels
[[index-sklearn-simple-linear-regression-model]]
```python
from statsmodels.formula.api import ols
model = ols('response_variable ~ explanatory_variables', 
							 data = data)
model = model.fit()

print(model.params)

# intercept 
# n_claimns
```

#### Predict model
```python
print(model.predict(explanatory_data)

explanatory_data = pd.DataFrame(
								{"variable": np.arange(20,41)}
)

prediction_data = explanatory_data.assign(
mass_g = model.predict(explanatory_data))

```

### showing predictions
[[regression-plots]]
```python
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure() # to plot two plots at same figure
sns.regplot(x="variable",
		   y="variable",
		   ci=None,
		   data = bream)

sns.scatterplot(x="variable",
			   data=predicition_Data,
			   color="red",
			   marker="s")
```


### working with model objects
`.fittedvalues` Atribute : predictions on the original dataset :
```python
print(model.fittedvalues)
# or equivalently
explanatory_data = bream['variable']
print(model.predict(explanatory_data))
```

`.resid` : Actual response values minus predicted response values
```python
print(model.resid)
# or equivalently
print(data['variable'] - model.fittedvalues)
```

`summary()`
```python
mdl_mass_vs_lengh.summary()
```


## regression to the mean

Transform variables

## Quantify model fit

- coefficient of determination (r-squared)
	- que proportion of the variance in the response variable that is predictable from the exp´lanatory variable 
- [[concept-regressao-linear-residuos]]

`.summary()`
`.rsquared()` :  the coefficient of determination
`.mse_resid`

calculating rse
correlation squared
```python
coeff_determination = bream['length_cm'].corr(bream['mass_g']) **2
```

residual stard error(RSE)

![Imgur](https://i.imgur.com/JzO7UJf.png)

A "typical"  diference between a prediction and an observed response

```python
residuals_sq = mdl_bream.resid **2 # sqrt to eliminate negative values
resid_sum_of_sq = sum(residual_sq)
deg_freddom len(bream.index) -2
rse =np.sqrt(resid_sum_of_sq/deg_freedom)
print("rse:", rse)

```

em modelo de regressão linear simples os graus de liberdade são dados pelo número de observações (`len(bream.index)`) menos o número de parâmetros estimados

#### Residual plot Seaborn
```python
sns.residplot(x="", y="", data=data, lowess=True)
plt.xlabel("")
plt.ylabel("")
```

#### qqPlot from Statsmodels
```python
from statsmodels.api import qqplot
qqplot(data=data.resid, fit=True, line="45")
```

## Outliers, leverage an influence

```python
model = ols('response_variable ~ explanatory_variables', 
							 data = data).fit()
summary = model.get_influence().summary_frame()
```

[[conceitos-influencia-modelos-regressao-linear]]
cooks_distance
## logistic regression
regressão logística é um modelo estatístico usado para prever a probabilidade de um determinado evento ocorrer, onde o resultado é uma variável categórica binária.

Função sigmoide : 
$$P(Y=1)=\frac{1}{1+e^{-(\beta_0+\beta_1X_1+\beta_2X_2...\beta_nX_n)}}$$
exemplo cenário : alunos aprovados ou não com base em tempo de estudo.

![Imgur](https://i.imgur.com/wGo1ZKw.png)

- pontos vermelhos - os dados reais dos estudantes representando quem passou ou não
- curva azul - função sigmoide ajustada aos dados, que estima a probabilidade dele passar de acordo com as horas estudadas.
- linha verde pontilhada - fronteira de decisão.


```python
from statsmodels.formula.api import logit
model_ = logit("var_bool ~ var_", data=data).fit()
```





Last modified : `$= dv.current().file.mtime`

