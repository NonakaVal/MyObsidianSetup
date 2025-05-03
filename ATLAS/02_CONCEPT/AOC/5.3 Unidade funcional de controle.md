---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 5.3 Unidade funcional de controle

A Unidade Funcional de Controle é responsável por coordenar e controlar o fluxo de informações na [[aoc.5.oprocessador.organizacao.e.arquitetura|Unidade-Central-de-Processamento]] (UCP), garantindo que as instruções sejam buscadas na memória, decodificadas e executadas pela ULA de maneira correta e na sequência adequada. Entre suas principais atividades estão a busca de instruções na memória, a decodificação das instruções, o controle do fluxo de dados e a coordenação da execução das instruções. A UFC é fundamental para o bom funcionamento da UCP, permitindo a execução das tarefas solicitadas pelos programas armazenados na memória.

a) busca da instrução que será executada, armazenando-a em um registrador da UCP;

b) interpretação das instruções a fim de saber quais operações deverão ser executadas pela ULA (ex.: soma, subtração, comparação) e como realizá-las;

c) geração de sinais de controle apropriados para a ativação das atividades necessárias à execução propriamente dita da instrução identificada. Esses sinais de controle são enviados aos diversos componentes do sistema,sejam eles internos à UCP (ex.: a ULA) ou externos (ex.: memória e dispositivos de entrada e saída)

A seguir apresentamos os dispositivos que compõem a Unidade Funcional de Controle – [[1.16-(rdm)-(rem)|RDM,-REM]], [[1.17-(ci)---(ri)|CI,-RI]], [[1.18-decodificador-de-instrucoes|Decodificador-de-Instrucoes]], [[1.15-unidade-funcional-de-controle|UC]], [[1.19-relogio-(clock)|Clock]], os quais estão em destaque na Figura 5.4..