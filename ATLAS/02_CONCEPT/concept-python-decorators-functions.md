---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
created: "[[2024-03-09]]"
share_link: https://share.note.sx/4tilrsxf#fORycnMm6dHGHRRi1tRlQHyFAE68c+hLO5f1lisQHzw
share_updated: 2025-05-11T01:01:29-03:00
---
# Decoradores em Python

## Conceito Básico
Decoradores são funções que:
- Recebem uma função como argumento
- Retornam uma nova função modificada
- Permitem estender comportamento sem alterar código original

## Sintaxe Fundamental
```python
def decorador(func):
    def wrapper(*args, **kwargs):
        # Código pré-execução
        resultado = func(*args, **kwargs)
        # Código pós-execução
        return resultado
    return wrapper
```

## Exemplo Prático: Decorador de Autenticação
```python
usuarios = {'user1': 'pass123', 'user2': 'pass456'}

def autenticado_required(func):
    def wrapper(usuario, senha, *args, **kwargs):
        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"Autenticação bem-sucedida para {usuario}")
            return func(*args, **kwargs)
        else:
            print("Acesso negado!")
    return wrapper

@autenticado_required
def operacao_restrita():
    print("Operação sensível executada")

operacao_restrita(usuario='user1', senha='pass123')  # Autenticado
operacao_restrita(usuario='user1', senha='errada')   # Negado
```

## Decorador com Classes
```python
import functools

class ControleAcesso:
    def __init__(self, tem_acesso=False):
        self.tem_acesso = tem_acesso

    def verificar_acesso(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.tem_acesso:
                return func(*args, **kwargs)
            print("Acesso restrito!")
        return wrapper

admin = ControleAcesso(tem_acesso=True)
usuario = ControleAcesso(tem_acesso=False)

@admin.verificar_acesso
def config_sistema():
    print("Configurações alteradas")

config_sistema()  # Executa
```

## Boas Práticas
1. Use `functools.wraps` para preservar metadados
2. Documente o propósito do decorador
3. Mantenha a assinatura original quando possível
4. Evite efeitos colaterais complexos

## Casos de Uso Comuns
✅ Validação de acesso  
✅ Logging de execução  
✅ Medição de tempo  
✅ Cache de resultados  
✅ Tratamento de exceções  

> **Dica**: Decoradores podem ser combinados usando múltiplas declarações `@`

Principais benefícios:
- Separação de preocupações
- Reutilização de código
- Extensibilidade limpa
- Manutenção simplificada