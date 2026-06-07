---
source: "05 Toolbox/Functions/py-importing-data.md"
block: 1
language: python
added: 2026-05-21
tags: []
---

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
