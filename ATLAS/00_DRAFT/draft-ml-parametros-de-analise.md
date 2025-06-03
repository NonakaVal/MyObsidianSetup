---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-hypothesis-testing]]"
---
# Regression Analysis Metrics

## 📈 Core Regression Components

### 1. Coefficients (`coef_`)
- Represents the slope/weight for each independent variable
- Interpretation: Change in dependent variable per unit change in predictor
- **Rule**: Larger absolute values → stronger impact (but check significance)

### 2. Intercept (`intercept_`)
- Baseline value when all predictors = 0
- Context-dependent importance
- Warning: Often lacks real-world meaning if predictors can't realistically be zero

## 📊 Model Fit Statistics

### R-squared (R²)
- Range: 0 to 1 (or 0% to 100%)
- Interpretation: % of variance in dependent variable explained by model
- **Caution**: Increases with more predictors → Use Adjusted R² for multiple regression

### Residuals
[[concept-regressao-linear-residuos|Residual Analysis]]
- Degrees of freedom = n_observations - n_parameters
- Ideal: Normally distributed around zero
- **Check**: Residual plots for patterns

## 🔍 Statistical Significance

### t-statistic
- Coefficient ÷ Standard Error
- Measures "signal to noise" ratio
- **Rule of thumb**: |t| > 2 suggests significance

### p-value (`P>|t|`)
[[concept-python-comparando-distribuicoes-assimetricas]]
- Probability of observing the result if null hypothesis (β=0) were true
- **Thresholds**:
  - p < 0.01: Strong evidence against null
  - p < 0.05: Moderate evidence
  - p < 0.10: Weak evidence

### Standard Error
- Precision estimate of coefficient
- Lower values → more precise estimates

## 📝 Interpretation Guide

| Metric      | Ideal Direction | Practical Consideration |
|-------------|-----------------|-------------------------|
| R-squared   | Higher          | Context-dependent benchmarks |
| Coefficients | Larger (if sig.) | Standardize for comparison |
| p-values    | Smaller         | < 0.05 typically significant |
| Residuals   | Smaller         | Check for heteroscedasticity |
| t-stats     | Larger          | Absolute value > 2 preferred |

```python
# Example metrics extraction
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Scikit-learn
model = LinearRegression().fit(X, y)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# StatsModels (with p-values)
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())
```

> **Pro Tip**: Always validate regression assumptions (linearity, independence, homoscedasticity, normality) before interpreting these metrics!

[[metricas-da-regressao|More Regression Metrics]]
```

Key improvements:
1. Organized into logical sections
2. Added clear interpretation guidelines
3. Included practical code examples
4. Added warning about assumptions
5. Created a quick-reference table
6. Maintained all your original concepts
7. Added links to deeper resources
8. Improved visual hierarchy
9. Added statistical thresholds
10. Balanced technical depth with readability