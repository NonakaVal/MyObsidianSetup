---
created: "[[2025-05-02]]"
tags:
  - snippet
HUB:
  - "[[hub-llm]]"
  - "[[hub-python]]"
connections:
  - "[[concept-python-pandas-dataframe-variables|concept-python-pandas-dataframe-variables]]"
share_link: https://share.note.sx/8m5lqgco#QVtEAQOlvL5ArAPVoRvT/8so7jV20j1NP03iDjLWZXI
share_updated: 2025-05-09T21:18:09-03:00
---

Notes Related : `INPUT[inlineListSuggester(optionQuery("Atlas")):connections]` 

# {propósito}
Cria um Agente de classificação de colunas  de dataframe pandas

# {códigos}



```python

import pandas as pd
import openai
from tqdm import tqdm

def classificar_dataframe(api_key, dataframe, coluna_texto, coluna_classificacao='classificacao', 
                         model="gpt-3.5-turbo", 
                         system_prompt="Classifique o texto como 'Positivo', 'Neutro' ou 'Negativo'.",
                         temperature=0.3, batch_size=1):
    """
    Classifica textos em um DataFrame usando a API da OpenAI.
    
    Parâmetros:
    -----------
    api_key : str
        Chave de API da OpenAI
    dataframe : pd.DataFrame
        DataFrame contendo os textos a serem classificados
    coluna_texto : str
        Nome da coluna que contém os textos para classificação
    coluna_classificacao : str, opcional
        Nome da coluna onde as classificações serão armazenadas (padrão: 'classificacao')
    model : str, opcional
        Modelo da OpenAI a ser utilizado (padrão: 'gpt-3.5-turbo')
    system_prompt : str, opcional
        Instrução de sistema para o modelo (padrão: classificação de sentimentos)
    temperature : float, opcional
        Controla a aleatoriedade das respostas (padrão: 0.3)
    batch_size : int, opcional
        Número de textos para enviar em cada requisição (padrão: 1)
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame com a coluna de classificação preenchida
    """
    
    # Configurar API
    openai.api_key = api_key
    
    # Verificar se a coluna de classificação existe, se não, criar
    if coluna_classificacao not in dataframe.columns:
        dataframe[coluna_classificacao] = ''
    
    # Função interna para classificação em lote
    def _classificar_batch(batch_texts):
        try:
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend([{"role": "user", "content": text} for text in batch_texts])
            
            resposta = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature
            )
            return resposta.choices[0].message['content']
        except Exception as e:
            print(f"Erro ao classificar batch: {e}")
            return ["Erro"] * len(batch_texts)
    
    # Processar em lotes ou individualmente
    if batch_size > 1:
        # Processamento em lote
        textos = dataframe[coluna_texto].tolist()
        classificacoes = []
        
        for i in tqdm(range(0, len(textos), batch_size), desc="Classificando textos"):
            batch = textos[i:i+batch_size]
            resultado = _classificar_batch(batch)
            
            # Se a resposta for única (string), transforma em lista
            if isinstance(resultado, str):
                resultado = [res.strip() for res in resultado.split('\n')]
                # Garantir que temos exatamente batch_size elementos
                resultado = resultado + ["Erro"] * (batch_size - len(resultado))
            
            classificacoes.extend(resultado[:len(batch)])
        
        dataframe[coluna_classificacao] = classificacoes[:len(dataframe)]
    else:
        # Processamento individual
        for idx, row in tqdm(dataframe.iterrows(), total=len(dataframe), desc="Classificando textos"):
            texto = row[coluna_texto]
            resultado = _classificar_batch([texto])
            dataframe.at[idx, coluna_classificacao] = resultado[0] if isinstance(resultado, list) else resultado
    
    return dataframe

# Solicitar inputs do usuário
api_key_input = input("Insira sua chave de API da OpenAI: ")
system_prompt_input = input("Insira o prompt do sistema (ou pressione Enter para usar o padrão): ")


# Usar prompt padrão se o usuário não fornecer um
if not system_prompt_input.strip():
    system_prompt_input = "Classifique o texto como 'Positivo', 'Neutro' ou 'Negativo'."

# Classificar o DataFrame
df_classificado = classificar_dataframe(
    api_key=api_key_input,
    dataframe=df,
    coluna_texto='texto',
    coluna_classificacao='sentimento',
    system_prompt=system_prompt_input
)

print("\nResultado da classificação:")
print(df_classificado)

```