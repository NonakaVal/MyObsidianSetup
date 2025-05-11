---
tags:
  - learning
  - workflow
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---


🧿<font color = 00bfff> Removendo Valores Nulos</font>
- [[removendo-valores-nulos]]   | [[concept-pandas-dropna-isnull-fillna]] 
	- `info()` , 
	- `dados[dados.Valor.isnull()].shape[0]` 
	- `dados.dropna(subset = ['Valor'], inplace = True)`
	- `dados = dados.fillna({'Condominio':0, 'IPTU':0})`
-  [[cmp-pandas-fillna-nullvalues-wrangling]]
	- `s.fillna(method = 'ffill')`
	- `s.fillna(method = 'bfill')`
	- `s1 = s.fillna(method = 'ffill', limit = 1)`


```
tmdb.query("runtime>0").runtime.dropna().quantile(q=0.8)
```
