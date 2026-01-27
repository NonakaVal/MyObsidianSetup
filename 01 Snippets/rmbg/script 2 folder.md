---
title: script 2 folder
id: 7
---

```
#!/bin/bash

PASTA="${1:-.}"
MODO="${2:-confirmar}"

EXTENSOES="png jpg jpeg webp"

echo "🧹 Limpeza de imagens"
echo "📂 Pasta alvo: $PASTA"
echo "⚙️  Modo: $MODO"
echo

if [ ! -d "$PASTA" ]; then
  echo "❌ Pasta não encontrada."
  exit 1
fi

# Monta o find
FIND_CMD=(find "$PASTA" -type f \( )
FIRST=true
for ext in $EXTENSOES; do
  if [ "$FIRST" = true ]; then
    FIRST=false
  else
    FIND_CMD+=(-o)
  fi
  FIND_CMD+=(-iname "*.$ext")
done
FIND_CMD+=( \) )

if [ "$MODO" = "listar" ]; then
  echo "📋 Arquivos que seriam apagados:"
  "${FIND_CMD[@]}"
  exit 0
fi

if [ "$MODO" = "confirmar" ]; then
  echo "⚠️ Confirmação individual ativada"
  "${FIND_CMD[@]}" -ok rm {} \;
  exit 0
fi

if [ "$MODO" = "forcar" ]; then
  echo "🔥 Apagando todas as imagens sem confirmação"
  "${FIND_CMD[@]}" -delete
  exit 0
fi

echo "❌ Modo inválido."
echo "Use: listar | confirmar | forcar"
exit 1

```
