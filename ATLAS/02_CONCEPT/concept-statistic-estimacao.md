---
tags:
  - learning
HUB:
  - "[[hub-python]]"
  - "[[hub-statistic]]"
  - "[[hub-probabilidade]]"
---


Estimação: é a forma de fazer suposições generalizadas sobre parâmetros  de uma população tendo como base as informações da amostra

- Parâmetros: são atributos numéricos de uma população, tal como [[media-aritmetica]] e [[concept-statistic-desvio-do-padrao]].
- Estimativa: é o valor obtido para determinado parâmetro a partir dos dados e uma amostra

#### [[concept-teorema-do-limite-central]]
<font color = 00bbfff>Desvio padrão e a média na população</font> $$\sigma_\bar{x} = \frac{\sigma}{\sqrt{n}}$$

### [[nivel-de-confianca-e-significancia]]
- <font color = 00bfff>nível de confiança</font> $(1 -\alpha)$
- <font color = 00bfff>Erro inferencial</font> : $e = z \frac{\sigma}{\sqrt{n}}$
	- <font color = 00bfff> Intervalo de confiança</font>
		- <font color = 00bfff> Desvio padrão populacional conhecido</font>   $$\mu = \bar{x} \pm z\frac{\sigma}{\sqrt{n}}$$
		- <font color = 00bfff> Desvio padrão populacional desconhecido</font>  $$\mu = \bar{x} \pm z\frac{s}{\sqrt{n}}$$

Obtendo intervalos de confiança

```python
from statsmodels.stats.weightstats import zconfint
zconfint(nota_media_dos_filmes_com_pelo_menos_10_votos)
```

```python
from statsmodels.stats.weightstats import DescrStatsW

descr_todos_com_10_votos = DescrStatsW(nota_media_dos_filmes_com_pelo_menos_10_votos)
descr_todos_com_10_votos.tconfint_mean()
```



### Valores de $z$ para os níveis de confiança mais utilizados

|Nível de<br>confiança|Valor da área sob<br>a curva normal| $z$ |
|:----------------:|:---------------------------------:|:---:|
|90%               |0,95                               |1,645|
|95%               |0,975                              |1,96 |
|99%               |0,995                              |2,575|   | 

