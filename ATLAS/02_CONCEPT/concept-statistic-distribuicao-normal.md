---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
---


[[concept-statistic-distribuicao-normal-(gaussiana)]] com [[scipy.stats.norm]]

>Probema

Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma **distribuição aproximadamente normal**, com **média 1,70** e **desvio padrão de 0,1**. Com estas informações obtenha o seguinte conjunto de probabilidades:


> **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
> <img src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img004.png' width='350px'>
```css
# probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.
from scipy.stats import norm

media = 1.7
desvio_padrao = 0.1
Z = (1.8 - media) / desvio_padrao

probabilida = norm.cdf(Z)
```


 
 > **B.** Probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.  
  <img  src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img005.png' width='350px'> 


```css
# probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros
z_superior = (1.8 - media) / desvio_padrao
z_inferior = (1.6 - media) / desvio_padrao

probabilidade = norm.cdf(z_superior) - norm.cdf(z_inferior)

probabilidade

# probabilidade1 = norm.cdf(z_superior) - (1 - norm.cdf(z_superior)) # considerando a simetria do gráfico
```


> **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.
{estudos para provas}

<img src='https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img006.png' width='350px'>
```css
# probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

z = (1.9 - media) /  desvio_padrao

probabilidade = 1 - norm.cdf(z)
probabilidade.round(3)
```
