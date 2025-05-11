---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---

#### Tipo sequência de caracteres (strings)
- são imutáveis introduzidas em [[tipos-de-variaveis]]

```css
texto = "Aprendendo python na disciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"python in texto = {'python' in texto}" )
print (f"quantidade de y no texto = {texto.count('y')}" )
print (f"as 5 primeiras letras são = {texto[0:5]}")
```

``lower()`` e ``upper()`` para tornar letras minúsculas ou maiúsculas e replace 

```css
texto = "Aprendendo python na disciplina de linguagem de programação"
print(texto.upper())
print(texto.replace("o", "X"))

# APRENDENDO PYTHON NA DISCIPLINA DE LINGUAGEM DE PROGRAMAÇÃO
# AprendendX pythXn na disciplina de linguagem de prXgramaçãX

```
![[concept-python-split]]
