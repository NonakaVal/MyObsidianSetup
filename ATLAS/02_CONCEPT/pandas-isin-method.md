---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---
 

[[cmp-pandas-importing-data|dados-importados]] de um csv para a variável "dados":
```css
import pandas as pd
dados = pd.read_csv('aluguel.csv', sep= ';')
```

Criando uma lista  e usando [[concept-pandas-drop_duplicates-method]] na coluna "Tipos"
```css
list(dados['Tipo'].drop_duplicates())
```
- será criada uma lista com **todos** os elementos da coluna "Tipo" sem repetições

Criando uma lista com valores **selecionados** da coluna "Tipo"
```css
residencial = ['Quitinete', 'Casa','Apartamento', 'Casa de Condomínio', 'Casa de Vila']
```
- lista com os valores selecionados é armazenado na variável residencial para ser usado na seleção no metodo de filtragem .isin

método [[concept-pandas-isin]]
```css
selecao = dados['Tipo'].isin(residencial)
```
- isin é um método pandas que verifica se cada valor da coluna "Tipo" está condito na lista "residencial" retornando uma Series booleana com "True" para os valores que estão na lista e "False" para os que não estão.

criando novo dataframe com base na variável booleana criada "selecao"
```css
dados_residencial = dados[selecao]
```

resetando o do dataframe "dados_residencial"
```css
dados_residencial.index = range(dados_residencial.shape[0])
```



