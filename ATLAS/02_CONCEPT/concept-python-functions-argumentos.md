---
tags:
  - learning
  - 
HUB:
  - "[[hub-python]]"
---
### Argumentos em Funções

#### 1. Argumentos Posicionais
Valores que são passados na ordem dos parâmetros da função.

```python
def boas_vindas(nome, sobrenome, curso):
    print("Olá", nome, sobrenome)
    print("Bem vindo ao curso de", curso)

# Chamada posicional
boas_vindas("Rodrigo", "Saldanha", "Python")
```

Características:
- A posição determina qual parâmetro recebe qual valor
- Ordem: 
  1. "Rodrigo" → `nome`
  2. "Saldanha" → `sobrenome` 
  3. "Python" → `curso`

#### 2. Argumentos Nomeados (Keyword Arguments)
Valores passados explicitamente associados a seus parâmetros.

```python
def boas_vindas(nome, sobrenome, curso):
    print("Olá", nome, sobrenome)
    print("Bem vindo ao curso de", curso)

# Chamada nomeada
boas_vindas(nome="Rodrigo", curso="Python", sobrenome="Saldanha")
```

Vantagens:
- Independência da ordem de declaração
- Maior clareza do código
- Devem ser passados **após** os argumentos posicionais (se misturados)


Regra importante:  
`Argumentos nomeados sempre vêm após os posicionais em chamadas de função`
```

Key improvements:
1. Fixed encoding issues (ç, ã, etc.)
2. Proper Python syntax highlighting
3. Clear hierarchical structure
4. Added explanations of characteristics
5. Better visual separation between sections
6. Consistent formatting
7. Added important usage rule
8. Fixed indentation in code examples
9. Added emphasis to key s

