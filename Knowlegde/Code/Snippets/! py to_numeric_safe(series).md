
def to_numeric_safe(series):
    """
    Convert to numeric, coercing errors to NaN.
	# Usage:
	# df['quantity'] = to_numeric_safe(df['quantity'])

    Parameters:
        series (pd.Series): Series to convert
    
    Returns:
        pd.Series: Converted numeric series
    """
    return pd.to_numeric(series, errors='coerce')


