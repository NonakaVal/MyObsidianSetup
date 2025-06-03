---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
link-to-lib: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
dg-publish: true
---
Operação usada para agrupar dados em um dataframe com base em uma ou mais colunas, ela permite dividir os dados em grupos com base em critérios.

![[snip-pandas-groupby-function]]


Padrão:
```python
df.groupby(by=coluna_ou_colunas)
```
Diversas operações podem ser feitas em grupos:
exemplos:
[[informacoes-de-um-dataframe|sum]]()
```css
df.groupby("Categoria")["Vendas"].sum()
```

---

```css
import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])
```
Obtendo média das notas separadamente por sexo do dataframe
```css
sexo = alunos.groupby('Sexo')
sexo = pd.DataFrame(sexo['Notas'].mean().round(2))
sexo.columns = ['Notas Médias']
sexo
```

```python
import pandas as pd

# Criar um DataFrame de exemplo
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 20, 15, 25, 12, 18]}
df = pd.DataFrame(data)

# GroupBy pela coluna 'Category'
grouped = df.groupby('Category')

# Obter o grupo correspondente a 'A'
group_A = grouped.get_group('A')

# Exibir o grupo 'A'
print(group_A)

```