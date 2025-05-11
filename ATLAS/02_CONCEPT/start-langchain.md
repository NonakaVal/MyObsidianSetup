---
tags:
  - learning
created: "[[2024-04-27]]"
hub:
  - "[[hub-python]]"
---
### [[start-langchain]]


- Requirements
	- pip install langchain_openai
	- pip install langchain_experimental
	- pip pandas
	- pip install tabulate

```python
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI


def _chat(df_path):
    openai_api_key = ""
    df = df_path
    llm = ChatOpenAI(model = "gpt-3.5-turbo", openai_api_key=openai_api_key)
    agent_prefix = "O df importado é\n"

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        prefix=agent_prefix,
        verbose  = True,
        agent_type = AgentType.OPENAI_FUNCTIONS,
    )

    while True:
        prompt = input("Digite o prompt ou 'sair\n'")
        if prompt.lower() == 'sair':
            print("finalizando...")
            break
        response = agent.invoke(prompt)
```
