---
tags:
  - learning
HUB:
  - "[[hub-visualization-data]]"
---

```python
x_farinha = np.linspace(start = 0.5, stop = 1.5, num = 10)
x_chocolate = np.linspace(start = 0.1, stop = 0.5, num = 10)

```

```python
pontos = []

for cont1 in x_farinha:
    temp = []    
    for cont2 in x_chocolate:    
        temp.append(modelo_receita(cont1, cont2))
    pontos.append(temp)
```

```python
import matplotlib.cm as cm 
```

```python
#base
plt.figure(figsize = (16,6))
plt.xlabel('Farinha (kg)', fontsize = 16)
plt.ylabel('Chocolate (kg)', fontsize = 16)


#Mapa de cores 
mapa_cor = plt.imshow(pontos, origin = 'lower',  cmap = cm.rainbow, interpolation= 'quadric', extent = (0.5,1.5, 0.1,0.5)   )

#Barra de cor
plt.colorbar().set_label('Porcoes', fontsize = 16)

#linha 
linhas = plt.contour(x_farinha, x_chocolate, pontos, colors = 'k', linewidths = 1.5)
plt.clabel(linhas, inline = True, fmt = '%1.0f', fontsize = 15.0 , inline_spacing = 10)
```

![Imgur](https://i.imgur.com/tPLKJaq.png)


