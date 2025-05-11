---
tags:
  - learning
HUB:
  - "[[hub-statistic]]"
  - "[[hub-python]]"
---

retorna estatísticas descritivas

considere as seguinte dataFrame:
```css
precos = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]], 
                        columns = ['Local', 'Produto', 'Preço'])
```

Criando agrupamentos com [[cmp-pandas-groupby-method]]
```css
produtos = precos.groupby('Produto', sort = False)
```

describe() , para retornar [[concept-statistic-descritivas]]
```css
grupo_bairro['Valor'].describe().round(2)
```

dados com aggregate:
```css
df1 = grupo_bairro.Valor.aggregate(['min','std']).round(2).reset_index()
```

rename()
```
grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = {'min': 'Mínimo', 'max': 'Máximo'})
```