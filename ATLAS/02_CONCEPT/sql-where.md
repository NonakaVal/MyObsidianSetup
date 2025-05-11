---
tags:
  - learning
HUB:
  - "[[hub-sql]]"
---



`WHERE`  é usado para filtras registros, permitindo extrair dados que atendem a uma condição especificada

```sql
SELECT column1, column2
FROM table name
WHERE condition;
```

tal condição pedem ser aplicadas não apenas em queries com SELECT mas também de UPDATE, DELETE  etc..


ex: `
```sql
SELECT * FROM Customers  
WHERE Country='Mexico';
```
	
campos numéricos não devem ser colocado entre áspas
```sql
SELECT * FROM Customers  
WHERE CustomerID=1;
```

diversos operadores podem ser usados na condição do `WHERE`, tais como:


| operador | descrição                                  |
| -------- | ------------------------------------------ |
| =        | igual                                      |
| >        | maior que                                  |
| <        | menor que                                  |
| <=       | menor ou igual                             |
| >=       | maior ou igual                             |
| between  | entre um determinado range                 |
| like     | estabelece um padrão                       |
| in       | especificar diversos valores em uma coluna |
|          |                                            |



consultas 

```SQL

SELECT * FROM tbproduto
```

```sql
SELECT * FROM TABELA_DE_VENDEDORES WHERE YEAR(DATA_ADMISSAO) >= 2016;
```

```sql
SELECT * FROM tbcliente WHERE (IDADE >= 18 AND IDADE <= 22 AND SEXO = 'M')
 OR (cidade = 'Rio de Janeiro' OR BAIRRO = 'Jardins');
```

```sql
SELECT * FROM TABELA_DE_VENDEDORES WHERE YEAR(DATA_ADMISSAO) < 2016 AND DE_FERIAS = 1;
```


```sql
SELECT CPF as IDENTIFICADOR, NOME as CLIENTE FROM tabela_de_clientes;
```

busca de float com sql 

```sql
SELECT * FROM tabela_de_produtos WHERE PRECO_DE_LISTA BETWEEN 19.50 AND 19.52;
```


```sql
SELECT * FROM tabela_de_produtos WHERE SABOR IN ('Laranja', 'Manga');
```

```sql
SELECT * FROM tabela_de_produtos WHERE SABOR LIKE '%Maça%';
```
