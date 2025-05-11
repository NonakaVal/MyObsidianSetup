---
tags:
  - learning
  - 
HUB:
  - "[[hub-sql]]"
---

 
```sql
DELIMITER//
CREATE TRIGGER nome_do_trigger
    BEFORE INSERT
    ON nome_da_tabela FOR EACH ROW
BEGIN
-- codigo_a_ser_executado
END//
```

```sql

DELIMITER//

CREATE TRIGGER TG_CLIENTES_IDADE_INSERT BEFORE INSERT ON CLIENTES

FOR EACH ROW

BEGIN

SET NEW.IDADE = timestampdiff(YEAR, NEW.DATA_NASCIMENTO, NOW());

END//
```

