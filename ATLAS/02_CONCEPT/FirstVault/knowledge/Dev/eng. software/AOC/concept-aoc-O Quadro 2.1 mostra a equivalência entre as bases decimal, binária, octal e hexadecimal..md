---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### O Quadro 2.1 mostra a equivalência entre as bases decimal, binária, octal e hexadecimal.




#### 2.1.2.1 Base binária para base octal ou hexadecimal


Observe que os dígitos octais e hexadecimais correspondem à combinações de 3 (para octais) e 4 (para  hexadecimais) bits (ou seja, da representação binária – disponível na tabela de equivalências apresentada anteriormente), permitindo a fácil conversão entre estes sistemas.



#### 2.1.2.2 Base octal ou hexadecimal para base binária

A conversão inversa de octal ou hexadecimal para binário deve ser feita a partir da representação binária de cada algarismo do número, seja octal ou hexadecimal.

#### 2.1.2.3 Base octal para base hexadecimal (e vice-versa)

A representação binária de um número octal é idêntica à representação binária de um número hexadecimal, a conversão de um número octal para hexadecimal consiste simplesmente em agrupar os bits não mais de três em três (octal), mas sim de quatro em quatro bits (hexadecimal), e vice-versa.,

#### 2.1.2.4 Base B (qualquer) para base decimal


101101² = ?^10
b = 2, n = 6
Portanto: 1 x 2^5  + 0 x 2^4 + 1 x 2^3 + 1 x 2^2 + 0 x 2^1 + 1 x 2^0 = 32 + 8 + 4 + 1 = 45^10
Logo: 101101² = 45^10

27^8 = ?^10
b = 8, n = 2
Portanto: 2 X 8¹ + 7 X 8^0 = 23^10
Logo: 27^8 = 23^10

2A5^16 = ?^10
b = 16, n = 3
Portanto: 2 X 16² + 10 X 16¹ + 5 X 16^0 = 512 + 160 + 5 = 677^10
Logo: 2A5^16 = 677^10



#### 2.1.2.5 Base decimal para base B (qualquer)

Consiste no processo inverso, ou seja, efetuamos divisões sucessivas do número decimal pela base desejada, até que o quociente seja menor que a referida base. Utilizamos os restos e o último quociente (a começar dele) para formação do número desejado, conforme Quadro 2.2.