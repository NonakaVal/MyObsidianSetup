---
tags:
  - learning
HUB:
  - "[[hub-python]]"
dg-publish: true
---


[DataFrame()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

series a partir de uma array.
```css
data = [1, 2, 3, 4, 5, 6]

s = pd.Series(data)

s
```


### Series para DaraFrame e .reset_index

**Pandas Series**: Estrutura de dados unidimencional

**Pandas Dataframe**: Estrutura de dados bidimencional (tabela) em que os dados são organizados em colunas e linhas

```python
contagem_de_lingua = tmdb["original_language"].value_counts().to_frame().reset_index()
```
- é criada a variável "contagem_de_lingua" que recebe  primeiro a variável  (tmdb) onde está o arquivo, então executa o "value_counts" na coluna "["original_language"]"
- ".to_frame()" transforma a série da coluna em um Dataframe
- "reset_index()" redefine o indice do dataframe recém criado. criando uma coluna adicional com um índice númerico.



