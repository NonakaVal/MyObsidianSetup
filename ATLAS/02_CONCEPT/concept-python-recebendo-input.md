---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---

### Recebendo input

- comando "input()"
```css
idade = input("digite a idade\n")
idade = int(idade)

print("é maior de idade\n", idade >= 18)
```
- comando (input()) abre no terminal a opção de digitar o valor que será armazenada na variável (idade)
	- por padrão python o valor digitado sempre será do tipo "string"
- comando (int) aplicado a variável torna a string uma variável de valor intereiro (int)
	- comando (print) com string e operador relacional maior ou igual o valor armazenado na idade:
- (\n) usado para dar o espaço de uma linha na string 
