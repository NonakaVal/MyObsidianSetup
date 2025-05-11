---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-hypothesis-testing]]"
  - "[[hub-statistic]]"
---


```python
# Executando o teste ranksums
statistic, p_value = ranksums(grupo_medicamento_A, grupo_medicamento_B)

# Imprimindo o resultado
print("Estatística do teste:", statistic)
print("Valor-p:", p_value)

if p_value < 0.05:
    print("Existe uma diferença significativa entre os dois grupos.")
else:
    print("Não há evidências de diferença significativa entre os dois grupos.")

```
