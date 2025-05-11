---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
## 5.1 Organização do processador

Na Aula 1 estudamos os componentes básicos da arquitetura de um computador, segundo o modelo de Von Neumann, cuja proposta vale a pena relembrar no início desta seção, a qual irá tratar especificamente de um dos elementos dessa arquitetura: o processador. A proposta de Von Neumann para a construção de um computador previa que:

a) Codificasse instruções que pudessem ser armazenadas na memória e sugeriu que se usassem cadeias de uns e zeros (binário) para codificá-lo;

b) Armazenasse na memória as instruções e todas as informações que fossem necessárias para a execução da tarefa desejada;

c) Ao processar o programa, as instruções fossem buscadas diretamente na memória.

A Unidade Central de Processamento ([[aoc.5.oprocessador.organizacao.e.arquitetura|UCP]]) é responsável por processar e executar programas armazenados na memória principal. Ela busca as instruções do programa, examina-as e as executa uma por vez. A sigla ([[aoc.5.oprocessador.organizacao.e.arquitetura|UCP]]) se refere ao processador do computador.

A ([[aoc.5.oprocessador.organizacao.e.arquitetura|UCP]])é composta por vários componentes, incluindo registradores, Unidade de Controle ([[1.15-unidade-funcional-de-controle|UC]]) e Unidade Lógica Aritmética ([[1.14-unidade-logica-e-aritmetica-(ula)|ULA]]). Ela pode ser dividida em duas categorias funcionais: Unidade Funcional de Controle e Unidade Funcional de Processamento. A Unidade Funcional de Controle é composta pelos elementos em azul no diagrama funcional básico da UCP, enquanto a Unidade Funcional de Processamento é composta pelos elementos em amarelo claro.

:luc_link:[CODPLAYER UCP](https://docplayer.com.br/49352054-Unidade-central-de-processamento-ucp-cpu.html)




A Unidade Funcional de Processamento é composta pelos seguintes elementos: Registradores, ACC, ULA. A Unidade Funcional de Controle é composta pelos seguintes elementos: RDM, REM, CI, RI, Decodificador de Instruções, UC, Clock (relógio)

O barramento é um conjunto de fios paralelos que conecta os componentes do processador, como a UCP, memória e dispositivos de entrada e saída, permitindo a transmissão de dados, endereços e sinais de controle. Existem barramentos externos ao processador que o conectam à memória e aos dispositivos de entrada/saída, além dos barramentos internos na UCP.


#![[concept-aoc-5.2 Unidade funcional de processamento]]

