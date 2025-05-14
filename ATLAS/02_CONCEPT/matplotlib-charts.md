---
tags:
  - learning
  - resources
  - tocomplete/explicar
HUB:
  - "[[hub-visualization-data]]"
---
[matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html)


```python
fig = plt.figure(figsize=(15,8))

eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.65,0.3,0.3])

eixo.grid(True)
eixo.plot(df['data'], df['temperatura'], color = 'green')
eixo.set_xlim(datetime.datetime(2014,5,1),datetime.datetime(2014,6,1)) # Apenas maio/14
eixo.set_ylim(0,50) # eixo y de 0 a 50
eixo.set_title('Temperatura em Maio/2014', fontsize=25, pad = 20)
eixo.set_ylabel('Temperatura', fontsize=20)
eixo.set_xlabel('Data', fontsize=20)
eixo.legend(['Temperatura'], loc = 'lower right', fontsize= 15)

eixo2.grid(True)
eixo2.plot(df['data'], df['temperatura'], color = 'b')
eixo2.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1)) # Apenas 2014
eixo2.legend(['Temperatura'], loc = 'lower right')
eixo2.set_title('Temperatura 2014', fontsize=15)
```


Gráfico de barras
```python
temperatura_por_dia_da_semana = df.groupby('dia_da_semana')['temperatura'].mean()
nome_dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
temperatura_por_dia_da_semana = temperatura_por_dia_da_semana[nome_dias]

fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

indice = range(len(temperatura_por_dia_da_semana))

eixo.bar(indice, temperatura_por_dia_da_semana)
eixo.set_title('Temperatura por dia da semana', fontsize=15, pad=10)
eixo.set_xlabel('Dia da semana', fontsize=15)
eixo.set_ylabel('Temperatura média', fontsize=15)
eixo.set_xticks(indice)
eixo.set_xticklabels(nome_dias)
```
![Imgur](https://i.imgur.com/MRVw8Mo.png)

gráfico pizza
```python
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

explodir = [0.1, 0, 0, 0, 0, 0.1, 0.1]

eixo.pie(temperatura_por_dia_da_semana, labels=temperatura_por_dia_da_semana.index,
         autopct='%.1f%%', explode=explodir, shadow=True)
eixo.set_title('Temperatura por dia da semana', fontsize=15, pad=10)
```
