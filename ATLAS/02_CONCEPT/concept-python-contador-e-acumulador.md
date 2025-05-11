---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---


```css
n = int(input('digite o número de temperaturas\n'))

if n >= 0:
	s =0
	i =1 # contador
	while i <=n:
		t = int(input('temperatura\n'))
		s = s+t # acoumulador
		i = i+1 
	print(s/n)      
else:
print('numerop deve ser maior que zero')
```

