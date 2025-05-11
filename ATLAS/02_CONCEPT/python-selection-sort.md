---
tags:
  - learning/artigo
HUB:
  - "[[hub-python]]"
  - "[[hub-logic]]"
---


Selection sort (ordenação por seleção)

- 1 - percorre toda a lista, procurando o menor valor e ocupa a posição 0.
- 2 - a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1
- 3 - a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2
- 4 - processo é repetido n-1 vezes, sendo n o tamanho da lista

![[algoritmo-selection-sort.png]]


```python
def selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index = i
        for j in range(i + 1, n):
            if lista[j] < lista[index]:
                 index = j
        lista[i],lista[index] = lista[index], lista[i]
    return lista
lista = [10, 9, 5, 8, 11, -1, 3]
print(selection_sort(lista))
```

[1, 3 ,4,2]
0 1 2  3 = 4

i = 1 < j=3 