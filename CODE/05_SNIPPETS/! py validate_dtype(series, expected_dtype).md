def validate_dtype(series, expected_dtype):
    """
    Validate if series has expected dtype.
    
    # Usage:
	# validate_dtype(df['age'], 'int')
    
    Parameters:
        series (pd.Series): Series to validate
        expected_dtype (str/dtype): Expected dtype (e.g., 'int', 'float', 'category')
    
    Raises:
        TypeError: If dtype doesn't match
    """
    if not pd.api.types.is_dtype(series.dtype, expected_dtype):
        raise TypeError(f"Expected {expected_dtype}, got {series.dtype}")


