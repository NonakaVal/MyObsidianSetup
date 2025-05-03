---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
🔗[ACERVOLIMA](https://acervolima.com/arquitetura-do-computador-taxonomia-de-flynn/)

A classificação de Flynn é uma maneira de categorizar arquiteturas de computadores em quatro tipos, de acordo com a maneira como os dados e as instruções são processados. Essa classificação foi proposta por Michael J. Flynn em 1966 e ainda é amplamente utilizada para descrever as arquiteturas de computadores modernos.

Os quatro tipos de classificação de Flynn são os seguintes:

## SISD

1. SISD (Single Instruction Single Data): Uma única instrução é executada em um único conjunto de dados. Essa é a configuração mais simples e é usada em computadores de processamento sequencial, como um PC.

O sistema SISD (Single Instruction Single Data) é uma das quatro categorias de sistemas de processamento propostos pela classificação de Flynn. Esse tipo de sistema é caracterizado pela execução de uma única instrução em um único conjunto de dados em um único processador. É um sistema sequencial simples em que as instruções são executadas uma após a outra e o processador processa apenas um conjunto de dados por vez.

O sistema SISD é usado em computadores comuns, como os PCs, onde um único processador executa as instruções sequencialmente em uma única tarefa. A CPU busca cada instrução da memória e executa-a em um único conjunto de dados armazenado nos registradores. Depois de executar uma instrução, a CPU busca a próxima instrução na memória e executa-a no próximo conjunto de dados, e assim por diante.

Embora o sistema SISD seja simples, ele é eficiente para tarefas que não requerem muita capacidade de processamento. É uma arquitetura útil para programas que exigem muito controle, como sistemas operacionais, programas de controle de dispositivos e outros aplicativos de tempo real.

No entanto, para tarefas que exigem grande capacidade de processamento, o sistema SISD pode ser ineficiente e lento. Nesses casos, outras arquiteturas, como sistemas SIMD ou MIMD, são mais adequadas para lidar com grande quantidade de dados e execução simultânea de várias instruções.



## SIMD

2.  SIMD (Single Instruction Multiple Data): Uma única instrução é executada em vários conjuntos de dados ao mesmo tempo. Essa configuração é usada em arquiteturas de computadores paralelos que operam com grande quantidade de dados em paralelo, como processadores gráficos (GPU).

A arquitetura SIMD (Single Instruction Multiple Data) é uma das quatro categorias de sistemas de processamento propostos pela classificação de Flynn. Esse tipo de sistema é caracterizado pela execução simultânea de uma única instrução em múltiplos conjuntos de dados por vários processadores.

Na arquitetura SIMD, cada processador executa a mesma instrução em seu próprio conjunto de dados. Esses processadores podem estar contidos em uma única CPU ou distribuídos em várias CPUs em um cluster. Isso permite que a mesma operação seja executada em vários dados simultaneamente, o que é útil para tarefas que exigem grande capacidade de processamento, como processamento de imagens, processamento de áudio e vídeo, modelagem e simulação.

Por exemplo, imagine que um aplicativo precisa calcular a soma de dois vetores de 100 elementos. Na arquitetura SIMD, um conjunto de processadores executa a mesma instrução de adição em cada elemento do vetor ao mesmo tempo. Isso pode ser feito em um único ciclo de clock da CPU, ao contrário do sistema SISD, que exigiria 100 instruções de adição sequenciais.

A arquitetura SIMD pode ser eficiente para tarefas que podem ser paralelizadas e podem ser divididas em operações que podem ser executadas em paralelo. No entanto, a eficiência depende do tamanho dos conjuntos de dados e do número de processadores. Se o tamanho dos conjuntos de dados for pequeno, a arquitetura SIMD pode ser menos eficiente do que a arquitetura SISD, que executa as instruções sequencialmente.



## MISD

3.  MISD (Multiple Instruction Single Data): Múltiplas instruções são executadas em um único conjunto de dados. Essa configuração é rara e é usada em sistemas de redundância para fornecer tolerância a falhas em sistemas críticos.

A arquitetura MISD (Multiple Instruction Single Data) é uma das quatro categorias de sistemas de processamento propostas pela classificação de Flynn. Nesse tipo de arquitetura, vários processadores executam instruções diferentes na mesma fonte de dados.

Essa arquitetura é pouco comum em sistemas de computação comercial, mas pode ser usada em sistemas de missão crítica, como processamento de imagens médicas, controle de tráfego aéreo e sistemas de segurança, onde é necessário redundância e tolerância a falhas.

Em um sistema MISD, vários processadores executam instruções diferentes na mesma fonte de dados. Cada processador executa uma instrução diferente, mas em paralelo, em um único conjunto de dados. Cada processador pode ter uma instrução diferente, o que pode ser útil em situações onde a redundância é necessária. Se um processador falhar, outro pode assumir seu lugar sem interromper o processamento de dados.

No entanto, a arquitetura MISD é raramente usada porque é difícil encontrar tarefas que possam ser executadas dessa maneira. Além disso, a redundância oferecida por essa arquitetura pode ser fornecida por outras arquiteturas, como a arquitetura MIMD, que permite que múltiplos processadores executem tarefas independentes simultaneamente.


## MIND


4.  MIMD (Multiple Instruction Multiple Data): Múltiplas instruções são executadas em múltiplos conjuntos de dados ao mesmo tempo. Essa é a configuração mais complexa e é usada em arquiteturas de computadores paralelos que executam várias tarefas simultaneamente, como clusters de servidores e supercomputadores.                                                                 



Máquinas MIMD são amplamente classificados em **memória compartilhada MIMD** e **MIMD de memória distribuída** com base na maneira PEs são acoplados à memória principal.

No modelo **MIMD de memória compartilhada** (sistemas multiprocessadores fortemente acoplados), todos os PEs são conectados a uma única memória global e todos têm acesso a ela. A comunicação entre os PEs neste modelo ocorre através da memória compartilhada, a modificação dos dados armazenados na memória global por um PE é visível para todos os outros PEs. Os sistemas MIMD representativos dominantes de memória compartilhada são as máquinas Silicon Graphics e o SMP (Symmetric Multi-Processing) da Sun / IBM.  

Em **memória distribuída MIMD**  máquinas (sistemas multiprocessadores fracamente acoplados), todos os PEs têm uma memória local. A comunicação entre PEs neste modelo ocorre através da rede de interconexão (o canal de comunicação entre processos, ou IPC). 

A rede que conecta os PEs pode ser configurada para árvore, malha ou de acordo com o requisito.  
A arquitetura MIMD de memória compartilhada é mais fácil de programar, mas é menos tolerante a falhas e mais difícil de estender em relação ao modelo MIMD de memória distribuída. Falhas em um MIMD de memória compartilhada afetam todo o sistema, ao passo que este não é o caso do modelo distribuído, no qual cada um dos PEs pode ser facilmente isolado. Além disso, as arquiteturas MIMD de memória compartilhada têm menos probabilidade de escalar porque a adição de mais PEs leva à contenção de memória. Esta é uma situação que não ocorre no caso da memória distribuída, em que cada PE possui a sua própria memória. Como resultado de resultados práticos e requisitos do usuário, a arquitetura de memória distribuída MIMD é superior aos outros modelos existentes.


## segunda parte



