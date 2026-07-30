---
dateCreated: "[[2025-06-11]]"
tags:
  - learning/review
  - learning
subject:
  - "[[hub-regex]]"
  - "[[hub-tec]]"
  - "[[hub-linux]]"
related:
  - "[[draft-regex-rg-all-notes]]"
  - "[[cmp-first-ripgrep-regex-queries]]"
  - "[[draft-code-search-ripgrap-functions]]"
---

## Validaçao de e-mail simples
**Exemplo:** Padrao basico para emails
```
\w+@\w+\.\w+
```
- Encontra: "nome@site.com", "user123@mail.br"
- Versao simplificada (nao cobre todos os casos validos)

### Como praticar:
1. Abra o Bloco de Notas ou VS Code
2. Ative a busca com regex (geralmente com Ctrl+F e marcando a opçao "Regex")
3. Cole este texto de exemplo e teste os padrões acima:

```
O gato e os gatos brincam no jardim. 
Meus números favoritos sao 123 e 4567.
Data importante: 25/12/23.
Meu email é teste@exemplo.com e o seu é usuario123@site.br.
As siglas sao BR, EUA e ONU.
O rio esta limpo, diferente do prion proteico.
```

Dica: Comece modificando estes exemplos simples antes de tentar padrões mais complexos!

Aqui esta uma lista pratica de exemplos de regex, organizada por níveis de complexidade:

#### Nível Basico (Padrões Simples)
1. **Palavra exata**
   - `gato` → encontra "gato" (mas nao "GATO" ou "gatinho")

1. **Variaçao simples**
   - `gatos?` → encontra "gato" e "gatos" (`s` opcional)

3. **Qualquer caractere**
   - `p.to` → encontra "pato", "pito", "péto" (mas nao "pto")

4. **Início/Fim de palavra**
   - `\bcasa\b` → encontra "casa" mas nao "casaco"

#### Nível Intermediario (Classes e Quantificadores)
5. **Números simples**
   - `\d\d\d` → encontra "123", "456" (3 dígitos)

6. **Letras específicas**
   - `[A-Za-z]` → qualquer letra maiúscula ou minúscula

7. **Intervalo de caracteres**
   - `[0-5]` → números de 0 a 5

8. **Repetições**
   - `a{2,4}` → encontra "aa", "aaa" ou "aaaa"

#### Nível Avançado (Validações Úteis)
9. **Data simples (DD/MM/AAAA)**
   - `\d{2}/\d{2}/\d{4}` → "25/12/2023"

9. **E-mail basico**
    - `\w+@\w+\.\w{2,3}` → "user@mail.com"

10. **CEP brasileiro**
    - `\d{5}-\d{3}` → "12345-678"

11. **Horario (24h)**
    - `([01]?[0-9]|2[0-3]):[0-5][0-9]` → "09:30" ou "23:59"

### Exemplos Praticos no Mundo Real
13. **Extrair URLs**
    - `https?://[^\s]+` → "http://site.com" ou "https://exemplo.org"

14. **Identificar hashtags**
    - `#[A-Za-z0-9_]+` → "#regex #Aula123"

15. **Validar senha (6+ chars com número)**
    - `^(?=.*\d).{6,}$` → "senha123" (mas nao "senha")

16. **Remover HTML tags**
    - `<\/?[^>]+>` → remove `<b>`, `</p>`, etc.

### Bônus (Truques Úteis)
17. **Substituir múltiplos espaços**
    - `\s+` → por " " (um único espaço)

18. **Capturar conteúdo entre aspas**
    - `"([^"]*)"` → pega o texto dentro das aspas

19. **Encontrar palavras repetidas**
    - `\b(\w+)\s+\1\b` → encontra "o o gato" (repetiçao do "o")

20. **Versao simplificada para CPF**
    - `\d{3}\.?\d{3}\.?\d{3}-?\d{2}` → aceita "123.456.789-00" ou "12345678900"

### Como usar estes exemplos:
1. **Em editores de texto** (VS Code, Sublime): Ative regex no Ctrl+F
2. **Em linguagens de programaçao**:
   ```python
   import re
   re.findall(r'\d{3}', "ABC 123 DEF 456")  # Retorna ['123', '456']
   ```

Dica: Teste estes padrões em ferramentas como [Regex101](https://regex101.com/) com textos reais para ver os matches em tempo real!

← Parte de [[concept-regex-introductions-and-basic]]