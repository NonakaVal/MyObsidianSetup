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

## Componentes Basicos

### 1. Literais
Correspondem exatamente ao caractere especificado:
```
"abc" corresponde a "abc" no texto
```

### 2. Metacaracteres
Caracteres especiais com significado especial:
```
. ^ $ * + ? { } [ ] \ | ( )
```

### 3. Classes de Caracteres
- `[abc]` - Qualquer um dos caracteres a, b ou c
- `[a-z]` - Qualquer letra minúscula
- `[^abc]` - Qualquer caractere EXCETO a, b ou c

### 4. Quantificadores
- `?` - Zero ou uma ocorrência
- `*` - Zero ou mais ocorrências
- `+` - Uma ou mais ocorrências
- `{n}` - Exatamente n ocorrências
- `{n,}` - No mínimo n ocorrências
- `{n,m}` - Entre n e m ocorrências

### 5. Âncoras
- `^` - Início da linha/string
- `$` - Fim da linha/string
- `\b` - Limite de palavra

### 6. Grupos e Captura
- `(abc)` - Grupo de captura
- `(?:abc)` - Grupo sem captura
- `a|b` - "a" OU "b"

### 7. Classes Especiais
- `\d` - Dígito (equivalente a [0-9])
- `\D` - Nao dígito
- `\w` - Caractere de palavra (letras, números, _)
- `\W` - Nao caractere de palavra
- `\s` - Espaço em branco
- `\S` - Nao espaço em branco

← Parte de [[concept-regex-introductions-and-basic]]