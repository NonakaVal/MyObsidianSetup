---
title: Jekyll install debian
id: 26
---

```
# 1. Instalar dependências do sistema
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev

# 2. Configurar o caminho das Gems no seu .bashrc (para evitar usar sudo no gem install)
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 3. Instalar Jekyll e Bundler
gem install jekyll bundler
```
