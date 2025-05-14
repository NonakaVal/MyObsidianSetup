---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
<font color = 00bfff> Determinando Seleções </font>

### [[concept-python-pandas-formas-de-selecao]] | [[concept-python-pandas-loc-iloc-method-selection]] | [[pandas-query-method]] 

### [[concept-pandas-criando-agrupamentos]]

### [[concept-pandas-with.query]]
- `df_selected_columns = df[['c3',-'c2']]`
- `df_selected_rows = df[1:4]`
- `df_selected_rows_columns = df[1:][['c3',-'c2']]`
- `df_loc_rows = df.loc[['l3',-'l2']]`
- `df_loc_rows_columns = df.loc[['L3', 'L1'], ['C4', 'C1']]`
- `specific_value = df.iloc[0, 1]`
- `interval_values = df.iloc[[2, 0], [3, 0]]`
- `df_filtered = df[~(df['C1'] == 5)]` - *boole*
- `notas_por_filme = notas.query("filmeid==1").nota.mean()`

### [[concept-python-Pandas-DataFrame-Selection-Methods]]
- `selecao = alunos['Aprovado'] == True`
- `selecao = (alunos['Aprovado'] == True) & (alunos['Sexo'] == 'F')`
- `selecao = (alunos.Idade > 10) & (alunos.Idade < 20 ) | (alunos.Idade >= 40)`
    - `idades = alunos[selecao]`
        - [[concept-python-pandas-loc-iloc-method-selection]]
            - `selecao = alunos.Aprovado == False`
            - `reprovados = alunos.loc[selecao, ['Nome', 'Sexo', 'Idade']]`

### [[concept-python-Pandas-DataFrame-Selection-Methods-2]]
- `selecao = dados['Tipo'] == 'Apartamento'`
- `selecao = (dados.Tipo == 'Casa') | (dados.Tipo == 'Casa de Condomínio')`
- `selecao = (dados.Area >= 60) & (dados.Area <= 100)`
- `selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)`

### [[pandas-isin-method]] | [[concept-pandas-drop_duplicates-method]]
- `residencial = ['Quitinete', 'Casa de Vila']`
    - `selecao = dados['Tipo'].isin(residencial)`
- `list(dados['Tipo'].drop_duplicates())`
