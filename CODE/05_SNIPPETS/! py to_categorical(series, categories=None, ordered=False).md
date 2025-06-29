def to_categorical(series, categories=None, ordered=False):
    """
    Convert to categorical with optional categories.
    Usage:
	df['grade'] = to_categorical(df['grade'], categories=['A','B','C','D','F'])
    
    Parameters:
        series (pd.Series): Series to convert
        categories (list): Optional predefined categories
        ordered (bool): Whether categories are ordered
    
    Returns:
        pd.Series: Converted categorical series
    """
    return series.astype(
        pd.CategoricalDtype(categories=categories, ordered=ordered)
    )

