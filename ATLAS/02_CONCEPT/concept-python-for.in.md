---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---


-  for/in em python é uma estrutura que percorrer elementos de uma sequência, e é útil quando é preciso executar uma mesma operação em cada elemento da sequência:

##### for in aplicado a um dicionário
```css
notas = {
	"joão":10,
	"maria":8,
	"henrique":10, 
}

for lista in notas.items():
	print(lista)
```
- for percorre todo o dicionário "notas" e armazena da variável lista.


##### separando variáveis no for in
[[concept-python-dicionarios|-metodos-.items()-para-separar-nas-variaveis:]]

```css
notas = {
	"joão":10,
	"maria":8,
	"henrique":10, 
}

for k, v in notas.items():
	v = v + 1
	print(v)
	
```
- tornará uma lista dos valores dos "values" do dicionário armazenados na variável "v" que então é somado 1, 
	- 11, 9, 11 

```
for lab, row in cars.iterrows() :

    print(lab)

    print(row)
```