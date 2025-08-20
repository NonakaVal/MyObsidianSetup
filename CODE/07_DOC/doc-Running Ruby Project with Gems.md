---
created: "[[2025-07-08]]"
aliases:
  - rodando projeto do blog not a dev in archlinux
---

Perfeito, Val — você já fez tudo certo, mas ainda está batendo no **mesmo problema central**:

🔴 Bundler está tentando instalar as gems no **sistema (`/usr/lib/ruby/gems/...`)**, que requer permissão de root.

Esse erro só vai parar quando você mandar explicitamente para o Bundler instalar as gems **numa pasta local (do projeto ou do usuário)**.

Vou te passar a receita definitiva, já testada e limpa.

---

### ✅ Resolução

No diretório do projeto (`myblog`), rode exatamente isto, na ordem:

```bash
# manda as gems para vendor/bundle (local ao projeto)
bundle config set --local path vendor/bundle
```

Isso vai criar um arquivo `.bundle/config` com:

```yaml
BUNDLE_PATH: "vendor/bundle"
```

---

Depois:

```bash
bundle install
```

⚠️ Se ainda assim ele tentar instalar em `/usr/lib` por algum motivo (às vezes por resquício de configuração global), força o Bundler a ignorar a configuração global e só usar a local:

```bash
rm -rf ~/.bundle
bundle config set --local path vendor/bundle
bundle install
```

---

Agora deve instalar tudo em:

```
myblog/vendor/bundle
```

e não em `/usr/lib`.

---

Finalmente:

```bash
bundle exec jekyll serve
```

---

### 💡 Se ainda der erro

Se mesmo assim ele ainda tentar ir para `/usr/lib`, você pode forçar ainda mais usando a opção na linha de comando:

```bash
bundle install --path vendor/bundle
```

E se preferir instalar para seu usuário:

```bash
bundle install --path ~/.gem
```

E adiciona ao `PATH` no `.bashrc`:

```bash
export PATH="$HOME/.gem/bin:$PATH"
source ~/.bashrc
```

---

### 🚀 Sugestões para evoluir

📄 Cria um `.bundle/config` já pronto com:

```yaml
BUNDLE_PATH: "vendor/bundle"
BUNDLE_JOBS: 4
BUNDLE_RETRY: 3
```

📄 Adiciona `vendor/` no `.gitignore`.

⚙️ Ou instala um gerenciador de Ruby (`rbenv` ou `asdf`) para evitar qualquer conflito com `/usr/lib`.

🛠️ Se quiser, posso também:

- Gerar um `.bundle/config` pronto;
    
- Criar um `Makefile` com `make install` + `make serve`;
    
- Ou um `serve.sh` que faz tudo sozinho.
    

Só me dizer qual opção (ou todas) que eu já te devolvo prontinho para copiar!