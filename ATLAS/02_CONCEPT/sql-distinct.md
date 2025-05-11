---
tags:
  - learning
HUB:
  - "[[hub-sql]]"
---
```sql
SELECT DISTINCT BAIRRO FROM tabela_de_clientes WHERE CIDADE = 'Rio de Janeiro'
```

```sql
SELECT * FROM notas_fiscais  WHERE DATA_VENDA = '2017-01-01' limit 10
```

```sql
SELECT ESTADO, SUM(LIMITE_DE_CREDITO) as SOMA_LIMITE FROM tabela_de_clientes
GROUP BY ESTADO
HAVING SUM(LIMITE_DE_CREDITO) > 900000;
```

