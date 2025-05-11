---
tags:
  - learning/review
  - 
HUB:
  - "[[hub-python]]"
---


-  S�o uma sequ�ncia mut�vel de elementos que podem ser acessados por um �ndice, podem ter elementos de diferentes tipos.
	- podem ser constru�das de v�rias maneiras:
		- par de colchetes []
		- usando um construtor tipo list()
- list comprehension
	- listas criadas a partir de objetos por algum crit�rio exemplo: [[split]]

``` css
notas = [8, 1, 9]
#indice [0, 1, 2]

print (notas[2])
```
- A lista "notas" com a sequencia armazenada em [] sendo o indice sendo chamado em "notas[de 0 a 3]" ou valor m�ximo de de valores armazenados na lista
	- um �ndice sempre come�a no 0


### .enumerate()
- usada para iterar sobre uma fun��o enquanto acompanha o �ndice de cada elemento:
```css
lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "ma�a"]

for i, item in enumerate(lista):

� � print(f"posi��o= {i},\t valor {item}" �)
```



### map() e lambda: 
- permite aplicar uma fun��o em  cada elemento de uma ou mais iter�veis: [[concept-python-conjuntos]], [[tuplas]] , [[concept-python-arrays]]

```css
linguagens = "pyhton java js c c# c++".split()

nova_lista = map(lambda x: x.upper(), linguagens)

nova_lista = list(nova_lista)
```
- [[split]] divide a string
	- map � o metodo que atribui a fun��o sobre cada elemento da lista criada
		- [[concept-lambda]] cria a fun��o que vai ser atribu�da

### filter()
```css
numeros  = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
```
-  filter() � o metodo que verifica a fun��o sobre cada elemento da lista criada
	- [[concept-lambda]] cria a fun��o que vai ser atribu�da


### Altera��es em uma array

##### Inser��o de dados
.append()  
```css
notas = [8, 1, 9]
#indice [0, 1, 2]

notas.append(50)
```
- adiciona o valor em "()" no final da lista
	-  resultado da lista : notas =  [8, 1, 9, 50]

.insert()
```
notas = [8, 1, 9]
#indice [0, 1, 2]

notas.insert(1, 8)
```
- m�todo insert insere o valor "8" no �ndice 1 do array "notas".
	- os valores avan�am um n�mero no indice para se adaptar a inser��o
		- resultado da inser��o: notas = [8, 8, 9, 50] , com indice [0, 1, 2, 3]


### Remo��o de dados
.pop()
```css
notas = [8, 1, 9]
#indice [0, 1, 2]

x = notas.pop()
notas.pop(1)
```
- ".pop()" sem determinar um valor em () retorna na remo��o do ultimo item na lista "notas" no caso "9", indice "2", que por sua vez pode ser armazenado em uma vari�vel "x"
	- .pop(1) pode ser usado para indicar qual indice vai ser removido, nesse exeplo o valor "1" tamb�m no indicide "1"


### Ordem do Array
.sort() 
```css
notas = [8, 1, 9]
#indice [0, 1, 2]
notas.sort()
notas.sort(reverse=True)
```
- ".sort()" organiza em ordem o indice notas 
	- resultado: notas = [1, 8, 9]
- "sort(reverse=True)" organiza na ordem inversa
	- resultado = notas = [9, 8, 1]
- n�o cria uma nova lista, mas sim no modo inplace diretamente na lista


sorted()
```css
lista_ordenada1 = sorted(lista)
```
- pode ser armazenado em uma vari�vel.
	- cria uma nova lista n�o alterando a original


### Calcular m�dias de notas com arrays

``` css
notas =[8, 9, 10, 7.5, 5, 6]
i = 0
total = 0
qtd = len(notas)

while i < qtd:
	total = total + notas[i]
	i = i + 1

print ("total", total)
media = total/qtd
print ("m�dia", media)

```
- "notas", lista de notas com que pode receber tipos diferentes de dados
- vari�veis "i". "total" e "qtd' para opera��es
	-  m�todo "len" � usado para retonar o tamanho ou numero de elementos de uma sequencias, no caso da lista notas: 6
- while cria o loop para execu��o de contagem das notas na lista, "i = i +1 " at� que o valor de i chegue no valor da vai�vel "qtd" determinado no while
- por fim a m�dia � calculada pela divis�o dos resultados
