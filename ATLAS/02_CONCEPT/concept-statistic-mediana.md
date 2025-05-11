---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-descriptive-analysis]]"
---

## <font color=#39b8fa>3.2 Mediana</font>
***

Para obtermos a mediana de uma conjunto de dados devemos proceder da seguinte maneira:
1. Ordenar o conjunto de dados;
2. Identificar o número de observações (registros) do conjunto de dados ($n$);
3. Identificar o elemento mediano:

> Quando $n$ for ímpar, a posição do elemento mediano será obtida da seguinte forma:
# $Elemento_{Md} = \frac{n+1}2$ 

> Quando $n$ for par, a posição do elemento mediano será obtida da seguinte forma:
# $Elemento_{Md} = \frac{n}2$


4. Obter a mediana:

> Quando $n$ for ímpar:
# $Md = X_{Elemento_{Md}}$

<img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img003.png' width="50%">

> Quando $n$ for par:
# $Md = \frac{X_{Elemento_{Md}} + X_{Elemento_{Md}+1}}2$

<img src='https://caelum-online-public.s3.amazonaws.com/1177-estatistica-parte1/01/img003.png'  width='50%'>

```css
dados['Renda'].median()
```


