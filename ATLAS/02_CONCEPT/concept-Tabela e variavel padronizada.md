---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
---


Foram criadas para facilitar a obtenção dos valores das áreas sob a curva normal

>Variável padronizada

### $$Z = \frac{x-\mu}{\sigma}$$


$x$ = variável normal com média $\mu$ e desvio padrão $\sigma$
$\sigma$ = desvio padrão
$\mu$ = média


Valores da tabela padronizada em [[concept-statistic-distribuicao-normal-(gaussiana)]]

```python
import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada
```


