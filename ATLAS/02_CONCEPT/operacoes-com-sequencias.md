---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---


#### [[python-operacoes|operacoes]] comuns com Sequências 

"x in s" retorna um 'True' se um item de s seja igual a x senão "False"
```css
x = 'olá mundo'
y = 'mundo'

nada = y in x

print(nada) # True
```

s+t concatenação de  de s e t (junta as duas sequências)
```css
x = 'olá'
y = " mundo"

saudacao = x + y
print(saudacao) # "olá mundo"
```

n* s multiplica a sequência n vezes
```css
i = [2]*10

print(i) # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
```

s[i] acessa um valor na posição i da sequência - o primeiro valor ocupa a posição 0
```css
i = [1, 2, 3, 4]
print(i[2]) # retornará 3
```

`[i:j:k]` acessa valores de i até j e k sendo o passo, ou seja, o intervalo que será consultado:
```css
i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(i[0:7:2]) # [1, 3, 5, 7]
```
o valor de k também pode ser invertido, mas por padrão é 1
```css
i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(i[7:0:-2]) # [8, 6, 4, 2]
```

`len(s)` comprimento de s, usada para saber o tamanho da sequência:
```css
i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(i)) # 10
```


`min(s)` usada para saber o menor valor da sequência
```css
i = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(i)) # 2
```

`max(s) ` maior valor da sequência:
```css
i = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(max(i)) # 10
```

`s.count(x)` conta quantas vezes o x foi encontrado no s:
```css
i = [2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = 2
  
print(i.count(x)) # 3
```

[[concept-python-arrays]]