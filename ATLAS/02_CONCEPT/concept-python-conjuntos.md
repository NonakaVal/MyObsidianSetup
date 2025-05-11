---
tags:
  - learning
HUB:
  - "[[hub-math]]"
---

# conjuntos ou .set

- conjuntos é uma coleção de elementos não ordenados e não duplicados, são definidos por { } ou pelo método .set
	- não é possível buscar um elemento especifico dentro de um conjunto por não serem ordenados.

##### Alterações com conjuntos
- os elementos podem ser alterados dentro dos conjuntos, mas não possuem ordem.
	- .add e .remove
```css
conjunto1 = {1, 3, 4}
conjunto2 = set(["nada", 4, "três"])

conjunto1.add(6)
conjunto2.remove("nada")
```
- conjuntos criados e atribuídos nas variáveis "conjunto1" e "conjunto2" com os metodos {} e set.
	- método add adicionando o elemento 6 no conjunto "conjunto1"
	- método remove removendo o elemento "nada" do "conjunto2"


- odem ser usados para criar uma lista um conjunto em repetições apatir de conjuntos de arrays ou tuplas.

```css 
minha_lista = [1, 2, 2, 3, 3, 3, 4, 5, 5]
meu_conjunto = set(minha_lista)
lista_sem_repeticao = list(meu_conjunto)
```
- "minha_lista" é uma array com vários números repetidos
	- meu_conjunto usa o método set para criar um conjunto com essa array, esse conjunto possuí só os valores únicos dessa lista
	- lista_sem_repeticao cria uma lista com o resultado do cojunto
		- resultado desse processo é uma lista [1, 2, 3, 4, 5]

##### operações com conjuntos

[Documentação completa w3scools](https://www.w3schools.com/python/python_sets_methods.asp)

``.union() ``ou | : faz a junção dos conjuntos.
``` css
conjunto1 = {1, 3, 4}
conjunto2 = {2, 3, 4}
conjunto3 = set(["2, 3, 5"]) 

juntar_conjuntos = conjunto1.union(conjunto2) # saída {1, 2, 3, 4, 5}
juntar_conjuntos = conjunto1|conjunto3 # saída {1, 3, 4, '2, 3, 5'}


 # union pode ser trocado pelo operador |
```

``.intersection()`` ou &: interseção é um novo conjunto com os elementos que estão presentes em ambos os conjuntos, que são armazenados em uma variável
``` css
conjunto1 = {1, 3, 4}
conjunto2 = {2, 3, 4}

intersecao = conjunto1.intersection(conjunto2) # intersection() pode ser trocado pelo operador &
```
- Retorno será 3 e 4

``.diference`` ou - : a diferença como um novo conjunto que contem apenas os elementos presentes no primeiro conjunto:
```css
conjunto1 = {1, 3, 4}
conjunto2 = {2, 3, 4}

diferenca = conjunto1.difference(conjunto2) # difference pode ser trocado pelo operador - 

```
- resultado dessa operação é 1
