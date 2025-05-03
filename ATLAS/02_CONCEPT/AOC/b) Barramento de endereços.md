---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### b) Barramento de endereços

O barramento descrito interliga o [[1.16-(rdm)-(rem)|REM]], localizado na [[1.13-organizacao-do-processador|UCP]], à memória principal, permitindo a transferência unidirecional dos bits que representam um endereço de memória onde se localiza uma instrução ou dado a ser executado. Ele é composto por tantas vias de transmissão quantos são os bits que representam o valor de um endereço. Somente a UCP aciona a memória principal para realizar operações de leitura ou escrita através desse barramento.

Seguindo o exemplo anterior, no antigo PC-XT, este barramento possuía 20 linhas: com isso era possível utilizar endereços de no máximo 20 bits. Logo, o maior endereço possível, será:

2^20 = 1.048.576 Bytes = 1 MB

O tamanho do barramento de endereços determina a quantidade máxima de armazenamento de dados que a memória principal pode dispor. No caso descrito, a capacidade máxima de armazenamento da memória RAM é de 1MB devido ao tamanho do barramento de endereços. Atualmente, os barramentos possuem grande capacidade de armazenamento, como por exemplo, 32, 64 ou 128 bits, possibilitando grandes espaços para armazenamento na memória principal.