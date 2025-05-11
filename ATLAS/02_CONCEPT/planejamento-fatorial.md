---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
  - "[[hub-hypothesis-testing]]"
---
[vídeo explicativo](https://www.youtube.com/watch?v=0164j1IxQ6o&t=1395s&ab_channel=CanaldaEngenhariadeManufaturaeQualidade)

![Imgur](https://i.imgur.com/lRQUeuV.png)


Criando uma matriz de ensaios  com [py2DOE](https://pypi.org/project/pyDOE2/)

```python
import pyDOE2 as doe
ensaios  = doe.ff2n(2)
```
> matriz 2x2


> Criando o DataFrame com os experimentos 
>  Criando as colunas com os resultados
```python
experimento = pd.DataFrame(ensaios, columns = ['Farinha','Chocolate']    )
experimento['Porcoes'] = [19,37,24,49]
```

