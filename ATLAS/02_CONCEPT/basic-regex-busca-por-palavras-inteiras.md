---
created: "[[2025-06-11]]"
tags:
  - learning/review
HUB:
  - "[[hub-regex]]"
  - "[[hub-tec]]"
  - "[[hub-linux]]"
tags:
  - learning
connections:
  - "[[draft-regex-rg-all-notes]]"
  - "[[cmp-first-ripgrep-regex-queries]]"
  - "[[draft-code-search-ripgrap-functions]]"
---

## Busca por palavras inteiras
**Exemplo:** Encontrar apenas a palavra "rio" (nao partes de outras palavras)
```
\brio\b
```
- Encontra: "O rio é lindo"
- Nao encontra: "O prion é perigoso"

← Parte de [[concept-regex-introductions-and-basic]]