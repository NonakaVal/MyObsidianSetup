---
tags:
status: approved
summary: Por Que Usar Obsidian - Visão Geral do Meu Setup
rank: 8
chance: 7
cssclasses:
  - imagegallery
area:
  - "[[Val Channel]]"
subject:
  - "[[hub-work]]"
  - "[[hub-pkm]]"
---
# Prints de apresentação

![[readme.png]]

![[PRINT1.png]]
![[between notes apresentation.png]]
![[aprr.png]]

![[between notes apresentation3.png]]
![[between notes apresentation3-1.png]]

## Roteiro: Por Que Usar Obsidian - Visão Geral do Meu Setup

# 🎬 **Timestamps Recomendados**s

```
00:00 - Introdução
02:30 - Conceitos Fundamentais
09:00 - Tour pela Estrutura
19:00 - Templates Essenciais
27:00 - Dataview & Automações
34:00 - Sistema de Tags
39:00 - Fluxo de Trabalho
47:00 - Plugins
52:00 - Personalização
58:00 - Casos de Uso
65:00 - Próximos Passos
```

---

### 📖 **Introdução**
Pela maior parte da nossa história o mero acesso a informação foi um privilégio que garantia aos poucos detentores da mesma uma vantagem absoluta sobre as outras, das quais mesmo quando conseguiam acesso aos livros ainda não podiam entender ou questionar seu conhecimento, afinal alfabetização também era pra poucos. O que torna a escassez de conhecimento e a informação um dos problemas mais longevos da humanidade. Entretanto nas últimas décadas passamos a ter outro problema. Não mais é a falta de informação... é o **EXCESSO dela**.

### 🎯 **Definição simples**
A **Gestão do Conhecimento** busca coletar, organizar, conectar e aplicar informações para transformá-las em conhecimento útil.

![[fundamentals.png]]
![[bran.png]]
![[overload info.jpg]]

## 🎯 **Boas-vindas e Contexto**

Seja muito bem vindo, hoje eu decidi enfim trazer um vídeo muito pedido por alguns de vcs que no caso é um overview geral do meu obsidian, minhas configurações, plugins e workflow no geral.. e decidi fazer um pouco mais que isso... alguns de vcs já devem saber mas eu tenho um repositório lá no github com meu setup completo, com vários exemplos de notas pessoais no meu campo de estudo, e também um segundo repositório que postei mais recentemente lá no reddit sendo uma vault configurada pra uso e com estudos de pkm, e é essa vault que vou tá apresentando hj desde como vcs podem baixar até explicar o uso. 


**⚠️ Aviso Importante:** Se tu nunca usou obsidian eu definitivamente não recomendo que use modelos pré prontos. Uma das coisas mais belas do obsidian está na simplicidade, vou deixar algumas ótimas discussões aqui sobre o porque usar obsidian sem sequer ativar os plugins da comunidade, e o por que usar com e na minha opinião e com mais de 2 anos de uso, ao menos no começo com nossas primeiras notas, devemos usar da forma mais simples possível, focar em nada além da escrita e revisão. Se naturalizar com o sistema de links e propriedades, além é claro das notas diárias.. então a partir disso, quando entendemos como necessário expandir nosso controle sobre o que estudamos, de fato buscamos aprender conceitos além disso, mensagem dada agora vamos começar a entender alguns conceitos.

---

# Entendendo o básico


![[arc-ilustration.png]]




[[Markdown]]


---
## Propriedades

### 📄 **Propriedades Essenciais**


```yaml
---
created: [[2025-08-19]]
up: [[Projeto X]]
collection: [[Estudos]]
related: [[Ideia A]], [[Pessoa B]]
---
````

Esses metadados funcionam como **camadas de contexto**, ajudando a:
- Organizar e estruturar suas notas
- Navegar entre hierarquias e conexões
- Automatizar consultas com **Dataview** ou **DataviewJS**
### 🔑 Principais Metadados

- **`created` → Data de criação**  
    Acompanha a linha do tempo das anotações e permite gerar históricos, revisões mensais ou anuais.
    > Ex.: `created: [[2025-08-19]]`
- **`up` → Hierarquia**  
    Define a **nota superior** ou o contexto maior em que a nota se insere.
    > Ex.: um capítulo teria `up: [[Livro X]]`.
- **`collection` → Coleções**  
    Agrupa notas em **temas ou áreas específicas**.
    > Ex.: `collection: [[AULAS]], [[CURSOS]]`
- **`related` → Conexões manuais**  
    Lista notas relacionadas, ampliando o **Graph View** com links explícitos.
    > Ex.: `related: [[Conceito Y]], [[Questão Z]]`

---


### ⚙️ Tags do Sistema
- `#calendar/daily`: Notas diárias
- `#calendar/weekly`: Notas semanais
- `#task`: Tarefas
- `#project/*`: Projetos
- `#area/*`: Áreas



## Fluxo de notetaking


como comecei explicar no meu vídeo 
[[2024-12-29-aceXpara-method-video]]


![[capture-calendar-ilustration.png]]
![[3tiposdenotas.png]]
### 🔄 **Sistema ACE**

[[forum.obsidian]]/t/the-ultimate-folder-system-a-quixotic-journey-to-ace/63483) e se organiza em três áreas principais

![[arc-maid.png]]
![[ace-table-principles.png]]
### 🎯 **Framework ARC**
ARC define o fluxo das suas ideias pelo tempo e espaço, muito além disso. Esse é um framework que amplia seu processo criativo.

![[arc-flow 1.png]]
![[arc-flow-2.png]]


**Ciclo**: Novas ideias → Organização natural → Aplicação concreta = Sistema autossustentável de aprendizado.


- **[[Adicionar]]**  
  - Pasta `+` como "área de resfriamento" para ideias novas  
  - Processo: espere → reformule → conecte → mova para pasta definitiva  
- **[[Relacionar]]**  
  - Foco em conexões orgânicas e desenvolvimento natural do pensamento  
- **[[Comunicar]]**  
  - Compartilhe (trabalho, redes, e-mail próprio) para dar propósito ao conhecimento  



---



# 🏠 **TOUR PELA ESTRUTURA**

![[folders.png]]

### 🏠 **Página Inicial (🏠.md)**
- Demonstração dos botões de ação rápida
- Dashboard com visão geral
- Como navegar pelo vault

![[homepage2.png]]
![[recent-created.png]]
![[dashboard++.png]]
![[grid.png]]
![[tracker.png]]

### ➕ **Pasta + (Quick Capture)**
- Para que serve
- Como usar para captura rápida
- Quando mover para local definitivo



### 🗺️ **Pasta ATLAS**
- **Conceitos**: Para ideias e aprendizados
- **Mapas (MOCs)**: Como organizar conhecimento por temas
- Demonstração: Como criar e linkar conceitos
- Sistema de tags Garden/Architect

### 📅 **Pasta CALENDAR & REVIEW**

![[capture-calendar-ilustration.png]]

- **Daily Notes**: Template de nota diária
- **Weekly Notes**: Revisão semanal com mood tracker
- **Monthly Notes**: Visão mensal com gráficos
- Como usar as propriedades de humor

### 🎯 **Pasta PROJECTS & AREAS**

![[projects-vs-area-ilustration.png]]

- Diferença entre Projetos (temporário) e Áreas (contínuo)
- Template de projeto com meta-bind
- Template de área
- Como criar notas relacionadas


### ⚙️ **Pasta System**
- Assets
- Mídia 
- Templates

---

## 📝 **TEMPLATES + Quick Add**

### 📋 **Templates de Formato**
- **Daily Note**: Estrutura completa
- **New Note**: Nota básica com tags garden
- **Project**: Gerenciamento de projetos
- **Area**: Gestão de áreas de responsabilidade

### 📓 **Templates de Journal**
- **Morning**: Gratidão e prioridades
- **Evening**: Reflexão do dia
- **Mood Tracker**: Acompanhamento emocional
- **Reading**: Registro de leituras

### 🛠️ **Snippets Úteis**
- Botões com Meta-Bind
- Dataview queries prontos
- Inserção de imagens
- Links e referências




---

## 📊 **Assets**

### 🔍 **Queries Prontas para Usar**
- `@_modified`: Últimas notas modificadas
- `@_created`: Notas recentes
- `@_projects`: Visão de projetos
- `@_areas`: Áreas ativas
- `@_collections`: Coleções temáticas

##### 🌱 Garden Tags (Jardineiro)

!e[[jarden-vs-archtect.png]]

- 🌱 `#garden/plant`: Ideias para desenvolver
- ☘️ `#garden/cultivate`: Notas precisando profundidade
- 🍄 `#garden/question`: Questões abertas
- 🪴 `#garden/repot`: Reorganizar
- 💦 `#garden/revitalize`: Reativar
- 🍁 `#garden/revisit`: Revisar

##### 🏗️ Architect Tags (Arquiteto)
- 🧱 `#architect/build`: Criar estruturas
- 🪜 `#architect/renovate`: Atualizar mapas



- Coleções, hubs ou Category 
- Boas práticas de classificação





## 🔌 **Plugins da comunidade**

### 📈 **Mood Tracker Automático**
- Como funciona
- Gráficos gerados
- Análise de tendências

### ⏱️ **Pomodoro & Time Tracking**
- Integração com TaskNotes
- Relatórios de produtividade
- Logs de trabalho

### 🎛️ **Como usar Meta-Bind**
- Botões de ação
- Inputs dinâmicos
- Status de projetos
- Datas de entrega

---

## 🔄 **FLUXO DE TRABALHO PRÁTICO** (6-8 min)

### 📅 **Dia a Dia Recomendado**
1. **Manhã**: Abrir daily note, definir humor e prioridades
2. **Durante o dia**: Captura rápida na pasta +
3. **Tarde**: Processar notas, adicionar tags, criar links
4. **Noite**: Reflexão e registro de logs

### 💡 **Captura de Ideias**
- Demonstração real de captura rápida
- Como processar depois
- Quando criar um conceito vs quando linkar

### 📂 **Gestão de Projetos**
- Criar novo projeto
- Adicionar tarefas
- Acompanhar progresso
- Arquivar quando concluído

### 🔍 **Revisão Periódica**
- Semanal: Mood tracker + logs
- Mensal: Análise de produtividade
- Como usar os relatórios automáticos

---

## 🔌 **PLUGINS RECOMENDADOS** (4-5 min)

### ⭐ **Essenciais Já Configurados**
- **Dataview**: Queries e tabelas dinâmicas
- **Templater**: Sistema de templates
- **Meta-Bind**: Botões e inputs interativos
- **TaskNotes**: Gestão de tarefas e pomodoro
- **Calendar**: Visualização de daily notes
- **Periodic Notes**: Weekly e monthly notes

### ⚙️ **Configurações Importantes**
- Como estão configurados
- O que cada um faz
- Onde ajustar se necessário

---

## 🎨 **PERSONALIZAÇÃO** (4-5 min)

### 🔧 **Adaptando ao Seu Uso**
- Como modificar templates
- Adicionar suas próprias categorias
- Criar novos snippets
- Ajustar dataview queries

### 🎨 **CSS Snippets Incluídos**
- Dashboard++
- Multi-column
- Callouts personalizados
- Banner de imagens

### 🖼️ **Temas e Aparência**
- Theme "Things" pré-configurado
- Como trocar de tema
- Ajustar tamanho da fonte

---



## ❓ **TROUBLESHOOTING & FAQ** (3-4 min)

### 🛠️ **Problemas Comuns**
- Plugins não carregam
- Dataview não funciona
- Templates não aparecem
- Meta-Bind não responde

### ⚡ **Dicas de Performance**
- Limite de notas
- Otimização de queries
- Backup recomendado

---





### 🙏 **Agradecimentos**
- Créditos e inspirações
- Comunidade PKM
- Nick Milo (LYT)
- Outros criadores

---

## 🔗 **Links na Descrição**

- 📥 Download do Vault
- 📚 Documentação Completa
- 🔗 GitHub Repository
- 💬 Comunidade
- 🎓 Curso Completo (se houver)
- ☕ Apoiar o Projeto

https://github.com/DuskWasHere/dusk-obsidian-vault
https://fortelabs.com/blog/para/


https://medium.com/obsidian-observer/ace-an-exciting-framework-for-pkm-bc3fbbc5665b
[[forum.obsidian]]/t/the-ultimate-folder-system-a-quixotic-journey-to-ace/63483

https://youtube.com/watch?v=lqrzxfZD_hc


https://github.com/DuskWasHere/dusk-obsidian-vault
https://fortelabs.com/blog/para/


