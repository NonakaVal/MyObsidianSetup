---
tags:
  - roteiro
status: revised
dateCreated: "[[2026-06-04]]"
dateRevised: "[[2026-06-04]]"
pipeline: standard
---

# Roteiro — Tudo sobre Bases: o Dataview nativo do Obsidian

## Regras de Escrita

- Escrever como se fala — não como texto formal
- Ler em voz alta antes de gravar — obrigatório
- Qualquer frase que travar → reescrever
- Cada bloco gravável de forma independente
- Notas de direção restritas a elementos visuais de tela
- Pausas com `[PAUSA Xs]`
- Marcas de edição inline: `[BROLL: ...]`, `[TEXTO: ...]`, `[ZOOM: ...]`, `[CORTE]`

---

## 0 — Setup

- img _preparação técnica_
	- Obsidian aberto com vault de demonstração (tema dark mode, sidebar com pastas visíveis)
	- Plugin Bases habilitado em Settings → Core Plugins
	- Vault de demo com pelo menos 30 notas variadas (livros, notas de estudo, templates, notas órfãs)
	- Propriedades já preenchidas em várias notas (tags, tipo, status, autor, data)
	- Resolução de gravação: 1920×1080, área de escrita centralizada
	- Desabilitar plugins de barra lateral que não sejam nativos pra manter a interface limpa

- sec _setup_ preparacao
	- rec _Não narrável. Apenas referência de preparação da tela._

- dur _N/A_

---

## 1 — Gancho

- img _notas de edição_
	- `[BROLL: tela do Obsidian com uma view de Bases em cards com thumbnails de livros]` — abertura imediata
	- `[TEXTO: "BASES"]` — ao mencionar o nome do plugin
	- `[ZOOM: suave na view de cards]` — durante "visualizar do jeito que faz sentido"
	- Musica: sem música. Silêncio limpo pra entrar direto com a voz.

- sec _narração_ gancho
	- rec _Se tu usa Obsidian e ainda organiza tudo por pastas — tu tá trabalhando demais._
	- rec _O plugin nativo Bases é basicamente o Dataview sem dor de cabeça. Hoje eu vou mostrar como ele funciona, com os meus usos reais._

- dur _12 seg_

---

## 2 — Contexto / Problema

- img _notas de edição_
	- `[BROLL: tela de Settings → Core Plugins com Bases marcado]` — ao mencionar "nativo"
	- `[TEXTO: "Dataview vs Bases"]` — durante a comparação
	- `[BROLL: print do Discord/Reddit com gente reclamando de lentidão]` — durante "se teu Obsidian trava muito"
	- `[ZOOM: na lista de plugins community instalados]` — ao falar de plugins comendo RAM
	- Musica: lo-fi baixinho, volume 15%, ambiente

- sec _narração_ contexto
	- rec _Bases é o plugin nativo mais recente do Obsidian. Nativo — vem com o app. Tu habilita em Settings e pronto._
	- rec _Na prática, é a resposta oficial ao Dataview — um dos plugins comunitários mais famosos que existem._
	- rec _Mas aqui vai algo que ninguém te conta. [PAUSA 1s] Se teu Obsidian tá travando demais, provavelmente não é o app. É algum plugin da comunidade comendo tua RAM inteira._
	- rec _Plugins nativos são otimizados pra arquivos locais simples. Isso faz diferença quando tu tem centenas ou milhares de notas._
	- rec _Então, antes de mais nada — se teu Obsidian anda lento, abre a lista de plugins. Desabilita um por um e vê qual é o culpado._
	- rec _[PAUSA 2s] Dito isso, vamos pro que interessa._
	- rec _O Bases te permite visualizar tuas notas em tabelas, cards, listas — várias opções de views._
	- rec _A ideia é simples: em vez de organizar nota por nota, pasta por pasta, tu cria views que filtram e agrupam automaticamente com base nas propriedades._
	- rec _E aqui a palavra "base" não é coincidência. [PAUSA 1s] O que faz o Bases funcionar são as propriedades — aqueles campos de frontmatter no topo de cada nota. Tipo, status, tags, data._
	- rec _Sem propriedades, o Bases não tem nada pra filtrar. É como tentar fazer uma busca sem ter preenchido os dados._

- dur _2 min_

---

## 3 — Núcleo / Desenvolvimento

- img _notas de edição_
	- `[BROLL: abrir uma nota com propriedades preenchidas — mostrar o frontmatter]` — ao falar de propriedades
	- `[ZOOM: no bloco de propriedades no topo da nota]` — durante "como tu organiza"
	- `[BROLL: criar/abrir uma nota de convenções no vault]` — ao mencionar "nota de convenções"
	- `[TEXTO: "Convenções da Vault"]` — ao mostrar a nota de convenções
	- `[CORTE]` — transição para o primeiro caso de uso
	- `[BROLL: view de Bases configurada para livros — tabela com colunas: título, autor, status, nota]` — durante "Livros"
	- `[ZOOM: na configuração da view de livros — mostrar filtros e agrupamentos]` — durante a explicação
	- `[BROLL: view de cards com thumbnails de capas de livros]` — durante "Boards com thumbs"
	- `[ZOOM: no card mostrando a imagem de capa]` — ao mencionar thumbnails
	- `[BROLL: view de mídia — galeria com imagens e vídeos embutidos]` — durante "View de mídia"
	- `[BROLL: view do tipo Knowledge — graph ou lista de notas conectadas por tags/links]` — durante "Knowledge"
	- Musica: lo-fi, volume 15%, mesma faixa do bloco anterior — continuidade

- sec _narração_ nucleo
	- rec _Antes de mostrar os casos de uso, uma dica que salva vidas._
	- rec _Cria uma nota chamada "Convenções". Ali tu anota como tu nomeia as coisas — se tu usa "status" ou "estado", se a tag é "#livro" ou "#livros", se a data é "YYYY-MM-DD" ou "DD/MM/YYYY"._
	- rec _O nome não importa tanto quanto a consistência. [PAUSA 1s] Se tu tem três propriedades que significam a mesma coisa — "tag", "tags", "categoria" — o Bases trata como três coisas diferentes._
	- rec _E se tu já tem uma bagunça nas propriedades, relaxa. O próprio Bases te permite renomear e unificar tudo. Tu define o padrão e ajusta as notas que estão fora dele._
	- rec _[PAUSA 1s] Beleza. Agora vamos pro que interessa._
	- rec _Eu não vou listar todas as funções uma por uma — pra isso existe a documentação oficial. Vou mostrar os meus usos reais, e a gente vai montar alguns juntos._
	- rec _Primeiro caso: livros. [PAUSA 1s] Eu leio bastante, e toda nota de livro tem as mesmas propriedades — autor, status, nota de avaliação, gênero._
	- rec _No Bases eu criei uma view de tabela que filtra tudo que tem tipo "livro" e organiza por status: "lendo", "lido", "quero ler". [PAUSA 1s] É uma estante virtual que se atualiza sozinha._
	- rec _Segundo caso: Boards com thumbnails. [PAUSA 1s] Esse é um dos meus favoritos. Em vez de tabela, eu uso a view de cards, e cada card mostra a capa do livro._
	- rec _Fica visual, fica bonito. Tu encontra o que precisa muito mais rápido do que lendo linha por linha. [PAUSA 1s] Funciona pra qualquer coisa que tenha imagem — jogos, filmes, cursos._
	- rec _Terceiro caso: View de mídia. [PAUSA 1s] Pra quando tu tem notas com imagens ou vídeos embutidos — capturas de tela, referências visuais, clippings com figuras._
	- rec _A view de mídia mostra tudo como galeria. Tu vê a imagem direto, sem abrir a nota. Pra quem trabalha com referência visual, isso é ouro._
	- rec _Quarto caso: Knowledge. [PAUSA 1s] Uma view que agrupa notas por tags e mostra os backlinks entre elas._
	- rec _Não é o Graph View — é mais focado. Tu vê quais conceitos se conectam, quais notas estão isoladas, quais tu precisa revisitar. É um mapa da tua base de conhecimento, só que filtrável._

- dur _6 min_

---

## 4 — Aprofundamento / Prova

- img _notas de edição_
	- `[BROLL: view de Bases filtrada por notas sem backlinks e sem tags]` — durante "Notas órfãs"
	- `[ZOOM: no filtro mostrando "empty backlinks" e "empty tags"]` — ao explicar como encontrar órfãs
	- `[BROLL: view de Recents — notas modificadas nos últimos 7 dias em lista]` — durante "Recents"
	- `[BROLL: view de Youtube — tabela com canal, título, data, tags de vídeo]` — durante "Youtube"
	- `[ZOOM: nas propriedades específicas de notas de vídeo — canal, duração, assistido]` — ao detalhar os campos
	- `[BROLL: view de Templates — lista filtrada por tipo "template" com preview do conteúdo]` — durante "Templates"
	- `[CORTE]` — transição para a construção ao vivo
	- `[BROLL: construção ao vivo de uma view de livros passo a passo — criar nova view, adicionar filtros, escolher layout de cards, adicionar colunas]` — durante "vamos montar junto"
	- `[ZOOM: em cada passo do processo — settings da view, seção de filtros, seção de layout]` — conforme explica cada etapa
	- Musica: lo-fi, volume 10%, mais suave — foco total na demonstração

- sec _narração_ aprofundamento
	- rec _Agora os casos mais específicos — e mais úteis se tu já tem uma vault com bastante coisa._
	- rec _Quinto caso: Notas órfãs. [PAUSA 1s] Toda vault com mais de cem notas tem. Aquelas sem backlink, sem tag, sem conexão com nada. Notas perdidas._
	- rec _No Bases eu criei uma view que filtra notas com backlinks vazio e tags vazio. [PAUSA 1s] Pronto — ali está o cemitério da tua vault._
	- rec _Aí tu decide: conecta essas notas com o resto do conhecimento, ou arquiva. Mas pelo menos tu sabe que elas existem._
	- rec _Sexto caso: Recents. [PAUSA 1s] Simples e direto. Uma view com as últimas notas modificadas — eu configuro pra 7 dias._
	- rec _É tipo o "recentemente modificados" de qualquer app, só que dentro do Obsidian e customizável. Eu uso como landing page da vault._
	- rec _Sétimo caso: Youtube. [PAUSA 1s] Eu salvo vídeos do Youtube como notas — cada uma com canal, título, data e tags do conteúdo._
	- rec _No Bases eu tenho uma view que filtra por canal e por tag. [PAUSA 1s] Se eu quero revisitar tudo que o Nick Milo falou sobre Atomic Notes — está ali. Meu banco de referências de vídeo._
	- rec _Oitavo caso: Templates. [PAUSA 1s] Uma view que lista todos os meus templates, filtrados pelo tipo "template", mostrando a estrutura de cada um._
	- rec _Quando eu preciso criar um template novo, eu olho essa view primeiro. Pra não reinventar a roda._
	- rec _[PAUSA 2s] E antes de te mandar embora, vamos montar uma view juntos._
	- rec _Supondo que tu tem notas de livros com propriedades preenchidas. Abre o Bases, cria uma nova view._
	- rec _Primeiro: escolhe o layout. Vamos de cards. [PAUSA 1s] Segundo: adiciona o filtro — tipo é igual a "livro"._
	- rec _Terceiro: escolhe as propriedades que aparecem no card — título, autor, status. [PAUSA 1s] Quarto: se tu tem imagem de capa, habilita como thumbnail._
	- rec _Salva. [PAUSA 1s] Pronto. Em trinta segundos tu tem uma estante virtual que se atualiza sozinha toda vez que tu adiciona um livro novo._

- dur _4 min_

---

## 5 — Conclusão / CTA

- img _notas de edição_
	- `[BROLL: visão geral da vault com várias views de Bases abertas na sidebar]` — durante o resumo
	- `[TEXTO: "Plugin Bases — Obsidian"]` — ao mencionar a documentação
	- `[TEXTO: "Inscreve + Like"]` — durante o CTA
	- Musica: lo-fi, volume 20%, encerramento suave

- sec _narração_ conclusao
	- rec _Então é isso. [PAUSA 1s] O Bases é o jeito nativo de transformar tua vault de "pasta cheia de arquivos" em algo que tu consegue consultar, filtrar e visualizar sem abrir nota por nota._
	- rec _A única exigência: propriedades preenchidas. Sem isso, não tem mágica._
	- rec _Pra saber mais sobre as opções de view, filtros e agrupamentos, a documentação oficial do Obsidian cobre tudo. Link na descrição._
	- rec _Se esse vídeo te ajudou, se inscreve e deixa o like. Ajuda o canal e me motiva a continuar. [PAUSA 1s] Até a próxima._

- dur _40 seg_

---

## Checklist Pós-Gravação

- [ ] Todos os blocos gravados?
- [ ] B-roll necessário gravado? (8 views de Bases, construção ao vivo, props)
- [ ] Arquivos transferidos para assets/gravacao/?
- [ ] Verificar se todas as views de demonstração estão funcionando antes de gravar
- [ ] Conferir se as propriedades nas notas de demo estão consistentes (nota de convenções)
