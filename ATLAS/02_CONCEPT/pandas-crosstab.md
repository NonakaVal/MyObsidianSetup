---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html
created: "[[30-01-2024]]"
---
2024-01-30 18:22

{{Objetivo do método}}
Calcular uma tabela de frequência cruzada, útil para entender a relação entre duas variáveis categóricas e distribuição conjunta dessas variáveis

![Imgur|670](https://i.imgur.com/olX0qVp.png)
{{assinatura básica}}

```python
pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)
```

{{parâmetros}}

- `index` - variável categórica a ser usada como indice
- `columns` - variável categórica a ser usada como colunas da tabéla
- `values` -  valores a serem agregados nas celulas
- `rowname` - nomes para as linhas da tabela
- `colnames` - nome para as colunas
- `aggfunc` - função de agregação a ser aplicada caso `values` seja especificado
- `margins` - se True adicona totais gerais nas margens da tabela
- `margins_name` - nome a ser usado para linhas e colunas de totais gerais
- `dropna` - se True exclui linhas ou colunas que contém apenas valores nulos
- `normalize` - se True, normaliza os valores para mostrar as proporções em vez de contagens