---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
# Padrões para Notas de Pessoas

`peopleType`: Agrupa pessoas em grandes blocos  
`peopleDomain`: Segmenta em blocos menores, mas ainda amplos  
`peopleGroups`: Cria agrupamentos personalizados

> [!contact]- 4 tipos de pessoas  
> - fictício  
> - rede  
> - notável  
> - proeminente

> [!contact]- 10 domínios de pessoas  
> 1. Artes  
> 2. Negócios  
> 3. Humanidades  
> 4. Política  
> 5. Ciência & Tecnologia  
> 6. Espiritualidade  
> 7. Esportes  
> 8. Guerra  
> 9. Figura Pública  
> 10. Outro  

Campos adicionais possíveis:  
- `lifespan`: Ex.: 1954 - 2006  
- `finalAge`: Ex.: 52  
- `culturalEra`: Ex.: "Período Romântico" (Mary Shelley)  
- `culturalWorks`: Ex.: "Frankenstein"

#### ROAR: Acompanhar Contatos e Respostas

ROAR = "Reach-Outs And Replies".  
Propriedades:  
- `ROAR`: reach-out; reply; waiting  
- `ROARrank`: 1-5  
- `ROARdetails`: resumo em uma frase  

Funciona melhor para pessoas com quem você não fala diariamente.

---

# Padrões para Notas de Ideias

A classificação de ideias quase sempre falha. Ideias devem ser livres, não engessadas.  

- Evite `ideaCategory`.  
- `ideaGroup` só funciona se for **pessoal** (ex.: "top concepts").  
- Melhor solução: usar **pastas e tags**.

---

# Padrões para Notas de Mídia

Propriedades comuns:  
- `yearXP`: Ano em que foi experienciado pela primeira vez  
- `yearXPL`: Ano em que foi experienciado pela última vez  

---

# Padrões para Notas de Saída

Outputs são complexos por envolverem diferentes estados e mídias.  

Exemplo:  
- `outputMedium`: YouTube, Newsletter  
- `outputMediumStatus`: andamento, publicado, arquivado  

O desafio é não criar infinitas propriedades redundantes.  

---

![[Sistema de Classificação para Gestão de Conhecimento Pessoal]]