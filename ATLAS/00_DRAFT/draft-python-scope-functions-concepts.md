---
type: new_note
tags:
  - new_note
created: '[[2025-05-20]]'
---
### Scope
Ao definir uma variável dentro de uma [[concept-Writng-Functlons-In-Python|funcao]], o valor dessa variável será usada apenas dentro do escopo dessa função, o interpretador só irá buscar fora desse escopo caso não encontre dentro desse escopo, ou caso seja definida para usar valores em escopos específicos com métodos como `global` ou `nonlocal`

global: usa o valor definido fora da função

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


nonlocal:
the nonlocal keyword: usada quando estamos trabalhando com [[concept-Writng-Functlons-In-Python|funcoes]] aninhadas, ou seja, funções dentro de funções, permitindo atribuir valores específicos para a mesma variável dentro de um escopo específico da função

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

Clousure:
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




## Decorators
Funções que recebem uma função como argumento e cria uma versão modificada dessa função.

Sintataxe de decorators e double_args 

```python
def multiply(a, b):
    return a * b
```

```python
def double_args(func):
	def wraper(a,b)
		return func(a *2,b *2)
	return wraper

new_multiply = duble_args(multiply)
new_multiply(1,5)
```

```python
@duble_args
def multiply(a,b):
	return a *b
new_multiply(1,5)

```

```python
# Simulação de uma base de dados de usuários autenticados
usuarios_autenticados = {'usuario1': 'senha123', 'usuario2': 'senha456'}

def autenticar_usuario(usuario, senha):
    # Função que verifica a autenticação (simulação)
    return usuario in usuarios_autenticados and usuarios_autenticados[usuario] == senha

def autenticado_required(func):
    def wrapper(usuario, senha, *args, **kwargs):
        if autenticar_usuario(usuario, senha):
            print(f"Usuário {usuario} autenticado com sucesso.")
            return func(*args, **kwargs)
        else:
            print("Autenticação falhou. Acesso negado.")
    return wrapper


@autenticado_required
def operacao_secreta():
    print("Operação secreta realizada com sucesso!")

# Tentativa de chamar a função decorada sem autenticação
operacao_secreta(usuario='usuario1', senha='senha12')
```

---

```python 
import functools

class Usuario:
    def __init__(self, nome, tem_permissao=False):
        self.nome = nome
        self.tem_permissao = tem_permissao

def verificar_permissao(func):
    @functools.wraps(func)
    def wrapper(usuario, *args, **kwargs):
        if usuario.tem_permissao:
            print(f"Usuário {usuario.nome} tem permissão para executar a função.")
            resultado = func(usuario, *args, **kwargs)
            return resultado
        else:
            print(f"Acesso negado para o usuário {usuario.nome}.")
            # Poderíamos levantar uma exceção aqui ou fazer qualquer outra ação desejada.
    return wrapper

@verificar_permissao
def operacao_secreta(usuario):
    print(f"Executando operação secreta para o usuário {usuario.nome}.")

# Criando um usuário com permissão
usuario_com_permissao = Usuario(nome="Alice", tem_permissao=True)

# Criando um usuário sem permissão
usuario_sem_permissao = Usuario(nome="Bob", tem_permissao=False)

# Testando as funções decoradas
operacao_secreta(usuario_com_permissao)  # Usuário com permissão
operacao_secreta(usuario_sem_permissao)  # Usuário sem permissão
```


