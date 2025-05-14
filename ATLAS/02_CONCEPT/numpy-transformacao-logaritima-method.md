---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-data-wrangling]]"
---
Em análise estatística e modelagem, quando temos uma variável com [[concept-estatistica-media-mediana-moda]] , é comum aplicar a transformação logarítmica para tornar a distribuição mais próxima da normalidade 

```python
import numpy as np

dados['log_Valor'] = np.log(dados['Valor'])
dados['log_Area'] = np.log(dados['Area'])
dados['log_Dist_Praia'] = np.log(dados['Dist_Praia'] + 1)
dados['log_Dist_Farmacia'] = np.log(dados['Dist_Farmacia'] + 1)
```

[[index-sklearn-simple-linear-regression-model]]

uma vez usado do método de transformação logarítmica, para que o resultado final retorne ao valor correto, é necessário usar o método exp do numpy no resultado:

```python
np.exp(modelo.predict(entrada)[0])
```
