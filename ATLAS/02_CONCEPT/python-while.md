---
HUB:
  - "[[hub-python]]"
tags:
  - learning
---

##### while 

[[concept-python-contador-e-acumulador]]

- Loop while repete um bloco enquanto a condição for verdadeira:
```css
i = 0
while i < 5:
	print(i)
	i += 1
```
- loop verifica a condição (i<5) enquanto não for execula o loop (i+=1) 
	- retorna na impressão dos valores de 0 a 4

- while com if 
``` css
total = 0
while True:
	valor = float(input("digite o valor da compra: \n"))
	total = total + valor
	continuar = input ("deseja continuar? (s/n)")
	if continuar != "s":
		break
print("o valor total da compra é:", total)
```
- cria um loop sobre as condições de input e soma os valores armazenados nas variáveis
	- "froat" converte o valor para um número decimal
	- "break" comando que para o loop com base na condição de terminada no operardor do "if"

- exemplo  2
``` css
total = 0
continuar = "s"

while continuar == "s":
	valor = float(input("digite o valor da compra: \n"))
	total = total + valor
	continuar = input ("deseja continuar? (s/n)")
	
print("o valor total da compra é:", total)
```


![[concept-python-for.in]]