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

## Validaçao de datas simples
**Exemplo:** Encontrar datas no formato DD/MM/AA
```
\d\d\/\d\d\/\d\d
```
- Encontra: "25/12/23", "01/01/24"
- Nao valida se a data é correta, apenas o formato

← Parte de [[concept-regex-introductions-and-basic]]