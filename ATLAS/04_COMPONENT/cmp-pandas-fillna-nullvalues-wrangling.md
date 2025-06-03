---
tags:
  - learning
  - component
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
dg-publish: true
---


métodos no [[removendo-valores-nulos|fillna()]]
**ffill** e **bfill**
```css
s.fillna(method = 'ffill')
```
- forward fill 
	- preenche os valores nulos com os valores anteriores válidos
```css
s.fillna(method = 'bfill')
```
- backward fill
	- preenche os valores nulos com os valores anteriores validos de baixo pra cima
 limit
```css
s1 = s.fillna(method = 'ffill', limit = 1)
```
-  estabele um limite de quantos valores nulos podem ser sobrepostos com os valores anteriores
	- fowardfill com limite armazenado em uma nova variável

```css
s1.fillna(method = 'bfill', limit = 1)
```
- aplicando backwardfill na variável
