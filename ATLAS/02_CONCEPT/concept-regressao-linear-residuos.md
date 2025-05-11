---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-ml-models]]"
  - "[[hub-python]]"
  - "[[hub-data-visualization]]"
---
Em uma regressão linear, os resíduos são a diferença entre os valores observados e os valores previstos pelo modelo de regressão, e representam a variação não explicada pelo modelo e fornecem informações sobre a qualidade do ajuste.

[[index-sklearn-simple-linear-regression-model]]

> a partir da criação de um modelo é possível observar a distribuição dos resíduos da seguinte forma:

```python
residuo = y_train - y_previsto_train
ax = sns.scatterplot(x = y_previsto_train, y = residuo , s = 100)
```


![Imgur](https://i.imgur.com/OqX7UI5.png)

