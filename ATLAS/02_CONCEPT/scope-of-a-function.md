---
tags:
  - learning
HUB:
  - "[[hub-python]]"
created: "[[2024-03-07]]"
---
2024-03-07  19:49


>[!info] Scope
>>Ao definir uma variável dentro de uma [[concept-Writng-Functlons-In-Python|funcao]], o valor dessa variável será usada apenas dentro do escopo dessa função, o interpretador só irá buscar fora desse escopo caso não encontre dentro desse escopo, ou caso seja definida para usar valores em escopos específicos com métodos como `global` ou `nonlocal`

![Imgur|400](https://i.imgur.com/hzesp4Y.png)

[[scope-and-user-defined-functions]]
### **Global** : usa o valor definido fora da função

```python
call_count = 0

def my_function():
  # Use a keyword that lets us update call_count 
  global call_count
  call_count += 1
  print("You've called my_function() {} times!".format(
    call_count
  ))

for _ in range(20):
  my_function()
```


### **nonlocal keyword**:  funções dentro de funções,
usada quando estamos trabalhando com [[concept-Writng-Functlons-In-Python|funcoes]] aninhadas, ou seja, funções dentro de funções, permitindo atribuir valores específicos para a mesma variável dentro de um escopo específico da função

```python
def foo():
    x = 10
    def bar():
        x = 200
        print(x)
    bar()
    print(x)

foo()  # 200 e 10
```

```python
def foo():
    x = 10
    def bar():
        nonlocal x
        x = 200
        print(x)
    bar()
    print(x)

foo() # 200 e 200
```

### **Clousure**:
Ocorre quando uma variável de uma função interna faz referência a uma variável da função externa:

```python
def parent(arg_1, arg_2):
    value = 22
    my_dict = {'chocolate':'yummy'}
    
    def child():
        print(2 *value)
        print(my_dict['chocolate'])
        print(arg_1 + arg_2)
    return child

new_function = parent(3,4)

print([cell.cell_contents for cell in new_function.__closure__])
```




