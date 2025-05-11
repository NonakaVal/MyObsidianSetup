---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### c) Barramento de controle

O barramento de controle interliga a [[1.15-unidade-funcional-de-controle|Unidade-de-Controle-(UC)]] da [[1.13-organizacao-do-processador|UCP]] aos demais componentes do sistema computacional, como a memória principal e os componentes de entrada e saída, para a passagem de sinais de controle gerados pelo sistema. Exemplos de sinais de controle são: leitura e escrita de dados na memória principal, leitura e escrita de componentes de entrada e saída, certificação de transferência de dados, pedido de interrupção e relógio (clock), que é responsável por sincronizar os pulsos de eventos durante o funcionamento do sistema.

O barramento de controle é bidirecional e permite a troca de sinais de controle entre a Unidade de Controle (UC) da UCP e os demais componentes do sistema computacional, como a memória principal. A UCP pode enviar sinais de controle para a memória principal indicando uma operação de leitura ou escrita, enquanto a memória principal pode enviar sinais de espera (wait) para a UCP aguardar o término de uma operação.

:luc_info:
*Interrupção: É um aviso gerado à UCP comunicando que um dispositivo deseja realizar uma operação (ex.: leitura de dados de um pen-drive, transferência de dados do disco rígido para a memória, chegada de um pacote de dados da rede).