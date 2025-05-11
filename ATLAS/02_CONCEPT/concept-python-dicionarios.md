---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---



- um dicionário em python é uma coleção não ordenada de pares "chave-valor", cada chave é única e mapeia um valor específico.
	- {key:value}
- cada chave retorna o valor mapeado

```css
alice = {
	"nome":"alice",
	"endereço": {
		"rua":"25 de março",
		"numero":279 
	},
	"admin": True
}

bob = {
	"nome":"bob",
	"endereço": {
		"rua":"sem rua",
		"numero":288 
	},
	"admin": True
}
```
- "nome" é a chave para o valor "alice"

- podemos retornar um elemento especifico do dicionário da seguinte forma:
```css
print (alice["nome"]) 
print (alice["endereço"])
print (alice["endereço"]["numero"])
```
- "nome": retorna o valor correspondente a chave , no caso "alice"
- "endereço" : retorna toda a estrutura em dicionário armazenado no em "rua'' e "número"
- "endereço"e 'numero' : retorna o valor especifico armazenado em número : 279

#### Métodos com Dicionário

[Documentação completa w3](https://www.w3schools.com/python/python_dictionaries_methods.asp)

`` items(), keys() e values() ``no [[concept-python-for.in|-loop-for]]

.items() : retorna uma lista de todos os elementos do dicionário
```css
notas = {
	"joão":10,
	"maria":8,
	"henrique":10, 
}

for lista in notas.items():
	print(lista)
```
- o resultado é a saída de todos os elementos em "notas"

.keys(): retorna uma lista das chaves do dicionário
```css
notas = {
	"joão":10,
	"maria":8,
	"henrique":10, 
}

for lista in notas.keys():
	print(lista)
```
- retorna uma lista com "joão ,maria,henrique",

.values(): retorna uma lista com todos os valores
``` css
notas = {
	"joão":10,
	"maria":8,
	"henrique":10, 
}

for lista in notas.values():
	print(lista)
```
- retorna uma lista com "10, 8,  10"