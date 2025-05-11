---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
---


[[concept-python-pickle-exportando-importando-modelos]] :

```python
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from ipywidgets import widgets, HBox, VBox
from IPython.display import display

# Carregar o modelo salvo
modelo = open('modelo_preço2', 'rb')
lm_new = pickle.load(modelo)
modelo.close()
```


display: 
```python
def simulador(sender):
    entrada = [[
--------float(area.value-if-area.value-else-0),
--------float(garagem.value-if-garagem.value-else-0),
--------float(banheiros.value-if-banheiros.value-else-0),
--------float(lareira.value-if-lareira.value-else-0),
--------float(marmore.value-if-marmore.value-else-0),
--------float(andares.value-if-andares.value-else-0)
----]]
    dados_entrada = pd.DataFrame(entrada, columns=['area', 'garagem', 'banheiros', 'lareira', 'marmore', 'andares'])
    previsao = lm_new.predict(dados_entrada)
    print('$ {0:.2f}'.format(previsao[0]))

# Criando os controles do formulário
area = widgets.Text(description="Área")
garagem = widgets.Text(description="Garagem")
banheiros = widgets.Text(description="Banheiros")
lareira = widgets.Text(description="Lareira")
marmore = widgets.Text(description="Mármore?")
andares = widgets.Text(description="Andares?")
botao = widgets.Button(description="Simular")

# Atribuindo a função "simulador" ao evento click do botão
botao.on_click(simulador)

# Posicionando os controles
left = VBox([area, banheiros, marmore])
right = VBox([garagem, lareira, andares])
inputs = HBox([left, right])
```

```python
# Exibindo o formulário
display(inputs, botao)
```