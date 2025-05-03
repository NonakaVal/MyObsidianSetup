---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 5.3.4 Decodificador de instruções

O Registrador de Instrução (RI) armazena temporariamente a instrução a ser executada pela Unidade Central de Processamento (UCP). A UCP emite sinais de controle em sequência para buscar a instrução na memória e armazená-la no RI. A função do decodificador de instrução é identificar qual operação será realizada a partir da instrução cujo código de operação foi decodificado. Cada instrução possui uma identificação única e o RI passa a sequência de bits !representando a instrução ao decodificador.



Um decodificador de instruções é um elemento da Unidade Central de Processamento (UCP) que identifica a operação a ser realizada a partir do código de instrução contido no Registrador de Instruções (RI). Ele possui 2^n saídas, sendo n a quantidade de algarismos binários do valor de entrada. O decodificador envia o resultado da decodificação à Unidade de Controle (UC), que emite os sinais de controle necessários para os demais elementos da UCP realizarem a operação especificada pela instrução.

O decodificador de instruções é um componente da UCP que interpreta o código de operação de uma instrução e identifica a operação que deve ser realizada. Ele é essencial para a execução de instruções em processadores CISC (Complex Instruction Set Computer), que utilizam um conjunto grande e complexo de instruções de máquinas. Na arquitetura CISC, as instruções de máquina são operações básicas que o hardware realiza diretamente.

:ril_information:
*Ciclo de instrução: É o período de tempo no qual a UCP lê e processa uma instrução armazenada na memória, ou ainda, pode ser definido pela sequência de ações que a UCP realiza para executar cada instrução de um programa.