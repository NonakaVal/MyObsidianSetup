---
tags:
  - learning/review
HUB:
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
  - "[[hub-python]]"
---
- [[probabilidade|introducao-probabilidade-e-definicoes]]
- [[concept-statistic-distribuicao-normal]]  | [[concept-statistic-distribuicao-normal-(gaussiana)|-gaussiana]] | [[concept-distribuicao-normal|conceito]] |  [[tabela-e-variavel-padronizada]] | 
	- [[scipy.stats.norm]] : `probabilidade = norm.cdf(Z_superior) - norm.cdf(Z_inferior)`
		- `probabilidade = norm.cdf(Z)`

- [[probabilidade-comb-binom]] | [[scipy-comb]] | [[scipy-stats.binom]]
	- `combinacao = comb(60 , 6)`
		- `probabilidade = binom.pmf(k,n,p)`
			- ` binom.cdf(4,n,p)`

- [[scipy.stats.poisson]]  
	- `probabilidade = poisson.pmf( k , media  )` 






