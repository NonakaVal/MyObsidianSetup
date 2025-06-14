---
created: "[[2025-06-14]]"
tags:
  - snippet
HUB:
  - "[[hub-regex]]"
  - "[[hub-linux]]"
connections:
  - "[[draft-regex-rg-all-notes]]"
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}

Conjunto completo para buscas interativas em código com suporte a múltiplas linguagens, pré-visualização inteligente e modos personalizados. Inclui verificação automática de dependências, seleção de visualizador e modos configuráveis para busca por definições, comentários, TODOs e trechos genéricos.

# {código}


```bash
# ==============================================
# FZF Code Search Suite (Full Installation)
# ==============================================

# Dependencies check
_code_search_deps=("fzf" "rg")
for dep in "${_code_search_deps[@]}"; do
  if ! command -v "$dep" &> /dev/null; then
    echo "⚠️  Missing dependency: $dep"
    case "$dep" in
      fzf) echo "Install with: sudo apt install fzf (or brew install fzf)" ;;
      rg)  echo "Install ripgrep: sudo apt install ripgrep (or brew install ripgrep)" ;;
    esac
    return 1 2>/dev/null || exit 1
  fi
done

# Smart preview selector
if command -v bat &> /dev/null; then
  export FZF_PREVIEW_CMD="bat --style=numbers,header --color=always --line-range"
elif command -v batcat &> /dev/null; then  # Ubuntu/Debian alternative
  export FZF_PREVIEW_CMD="batcat --style=numbers,header --color=always --line-range"
else
  export FZF_PREVIEW_CMD="head -n 100"
  echo "ℹ️  For better previews, install 'bat': sudo apt install bat (or brew install bat)"
fi

# Core search engine
_search_engine() {
  local mode="$1" query="$2" lang="${3:-py}"
  local ext pattern preview_range

  # Language extension mapping
  case "$lang" in
    js|javascript) ext="js" ;;
    ts|typescript) ext="ts" ;;
    go|golang)     ext="go" ;;
    *)             ext="$lang" ;;
  esac

  # Mode configuration
  case "$mode" in
    strict)   
      pattern="^(def|class|function|const|let|var|struct|enum|interface|trait)\\s+\\w+"
      preview_range=":200"
      ;;
    balanced) 
      pattern="^(function|class|const|let|var|import|export|def|from|type|module)\\s"
      preview_range=":300" 
      ;;
    comments) 
      pattern="(^\\s*[#//]|/\\*|^\\s*--|^\\s*\"\"\")"
      preview_range=":100"
      ;;
    todos)    
      pattern="(TODO|FIXME|NOTE|BUG|XXX|HACK)[ :]" 
      preview_range=":50"
      ;;
    flexible) 
      pattern="."
      preview_range=":500" 
      ;;
    *)        
      echo "Invalid mode: $mode" >&2
      return 1
      ;;
  esac

  # Build preview command
  local preview_cmd="$FZF_PREVIEW_CMD $preview_range {1} 2>/dev/null || echo 'Preview not available'"

  # Execute search
  rg --color=always --hidden --follow --smart-case -n "$pattern" -g "*.$ext" |
  awk -F: '{
    filename=$1
    gsub(/^.*\//, "", filename)
    print $1 ":" $2 ":" filename ":" substr($0, index($0,$3))
  }' |
  fzf \
    --query "$query" \
    --ansi \
    --delimiter=":" \
    --with-nth="3,4" \
    --preview="$preview_cmd" \
    --preview-window="right:48%:wrap" \
    --bind "change:reload(rg --color=always --hidden --smart-case -n {q} -g '*.$ext' || echo 'No matches')" \
    --bind "alt-f:unbind(change)+reload(rg --color=always --hidden -n '$pattern' -g '*.$ext')" \
    --height=90% \
    --layout=reverse \
    --border=rounded \
    --prompt="Code($mode:$ext)> "
}

# User-friendly wrappers
search_code()       { _search_engine "balanced" "$@"; }
search_def()        { _search_engine "strict" "$@"; }
search_comments()   { _search_engine "comments" "$@"; }
search_todos()      { _search_engine "todos" "$@"; }
search_all()        { _search_engine "flexible" "$@"; }

# CLI version (optional)
code_search() {
  case "$1" in
    -m) _search_engine "$2" "$4" "$3";;
    *)  _search_engine "flexible" "$@";;
  esac
}
```

← Parte de [[flow-build-setup-codeSearch-with-ripgrep-fzf-bat]]

#  code_search bash core command -2 with alias

```BASH
#!/bin/bash

# ==============================================
# FZF Code Search Suite - Full Installation
# ==============================================

# 👉 1. Checagem de Dependências
_code_search_deps=("fzf" "rg")
for dep in "${_code_search_deps[@]}"; do
  if ! command -v "$dep" &> /dev/null; then
    echo "⚠️  Missing dependency: $dep"
    case "$dep" in
      fzf) echo "Install with: sudo apt install fzf (or brew install fzf)" ;;
      rg)  echo "Install ripgrep: sudo apt install ripgrep (or brew install ripgrep)" ;;
    esac
    return 1 2>/dev/null || exit 1
  fi
done

# 👉 2. Configuração do Preview Inteligente
if command -v bat &> /dev/null; then
  export FZF_PREVIEW_CMD="bat --style=numbers,header --color=always --line-range"
elif command -v batcat &> /dev/null; then
  export FZF_PREVIEW_CMD="batcat --style=numbers,header --color=always --line-range"
else
  export FZF_PREVIEW_CMD="head -n 100"
  echo "ℹ️  Para previews aprimorados, instale 'bat': sudo apt install bat"
fi

# 👉 3. Função Principal de Busca
_search_engine() {
  local mode="$1" query="$2" lang="${3:-py}"
  local ext pattern preview_range

  # Extensões por linguagem
  case "$lang" in
    js|javascript) ext="js" ;;
    ts|typescript) ext="ts" ;;
    go|golang)     ext="go" ;;
    *)             ext="$lang" ;;
  esac

  # Padrões por modo
  case "$mode" in
    strict)   
      pattern="^(def|class|function|const|let|var|struct|enum|interface|trait)\\s+\\w+"
      preview_range=":200"
      ;;
    balanced) 
      pattern="^(function|class|const|let|var|import|export|def|from|type|module)\\s"
      preview_range=":300" 
      ;;
    comments) 
      pattern="(^\\s*[#//]|/\\*|^\\s*--|^\\s*\"\"\")"
      preview_range=":100"
      ;;
    todos)    
      pattern="(TODO|FIXME|NOTE|BUG|XXX|HACK)[ :]" 
      preview_range=":50"
      ;;
    flexible) 
      pattern="."
      preview_range=":500" 
      ;;
    *)        
      echo "❌ Modo inválido: $mode" >&2
      return 1
      ;;
  esac

  # Comando de preview final
  local preview_cmd="$FZF_PREVIEW_CMD $preview_range {1} 2>/dev/null || echo 'Preview not available'"

  # Execução do fzf com rg
  rg --color=always --hidden --follow --smart-case -n "$pattern" -g "*.$ext" |
  awk -F: '{
    filename=$1
    gsub(/^.*\//, "", filename)
    print $1 ":" $2 ":" filename ":" substr($0, index($0,$3))
  }' |
  fzf \
    --query "$query" \
    --ansi \
    --delimiter=":" \
    --with-nth="3,4" \
    --preview="$preview_cmd" \
    --preview-window="right:48%:wrap" \
    --bind "change:reload(rg --color=always --hidden --smart-case -n {q} -g '*.$ext' || echo 'No matches')" \
    --bind "alt-f:unbind(change)+reload(rg --color=always --hidden -n '$pattern' -g '*.$ext')" \
    --height=90% \
    --layout=reverse \
    --border=rounded \
    --prompt="Code($mode:$ext)> "
}

# 👉 4. Funções Wrapper
search_code()       { _search_engine "balanced" "$@"; }
search_def()        { _search_engine "strict" "$@"; }
search_comments()   { _search_engine "comments" "$@"; }
search_todos()      { _search_engine "todos" "$@"; }
search_all()        { _search_engine "flexible" "$@"; }

# 👉 5. CLI Alternativo
code_search() {
  case "$1" in
    -m) _search_engine "$2" "$4" "$3";;
    *)  _search_engine "flexible" "$@";;
  esac
}

# 👉 6. Aliases Recomendados
alias sd='search_def'
alias sc='search_code'
alias st='search_todos'
alias sa='search_all'

# ✅ Pronto para uso!
echo "✅ FZF Code Search Suite instalado e pronto."

```

