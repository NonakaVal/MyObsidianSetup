---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---



### Tuplas

- usando parênteses()
	- contrutor tuple()


-  estruturas de dados imutáveis ordenada para armazenar conjunto de elementos
	- é parecido com Arrays, divergindos em algumas regras e aplicações
		- são criados indices tal como em arrays
```css
turma = (
	("nono ano", 3)
	[8, 8, 9]
)
```
- Estrutura tupla armazenando outra tupla ("nono ano", 3) e uma array [8, 8, 9] nos indices [0] e [1]
	- os valores em uma tulipa não podem ser mudados

###### descompactação da tupla

```css
pessoa = ("gabriel", 27, True)

nome, idade, admin = pessoa
```
- os valores nos indices [0], [1] e [2] são armazenados em ordem nas variáveis "nome", idade e admin.
 