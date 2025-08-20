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

## Exemplos Praticos

1. Validar email:
```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

2. Extrair datas no formato DD/MM/AAAA:
```regex
(\d{2})\/(\d{2})\/(\d{4})
```

3. Buscar tags HTML:
```regex
<([a-z]+)([^<]+)*(?:>(.*)<\/\1>| *\/>)
```


# Exemplos Praticos Simples de Regex (Expressões Regulares)

← Parte de [[concept-regex-introductions-and-basic]]