---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-data-wrangling]]"
connections:
  - "[[rename-colluns-dataframe]]"
  - "[[concept-pandas-dropna-isnull-fillna]]"
  - "[[pandas-isin-method]]"
---
### Importar pandas e ler arquivo.
```python
import pandas as pd
from pathlib import Path

def load_data(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Carrega dados de arquivos CSV, Excel, JSON, Parquet ou TXT/TSV.
    
    Detecta o tipo automaticamente pela extensão do arquivo.

    Parâmetros:
        filepath (str): Caminho do arquivo a ser carregado.
        **kwargs: Parâmetros adicionais passados ao pandas.

    Retorna:
        pd.DataFrame: Dados carregados.
    """
    path = Path(filepath)
    ext = path.suffix.lower()

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    if ext in [".csv"]:
        try:
            return pd.read_csv(path, **kwargs)
        except UnicodeDecodeError:
            return pd.read_csv(path, encoding="latin1", **kwargs)

    elif ext in [".json"]:
        return pd.read_json(path, **kwargs)

    elif ext in [".xls", ".xlsx"]:
        return pd.read_excel(path, **kwargs)

    elif ext in [".parquet"]:
        return pd.read_parquet(path, **kwargs)

    elif ext in [".tsv", ".txt"]:
        return pd.read_table(path, **kwargs)

    else:
        raise ValueError(f"Extensão não suportada: {ext}")

```
- Importar a biblioteca pandas com o nome pd
	- Variável "notas" onde armazenamos a biblioteca pandas (pd) usada para ler tipo de arquivo "csv" , selecionando o caminho do arquivo dentro do ("")
- Notas.head é um comando de imprime no console as 5 primeiras informações guardadas do dataframe "ratings.csv" que está armazenado no "notas"

###  seperar colunas . sep
- "alt" + "tab" te permite ter acesso a metadados sobre o arquivo e regras de separação de colunas etc.
```css
import pandas as pd

dados = pd.read_csv("aluguel.csv", sep";")

def import_data(path):
	pd.read_csv(path)

```
-  o arquivo passa a separar as colunas por ";"

![[concept-importando-outros-tipos-de-arquivos]]


![[concept-dataframe-para-csv]]

