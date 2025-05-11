---
tags:
  - learning/book
HUB:
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
created: "[[2024-06-09]]"
origin: "[[book-introducao-estatistica-12edicao-mario-f-triola-2017]]"
---
### [[probabilidade-definicoes-notacoes-basicas]]

- pen **Definições** 
	- *Evento* - qualquer conjunto de resultados de um experimento.
	- *Evento simples* - resultado ou evento que não pode ser decomposto.
	- *Evento compostos* - qualquer evento que combina um ou mais eventos simples
	- *Espaço amostral* - Todos os eventos simples possíveis, ou seja, todos os resultados.
- pen **Contagem**
	- *Permutações* - de itens são arranjos nos quais sequências diferentes dos mesmos itens são contados separadamente, por exemplo : {a,b,c}, os arranjos {a,b,c}, {a,c,b} etc são contados separadamente;
	- *Combinações* - sequências diferentes de um mesmo arranjo não são contadas separadamente, {a,b,c}, os arranjos {a,b,c}, {a,c,b} etc a mesma combinação;

- pen **Notações**
	- $P$  = *Probabilidade*
	- $A,\ B,\ C$ = *Eventos específicos*
	- $P(A)$ = *Probabilidade evento A*
- ~ *Aproximação da Probabilidade pela Frequência Relativa* - número de vezes que o evento ocorre dividido pelo número total de ensaios ou experimentos.
	- $n$ = número ***total*** de experimentos.
	- $f(A)$ =número de vezes que evento $A$ ocorre.
	- $P(A)$ = Frequência relativa.
## $$P(A)\approx\frac{f(A)}{n}$$
- ~ *Abordagem clássica (**requer resultados igualmente prováveis**)

## $$P(A)=\frac{n\ ocorrência\ A}{total\ diferetentes\ simples}$$
- pen **Eventos Complementares**: O **Complementar** de avento $A$, representado por $\overline{A}$, consistem em todos os resultados em que A não ocorre.

Considerando um evento $A$, então o complemento, denominado por $A^c$, é o evento que $A$ não ocorre, sendo a soma das probabilidades = 1.
### $$P(A)+P(A^c)=1$$
logo, a probabilidade do complemento de $A$ é :
### $$P(A^c)=1-P(A)$$



- pen **Probabilidade de "pelo menos um"** - A probabilidade complementar para calcular a probabilidade de obtermos, entre várias tentativas, *pelo menos um* de algum evento especificado. sendo um ou mais.
### $$P(pelo\ menos\ 1\ A)=1-(P(A))^n$$

- pen *Probabilidade condicional* - Ache a probabilidade de um evento quando temos a informação adicional de que algum outro evento já ocorreu.
### $$P(B|A)=\frac{P(A\cap B)}{P(A)}$$