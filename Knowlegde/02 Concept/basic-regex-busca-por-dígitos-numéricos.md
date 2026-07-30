---
dateCreated: "[[2025-06-11]]"
tags:
  - learning/review
  - learning
subject:
  - "[[hub-regex]]"
  - "[[hub-tec]]"
  - "[[hub-linux]]"
related:
  - "[[draft-regex-rg-all-notes]]"
  - "[[cmp-first-ripgrep-regex-queries]]"
  - "[[draft-code-search-ripgrap-functions]]"
---

## Busca por dígitos numéricos
**Exemplo:** Encontrar números de 3 dígitos
```
\d\d\d
```
ou
```
[0-9]{3}
```
- Encontra: "123", "456", "789"
- Nao encontra: "12", "1234"

← Parte de [[concept-regex-introductions-and-basic]]