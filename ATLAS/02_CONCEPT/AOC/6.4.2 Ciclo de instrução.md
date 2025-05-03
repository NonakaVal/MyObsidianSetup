---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 6.4.2 Ciclo de instrução

A partir da proposta da arquitetura de Von Neumann, da qual os conceitos básicos ainda são válidos, propunha-se que as instruções fossem executadas sequencialmente (a não ser pela ocorrência de um desvio), uma a uma. O contador de instruções indica a sequência de execução, isto é, o CI controla o fluxo de execução das instruções. A seguir (Figura 5.13) é ilustrado o ciclo de execução de uma instrução. Em seguida, é descrita em mais detalhes cada uma das fases



##### 6.4.2.1 Fase 1

A UCP busca o código de operação (Opcode) na memória principal, o qual está localizado no endereço contido no CI (endereço da próxima instrução a ser executada) e armazena-o no Registrador de Instrução (RI): RI ← (CI)

Micro-operações da fase 1,

a) a UC lê o conteúdo do CI (endereço da próxima instrução) e coloca o endereço no REM; 
b) a UC envia um sinal – via barramento de controle – à controladora da memória principal para que realize uma operação de leitura;
c) a memória principal lê o endereço que está no REM – via barramento de endereço – e busca o conteúdo da célula referenciada;
d) a memória principal coloca no RDM – via barramento de dados – o conteúdo da célula;
e) a controladora da memória principal envia à UC – via barramento de controle – o sinal de leitura concluída;
f) a UC transfere o código de operação (conteúdo que está no RDM) ao RI.


##### 6.4.2.2 Fase 2

O Decodificador de Instrução decodifica (interpreta) o Código de Operação (Opcode) contido no RI

a) o RI envia para o decodificador de instrução os bits correspondentes ao Opcode;
b) o Decodificador de Instruções determina quantas células a instrução ocupa e identifica a operação a ser realizada;
c) a UC envia um sinal de controle à ULA informando a operação a ser realizada e incrementa o CI para apontar para a próxima instrução: CI → (CI+N), onde, N = nº de células que a próxima instrução ocupa.


##### 6.4.2.3 Fase 3
A UC busca (se houver) o(s) dado(s) (Operandos): RI ← (Op)

Micro-operações da fase 3:
a) a UC envia um sinal – via barramento de controle – à controladora da memória principal para que realize uma operação de leitura;
b) a memória principal lê o endereço que está no REM – via barramento de endereços – e busca o conteúdo da célula referenciada; 
c) a memória coloca no RDM – via barramento de dados – o conteúdo da célula lida;
d) a memória principal envia à UC – via barramento de controle – um sinal de leitura concluída; 
e) a UC transfere o operando (conteúdo do RDM) ao RI (se for um código de operação) ou a um dos registradores internos da UCP (se for um dado).

Obs.: Esta fase se repete até que sejam trazidos para dentro da UCP todos os operandos necessários à execução da instrução.

##### 6.4.2.4 Fase 4

A UC comanda a execução da instrução (a operação é executada sobre o(s) dado(s));

a) a ULA executa a instrução sobre os dados disponíveis nos registradores;

b) ao concluir a operação, a ULA envia um sinal para a UC informando que a execução terminou;

c) a UC identifica o endereço de memória para onde deve ser enviado o resultado da operação e o armazena no REM;

d) a UC autoriza o envio do resultado da operação para o RDM;

e) a UC autoriza a controladora de memória a realizar uma operação de leitura no REM para obter o endereço de memória onde deverá ser escrito o resultado e uma leitura no RDM para obter o resultado a ser escrito na memória


  
##### 6.4.2.5 Fase 5

Se o programa tiver terminado, pára; senão, volta à Fase 1