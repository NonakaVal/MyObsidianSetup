---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---

Com o surgimento das [[Propriedades]] (basicamente uma forma adequada de gerenciar metadados), é mais importante do que nunca oferecer uma coleção sugerida de boas práticas e padrões para tipos específicos de notas. Alguns nerds podem chamar isso de "ontologias", mas aqui usaremos o termo "padrões". Lembre-se de que estes não estão gravados em pedra. São uma lista curada de boas práticas. Algumas surgiram através de uso intenso; outras são pequenos testes que ainda precisam ser validados. A contribuição da comunidade global continuará moldando os **Padrões de Classificação LYT** em futuras iterações.

Você pode esperar padrões sobre:
- O [[Sistema de Classificação para Gestão de Conhecimento Pessoal]]
- Termos
- Sistema de Ranqueamento
- Tipos específicos de Coleções
- Boas Práticas para Classificação em PKM

---
# Termos

**Coleções** se referem a notas especiais que possuem "buscas salvas" (queries) que permanecem sempre atualizadas (alguns dizem "automágicas"). Elas também podem ser chamadas de "dashboards dinâmicos". Exemplos comuns incluem:

- Mapas
- Coisas, Conceitos, Pessoas
- Declarações, Perguntas, Citações
- Livros, Filmes, Séries
- Reuniões, Entidades
- Esforços
#### Visualizações

**Visualizações** referem-se a notas que têm "buscas salvas" (queries), mas abrangendo diferentes tipos de notas em seu cofre, não apenas um tipo como as coleções fazem.  

---

# Boas Práticas para Classificação em PKM

- `collectionProperty`: Uma prática emergente é fazer com que propriedades especializadas comecem com a coleção a que se relacionam.  
  Ex.: `bookGroups`, `showGroups`, `peopleGroups`.  
  - Se fosse apenas `Groups`, você teria sugestões de auto-complete cheias de ruído. Ao digitar `showGroups`, quer ver apenas sugestões relevantes como "favoritos da família" ou "adaptações".
  - Além disso, ao incluir o nome da coleção na propriedade, você não precisa memorizar todas as propriedades: basta começar a digitar "book" e terá sugestões limpas como `bookGenre`, `bookCategory` e `bookAgent`.

- Singular vs Plural: Para tags, a recomendação LYT foi manter tudo no singular. Para propriedades, ainda não há consenso.

---

 Boas Práticas para Classificação por `Type`, `Category`, `Group`, `Class`, `Genre`, `Kind`

Nem toda coleção precisa de todos os tipos de classificação. **Menos é mais** — até você ter um motivo real para expandir.

Usar templates pode automatizar metadados sem esforço, permitindo criar dashboards dinâmicos rapidamente.

- `Type` (_mais abstrato_): Diferencia no nível mais alto.  
  Ex.: `bookType`: "ficção" e "não-ficção"; `showType`: "filme", "série", "peça".
- `Category` (_mais oficial_): Classificações amplamente reconhecidas.
- `Genre` (_mais oficial nas Artes_): Classificações consensuais.  
  Ex.: `showGenre`: "Ação", "Aventura", "Drama" para O Senhor dos Anéis.
- `Groups` (_mais pessoal_): Agrupamentos que você cria, não oficiais.  
  Ex.: `showGroup`: adicionar "Sci-Fi" para gerar uma visualização dinâmica só de filmes Sci-Fi.

Resumo mental do autor:
- "`type` no topo e `group` na base."
- "Preciso de algo no meio? `category` ou `genre` faz mais sentido?"

### Outros termos

- `kind`: Muito parecido com `type`, pode gerar confusão se usado junto. Melhor para pensar em "tipos de notas": Livro, Esforço, Ideia, Reunião, Filme, Pessoas, Série.
- `class`: Também próximo de `type`, raramente usado em propriedades, mas pode ser útil em contextos avançados.

---

#   ![[Sugestões de Padrões de Classificações]]
