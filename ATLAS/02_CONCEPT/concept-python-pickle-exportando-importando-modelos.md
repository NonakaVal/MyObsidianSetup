---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-statistic]]"
---


exportando:
```python
import pickle

output = open('modelo_preco', 'wp')
pickle.dump(modelo, output)
output.close()
```

importando:
```python
import pickle

modelo = open('modelo_preço','rb')
lm_new = pickle.load(modelo)
modelo.close()

area = 38
garagem = 2
banheiros = 4
lareira = 4
marmore = 0
andares = 1

entrada = [[area,-garagem,-banheiros,-lareira,-marmore,-andares]]

print('$ {0:.2f}'.format(lm_new.predict(entrada)[0]))

```

[[concept-python-display-para-previsoes]]

