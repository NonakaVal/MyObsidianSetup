---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### a) Barramento de dados

O barramento descrito interliga o [[1.16-(rdm)-(rem)|RDM]]  localizado na [[1.13-organizacao-do-processador|UCP]], à memória principal, permitindo a transferência bidirecional de instruções e dados a serem executados. O desempenho do sistema é diretamente afetado pela largura do barramento, que determina a quantidade de bits transferidos por vez. Quanto maior a largura, mais rapidamente os dados são transferidos entre a [[1.13-organizacao-do-processador|UCP]] e a memória principal.

Os primeiros computadores pessoais (ex.: PC-XT) possuíam barramento de dados de oito vias, ou seja, capaz de transferir oito bits por vez. Atualmente, conforme a arquitetura do processador, podem existir barramento de dados de 32, 64 ou 128 bits