---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-descriptive-analysis]]"
---


> medida de dispersão que indica o quanto os valores de uma população se afastam da média populacional:

### Desvio padrão populacional
>quanto se tem todos os dados, e calcula a média dos quadrados de cada valor
# $$\sigma = \sqrt{\frac 1n\sum_{i=1}^{n}(X_i-\mu)^2} \Longrightarrow \sigma = \sqrt{\sigma^2}$$
### Desvio padrão amostral
> quando se tem apenas uma amostra do total
# $$S = \sqrt{\frac 1{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2} \Longrightarrow S = \sqrt{S^2}$$
desvio do padrão com numpy: a partir do valor da [[variancia]]
```css
import numpy as np
np.sqrt(variancia)
```

com operação direta:
```css
desvio_padrao = notas_fulano.Fulano.std()
desvio_padrao
```

