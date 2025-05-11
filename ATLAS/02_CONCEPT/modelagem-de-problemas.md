---
tags:
  - reading
HUB:
  - "[[hub-logic]]"
---


22-05-2023  21:39  #reading : Algoritmos e Lógica de Programação 3ª ed - Marco A. Furlan de Souza
{modelagem de problemas} {17} {19} 

## Modelagem de Problemas 
- principal responsável pela facilidade ou dificuldade da resolução de um problema
	- Uso da linguagem matemática é Fundamental
		- pela eliminação de duplo sentido
			- o mesmo vale para linguagens para criação de algoritmo(fluoxograma)
				- e linguagens de programação

{exemplos}
### Problema das Canetas
---
*"compraram-se 10 canetas iguais, que foram pagas com uma nota de 100, obtendo-se 67 de troco, quanto custou cada caneta ?"*
uma possível solução:
*"eu tinha 100 e recebi 67, o custo total é a diferença entre os 100 que eu tinha e os 67 de troco, então vale 33, esse valor foi total pago pelas canetas, para saber quanto cada caneta, basta dividir  os 33 por 30, resultado é 1,10"*

----
**Matemáticamente**: sendo x o valor de cada caneta, então, quanto gastei = 30x. Como quanto gastei + troco = 100:

$$30x+67=100$$
$$30x=100-67$$
$$30x=33$$
$$x=\frac{33}{30}$$
$$x=1.1$$
---
**Algoritmo inicial** para solucionar o problema das canetas.
1. pegar os valores 30, 100 e 67
2. subtrair 67 de 100 e dividir o resultado por 30
3. mostrar o resultado
----
#### Solução de caso Geral 1
1. Ler N, Y e Z.
2. Subtrair Y de Z e dividir o Resultado por N
3. Mostrar o resultado 
- porem a proposta apresenta diversas restrições,  esse algoritmo não funciona de forma lógica caso alguém pense em comprar - 3 canetas
	- para isso usamos podemos usar condições, em termos matemáticos:
#### Solução de caso Geral das canetas de forma correta 
1. Ler valores de N, Y e Z
2. se Z>Y  e N>0 e Y>=0 e Z>0 então
	1. subtrair Y de Z e dividir o resultado por Z  
	2. mostrar o resultado
3. senão 
	1. exibir a mensagem de erro

### Algorimo caneta em python
usando variáveis de [[concept-python-recebendo-input|input]] e um algoritmo com [[concept-python-condicionais]] 
```css
y = input("reais de troco\n")
y = int(y)

n = input("n de canetas compradas\n")
n = int(n)

z = input("valor da nota entrege\n")
z = int(z)  

if z > y and n > 0 and y >= 0 and z > 0:
   caneta = z - y
   cadacaneta = caneta / n
   print(cadacaneta)
else:
   print("deu erro")

```

{exercícios}

{recursos adicionais}






