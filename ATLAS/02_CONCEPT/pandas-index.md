---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---

## .index

- index é uma posição numérica que indica a localização de um elemento dentro de uma sequência

criando um .index com .shape ex1: 
- quando o index criado é adicionado na criação da series
``` css
data = [1, 2, 3, 4, 5, 6]

index = ['linha' + str(i) for i in range(s.shape[0])]
index

s = pd.Series(data = data, index = index)
```

criando um .index com .shape ex2
- quando o index é adicionado em um dataframe que já foi criado
 
	- algoritmo base para o index de 0 até o x = n (colunas data frame)
		- dataframe [[cmp-pandas-importing-data|carregado-na-variavel-"tipos_de_imovel"-]]
```css
for i in range(tipos_de_imovel.shape[0])
	print(i)
```
- adicionando o index no DataFrame
```css
tipos_de_imovel.index = range(tipos_de_imovel.shape[0])
```


[[series-para-dataframe|reset_index]] 