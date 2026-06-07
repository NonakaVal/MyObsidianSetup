---
tags:
  - calendar/week
  - content
  - <% tp.system.suggester(item => item, Object.keys(tp.app.metadataCache.getTags()).map(x => x.replace("#", "")))%>
dateCreated: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
status: idea
summary:<% tp.system.prompt("summary")%>
---

<%*

// Get all folders

const items = tp.app.vault.getAllLoadedFiles().filter(x => x instanceof tp.obsidian.TFolder);

// Prompt user to select folder

const selectedItem = (await tp.system.suggester((item) => item.path, items)).path;

// Move current file to be in selected folder

if (selectedItem) {

await tp.file.move(`${selectedItem}/${tp.file.title}`);

}

-%>

# TEMPLATE PRINCIPAL — PRODUÇÃO DE CONTEÚDO

---

## _1) Antes de Ligar a Câmera (Estratégia)_

### Tipo de Conteúdo
- [ ] **Autoridade** (Evergreen)
- [ ] **Engajamento** (Stories / Reels)
- [ ] **Blindagem de Prestígio** (NFS)
- [ ] **Conversão** (Leilão / Oferta)

### Item Central
- **Nome do item:** ______________________________________
- **Categoria:**
  - [ ] Console
  - [ ] Figura
  - [ ] Edição Especial
  - [ ] Documento

### Mensagem Principal (1 frase obrigatória)
> “Este conteúdo existe para provar que ______________________________________________.”

### Gatilho Dominante
- [ ] Autoridade técnica
- [ ] Escassez
- [ ] Exclusividade
- [ ] Educação de mercado

### Resultado Esperado
> O público deve sair entendendo: ______________________________________________.

---

## _2) Decisão de Cenário e Iluminação_

### Complexidade do Item
- [ ] **Alta** (reflexivo, muitos detalhes)
- [ ] **Média**
- [ ] **Baixa**

### Decisão Automática de Cenário
- **Se Alta** → Balcão Branco + Fundo Limpo  
- **Se Média** → Balcão + Nichos Cinza  
- **Se Baixa** → Vitrine ou Prateleira de Acervo  

### Iluminação Obrigatória
- **Key Light:** Difusa, frontal
- **Separação cromática:** (Vermelho / Azul / Nenhuma)
- **Spot IRC Alto:**
  - [ ] Sim
  - [ ] Não

### Elementos de Identidade Visíveis
- [ ] Linha Vermelha de Horizonte
- [ ] Kanji **武**
- [ ] Logo Retroiluminado

> **Regra:** Se **2 desses 3** não aparecem → cenário incompleto.

---

## _3) Estrutura de Vídeo (Roteiro)_

### Ato 1 — O Chamado (5–8s)
**Tipo de close:**
- [ ] Macro
- [ ] Detalhe
- [ ] Textura

**O que precisa ficar óbvio sem falar?**  
> ____________________________________________________________

---

### Ato 2 — A Curadoria (20–40s)
**Movimento de câmera:**
- [ ] Pan
- [ ] Tilt
- [ ] Estático técnico

**Elemento de autoridade no frame:**
- [ ] Branding
- [ ] Acervo ao fundo
- [ ] Ferramenta técnica

---

### Ato 3 — Encerramento (5–10s)
**Onde a câmera termina?**  
> ____________________________________________________________

**O público deve sentir:**
- [ ] Confiança
- [ ] Desejo
- [ ] Respeito
- [ ] Urgência

---

## _4) Verificação Final (Antes de Gravar)_
- [ ] Mensagem principal definida
- [ ] Cenário condizente com a complexidade
- [ ] 2+ elementos de identidade visíveis
- [ ] Iluminação correta
- [ ] Encerramento planejado
