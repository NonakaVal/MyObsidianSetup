---
tags:
  - learning
HUB:
  - "[[hub-git]]"
  - "[[hub-tec]]"
---
>[!verifica versão]
```css
git -- version 
```

>[!inicia um repositório vazio]
```css
git init
```

>[!manda arquivos para stading]
```css
git add {nome arquivo} ou  .
```

>[!display the state of the working]
```css
git status
```

>[!commits the changes staged]
```css
git commit -m {'mensagem'}
```

>[!criar conexãodo git para o repo no github {mesmo nome}]
```css
git remote add origin {link repo} 
```

>[!Envia os commits para o repositório no GitHub]
```css
git push -u origin main
```

---

>[!Criar e Mudar para um Novo Branch]
```css
git chackout -b 'novo-botão'
```

>[!volta para o branch que você estava antes do último comando]
```css
git checkout -
```


```css
git commit -m 'novo botao'
git push origin novo-botao
```

>[!combinar alterações de diferentes branches]
```css
git merge novo-botao
```

>[!atualiza seu branch local]
```css
git pull
```

