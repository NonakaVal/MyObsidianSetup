---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---

## Seleção de Frequência 1

[[concept-python-pandas-formas-de-selecao]]

[[concept-python-pandas-dicionario-para-dataframe|criando-um-dataframe-com-um-dicionario]]
```css
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'], 
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'], 
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35], 
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6], 
                        'Aprovado': [True, False, False, True, True, True, False, False]}, 
                        columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

```

Crie um DataFrame somente com os alunos aprovados:
```css
selecao = alunos['Aprovado'] == True
aprovados = alunos[selecao]
```
- operador lógico "= =" cria uma série lógica com base na condição "alunos['Aprovados']"
	- armazenar 

Crie um DataFrame somente com as alunas aprovadas.
```css
selecao = (alunos['Aprovado'] == True) & (alunos['Sexo']== 'F')
aprovadas = alunos[selecao]
```
- o operador & exige que todas as condições sejam verdadeiras

Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos:
```css
selecao = (alunos.Idade > 10) & (alunos.Idade < 20 ) | (alunos.Idade >= 40)
idades = alunos[selecao]
```
- o operador & exige que todas as condições sejam verdadeiras
	- usado o operador lógico "|" para verificar se uma das condições é verdadeira

Crie um DataFrame somente com os alunos reprovados e mantenha neste DataFrame apenas as colunas Nome, Sexo e Idade, nesta ordem.
```css
selecao = alunos.Aprovado == False
reprovados = alunos.loc[selecao,['Nome', 'Sexo', 'Idade']] 
```
- usado o  [[concept-python-pandas-loc-iloc-method-selection|-metodo-loc]] para filtrar os dados, as linhas são determinadas pela "selecao" e as colunas especificadas em[]

Crie uma visualização com os três alunos mais novos.
```css
alunos.sort_values(by = ['Idade'], inplace = True)
alunos.iloc[:3]
```
- idade organizada com [[organizando-dataframe|-.sort_values]]


[[selecao-frequencia-2]]
