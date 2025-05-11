---
tags:
  - learning/review
HUB:
  - "[[hub-ml-models]]"
  - "[[hub-python]]"
---
<font color = 00bffff>Correlação</font> : Mede a relação ou a associação entre duas variáveis, e indica se as duas estão relacionadas, e se sim, qual a natureza dessa relação ( positiva, negativa ou neutra)
- info Uma correlação de 1 indica uma relação positiva.

> Método `corr` para ver a correlação entre as variáveis gerais de um dataframe.

```python
dados.corr(numeric_only=True).round(4)
```

> Método `corr`  selecionando variáveis .
```python
import pandas as pd

data = {'Temperatura': [20, 25, 30, 35, 40],
        'Consumo_Energia': [100, 120, 150, 180, 200]}

df = pd.DataFrame(data)

correlation = df['Temperatura'].corr(df['Consumo_Energia'])
print(f"A correlação entre temperatura e consumo de energia é: {correlation}")
```

[[concept-correlacao-plots]]

