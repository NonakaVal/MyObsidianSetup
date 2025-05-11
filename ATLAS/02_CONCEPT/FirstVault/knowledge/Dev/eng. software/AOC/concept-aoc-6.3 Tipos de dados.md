---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 6.3 Tipos de dados

Definem para o sistema como cada dado deverá ser manipulado, pois conforme citado anteriormente, cada tipo de dado recebe um tratamento diferenciado pelo processador.

Exemplo: VAR X:=INTEGER; VAR X:=REAL;

Os termos INTEGER e REAL são interpretados de modo diferente, acarretando alterações significativas tanto no modo de organizar os bits que representam um número quanto na sequência de etapas do algoritmo de execução de uma operação aritmética com o número (MONTEIRO, 2007).

De modo geral, as seguintes formas de dados são mais utilizadas nos programas atuais de computadores (formas primitivas, entendidas pelo hardware) (MONTEIRO, 2007)

– Tipo Caractere: dados sob forma de caractere; 
– Tipo Lógico: dados sob forma lógica; 
– Tipo Numérico: dados sob forma numérica.

Outras formas mais complexas são permitidas em certas linguagens modernas (como tipo REGISTRO, tipo ARRAY, tipo INDEX, tipo POINTER etc.). No entanto, durante o processo de compilação, os dados acabam sendo convertidos finalmente nas formas primitivas já mencionadas, para que o hardware possa executá-las.

![[concept-aoc-1.29-tipo-caractere]]

![[concept-aoc-1.30-tipo-logico]]

![[concept-aoc-1.31-tipo-numerico]]