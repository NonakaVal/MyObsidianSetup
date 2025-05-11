---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---

##### Valor padrão na função
```css
def calcular_potencia(base, expoente=2):
	resultado = base ** expoente
	return resultado

conta1 = calcular_potencia(13, 14)
conta2 = calcular_potencia(10)
```
- valor padrão da função é quando um valor é atribuido diretamente na função
	- o valor só retona o valor quando não existe nenhuma valor sobreescrito na chamada da função
		- conta1 por exemplo realiza a operação normal
			- já a conta 2 toma o valor padrão da função