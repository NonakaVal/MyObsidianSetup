---
tags:
  - learning
created: "[[2024-03-29]]"
hub:
  - "[[hub-python]]"
origin: https://docs.pandas-ai.com/en/latest/
---
 [[pandas-ai-start]]

- 01 Libs necessárias
	- key [link to api-key](https://www.pandabi.ai/admin/api-keys)

```python
import os
import pandas as pd
from pandasai import SmartDataframe

os.environ["PANDASAI_API_KEY"] = "$2a$10$dlK.TmvqXwy57o.xv3gPyuMvLMi5s1mZhmTd8378dVR/nElK4QM7e"
```

- 01 Função para simplificar troca de df para prompt
```python
def chat_(df,prompt):
    """Recebe um dataframe e um prompt e retorna o resultado do pandasai
    """
    agent = SmartDataframe(df)
    output = agent.chat(prompt)
    return output
```
