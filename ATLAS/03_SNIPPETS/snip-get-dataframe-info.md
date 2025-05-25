---
tags:
  - snippet
HUB:
  - "[[hub-tratamento-de-dados]]"
  - "[[hub-jupyterNotebook]]"
connections:
  - "[[concept-python-pandas-obtendo-informacoes-dados]]"
---
{propósito}

Obter informações básicas do dataframe


```python
def get_df_info(df):
    """
Gera um relatório informativo sobre o DataFrame fornecido, incluindo dimensões, tipos, nulos, únicos e estatísticas.
Generates an informative report about the given DataFrame, including dimensions, types, nulls, uniques, and statistics.
    
    """

    print("📊 📋 RELATÓRIO DO DATAFRAME 📋 📊\n")

    # Dimensões
    print("✅ Dimensões: df.shape")
    print(f"- Linhas: {df.shape[0]:,}")
    print(f"- Colunas: {df.shape[1]}\n")

    # Tipos de dados
    print("🔠 Tipos de dados: df.dtypes.value_counts()")
    print(df.dtypes.value_counts())
    print("\n📑 Tipos por coluna: df.dtypes.sort_index()")
    print(df.dtypes.sort_index())
    print()

    # Valores nulos
    print("🚫 Valores Nulos: df.isnull().sum()")
    null_counts = df.isnull().sum()
    null_percent = (null_counts / len(df)) * 100
    null_df = pd.DataFrame({
        "Nulos": null_counts,
        "Percentual (%)": null_percent.round(2)
    })
    print(null_df[null_df["Nulos"] > 0].sort_values(by="Nulos", ascending=False))
    print()

    # Valores únicos
    print("🔁 Valores únicos: df.nunique()")
    unique_vals = df.nunique().sort_values(ascending=False)
    print(unique_vals)
    print()

    # Amostra dos dados
    print("📌 Amostra (5 primeiras linhas): df.head()")
    print(df.head())
    print()

    # Estatísticas descritivas - Numéricos
    print("📈 Estatísticas descritivas (numéricos): df.describe()")
    print(df.describe().transpose())
    print()

    # Estatísticas descritivas - Categóricos
    print("🗂️ Estatísticas descritivas (categóricos): df.describe(include=['object'])")
    print(df.describe(include=['object']).transpose())
```