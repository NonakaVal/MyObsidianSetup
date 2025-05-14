---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---



[[cmp-pandas-importing-data|dado-importado-como-csv]]
```css
import pandas as pd

dados = pd.read_csv("aluguel_residencial.csv", sep = ";")
dados
```


Criando uma seleo com [[concept-pandas-isin|.isin()]]
```css
bairros = ['Copacabana', 'Jardim Botnico', 'Centro', 'Higienpolis',
       'Cachambi', 'Barra da Tijuca', 'Ramos', 'Graja']

selecao = dados.Bairro.isin(bairros)

dados = dados[selecao]

```


Agrupando com a operao [[cmp-pandas-groupby-method]]:
```css
grupo_bairro = dados.groupby('Bairro')
```


Selecionando uma coluna especifica no agrupamento
```python
nota_media_por_filme = notas.groupby('movieId').mean()['rating']
```


Conseguindo mdias por bairro:
```css
for bairro, data in grupo_bairro:
    print('{} --->{}'.format(bairro, data.Valor.mean()))
```
```css
grupo_bairro[["valor",-"condominio"]].mean().round(2)
```



