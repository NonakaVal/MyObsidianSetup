---
tags:
  - learning
HUB:
  - "[[hub-ml-models]]"
  - "[[hub-python]]"
  - "[[hub-hypothesis-testing]]"
---
# Data Analysis & Statistical Modeling Toolkit

## 📊 Hypothesis Testing Framework
[[testes-de-hipoteses|Hypothesis Testing Fundamentals]]
- **Null Hypothesis ($H_0$)** : ''$\geq$, $=$, $\leq$''
- **Alternative Hypothesis ($H_1$)** : $<$, $\neq$, $>$

## 🔧 Core Analysis Parameters
[[draft-ml-parametros-de-analise|Key Analysis Parameters]]
### Regression Metrics
[[metricas-da-regressao|Regression Evaluation Metrics]]
```python
from sklearn import metrics
metrics.r2_score(y_true, y_pred)  # R-squared
metrics.mean_squared_error(y_true, y_pred)  # MSE
```

### Statistical Modeling
[[concept-python-statsmodel-estimando-o-modelo|StatsModels Implementation]]
```python
import statsmodels.api as sm
model = sm.OLS(y, X).fit()
print(model.summary())  # Detailed regression report
```

## 📐 Confidence Intervals
[[obtendo-intervalos-de-confianca|Calculating Confidence Intervals]]
```python
from statsmodels.stats.weightstats import zconfint
ci = zconfint(sample_data)  # 95% CI by default
```

[[relacao-de-intervalos-de-confiancas-com-z-test-e-t-test|CI ↔ Z/T Test Relationships]]
[[concept-python-scipy-comparando-intervalos-de-confianca|Comparing CIs with SciPy]]

## 🧮 Distribution Analysis
[[snip-verificar-normalidade-amostra-dataframe|Checking Sample Normality]]
- Shapiro-Wilk Test
- Q-Q Plots
- Anderson-Darling Test

[[concept-python-comparando-distribuicoes-assimetricas|Comparing Skewed Distributions]]
- Kolmogorov-Smirnov Test
- Mann-Whitney U Test

## 📚 Research Methodology
[[concept-artigo-coleta-dados-mettzer]]
[[concept-ml-dados-experimentais|Experimental Data in ML]]

## 🔄 Workflow Integration
1. Formulate hypotheses
2. Select appropriate tests
3. Calculate confidence intervals
4. Verify distribution assumptions
5. Interpret model outputs

> **Pro Tip**: Always validate statistical assumptions before interpreting results!
```

Key improvements:
1. Added clear section headers with icons
2. Organized related concepts together
3. Included practical code examples
4. Added workflow guidance
5. Maintained all original links
6. Improved mathematical notation
7. Added visual hierarchy
8. Included professional recommendations
9. Standardized formatting
10. Enhanced readability while preserving technical depth

This structure makes your statistical toolkit more accessible while maintaining its technical rigor.