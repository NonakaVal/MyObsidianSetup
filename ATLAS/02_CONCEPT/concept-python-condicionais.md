---
tags:
  - learning
HUB:
  - "[[hub-probabilidade]]"
  - "[[hub-statistic]]"
---

### Condicionais 

- As estruturas condicionais permite que um programa tome decisões com base em uma condição
	- **(if), (else), (elif)**

``` css
idade = 18
if idade >= 18:
	print("adulto")
```
- o comando (if >=18:) seguido da condição (print"adulto")  indentada verifica o valor da  variável (idade), e só execura se a condição for verdadeira.

``` css
idade = 18
if idade >=18:
	print("adulto")
else:
	print("menor")
```

##### multiplos blocos de condicionais 
-  comando (elif)
```css
nota = 7

if nota >= 9:
	print("passou passado")
elif nota >= 7:
	print("passou com 7")
elif nota >= 5:
	print("cagasso")
else:
	print("se fudeu")
```
-  o programa testa várias condições na ordem (elif)
