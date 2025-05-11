---
tags:
  - learning
  - snippet
HUB:
  - "[[hub-statistic]]"
  - "[[hub-ml-models]]"
  - "[[hub-hypothesis-testing]]"
connections:
  - "[[concept-distribuicao-normal]]"
  - "[[concept-statistic-distribuicao-normal]]"
---

# {propósito}

Obter valores de [[concept-distribuicao-normal|normalidade]] ne um intervalo de dados ou amostra .

# {códigos}

```python
import numpy as np
from scipy.stats import normaltest

def test_normality(sample=None, size=100, alpha=0.05):
    """
    Perform a normality test on a sample using D'Agostino's K^2 test.
    
    Parameters:
    - sample: Input array-like data. If None, generates random uniform samples.
    - size: Size of random sample to generate if sample is None.
    - alpha: Significance level (default 0.05).
    
    Returns:
    - dict: Contains test statistic, p-value, and normality conclusion.
    """
    if sample is None:
        sample = np.random.rand(size)
    
    statistic, p_value = normaltest(sample)
    
    result = {
        'statistic': statistic,
        'p_value': p_value,
        'is_normal': p_value >= alpha,
        'conclusion': "A amostra segue uma distribuição normal." if p_value >= alpha 
                     else "A amostra NÃO segue uma distribuição normal."
    }
    
    return result

```



