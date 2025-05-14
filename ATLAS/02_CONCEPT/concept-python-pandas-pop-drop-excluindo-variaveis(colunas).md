---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
---

usando del()
```css
del dados['Valor Bruto']
```
- a coluna 'valor bruto'

pop()
```css
dados_aux.pop('Valorm2')
```
- mesmo efeito do 'valor bruto'
	-  com a diferença que o valor pode retornar em uma variável enquanto com del o valor é excluído diretamente sem retornar

.drop()
```css
dados.drop(['Valorbrutom2', 'Valor Bruto'], axis = 1, inplace = True)
```




