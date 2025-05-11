---
tags:
  - learning/artigo
HUB:
  - "[[hub-python]]"
  - "[[hub-logic]]"
---
 
Insertion sort ( ordenação por inserção)

- 1: parte do princípio de que a lista possui um único valor e, consequentemente, está ordenada
- 2: - parte do princípio de que um novo valor precisa ser inserido na lista, nesse caso ele é comparado com o valor já existente para saber se precisa ser feira uma troca de posição.
- 3: parte-se do princípio de que um novo valor precisa ser inserido da lista, nesse caso, ele é comparado com os valores já existentes para saber se precisam ser feitas trocas de posições
- 4: iteração n, parte-se do princípio de que um novo valor precisa ser inserido na lista, nesse caso, ele é comparado com todos os valores já existentes (desde o inicio), para saber se precisam ser feitas trocas de posição

algoritmo-insertion-sort-image

```css
def insertion_sort(lista):
	n = len(lista)
	for i in range(1, n):
		valor_inserir = lista[i]
		j = i -1
		
		while j >=0 and lista[j] > valor_inserir:
			lista[j + 1] = lista[j]
			j -= 1
		lista[j +1] = valor_inserir
	return lista
lista = [10, 9, 5, 8, 11, -1, 3]
```