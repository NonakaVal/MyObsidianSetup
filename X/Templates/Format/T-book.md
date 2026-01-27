---
tags:
  - book
aliases:
  - '"{{subtitle}}"'
title: "{{title}}"
subtitle: "{{subtitle}}"
author:
  - "{{author}}"
genres:
  - "{{category}}"
publisher: "{{publisher}}"
published: "{{publishDate}}"
volume: "{{totalPage}}"
isbn: "{{isbn10}} {{isbn13}}"
cover: "{{coverUrl}}"
localCover: "{{localCoverImage}}"
status: unread
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---


%% To use an image URL from the server, use the following syntax: %%
<%* if (tp.frontmatter.cover && tp.frontmatter.cover.trim() !== "") { tR += `![cover|150](${tp.frontmatter.cover})` } %>

%% To save images locally, enable the 'Enable Cover Image Save' option in the settings and enter as follows: %%
<%* if (tp.frontmatter.localCover && tp.frontmatter.localCover.trim() !== "") { tR += `![[${tp.frontmatter.localCover}|150]]` } %>

# {{title}}



# Principais Aprendizados 📚
_Resuma os principais pontos ou lições que você aprendeu com o livro._
- 
- 
- 

# Citações Favoritas 💬
_Anote trechos ou citações que mais ressoaram com você._
- 
- 
- 

# Reflexões Pessoais ✨
_Compartilhe seus pensamentos, opiniões e como o livro o impactou._
- 

# Avaliação ⭐
_Atribua uma nota ao livro com base na sua experiência pessoal (ex.: 1–5 estrelas)._
- 

# Próximo Objetivo de Leitura 📖
_Defina uma intenção para a sua próxima jornada de leitura._
- 
