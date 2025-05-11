---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---


### Operadores lógicos

- info São usados para combinar ou negar valores booleanos (true ou false) e retornar true ou false com base nas condições de cada operador:
	- (and): retorna true se todas as expressões são verdadeiras, caso contrário retorna false
	- (or): retorna true se pelo menos uma das expressões forem verdadeiras, se não, retornará false
	- (not): retorna o inverso do valor booleano da expressão

```css
A = 15
B = 9
C = 9

print(B == C or A < B and A < C)
print((B == C or A < B) and A < C )
```

