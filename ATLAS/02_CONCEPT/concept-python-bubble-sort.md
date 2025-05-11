---
tags:
  - learning/artigo
HUB:
  - "[[hub-python]]"
  - "[[hub-logic]]"
---
# Bubble Sort (Ordenação por Bolha)

## Conceito
Algoritmo simples de ordenação que:
- Compara pares de elementos adjacentes
- Troca suas posições se estiverem na ordem errada
- Repete o processo até a lista estar ordenada

## Funcionamento
1. Seleciona o valor na posição 0 e compara com seu vizinho (posição 1)
   - Se `lista[j] > lista[j+1]`, troca os elementos
   - Senão, mantém na posição atual
2. Avança para o próximo par de elementos
3. Repete o processo até percorrer toda a lista
4. Executa `n-1` iterações (onde `n` = tamanho da lista)

## Implementação em Python
```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                # Troca os elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Exemplo de uso
lista = [10, 9, 5, 8, 11, -1, 3]
print(bubble_sort(lista))  # Output: [-1, 3, 5, 8, 9, 10, 11]

```

