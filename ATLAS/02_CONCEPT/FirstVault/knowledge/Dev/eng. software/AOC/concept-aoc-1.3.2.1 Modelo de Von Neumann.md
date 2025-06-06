---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 1.3.2.1 Modelo de Von Neumann

:luc_link:
 [John Von Neumann](https://pt.wikipedia.org/wiki/John_von_Neumann) foi um matemático e físico húngaro que viveu a maior parte de sua vida nos Estados Unidos e contribuiu significativamente para a evolução dos computadores. Sua principal contribuição foi a construção de um computador sequencial binário de programa armazenado e a proposição dos elementos críticos de um sistema computacional, conhecido como Modelo de Von Neumann. Esse modelo descreve a arquitetura básica de um computador, composta por quatro elementos principais: CPU, memória, dispositivos de entrada e dispositivos de saída. Essa arquitetura permitiu a flexibilidade e a programabilidade dos computadores, tornando-os capazes de executar uma ampla variedade de tarefas. As contribuições de Von Neumann perduram até os dias atuais e são fundamentais para o desenvolvimento da ciência da computação


a) uma [[concept-aoc-aoc.4.subsistema.de.memoria]] (para armazenar programas e dados – representados por 0’s e 1’s); 

b) uma [[concept-aoc-1.14-unidade-logica-e-aritmetica-(ula)]], cuja função é executar operações indicadas pelas instruções de um programa. Seu trabalho é apoiado por diversos registradores (ex.: acumulador);.

c) uma [[concept-aoc-1.15-unidade-funcional-de-controle]], cuja função é buscar um programa na memória, instrução por instrução, e executá-lo sobre os dados de entrada (que também se encontram na memória); e

d) equipamento de [[concept-aoc-1.32-dispositivos-de-entrada-e-saida]].

É importante esclarecer que a ULA e a UC, juntamente com diversos registradores específicos, formam [[concept-aoc-5.2 Unidade funcional de processamento]] do computador.



Embora a proposta inicial de Von Neumann ainda seja amplamente utilizada na construção de computadores, muitas melhorias foram feitas ao longo dos anos para obter um desempenho cada vez mais elevado. Isso inclui o uso de arquiteturas paralelas que replicam alguns elementos da arquitetura básica de Von Neumann. No entanto, apesar dos esforços de pesquisadores para encontrar alternativas a essa arquitetura, ainda não foi encontrada uma solução que a substitua com sucesso.


##### A seguir serão descritos cada um dos principais componentes de um computador:

a)[[ucp]] sigla representativa de Unidade Central de Processamento. Podemos dizer que se trata do componente principal do computador. Algumas pessoas chamam de processador ou microprocessador. É responsável pela execução de dados e instruções armazenadas em memória (código de programas e dados);

b)  [[concept-aoc-memoria]] : existem diversos tipos de memória em um computador (ex.: RAM (principal), ROM, cache, registradores), mas existe uma delas denominada memória principal, a qual é indispensável. A memória principal é tão importante quanto a UCP, pois sem ela não seria possível disponibilizar os programas e seus dados para o processamento pela CPU. Portanto, a memória é responsável por armazenar todos os programas que executam no computador e os dados que utilizam;

c) [[concept-aoc-1.32-dispositivos-de-entrada-e-saida]]: são dispositivos responsáveis pelas entradas e saídas de dados, ou seja, pelas interações entre o computador e o mundo externo (usuários). São exemplos de dispositivos de E/S: monitor de vídeo, teclado, mouse, webcam, impressora, entre outros;

d)[[concept-aoc-1.20-barramentos]]: é responsável por interligar todos os componentes listados acima. Trata-se de uma via de comunicação composta por diversos fios ou condutores elétricos por onde circulam os dados manipulados pelo computador.