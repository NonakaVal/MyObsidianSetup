---
tags:
  - learning
hub:
  - "[[hub-tec]]"
  - "[[hub-sql]]"
created: "[[2024-03-26]]"
---
### [[sql-estrutura-basica-consulta]]

Estrutura básica das consultas SQL

`SELECT` - identificação dos campos desejados
`FROM` - lista as tabelas que deverão ser lidas.
`WHERE` - expressões lógicas sobre os campos das tabelas do `FROM`


```SQL
SELECT nome FROM cidade;
```

```SQL
SELECT nome,nascimento,cpf FROM clientes WHERE cpf="12345678901";
```

```SQL
SELECT * FROM clientes;
```
