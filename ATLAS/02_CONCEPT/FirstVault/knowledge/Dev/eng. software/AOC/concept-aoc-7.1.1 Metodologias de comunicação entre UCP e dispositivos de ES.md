---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 7.1.1 Metodologias de comunicação entre UCP e dispositivos de E/S

Para que a UCP se comunique com a memória principal e os dispositivos de E/S, é necessário definir endereços para cada posição de memória e para cada periférico. Assim, a UCP pode indicar o endereço correto para acessar as informações desejadas.

Cada periférico de E/S possui um endereço de porta único no sistema, que é identificado por um número de oito bits. Isso significa que até 256 dispositivos podem ser conectados ao sistema, cada um com seu próprio endereço de porta.

Diversas formas de comunicação entre UCP e memória principal foram propostas, as quais sofreram melhorias ao longo do tempo, buscando sempre alcançar uma melhor utilização da UCP e um melhor desempenho para o sistema como um todo. Murdocca (2000) destaca três métodos para gerenciar a entrada e saída:


a) Entrada e saída programada

Neste método, também chamado de pooling, a UCP precisa verificar continuamente se cada um dos dispositivos necessita de atendimento, ou seja, tudo depende da UCP. Por exemplo, se o disco quer transferir algum dado para a memória, a UCP deve ficar dedicada a esse processo de transferência até que esta seja concluída. A grande desvantagem é a subutilização da UCP, a qual, enquanto houver uma operação de transferência de dados, não realiza outras operações de processamento. Este método não é mais utilizado.,

b) Entrada e saída controladas por interrupção

Este método possibilita que a UCP não fique presa em espera ocupada até que um dispositivo esteja pronto para realizar a transferência de dados propriamente dita. Assim, a UCP dá início à operação emitindo uma instrução de E/S para a interface ou controlador do dispositivo em questão e, quando o dispositivo estiver pronto para a operação de transferência, recebe uma interrupção avisando que ela poderá começar. Essa demora para iniciar a transferência, após as instruções da UCP, deve-se à lentidão dos dispositivos de E/S em relação à UCP, problema que é diminuído com o uso de interrupções. Este método sofreu melhorias e não é mais utilizado.
:ril_information:
*Interrupção: pode ser definida como um evento ou um aviso à UCP de que algum dispositivo está solicitando a realização de uma operação (ex.: o recebimento de dados via rede, a pressão de uma tecla). Quando uma interrupção ocorre, a UCP deve suspender imediatamente a execução de seu programam corrente e começar a executar um procedimento de tratamento da interrupção

c) Acesso direto à memória (DMA)