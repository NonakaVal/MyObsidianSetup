---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-ml-models]]"
  - "[[hub-statistic]]"
---
[[sklearn-criando-modelos]]
[[index-sklearn-simple-linear-regression-model]]


![Imgur](https://i.imgur.com/TR7glYS.png)
![Imgur](https://i.imgur.com/X7h3xna.png)



> Criando modelo preditivo 
```python
preditos = modelo_ajustado_2.predict()
```

```python
def modelo_receita(x_f, x_c):
    #limite
    limite_normalizado = [-1,+1]
    limite_farinha = [0.5,1.5]
    limite_chocolate = [0.1,0.5]
    
    #Converter 
    x_f_convertido = np.interp(x_f, limite_farinha, limite_normalizado )   
    x_c_convertido = np.interp(x_c, limite_chocolate, limite_normalizado )


    porcoes = parametros['Intercept'] + parametros['Farinha']*x_f_convertido  + parametros['Chocolate']*x_c_convertido
    
    return round(porcoes)


modelo_receita(0.6,0.1)
```


[[concept-python-matplot-criando-grafico-de-temperatura]]
