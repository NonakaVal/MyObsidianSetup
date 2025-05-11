---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
created: "[[30-01-2024]]"
---
2024-01-30 18:14

{{Objetivo do método}}
### .pivot_table()
Método útil para resumir e agregar dados com funções de agregação, como média, somas, contagens etc.
Útil para análise de dados, resumo de informações

![Imgur|720](https://i.imgur.com/If4BG6V.png)

{{assinatura básica}}

```python
pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, margins_name='All', dropna=True, margins_fill_value=None, observed=False, sort=True)

```
{{parâmetros}}


- `data` - df com os dados
- `values` - A coluna cujo os valores serão agregados
- `index` - coluna ou colunas que serão utilizados como indices da tabela
- `columns` - coluna ou colunas que serão utilizadas
- `aggfunc` - Função de agregação a ser aplicada, como mean, sum, count
- `fill_value` - valor a ser usado para preencher valores ausentes
- `margins` - se True, adiciona linhas e colunas com totais gerais
- `margin_name` - nomer as linhas e colunas de totais gerais
- `dropna` - se True exclui linhas ou colunas que contem apenas valores nulos
- `margin_fill_value` - valor a ser usada para preencher celulas dos totais gerais