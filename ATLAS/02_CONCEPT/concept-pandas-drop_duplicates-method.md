---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---

## .drop_duplicates

DataFrame [[cmp-pandas-importing-data|carregado]] na variável "dados"
```css
import pandas as pd
dados = pd.read_csv("aluguel.csv", sep =";")
```

para filtrar uma coluna especifica do dataframe:
```css
tipos_de_imovel = dados['tipo']
```
-  "tipo" precisa ser uma coluna válida
- novo dataframe só com a coluna "tipos" é armazenado em "tipos de variáveis"

Tirando duplicadas
```python
tipos_de_imovel.drop_duplicates(inplace = True)
```
- "drop_duplicates " é o metodo utilizado para remover linhas duplicadas de um dataframte criando um dataframe sem linhas repetidas
	- inplace = True modifica o dataframe em si


