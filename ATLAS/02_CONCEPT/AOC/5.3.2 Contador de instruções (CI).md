---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 5.3.2 Contador de instruções (CI)

O CI (Counter Instruction) ou Program Counter (PC) é um registrador da CPU que armazena o endereço da próxima instrução a ser buscada e executada da memória principal. É um componente crucial para o controle e sequenciamento da execução dos programas, pois indica qual instrução deve ser executada em seguida. Após a busca e execução de uma instrução, o valor do CI é atualizado automaticamente para apontar para o endereço da próxima instrução na sequência.

#### 5.3.3 Registrador de instruções (RI)

O RI, também chamado de Instruction Register, é um registrador responsável por armazenar temporariamente a instrução a ser executada pela UCP. A UC emite sinais de controle em sequência no tempo para processar a realização de um ciclo de leitura para buscar a instrução na memória e armazená-la no RI. Em seguida, o decodificador de instruções interpreta a instrução e avisa a Unidade de Controle (UC) para que execute as operações necessárias.