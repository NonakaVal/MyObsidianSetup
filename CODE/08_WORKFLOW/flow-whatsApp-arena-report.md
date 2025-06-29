---
tags:
  - workflow
HUB:
  - "[[hub-jupyterNotebook]]"
  - "[[hub-work]]"
created: "[[2025-05-03]]"
share_link: https://share.note.sx/d01qiii9#fd0tXc6kt8c2tl3KvOucKm/Wn4LM3oghTxk467eTblY
share_updated: 2025-05-09T20:53:53-03:00
---
# Análise de Leilões
## Processamento e análise de dados exportados diretamente do chat de leilões do whatsapp


```python
# %% Requirements
import pandas as pd
import re
from datetime import datetime
from pathlib import Path

# %% [markdown]

# %%
# Configurações globais
CAMINHO_ARQUIVO = r'C:\Users\nonak\Documents\CollectorsGuardian\_chat.txt'
DATA_INICIO = datetime(2025, 3, 1).date()
DATA_FIM = datetime(2025, 4, 30).date()
NOME_ARQUIVO_EXCEL = r"H:\Meu Drive\Workspaces\relatorio_arena_collectors1.xlsx"

DIAS_SEMANA = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

```


# Processamento de mensagens

## Funções de Extração de Dados
- Data e Hora
- Produto vendido.
- Mensagens ADM
- Entrada e saída
- Entradas/saídas de membros.
- Processa mensagens apagadas.


```python
###     """Extrai data e hora de uma linha de mensagem."""
def extrair_data_hora(linha):
    """Extrai data e hora de uma linha de mensagem."""
    data_hora_match = re.match(r"\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\]", linha)
    if not data_hora_match:
        return None, None
        
    data_str, hora_str = data_hora_match.groups()
    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date(), hora_str
    except ValueError:
        return None, None
```


```python
# %%     """Processa mensagens de produto vendido."""
def processar_produto(linha, data, hora, container):
    """Processa mensagens de produto vendido."""
    if "se torna o guardião do" not in linha and "venceu a disputa e agora guarda o" not in linha:
        return False

    try:
        # Padrão 1: "🏆 *Nome* se torna o guardião do *Produto* por R$*Valor*"
        # Padrão 2: "👑 *Nome* venceu a disputa e agora guarda o *Produto* em seu legado. Conquistado por R$*Valor*"
        padrao = re.compile(
            r"(?:🏆 \*(.*?)\* se torna (?:o|a) guardi(?:ão|ã) do \*(.*?)\* por \*R\$(.*?)\*|"
            r"👑 \*(.*?)\* venceu a disputa e agora guarda o \*(.*?)\* em seu legado\. Conquistado por \*R\$(.*?)\*)"
        )
        match = padrao.search(linha)
        
        if not match:
            print(f"Padrão não encontrado na mensagem de produto: {linha[:100]}...")
            return False
            
        # Determina qual padrão foi encontrado
        if match.group(1):  # Padrão 1
            vencedor = match.group(1).strip()
            produto = match.group(2).strip()
            valor_str = match.group(3).replace(".", "").replace(",", ".")
        else:  # Padrão 2
            vencedor = match.group(4).strip()
            produto = match.group(5).strip()
            valor_str = match.group(6).replace(".", "").replace(",", ".")
        
        container.append({
            "Data": data,
            "Hora": hora,
            "Produto": produto,
            "Valor Final": float(valor_str),
            "Vencedor": vencedor
        })
        return True
        
    except Exception as e:
        print(f"⚠️ Erro ao processar produto: {linha[:50]}...")
        print(f"Erro detalhado: {str(e)}")
        return False
```


```python
# %% """Processa mensagens de lance."""
def processar_lance(linha, data, hora, produto_atual, container):
    """Processa mensagens de lance."""
    match = re.search(r"\] ([^:]+): (\d+)(?:\D|$)", linha)
    if not match or "Collector's Guardian" in match.group(1):
        return False

    container.append({
        "Data": data,
        "Hora": hora,
        "Nome": match.group(1).strip(),
        "Valor": int(match.group(2)),
        "Tipo": "Lance",
        "Produto": produto_atual
    })
    return True

# %%
```


```python
# %%     """Processa mensagens administrativas."""
def processar_admin(linha, data, hora, container):
 
    if "Collector's Guardian:" not in linha:
        return False

    mensagem = linha.split("Collector's Guardian:")[1].strip()
    tipo = "Administrativa"
    
    if "assumiu a liderança" in mensagem or "Domina a Arena" in mensagem:
        tipo = "Liderança"
    elif "Parabéns" in mensagem or "se torna o guardião" in mensagem or "venceu a disputa" in mensagem:
        tipo = "Vencedor"
    elif "⌛" in mensagem or "Faltam" in mensagem:
        tipo = "Tempo"
    elif "🔥" in mensagem or "vira o jogo" in mensagem:
        tipo = "Virada"

    container.append({
        "Data": data,
        "Hora": hora,
        "Mensagem": mensagem,
        "Tipo": tipo
    })
    return True
```


```python
# %%    """Processa entradas/saídas de membros."""
def processar_membro(linha, data, hora, container):
    """Processa entradas/saídas de membros."""
    if " entrou" not in linha and " saiu" not in linha and "deseja entrar" not in linha:
        return False

    if "deseja entrar" in linha:
        acao = "solicitou entrada"
        nome = linha.split("] ")[1].split(" deseja")[0].strip()
    else:
        acao = "entrou" if " entrou" in linha else "saiu"
        nome = linha.split("] ")[1].split(acao)[0].strip()

    container.append({
        "Data": data,
        "Hora": hora,
        "Membro": nome,
        "Ação": acao,
        "Detalhes": linha.strip()
    })
    return True
```


```python
# %%     """Processa mensagens apagadas."""
def processar_apagada(linha, data, hora, container):
    """Processa mensagens apagadas."""
    if "‎Mensagem apagada" not in linha:
        return False

    autor = linha.split("] ")[1].split(":")[0].strip()
    container.append({
        "Data": data,
        "Hora": hora,
        "Autor": autor,
        "Tipo": "Mensagem Apagada"
    })
    return True

# %%
```

## Função principal para extrair dados do chat


```python
# %%     """Função principal para extrair dados do chat."""
def extrair_dados(linhas):
    """Função principal para extrair dados do chat."""
    dados = {
        "lances": [],
        "admin": [],
        "membros": [],
        "apagadas": [],
        "produtos": []
    }
    
    produto_atual = None
    
    for linha in linhas:
        # Extrair data e hora
        data, hora = extrair_data_hora(linha)
        if not data or not (DATA_INICIO <= data <= DATA_FIM):
            continue
            
        # Tenta processar cada tipo de mensagem
        if processar_produto(linha, data, hora, dados["produtos"]):
            produto_atual = dados["produtos"][-1]["Produto"]
            continue

        if processar_lance(linha, data, hora, produto_atual, dados["lances"]):
            continue

        if processar_admin(linha, data, hora, dados["admin"]):
            continue

        if processar_membro(linha, data, hora, dados["membros"]):
            continue

        processar_apagada(linha, data, hora, dados["apagadas"])
    
    # Converter listas para DataFrames
    return {k: pd.DataFrame(v) for k, v in dados.items()}
```

# Funções de Análise



```python
# %% Gera consolidação de lances por participante.
def gerar_consolidado_lances(df_lances):
    """Gera consolidação de lances por participante."""
    if df_lances.empty:
        return pd.DataFrame()

    return (
        df_lances[df_lances["Tipo"] == "Lance"]
        .groupby("Nome")
        .agg(
            Total_Lances=("Valor", "count"),
            Valor_Total=("Valor", "sum"),
            Maior_Lance=("Valor", "max"),
            Média_Lances=("Valor", lambda x: round(x.mean(), 2)),
            Primeiro_Lance=("Data", "min"),
            Último_Lance=("Data", "max")
        )
        .sort_values("Valor_Total", ascending=False)
        .reset_index()
    )
```


```python
# %% Gera análise de atividade administrativa
def gerar_atividade_admin(df_admin):
    """Gera análise de atividade administrativa."""
    if df_admin.empty:
        return pd.DataFrame()

    return (
        df_admin.groupby(["Tipo", "Data"])
        .size()
        .unstack(fill_value=0)
        .T
        .reset_index()
    )

```


```python
# %% Gera análise de movimentação de membros
def gerar_movimentacao_membros(df_membros):
    """Gera análise de movimentação de membros."""
    if df_membros.empty:
        return pd.DataFrame()

    return (
        df_membros.groupby(["Ação", "Data"])
        .size()
        .unstack(fill_value=0)
        .T
        .reset_index()
    )

# %%
```


```python
# %% Gera análise de lances por dia da semana.
def gerar_lances_dia_semana(df_lances):
    """Gera análise de lances por dia da semana."""
    if df_lances.empty:
        return pd.DataFrame()

    df = df_lances.copy()
    df["Dia_Semana"] = (
        pd.to_datetime(df["Data"])
        .dt.day_name()
        .map(DIAS_SEMANA)
    )

    return (
        df.groupby("Dia_Semana")
        .agg(
            Total_Lances=("Valor", "count"),
            Valor_Total=("Valor", "sum"),
            Média=("Valor", lambda x: round(x.mean(), 2))
        )
        .reindex(list(DIAS_SEMANA.values()))
        .reset_index()
        .rename(columns={"Dia_Semana": "Dia da Semana"})
    )

```


```python
# %% Gera análise consolidada dos produtos leiloados. - """Gera todas as análises consolidadas.""""""
def gerar_analise_produtos(df_produtos):
    """Gera análise consolidada dos produtos leiloados."""
    if df_produtos.empty:
        return pd.DataFrame()

    return (
        df_produtos.groupby("Produto")
        .agg(
            Total_Leilões=("Produto", "count"),
            Valor_Médio=("Valor Final", lambda x: round(x.mean(), 2)),
            Valor_Máximo=("Valor Final", "max"),
            Valor_Mínimo=("Valor Final", "min"),
            Última_Data=("Data", "max")
        )
        .sort_values("Valor_Máximo", ascending=False)
        .reset_index()
    )

# %%
def gerar_analises(df_lances, df_admin, df_membros, df_produtos):
    """Gera todas as análises consolidadas."""
    return {
        "consolidado_lances": gerar_consolidado_lances(df_lances),
        "atividade_admin": gerar_atividade_admin(df_admin),
        "movimentacao_membros": gerar_movimentacao_membros(df_membros),
        "lances_dia_semana": gerar_lances_dia_semana(df_lances),
        "analise_produtos": gerar_analise_produtos(df_produtos)
    }
```

# Processamento Principal


```python
# # Carregar e processar dados
# with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
#     dados = extrair_dados(f.readlines())

# # # Gerar análises
# # analises = gerar_analises(dados["lances"], dados["admin"], dados["membros"], dados["produtos"])

```


```python
# %%     """Exibe resumo do processamento."""
def mostrar_resumo(dados, analises):
    """Exibe resumo do processamento."""
    tem_produtos = not dados["produtos"].empty
    caminho = Path(NOME_ARQUIVO_EXCEL).absolute()

    print(f"""
✅ Relatório gerado com sucesso: {caminho}

📊 Estrutura do relatório:
1. Lances - Todos os lances válidos
2. Mensagens Admin - Mensagens do Collector's Guardian
3. Movimentação - Entradas e saídas de membros
4. Mensagens Apagadas - Mensagens removidas
5. Resumo Lances - Consolidação por participante
6. Atividade Admin - Tipos de mensagens administrativas
7. Resumo Movimentação - Entradas/saídas por data
8. Lances por Dia - Atividade por dia da semana
{'9. Produtos Leiloados - Itens leiloados com valores e vencedores' if tem_produtos else ''}
{'10. Análise Produtos - Estatísticas por produto' if tem_produtos else ''}

📅 Período analisado: {DATA_INICIO.strftime('%d/%m/%Y')} a {DATA_FIM.strftime('%d/%m/%Y')}

📈 Estatísticas:
- Total de lances: {len(dados['lances'])}
- Total de produtos leiloados: {len(dados['produtos'])}
- Participantes ativos: {analises['consolidado_lances']['Nome'].nunique()}
    """)

# Mostrar resumo
mostrar_resumo(dados, analises)
```

    
    ✅ Relatório gerado com sucesso: H:\Meu Drive\Workspaces\relatorio_arena_collectors1.xlsx
    
    📊 Estrutura do relatório:
    1. Lances - Todos os lances válidos
    2. Mensagens Admin - Mensagens do Collector's Guardian
    3. Movimentação - Entradas e saídas de membros
    4. Mensagens Apagadas - Mensagens removidas
    5. Resumo Lances - Consolidação por participante
    6. Atividade Admin - Tipos de mensagens administrativas
    7. Resumo Movimentação - Entradas/saídas por data
    8. Lances por Dia - Atividade por dia da semana
    9. Produtos Leiloados - Itens leiloados com valores e vencedores
    10. Análise Produtos - Estatísticas por produto
    
    📅 Período analisado: 01/03/2025 a 30/04/2025
    
    📈 Estatísticas:
    - Total de lances: 679
    - Total de produtos leiloados: 46
    - Participantes ativos: 85
        
    

###  Exportar como arquivo Excel


```python
## Exportar para Excel

# %%
def exportar_para_excel(nome_arquivo, dados, analises):
    """Exporta dados e análises para Excel."""
    with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
        # Dados brutos
        dados["lances"].to_excel(writer, sheet_name="Lances", index=False)
        dados["admin"].to_excel(writer, sheet_name="Mensagens Admin", index=False)
        dados["membros"].to_excel(writer, sheet_name="Movimentação", index=False)
        dados["apagadas"].to_excel(writer, sheet_name="Mensagens Apagadas", index=False)
        
        # Análises
        analises["consolidado_lances"].to_excel(writer, sheet_name="Resumo Lances", index=False)
        analises["atividade_admin"].to_excel(writer, sheet_name="Atividade Admin", index=False)
        analises["movimentacao_membros"].to_excel(writer, sheet_name="Resumo Movimentação", index=False)
        analises["lances_dia_semana"].to_excel(writer, sheet_name="Lances por Dia", index=False)
        
        # Produtos (se houver dados)
        if not dados["produtos"].empty:
            dados["produtos"].to_excel(writer, sheet_name="Produtos Leiloados", index=False)
            analises["analise_produtos"].to_excel(writer, sheet_name="Análise Produtos", index=False)

        # Ajustar largura das colunas
        for sheet in writer.sheets.values():
            for column in sheet.columns:
                max_length = max(len(str(cell.value)) for cell in column)
                sheet.column_dimensions[column[0].column_letter].width = min(max_length + 2, 50)

# %%
# Executar exportação
exportar_para_excel(NOME_ARQUIVO_EXCEL, dados, analises)
```


```python
# # %%
# # Visualizar primeiros registros de cada DataFrame
# if not dados["produtos"].empty:
#     display(dados["produtos"].head())
    
# display(dados["lances"].head())
# display(analises["consolidado_lances"].head())
```


