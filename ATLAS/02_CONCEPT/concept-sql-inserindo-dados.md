---
tags:
  - learning
HUB:
  - "[[hub-sql]]"
---



> Desativando as restrições das chaves estrangeira
```sql
SET FOREIGN_KEY_CHECKS = 0;
```


livro
```sql
INSERT INTO LIVROS VALUES (
 1,
'Percy Jackson e o Ladrão de Raios',
'Rick Riordan',
'Intrínseca',
'Aventura',
34.45
);
```


inserindo dados nas tabelas

```sql
INSERT INTO LIVROS (ID, Titulo, Autor, Editora, Genero, Preco) VALUES
(3, 'O Cortiço', 'Aluísio de Azevedo', 'Panda Books', 'Romance', 47.8),
(4, 'Dom Casmurro', 'Machado de Assis', 'Via Leitura', 'Romance', 19.90),
(5, 'Memórias Póstumas de Brás Cubas', 'Machado de Assis', 'Antofágica', 'Romance', 45),
(6, 'Quincas Borba', 'Machado de Assis', 'L&PM Editores', 'Romance', 48.5),
(7, 'Ícaro', 'Gabriel Pedrosa', 'Ateliê', 'Poesia', 36),
(8, 'Os Lusíadas', 'Luís Vaz de Camões', 'Montecristo', 'Poesia', 18.79),
(9, 'Outros Jeitos de Usar a Boca', 'Rupi Kaur', 'Planeta', 'Poesia', 34.8);

```


```sql
INSERT INTO VENDEDORES 
VALUES
(1,'Paula Rabelo'),
(2,'Juliana Macedo'),
(3,'Roberto Barros'),
(4,'Barbara Jales');
```


```shell
#######       Código Extra      ########
# Excluindo uma tabela
DROP TABLE VENDEDORES;
```
