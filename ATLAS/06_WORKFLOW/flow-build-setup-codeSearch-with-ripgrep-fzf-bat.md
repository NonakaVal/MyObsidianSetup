---
created: "[[2025-06-14]]"
HUB:
  - "[[hub-regex]]"
  - "[[hub-linux]]"
connections:
  - "[[cmp-first-ripgrep-regex-queries]]"
  - "[[concept-regex-introductions-and-basic]]"
tags:
  - learning
---
# Key Features
1. **Automatic Dependency Check** - Verifies `fzf` and `ripgrep` are installed
2. **Multi-OS Support** - Handles both `bat` (macOS) and `batcat` (Linux)
3. **Smart Preview Fallback** - Uses `head` if bat isn't available
4. **Enhanced Language Support** - Special handling for JS/TS/Go
5. **New Search Modes** - Added dedicated `search_todos()` function
6. **Interactive Reload** - Change searches dynamically with `alt-f` binding
7. **Better Error Handling** - Previews show fallback message when unavailable

##💻 Instalação e Configuração

### 🐧 Configuração no WSL

[[draft-reset-wsl-dist|Guia de Configuração no WSL]]

```bash
# Atualize os pacotes e instale as dependências necessárias
sudo apt update && sudo apt install -y ripgrep fzf bat
```

### Instalação via Homebrew (macOS/Linux)

```bash
# Instale as dependências
brew install ripgrep fzf bat
```

---

### ⌨️ Atalhos de Teclado no Modo Interativo

Durante a execução no modo interativo do FZF:

- `Enter`: Seleciona e sai com o resultado.
    
- `Ctrl+C`: Interrompe a busca.
    
- `Alt+F`: Restaura o padrão original de busca.
    
- `Ctrl+R`: Alterna o modo regex.
    
- `Tab`: Ativa o modo de seleção múltipla.
    
# CORE SCRIPTS

## [[snip-rg-search-code]]




---

## 📚 Exemplos de Uso

### 🔍 Exemplos Básicos

- **[[draft-codeSearchbasic-usage-examples|Busca por palavras específicas]]**: Encontre todas as ocorrências de "gato" no texto.
    
- **[[draft-codeSearchbasic-usage-examples|Busca com variações simples]]**: Encontre "casa" no singular ou plural.
    
- **[[draft-codeSearchbasic-usage-examples|Busca por qualquer caractere]]**: Encontre palavras que começam com "p" e terminam com "to".
    
- **[[draft-codeSearchbasic-usage-examples|Busca por dígitos numéricos]]**: Encontre números de 3 dígitos.
    
- **[[draft-codeSearchbasic-usage-examples|Validação de datas simples]]**: Encontre datas no formato DD/MM/AA.
    
- **[[draft-codeSearchbasic-usage-examples|Busca por letras maiúsculas]]**: Encontre siglas de 2 ou 3 letras maiúsculas.
    
- **[[draft-codeSearchbasic-usage-examples|Busca por vogais]]**: Encontre todas as vogais em um texto.
    
- **[[draft-codeSearchbasic-usage-examples|Validação de senha simples]]**: Senha com pelo menos 6 caracteres.
    
- **[[draft-codeSearchbasic-usage-examples|Busca por palavras inteiras]]**: Encontre apenas a palavra "rio".
    
- **[[draft-codeSearchbasic-usage-examples|Validação de e-mail simples]]**: Padrão básico para e-mails.
    

### 🛠️ Exemplos Avançados

- **[[draft-codeSearchadvanced-workflows|Extração de URLs]]**: `https?://[^\s]+` encontra URLs com http ou https.
    
- **[[draft-codeSearchadvanced-workflows|Identificação de hashtags]]**: `#[A-Za-z0-9_]+` encontra hashtags como "#regex".
    
- **[[draft-codeSearchadvanced-workflows|Validação de CPF]]**: Expressões para validar o formato de CPF.
    

---

## 🌐 Integração com Git e Outros Ferramentas

- **[[draft-codeSearchgit-integration-examples|Integração com Git]]**: Como buscar por commits, branches ou tags específicas no seu repositório Git.
    
- **[[draft-codeSearchcombined-with-other-tools|Combinando com Outras Ferramentas]]**: Usando a ferramenta de busca junto a outras, como `grep`, `awk`, ou `sed`.
    
