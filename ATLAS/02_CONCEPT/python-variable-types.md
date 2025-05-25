---
tags:
  - learning
HUB:
  - "[[hub-python]]"
aliases:
  - data-types
dg-publish: false
---
### Primitivas:

1. **String**
	- "olá mundo"
2. **Float/decimal**
	-  9.99
3. **Inteiro**
	-  10 and 20
4. **Booleanos/lógicos**
	- true/false


- info Comando que retorna a classe no terminal `.type()`
- pen Exemplo com types
```python
salgado = 8 
refri = 5
subtotal = salgado + refri
gorjeta = subtotal * 0.1
total = subtotal + gorjeta
print(total)
```

- info **Truthy e Falsy**
- Regras que são aplicados implicitamente de tipos não booleanos 
	- categoriza em (truthy) ou (falsy)

- ! Truthy 
	- qualquer número diferente de 0 (inteiros, float, complexos)
	- qualquer string não vazia
	- qualquer objeto 'None'
	- sequencia não vazia
	- mapeamento não vazio (dicionário)
- ! Falsy
	- O valor `'False'`
	- O valor `'None'`
	- Qualquer numero 0
	- qualquer sequência vazia (lista vazia, tupla) ou mapeamento

