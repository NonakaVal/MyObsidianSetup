---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 6.3.3 Tipo numérico

Como os computadores são elementos binários, a forma mais eficiente de representar números deve ser “binária”, isto é, converter o número diretamente de decimal para seu correspondente valor binário. Deste modo a ULA poderá executar as operações mais rapidamente.

Conforme Monteiro (2007), existem três fatores que devem ser considerados, pois podem acarretar inconvenientes no projeto e na utilização da máquina:

a) a representação do sinal do número;
b) a representação da vírgula (ou ponto) que separa a parte inteira da fracionária de um número não inteiro;
c) a quantidade limite de algarismos possível de ser processada pela ULA.

O problema que consiste do sinal do número pode ser resolvido com o acréscimo de mais um bit na representação do número (adicionado à esquerda), como bit mais significativo. Esse bit adicional indica o sinal do número. A conversão adotada (conforme o Quadro 6.3) é:
– Valor positivo: bit de sinal igual a 0; – Valor negativo: bit de sinal igual a 1




Outro problema reside na forma de representação de números fracionários, por causa da dificuldade de representar a vírgula/ponto internamente, entre a posição de dois bits. O que ocorre é que a vírgula não é efetivamente representada, mais sim assumida sua posição no número e este sendo representado apenas pelos seus algarismos significativos como se fosse inteiro. Exemplo: 110111,110 ⇒ 110111110

O sistema identifica que quantidade de algarismos é inteira e que a quantidade é fracionária através da escolha entre dois modos de representação e de realização de operações aritméticas

a) representação em ponto fixo (vírgula fixa); b) representação em ponto flutuante (vírgula flutuante).

A quantidade de dígitos disponíveis no sistema de computação (processador) para representar números é um problema relevante. Na matemática os números reais existentes são infinitos; no entanto, computadores são má são infinitos; no entanto, computadores são máquinas onde as células e registradores possuem tamanho finito mas que têm capacidade de representar uma quantidade finita de números. Desse modo surge o aspecto denominado overflow ou estouro da capacidade de representar números. Há também o underflow, que se caracteriza por ocorrer um resultado cujo valor é menor que o menor valor representável.