---
tags:
  - learning
  - resources
HUB:
  - "[[hub-python]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.melt.html
created: "[[30-01-2024]]"
---
*2024*-01-30 18:08

{{Objetivo do método}}
### `.melt()`
- destorce um Dataframe de um formato largo para um formato longo, deixando opcionalmente os identificadores definidos
	- útil para transformar um df em um formato onde uma ou mais colunas são variáveis identificadoras, enquanto outras são variáveis de medidas, são 'não dinâmicas' para o eixo da linha, deixando apenas duas não-identificadoras colunas, variável e valor

{{assinatura básica}}

```python

pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)
```

{{parâmetros}}

- `frame` - O dataframe que deseja usar
- `id_vars` - colunas que deseja manter inalterada
	- `scalar, tuple, list, or ndarrays, optional`
- `var_name` - nome da coluna que armazenará os rótulos das colunas derretidas 
	- `scalar, optional`
