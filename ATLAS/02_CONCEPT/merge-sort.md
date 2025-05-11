---
tags:
  - learning/artigo
HUB:
  - "[[hub-python]]"
  - "[[hub-logic]]"
---
 
Merge Sort (ordenação por junção)

Etapa de divisão
- encontre o meio e separe-a em duas sublistas, esquerda e direita
- com base na sublista esquerda, se a quantidade de elementos for maior que a 1, encontre o meio e separe-a em duas listas: esquerda11 e direita11
- com base na esquerda 11, se a quantidade de elementos for maior que a 1, encontre o meio e separe em duas listas, esquerda12, direita12
- separe até achar uma lista com tamanho 1
- chame a etapa de merge
- repita o processo com todas as sublistas

Etapa de merge:
- dada as duas listas, cada uma das quais contem valor 1, para ordenar , basta comparar esses valores e fazer a troca, gerando sublista com dois valores ordenados
- dada duas listas, cada uma quais contém dois valores, para ordenar, basta ir escolhendo o menor valor em cada uma e gerar uma sublista com quatro valores ordenados
- repita o processo de comparação e junção dos valores até chegar à lista original agora ordenada
algoritmo-merge-sort-image


```css
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
        return merge(esquerda, direita)  # Call the merge() function with both sublists

def merge(esquerda, direita):
    sublista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sublista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sublista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sublista_ordenada += esquerda[topo_esquerda:]
    sublista_ordenada += direita[topo_direita:]

    return sublista_ordenada

lista = [10, 9, 5, 8, 11, -1, 3]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)

```
