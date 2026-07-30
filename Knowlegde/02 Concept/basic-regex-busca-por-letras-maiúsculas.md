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

## Busca por letras maiúsculas
**Exemplo:** Encontrar siglas de 2 ou 3 letras maiúsculas
```
[A-Z]{2,3}
```
- Encontra: "BR", "EUA", "ONU"
- Nao encontra: "Br", "eua"

← Parte de [[concept-regex-introductions-and-basic]]