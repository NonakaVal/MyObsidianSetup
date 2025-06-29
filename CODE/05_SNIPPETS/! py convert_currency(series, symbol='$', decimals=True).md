def convert_currency(series, symbol='$', decimals=True):
    """
    Convert currency string to numeric value.
    
    Usage:
	df['price'] = convert_currency(df['price'], symbol='€')
    
    Parameters:
        series (pd.Series): Series containing currency values
        symbol (str): Currency symbol to remove (default '$')
        decimals (bool): Whether to keep decimals (default True)
    
    Returns:
        pd.Series: Converted numeric values
    """
    dtype = float if decimals else int
    return (
        series.str.replace(f'[{symbol},]', '', regex=True)
        .astype(dtype)
    )

