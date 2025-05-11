---
tags:
  - learning
HUB:
  - "[[hub-data-visualization]]"
---
  - configurando para ambiente jupyter
```python
import matplotlib.pyplot as plt
%matplotlib inline
```

>criando o gráfico
```python
plt.figure(figsize=(15,8))
plt.plot(df['data'], df['temperatura'])
plt.title('Temperatura no momento')
```
![[lineplot.png]]

> alterações no gráfico
```python
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0, 0, 1, 1])
eixo.plot(df['data'], df['temperatura'], color = 'green')

eixo.set_title('Temperatura no momento', fontsize=25)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['temperatura'], loc = 'lower right', fontsize=15)
```
- tamanho do gráfico
- parâmetros de posição e proporções
- plot dos dados
	- definindo titulo e descrições

