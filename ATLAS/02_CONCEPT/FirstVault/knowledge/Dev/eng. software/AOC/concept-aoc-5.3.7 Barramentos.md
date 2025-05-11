---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 5.3.7 Barramentos

![[concept-aoc-1.20-barramentos]]


![[concept-aoc-1.21-barramento-de-dados]]

![[concept-aoc-1.22-barramento-de-enderecos]]

#### c) Barramento de controle

O barramento de controle interliga a Unidade de Controle (UC) da UCP aos demais componentes do sistema computacional, como a memória principal e os componentes de entrada e saída, para a passagem de sinais de controle gerados pelo sistema. Exemplos de sinais de controle são: leitura e escrita de dados na memória principal, leitura e escrita de componentes de entrada e saída, certificação de transferência de dados, pedido de interrupção e relógio (clock), que é responsável por sincronizar os pulsos de eventos durante o funcionamento do sistema.

O barramento de controle é bidirecional e permite a troca de sinais de controle entre a Unidade de Controle (UC) da UCP e os demais componentes do sistema computacional, como a memória principal. A UCP pode enviar sinais de controle para a memória principal indicando uma operação de leitura ou escrita, enquanto a memória principal pode enviar sinais de espera (wait) para a UCP aguardar o término de uma operação.

:luc_info:
*Interrupção: É um aviso gerado à UCP comunicando que um dispositivo deseja realizar uma operação (ex.: leitura de dados de um pen-drive, transferência de dados do disco rígido para a memória, chegada de um pacote de dados da rede).

Os barramentos são responsáveis por compartilhar suas vias de comunicação entre diversos componentes do sistema. No entanto, somente um conjunto de bits pode ser transmitido por vez, o que torna o controle do barramento fundamental para o funcionamento adequado do sistema

O modelo apresentado na Figura 5.6 possui um único barramento de dados, endereços e controle que interconecta todos os componentes do computador. Essa escolha é justificada pela grande diferença de características dos diversos componentes, principalmente periféricos, que possuem velocidades de transferência de dados muito distintas. O controle do barramento é essencial para garantir o funcionamento adequado do sistema.

Os projetistas de sistemas de computação criaram diversos tipos de barramento, com taxas de transferência de bits apropriadas às velocidades dos componentes interconectados. Esses barramentos são organizados em uma hierarquia, e atualmente os modelos de organização de sistemas de computação adotados pelos fabricantes possuem diferentes tipos de barramentos.


a) O barramento local é um tipo de barramento que possui alta velocidade de transferência de dados e funciona normalmente na mesma frequência do relógio do processador. Ele é utilizado para interligar o processador a dispositivos de alta velocidade, como a memória cache e a memória principal, com o objetivo de não atrasar as operações do processador.

b) O barramento do sistema é um barramento opcional, adotado por alguns fabricantes, que interliga a memória cache com os módulos de memória principal (RAM) por meio do chipset, não permitindo acesso direto do processador à memória principal.

c) O barramento de expansão é responsável por conectar os dispositivos de entrada e saída (E/S) ao restante do computador. Ele é dividido em dois barramentos, um de alta velocidade para dispositivos mais rápidos e outro de menor velocidade para dispositivos mais lentos. Para se conectar ao barramento do sistema, utiliza-se uma ponte que sincroniza as diferentes velocidades dos barramentos.

Para maximizar o desempenho nas transferências de dados entre dispositivos com diferentes velocidades, a indústria de computadores desenvolveu a separação do barramento de expansão em dois: um de alta velocidade para dispositivos mais rápidos e outro de menor velocidade para dispositivos mais lentos. Essa separação visa otimizar as transferências de dados entre os dispositivos, maximizando o desempenho do sistema.

:luc_info:
*Chipset: É um conjunto de circuitos integrados ou chips, que são projetados para trabalhar em conjunto, sendo considerados circuitos de apoio na placa-mãe para controlar a interconexão entre os seus componentes.
  

A largura do barramento refere-se à quantidade de informações (bits) que podem ser transmitidas simultaneamente por ele e é influente no desempenho do sistema computacional. É determinada pela quantidade de fios ou vias do barramento.

A taxa de transferência de um barramento é a quantidade de bits que ele pode transmitir em um segundo e é especificada em bits por segundo (K bits, M bits, etc.).

Para permitir o compartilhamento de um barramento com vários componentes, é necessário um mecanismo de controle de acesso que garanta que apenas um dispositivo possa utilizar o barramento em um dado momento. Esse controle é baseado em regras para evitar colisões e garantir que todos os dispositivos tenham a oportunidade de acessar o barramento quando necessário.

Esse mecanismo de controle de acesso é denominado protocolo. Isso faz com que um barramento não seja composto somente de fios condutores, mas também de um protocolo 

Os fabricantes de computadores buscam padronização na definição de protocolos para evitar a criação de características diferentes dos demais e tornar o uso de componentes disponibilizados no mercado mais flexível. Essa padronização permite que componentes de diferentes fabricantes funcionem corretamente, desde que estejam de acordo com os padrões de protocolos definidos pela indústria de computadores.

Sendo assim, muitos padrões de barramento de expansão foram desenvolvidos ao longo do tempo, alguns deles já não mais utilizados. Os mais populares são apresentados a seguir

a) ISA (Industry Standard Adapter): desenvolvido pela IBM. Apresenta uma taxa de transferência baixa, mas apesar disso, foi adotado por toda a indústria. Os sistemas atuais não mais o empregaram;

b) PCI (Peripheral Component Interconnect): desenvolvido pela Intel, tornando-se quase um padrão para todo o mercado, como barramento de alta velocidade. Permite transferência de dados em 32 ou 64 bits a velocidades de 33 MHz e de 66 MHz. Cada controlador permite cerca de quatro dispositivos;

c) USB (Universal Serial Bus): tem a característica particular de permitir a conexão de muitos periféricos simultaneamente (pode conectar até 127 dispositivos em um barramento – por meio de uma espécie de centralizador) ao barramento; este, por uma única porta (conector), conecta-se à placa-mãe. Grande parte dos dispositivos USB é desenvolvida com a característica de eles serem conectados ao computador e utilizados logo em seguida, o que é chamado de plug-and-play;

d) AGP (Accelerated Graphics Port): barramento desenvolvido por vários fabricantes, porém liderados pela Intel, com o objetivo de acelerar as transferências de dados do vídeo para a memória principal, especialmente dados em 3D (terceira dimensão), muito utilizados em aplicativos gráficos (ex.: jogos);

e) PCI Express (Peripheral Component Interconnect Express): esse barramento foi construído por um grupo de empresas denominado PCI-SIG (Peripheral Component Interconnect Special Interest Group), composto por empresas como a Intel, AMD, IBM, HP e Microsoft. Este barramento veio para atender às demandas por mais velocidade gerada por novos chips gráficos e tecnologias de rede apresentando altas taxas de transferência. Assim, o PCI e o AGP foram substituídos pelo PCI Express. Nesse barramento, a conexão entre dois dispositivos ocorre de modo ponto a ponto (exclusivo) – comunicação serial. Por esse motivo, o PCI Express não é considerado um barramento propriamente dito (considerando que barramento é um caminho de dados onde você pode ligar vários dispositivos ao mesmo tempo, compartilhando-o). Essa característica é que o faz ser o meio de comunicação entre dois dispositivos de um computador mais rápido atualmente. Até o momento existiram três versões desse barramento (1.0 – lançado em 2004; 2.0 – lançado em 2007; e o 3.0 – lançado em 2010).

Cada barramento possui um protocolo padrão que é utilizado pela indústria de computadores para a fabricação de todos os dispositivos de entrada e saída a serem conectados nos diferentes tipos de barramento. Dessa forma, foram desenvolvidos os chamados slots. Um slot nada mais é do que um orifício ou um encaixe padronizado inserido na placa-mãe dos computadores de maneira que os diversos dispositivos possam ser encaixados, desde que atendam a um dos padrões disponíveis nela. Assim, nas Figuras 5.8, 5.9 e 5.10 são apresentados alguns slots correspondentes aos padrões de barramentos de expansão listados acima.

Nesse caso, a principal diferença entre os diversos tipos de barramentos está na quantidade de bits que podem ser transmitidos por vez e na frequência de operação utilizada. Os barramentos AGP e PCI Express são considerados os mais rápidos, seguidos pelo barramento PCI original, sendo esses os barramentos mais utilizados em computadores atualmente..


![[concept-aoc-1.24-instrucoes-de-maquina]]


![[concept-aoc-1.25-formato-das-instrucoes]]
![[concept-aoc-1.26-ciclo-de-instrucao]]
![[concept-aoc-1.27-arquiteturas-risc-e-cisc]]