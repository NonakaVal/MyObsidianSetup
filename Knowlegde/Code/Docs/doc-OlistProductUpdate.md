---
tags:
  - workflow
HUB:
  - "[[hub-work]]"
  - "[[hub-data-wrangling]]"
  - "[[hub-jupyterNotebook]]"
repo: 
---
# Descrição

Atualizar todos os produtos no olist a partir de planilhas do mercado livre 

# Planilhas Necessárias

## Local no ML

## Local no Olist 
Cadastro > Produtos
![Imgur](https://i.imgur.com/S7Ygqs4.png)

Mais opções > Exportar produtos para planilha
![Imgur](https://i.imgur.com/0HBrhUb.png)

Selecionar formato `.csv` e download
Como descrito é necessário baixar multiplos arquivos, e em `.csv`
![Imgur](https://i.imgur.com/fIdnhBJ.png)

# Requirements and Libs

## import and set category map


```python
import os
import pandas as pd
import numpy as np
import pyshorteners
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import math

import warnings
warnings.filterwarnings('ignore')

```


```python
categorias = {
    'Videogames': '001',
    'Figuras de ação': '002',
    'Consoles de videogames': '003',
    'Gamepads e joysticks': '004',
    'Figuras interativas para videogames': '005',
    'Consoles de videogames, videogames e máquinas de fliperama': '006',
    'Relógios de pulso': '007',
    'Skins para consoles e controles de videogames': '008',
    'Camisetas': '009',
    'Livros': '010',
    'Veículos em miniatura': '011',
    'Camisas de futebol': '012',
    'Câmeras e barras sensoras para consoles de videogames': '013',
    'Controles remotos multimídia para consoles de videogames': '014',
    'Tênis': '015',
    'Brinquedos e hobbies': '016',
    'Produtos não classificados': '017',
    'Controles remotos para reprodutores de vídeo': '018',
    'Óculos de realidade virtual': '019',
    'Relógios de parede': '020',
    'Relógios de bolso': '021',
    'Luminárias de mesa e escritório': '022',
    'Canecas': '023',
    'Suportes para reprodutores de vídeo e consoles de videogames': '024',
    'Copos e taças': '025',
    'Álbuns de música antigos': '026',
    'Capas e estojos para consoles de videogames': '027',
    'Cartões de memória': '028',
    'Fontes de alimentação para consoles de videogames': '029',
    'Cabos e adaptadores de áudio e vídeo' : '030'
}
```

# Functions set

## Load_data and Merge_sku


```python
def load_data(path_excel, path_csv, sheet_name_value=2):
    data_excel = pd.read_excel(path_excel, 
                               sheet_name=sheet_name_value, 
                               skiprows=range(1, 6))
    data_excel['STATUS'] = data_excel['STATUS'].str.strip()
    data_excel = data_excel.drop_duplicates(subset='ITEM_ID', keep='first')
    data_excel = data_excel.drop(columns=['VARIATIONS', 'VARIATION_ID'])
    
    data_csv = path_csv

    return data_excel, data_csv

def merge_and_get_sku(df_with_sku, df_without_sku):
    """Preenche os SKUs em df_without_sku com base em df_with_sku (usando ITEM_ID como chave)."""
    merged_data = df_without_sku.merge(df_with_sku[['TITLE', 'SKU']], on='TITLE', how='left', suffixes=('', '_from_df1'))
    merged_data['SKU'] = merged_data['SKU_from_df1']
    merged_data.drop(columns=['SKU_from_df1'], inplace=True)
    merged_data['CATEGORY_ID'] = merged_data['CATEGORY'].map(categorias)
    
    return merged_data
```

## SKU GENERATE


```python
def update_product_skus(data):
    
    current_year_month = datetime.now().strftime("%y%m")  # Ano e mês atual no formato "yyMM"
    
    # Preparando para rastrear informações adicionais sobre novos SKUs
    new_skus_list = []
    new_skus_details = []  # Lista para armazenar detalhes para novos SKUs incluindo ITEM_ID e TITLE

    # Certifique-se de que CATEGORY_ID tenha 3 dígitos
    data['CATEGORY_ID'] = data['CATEGORY_ID'].str.zfill(3)

    # Dicionário para rastrear o contador por categoria e mês
    category_counters = {}

    for category_id in data['CATEGORY_ID'].unique():
        category_mask = data['CATEGORY_ID'] == category_id

        # Filtra os SKUs existentes dessa categoria e mês
        existing_skus = data.loc[category_mask & data['SKU'].notna(), 'SKU']

        # Verifica o ano/mês atual para a categoria
        year_month = current_year_month

        # Extraímos os contadores do SKU, considerando a categoria e mês
        counters = existing_skus.str.extract(f"^{category_id}-{year_month}-(\\d{{4}})$")[0]
        valid_counters = pd.to_numeric(counters, errors='coerce').dropna().astype(int)
        
        # Define o próximo contador, baseado no maior contador existente, ou inicia em 1
        if not valid_counters.empty:
            next_counter = valid_counters.max() + 1
        else:
            next_counter = 1

        # Filtra os índices dos produtos sem SKU
        null_skus_indices = data.index[category_mask & data['SKU'].isna()]
        for idx in null_skus_indices:
            # Gera um SKU único com base na categoria, ano/mês e o contador
            new_sku = f"{category_id}-{year_month}-{next_counter:04d}"
            data.at[idx, 'SKU'] = new_sku
            new_skus_list.append(new_sku)
            new_skus_details.append({
                'TITLE': data.at[idx, 'TITLE'],
                'SKU': new_sku,
                'ITEM_ID': data.at[idx, 'ITEM_ID'],
            })

            # Incrementa o contador após gerar o SKU para o próximo
            next_counter += 1

    # Converte a lista de dicionários em DataFrame
    new_skus_data = pd.DataFrame(new_skus_details)  # Agora inclui ITEM_ID e TITLE

    return data, new_skus_data

# def get_links(data):
#     data['ITEM_LINK'] = data['ITEM_ID'].apply(
#         lambda x: f"https://www.mercadolivre.com.br/anuncios/lista?filters=OMNI_ACTIVE|OMNI_INACTIVE|CHANNEL_NO_PROXIMITY_AND_NO_MP_MERCHANTS&page=1&search={x[3:]}" if pd.notnull(x) else "")

#     data['URL'] = data.apply(
#         lambda row: f"https://www.collectorsguardian.com.br/{row['ITEM_ID'][:3]}-{row['ITEM_ID'][3:]}-{row['TITLE'].replace(' ', '-').lower()}-_JM#item_id={row['ITEM_ID']}", 
#         axis=1)

#     return data
```

# Paths and run


```python
excel_path = r'data\Anuncios-2025_04_30-16_06.xlsx'
csv_1 = pd.read_csv(r'data\produtos_2025-04-30-17-06-40-1.csv')
csv_2 = pd.read_csv(r'data\produtos_2025-04-30-17-06-51-2.csv')
```


```python
csv_df = pd.concat([csv_1, csv_2], ignore_index=True)
csv_df = csv_df.rename(columns={'Descrição': 'TITLE','Código (SKU)':"SKU"})
excel_df, csv_df = load_data(excel_path, csv_df)
merged_df = merge_and_get_sku(csv_df, excel_df)

data, news = update_product_skus(merged_df)
data = get_links(data)
```

## GET IMAGES FUNG - NÃO OTIMIZADA


```python
# def extract_first_src(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         soup = BeautifulSoup(response.text, 'html.parser')
    
#         img_tag = soup.find('img', class_='ui-pdp-image ui-pdp-gallery__figure__image')
#         if img_tag and 'src' in img_tag.attrs:
#             return img_tag['src']
#         return None  # Caso a tag ou atributo não seja encontrado
#     except Exception as e:
#         print(f"Erro ao processar {url}: {e}")
#         return None

# # Aplicando a função a cada link no DataFrame
# df['IMG'] = df['URL'].apply(extract_first_src)
```

# OLIST formatation


```python
df_2 = data[['SKU', 'TITLE', 'MSHOPS_PRICE','QUANTITY']]
```


```python
col_names = {
    'SKU' : 'Código (SKU)',
    'TITLE': 'Descrição',
    'MSHOPS_PRICE':'Preço',    
    'QUANTITY' : 'Estoque',
    'IMG' : 'URL imagem 1'
}
df_2 = df_2.rename(columns=renames)
```


```python
df_2['Situação'] = 'Ativo'
df_2['Tipo do produto'] = 'S'
df_2['Sob encomenda'] = 'Não'
df_2['Controlar lotes'] = 'Não'
# Lista completa das colunas desejadas
colunas_desejadas = [
    'ID', 'Código (SKU)', 'Descrição', 'Unidade', 'Classificação fiscal', 'Origem', 'Preço',
    'Valor IPI fixo', 'Observações', 'Situação', 'Estoque', 'Preço de custo', 'Cód do Fornecedor',
    'Fornecedor', 'Localização', 'Estoque máximo', 'Estoque mínimo', 'Peso líquido (Kg)', 'Peso bruto (Kg)',
    'GTIN/EAN', 'GTIN/EAN tributável', 'Descrição complementar', 'CEST', 'Código de Enquadramento IPI',
    'Formato embalagem', 'Largura embalagem', 'Altura embalagem', 'Comprimento embalagem', 'Diâmetro embalagem',
    'Tipo do produto', 'URL imagem 1', 'URL imagem 2', 'URL imagem 3', 'URL imagem 4', 'URL imagem 5', 
    'URL imagem 6', 'Categoria', 'Código do pai', 'Variações', 'Marca', 'Garantia', 'Sob encomenda',
    'Preço promocional', 'URL imagem externa 1', 'URL imagem externa 2', 'URL imagem externa 3',
    'URL imagem externa 4', 'URL imagem externa 5', 'URL imagem externa 6', 'Link do vídeo', 'Título SEO',
    'Descrição SEO', 'Palavras chave SEO', 'Slug', 'Dias para preparação', 'Controlar lotes',
    'Unidade por caixa', 'URL imagem externa 7', 'URL imagem externa 8', 'URL imagem externa 9',
    'URL imagem externa 10', 'Markup', 'Permitir inclusão nas vendas', 'EX TIPI'
]

# Adiciona ao df as colunas faltantes com valor nulo
for coluna in colunas_desejadas:
    if coluna not in df_2.columns:
        df_2[coluna] = np.nan

# Reorganiza as colunas na ordem correta
df_2 = df_2[colunas_desejadas]
df_2['Preço'] =  df_2['Preço'].astype(int)
```

## Exportando em arquivos de até 500 linhas


```python
# Supondo que o DataFrame 'data' já esteja definido
tamanho_maximo = 500
numero_partes = math.ceil(len(df_2) / tamanho_maximo)

# Dividindo o DataFrame
dataframes_divididos = np.array_split(df_2, numero_partes)

# Exportando cada parte como CSV separado
for i, df_2 in enumerate(dataframes_divididos):
    nome_arquivo = f"produtos_parte_{i + 1}.csv"
    df_2.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')

print("Arquivos CSV exportados com sucesso!")

```

    Arquivos CSV exportados com sucesso!
    


```python

```
