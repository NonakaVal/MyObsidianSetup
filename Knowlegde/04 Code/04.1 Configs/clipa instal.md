---
dateCreated: "[[2026-05-22]]"
---
No Arch/EndeavourOS, troca o `apt` por `pacman`:

```bash
sudo pacman -Syu --needed wl-clipboard fzf xclip xsel git
```

Se quiser já instalar com histórico de clipboard também:

```bash
sudo pacman -Syu --needed wl-clipboard fzf xclip xsel git cliphist copyq
```

O pacote `wl-clipboard` fornece `wl-copy` e `wl-paste` no Arch, e o `cliphist` também está no repositório `extra`, dependendo do `wl-clipboard`. ([Arch Linux](https://archlinux.org/packages/extra/x86_64/wl-clipboard/?utm_source=chatgpt.com "Arch Linux - wl-clipboard 1:2.3.0-1 (x86_64)"))

Depois cria o comando global:

```bash
mkdir -p ~/.local/bin

cat > ~/.local/bin/clipa <<'EOF'
#!/usr/bin/env bash

copy_clipboard() {
  if command -v wl-copy >/dev/null 2>&1 && [[ "${XDG_SESSION_TYPE:-}" == "wayland" ]]; then
    wl-copy
  elif command -v xclip >/dev/null 2>&1; then
    xclip -selection clipboard
  elif command -v xsel >/dev/null 2>&1; then
    xsel --clipboard --input
  elif command -v pbcopy >/dev/null 2>&1; then
    pbcopy
  elif command -v copyq >/dev/null 2>&1; then
    copyq add -
  else
    echo "Nenhuma ferramenta de clipboard encontrada." >&2
    exit 1
  fi
}

paste_clipboard() {
  if command -v wl-paste >/dev/null 2>&1 && [[ "${XDG_SESSION_TYPE:-}" == "wayland" ]]; then
    wl-paste
  elif command -v xclip >/dev/null 2>&1; then
    xclip -selection clipboard -o
  elif command -v xsel >/dev/null 2>&1; then
    xsel --clipboard --output
  elif command -v pbpaste >/dev/null 2>&1; then
    pbpaste
  elif command -v copyq >/dev/null 2>&1; then
    copyq clipboard
  else
    echo "Nenhuma ferramenta de leitura do clipboard encontrada." >&2
    exit 1
  fi
}

notify_copy() {
  echo "Copiado: $1"
}

pick_file() {
  find . -type f 2>/dev/null | sed 's#^\./##' | fzf --prompt="Arquivo > "
}

pick_dir() {
  find . -type d 2>/dev/null | sed 's#^\./##' | fzf --prompt="Pasta > "
}

choice=$(cat <<MENU | fzf --prompt="Clipboard Assistant > " --height=40% --border
pwd                 Copiar caminho atual
pwd-md              Copiar caminho atual como inline Markdown
cd                  Copiar comando cd para pasta atual
code                Copiar comando code para pasta atual
file                Escolher arquivo e copiar caminho absoluto
file-cmd            Escolher arquivo e copiar comando cat
dir                 Escolher pasta e copiar caminho absoluto
branch              Copiar branch Git atual
git-root            Copiar raiz do repositório Git
git-remote          Copiar URL remote origin
diff                Copiar git diff
diff-staged         Copiar git diff --staged
last14              Copiar últimos 14 comandos
last14-clean        Copiar últimos 14 comandos sem numeração
clip-show           Mostrar conteúdo atual do clipboard
clip-md             Copiar clipboard atual como bloco Markdown
today               Copiar data de hoje
now                 Copiar data e hora atual
MENU
)

key="${choice%% *}"

case "$key" in
  pwd)
    printf "%s" "$PWD" | copy_clipboard
    notify_copy "$PWD"
    ;;

  pwd-md)
    printf '`%s`' "$PWD" | copy_clipboard
    notify_copy "caminho em Markdown"
    ;;

  cd)
    printf "cd %q" "$PWD" | copy_clipboard
    notify_copy "cd $PWD"
    ;;

  code)
    printf "code %q" "$PWD" | copy_clipboard
    notify_copy "code $PWD"
    ;;

  file)
    file=$(pick_file) || exit 0
    realpath "$file" | copy_clipboard
    notify_copy "$(realpath "$file")"
    ;;

  file-cmd)
    file=$(pick_file) || exit 0
    printf "cat %q" "$(realpath "$file")" | copy_clipboard
    notify_copy "cat $(realpath "$file")"
    ;;

  dir)
    dir=$(pick_dir) || exit 0
    realpath "$dir" | copy_clipboard
    notify_copy "$(realpath "$dir")"
    ;;

  branch)
    git branch --show-current 2>/dev/null | copy_clipboard
    notify_copy "branch atual"
    ;;

  git-root)
    git rev-parse --show-toplevel 2>/dev/null | copy_clipboard
    notify_copy "raiz do repositório"
    ;;

  git-remote)
    git remote get-url origin 2>/dev/null | copy_clipboard
    notify_copy "remote origin"
    ;;

  diff)
    git diff | copy_clipboard
    notify_copy "git diff"
    ;;

  diff-staged)
    git diff --staged | copy_clipboard
    notify_copy "git diff --staged"
    ;;

  last14)
    history 14 | copy_clipboard
    notify_copy "últimos 14 comandos"
    ;;

  last14-clean)
    history 14 | sed 's/^ *[0-9]* *//' | copy_clipboard
    notify_copy "últimos 14 comandos limpos"
    ;;

  clip-show)
    paste_clipboard
    ;;

  clip-md)
    {
      echo '```'
      paste_clipboard
      echo '```'
    } | copy_clipboard
    notify_copy "clipboard como bloco Markdown"
    ;;

  today)
    date "+%Y-%m-%d" | copy_clipboard
    notify_copy "data de hoje"
    ;;

  now)
    date "+%Y-%m-%d %H:%M:%S" | copy_clipboard
    notify_copy "data e hora"
    ;;

  *)
    exit 0
    ;;
esac
EOF

chmod +x ~/.local/bin/clipa
```

Garante que `~/.local/bin` está no PATH:

```bash
grep -q 'export PATH="$HOME/.local/bin:$PATH"' ~/.bashrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Testa:

```bash
clipa
```

Aliases estilo macOS:

```bash
cat >> ~/.bashrc <<'EOF'

# Clipboard helpers
alias pbcopy='wl-copy'
alias pbpaste='wl-paste'
alias clipa="$HOME/.local/bin/clipa"

EOF

source ~/.bashrc
```

Uso:

```bash
pwd | pbcopy
pbpaste
clipa
```

Pra evoluir isso depois, eu colocaria um atalho global no KDE/GNOME chamando `kitty -e clipa`, ou faria uma versão `rofi/dmenu` para abrir como popup gráfico. Aí vira literalmente um “clipboard command palette” do sistema.

