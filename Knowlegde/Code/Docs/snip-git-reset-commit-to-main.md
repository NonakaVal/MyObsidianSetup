---
created: "[[2025-06-03]]"
tags:
  - snippet
HUB:
  - "[[hub-git]]"
connections:
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

restaurar o main com base em um commit especifico 

# {código}

## PRIMEIRA FUNÇÃO - {date}


```bash
git log --oneline
```

## 🔙 **Reverter o projeto exatamente para esse commit**

### ➕ **Opção 1 — Checkout desvinculado (não afeta branches, apenas explora aquele commit)**

```bash
git checkout e4f5g6h
```

```bash
git push origin main --force
```

```bash
git push origin main --force
```
