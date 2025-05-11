---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-SistemaOperacional]]"
---
---

---
![[2.20-introducao-a-processos]]


![[2.21-estado.-execucao,-pronto-e-espera]]


:luc_info:
![[2.22-processos-sejam-criados]]

![[2.23-pcb-(process-crontrol-block)]]

:luc_info:
![[2.24-encerrado-quando]]

![[2.25-cpu-bound.io-bound]]


Além disso, há dois canais para realizar a comunicação entre os processos. Eles são chamados de foreground e background. Processos foreground (primeiro plano são aqueles que permitem que o usuário interaja com ele, por exemplo, os de entrada e saída. Já os background (segundo plano) são os processos que não permitem a comunicação com o usuário durante o seu processamento

#### THREADS

Processos podem ser independentes, subprocessos ou threads. Subprocessos são gerados por processos pais e compartilham recursos com eles.

---- 


Processos são programas em execução no computador. Eles são compostos por um conjunto de instruções e dados que são carregados na memória RAM do sistema operacional para serem executados. Um processo pode ser criado por outro processo, chamado de processo pai.

Existem três tipos de processos: independentes, subprocessos e threads. Os processos independentes são aqueles que não têm relação com outros processos, eles iniciam sua execução a partir de um programa ou comando do sistema operacional. Já os subprocessos são gerados por processos pais e compartilham recursos com eles, como memória e arquivos abertos.

![[2.29-threads]]

![[2.26--independentes,-subprocessos-ou-threads]]
 
 ---- 
![[2.31-pipe]]


----
![[2.32-semaforos]]



-----

![[2.33-c)-troca-de-mensagens]]


![[2.34-implementacao-de-theads]]

## Comunicação entre processos e problemas clássicos de comunicação entre processos

![[2.35-comunicacao-entre-processos]]

![[2.36-exclusao-multua]]

![[2.37-algoritimos-controle-de-software-exclusao-mutua]]

Embora existam algoritmos de correção para o problema de exclusão mútua, ainda há a possibilidade de erros de comunicação, o que levou a cientistas a desenvolverem outros algoritmos, como o de Dekker e Peterson, que resolvem o problema da exclusão mútua entre dois ou N processos. O algoritmo de Peterson evita o bloqueio indefinido do processo, inserindo verificação antes da alternância dos processos

Mas, além da exclusão mútua, existem outros mecanismos. Confira a seguir os demais e suas respectivas descrições:

![[2.38-sincronizacao-condicional]]


![[2.32-semaforos]]


---



![[2.39-monitores]]
![[2.40-troca-de-mensagens]]


![[2.41deadlock]]

## Introdução ao escalonamento: conceitos, tipos e escalonamento de threads


 três tipos de estados de processos: execução, pronto e espera.
 
  Um processo fica em espera até que todos os recursos necessários sejam alocados e passa para o estado de pronto. Depois disso, pode ser chamado para processamento e permanecerá em execução até o término da operação. O estado "bloqueado" é semelhante ao estado de "espera", pois depende de um evento para mudar para o estado de execução.

O processo, quando entra em execução, permanece com esse estado até o término do processamento. Quando encerra, é liberado o acesso para outro processo, que deixará o estado de pronto e entrará em execução, e assim por diante. Mas como é possível controlar quais os processos que devem ter prioridade, ou, ainda, quais processos estão na fila para processamento?

Para que isso aconteça, os mecanismos de escalonamento de processos foram desenvolvidos. Alguns critérios de escalonamento são necessários e determinados de acordo com as características do sistema operacional. 

![[2.42-escalonamento]]

![[2.43-preemptivo-ou-preemptivo]]

![[2.44--fifo-(first-in-first-out)]]

![[2.45--(shortest-job-first)]]

![[2.46-cooperativo]]



![[2.47-escalonamento-circular]]

![[2.48-propriedade]]



![[2.49-circular-com-prioridades]]


----


Mas existem outros escalonamentos que visam otimizar ainda mais a organização dos processos e o seu tempo de execução. Podemos citar o escalonamento por múltiplas filas, que, como o próprio nome diz, trabalha com a formação de várias filas que são tratadas de acordo com a importância da aplicação para o sistema operacional ou mesmo a quantidade e a área da memória que será alocada, ou seja, a prioridade não está associada ao processo e sim à fila de processos.

Como processos possuem características de processamento distintas, é difícil que um único mecanismo de escalonamento seja adequado a todos. A principal vantagem de múltiplas filas é a possibilidade da convivência de mecanismos de escalonamento distintos em um mesmo sistema operacional. Cada fila possui um mecanismo próprio, permitindo que alguns processos sejam escalonados pelo mecanismo FIFO, enquanto outros pelo circular 

Existe outro tipo de escalonamento que utiliza múltiplas filas com realimentação, onde o processo muda de fila dependendo da sua prioridade. Isso ajuda a dinamizar o processamento do sistema operacional com base no comportamento do processo. Esse escalonamento segue o princípio FIFO, mas controla o tempo de execução por fatias, ou seja, quanto maior a prioridade da fila, menor será a fatia de tempo que o processo precisará para ser concluído.


## Algoritmos de escalonamento: características, políticas, tipos e exemplos

117

![[2.50-algoritimos-de-escalonamento-de-processos]]


O objetivo da política de escalonamento é maximizar o uso de recursos da máquina, atendendo uma quantidade maior de processos em menor tempo e minimizando tempos de resposta. Além disso, é importante evitar interrupções por tempo indefinido, impor prioridades na escolha de processos e alocação de recursos, reduzir a probabilidade de sobrecarga e melhorar a previsibilidade do tempo mínimo de resposta, espera e execução dos processos.

:luc_info:
*Sobrecarga frequentemente resulta em desperdício de recursos, mas uma certa porção dos recursos do sistema se investida efetivamente como sobrecarga pode melhorar muito o desempenho geral do sistema



![[2.51-politica-de-escalonamento-adequada]]

![[2.52-outros-algoritmos-de-escalonamento.]]

![[2.53-algoritmo-hrrn]]

#### SRT - SPF



Embora o algoritmo SRT teoricamente ofereça tempos de espera mínimos, em certas situações, o SPF pode ser mais vantajoso devido à sobrecarga de preempção. Por exemplo, se um processo quase concluído está em execução e um novo processo com estimativa de tempo pequeno chega, a preempção pelo SRT pode não ser a melhor opção. Uma solução para isso é impedir a preempção do processo em execução quando seu tempo restante alcançar um nível baixo determinado.

#### FSS

O algoritmo de escalonamento por fração justa (FSS) é uma técnica que identifica o grupo de processos que mais necessita de recursos em função de suas operações e determina uma quantidade de recursos para o processamento desse grupo sem comprometer o processamento de outros grupos com menor prioridade em termos de consumo de recursos. O objetivo é distribuir os recursos da forma mais justa possível, levando em consideração a quantidade de recursos utilizados versus o tempo necessário para processar as tarefas.



#### escalonamento por prazo

Outro algoritmo que elencamos é o escalonamento por prazo. Como enfatizado esse algoritmo necessita da requisição prévia de recursos do sistema, com a inserção exata que será necessária para que se cumpra o prazo previsto de processamento de um conjunto de processos.

O escalonamento de processos em tempo real, embora importante, pode levar à sobrecarga de recursos e prejudicar o desempenho da máquina. Para contornar isso, uma estratégia é priorizar a execução dos processos que requerem menos recursos.

#### processos em tempo real

Como mencionado, os algoritmos de escalonamento de processos em tempo real permitem a alocação de algoritmos distintos de acordo com a solicitação que foi realizada. Dessa forma, há algumas classificações para eles. Vejamos:

a) escalonamento de tempo real não crítico: visa garantir que processos em tempo real sejam executados, porém sem a garantia de que cumprirá alguma restrição de tempo;

b) escalonamento de tempo real crítico: ao contrário do anterior, garante o processamento antes do prazo estabelecido;

c) escalonamento de tempo real estático: nesse, as prioridades dos processos são determinadas uma única vez;

d) escalonamento de tempo real dinâmico: estes realizam o escalonamento por prioridades e isso acontece durante a execução dos processos. Pode haver a interrupção preemptiva, de acordo com as necessidades de alocação identificadas, de forma a preencher, inclusive, os espaços considerados de folga entre a seleção de processos ou de execução. Essa folga refere-se ao tempo restante ao processo para que seja finalizada a sua execução.


#### escalonamento de thread  Java 

O escalonamento de thread Java é tratado de forma distinta para usuários e núcleo no sistema operacional. As considerações sobre quantidade, ordem e prioridade das threads devem ser definidas pelo responsável pela implementação em nível de software, utilizando algoritmos como o de fração justa, alternância circular ou por intervalo de tempo. O objetivo é garantir um bom desempenho da máquina.

:luc_info:

É importante lembrar que todas as aplicações em Java são multithread, ou seja, utilizam threads. Em Java, os threads possuem níveis de prioridade que variam entre 0 e 1, sendo Thread.MIN_PRIORITY e Thread.MAX_PRIORITY os valores constantes definidos para a prioridade mínima (1) e máxima (10), respectivamente.

Threads Prontos
1. Um thread pode ser executado até o encerramento das instruções
2. Pode sair de execução e entrar em espera, para que outro processo de maior prioridade seja escalonado
3.  Pode sofrer preempção para que outro thread de maior prioridade seja executado.
4. O thread de maior prioridade pode executar todo o tempo até o seu encerramento ou, se for multithread, poderá realizar a alternância circular.

