def filter_outliers_iqr(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Filtra outliers de uma coluna numérica usando o método IQR (Intervalo Interquartil).
	# dados_sem_outliers = filter_outliers_iqr(dados, 'Valor')
	
    Args:
        data (pd.DataFrame): DataFrame contendo os dados.
        column (str): Nome da coluna numérica a ser analisada.

    Returns:
        pd.DataFrame: DataFrame sem os outliers da coluna especificada.
    """
    valor = data[column]
    
    # Cálculo dos quartis e limites
    q1 = valor.quantile(0.25)
    q3 = valor.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Filtro dos dados
    selecao = (valor >= lower_bound) & (valor <= upper_bound)
    return data[selecao]

# Exemplo de uso:
