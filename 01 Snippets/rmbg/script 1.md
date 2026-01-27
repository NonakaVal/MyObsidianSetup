---
title: script 1
id: 6
---

```
#!/bin/bash

DESTINO="sem_fundo"
MODO="single"

# Parse de argumentos
for arg in "$@"; do
  case "$arg" in
    --all)
      MODO="all"
      ;;
    *)
      DESTINO="$arg"
      ;;
  esac
done

echo "🐳 Remoção de fundo via Docker (rembg)"

# Verificações
if ! command -v docker &>/dev/null; then
  echo "❌ Docker não instalado."
  exit 1
fi

if ! docker info &>/dev/null; then
  echo "❌ Docker não está rodando."
  exit 1
fi

mkdir -p "$DESTINO"

# Coleta de imagens
IMAGENS=()

if [ "$MODO" = "all" ]; then
  echo "📂 Processando TODAS as imagens da pasta..."
  mapfile -t IMAGENS < <(
    ls *.png *.jpg *.jpeg *.webp 2>/dev/null
  )
else
  IMG=$(ls *.png *.jpg *.jpeg *.webp 2>/dev/null | \
        fzf --height=40% --layout=reverse --border)

  [ -z "$IMG" ] && echo "❌ Nenhuma imagem selecionada." && exit 1
  IMAGENS=("$IMG")
fi

[ "${#IMAGENS[@]}" -eq 0 ] && echo "❌ Nenhuma imagem encontrada." && exit 1

# Processamento
for IMG in "${IMAGENS[@]}"; do
  echo "🖼️ Removendo fundo: $IMG"

  OUTPUT="$DESTINO/${IMG%.*}_nobg.png"

  docker run --rm \
    -v "$(pwd):/app" \
    danielgatis/rembg:latest \
    i "/app/$IMG" "/app/$OUTPUT"

  if [ -f "$OUTPUT" ]; then
    echo "✅ Gerado: $OUTPUT"
  else
    echo "❌ Falha ao processar: $IMG"
  fi
done

echo "🎉 Todas as imagens processadas."

```
