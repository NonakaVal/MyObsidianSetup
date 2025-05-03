---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 4.3 Memória cache

Os processadores precisam buscar dados e instruções na memória principal para processá-los. No entanto, a velocidade dos processadores é muito maior do que a da memória principal, o que gera um atraso na transferência de dados entre os dois dispositivos. Para reduzir esse atraso, foram desenvolvidas tecnologias que permitem que os processadores acessem dados mais rapidamente, como caches de memória e técnicas de pré-busca de dados. 

A técnica de incluir um dispositivo de memória chamado de memória cache entre o processador e a memória principal foi desenvolvida para acelerar a transferência de informações e melhorar o desempenho dos sistemas de computação. A memória cache é volátil, o que significa que precisa de energia para manter o conteúdo armazenado, assim como os registradores.

A Figura 4.2 apresenta um diagrama de blocos de um processador Pentium original, a distribuição da memória cache e sua relação com a memória principal (MONTEIRO, 2007).



Para diminuir o custo de produção da memória cache e ainda assim melhorar o desempenho do sistema, foram incorporadas ao computador pequenas porções de memória cache localizadas internamente ao processador e entre ele e a memória principal. Essas porções de memória funcionam como um espelho de parte da memória principal.

Quando um processador solicita um dado que já está armazenado na memória cache, não é necessário buscar esse dado na memória principal, o que reduz significativamente o tempo de processamento. Quanto mais memória cache um processador tiver, melhor será o seu desempenho, já que mais dados poderão ser armazenados na memória cache, reduzindo a necessidade de acessar a memória principal.

A tecnologia de memória cache SRAM não requer refresh constante como as memórias DRAM, devido ao uso de seis transistores (ou quatro transistores e dois resistores) por célula de memória. Isso torna a memória SRAM mais rápida e com menor consumo de energia.

De acordo com Alecrim (2010), os processadores trabalham, basicamente, com dois tipos de cache: cache L1 (Level 1 ou Nível 1) e cache L2 (Level 2 ou Nível 2). Normalmente a cache L2 é um pouco maior que a L1 e foi implantada quando a cache L1 se mostrou insuficiente.

Nas gerações anteriores, a cache L1 ficava localizada no interior do processador e a cache L2 era externa a ele. Nas gerações de computadores atuais, ambos os tipos ficam localizados dentro do chip do processador, sendo que, em muitos casos, a cache L1 é dividida em duas partes: “L1 para dados” e “L1 para instruções”. Alecrim (2010) destaca, ainda, que dependendo da arquitetura do processador, é possível o surgimento de modelos que tenham um terceiro nível de cache (L3).