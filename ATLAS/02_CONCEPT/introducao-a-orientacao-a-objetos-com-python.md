---
tags:
  - learning
HUB:
  - "[[hub-python]]"
---





1. **Nomes dos Atributos:**
    - **Primeira Classe (`Conta`):** Utiliza atributos com nomes simples, como `numero`, `titular`, `saldo` e `limite`.
    - **Segunda Classe (`Conta`):** Utiliza atributos com nomes precedidos por dois underscores (`__numero`, `__titular`, `__saldo` e `__limite`). Isso é uma convenção em Python para indicar que esses atributos são privados e não devem ser acessados diretamente fora da classe.
2. **Encapsulamento:**
    - **Primeira Classe:** Não utiliza encapsulamento. Isso significa que os atributos podem ser acessados diretamente de fora da classe.
    - **Segunda Classe:** Utiliza encapsulamento ao adicionar dois underscores antes dos nomes dos atributos. Isso significa que os atributos são considerados privados, e métodos especiais (getters e setters) geralmente são fornecidos para acessá-los ou modificá-los.


### Exemplo 1
```python
class Conta:

	def __init__(self, numero, titular, saldo, limite):
		print('construindo objeto{}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta_objeto = Conta(123,'John Doe', 1000, 500)

print("Número da conta:", conta_objeto.numero)
```


```python
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite
```

---

### Exemplo 2
```python 
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # Getter para o número da conta
    @property
    def numero(self):
        return self.__numero

    # Setter para o número da conta
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero

    # Getter para o titular da conta
    @property
    def titular(self):
        return self.__titular

    # Setter para o titular da conta
    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    # Getter para o saldo da conta
    @property
    def saldo(self):
        return self.__saldo

    # Setter para o saldo da conta
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    # Getter para o limite da conta
    @property
    def limite(self):
        return self.__limite

    # Setter para o limite da conta
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

```
