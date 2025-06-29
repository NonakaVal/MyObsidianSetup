---
HUB:
  - "[[hub-regex]]"
tags:
  - learning
  - component
created: "[[2025-06-14]]"
---

# H3+ headings (`###`, `####`, etc.):

* Regex: `^#{3,6} .+`
* Comando `ripgrep`: 
```
rg "^#{3,6} .+"
```
# Datas no formato `YYYY-MM-DD`:

* Regex: `\d{4}-\d{2}-\d{2}`
* Comando `ripgrep`: 

```
rg -o "\d{4}-\d{2}-\d{2}"`
```

# Links externos em markdown:

* Regex: `\[([^\]]+)\]\(http`
* Comando `ripgrep`: `

```
rg "\[([^\]]+)\]\(http" -o
```
---

# Links externos contendo "github" ou "stackoverflow":

* Comando `ripgrep`:

  ```bash
  rg -o '\[([^\]]+)\]\(http[^)]*(github|stackoverflow)[^)]*\)'
  ```



# Busca paralela (`-j8`) por `pandas` com até 3 linhas de contexto:

```bash
rg   rg -o '\[([^\]]+)\]\(http[^)]*(github|stackoverflow)[^)]*\)' "(^|\n)import pandas[^\n]*(\n[^\n]*){0,3}\b(pd\.|read_)" -g "*.{py,ipynb,md}" --no-ignore
```

---
