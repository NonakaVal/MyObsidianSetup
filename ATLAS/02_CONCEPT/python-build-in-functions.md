---
tags:
  - learning
  - learning/review
HUB:
  - "[[hub-python]]"
---
2024-03-17  06:17


##### [Built-in functions](https://docs.python.org/3/library/functions.html)

ex: ``eval()``
```css
equacao = input("digite a formula geral  da equação linear (a * x + b)")
print(f"\n a entrada do usuário {equacao} é do tipo {type(equacao)}")
for x in range(5):
    y = eval(equacao)
    print(f"\n resultado da para x é = {x} é {y}")
```
