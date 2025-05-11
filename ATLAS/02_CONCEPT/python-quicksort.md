---
tags:
  - learning/artigo
HUB:
  - "[[hub-logic]]"
  - "[[hub-python]]"
---


Quicksort ( ordenação rápida)


- 1 quebra a lista através de um valor chamado pivô, após a quebra os valores que são menores que o pivô ficará a esquerda e os maiores à sua direita, o pivô é inserido no local adequado, trocando posição com o valor atual.
- 2 Há duas listas, da direta e a esquerda do pivô, novamente é escolhido um novo pivô e é feito o mesmo processo.
- 3 olhando para as duas novas sublistas, repete-se o processo de escolha dos pivôs e separação
- 4 na ultima iteração, a lista estará ordenda

![[algoritimo-quicksort.png]]


```css
def quick_sort(lista, inicio, fim):

    if inicio < fim:
        pivo = particao(lista, inicio, fim)
        quick_sort(lista, inicio, pivo -1)
        quick_sort(lista, pivo +1, fim)
    return lista

def particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[direita], lista[fim] = lista[esquerda], lista[direita]

    return esquerda
```