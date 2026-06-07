---
title: install node pnpm dev
tags:
  - install
dateCreated: "[[2026-05-06]]"
---

```
#!/usr/bin/env bash
set -euo pipefail

# ==========================================================
# Instalação completa:
# - dependências básicas
# - NVM
# - Node.js LTS
# - npm
# - Corepack
# - pnpm
# ==========================================================

NVM_VERSION="v0.40.4"

echo "==> Atualizando pacotes do sistema..."
sudo apt update

echo "==> Instalando dependências básicas..."
sudo apt install -y curl ca-certificates git build-essential

echo "==> Verificando instalação do NVM..."

export NVM_DIR="$HOME/.nvm"

if [ ! -d "$NVM_DIR" ]; then
    echo "==> Instalando NVM $NVM_VERSION..."
    curl -o- "https://raw.githubusercontent.com/nvm-sh/nvm/$NVM_VERSION/install.sh" | bash
else
    echo "==> NVM já existe em $NVM_DIR"
fi

echo "==> Carregando NVM na sessão atual..."

export NVM_DIR="$HOME/.nvm"

if [ -s "$NVM_DIR/nvm.sh" ]; then
    # shellcheck disable=SC1091
    . "$NVM_DIR/nvm.sh"
else
    echo "ERRO: nvm.sh não encontrado em $NVM_DIR"
    exit 1
fi

if [ -s "$NVM_DIR/bash_completion" ]; then
    # shellcheck disable=SC1091
    . "$NVM_DIR/bash_completion"
fi

echo "==> Instalando Node.js LTS..."
nvm install --lts

echo "==> Usando Node.js LTS..."
nvm use --lts

echo "==> Definindo Node.js LTS como padrão..."
nvm alias default 'lts/*'

echo "==> Versões instaladas:"
echo "Node: $(node -v)"
echo "npm:  $(npm -v)"

echo "==> Instalando Corepack atualizado..."
npm install --global corepack@latest

echo "==> Ativando Corepack..."
corepack enable

echo "==> Instalando/ativando pnpm..."
corepack prepare pnpm@latest --activate

echo "==> Verificando pnpm..."
pnpm -v

echo ""
echo "=========================================================="
echo "INSTALAÇÃO CONCLUÍDA"
echo "=========================================================="
echo "Node: $(node -v)"
echo "npm:  $(npm -v)"
echo "pnpm: $(pnpm -v)"
echo ""
echo "Agora entre na pasta do projeto e rode:"
echo ""
echo "  cd ~/Documentos/Github/NOME-DO-PROJETO"
echo "  pnpm install"
echo ""
echo "Se o terminal atual não reconhecer node/pnpm depois disso, rode:"
echo ""
echo "  source ~/.bashrc"
echo ""
```
