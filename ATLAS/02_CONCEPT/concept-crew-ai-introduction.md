---
created: "[[2025-05-13]]"
HUB:
  - "[[hub-llm]]"
  - "[[hub-python]]"
tags:
  - concept
---




![Imgur|500](https://i.imgur.com/PV4JKSN.png)


# core concepts

### Agent (agentes)
- pen Unidade autônoma programada para:
	- *Executar tarefas*
	- *Tomar decisões*
	- *Se comunicar  ou outros agentes*
- ! Pense em um agente como um membro de uma equipe, com habilidades específicas e um trabalho particular a fazer. Os agentes podem ter diferentes papéis, como 'Pesquisador', 'Escritor' ou 'Suporte ao Cliente', cada um contribuindo para o objetivo geral da equipe.



Tasks (tarefas)
- pen No framework crewAI, tarefas são atribuições específicas concluídas por agentes. Elas fornecem todos os detalhes necessários para execução, como uma descrição, o agente responsável, ferramentas necessárias e mais, facilitando uma ampla gama de complexidades de ação.

|Atributo|Parâmetros|Descrição|
|---|---|---|
|**Descrição**|`description`|Uma declaração clara e concisa do que a tarefa envolve.|
|**Agente**|`agent`|O agente responsável pela tarefa, designado diretamente ou pelo processo da equipe.|
|**Saída esperada**|`expected_output`|Uma descrição detalhada de como é a conclusão da tarefa.|
|**Ferramentas** _(opcional)_|`tools`|As funções ou capacidades que o agente pode utilizar para executar a tarefa.|
|**Execução assíncrona** _(opcional)_|`async_execution`|Se definido, a tarefa será executada de forma assíncrona, permitindo a progressão sem esperar pela conclusão.|
|**Contexto** _(opcional)_|`context`|Especifica tarefas cujas saídas são usadas como contexto para esta tarefa.|
|**Configuração** _(opcional)_|`config`|Detalhes de configuração adicionais para o agente que executa a tarefa, permitindo maior personalização.|
|**Saída JSON** _(opcional)_|`output_json`|Gera um objeto JSON, exigindo um cliente OpenAI. Apenas um formato de saída pode ser definido.|
|**Saída Pydantic** _(opcional)_|`output_pydantic`|Gera um objeto de modelo Pydantic, exigindo um cliente OpenAI. Apenas um formato de saída pode ser definido.|
|**Arquivo de saída** _(opcional)_|`output_file`|Salva a saída da tarefa em um arquivo. Se usado com `Output JSON`ou `Output Pydantic`, especifica como a saída é salva.|
|**Retorno de chamada** _(opcional)_|`callback`|Um invocável Python que é executado com a saída da tarefa após sua conclusão.|
|**Entrada humana** _(opcional)_|`human_input`|Indica se a tarefa requer feedback humano no final, útil para tarefas que exigem supervisão humana.|

Last modified : `$= dv.current().file.mtime`