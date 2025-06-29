def check_nulls(series, raise_error=False, threshold=0):

    """
    Check for null values in series.
	ex: Nulls = check_nulls(df['email'], raise_error=True)
    
    Parameters:
        series (pd.Series): Series to check
        raise_error (bool): Whether to raise error if nulls found
        threshold (int): Maximum allowed null count
    
    Returns:
        int: Number of nulls
    """
    null_count = series.isna().sum()
    if raise_error and null_count > threshold:
        raise ValueError(f"Series contains {null_count} null values")
    return null_count
