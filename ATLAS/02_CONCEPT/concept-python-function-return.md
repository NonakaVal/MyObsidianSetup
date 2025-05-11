---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---

# Return em funções
- é usado para especificar o valor que a função deve retornar quando é chamada

ex : calculo de potenciação
```css
def calcular_potencia(base, expoente):
	resultado = base ** expoente
	return resultado

conta1 = calcular_potencia(13, 14)
conta2 = calcular_potencia(10, 10)
```
- toda função(def) possui um return mesmo quando não é declarado

##### early return
- quando um return é usado antes das instruções

```css
def calcular_potencia(base, expoente):
	if expoente > 0:
		return "número não pode ser negativo"
		
	resultado = base ** expoente
	return resultado

conta1 = calcular_potencia(13, 14)
conta2 = calcular_potencia(10, -10)
```
- neste caso a função só vai executar a segunda parte da função se a condição do if for verdadeira
	- retornando "número não pode ser negativo" caso não for


# Calculo de média com função

```css
def calculo_media(lista):
	if len(lista) == 0:
		return "não é possível calcular a lista"
	soma = 0
	for numero in lista:
		soma += numero

	media = soma / len(lista)
	return media

lista1 = [4, 5, 6, 7, 7, 8]
```



