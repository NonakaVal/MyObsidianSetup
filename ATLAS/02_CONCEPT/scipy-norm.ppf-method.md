---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-tratamento-de-dados]]"
---
A função `ppf` (Percent Point Function), também conhecida como inversa da CDF, retorna o valor abaixo do qual uma certa porcentagem dos dados da distribuição normal se encontra. Por exemplo, se você quiser saber o valor que corresponde ao percentil 95 de uma distribuição normal, você usaria `ppf(0.95)`

[[nivel-de-confianca-e-significancia]] com [[scipy.stats.norm]] método **ppf** e **interval**

>Problema: Para estimar o valor médio gasto por cada cliente de uma grande rede de fast-food, foi selecionada uma amostra de 50 clientes.

Assumindo que o valor do desvio padrão da população seja de R$ 6,00 e que esta população se distribui normalmente, obtenha a margem de erro desta estimativa para um nível de confiança de 95%.

```css
from scipy.stats import norm
import numpy as np

z = norm.ppf(0.975)
desvio_padrao = 6
n = 50

e = z * (desvio_padrao / np.sqrt(n))
print("R$ {0:0.2f}".format(e))
```

![[scipy-norm.interval-method]]

