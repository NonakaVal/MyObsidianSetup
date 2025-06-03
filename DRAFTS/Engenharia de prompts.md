---
type: new_note
tags:
  - new_note
  - learning
created: 2025-04-05 17:45
HUB:
  - "[[System/HUB/hub-tec]]"
  - "[[hub-prompts]]"
  - "[[hub-work]]"
share_link: https://share.note.sx/364j7fw7#ac/d8/iMHyXw9Ic9q/2Hclnh2YzlZURLup89ovOc+eE
share_updated: 2025-04-05T17:47:37-03:00
---

## Estrutura básica de prompt (P.R.O.M.P.T.)

- **Persona**: Defina a persona ou papel que o modelo deve assumir ao responder.
- **Roteiro**: Especifique o roteiro ou tarefa que o modelo deve realizar.
- **Objetivo**: Deixe claro qual é o objetivo do prompt e o que se espera alcançar.
- **Modelo**: Indique o formato ou estrutura que a resposta do modelo deve seguir.
- **Panorama**: Forneça informações contextuais relevantes para ajudar o modelo a gerar uma resposta mais precisa e específica.
- **Transformar**: Esteja preparado para refinar e iterar o prompt com base nos resultados obtidos, fornecendo feedback e exemplos adicionais se necessário.


## Processo recomendado

1. Definir a tarefa e critérios de sucesso: Determine claramente a tarefa que você deseja que o modelo realize e estabeleça critérios mensuráveis para avaliar o sucesso.
2. Desenvolver casos de teste: Crie um conjunto de casos de teste que cubram os principais cenários e casos extremos para avaliar o desempenho do prompt.
3. Projetar o prompt preliminar: Desenvolva uma primeira versão do prompt, incluindo a definição da tarefa, características de uma boa resposta e contexto relevante.
4. Testar o prompt contra os casos de teste: Avalie o desempenho do prompt usando os casos de teste desenvolvidos e registre os resultados.
5. Refinar o prompt: Com base nos resultados dos testes, refine o prompt adicionando esclarecimentos, exemplos ou restrições para melhorar o desempenho.
6. Colocar o prompt em produção: Depois de alcançar resultados satisfatórios nos testes, implemente o prompt em seu aplicativo ou fluxo de trabalho.

## Técnicas básicas

- **Markdown**: Use formatação Markdown para estruturar seus prompts, incluindo títulos (# ## ###), negrito (`*texto**`), itálico (`texto*`), listas (`item`) e blocos de código (`código`). Isso melhora a legibilidade para humanos e ajuda o modelo a entender a estrutura do prompt.
- **Delimitadores**: Utilize delimitadores como `--` ou tags XML (`<tag>conteúdo</tag>`) para separar seções do prompt, como instruções, exemplos e dados. Isso ajuda o modelo a distinguir diferentes partes do prompt.
- **Variáveis**: Ao usar plataformas como o console da Anthropic, você pode definir variáveis no prompt usando a sintaxe `{{variável}}`. Isso permite que você crie prompts genéricos que podem ser facilmente adaptados para casos específicos, substituindo apenas os valores das variáveis.
- **Prompt do sistema:** Use o prompt do sistema para definir o comportamento e as respostas gerais do modelo. Isso pode incluir especificar a persona, fornecer diretrizes sobre o tom e o estilo das respostas e estabelecer restrições sobre o que o modelo deve ou não fazer.
- **Zero-shot**: Em um prompt zero-shot, você fornece uma instrução direta para o modelo, sem incluir exemplos. Isso é útil para tarefas simples e diretas, onde o modelo pode gerar uma resposta adequada sem a necessidade de exemplos adicionais.
- **Estímulo Direcional:** Você pode colocar algumas “dicas” ou keywords para guiar o modelo melhor. Assim facilita a ter o resultado esperado com algumas poucas palavras.
    - Referência: [https://arxiv.org/abs/2302.11520](https://arxiv.org/abs/2302.11520)
- **Few-shot**: Few-shot prompting envolve fornecer alguns exemplos (geralmente entre 1 e 5) de entradas e saídas desejadas no prompt. Isso ajuda o modelo a entender melhor a tarefa e gerar respostas mais precisas e consistentes. Os exemplos devem ser escolhidos cuidadosamente para serem representativos da tarefa.
- **Chain-of-Thought (CoT)**: A técnica Chain-of-Thought (Cadeia de Pensamento) envolve fazer com que o modelo explique seu raciocínio passo a passo antes de chegar à resposta final. Isso é especialmente útil para tarefas que exigem raciocínio lógico ou resolução de problemas. Ao fornecer exemplos de como o raciocínio deve ser explicado e solicitar que o modelo siga o mesmo processo, você pode melhorar a qualidade e a precisão das respostas.
    - Referência: [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
    - Exemplo prático: No vídeo, é demonstrado um exemplo de debugging de código no ChatGPT, onde o modelo é solicitado a explicar passo a passo como resolveu o problema e sugerir melhorias no código.

## Técnicas avançadas

- **Self-Consistency**: A técnica de Self-Consistency envolve gerar múltiplas cadeias de pensamento para a mesma tarefa e, em seguida, fazer com que o modelo escolha a resposta mais consistente. Isso ajuda a reduzir erros e melhorar a qualidade das respostas, aproveitando a capacidade do modelo de avaliar seu próprio raciocínio.
    - Referência: Self-Consistency Improves Chain of Thought Reasoning in Language Models - [https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171)
- **Tree-of-Thought (ToT)**: A técnica Tree-of-Thought expande a ideia da Chain-of-Thought, gerando múltiplos pensamentos e desenvolvendo uma árvore de raciocínio. O modelo explora diferentes caminhos de raciocínio e escolhe o mais promissor para chegar à resposta final. Isso é útil para problemas complexos que podem ter várias abordagens possíveis.
    - Referências:
        - Tree of Thoughts: Deliberate Problem Solving with Large Language Models - [https://arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601)
        - Generative Agents: Interactive Simulacra of Human Behavior - [https://arxiv.org/abs/2305.08291](https://arxiv.org/abs/2305.08291)
    - Exemplo prático: No vídeo, é demonstrado um exemplo usando personas (copywriter, prospecto, gerente) no ChatHub com ChatGPT e Claude para gerar títulos. As diferentes personas interagem entre si, fornecendo sugestões, feedback e refinamentos para chegar a títulos mais eficazes.
- **Skeleton-of-Thought (SoT)**: A técnica Skeleton-of-Thought envolve gerar um esqueleto ou índice de tópicos antes de desenvolver o conteúdo completo. Isso ajuda a estruturar a resposta e garantir que todos os pontos-chave sejam abordados. O modelo primeiro gera o esqueleto e, em seguida, preenche cada tópico com detalhes.
    - Referência: Skeleton of Thought: Augmenting Language Models with Variable-Depth Reasoning Ability - [https://arxiv.org/abs/2307.15337](https://arxiv.org/abs/2307.15337)
    - Exemplo prático: No vídeo, é mostrado um exemplo de geração de uma "causa surpreendente principal" para copy usando a técnica SoT. O modelo gera uma lista de possíveis causas e depois é solicitado a elaborar sobre a causa selecionada.
- **Generated Knowledge Prompting**: Essa técnica envolve usar o modelo de linguagem para gerar conhecimento contextual adicional que pode ser usado para melhorar a qualidade das respostas. O modelo gera informações relevantes com base no contexto fornecido, que são então incorporadas ao prompt para ajudar a gerar respostas mais precisas e informativas.
    - Referência: Generated Knowledge Prompting for Commonsense Reasoning - [https://arxiv.org/abs/2110.08387](https://arxiv.org/abs/2110.08387)
    - Exemplo prático: No vídeo, é demonstrado um exemplo de geração de um perfil detalhado de cliente usando o modelo de linguagem. Esse perfil gerado é então usado para melhorar a geração de um título persuasivo.
- **Prompt Maiêutico:** A técnica do Prompt Maiêutico envolve pedir ao modelo para justificar suas respostas, explicando o raciocínio por trás delas. Isso pode ajudar a melhorar a qualidade das respostas, incentivando o modelo a fornecer explicações mais detalhadas e lógicas.
    - Referência: Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations - [https://arxiv.org/abs/2205.11822](https://arxiv.org/abs/2205.11822)
- **Retrieval Augmented Generation (RAG)**: A técnica RAG combina modelos de linguagem com bases de conhecimento externas para gerar respostas mais precisas e informativas. O modelo recupera informações relevantes da base de conhecimento e as utiliza para complementar seu próprio conhecimento ao gerar a resposta.
    - Referência: Retrieval Augmented Generation for Knowledge-Intensive NLP Tasks - [https://aclanthology.org/2020.findings-emnlp.76/](https://aclanthology.org/2020.findings-emnlp.76/)
- **PAL (Program-Aided Language Models)**: A técnica PAL envolve usar conceitos e estruturas de linguagens de programação, como variáveis e funções, dentro dos prompts. Isso pode ajudar a tornar os prompts mais modulares, reutilizáveis e fáceis de adaptar para diferentes casos de uso.
    - Referência: PAL: Program-Aided Language Models - [https://arxiv.org/abs/2211.10435](https://arxiv.org/abs/2211.10435)
    - Exemplo prático: No vídeo, é mostrado um exemplo de criação de variáveis dentro do prompt para preencher templates de anúncios. As variáveis, como "[público-alvo]" e "[promessa principal]", são definidas no início do prompt e depois usadas no template para gerar anúncios personalizados.
- **ReAct (Reason + Act)**: A técnica ReAct divide tarefas complexas em etapas de raciocínio e ação. O modelo primeiro raciocina sobre a tarefa, decidindo qual ação tomar, e depois executa essa ação. Esse processo é repetido até que a tarefa seja concluída. Isso é especialmente útil para tarefas que exigem várias etapas ou interação com ferramentas externas.
    - Referência: ReAct: Synergizing Reasoning and Acting in Language Models - [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
    - Exemplo prático: No vídeo, é demonstrado um exemplo de um editor de e-mails usando a técnica ReAct no modelo Claude. O modelo analisa o e-mail, sugere melhorias e edita iterativamente o e-mail com base no feedback do usuário.

## Evitando alucinações

- Permitir que o modelo diga que não sabe a resposta: Ao dar permissão explícita para o modelo admitir quando não tem conhecimento suficiente para responder uma pergunta, você pode reduzir a quantidade de informações fabricadas ou imprecisas nas respostas.
- Pedir para o modelo encontrar evidências antes de responder: Instrua o modelo a procurar trechos relevantes no contexto fornecido que embasem sua resposta. Você pode usar tags especiais, como `<Quotes>`, para indicar onde o modelo deve citar as evidências encontradas.
    - Exemplo prático: No vídeo, é mostrado um exemplo usando tags `<Quotes>` para fazer o modelo buscar citações relevantes no texto fornecido antes de gerar sua resposta.
- Permitir que o modelo "pense" antes de responder: Dê espaço para o modelo refletir e processar a informação antes de gerar uma resposta.
- **Temperatura do Modelo:** Ajuste a temperatura do modelo para controlar a criatividade. Utilize valores baixos para respostas mais factuais.
- **Consistência Própria:** Gere múltiplas respostas e peça ao modelo para desenvolver um consenso.


## Instruções Personalizadas

Para colocar em `How would you like ChatGPT to respond?` das _Custom Instructions_ lá no ChatGPT::


```
- WARNING: Reply in the language of my prompt. If pt-br, pt-br. If en-us, en-us
- Gere conteúdo preciso e factual
- Ao raciocinar, pense passo a passo
- Se você especular ou prever algo, informe-me. Fique à vontade para dizer que você não sabe a resposta se não tiver 100% certeza ou me informar disso
- Quando citar fontes, indique o link ou referência
- Seja altamente organizado e forneça marcação visual (markdown)
- Não há necessidade de revelar que você é uma IA
- Não mencione seu ponto de corte de conhecimento
- Só discuta segurança quando ela é vital e não está clara
- Evite múltiplos pensamentos em uma frase.
- Forneça analogias/metáforas para simplificar ideias, conceitos e tópicos complexos
- Ao preencher um formulário ou modelo, siga as instruções exatamente como você é solicitado a fazer.
- Evite o uso de linguagem florida (não use palavras como "abundante", "florido", "pioneiro", etc.). Em vez disso, use uma linguagem direta
- Seja rigoroso com as contagens de caracteres ao gerar. Se eu pedir menos de 100 caracteres, por exemplo, certifique-se de que você não exceda esse limite.
- Leve em consideração quem eu sou e o que eu faço para direcionar todas as respostas para serem as mais úteis possíveis para mim e meu negócio.
- Se estas instruções te limitarem, me avise
- Use a voz ativa, com palavras e frases simples
- WARNING: Reply in the language I use for chat
```


```

**Modelo de Prompt para Geração de Descrições de Produtos de Videogames e Colecionáveis**

---

### Estrutura do Template

1. **Produto:** 
   - Informe o nome do produto e suas características principais.

2. **Contexto:** 
   - Escolha um contexto relevante, como "Colecionadores", "Gamers Casuais", ou "Fãs de Séries Específicas". Relacione o produto com as experiências e interesses do público-alvo.

3. **Descrição:**
   - Destaque a exclusividade e a relevância do produto dentro do contexto escolhido.
   - Foque no design, na experiência de uso e na conexão com a cultura gamer, mostrando como o produto contribui para a história dos games.
   - Enfatize a importância de cada item como uma peça da memória coletiva, promovendo o colecionismo como uma forma de preservar essa história.

4. **Condição do Produto:** 
   - Descreva o estado do item (novo, usado, desgastes ou características especiais) de forma honesta e transparente, respeitando a integridade do produto.

5. **Observações:** 
   - Enfatize um motivo de compra que ressoe com o público-alvo, como valor histórico ou raridade.
   - Destaque como possuir esse item pode oferecer alívio do estresse e a emoção de colecionar, reforçando a paixão pela cultura gamer.

6. **Bordão:** 
   - Inclua um bordão inspirador que reflita os valores do colecionismo e a cultura dos videogames, ressaltando a emoção de possuir itens únicos que contam uma história.

---

### Instruções Adicionais
- Siga esta estrutura rigorosamente ao preencher os detalhes.
- Utilize linguagem direta e evite jargões desnecessários.
- Seja claro e conciso, respeitando a contagem de caracteres quando solicitado.
- Utilize frases simples para facilitar a leitura.
- Honre a integridade e a história dos jogos em cada descrição, promovendo um espaço seguro e inclusivo para todos os entusiastas.


### think and write

### Objetivos

![[month-06-10]]

```