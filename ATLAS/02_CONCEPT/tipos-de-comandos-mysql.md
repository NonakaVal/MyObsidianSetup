---
tags:
  - learning
hub:
  - "[[hub-tec]]"
  - "[[hub-sql]]"
created: "[[2024-03-24]]"
---
### [[tipos-de-comandos-mysql]]


SQL(Structured Query Language)

- info **DDL** - *Data Definition Language*
	- ~ Conjunto de instruções SQL para definição dos dados e sua estrutura
		- 01 `CREATE` - Criar banco de dados, tabelas, colunas
		- 01 `DROP` - Excluir banco de dados, tabelas, colunas
		- 01 `ALTER` - Alterar bando de dados
		- 01 `TRUNCATE` - Esvaziar toda a tabela
- info **DML** - *Data Manipulation Language*
	- ~ Inserção e manutenção dos dados.
		- 01 `INSERT` - insere dados em uma tabela
		- 01 `UPDATE` - Atualiza os dados existentes em uma tabela
		- 01 `DELETE` - Excluir registros de uma tabela
- info **DQL** - *Data Query Language*
	- ~ Comandos para consultas dos dados.
		- 01 `SELECT` - Principal instrução de consulta SQL
		- 01 `SHOW` - Exibir todas as informações do bd
		- 01 `HELP` - informações do manual do mysql
- info **DCL** - *Data Control Language*
	- ~ controle de autorizações de acesso
		- 01 `GRANT` - concede privilégios às contas de usuário
		- 01 `REVOKE` - revoga privilégios
- info **DTL** - *Data Transaction Language*
	- ~ Controle de transações lógicas
		- 01 `START TRANSACTION` - inicia uma nova transação
		- 01 `SAVEPOINT` - identificação de um determinado ponto numa transação
		- 01 `COMMIT` - instrução de entrega
