---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-probabilidade]]"
  - "[[hub-ml-models]]"
---
[Scipy](https://docs.scipy.org/doc/scipy/index.html)
[[probabilidade-comb-binom]]
[[scipy-probability-methods]]
- - <font color = 00bfff> Distribuição Normal</font> : `from scipy.stats import norm`
	- [[scipy-norm.cdf-method]]  : `probabilidade = norm.cdf(a_limit) - norm.cdf(b_limit)`
	- [[scipy-norm.ppf-method]] : `z = norm.ppf(0.975)`
`norm.interval(confidence = 0.90, loc = media_amostral, scale = desvio_padrao / np.sqrt(n))`
- <font color = 00bfff> Distribuição Binominal</font>
	- [[scipy-comb]] : `from scipy.special import comb`
		-  `prob = (comb(n ,k) * (p**k) * (q**(n - k)))`
	- [[scipy-stats.binom]] : `from scipy.stats import binom`
		-  `print("{0:.2%}".format(binom.sf(2, n, p)))` , `binom.pmf(k, n, p)` 
- <font color = 00bfff> Distribuição Poisson</font> 
	- [[scipy.stats.poisson]] : `from scipy.stats import poisson`
		- `probabilidade = poisson.pmf( k , media  )`


