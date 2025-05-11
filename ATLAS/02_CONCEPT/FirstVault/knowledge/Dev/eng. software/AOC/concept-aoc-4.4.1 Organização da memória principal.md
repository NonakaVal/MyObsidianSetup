---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 4.4.1 Organização da memória principal

A memória principal é responsável por armazenar dados e instruções de um programa para serem usados pelo [[aoc.5.oprocessador.organizacao.e.arquitetura|processador]] durante sua execução. Para garantir que esses dados e instruções possam ser acessados de maneira eficiente, eles devem ser organizados em uma estrutura padronizada que permita a identificação do local onde cada um deles está armazenado na memória.

A memória principal é organizada em células que representam um agrupamento de bits, sendo que cada célula possui um endereço único usado pelo processador para acessar seu conteúdo. Cada célula é a menor unidade endereçável em um computador e é constituída por circuitos eletrônicos baseados em semicondutores que permitem o armazenamento de valores 0 ou 1, representando dados ou instruções.

O tamanho de uma célula na memória principal é definido pelo fabricante e determina a quantidade de bits que podem ser armazenados nela. Uma célula com N bits permite armazenar 2N combinações de valores, o que determina a quantidade total de células possíveis na memória. Um tamanho comum de célula é de 8 bits (1 byte).

Se for possível armazenar em uma memória de 2N combinações possíveis de células (cada uma delas contendo dados armazenados), então será possível calcular a capacidade de armazenamento da memória principal, da seguinte forma:

a) se N = 9 bits, tem-se que 2^9 = 512 (células de memória); 

b) se cada célula pode armazenar 8 bits, tem-se que: 512 x 8 = 4KB (4 quilo byte) de espaço em memória.

A memória principal permite o acesso aleatório a cada posição de célula, o que proporciona grande flexibilidade graças à sua tecnologia de fabricação. As duas operações que podem ser realizadas na memória são a escrita (write) para armazenamento de dados e a leitura (read) para recuperação de dados e instruções armazenados na memória.

:luc_link:[CÉLULA DE MEMÓRIA WIKI](https://pt.wikipedia.org/wiki/C%C3%A9lula_de_mem%C3%B3ria_(computa%C3%A7%C3%A3o))