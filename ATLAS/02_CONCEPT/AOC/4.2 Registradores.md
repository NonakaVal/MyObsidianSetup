---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 4.2 Registradores

A memória tem a função de armazenar dados para serem utilizados pelo processador, que busca esses dados e instruções e os deposita temporariamente nos registradores para realizar as operações solicitadas utilizando seus demais componentes.

Os registradores são dispositivos que armazenam temporariamente dados intermediários durante o processamento realizado pelo processador. Eles surgiram da necessidade de armazenar dados enquanto se aguarda por outras informações para realizar operações subsequentes, por exemplo, armazenando o resultado de uma operação até que um dado da memória esteja disponível para realizar uma nova operação.

Os registradores são um tipo de memória extremamente rápida e cara, localizados dentro do processador (CPU), que armazenam temporariamente dados intermediários durante o processamento. Eles possuem capacidade limitada, mantendo apenas uma palavra de dados por registrador.

---- 

Os registradores são elementos de armazenamento temporário localizados na [[1.13-organizacao-do-processador|UCP]] e sua tecnologia de fabricação permite que sejam extremamente rápidos. As UCPs são fabricadas com uma quantidade de registradores que são usados para armazenar dados que estão sendo processados, servindo como memória auxiliar básica da [[1.14-unidade-logica-e-aritmetica-(ula)|ULA]]
A quantidade e o emprego dos registradores variam bastante de modelo para modelo de processador. Devido à sua tecnologia de construção e por estarem localizados no interior da [[1.13-organizacao-do-processador|UCP]], são muito caros e, por isso, disponíveis em quantidade limitada.

Nos sistemas mais antigos, o registrador especial chamado acumulador (ACC) era usado para armazenar dados e como elemento de ligação entre a [[1.14-unidade-logica-e-aritmetica-(ula)|ULA]] e os outros dispositivos da UCP. Em computadores mais simples, há apenas um acumulador, enquanto em arquiteturas mais complexas, vários registradores podem desempenhar as funções do acumulador, além de haver diversos registradores de dados de uso geral.

O tamanho da palavra dos registradores está vinculado ao projeto de fabricação da UCP e corresponde ao tamanho dos elementos ligados à área de processamento, incluindo a [[1.14-unidade-logica-e-aritmetica-(ula)|ULA]] e os registradores de dados. A capacidade de processamento de uma UCP é influenciada pelo tamanho da palavra, que atualmente pode ser de 32 bits ou 64 bits, conforme a arquitetura do computador.


:luc_info:
*palavra De forma genérica o termo palavra é um grupo de bits de tamanho fixo que é processado em conjunto em um computador. O número de bits em uma palavra (comprimento da palavra) é uma característica importante de uma arquitetura de computador. A maioria dos registradores em um computador possui o tamanho da palavra.